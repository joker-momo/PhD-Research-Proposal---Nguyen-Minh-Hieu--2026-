"""Tests for the canonical HK261 current-state validator and renderer."""
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import subprocess
import tempfile
import unittest

import project_state


class ProjectStateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hk261-state-test-")
        self.root = Path(self.temp.name)
        self.state_path = self.root / "current_state.json"
        self.events_path = self.root / "events.jsonl"
        self.now = datetime.now(timezone.utc)
        stamp = (self.now - timedelta(minutes=1)).isoformat(timespec="seconds")
        self.state = {
            "schema_version": 1,
            "updated_at": stamp,
            "goal": {
                "version": "test-goal-v1",
                "status": "active",
                "summary": "Complete the verified review workflow.",
            },
            "task": {
                "task_id": "task-1",
                "owner": "CODEX_WRITING",
                "status": "completed",
                "started_at": stamp,
                "updated_at": stamp,
                "completed_at": stamp,
                "decision_id": "task-1-v1",
            },
            "next_task": {
                "task_id": "task-2",
                "owner": "GEMINI_RESEARCH",
                "status": "ready",
                "action": "Dispatch the committed correction brief once.",
                "acceptance": "Five records and twenty supported quotes.",
            },
            "project": {
                "target_venue": "SN Computer Science",
                "submission_status": "NOT_READY_NOT_SUBMITTED",
                "canonical_manuscript": "manuscript/sn_computer_science/main.tex",
            },
            "evidence": {
                "retrieval_reports": 46,
                "screened_reports": 46,
                "working_decisions": {"include": 32, "exclude": 2, "uncertain": 12},
            },
            "blockers": ["Formal database search is incomplete."],
            "user_confirmation_required": ["Verified author metadata."],
            "history": {"event_log": "events.jsonl", "archive": "history/"},
        }
        self.event = {"task_id": "task-1", "event": "completed", "timestamp": stamp}
        self.write_fixture()
        self.addCleanup(self.temp.cleanup)

    def write_fixture(self):
        self.state_path.write_text(json.dumps(self.state) + "\n")
        self.events_path.write_text(json.dumps(self.event) + "\n")

    def test_valid_state_and_latest_event_pass(self):
        result = project_state.validate_files(
            self.state_path, self.events_path, now=self.now
        )

        self.assertEqual("task-1", result["task"]["task_id"])

    def test_missing_required_section_fails(self):
        self.state.pop("next_task")
        self.write_fixture()

        with self.assertRaisesRegex(ValueError, "next_task"):
            project_state.validate_files(self.state_path, self.events_path, now=self.now)

    def test_latest_event_must_match_task_and_updated_at(self):
        self.event["task_id"] = "other-task"
        self.write_fixture()

        with self.assertRaisesRegex(ValueError, "latest event"):
            project_state.validate_files(self.state_path, self.events_path, now=self.now)

    def test_future_state_timestamp_fails(self):
        self.state["updated_at"] = (self.now + timedelta(days=1)).isoformat(timespec="seconds")
        self.state["task"]["updated_at"] = self.state["updated_at"]
        self.state["task"]["completed_at"] = self.state["updated_at"]
        self.event["timestamp"] = self.state["updated_at"]
        self.write_fixture()

        with self.assertRaisesRegex(ValueError, "future"):
            project_state.validate_files(self.state_path, self.events_path, now=self.now)

    def test_summary_is_compact_and_contains_next_action(self):
        rendered = project_state.render_summary(self.state)

        self.assertLessEqual(len(rendered), 1800)
        self.assertIn("task-2", rendered)
        self.assertIn("NOT_READY_NOT_SUBMITTED", rendered)
        self.assertNotIn("Formal database search is incomplete.\nFormal", rendered)

    def test_cli_validate_and_show(self):
        script = Path(project_state.__file__)
        common = [
            "/usr/bin/python3", str(script),
            "--state", str(self.state_path),
            "--events", str(self.events_path),
        ]

        validated = subprocess.run([*common, "validate"], text=True, capture_output=True)
        shown = subprocess.run([*common, "show"], text=True, capture_output=True)

        self.assertEqual(0, validated.returncode, validated.stderr)
        self.assertEqual("task-1", json.loads(validated.stdout)["task_id"])
        self.assertEqual(0, shown.returncode, shown.stderr)
        self.assertIn("task-2", shown.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
