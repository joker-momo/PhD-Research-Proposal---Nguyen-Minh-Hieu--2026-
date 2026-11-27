"""Regression checks for the HK261 low-token onboarding contract."""
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma"
MUST_READ = PROJECT / "MUST_READ_AI_AGENT"
BASELINE_BYTES = 52_423
MAX_CORE_BYTES = 15_000
STATE_COMMAND = "python3 .codex/hooks/project_state.py show"


class ContextContractTests(unittest.TestCase):
    def test_manifest_uses_tiered_core_not_full_required_order(self):
        manifest = (MUST_READ / "context_manifest.yaml").read_text()

        self.assertRegex(manifest, r'(?m)^core_read_order:\n  - README\.md\ncore_state_command:')
        self.assertIn(f'core_state_command: "{STATE_COMMAND}"', manifest)
        self.assertIn("task_read_routes:", manifest)
        self.assertNotIn("required_read_order:", manifest)

    def test_default_context_budget_stays_below_limit(self):
        paths = (
            ROOT / "AGENTS.md",
            PROJECT / "AI_AGENT_START_HERE.md",
            MUST_READ / "context_manifest.yaml",
            MUST_READ / "README.md",
        )
        rendered = subprocess.run(
            [sys.executable, *STATE_COMMAND.split()[1:]],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout

        self.assertIn(b"# HK261 current state", rendered)
        current_bytes = sum(path.stat().st_size for path in paths) + len(rendered)

        self.assertLessEqual(current_bytes, MAX_CORE_BYTES)
        self.assertGreaterEqual(1 - current_bytes / BASELINE_BYTES, 0.60)

    def test_compatibility_markdown_contains_no_task_state_copy(self):
        for path in (
            MUST_READ / "CURRENT_HANDOFF.md",
            PROJECT / "corpus_expansion/current_tasks.md",
        ):
            self.assertNotIn("HK261_TASK_STATE", path.read_text())

    def test_verbose_pre_migration_state_is_preserved(self):
        self.assertTrue(
            (MUST_READ / "history/CURRENT_HANDOFF.pre-state-v1.2026-11-26.md").is_file()
        )
        self.assertTrue(
            (PROJECT / "corpus_expansion/history/current_tasks.pre-state-v1.2026-11-26.md").is_file()
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
