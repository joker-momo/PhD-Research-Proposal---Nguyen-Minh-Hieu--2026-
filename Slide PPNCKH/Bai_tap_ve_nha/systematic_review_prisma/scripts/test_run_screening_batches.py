"""Tests for the screening driver's baseline-aware Git precondition."""
from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts.run_screening_batches import owned_git_status


class OwnedGitStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="screening-driver-test-")
        self.repository = Path(self.temp.name)
        self.project = (
            self.repository
            / "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma"
        )
        self.project.mkdir(parents=True)
        (self.repository / ".codex").mkdir()
        self.agents = self.repository / "AGENTS.md"
        self.codex = self.repository / ".codex/owned.txt"
        self.project_file = self.project / "owned.txt"
        self.outside = self.repository / "outside.txt"
        for path in (self.agents, self.codex, self.project_file, self.outside):
            path.write_text("baseline\n")
        self.git("init", "-q")
        self.git("config", "user.name", "Driver Test")
        self.git("config", "user.email", "driver-test@example.invalid")
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.addCleanup(self.temp.cleanup)

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.repository), *args],
            check=True,
            capture_output=True,
        ).stdout

    def status(self):
        return owned_git_status(self.repository, self.project)

    def test_outside_scope_residue_is_ignored_for_all_git_states(self):
        untracked = self.repository / "external-baseline.txt"
        for state in ("untracked", "modified", "staged"):
            if state == "untracked":
                untracked.write_text("pending\n")
            else:
                untracked.unlink(missing_ok=True)
                self.outside.write_text("pending\n")
                if state == "staged":
                    self.git("add", "outside.txt")
            with self.subTest(state=state):
                self.assertEqual(b"", self.status())

    def test_each_owned_scope_is_checked(self):
        for path in (self.project_file, self.codex, self.agents):
            path.write_text("pending\n")
            with self.subTest(path=path.relative_to(self.repository)):
                self.assertNotEqual(b"", self.status())
            path.write_text("baseline\n")

    def test_project_residue_is_detected_for_all_git_states(self):
        untracked = self.project / "untracked.txt"
        for state in ("untracked", "modified", "staged"):
            if state == "untracked":
                untracked.write_text("pending\n")
            else:
                untracked.unlink(missing_ok=True)
                self.project_file.write_text("pending\n")
                if state == "staged":
                    self.git("add", str(self.project_file.relative_to(self.repository)))
            with self.subTest(state=state):
                self.assertNotEqual(b"", self.status())


if __name__ == "__main__":
    unittest.main(verbosity=2)
