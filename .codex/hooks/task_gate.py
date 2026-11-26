#!/usr/bin/env python3
"""Read-only HK261 task reminder and recognized A2A command guard."""
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

from automation_registry import validate_registry
from project_state import validate_files

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma"
CURRENT_STATE = PROJECT / "MUST_READ_AI_AGENT/current_state.json"
EVENT_LOG = PROJECT / "MUST_READ_AI_AGENT/events.jsonl"
OWNED_GIT_PATHS = (
    ROOT / "AGENTS.md",
    ROOT / ".codex",
    PROJECT,
)
AUTOMATION_CATALOG = PROJECT / "automation/artifact_catalog.json"
AUTOMATION_DECISIONS = PROJECT / "automation/decision_log.jsonl"
REMINDER = "HK261_GATE: follow AGENTS.md; run the pre-task gate before new work."


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


def owned_git_status():
    """Return residue only in HK261 and its repository-level rule surfaces."""
    relative_paths = [str(path.relative_to(ROOT)) for path in OWNED_GIT_PATHS]
    # No lock/index refresh; inspect this hook's worktree, not the A2A server cwd.
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    result = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain=v1", "-z",
         "--untracked-files=all", "--", *relative_paths], capture_output=True,
        env=env, timeout=8, check=False,
    )
    if result.returncode:
        raise RuntimeError("Cannot verify owned-scope Git status; A2A is blocked.")
    return result.stdout


def latest_commit_for(paths):
    relative_paths = [str(path.relative_to(ROOT)) for path in paths]
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-list", "-1", "HEAD", "--",
         *relative_paths], capture_output=True, text=True, env=env, timeout=8,
        check=False,
    )
    if result.returncode:
        raise RuntimeError("Cannot inspect project status-document history.")
    return result.stdout.strip()


def current_state_fresh():
    if not CURRENT_STATE.is_file():
        return False
    latest_project_commit = latest_commit_for((PROJECT,))
    latest_state_commit = latest_commit_for((CURRENT_STATE,))
    return bool(latest_project_commit and latest_state_commit == latest_project_commit)


def current_state_valid():
    state = validate_files(CURRENT_STATE, EVENT_LOG)
    registry = validate_registry(
        AUTOMATION_CATALOG, AUTOMATION_DECISIONS, ROOT
    )
    task = state["task"]
    decision = registry["active_by_task"].get(task["task_id"])
    if decision is None:
        raise ValueError("current task requires one active code-first decision")
    if decision["decision_id"] != task["decision_id"]:
        raise ValueError("current task decision_id does not match the active decision")
    return True


def main():
    try:
        payload = json.load(sys.stdin)
        event = payload.get("hook_event_name")
        if event in {"UserPromptSubmit", "SessionStart"}:
            print(REMINDER)
            return 0
        if event != "PreToolUse" or not is_dispatch(payload):
            return 0
        if owned_git_status():
            reason = ("HK261 A2A blocked: staged/modified/untracked residue "
                      "exists in an owned path. Finish, validate and commit the "
                      "current task, then verify clean HK261/.codex/AGENTS.md "
                      "scopes before dispatching another task.")
        elif not current_state_fresh():
            reason = ("HK261 A2A blocked: current state is stale. Update "
                      "current_state.json in the task-closing commit before "
                      "dispatching another task.")
        else:
            current_state_valid()
            return 0
    except (ValueError, AttributeError, OSError, RuntimeError,
            subprocess.TimeoutExpired) as error:
        reason = "HK261 task gate cannot validate input/state: " + str(error)
    print(reason, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
