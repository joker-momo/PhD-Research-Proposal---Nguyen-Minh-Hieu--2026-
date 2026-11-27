"""Focused checks for ID partition validation and the locked restart fixture."""
import json
import re
from pathlib import Path
import unittest
from unittest.mock import patch

from reconcile import audit, audit_baseline, audit_supplemental_intake, index, split, supplemental_study_groups


class TestReconciliation(unittest.TestCase):
    def test_duplicate_id_is_rejected_even_when_counts_could_match(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            index([{"id": "A"}, {"id": "A"}], "id", "fixture")

    def test_undocumented_category_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "bad decision"):
            split({"A": {"decision": "unknown"}}, "decision", {"INCLUDE", "EXCLUDE"})

    def test_supplemental_reconciles_current_checkout_without_changing_baseline(self):
        project = Path(__file__).resolve().parents[2]
        result = audit_supplemental_intake(project)
        self.assertEqual(len(result["intake_ids"]), 92)
        self.assertEqual(result["not_retrieved_ids"], ["R0116"])
        self.assertEqual(len(result["prior_awaiting_ids"]), 6)
        self.assertEqual(set(result["assessed_by_source"]["round_01"]), {"R0070"})
        covered = [set(result["pending_screening_ids"]), *(set(ids) for ids in result["assessed_by_source"].values())]
        self.assertEqual(set.union(*covered), set(result["intake_ids"]))
        self.assertEqual(sum(map(len, covered)), 92)
        self.assertIsNone(result["study_ids_to_report_ids"])

    def test_supplemental_rejects_duplicate_records_before_counting_batch(self):
        project = Path(__file__).resolve().parents[2]
        read_text = Path.read_text

        def duplicate_first_record(path, *args, **kwargs):
            raw = read_text(path, *args, **kwargs)
            if path.name == "batch_01_accepted.json":
                records = json.loads(raw)
                return json.dumps(records + records[:1])
            return raw

        with patch.object(Path, "read_text", duplicate_first_record):
            with self.assertRaisesRegex(ValueError, "batch_01_accepted.json:.*duplicate"):
                audit_supplemental_intake(project)

    def test_linkage_counts_reports_independently_from_studies(self):
        rows = [{"report_id": "R0001", "study_id": "S1"},
                {"report_id": "R0002", "study_id": "S1"}]
        self.assertEqual(supplemental_study_groups(rows, {"R0001", "R0002"}),
                         {"S1": ["R0001", "R0002"]})
        with self.assertRaisesRegex(ValueError, "mapping"):
            supplemental_study_groups(rows, {"R0001"})
        with self.assertRaisesRegex(ValueError, "duplicate"):
            supplemental_study_groups(rows + rows[:1], {"R0001", "R0002"})

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
        self.assertEqual(result["awaiting_classification_codes"], {})
        counts = result["counts"]
        self.assertEqual(
            tuple(counts[key] for key in ("reports_assessed", "reports_excluded", "included_reports", "included_studies")),
            (136, 90, 46, 46)
        )
        decision_sets = [set(ids) for ids in result["report_ids_by_fulltext_decision"].values()]
        assessed = set(result["report_ids_by_retrieval_decision"]["RETRIEVED_PDF"])
        self.assertEqual(set.union(*decision_sets), assessed)
        self.assertEqual(sum(map(len, decision_sets)), len(assessed))
        self.assertEqual(sum(map(len, result["fulltext_exclusions_by_primary_reason"].values())), 90)
        included = set(result["report_ids_by_fulltext_decision"]["INCLUDE"])
        self.assertTrue({"R0001", "R0082", "R0145", "R0223", "R0292"} <= included)
        self.assertNotIn("R0113", included)
        self.assertEqual(result["study_ids_to_report_ids"]["S047"], ["R0082"])
        self.assertEqual(result["study_ids_to_report_ids"]["S046"], ["R0292"])
        self.assertEqual(included, {report for group in result["study_ids_to_report_ids"].values() for report in group})
        self.assertIn("R0081", result["fulltext_exclusions_by_primary_reason"]["E7"])
        self.assertIn("R0113", result["fulltext_exclusions_by_primary_reason"]["E3"])
        self.assertIn("R0132", result["fulltext_exclusions_by_primary_reason"]["E3"])


if __name__ == "__main__":
    unittest.main()
