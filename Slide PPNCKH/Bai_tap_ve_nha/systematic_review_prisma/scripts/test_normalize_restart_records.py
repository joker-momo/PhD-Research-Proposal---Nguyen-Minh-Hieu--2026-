"""Verify normalization against the independently locked source inventory."""

import csv
import json
import unittest
from pathlib import Path

from normalize_restart_records import normalize

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "restart_2026_11_26/search_dataset_manifest.json"


class TestLockedNormalization(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST.read_text())

    def test_every_input_position_round_trips(self):
        rows = normalize(PROJECT, self.manifest)
        actual = {(row["source_file"], row["source_record_number"]): row for row in rows}
        self.assertEqual(len(actual), self.manifest["rows_before_normalization_and_dedup"])
        for item in self.manifest["canonical_raw_inputs"]:
            with (PROJECT / item["path"]).open(encoding="utf-8-sig", newline="") as handle:
                for number, source in enumerate(csv.DictReader(handle), start=1):
                    record = actual[(item["path"], number)]
                    self.assertEqual(record["source"], item["source"])
                    title = source.get("Document Title") or source.get("Title") or source["title"]
                    self.assertEqual(record["title"], title.strip())
                    if item["source"] == "ACM":
                        self.assertEqual(record["source_rank"], source["rank"])
                        self.assertEqual(record["search_variant"], source["query_variant"])
                        self.assertEqual(record["abstract"], "")
                        self.assertEqual(record["abstract_snippet"], source["abstract_snippet"].strip())

    def test_locked_checksum_mismatch_is_rejected(self):
        self.manifest["canonical_raw_inputs"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            normalize(PROJECT, self.manifest)


if __name__ == "__main__":
    unittest.main()
