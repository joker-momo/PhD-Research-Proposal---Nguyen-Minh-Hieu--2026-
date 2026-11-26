#!/usr/bin/env python3
"""Validate and search durable HK261 automation decisions and code artifacts."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma"
DEFAULT_CATALOG = PROJECT / "automation/artifact_catalog.json"
DEFAULT_DECISIONS = PROJECT / "automation/decision_log.jsonl"
MODES = {"REUSE_EXISTING", "WRITE_SCRIPT", "MANUAL"}
ARTIFACT_FIELDS = {
    "artifact_id", "name", "path", "purpose", "entrypoint", "inputs",
    "outputs", "tests", "test_command", "status", "tags",
}
DECISION_FIELDS = {
    "decision_id", "task_id", "decided_at", "recorded_at", "mode", "reason",
    "artifact_ids", "verification",
}


def _nonempty_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _string_list(value, label, allow_empty=False):
    if not isinstance(value, list) or (not value and not allow_empty):
        raise ValueError(f"{label} must be a non-empty list")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{label} must contain non-empty strings")
    return value


def _parse_timestamp(value, label, now):
    _nonempty_string(value, label)
    if value.endswith("-00:00"):
        raise ValueError(f"{label} timezone must be known")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{label} must be RFC 3339") from error
    if parsed.tzinfo is None:
        raise ValueError(f"{label} must include a timezone")
    if parsed > now:
        raise ValueError(f"{label} must not be in the future")
    return parsed


def _repository_path(root, value, label):
    relative = Path(_nonempty_string(value, label))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"{label} must be repository-relative without '..'")
    root = root.resolve()
    resolved = (root / relative).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise ValueError(f"{label} must stay inside the repository") from error
    return resolved


def _read_decisions(path):
    decisions = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid decision JSON at line {line_number}") from error
        if not isinstance(record, dict):
            raise ValueError(f"decision line {line_number} must be an object")
        decisions.append(record)
    if not decisions:
        raise ValueError("decision log must contain at least one record")
    return decisions


def validate_registry(catalog_path, decisions_path, root, now=None):
    """Return validated registry data or raise ValueError with an exact cause."""
    root = Path(root)
    catalog_path = Path(catalog_path)
    decisions_path = Path(decisions_path)
    now = now or datetime.now(timezone.utc)
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    if not isinstance(catalog, dict) or catalog.get("schema_version") != 1:
        raise ValueError("artifact catalog requires schema_version 1")
    artifacts = catalog.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError("artifact catalog must contain at least one artifact")

    artifacts_by_id = {}
    for index, artifact in enumerate(artifacts):
        label = f"artifact[{index}]"
        if not isinstance(artifact, dict) or not ARTIFACT_FIELDS.issubset(artifact):
            raise ValueError(f"{label} is missing required fields")
        artifact_id = _nonempty_string(artifact["artifact_id"], f"{label}.artifact_id")
        if artifact_id in artifacts_by_id:
            raise ValueError(f"duplicate artifact_id: {artifact_id}")
        for field in ("name", "purpose", "entrypoint", "test_command"):
            _nonempty_string(artifact[field], f"{label}.{field}")
        for field in ("inputs", "outputs", "tests", "tags"):
            _string_list(artifact[field], f"{label}.{field}")
        if artifact.get("status") not in {"active", "retired"}:
            raise ValueError(f"{label}.status must be active or retired")
        code_path = _repository_path(root, artifact["path"], f"{label}.path")
        if not code_path.is_file():
            raise ValueError(f"artifact path does not exist: {artifact['path']}")
        for test_path in artifact["tests"]:
            resolved_test = _repository_path(root, test_path, f"{label}.tests")
            if not resolved_test.is_file():
                raise ValueError(f"test path does not exist: {test_path}")
        artifacts_by_id[artifact_id] = artifact

    decisions = _read_decisions(decisions_path)
    decisions_by_id = {}
    superseded_ids = set()
    for index, decision in enumerate(decisions):
        label = f"decision[{index}]"
        if not DECISION_FIELDS.issubset(decision):
            raise ValueError(f"{label} is missing required fields")
        decision_id = _nonempty_string(decision["decision_id"], f"{label}.decision_id")
        task_id = _nonempty_string(decision["task_id"], f"{label}.task_id")
        if decision_id in decisions_by_id:
            raise ValueError(f"duplicate decision_id: {decision_id}")
        if decision.get("mode") not in MODES:
            raise ValueError(f"{label}.mode must be one of {sorted(MODES)}")
        _nonempty_string(decision["reason"], f"{label}.reason")
        artifact_ids = _string_list(
            decision["artifact_ids"], f"{label}.artifact_ids", allow_empty=True
        )
        verification = _string_list(decision["verification"], f"{label}.verification")
        unknown = sorted(set(artifact_ids) - set(artifacts_by_id))
        if unknown:
            raise ValueError(f"unknown artifact_id: {', '.join(unknown)}")
        if decision["mode"] in {"REUSE_EXISTING", "WRITE_SCRIPT"} and not artifact_ids:
            raise ValueError(f"{decision['mode']} requires at least one artifact")
        if not verification:
            raise ValueError(f"{label}.verification must not be empty")
        decided_at = _parse_timestamp(decision["decided_at"], f"{label}.decided_at", now)
        recorded_at = _parse_timestamp(decision["recorded_at"], f"{label}.recorded_at", now)
        if decided_at > recorded_at:
            raise ValueError(f"{label}.decided_at must not be after recorded_at")
        supersedes = decision.get("supersedes_decision_id")
        if supersedes is not None:
            _nonempty_string(supersedes, f"{label}.supersedes_decision_id")
            previous = decisions_by_id.get(supersedes)
            if previous is None:
                raise ValueError("supersedes_decision_id must reference an earlier decision")
            if previous["task_id"] != task_id:
                raise ValueError("supersedes_decision_id must reference the same task")
            if supersedes in superseded_ids:
                raise ValueError("a decision may be superseded only once")
            superseded_ids.add(supersedes)
        decisions_by_id[decision_id] = decision

    active_by_task = {}
    for decision_id, decision in decisions_by_id.items():
        if decision_id in superseded_ids:
            continue
        task_id = decision["task_id"]
        if task_id in active_by_task:
            raise ValueError(f"multiple active decisions for task_id: {task_id}")
        active_by_task[task_id] = decision

    return {
        "schema_version": 1,
        "artifacts": artifacts,
        "artifacts_by_id": artifacts_by_id,
        "decisions": decisions,
        "active_by_task": active_by_task,
    }


def search_registry(registry, query):
    """Return artifact and decision records containing all query terms."""
    terms = [term.casefold() for term in query.split() if term.strip()]

    def matches(record):
        haystack = json.dumps(record, ensure_ascii=False, sort_keys=True).casefold()
        return all(term in haystack for term in terms)

    return {
        "artifacts": [item for item in registry["artifacts"] if matches(item)],
        "decisions": [item for item in registry["decisions"] if matches(item)],
    }


def _parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="Validate catalog and decision history")
    search = subparsers.add_parser("search", help="Search code and decision evidence")
    search.add_argument("query")
    return parser


def main(argv=None):
    args = _parser().parse_args(argv)
    try:
        registry = validate_registry(args.catalog, args.decisions, args.root)
        if args.command == "validate":
            output = {
                "artifacts": len(registry["artifacts"]),
                "decisions": len(registry["decisions"]),
                "active_tasks": len(registry["active_by_task"]),
            }
        else:
            output = search_registry(registry, args.query)
        print(json.dumps(output, ensure_ascii=False, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"automation registry invalid: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
