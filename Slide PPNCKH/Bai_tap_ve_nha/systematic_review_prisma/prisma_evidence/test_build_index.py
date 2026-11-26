"""Check coverage and path validation for the evidence index."""
from pathlib import Path
import tempfile
import unittest

from build_index import evidence_link, render_index


class EvidenceIndexTests(unittest.TestCase):
    def test_existing_and_missing_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "evidence file.txt").touch()
            self.assertIn("../evidence%20file.txt", evidence_link(root, "evidence file.txt"))
            self.assertIn("Thiếu tệp", evidence_link(root, "missing.txt"))
            with self.assertRaises(ValueError):
                evidence_link(root, "../outside.txt")

    def test_requires_all_sixteen_steps_in_order(self):
        steps = [{"task_id": f"restart-{i:02}", "title": str(i),
                  "status": "pending", "updated_at": "timestamp",
                  "artifacts": [], "acceptance": []} for i in range(1, 17)]
        progress = {"updated_at": "timestamp", "steps": steps}
        document = render_index(Path.cwd(), progress, {})
        self.assertEqual(16, document.count("\n## Bước "))
        self.assertEqual(16, document.count("Chưa có tệp minh chứng"))
        steps.reverse()
        with self.assertRaises(ValueError):
            render_index(Path.cwd(), progress, {})


if __name__ == "__main__":
    unittest.main()
