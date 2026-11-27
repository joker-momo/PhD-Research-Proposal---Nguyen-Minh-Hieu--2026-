"""Focused checks for ID partition validation and the locked restart fixture."""
import re
from pathlib import Path
import unittest

from reconcile import audit, audit_baseline, index, split


class TestReconciliation(unittest.TestCase):
    def test_duplicate_id_is_rejected_even_when_counts_could_match(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            index([{"id": "A"}, {"id": "A"}], "id", "fixture")

    def test_undocumented_category_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "bad decision"):
            split({"A": {"decision": "unknown"}}, "decision", {"INCLUDE", "EXCLUDE"})

    def test_restart_ledger_and_checklist(self):
        folder = Path(__file__).resolve().parent
        result = audit_baseline(folder.parents[1])
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

    def test_active_ledger_accounts_for_every_sought_report(self):
        project = Path(__file__).resolve().parents[2]
        result = audit(project)
        self.assertEqual(set(result["arithmetic_differences"].values()), {0})
        self.assertEqual(result["supplemental_retrieval"], {
            "original_missing": 93, "recovered": 92, "unretrieved": 1
        })
        self.assertEqual(result["report_ids_by_retrieval_decision"]["NOT_RETRIEVED"], ["R0116"])
        self.assertEqual(result["awaiting_classification_codes"], {
            "R0082": "E7", "R0113": "E3", "R0292": "E7"
        })
        counts = result["counts"]
        self.assertEqual(
            tuple(counts[key] for key in ("reports_assessed", "reports_excluded", "included_reports", "included_studies")),
            (136, 89, 44, 44)
        )
        decision_sets = [set(ids) for ids in result["report_ids_by_fulltext_decision"].values()]
        assessed = set(result["report_ids_by_retrieval_decision"]["RETRIEVED_PDF"])
        self.assertEqual(set.union(*decision_sets), assessed)
        self.assertEqual(sum(map(len, decision_sets)), len(assessed))
        self.assertEqual(sum(map(len, result["fulltext_exclusions_by_primary_reason"].values())), 89)
        included = set(result["report_ids_by_fulltext_decision"]["INCLUDE"])
        self.assertTrue({"R0001", "R0145", "R0223"} <= included)
        self.assertTrue({"R0113", "R0292"}.isdisjoint(included))
        self.assertEqual(included, {report for group in result["study_ids_to_report_ids"].values() for report in group})
        self.assertIn("R0081", result["fulltext_exclusions_by_primary_reason"]["E7"])
        self.assertIn("R0132", result["fulltext_exclusions_by_primary_reason"]["E3"])


if __name__ == "__main__":
    unittest.main()
