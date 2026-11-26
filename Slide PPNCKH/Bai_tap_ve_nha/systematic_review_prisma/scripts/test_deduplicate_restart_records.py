"""Verify deduplication against the locked input and conflict cases."""

import csv
import unittest
from collections import Counter
from pathlib import Path

from deduplicate_restart_records import deduplicate

PROJECT = Path(__file__).resolve().parents[1]


class DeduplicationTest(unittest.TestCase):
    def test_locked_dataset_reconciles_and_preserves_year_conflicts(self):
        with (PROJECT / "restart_2026_11_26/records_normalized.csv").open() as handle:
            rows = list(csv.DictReader(handle))
        queue, mapping, unresolved, years = deduplicate(rows)
        self.assertEqual(len(rows), len(mapping))
        self.assertEqual(len(queue), 465)
        self.assertEqual(unresolved, [])
        self.assertEqual(len(years), 12)
        self.assertEqual(Counter(x["link_reason"] for x in mapping), {
            "representative": 465, "matching_doi_and_title": 216,
            "exact_title_year_acm_proceeding": 12,
        })
        self.assertEqual({x["record_id"] for x in rows}, {x["record_id"] for x in mapping})

    def test_distinct_dois_are_never_joined_on_title_alone(self):
        rows = [
            {"record_id": "a", "title": "Paper", "doi": "10.1000/a"},
            {"record_id": "b", "title": "Paper", "doi": "10.1000/b"},
        ]
        for row in rows:
            row.update(year="2025", abstract="", authors="", venue="", abstract_snippet="", url="")
        queue, mapping, unresolved, _ = deduplicate(rows)
        self.assertEqual(len(queue), 2)
        self.assertEqual(len(mapping), 2)
        self.assertEqual(unresolved[0]["reason"], "conflicting_doi_or_title")


if __name__ == "__main__":
    unittest.main()
