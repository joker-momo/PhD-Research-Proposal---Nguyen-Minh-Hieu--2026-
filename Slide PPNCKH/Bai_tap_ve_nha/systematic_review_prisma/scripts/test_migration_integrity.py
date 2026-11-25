import csv
import hashlib
import json
import re
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
HISTORICAL_PATH = re.compile(
    r"/Users/joker/\.codex/worktrees/[^\n]*?/Slide PPNCKH/"
    r"Bai_tap_ve_nha/systematic_review_prisma/[^\s,)]+"
)


class MigrationIntegrityTests(unittest.TestCase):
    def test_historical_locator_mapping_covers_immutable_accepted_outputs(self):
        mapping_path = PROJECT / "migration/historical_locator_mapping.tsv"
        with mapping_path.open() as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        observed = []
        for artifact in (
            "screening_46/results/batch_01_accepted.json",
            "screening_46/results/batch_02_accepted.json",
            "screening_46/results/batch_03_accepted.json",
        ):
            data = json.loads((PROJECT / artifact).read_text())

            def walk(value, locator="$"):
                if isinstance(value, dict):
                    for key, item in value.items():
                        walk(item, f"{locator}.{key}")
                elif isinstance(value, list):
                    for index, item in enumerate(value):
                        walk(item, f"{locator}[{index}]")
                elif isinstance(value, str):
                    for match in HISTORICAL_PATH.finditer(value):
                        observed.append((artifact, locator, match.group(0)))

            walk(data)

        mapped = [
            (row["artifact"], row["json_locator"], row["historical_path"])
            for row in rows
        ]
        self.assertEqual(len(observed), 8)
        self.assertEqual(mapped, observed)
        for row in rows:
            canonical = Path(row["canonical_path"])
            self.assertTrue(canonical.is_file(), canonical)
            self.assertEqual(
                hashlib.sha256(canonical.read_bytes()).hexdigest(),
                row["sha256"],
            )

    def test_context_manifest_registers_historical_locator_mapping(self):
        context = (PROJECT / "MUST_READ_AI_AGENT/context_manifest.yaml").read_text()
        self.assertIn(
            'historical_locator_mapping: "../migration/historical_locator_mapping.tsv"',
            context,
        )


if __name__ == "__main__":
    unittest.main()
