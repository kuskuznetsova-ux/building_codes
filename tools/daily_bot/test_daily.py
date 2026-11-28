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
EN = json.loads(daily.ENGLISH.read_text(encoding="utf-8"))


class T(unittest.TestCase):
    def test_examples_valid(self):
        self.assertGreater(len(ITEMS), 10)
        for x in ITEMS:
            self.assertTrue(x["ru"] and (x["ae"] or x["ge"]))

    def test_every_example_fits_telegram(self):
        for x in ITEMS:
            t = daily.format_example(x, EN)
            self.assertLessEqual(len(t), daily.LIMIT)
            self.assertIn("Россия", t)
            self.assertIn(x["url"], t)

    def test_pick_rotates_by_date(self):
        a = daily.pick(ITEMS, date(2026, 12, 1))
        b = daily.pick(ITEMS, date(2026, 12, 2))
        self.assertNotEqual(a["url"], b["url"])
        self.assertEqual(a, daily.pick(ITEMS, date(2026, 12, 1)))

    def test_fire_first_then_highrise(self):
        order = [daily.rank(daily.pick(ITEMS, index=i)) for i in range(len(ITEMS))]
        self.assertEqual(order, sorted(order))
        self.assertEqual(order[0], 0)
        self.assertEqual(daily.pick(ITEMS, date(2026, 11, 1)), daily.pick(ITEMS, index=0))

    def test_english_present_for_fire_and_highrise(self):
        for x in ITEMS:
            if daily.rank(x) < 2:
                self.assertIn(x["id"], EN, x["id"])
                self.assertIn("EN:", daily.format_example(x, EN))

    def test_no_internal_notes(self):
        for x in ITEMS:
            self.assertNotIn("Техэксперт", daily.format_example(x, EN))

    def test_cut(self):
        self.assertEqual(daily.cut("a  b", 10), "a b")
        self.assertTrue(daily.cut("слово " * 100, 50).endswith("…"))

    def test_html_escaped(self):
        x = dict(ITEMS[0]); x["topic"] = "a<b>"
        self.assertIn("a&lt;b&gt;", daily.format_example(x))


if __name__ == "__main__":
    unittest.main()
