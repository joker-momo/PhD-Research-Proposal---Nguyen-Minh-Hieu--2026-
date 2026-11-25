"""Exercise actual hook subprocesses in disposable Git worktrees; no network."""
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).with_name("task_gate.py")


class TaskGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hk261-gate-test-")
        self.root = Path(self.temp.name)
        self.script = self.root / ".codex/hooks/task_gate.py"
        self.script.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE, self.script)
        self.codex_file = self.root / ".codex/owned.txt"
        self.codex_file.write_text("baseline\n")
        self.agents_file = self.root / "AGENTS.md"
        self.agents_file.write_text("baseline\n")
        self.git("init", "-q")
        self.git("config", "user.name", "Gate Test")
        self.git("config", "user.email", "gate-test@example.invalid")
        self.file = self.root / "tracked.txt"
        self.file.write_text("baseline\n")
        self.project = (self.root / "Slide PPNCKH/Bai_tap_ve_nha/"
                        "systematic_review_prisma")
        self.owned_file = self.project / "owned.txt"
        self.owned_file.parent.mkdir(parents=True)
        self.owned_file.write_text("baseline\n")
        self.handoff = (self.project / "MUST_READ_AI_AGENT/"
                        "CURRENT_HANDOFF.md")
        self.tasks = self.project / "corpus_expansion/current_tasks.md"
        self.handoff.parent.mkdir(parents=True)
        self.tasks.parent.mkdir(parents=True)
        self.handoff.write_text("# Current Handoff\n\nCurrent fixture state.\n")
        self.tasks.write_text("# Current research tasks\n\nNo active task.\n")
        self.write_timestamps()
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.addCleanup(self.temp.cleanup)

    def write_timestamps(self):
        timestamp = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat(timespec="seconds")
        record = dict(task_id="fixture", status="completed", started_at=timestamp,
                      updated_at=timestamp, completed_at=timestamp)
        for path in (self.handoff, self.tasks):
            path.write_text(path.read_text() + "\n<!-- HK261_TASK_STATE\n" +
                            json.dumps(record) + "\n-->\n")
        manifest = self.handoff.parent / "context_manifest.yaml"
        manifest.write_text('updated_at: "' + timestamp + '"\n')
        self.events = self.handoff.parent / "events.jsonl"
        self.events.write_text(json.dumps(dict(task_id="fixture", event="completed",
                                              timestamp=timestamp)) + "\n")

    def commit_timestamp_change(self, mutate):
        for path in (self.handoff, self.tasks):
            text = path.read_text()
            prefix, block = text.split("<!-- HK261_TASK_STATE\n")
            record = json.loads(block.split("\n-->")[0])
            mutate(record)
            path.write_text(prefix + "<!-- HK261_TASK_STATE\n" + json.dumps(record) + "\n-->\n")
        self.git("add", str(self.project.relative_to(self.root)))
        self.git("commit", "-qm", "timestamp fixture")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args],
                              check=True, capture_output=True).stdout

    def call(self, command="", event="PreToolUse"):
        before = self.git("status", "--porcelain=v1", "-z")
        index_before = (self.root / ".git/index").read_bytes()
        content_before = self.file.read_bytes()
        result = subprocess.run(
            ["/usr/bin/python3", str(self.script)], cwd="/tmp",
            input=json.dumps({"hook_event_name": event, "tool_name": "Bash",
                              "cwd": "/tmp", "tool_input": {"command": command}}),
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(before, self.git("status", "--porcelain=v1", "-z"))
        self.assertEqual(index_before, (self.root / ".git/index").read_bytes())
        self.assertEqual(content_before, self.file.read_bytes())
        return result

    def test_clean_a2a_allowed(self):
        for cmd in ["rtk proxy /opt/research/scripts/a2a-route --brief brief.md",
                    "rtk proxy a2a send -a http://127.0.0.1:1 brief"]:
            self.assertEqual(0, self.call(cmd).returncode)

    def test_clean_a2a_blocked_when_status_documents_are_stale(self):
        artifact = self.project / "screening_46/results/batch_99.json"
        artifact.parent.mkdir(parents=True)
        artifact.write_text('{"status":"accepted"}\n')
        self.git("add", str(artifact.relative_to(self.root)))
        self.git("commit", "-qm", "accepted result without status update")

        result = self.call("rtk proxy scripts/a2a-route --brief next.md")

        self.assertEqual(2, result.returncode)
        self.assertIn("status documents are stale", result.stderr)

    def test_clean_a2a_allowed_after_status_documents_are_refreshed(self):
        artifact = self.project / "screening_46/results/batch_99.json"
        artifact.parent.mkdir(parents=True)
        artifact.write_text('{"status":"accepted"}\n')
        self.git("add", str(artifact.relative_to(self.root)))
        self.git("commit", "-qm", "accepted result without status update")
        self.handoff.write_text("# Current Handoff\n\nBatch 99 accepted.\n")
        self.tasks.write_text("# Current research tasks\n\nBatch 100 is next.\n")
        self.write_timestamps()
        self.git("add", str(self.project.relative_to(self.root)))
        self.git("commit", "-qm", "refresh current status")

        result = self.call("rtk proxy scripts/a2a-route --brief next.md")

        self.assertEqual(0, result.returncode)

    def test_clean_a2a_blocked_when_only_one_status_document_is_refreshed(self):
        artifact = self.project / "screening_46/results/batch_99.json"
        artifact.parent.mkdir(parents=True)
        artifact.write_text('{"status":"accepted"}\n')
        self.git("add", str(artifact.relative_to(self.root)))
        self.git("commit", "-qm", "accepted result without status update")
        self.handoff.write_text("# Current Handoff\n\nBatch 99 accepted.\n")
        self.git("add", str(self.handoff.relative_to(self.root)))
        self.git("commit", "-qm", "refresh only one status document")

        result = self.call("rtk proxy scripts/a2a-route --brief next.md")

        self.assertEqual(2, result.returncode)
        self.assertIn("status documents are stale", result.stderr)

    def test_dirty_a2a_blocked_for_each_residue_type(self):
        for state in ["untracked", "modified", "staged"]:
            if state == "untracked":
                (self.project / "residue.txt").write_text("pending")
            else:
                (self.project / "residue.txt").unlink(missing_ok=True)
                self.owned_file.write_text("pending\n")
                if state == "staged":
                    self.git("add", str(self.owned_file.relative_to(self.root)))
            for cmd in ["rtk proxy scripts/a2a-route --brief brief.md",
                        "rtk proxy a2a send -a http://127.0.0.1:1 brief",
                        "rtk proxy python3 scripts/run_screening_batches.py --start 2"]:
                with self.subTest(state=state, command=cmd):
                    r = self.call(cmd)
                    self.assertEqual(2, r.returncode)
                    self.assertIn("commit the current task", r.stderr)

    def test_outside_scope_residue_allowed_for_each_residue_type(self):
        for state in ["untracked", "modified", "staged"]:
            if state == "untracked":
                (self.root / "outside-residue.txt").write_text("pending")
            else:
                (self.root / "outside-residue.txt").unlink(missing_ok=True)
                self.file.write_text("pending\n")
                if state == "staged":
                    self.git("add", "tracked.txt")
            with self.subTest(state=state):
                r = self.call("rtk proxy scripts/a2a-route --brief brief.md")
                self.assertEqual(0, r.returncode)

    def test_each_owned_scope_blocks_a2a(self):
        for path in (self.owned_file, self.codex_file, self.agents_file):
            path.write_text("pending\n")
            with self.subTest(path=path.relative_to(self.root)):
                r = self.call("rtk proxy scripts/a2a-route --brief brief.md")
                self.assertEqual(2, r.returncode)
                self.assertIn("owned path", r.stderr)
            path.write_text("baseline\n")

    def test_dirty_non_a2a_allowed(self):
        self.owned_file.write_text("pending\n")
        for cmd in ["rtk proxy git status --short", "rtk proxy python3 check.py",
                    "rtk proxy git commit -m finish", "rtk proxy a2a task get TASK -o json"]:
            self.assertEqual(0, self.call(cmd).returncode)

    def test_reminder_on_prompt_start_resume_and_compaction_event(self):
        for event in ["UserPromptSubmit", "SessionStart"]:
            r = self.call(event=event)
            self.assertEqual(0, r.returncode)
            for field in ["TASK:", "OWNER:", "OWNED_PATHS:", "BINARY_ACCEPTANCE:",
                          "PRE_TASK_GIT_STATUS:"]:
                self.assertIn(field, r.stdout)

    def test_missing_timestamp_fields_block(self):
        original = json.loads(re.search(r"<!-- HK261_TASK_STATE\n(.*?)\n-->",
                                        self.handoff.read_text(), re.DOTALL).group(1))
        for field in ("started_at", "updated_at", "completed_at"):
            def remove_one(record):
                record.clear()
                record.update(original)
                record.pop(field)
            self.commit_timestamp_change(remove_one)
            self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_timezone_missing_blocks(self):
        self.commit_timestamp_change(lambda r: r.update(started_at="2026-01-01T00:00:00"))
        self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_malformed_timestamp_blocks(self):
        self.commit_timestamp_change(lambda r: r.update(started_at="2026-02-30T00:00:00+07:00"))
        self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_future_timestamp_blocks(self):
        future = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat(timespec="seconds")
        self.commit_timestamp_change(lambda r: r.update(completed_at=future))
        self.assertIn("future timestamp", self.call("a2a-route --brief next.md").stderr)

    def test_wrong_timestamp_order_blocks(self):
        self.commit_timestamp_change(lambda r: r.update(updated_at="2020-01-01T00:00:00Z"))
        self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_unknown_timezone_blocks(self):
        self.commit_timestamp_change(lambda r: r.update(started_at="2020-01-01T00:00:00-00:00"))
        self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_invalid_event_timestamp_blocks(self):
        event = json.loads(self.events.read_text())
        event["timestamp"] = "2026-01-01"
        self.events.write_text(json.dumps(event) + "\n")
        self.commit_timestamp_change(lambda r: None)
        self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_invalid_timestamps_allow_finishing_commands(self):
        self.commit_timestamp_change(lambda r: r.pop("started_at"))
        self.assertEqual(0, self.call("git commit -m repair").returncode)


if __name__ == "__main__":
    unittest.main(verbosity=2)
