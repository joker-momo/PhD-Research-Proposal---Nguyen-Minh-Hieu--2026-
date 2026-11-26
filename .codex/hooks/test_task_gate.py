"""Exercise actual hook subprocesses in disposable Git worktrees; no network."""
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).with_name("task_gate.py")
REGISTRY_SOURCE = Path(__file__).with_name("automation_registry.py")
STATE_SOURCE = Path(__file__).with_name("project_state.py")


class TaskGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hk261-gate-test-")
        self.root = Path(self.temp.name)
        self.script = self.root / ".codex/hooks/task_gate.py"
        self.script.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE, self.script)
        shutil.copyfile(REGISTRY_SOURCE, self.script.with_name("automation_registry.py"))
        shutil.copyfile(STATE_SOURCE, self.script.with_name("project_state.py"))
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
        self.state = self.handoff.parent / "current_state.json"
        self.write_timestamps()
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.addCleanup(self.temp.cleanup)

    def write_timestamps(self):
        timestamp = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat(timespec="seconds")
        record = dict(task_id="fixture", status="completed", started_at=timestamp,
                      updated_at=timestamp, completed_at=timestamp,
                      owner="CODEX_WRITING", decision_id="fixture-v1")
        self.state.write_text(json.dumps({
            "schema_version": 1,
            "updated_at": timestamp,
            "goal": {"version": "fixture-v1", "status": "active",
                     "summary": "Exercise the task gate."},
            "task": record,
            "next_task": {"task_id": "next", "owner": "GEMINI_RESEARCH",
                          "status": "ready", "action": "Dispatch once.",
                          "acceptance": "One complete result."},
            "project": {"target_venue": "Fixture", "submission_status": "NOT_READY",
                        "canonical_manuscript": "fixture.tex"},
            "evidence": {"retrieval_reports": 1, "screened_reports": 1,
                         "working_decisions": {"include": 1, "exclude": 0,
                                               "uncertain": 0}},
            "blockers": [],
            "user_confirmation_required": [],
            "history": {"event_log": "events.jsonl"},
        }) + "\n")
        self.events = self.handoff.parent / "events.jsonl"
        self.events.write_text(json.dumps(dict(task_id="fixture", event="completed",
                                              timestamp=timestamp)) + "\n")
        automation = self.project / "automation"
        automation.mkdir(exist_ok=True)
        self.catalog = automation / "artifact_catalog.json"
        self.catalog.write_text(json.dumps({
            "schema_version": 1,
            "artifacts": [{
                "artifact_id": "fixture-tool",
                "name": "Fixture tool",
                "path": ".codex/hooks/automation_registry.py",
                "purpose": "Exercise the registry gate fixture.",
                "entrypoint": "python3 .codex/hooks/automation_registry.py validate",
                "inputs": ["Fixture catalog and decision log"],
                "outputs": ["Validation status"],
                "tests": [".codex/hooks/task_gate.py"],
                "test_command": "python3 .codex/hooks/task_gate.py",
                "status": "active",
                "tags": ["fixture", "gate"],
            }],
        }) + "\n")
        self.decisions = automation / "decision_log.jsonl"
        self.decisions.write_text(json.dumps({
            "decision_id": "fixture-v1",
            "task_id": "fixture",
            "decided_at": timestamp,
            "recorded_at": timestamp,
            "mode": "REUSE_EXISTING",
            "reason": "The existing fixture tool is sufficient.",
            "artifact_ids": ["fixture-tool"],
            "verification": ["Fixture validation PASS"],
        }) + "\n")

    def commit_timestamp_change(self, mutate):
        state = json.loads(self.state.read_text())
        mutate(state["task"])
        self.state.write_text(json.dumps(state) + "\n")
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

    def prepare_bridge(self, brief_name="batch 01.md", *, commit_brief=True):
        brief = self.project / "briefs" / brief_name
        brief.parent.mkdir(exist_ok=True)
        brief.write_text("Approved brief.\n")
        state = json.loads(self.state.read_text())
        state["next_task"].update(
            dispatch_brief=brief.relative_to(self.project).as_posix(),
            message_id=brief.stem.replace(" ", "-"),
        )
        checkpoint = brief.with_suffix(".review")
        checkpoint.write_text("Checkpoint for the next batch.\n")
        state["task"]["checkpoint_path"] = checkpoint.relative_to(self.project).as_posix()
        self.state.write_text(json.dumps(state) + "\n")
        paths = [str(self.state), str(checkpoint)]
        if commit_brief:
            paths.append(str(brief))
        self.git("add", *paths)
        self.git("commit", "-qm", f"ready for {brief.stem}")
        return brief, state["next_task"]["message_id"]

    def bridge_command(self, brief, message_id):
        return shlex.join(["rtk", "proxy", "/opt/Gemini Research/bin/bridge",
                           "send", "--brief", str(brief), "--message-id", message_id])

    def test_bridge_allowed_after_unrelated_project_commit_and_stable_retry(self):
        brief, message_id = self.prepare_bridge()
        self.owned_file.write_text("A later committed project note.\n")
        self.git("add", str(self.owned_file))
        self.git("commit", "-qm", "project note without state churn")
        command = self.bridge_command(brief, message_id)
        for _ in range(2):
            result = self.call(command)
            self.assertEqual(0, result.returncode, result.stderr)

    def test_bridge_blocks_next_batch_until_ready_state_is_committed(self):
        first, first_id = self.prepare_bridge()
        second = first.with_name("batch 02.md")
        second.write_text("Prepared with the other briefs.\n")
        self.git("add", str(second))
        self.git("commit", "-qm", "prefile next brief")
        result = self.call(self.bridge_command(second, "batch-02"))
        self.assertEqual(2, result.returncode)
        self.assertIn("preceding batch review", result.stderr)
        result = self.call(self.bridge_command(first, first_id + "-changed"))
        self.assertEqual(2, result.returncode)
        self.assertIn("Brief/message ID", result.stderr)
        second, second_id = self.prepare_bridge("batch 02.md")
        result = self.call(self.bridge_command(second, second_id))
        self.assertEqual(0, result.returncode, result.stderr)

    def test_bridge_blocks_ignored_but_uncommitted_brief(self):
        (self.root / ".gitignore").write_text("batch 01.md\n")
        self.git("add", ".gitignore")
        self.git("commit", "-qm", "ignored brief fixture")
        brief, message_id = self.prepare_bridge(commit_brief=False)
        result = self.call(self.bridge_command(brief, message_id))
        self.assertEqual(2, result.returncode)
        self.assertIn("Commit batch 01.md", result.stderr)

    def test_bridge_blocks_state_only_change_without_review(self):
        brief, message_id = self.prepare_bridge()
        self.commit_timestamp_change(lambda task: task.update(notes="State-only update."))
        result = self.call(self.bridge_command(brief, message_id))
        self.assertEqual(2, result.returncode)
        self.assertIn("together with current_state.json", result.stderr)

    def test_bridge_blocks_active_preceding_task(self):
        brief, message_id = self.prepare_bridge()
        def mark_active(task):
            task["status"] = "active"
            task.pop("completed_at")
        self.commit_timestamp_change(mark_active)
        result = self.call(self.bridge_command(brief, message_id))
        self.assertEqual(2, result.returncode)
        self.assertIn("previous batch review", result.stderr)

    def test_bridge_requires_literal_single_dispatch(self):
        brief, message_id = self.prepare_bridge()
        command = self.bridge_command(brief, message_id)
        for invalid in (
            command + " --message-id duplicate",
            command + " && " + command,
            'bridge send --brief "$BRIEF" --message-id batch-01',
            "bridge send --brief batch01.md --message-id batch-01",
        ):
            with self.subTest(command=invalid):
                self.assertEqual(2, self.call(invalid).returncode)

    def test_bridge_blocks_brief_from_other_checkout(self):
        brief, message_id = self.prepare_bridge()
        result = self.call(self.bridge_command(self.root / brief.name, message_id))
        self.assertEqual(2, result.returncode)
        self.assertIn("inside this HK261 worktree", result.stderr)

    def test_clean_a2a_blocked_when_current_state_is_stale(self):
        artifact = self.project / "screening_46/results/batch_99.json"
        artifact.parent.mkdir(parents=True)
        artifact.write_text('{"status":"accepted"}\n')
        self.git("add", str(artifact.relative_to(self.root)))
        self.git("commit", "-qm", "accepted result without status update")

        result = self.call("rtk proxy scripts/a2a-route --brief next.md")

        self.assertEqual(2, result.returncode)
        self.assertIn("current state is stale", result.stderr)

    def test_clean_a2a_allowed_after_current_state_is_refreshed(self):
        artifact = self.project / "screening_46/results/batch_99.json"
        artifact.parent.mkdir(parents=True)
        artifact.write_text('{"status":"accepted"}\n')
        self.git("add", str(artifact.relative_to(self.root)))
        self.git("commit", "-qm", "accepted result without status update")
        self.write_timestamps()
        state = json.loads(self.state.read_text())
        state["goal"]["summary"] = "Batch 99 accepted; next task recorded."
        self.state.write_text(json.dumps(state) + "\n")
        self.git("add", str(self.project.relative_to(self.root)))
        self.git("commit", "-qm", "refresh current status")

        result = self.call("rtk proxy scripts/a2a-route --brief next.md")

        self.assertEqual(0, result.returncode)

    def test_clean_a2a_blocked_without_current_task_code_decision(self):
        self.decisions.write_text(json.dumps({
            "decision_id": "other-v1",
            "task_id": "other-task",
            "decided_at": "2026-01-01T00:00:00Z",
            "recorded_at": "2026-01-01T00:00:00Z",
            "mode": "MANUAL",
            "reason": "A different historical task.",
            "artifact_ids": [],
            "verification": ["Historical evidence"],
        }) + "\n")
        state = json.loads(self.state.read_text())
        state["goal"]["summary"] = "Fixture without a matching decision."
        self.state.write_text(json.dumps(state) + "\n")
        self.git("add", str(self.project.relative_to(self.root)))
        self.git("commit", "-qm", "remove current code decision")

        result = self.call("rtk proxy scripts/a2a-route --brief next.md")

        self.assertEqual(2, result.returncode)
        self.assertIn("active code-first decision", result.stderr)

    def test_compatibility_markdown_does_not_refresh_current_state(self):
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
        self.assertIn("current state is stale", result.stderr)

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
                        "rtk proxy python3 scripts/run_screening_batches.py --start 2",
                        "rtk proxy /opt/bridge send --brief /project/brief.md --message-id batch-01"]:
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
                    "rtk proxy git commit -m finish", "rtk proxy a2a task get TASK -o json",
                    "rtk proxy /opt/bridge get TASK"]:
            self.assertEqual(0, self.call(cmd).returncode)

    def test_reminder_on_prompt_start_resume_and_compaction_event(self):
        for event in ["UserPromptSubmit", "SessionStart"]:
            r = self.call(event=event)
            self.assertEqual(0, r.returncode)
            self.assertLessEqual(len(r.stdout), 160)
            self.assertIn("AGENTS.md", r.stdout)
            self.assertIn("pre-task gate", r.stdout)

    def test_missing_timestamp_fields_block(self):
        original = json.loads(self.state.read_text())["task"]
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
        self.commit_timestamp_change(lambda r: r.update(status="completed"))
        self.assertEqual(2, self.call("a2a-route --brief next.md").returncode)

    def test_invalid_timestamps_allow_finishing_commands(self):
        self.commit_timestamp_change(lambda r: r.pop("started_at"))
        self.assertEqual(0, self.call("git commit -m repair").returncode)


if __name__ == "__main__":
    unittest.main(verbosity=2)
