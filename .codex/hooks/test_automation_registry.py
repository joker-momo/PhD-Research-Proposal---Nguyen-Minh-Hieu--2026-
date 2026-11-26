"""Behavior tests for the append-only automation evidence registry."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import automation_registry


NOW = datetime(2026, 11, 26, 1, 0, tzinfo=timezone.utc)


class AutomationRegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="automation-registry-")
        self.root = Path(self.temp.name)
        self.script = self.root / ".codex/hooks/example.py"
        self.test_script = self.root / ".codex/hooks/test_example.py"
        self.script.parent.mkdir(parents=True)
        self.script.write_text("print('example')\n")
        self.test_script.write_text("# test fixture\n")
        self.catalog_path = self.root / "automation/artifact_catalog.json"
        self.decisions_path = self.root / "automation/decision_log.jsonl"
        self.catalog_path.parent.mkdir(parents=True)
        self.catalog = {
            "schema_version": 1,
            "artifacts": [
                {
                    "artifact_id": "example-tool",
                    "name": "Example tool",
                    "path": ".codex/hooks/example.py",
                    "purpose": "Validate DOI metadata in deterministic batches.",
                    "entrypoint": "python3 .codex/hooks/example.py",
                    "inputs": ["JSON records on stdin"],
                    "outputs": ["Validated JSON on stdout"],
                    "tests": [".codex/hooks/test_example.py"],
                    "test_command": "python3 .codex/hooks/test_example.py",
                    "status": "active",
                    "tags": ["doi", "validation"],
                }
            ],
        }
        self.decision = {
            "decision_id": "task-1-v1",
            "task_id": "task-1",
            "decided_at": "2026-11-26T07:30:00+07:00",
            "recorded_at": "2026-11-26T07:31:00+07:00",
            "mode": "WRITE_SCRIPT",
            "reason": "Repeated DOI validation is deterministic and reusable.",
            "artifact_ids": ["example-tool"],
            "verification": ["1/1 focused test PASS"],
        }
        self.write_registry()
        self.addCleanup(self.temp.cleanup)

    def write_registry(self, decisions=None):
        self.catalog_path.write_text(json.dumps(self.catalog) + "\n")
        rows = decisions if decisions is not None else [self.decision]
        self.decisions_path.write_text(
            "".join(json.dumps(row) + "\n" for row in rows)
        )

    def validate(self):
        return automation_registry.validate_registry(
            self.catalog_path, self.decisions_path, self.root, now=NOW
        )

    def test_valid_registry_returns_counts_and_active_decision(self):
        registry = self.validate()

        self.assertEqual(1, len(registry["artifacts"]))
        self.assertEqual(1, len(registry["decisions"]))
        self.assertEqual("task-1-v1", registry["active_by_task"]["task-1"]["decision_id"])

    def test_duplicate_artifact_id_is_rejected(self):
        self.catalog["artifacts"].append(dict(self.catalog["artifacts"][0]))
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "duplicate artifact_id"):
            self.validate()

    def test_artifact_path_escape_is_rejected(self):
        self.catalog["artifacts"][0]["path"] = "../outside.py"
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "repository-relative"):
            self.validate()

    def test_missing_artifact_file_is_rejected(self):
        self.catalog["artifacts"][0]["path"] = ".codex/hooks/missing.py"
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "artifact path does not exist"):
            self.validate()

    def test_missing_test_file_is_rejected(self):
        self.catalog["artifacts"][0]["tests"] = [".codex/hooks/missing_test.py"]
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "test path does not exist"):
            self.validate()

    def test_unknown_artifact_reference_is_rejected(self):
        self.decision["artifact_ids"] = ["unknown-tool"]
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "unknown artifact_id"):
            self.validate()

    def test_write_script_requires_an_artifact(self):
        self.decision["artifact_ids"] = []
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "requires at least one artifact"):
            self.validate()

    def test_reuse_existing_requires_verification(self):
        self.decision["mode"] = "REUSE_EXISTING"
        self.decision["verification"] = []
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "verification"):
            self.validate()

    def test_manual_decision_can_have_no_artifact_but_requires_verification(self):
        self.decision["mode"] = "MANUAL"
        self.decision["artifact_ids"] = []
        self.decision["verification"] = ["Human judgment recorded in review.md"]
        self.write_registry()

        registry = self.validate()

        self.assertEqual("MANUAL", registry["active_by_task"]["task-1"]["mode"])

    def test_duplicate_decision_id_is_rejected(self):
        self.write_registry([self.decision, dict(self.decision)])

        with self.assertRaisesRegex(ValueError, "duplicate decision_id"):
            self.validate()

    def test_two_active_decisions_for_one_task_are_rejected(self):
        second = dict(self.decision, decision_id="task-1-v2")
        self.write_registry([self.decision, second])

        with self.assertRaisesRegex(ValueError, "multiple active decisions"):
            self.validate()

    def test_superseding_decision_preserves_history_and_becomes_active(self):
        second = dict(
            self.decision,
            decision_id="task-1-v2",
            supersedes_decision_id="task-1-v1",
            decided_at="2026-11-26T07:32:00+07:00",
            recorded_at="2026-11-26T07:33:00+07:00",
            mode="REUSE_EXISTING",
            reason="A verified existing tool was found before implementation.",
        )
        self.write_registry([self.decision, second])

        registry = self.validate()

        self.assertEqual(2, len(registry["decisions"]))
        self.assertEqual("task-1-v2", registry["active_by_task"]["task-1"]["decision_id"])

    def test_supersedes_must_reference_earlier_same_task(self):
        second = dict(
            self.decision,
            decision_id="task-2-v1",
            task_id="task-2",
            supersedes_decision_id="task-1-v1",
        )
        self.write_registry([self.decision, second])

        with self.assertRaisesRegex(ValueError, "same task"):
            self.validate()

    def test_future_decision_timestamp_is_rejected(self):
        self.decision["recorded_at"] = "2026-11-26T09:00:00+07:00"
        self.write_registry()

        with self.assertRaisesRegex(ValueError, "future"):
            self.validate()

    def test_search_finds_code_path_by_tag(self):
        registry = self.validate()

        result = automation_registry.search_registry(registry, "doi")

        self.assertEqual(["example-tool"], [item["artifact_id"] for item in result["artifacts"]])
        self.assertEqual(["task-1-v1"], [item["decision_id"] for item in result["decisions"]])

    def test_cli_validate_and_search_emit_json(self):
        script = Path(automation_registry.__file__)
        common = [
            "/usr/bin/python3", str(script),
            "--root", str(self.root),
            "--catalog", str(self.catalog_path),
            "--decisions", str(self.decisions_path),
        ]
        validated = subprocess.run(
            [*common, "validate"], text=True, capture_output=True, check=False
        )
        searched = subprocess.run(
            [*common, "search", "doi"], text=True, capture_output=True, check=False
        )

        self.assertEqual(0, validated.returncode, validated.stderr)
        self.assertEqual({"artifacts": 1, "decisions": 1, "active_tasks": 1}, json.loads(validated.stdout))
        self.assertEqual(0, searched.returncode, searched.stderr)
        self.assertEqual("example-tool", json.loads(searched.stdout)["artifacts"][0]["artifact_id"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
