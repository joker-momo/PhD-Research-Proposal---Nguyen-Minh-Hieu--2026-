#!/usr/bin/env python3
"""Read-only HK261 task reminder and recognized A2A command guard."""
import json
from datetime import datetime, timezone
import re
import os
from pathlib import Path
import shlex
import subprocess
import sys

from automation_registry import validate_registry

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma"
STATUS_DOCUMENTS = (
    PROJECT / "MUST_READ_AI_AGENT/CURRENT_HANDOFF.md",
    PROJECT / "corpus_expansion/current_tasks.md",
)
OWNED_GIT_PATHS = (
    ROOT / "AGENTS.md",
    ROOT / ".codex",
    PROJECT,
)
AUTOMATION_CATALOG = PROJECT / "automation/artifact_catalog.json"
AUTOMATION_DECISIONS = PROJECT / "automation/decision_log.jsonl"
REMINDER = """Before EACH new HK261 task publish exactly five fields:
TASK: concrete task
OWNER: CODEX_WRITING or GEMINI_RESEARCH
OWNED_PATHS: explicit paths
BINARY_ACCEPTANCE: binary/countable checks
PRE_TASK_GIT_STATUS: observed branch, staged/modified/untracked counts, prior SHA
Any residue in HK261/.codex/AGENTS.md BLOCKS new tasks and A2A. Preserve the
authorized external baseline. Finish, validate, inspect diff, stage only owned
paths, commit current task, report SHA, and verify clean owned scopes first.
Codex owns writing/editing, project files, acceptance, and Git. Gemini via router
owns research/extraction/classification/structured synthesis, read-only. Commit
briefs before dispatch; require all five brief headings and all mandatory review
criteria PASS before adoption. Re-read project AGENTS.md and onboarding manifest
after restart, compaction, or a model change. Hooks are not a security boundary.
Update CURRENT_HANDOFF.md and current_tasks.md in the commit that closes or
changes a task; stale status documents block the next recognized A2A dispatch.
Use RFC 3339 timestamps with timezone (default Asia/Ho_Chi_Minh): started_at,
updated_at, completed_at for finished tasks; timestamp for every new log event.
Persist each CODE_FIRST_DECISION in automation/decision_log.jsonl. Register every
reused or newly written code artifact in automation/artifact_catalog.json so a
later agent can validate, search, test and reuse the exact committed path.
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


def status_documents_fresh():
    if any(not path.is_file() for path in STATUS_DOCUMENTS):
        return False
    latest_project_commit = latest_commit_for((PROJECT,))
    latest_status_commits = [latest_commit_for((path,))
                             for path in STATUS_DOCUMENTS]
    return bool(latest_project_commit and all(
        commit == latest_project_commit for commit in latest_status_commits
    ))


TIMESTAMP_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
)
TASK_STATE_PATTERN = re.compile(r"<!-- HK261_TASK_STATE\n(.*?)\n-->", re.DOTALL)


def parse_timestamp(value, now):
    if not isinstance(value, str) or not TIMESTAMP_PATTERN.fullmatch(value):
        raise ValueError("timestamp must be RFC 3339 with seconds and timezone")
    if value.endswith("-00:00"):
        raise ValueError("timestamp timezone must be known, not -00:00")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed > now:
        raise ValueError("future timestamp is not permitted")
    return parsed


def validate_task_timestamps(record, now):
    if not isinstance(record, dict) or not record.get("task_id"):
        raise ValueError("task record requires task_id")
    if record.get("status") not in {"active", "completed", "rejected", "blocked"}:
        raise ValueError("task record has missing or invalid status")
    started = parse_timestamp(record.get("started_at"), now)
    updated = parse_timestamp(record.get("updated_at"), now)
    if started > updated:
        raise ValueError("started_at must not be after updated_at")
    if record["status"] in {"completed", "rejected"} or "completed_at" in record:
        completed = parse_timestamp(record.get("completed_at"), now)
        if not started <= completed <= updated:
            raise ValueError("completed_at must lie between started_at and updated_at")


def status_timestamps_valid():
    now = datetime.now(timezone.utc)
    records = []
    for path in STATUS_DOCUMENTS:
        blocks = TASK_STATE_PATTERN.findall(path.read_text())
        if len(blocks) != 1:
            raise ValueError(f"{path.name} requires exactly one HK261_TASK_STATE block")
        record = json.loads(blocks[0])
        validate_task_timestamps(record, now)
        records.append(record)
    if records[0] != records[1]:
        raise ValueError("handoff and task queue metadata disagree")
    manifest = PROJECT / "MUST_READ_AI_AGENT/context_manifest.yaml"
    values = re.findall(r'^updated_at: "([^"\n]+)"$', manifest.read_text(), re.MULTILINE)
    if len(values) != 1 or values[0] != records[0]["updated_at"]:
        raise ValueError("manifest updated_at must match current task metadata")
    log = PROJECT / "MUST_READ_AI_AGENT/events.jsonl"
    events = [json.loads(line) for line in log.read_text().splitlines() if line.strip()]
    if not events:
        raise ValueError("event log is empty")
    for event in events:
        if not isinstance(event, dict) or not event.get("task_id") or not event.get("event"):
            raise ValueError("event requires task_id and event fields")
        parse_timestamp(event.get("timestamp"), now)
    last = events[-1]
    if last["task_id"] != records[0]["task_id"] or last["timestamp"] != records[0]["updated_at"]:
        raise ValueError("latest event must match current task and updated_at")
    registry = validate_registry(
        AUTOMATION_CATALOG, AUTOMATION_DECISIONS, ROOT, now=now
    )
    decision = registry["active_by_task"].get(records[0]["task_id"])
    if decision is None:
        raise ValueError("current task requires one active code-first decision")
    if parse_timestamp(decision["decided_at"], now) > parse_timestamp(
        records[0]["updated_at"], now
    ):
        raise ValueError("code-first decision must not be after task updated_at")
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
        elif not status_documents_fresh():
            reason = ("HK261 A2A blocked: status documents are stale. Update "
                      "CURRENT_HANDOFF.md and current_tasks.md together in a "
                      "focused commit before dispatching another task.")
        else:
            status_timestamps_valid()
            return 0
    except (ValueError, AttributeError, OSError, RuntimeError,
            subprocess.TimeoutExpired) as error:
        reason = "HK261 task gate cannot validate input/state: " + str(error)
    print(reason, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
