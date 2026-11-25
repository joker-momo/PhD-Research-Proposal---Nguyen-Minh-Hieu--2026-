"""Exercise actual hook subprocesses in disposable Git worktrees; no network."""
import json
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
        self.git("init", "-q")
        self.git("config", "user.name", "Gate Test")
        self.git("config", "user.email", "gate-test@example.invalid")
        self.file = self.root / "tracked.txt"
        self.file.write_text("baseline\n")
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.addCleanup(self.temp.cleanup)

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

    def test_dirty_a2a_blocked_for_each_residue_type(self):
        for state in ["untracked", "modified", "staged"]:
            if state == "untracked":
                (self.root / "residue.txt").write_text("pending")
            else:
                (self.root / "residue.txt").unlink(missing_ok=True)
                self.file.write_text("pending\n")
                if state == "staged":
                    self.git("add", "tracked.txt")
            for cmd in ["rtk proxy scripts/a2a-route --brief brief.md",
                        "rtk proxy a2a send -a http://127.0.0.1:1 brief",
                        "rtk proxy python3 scripts/run_screening_batches.py --start 2"]:
                with self.subTest(state=state, command=cmd):
                    r = self.call(cmd)
                    self.assertEqual(2, r.returncode)
                    self.assertIn("commit the current task", r.stderr)

    def test_dirty_non_a2a_allowed(self):
        self.file.write_text("pending\n")
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
