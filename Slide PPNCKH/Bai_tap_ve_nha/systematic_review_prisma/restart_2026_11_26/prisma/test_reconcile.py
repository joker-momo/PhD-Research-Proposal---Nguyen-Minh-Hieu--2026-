"""Focused checks for ID partition validation and the locked restart fixture."""
import re
from pathlib import Path
import unittest

from reconcile import audit, index, split


class TestReconciliation(unittest.TestCase):
    def test_duplicate_id_is_rejected_even_when_counts_could_match(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            index([{"id": "A"}, {"id": "A"}], "id", "fixture")

    def test_undocumented_category_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "bad decision"):
            split({"A": {"decision": "unknown"}}, "decision", {"INCLUDE", "EXCLUDE"})

    def test_restart_ledger_and_checklist(self):
        folder = Path(__file__).resolve().parent
        result = audit(folder.parents[1])
        self.assertEqual(set(result["arithmetic_differences"].values()), {0})
        self.assertEqual(result["counts"]["included_reports"], 25)
        self.assertEqual(result["counts"]["included_studies"], 25)
        self.assertEqual(result["retrieval_counts_by_title_decision"]["UNCLEAR"], {
            "NOT_RETRIEVED": 79, "RETRIEVED_PDF": 14
        })
        self.assertEqual(result["counts"]["reports_awaiting_classification"], 6)
        lines = (folder / "prisma_checklist.md").read_text().splitlines()
        items = [line.split("|")[1:-1] for line in lines if re.match(r"^\| [0-9]+ \|", line)]
        self.assertEqual([int(cols[0]) for cols in items], list(range(1, 28)))
        for cols in items:
            self.assertEqual(len(cols), 5)
            self.assertTrue(all(value.strip() for value in cols))
            for target in re.findall(r"\]\((?!https?://)([^)#]+)", cols[3]):
                self.assertTrue((folder / target).is_file(), target)


if __name__ == "__main__":
    unittest.main()
