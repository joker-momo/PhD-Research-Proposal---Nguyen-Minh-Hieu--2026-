#!/usr/bin/env python3
"""Validate and render the single canonical HK261 current-state record."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma"
DEFAULT_STATE = PROJECT / "MUST_READ_AI_AGENT/current_state.json"
DEFAULT_EVENTS = PROJECT / "MUST_READ_AI_AGENT/events.jsonl"
TIMESTAMP_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
)
TASK_STATUSES = {"active", "completed", "rejected", "blocked"}
NEXT_STATUSES = {"ready", "active", "blocked", "none"}
OWNERS = {"CODEX_WRITING", "GEMINI_RESEARCH"}


def _reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read valid JSON from {path}: {error}") from error


def parse_timestamp(value, now):
    if not isinstance(value, str) or not TIMESTAMP_PATTERN.fullmatch(value):
        raise ValueError("timestamp must be RFC 3339 with seconds and timezone")
    if value.endswith("-00:00"):
        raise ValueError("timestamp timezone must be known, not -00:00")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("timestamp is not a real calendar time") from error
    if parsed > now:
        raise ValueError("future timestamp is not permitted")
    return parsed


def _require_mapping(record, key):
    value = record.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"current state requires object: {key}")
    return value


def _require_text(record, key, label):
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} requires non-empty {key}")
    return value


def _validate_task(task, updated_at, now):
    _require_text(task, "task_id", "task")
    if task.get("owner") not in OWNERS:
        raise ValueError("task owner is invalid")
    if task.get("status") not in TASK_STATUSES:
        raise ValueError("task status is invalid")
    _require_text(task, "decision_id", "task")
    started = parse_timestamp(task.get("started_at"), now)
    updated = parse_timestamp(task.get("updated_at"), now)
    if task["updated_at"] != updated_at:
        raise ValueError("task updated_at must equal state updated_at")
    if started > updated:
        raise ValueError("task started_at must not be after updated_at")
    if task["status"] not in {"completed", "rejected"} and "completed_at" in task:
        raise ValueError("completed_at is only valid for completed or rejected tasks")
    if task["status"] in {"completed", "rejected"}:
        completed = parse_timestamp(task.get("completed_at"), now)
        if not started <= completed <= updated:
            raise ValueError("task completed_at must lie between started_at and updated_at")


def _validate_next_task(next_task):
    _require_text(next_task, "task_id", "next_task")
    if next_task.get("owner") not in OWNERS:
        raise ValueError("next_task owner is invalid")
    if next_task.get("status") not in NEXT_STATUSES:
        raise ValueError("next_task status is invalid")
    _require_text(next_task, "action", "next_task")
    _require_text(next_task, "acceptance", "next_task")


def _validate_evidence(evidence):
    for key in ("retrieval_reports", "screened_reports"):
        value = evidence.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError(f"evidence {key} must be a non-negative integer")
    if evidence["screened_reports"] > evidence["retrieval_reports"]:
        raise ValueError("screened_reports cannot exceed retrieval_reports")
    decisions = _require_mapping(evidence, "working_decisions")
    values = []
    for key in ("include", "exclude", "uncertain"):
        value = decisions.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError(f"working_decisions {key} must be a non-negative integer")
        values.append(value)
    if sum(values) != evidence["screened_reports"]:
        raise ValueError("working decision total must equal screened_reports")

    if "supplemental_screening" in evidence:
        _validate_supplemental(_require_mapping(evidence, "supplemental_screening"))


def _validate_supplemental(supplemental):
    def count(key, default=None):
        value = supplemental.get(key, default)
        if type(value) is not int or value < 0:
            raise ValueError(f"supplemental {key} must be a non-negative integer")
        return value

    intake = count("intake_pdf_count")
    screened = count("screened_supplemental_count", 0)
    accounted = count("supplemental_decisions_accounted", screened)
    remaining = count("remaining_supplemental_reports", intake - accounted)
    if not screened <= accounted <= intake or accounted + remaining != intake:
        raise ValueError("supplemental screened, accounted and remaining totals do not reconcile")
    pending = supplemental.get("pending_retrieval_ids", [])
    if (not isinstance(pending, list)
            or any(not isinstance(key, str) or not key.strip() for key in pending)
            or len(pending) != len(set(pending))):
        raise ValueError("supplemental pending_retrieval_ids must be a list of distinct IDs")


def validate_state(state, events, now=None):
    now = now or datetime.now(timezone.utc)
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        raise ValueError("current state requires schema_version 1")
    updated_at = _require_text(state, "updated_at", "current state")
    parse_timestamp(updated_at, now)
    goal = _require_mapping(state, "goal")
    for key in ("version", "status", "summary"):
        _require_text(goal, key, "goal")
    task = _require_mapping(state, "task")
    _validate_task(task, updated_at, now)
    _validate_next_task(_require_mapping(state, "next_task"))
    project = _require_mapping(state, "project")
    for key in ("target_venue", "submission_status", "canonical_manuscript"):
        _require_text(project, key, "project")
    _validate_evidence(_require_mapping(state, "evidence"))
    for key in ("blockers", "user_confirmation_required"):
        value = state.get(key)
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise ValueError(f"current state {key} must be a list of non-empty strings")
    _require_mapping(state, "history")

    if not events:
        raise ValueError("event log is empty")
    for event in events:
        if not isinstance(event, dict):
            raise ValueError("event must be an object")
        _require_text(event, "task_id", "event")
        _require_text(event, "event", "event")
        parse_timestamp(event.get("timestamp"), now)
    latest = events[-1]
    if latest["task_id"] != task["task_id"] or latest["timestamp"] != updated_at:
        raise ValueError("latest event must match current task and state updated_at")
    return state


def validate_files(state_path=DEFAULT_STATE, events_path=DEFAULT_EVENTS, now=None):
    state = _load_json(Path(state_path))
    events = []
    try:
        lines = Path(events_path).read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise ValueError(f"cannot read event log {events_path}: {error}") from error
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line, object_pairs_hook=_reject_duplicate_keys))
        except (json.JSONDecodeError, ValueError) as error:
            raise ValueError(f"invalid event JSON at line {number}: {error}") from error
    return validate_state(state, events, now=now)


def render_summary(state):
    task = state["task"]
    next_task = state["next_task"]
    project = state["project"]
    evidence = state["evidence"]
    decisions = evidence["working_decisions"]
    supplemental_progress = ""
    if supplemental := evidence.get("supplemental_screening"):
        intake = supplemental["intake_pdf_count"]
        accounted = supplemental.get("supplemental_decisions_accounted",
                                     supplemental.get("screened_supplemental_count", 0))
        not_retrieved = len(supplemental.get("pending_retrieval_ids", []))
        supplemental_progress = f"\n- Supplemental reports: {accounted}/{intake} accounted"
        supplemental_progress += f" / {not_retrieved} not retrieved"
    blockers = "\n".join(f"- {item}" for item in state["blockers"]) or "- None recorded."
    confirmations = "\n".join(
        f"- {item}" for item in state["user_confirmation_required"]
    ) or "- None recorded."
    return f"""# HK261 current state

Updated: {state['updated_at']}
Goal: {state['goal']['version']} ({state['goal']['status']})
Submission: {project['submission_status']} to {project['target_venue']}
Manuscript: `{project['canonical_manuscript']}`

## Last task

- `{task['task_id']}` — {task['status']} — {task['owner']}
- Decision: `{task['decision_id']}`

## Evidence snapshot

- Reports: {evidence['screened_reports']}/{evidence['retrieval_reports']} screened
- Working decisions: {decisions['include']} INCLUDE / {decisions['exclude']} EXCLUDE / {decisions['uncertain']} UNCERTAIN{supplemental_progress}

## Next task

- `{next_task['task_id']}` — {next_task['status']} — {next_task['owner']}
- Action: {next_task['action']}
- Acceptance: {next_task['acceptance']}

## Blockers

{blockers}

## User confirmation required

{confirmations}
"""


def _parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--events", type=Path, default=DEFAULT_EVENTS)
    parser.add_argument("command", choices=("validate", "show"))
    return parser


def main(argv=None):
    args = _parser().parse_args(argv)
    try:
        state = validate_files(args.state, args.events)
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    if args.command == "validate":
        print(json.dumps({
            "task_id": state["task"]["task_id"],
            "status": state["task"]["status"],
            "updated_at": state["updated_at"],
            "next_task_id": state["next_task"]["task_id"],
        }, sort_keys=True))
    else:
        print(render_summary(state), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
