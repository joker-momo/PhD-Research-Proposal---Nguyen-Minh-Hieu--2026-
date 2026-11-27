import csv
import hashlib
import json
import re
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
CONTEXT_MANIFEST = PROJECT / "MUST_READ_AI_AGENT/context_manifest.yaml"
LOCATOR_MAPPING = PROJECT / "migration/historical_locator_mapping.tsv"
HISTORICAL_PATH = re.compile(
    r"/Users/joker/\.codex/worktrees/[^\n]*?/Slide PPNCKH/"
    r"Bai_tap_ve_nha/systematic_review_prisma/[^\s,)]+"
)


class MigrationIntegrityTests(unittest.TestCase):
    def test_historical_locator_mapping_covers_immutable_accepted_outputs(self):
        with LOCATOR_MAPPING.open(encoding="utf-8", newline="") as handle:
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
        project_marker = f"/{PROJECT.name}/"
        for row in rows:
            recorded_path = Path(row["canonical_path"])
            self.assertTrue(recorded_path.is_absolute(), recorded_path)
            _, separator, locator = recorded_path.as_posix().partition(project_marker)
            self.assertTrue(separator and locator, recorded_path)
            local_path = (PROJECT / locator).resolve()
            self.assertTrue(local_path.is_relative_to(PROJECT), local_path)
            # Legacy PDFs and raw corrections may exist only in the recorded archive.
            source = local_path if local_path.is_file() else recorded_path
            self.assertTrue(source.is_file(), source)
            self.assertEqual(
                hashlib.sha256(source.read_bytes()).hexdigest(),
                row["sha256"],
            )

    def test_context_manifest_registers_historical_locator_mapping(self):
        context = CONTEXT_MANIFEST.read_text(encoding="utf-8")
        matches = re.findall(r'(?m)^  historical_locator_mapping: "([^"]+)"$', context)
        self.assertEqual(len(matches), 1)
        locator = Path(matches[0])
        self.assertFalse(locator.is_absolute())
        self.assertEqual((CONTEXT_MANIFEST.parent / locator).resolve(), LOCATOR_MAPPING)
        self.assertTrue(LOCATOR_MAPPING.is_file())


if __name__ == "__main__":
    unittest.main()
