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


def dispatch_command(payload):
    """Return the route and arguments of a recognized shell dispatch."""
    if payload.get("tool_name") not in {"Bash", "exec_command", "shell_command"}:
        return None
    args = payload.get("tool_input", {})
    if not isinstance(args, dict):
        return None
    command = args.get("command", args.get("cmd", ""))
    if not isinstance(command, str):
        return None
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|()")
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        # Conservatively guard malformed commands visibly naming dispatch.
        if any(marker in command for marker in ("bridge send", "a2a-route", "a2a send")):
            raise ValueError("Use a complete, literal dispatch command.")
        return None
    names = [Path(token).name for token in tokens]
    bridge_calls = [index for index in range(len(names) - 1)
                    if names[index:index + 2] == ["bridge", "send"]]
    legacy = ("a2a-route" in names or "run_screening_batches.py" in names
              or any(name == "a2a" and "send" in names[index + 1:]
                     for index, name in enumerate(names)))
    if bridge_calls:
        if (len(bridge_calls) != 1 or legacy
                or any(set(token) <= set(";&|()") for token in tokens)):
            raise ValueError("Run one literal bridge send in a separate tool call.")
        return "bridge", tokens[bridge_calls[0] + 2:]
    if legacy:
        return "legacy", []
    return None


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
    return state


def literal_option(args, name):
    values = []
    for index, arg in enumerate(args):
        if arg == name:
            values.append(args[index + 1] if index + 1 < len(args) else "")
        elif arg.startswith(name + "="):
            values.append(arg.split("=", 1)[1])
    if len(values) != 1:
        raise ValueError(f"bridge send requires exactly one literal {name}.")
    value = values[0]
    if not value or value.startswith("-") or any(char in value for char in "$`"):
        raise ValueError(f"bridge send requires a literal value for {name}.")
    return value


def project_path(path):
    try:
        return path.resolve().relative_to(PROJECT)
    except ValueError:
        raise ValueError(f"{path.name} must be inside this HK261 worktree.") from None


def require_committed_file(path):
    result = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "-t",
         f"HEAD:{path.relative_to(ROOT).as_posix()}"],
        capture_output=True, text=True, timeout=8, check=False,
    )
    if result.returncode or result.stdout.strip() != "blob" or not path.is_file():
        raise ValueError(f"Commit {path.name} before bridge send.")


def check_bridge_dispatch(args, state):
    task = state["task"]
    ready = state["next_task"]
    if (task["status"] not in {"completed", "rejected"}
            or ready["owner"] != "GEMINI_RESEARCH" or ready["status"] != "ready"):
        raise ValueError("Commit the phase setup or previous batch review before sending.")

    brief = Path(literal_option(args, "--brief"))
    if not brief.is_absolute():
        raise ValueError("Use an absolute --brief path inside this HK261 worktree.")
    relative = project_path(brief)
    if (relative.as_posix() != ready.get("dispatch_brief")
            or literal_option(args, "--message-id") != ready.get("message_id")):
        raise ValueError("Brief/message ID do not match the committed next_task. "
                         "Commit the preceding batch review before advancing.")

    checkpoint = task.get("checkpoint_path")
    if not isinstance(checkpoint, str) or not checkpoint or Path(checkpoint).is_absolute():
        raise ValueError("Set task.checkpoint_path to the phase manifest or batch review.")
    checkpoint = PROJECT / project_path(PROJECT / checkpoint)
    for path in (PROJECT / relative, checkpoint, CURRENT_STATE):
        require_committed_file(path)
    if (checkpoint in {PROJECT / relative, CURRENT_STATE, EVENT_LOG}
            or latest_commit_for((checkpoint,)) != latest_commit_for((CURRENT_STATE,))):
        raise ValueError("Commit the phase manifest or batch review together with current_state.json.")


def main():
    try:
        payload = json.load(sys.stdin)
        event = payload.get("hook_event_name")
        if event in {"UserPromptSubmit", "SessionStart"}:
            print(REMINDER)
            return 0
        if event != "PreToolUse":
            return 0
        dispatch = dispatch_command(payload)
        if dispatch is None:
            return 0
        route, args = dispatch
        if owned_git_status():
            reason = ("HK261 A2A blocked: staged/modified/untracked residue "
                      "exists in an owned path. Finish, validate and commit the "
                      "current task, then verify clean HK261/.codex/AGENTS.md "
                      "scopes before dispatching another task.")
        elif route == "legacy" and not current_state_fresh():
            reason = ("HK261 A2A blocked: current state is stale. Update "
                      "current_state.json in the task-closing commit before "
                      "dispatching another task.")
        else:
            state = current_state_valid()
            if route == "bridge":
                check_bridge_dispatch(args, state)
            return 0
    except (ValueError, AttributeError, OSError, RuntimeError,
            subprocess.TimeoutExpired) as error:
        reason = "HK261 task gate cannot validate input/state: " + str(error)
    print(reason, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
