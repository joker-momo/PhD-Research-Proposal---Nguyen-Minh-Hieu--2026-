import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from screening_paths import resolve_screening_path, to_screening_locator


SCREENING_ROOT = SCRIPT_DIR.parent / "screening_46"


class ScreeningPathTests(unittest.TestCase):
    def test_relative_locator_resolves_from_screening_root(self):
        resolved = resolve_screening_path(SCREENING_ROOT, "text/S01.txt")

        self.assertEqual(resolved, (SCREENING_ROOT / "text/S01.txt").resolve())

    def test_absolute_locator_remains_backward_compatible(self):
        absolute = (SCREENING_ROOT / "text/S01.txt").resolve()

        self.assertEqual(resolve_screening_path(SCREENING_ROOT, str(absolute)), absolute)

    def test_locator_outside_screening_root_is_rejected_for_new_manifest(self):
        outside = SCREENING_ROOT.parent / "protocol.md"

        with self.assertRaises(ValueError):
            to_screening_locator(SCREENING_ROOT, outside)
        with self.assertRaises(ValueError):
            resolve_screening_path(SCREENING_ROOT, "../protocol.md")

    def test_manifest_resolves_after_project_copy(self):
        manifest = json.loads((SCREENING_ROOT / "manifest.json").read_text())

        self.assertEqual(len(manifest["records"]), 46)
        with tempfile.TemporaryDirectory() as temporary:
            relocated_root = Path(temporary) / "screening_46"
            relocated_root.mkdir()
            for record in manifest["records"]:
                provenance = record["source_provenance"]
                self.assertFalse(Path(provenance).is_absolute(), (record["id"], provenance))
                self.assertTrue(provenance.startswith("legacy-root:"), (record["id"], provenance))
                for field in ("source", "pdf", "text"):
                    locator = record[field]
                    self.assertFalse(Path(locator).is_absolute(), (record["id"], field, locator))
                    resolved = resolve_screening_path(relocated_root, locator)
                    self.assertTrue(resolved.is_relative_to(relocated_root.resolve()))


if __name__ == "__main__":
    unittest.main()
