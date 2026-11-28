import json
import unittest
from datetime import date
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import daily
import build_examples

build_examples.main(Path(__file__).resolve().parents[2] / "docs")
ITEMS = json.loads((Path(daily.__file__).parent / "examples.json").read_text(encoding="utf-8"))


class T(unittest.TestCase):
    def test_examples_valid(self):
        self.assertGreater(len(ITEMS), 10)
        for x in ITEMS:
            self.assertTrue(x["ru"] and (x["ae"] or x["ge"]))

    def test_every_example_fits_telegram(self):
        for x in ITEMS:
            t = daily.format_example(x)
            self.assertLessEqual(len(t), daily.LIMIT)
            self.assertIn("Россия", t)
            self.assertIn(x["url"], t)

    def test_pick_rotates_by_date(self):
        a = daily.pick(ITEMS, date(2026, 11, 28))
        b = daily.pick(ITEMS, date(2026, 11, 29))
        self.assertNotEqual(a["url"], b["url"])
        self.assertEqual(a, daily.pick(ITEMS, date(2026, 11, 28)))

    def test_cut(self):
        self.assertEqual(daily.cut("a  b", 10), "a b")
        self.assertTrue(daily.cut("слово " * 100, 50).endswith("…"))

    def test_html_escaped(self):
        x = dict(ITEMS[0]); x["topic"] = "a<b>"
        self.assertIn("a&lt;b&gt;", daily.format_example(x))


if __name__ == "__main__":
    unittest.main()
