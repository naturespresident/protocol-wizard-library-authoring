import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import translation_chunks
import validate_translations

REAL_ENGLISH = validate_translations.EXAMPLES / "english" / "adamax.json"
LANGUAGE = "spanish"
NAME = "adamax.json"


class ChunkToolTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        (self.tmp / "english").mkdir()
        (self.tmp / LANGUAGE).mkdir()
        shutil.copy(REAL_ENGLISH, self.tmp / "english" / NAME)
        self.work = self.tmp / "work"
        for module in (translation_chunks, validate_translations):
            patcher = mock.patch.object(module, "EXAMPLES", self.tmp)
            patcher.start()
            self.addCleanup(patcher.stop)
        patcher = mock.patch.object(translation_chunks, "WORK", self.work)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.chunk_dir = self.work / LANGUAGE / "adamax"
        self.args = [LANGUAGE, NAME]

    def run_quiet(self, function, *args):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            function(*args)
        return out.getvalue()

    def chunk_files(self):
        return sorted(self.chunk_dir.glob("chunk-[0-9][0-9][0-9].json"))

    def translate_all(self, transform=lambda text: f"[{LANGUAGE}] {text}"):
        for chunk in self.chunk_files():
            data = json.loads(chunk.read_text())
            translated = {key: transform(text) for key, text in data.items()}
            chunk.with_name(chunk.stem + ".translated.json").write_text(
                json.dumps(translated, ensure_ascii=False)
            )

    def test_extract_covers_every_prose_string_within_limits(self):
        self.run_quiet(translation_chunks.extract, self.args)
        expected = list(translation_chunks.strings(json.loads(REAL_ENGLISH.read_text())))
        found = {}
        for chunk in self.chunk_files():
            data = json.loads(chunk.read_text())
            self.assertLessEqual(len(data), translation_chunks.MAX_STRINGS)
            found.update(data)
        self.assertEqual(len(found), len(expected))
        self.assertEqual(
            set(found), {json.dumps(list(path)) for path, _ in expected}
        )

    def test_extract_keeps_progress_unless_forced(self):
        self.run_quiet(translation_chunks.extract, self.args)
        self.translate_all()
        done = list(self.chunk_dir.glob("*.translated.json"))
        self.assertTrue(done)
        output = self.run_quiet(translation_chunks.extract, self.args)
        self.assertIn("keeping your translated work", output)
        self.assertEqual(len(list(self.chunk_dir.glob("*.translated.json"))), len(done))
        self.run_quiet(translation_chunks.extract, [*self.args, "--force"])
        self.assertEqual(list(self.chunk_dir.glob("*.translated.json")), [])

    def test_source_titles_publishers_and_locators_stay_english(self):
        self.run_quiet(translation_chunks.extract, self.args)
        english = json.loads(REAL_ENGLISH.read_text())
        offered = {text for chunk in self.chunk_files() for text in json.loads(chunk.read_text()).values()}
        for source in english["sources"]:
            self.assertNotIn(source["title"], offered)
            if source.get("publisher"):
                self.assertNotIn(source["publisher"], offered)
        for citation in english["citations"]:
            if citation.get("locator"):
                self.assertNotIn(citation["locator"], offered)
        self.translate_all()
        self.run_quiet(translation_chunks.apply, self.args)
        translated = json.loads((self.tmp / LANGUAGE / NAME).read_text())
        self.assertEqual(translated["sources"][0]["title"], english["sources"][0]["title"])
        translated["sources"][0]["title"] += " (traducido)"
        (self.tmp / LANGUAGE / NAME).write_text(json.dumps(translated, ensure_ascii=False))
        with self.assertRaisesRegex(ValueError, "structured value changed"):
            validate_translations.main(self.args)

    def test_status_reports_remaining_then_done(self):
        self.run_quiet(translation_chunks.extract, self.args)
        output = self.run_quiet(translation_chunks.status, self.args)
        self.assertIn("NOT DONE", output)
        self.translate_all()
        output = self.run_quiet(translation_chunks.status, self.args)
        self.assertIn("All", output)
        self.assertNotIn("NOT DONE", output)

    def test_status_without_extract_is_an_error(self):
        with self.assertRaises(ValueError):
            translation_chunks.status(self.args)

    def test_apply_requires_every_chunk_and_matching_keys(self):
        self.run_quiet(translation_chunks.extract, self.args)
        with self.assertRaisesRegex(ValueError, "missing"):
            translation_chunks.apply(self.args)
        self.translate_all()
        first = self.chunk_files()[0]
        translated = first.with_name(first.stem + ".translated.json")
        data = json.loads(translated.read_text())
        data.pop(next(iter(data)))
        translated.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "keys differ"):
            translation_chunks.apply(self.args)

    def test_apply_rejects_empty_translation(self):
        self.run_quiet(translation_chunks.extract, self.args)
        self.translate_all()
        first = self.chunk_files()[0]
        translated = first.with_name(first.stem + ".translated.json")
        data = json.loads(translated.read_text())
        data[next(iter(data))] = "  "
        translated.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "non-empty"):
            translation_chunks.apply(self.args)

    def test_identity_round_trip_rebuilds_the_original_bytes(self):
        self.run_quiet(translation_chunks.extract, self.args)
        self.translate_all(transform=lambda text: text)
        self.run_quiet(translation_chunks.apply, self.args)
        self.assertEqual(
            (self.tmp / LANGUAGE / NAME).read_bytes(), REAL_ENGLISH.read_bytes()
        )

    def test_translated_file_passes_the_validator(self):
        self.run_quiet(translation_chunks.extract, self.args)
        self.translate_all()
        self.run_quiet(translation_chunks.apply, self.args)
        output = self.run_quiet(validate_translations.main, self.args)
        self.assertIn("Validated 1 translated product files", output)

    def test_validator_rejects_untranslated_copy(self):
        shutil.copy(REAL_ENGLISH, self.tmp / LANGUAGE / NAME)
        with self.assertRaisesRegex(ValueError, "still in English"):
            validate_translations.main(self.args)


class ValidatorCommandLineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        (self.tmp / "english").mkdir()
        shutil.copy(REAL_ENGLISH, self.tmp / "english" / NAME)
        patcher = mock.patch.object(validate_translations, "EXAMPLES", self.tmp)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_named_file_that_was_not_saved_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "translation not found"):
            validate_translations.main([LANGUAGE, NAME])

    def test_no_translations_at_all_is_an_error(self):
        with self.assertRaisesRegex(ValueError, "no translated files found"):
            validate_translations.main([])

    def test_unknown_language_or_missing_file_name_is_a_usage_error(self):
        with self.assertRaisesRegex(ValueError, "usage"):
            validate_translations.main(["klingon", NAME])
        with self.assertRaisesRegex(ValueError, "usage"):
            validate_translations.main([LANGUAGE])


if __name__ == "__main__":
    unittest.main()
