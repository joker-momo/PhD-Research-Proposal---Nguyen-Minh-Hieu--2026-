"""Regression tests for the S2 evidence and agreement summary."""

import csv
import io
import json
import subprocess
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from audit_adjudication import HERE, PRISMA, PROJECT, build_report, load_rows, main, paired_agreement, render_latex
from build_editorial_evidence import review_log


class TestAdjudicationAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (HERE / "human_adjudication_log.csv").read_text()
        cls.baseline = review_log()
        cls.ledger = json.loads((PRISMA / "prisma_counts.json").read_text())
        cls.ids = set(cls.ledger["report_ids_by_retrieval_decision"]["RETRIEVED_PDF"])
        state = json.loads((PROJECT / "MUST_READ_AI_AGENT/current_state.json").read_text())
        cls.deferrals = state["evidence"]["alternative_technical_survey"]["editorial_integration"][
            "author_confirmed_deferrals"]

    def test_real_s2_does_not_count_blanks_as_changes(self):
        rows = load_rows(self.source, self.baseline, self.ids)
        report = build_report(rows, self.ledger, self.deferrals)
        self.assertEqual(report["s2"]["reports_in_log"], 136)
        self.assertEqual(report["s2"]["author_processed_reports"], 10)
        self.assertEqual(report["s2"]["reports_without_author_confirmation"], 126)
        self.assertEqual(report["s2"]["author_confirmed_deferrals"], {})
        comparison = report["ai_to_final_human_decisions"]
        self.assertEqual((comparison["changed_reports"], comparison["compared_reports"]), (4, 10))
        self.assertEqual(comparison["changed_among_author_processed"], {"changed": 4, "total": 10})
        self.assertEqual(comparison["transitions"],
                         {"AWAITING_CLASSIFICATION -> EXCLUDE": ["R0081", "R0132"],
                          "INCLUDE -> EXCLUDE": ["R0113"],
                          "AWAITING_CLASSIFICATION -> INCLUDE": ["R0082"]})
        self.assertEqual(report["paired_human_agreement"]["paired_reports"], 0)
        self.assertIsNone(report["paired_human_agreement"]["cohens_kappa"])
        table = render_latex(report)
        self.assertIn("Reports without author confirmation & 126", table)
        self.assertIn("Changes among author-processed reports & 4 / 10", table)
        self.assertIn("Changes among final human decisions & 4 / 10", table)
        self.assertIn("46 / 90 / 0", table)
        self.assertIn("PRISMA awaiting classification & None", table)

    def test_csv_rejects_duplicate_foreign_id_and_invalid_reason(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load(self.source + self.source.splitlines()[1] + "\n")
        with self.assertRaisesRegex(ValueError, "unexpected ID"):
            self.load(self.source.replace("R0001,", "R9999,", 1))
        reader = csv.DictReader(io.StringIO(self.source))
        out = io.StringIO()
        writer = csv.DictWriter(out, reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row["Record_ID"] == "R0081":
                row["Primary_Reason_Code"] = "E9"
            writer.writerow(row)
        with self.assertRaisesRegex(ValueError, "exclusion reason"):
            self.load(out.getvalue())

    def test_undefined_and_calculable_kappa(self):
        self.assertIsNone(paired_agreement([])["percent_agreement"])
        unanimous = paired_agreement([("INCLUDE", "INCLUDE")] * 3)
        self.assertEqual(unanimous["percent_agreement"], 100)
        self.assertIsNone(unanimous["cohens_kappa"])
        mixed = paired_agreement([("INCLUDE", "INCLUDE"), ("EXCLUDE", "EXCLUDE"),
                                  ("INCLUDE", "EXCLUDE"), ("EXCLUDE", "EXCLUDE")])
        self.assertEqual(mixed["percent_agreement"], 75)
        self.assertEqual(mixed["cohens_kappa"], 0.5)

    def test_failed_prisma_gate_leaves_outputs_unwritten(self):
        with TemporaryDirectory() as folder:
            mock_failure = subprocess.CalledProcessError(1, "reconcile.py --check")
            with (patch("audit_adjudication.HERE", Path(folder)),
                  patch("audit_adjudication.subprocess.run", side_effect=mock_failure),
                  patch("sys.argv", ["audit_adjudication.py"]),
                  redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised):
                main()
            self.assertEqual(raised.exception.code, 1)
            self.assertEqual(list(Path(folder).iterdir()), [])

    def load(self, source):
        return load_rows(source, self.baseline, self.ids)


if __name__ == "__main__":
    unittest.main()
