"""Validate translated product libraries against the English originals."""

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT / "community-examples"
LANGUAGES = (
    "japanese", "simplified-chinese", "german", "french",
    "korean", "spanish", "brazilian-portuguese",
)
TEXT_FIELDS = {
    "name", "title", "purpose", "benefits", "evidenceNotes", "evidenceNote",
    "notes", "note", "condition", "excerpt", "locator", "label", "section",
    "subsection", "description", "publisher",
}
NUMBER = re.compile(r"(?<![A-Za-z0-9_.])\d+(?:\.\d+)?")
# Dose units following a number (or U-100 style syringe labels) must survive translation verbatim.
UNIT = re.compile(r"(?<=\d)\s?(?:mcg|µg|μg|mg|kg|mL|ml|IU)\b|\bU-\d+\b")


def keep_english(path):
    """Source titles, publishers and citation locators stay in their original language."""
    field = next((part for part in reversed(path) if isinstance(part, str)), "")
    return (path[:1] == ("sources",) and field in {"title", "publisher"}) or (
        path[:1] == ("citations",) and field == "locator"
    )


def compare(original, translated, path=()):
    """Allow text changes only while retaining keys, ordering, data and prose numbers."""
    location = ".".join(map(str, path)) or "<root>"
    if type(original) is not type(translated):
        raise ValueError(f"{location}: value type changed")
    if isinstance(original, dict):
        if original.keys() != translated.keys():
            raise ValueError(f"{location}: JSON keys changed")
        for key in original:
            compare(original[key], translated[key], (*path, key))
    elif isinstance(original, list):
        if len(original) != len(translated):
            raise ValueError(f"{location}: array length changed")
        for index, (left, right) in enumerate(zip(original, translated)):
            compare(left, right, (*path, index))
    elif original != translated:
        field = next((part for part in reversed(path) if isinstance(part, str)), "")
        prose = not keep_english(path) and (
            field in TEXT_FIELDS
            or (field == "population" and "regimen" in path)
            or ("rows" in path and isinstance(original, str))
            or ("aliases" in path and isinstance(original, str))
        )
        if not isinstance(original, str) or not prose:
            raise ValueError(f"{location}: structured value changed")
        if sorted(NUMBER.findall(original)) != sorted(NUMBER.findall(translated)):
            raise ValueError(f"{location}: numbers in text changed")
        if sorted(u.strip() for u in UNIT.findall(original)) != sorted(
            u.strip() for u in UNIT.findall(translated)
        ):
            raise ValueError(f"{location}: dose units in text changed")


def is_prose_path(path):
    """True when a string at this JSON path is translatable prose."""
    field = next((part for part in reversed(path) if isinstance(part, str)), "")
    return not keep_english(path) and (
        field in TEXT_FIELDS
        or (field == "population" and "regimen" in path)
        or "rows" in path
        or "aliases" in path
    )


def untranslated(original, translated, path=()):
    """Yield paths of prose strings (4+ words) that are still identical to the English source."""
    if isinstance(original, dict):
        for key in original:
            yield from untranslated(original[key], translated[key], (*path, key))
    elif isinstance(original, list):
        for index, (left, right) in enumerate(zip(original, translated)):
            yield from untranslated(left, right, (*path, index))
    elif isinstance(original, str) and original == translated and len(original.split()) >= 4:
        if is_prose_path(path) and "aliases" not in path:  # aliases are often names, kept as is
            yield ".".join(map(str, path))


def main(argv):
    """Usage: validate_translations.py [<language> <file.json> ...]

    With arguments, each named translation must exist and pass; a missing file is an error.
    Without arguments, every translation found is checked, and finding none is an error.
    """
    if argv:
        language, *names = argv
        if language not in LANGUAGES or not names:
            raise ValueError(f"usage: validate_translations.py <{'|'.join(LANGUAGES)}> <file.json>...")
        targets = []
        for name in names:
            file = EXAMPLES / language / Path(name).name
            if not file.is_file():
                raise ValueError(f"{file}: translation not found; it was not saved at this path")
            targets.append(file)
    else:
        targets = [f for language in LANGUAGES for f in sorted((EXAMPLES / language).glob("*.json"))]
        if not targets:
            raise ValueError("no translated files found under community-examples/<language>/")
    schema = json.loads((ROOT / "template/library.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    count = 0
    for file in targets:
        original = EXAMPLES / "english" / file.name
        if not original.is_file():
            raise ValueError(f"{file}: no English original")
        source = json.loads(original.read_text())
        translation = json.loads(file.read_text())
        validator.validate(source)
        validator.validate(translation)
        compare(source, translation)
        left_in_english = list(untranslated(source, translation))
        if left_in_english:
            shown = ", ".join(left_in_english[:10])
            raise ValueError(
                f"{file}: {len(left_in_english)} prose strings are still in English "
                f"(translate them): {shown}"
            )
        count += 1
    expected = len(list((EXAMPLES / "english").glob("*.json"))) * len(LANGUAGES)
    print(f"Validated {count} translated product files against their English originals.")
    print(f"{expected - count} translations have not been added.")


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
