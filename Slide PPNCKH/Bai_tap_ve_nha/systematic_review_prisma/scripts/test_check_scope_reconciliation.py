import copy
import tempfile
import json
import subprocess
import sys
import unittest
from pathlib import Path

from check_scope_reconciliation import check, line_bounds


class ScopeChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        folder = self.root / "screening_46/text"; folder.mkdir(parents=True)
        (folder / "X.txt").write_text("=== PDF PAGE 1 ===\nTwo UAVs jointly allocate inference resources.\n=== PDF PAGE 2 ===\nOther evidence.\n")
        base = dict(id="X", title="Title", authors=["Author"], year=2025, venue="Venue", doi="10.test/one", decision="INCLUDE", gates={k:{"status":"YES"} for k in ["multi_uav_evaluated","collaborative_inference","primary_full_report","evaluative_evidence","date_window","english"]})
        self.ledger = {"records":[{"report_id":"X","accepted_record":base}]}
        r = {k:base[k] for k in ["id","title","authors","year","venue","doi"]}
        r.update(prior_decision="INCLUDE", proposed_decision="INCLUDE", scope_gates={k:{"status":"YES","rationale":"Bounded note","evidence_ids":["X1"]} for k in ["multi_uav_evaluated","collaborative_inference"]},other_gates_preserved={k:"YES" for k in ["primary_full_report","evaluative_evidence","date_window","english"]},architecture={**{k:"Reported condition" for k in ["uav_roles","inference_execution_nodes","inference_workload","coordinated_decisions","evaluated_conditions"]},"evidence_ids":["X1"]},supporting_interpretation={"note":"Supporting","evidence_ids":["X1"]},contrary_interpretation={"note":"Limiting","evidence_ids":["X2"]},unresolved=[],human_question=None,evidence=[{"evidence_id":f"X{i}","file":"screening_46/text/X.txt","page":1,"line_range":[2,2],"quote":"Two UAVs jointly allocate inference resources."} for i in range(1,5)])
        self.data = {"records":[r],"consistency_checks":[{"principle":str(i),"applies_to_ids":["X"],"evidence_ids":["X1"],"assessment":"Evidence note"} for i in range(3)],"shortfall":[],"project_files_changed":0,"final_prose_written":False}
    def run_check(self): return check(self.data,self.ledger,self.root,["X"])
    def test_valid_and_idempotent(self):
        before=copy.deepcopy(self.data); result=self.run_check()
        self.assertEqual(result["errors"],[]); self.assertEqual(result["quote_matches"],4)
        self.assertEqual(before,self.data); self.assertEqual(result,self.run_check())
    def test_quote_outside_range(self):
        self.data["records"][0]["evidence"][0]["quote"]="Other evidence."
        self.assertTrue(any("quote not present" in x for x in self.run_check()["errors"]))
    def test_wrong_page(self):
        self.data["records"][0]["evidence"][0]["page"]=2
        self.assertTrue(any("page/line" in x for x in self.run_check()["errors"]))
    def test_forged_source(self):
        self.data["records"][0]["evidence"][0]["file"]="../../unrelated.txt"
        self.assertTrue(any("supplied source" in x for x in self.run_check()["errors"]))
    def test_changed_identity_and_preserved_gate(self):
        r=self.data["records"][0];r["doi"]="wrong";r["other_gates_preserved"]["english"]="NO"
        errors=self.run_check()["errors"]
        self.assertTrue(any("changed identity" in x for x in errors));self.assertTrue(any("changed preserved gate" in x for x in errors))
    def test_unknown_evidence_and_decision(self):
        r=self.data["records"][0];r["scope_gates"]["collaborative_inference"].update(status="UNCERTAIN",evidence_ids=["missing"])
        errors=self.run_check()["errors"]
        self.assertTrue(any("truth-table" in x for x in errors));self.assertTrue(any("references" in x for x in errors))
    def test_missing_human_question(self):
        r=self.data["records"][0];r["scope_gates"]["collaborative_inference"]["status"]="UNCERTAIN";r["proposed_decision"]="UNCERTAIN"
        self.assertTrue(any("uncertainty" in x for x in self.run_check()["errors"]))
    def test_duplicate_evidence(self):
        self.data["records"][0]["evidence"][1]["evidence_id"]="X1"
        self.assertTrue(any("duplicate evidence" in x for x in self.run_check()["errors"]))
    def test_duplicate_identity(self):
        self.data["records"].append(copy.deepcopy(self.data["records"][0]))
        self.assertTrue(any("duplicate normalized" in x for x in self.run_check()["errors"]))
    def test_empty_normalized_quote(self):
        self.data["records"][0]["evidence"][0]["quote"] = "---"
        self.assertTrue(any("quote not present" in x for x in self.run_check()["errors"]))
    def test_cross_page_range(self):
        self.data["records"][0]["evidence"][0]["line_range"] = [2, 4]
        self.assertTrue(any("crosses pages" in x for x in self.run_check()["errors"]))
    def test_missing_architecture(self):
        del self.data["records"][0]["architecture"]["uav_roles"]
        self.assertTrue(any("architecture" in x for x in self.run_check()["errors"]))
    def test_unknown_consistency_report(self):
        self.data["consistency_checks"][0]["applies_to_ids"] = ["unknown"]
        self.assertTrue(any("unknown report" in x for x in self.run_check()["errors"]))
    def test_cli_rejects_input_overwrite(self):
        source = self.root / "result.json"
        ledger = self.root / "ledger.json"
        source.write_text(json.dumps(self.data)); ledger.write_text(json.dumps(self.ledger))
        before = source.read_bytes()
        result = subprocess.run([sys.executable, str(Path(__file__).with_name("check_scope_reconciliation.py")),
            str(source), "--ledger", str(ledger), "--project-root", str(self.root),
            "--ids", "X", "--output", str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("overwrite", result.stdout)
        self.assertEqual(before, source.read_bytes())
    def test_invalid_line_ranges(self):
        for value in [None,[2,1],[True,2],"bad",[1,2,3]]:
            with self.subTest(value=value),self.assertRaises(ValueError):line_bounds(value)
        self.assertEqual(line_bounds("lines 2–3"),(2,3));self.assertEqual(line_bounds("2-3"),(2,3))


if __name__ == "__main__": unittest.main()
