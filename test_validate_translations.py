import copy
import unittest

from validate_translations import compare, untranslated


class CompareTests(unittest.TestCase):
    def setUp(self):
        self.original = {
            "items": [{"id": "example", "name": "Example"}],
            "protocols": [{
                "population": "human",
                "regimen": {
                    "phases": [{"name": "Week 2", "dose": {"value": "0.25", "unit": "mg"}}]
                },
            }],
        }

    def test_translated_text_with_unchanged_numbers_is_allowed(self):
        translated = copy.deepcopy(self.original)
        translated["items"][0]["name"] = "Ejemplo"
        translated["protocols"][0]["regimen"]["phases"][0]["name"] = "Semana 2"
        compare(self.original, translated)

    def test_structured_dose_and_choice_cannot_change(self):
        for path, value in (("value", "0.5"), ("unit", "mcg")):
            with self.subTest(path=path):
                translated = copy.deepcopy(self.original)
                translated["protocols"][0]["regimen"]["phases"][0]["dose"][path] = value
                with self.assertRaises(ValueError):
                    compare(self.original, translated)
        translated = copy.deepcopy(self.original)
        translated["protocols"][0]["population"] = "humano"
        with self.assertRaises(ValueError):
            compare(self.original, translated)

    def test_changed_keys_and_numbers_in_text_are_rejected(self):
        translated = copy.deepcopy(self.original)
        translated["items"][0]["nombre"] = translated["items"][0].pop("name")
        with self.assertRaises(ValueError):
            compare(self.original, translated)
        translated = copy.deepcopy(self.original)
        translated["protocols"][0]["regimen"]["phases"][0]["name"] = "Semana 3"
        with self.assertRaises(ValueError):
            compare(self.original, translated)

    def test_dose_units_and_decimal_points_in_text_are_preserved(self):
        original = {"notes": "Inject 0.25 mg from a U-100 syringe."}
        compare(original, {"notes": "Injizieren Sie 0.25 mg mit einer U-100-Spritze."})
        for bad in (
            "Injizieren Sie 0.25 mcg mit einer U-100-Spritze.",
            "Injizieren Sie 0,25 mg mit einer U-100-Spritze.",
            "Injizieren Sie 0.25 mg mit einer U-40-Spritze.",
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                compare(original, {"notes": bad})

    def test_prose_left_in_english_is_reported(self):
        original = {"items": [{"name": "BPC-157", "benefits": "Supports tissue repair in studies."}]}
        done = {"items": [{"name": "BPC-157", "benefits": "Apoia o reparo tecidual em estudos."}]}
        self.assertEqual(list(untranslated(original, done)), [])
        self.assertEqual(list(untranslated(original, original)), ["items.0.benefits"])


if __name__ == "__main__":
    unittest.main()
