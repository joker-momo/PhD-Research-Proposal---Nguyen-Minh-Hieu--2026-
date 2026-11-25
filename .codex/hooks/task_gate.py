#!/usr/bin/env python3
"""Read-only HK261 task reminder and recognized A2A command guard."""
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
REMINDER = """Before EACH new HK261 task publish exactly five fields:
TASK: concrete task
OWNER: CODEX_WRITING or GEMINI_RESEARCH
OWNED_PATHS: explicit paths
BINARY_ACCEPTANCE: binary/countable checks
PRE_TASK_GIT_STATUS: observed branch, staged/modified/untracked counts, prior SHA
Any residue BLOCKS new tasks and A2A. Finish, validate, inspect diff, stage only
owned paths, commit current task, report SHA, and verify clean before continuing.
Codex owns writing/editing, project files, acceptance, and Git. Gemini via router
owns research/extraction/classification/structured synthesis, read-only. Commit
briefs before dispatch; require all five brief headings and all mandatory review
criteria PASS before adoption. Re-read project AGENTS.md and onboarding manifest
after restart, compaction, or a model change. Hooks are not a security boundary.
"""


def is_dispatch(payload):
    if payload.get("tool_name") not in {"Bash", "exec_command", "shell_command"}:
        return False
    args = payload.get("tool_input", {})
    if not isinstance(args, dict):
        return False
    command = args.get("command", args.get("cmd", ""))
    if not isinstance(command, str):
        return False
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|()")
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        # Conservatively guard malformed commands visibly naming dispatch.
        return "a2a-route" in command or "a2a send" in command
    names = [Path(token).name for token in tokens]
    if "a2a-route" in names or "run_screening_batches.py" in names:
        return True
    return any(name == "a2a" and "send" in names[index + 1:]
               for index, name in enumerate(names))


def git_status():
    # No lock/index refresh; inspect this hook's worktree, not the A2A server cwd.
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    result = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain=v1", "-z",
         "--untracked-files=all"], capture_output=True, env=env, timeout=8,
        check=False,
    )
    if result.returncode:
        raise RuntimeError("Cannot verify project Git status; A2A is blocked.")
    return result.stdout


def main():
    try:
        payload = json.load(sys.stdin)
        event = payload.get("hook_event_name")
        if event in {"UserPromptSubmit", "SessionStart"}:
            print(REMINDER)
            return 0
        if event != "PreToolUse" or not is_dispatch(payload):
            return 0
        if not git_status():
            return 0
        reason = ("HK261 A2A blocked: staged/modified/untracked residue exists. "
                  "Finish, validate and commit the current task, then verify a "
                  "clean project worktree before dispatching another task.")
    except (ValueError, AttributeError, OSError, RuntimeError,
            subprocess.TimeoutExpired) as error:
        reason = "HK261 task gate cannot validate input/state: " + str(error)
    print(reason, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
