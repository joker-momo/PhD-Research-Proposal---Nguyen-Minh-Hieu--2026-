# Automation Evidence and Reuse Registry

This directory is the canonical evidence store for automation-first decisions
and reusable code in the HK261 project. It is not a scratch folder.

## Files

- `decision_log.jsonl`: append-only history of every recorded
  `CODE_FIRST_DECISION`. Never edit or delete an accepted earlier line. If a
  decision changes, append a new record with `supersedes_decision_id`.
- `artifact_catalog.json`: machine-readable index of reusable code. Paths are
  repository-relative and must resolve to committed files with committed tests.

The code itself stays in its natural project location. The catalog provides the
stable pointer, entrypoint, inputs, outputs, tests and tags needed by a later AI
agent to find and reuse it without copying or rewriting it.

## Required workflow

1. Search before writing code:

   ```bash
   python3 .codex/hooks/automation_registry.py search "<task keywords>"
   ```

2. Record `REUSE_EXISTING`, `WRITE_SCRIPT`, or `MANUAL` in
   `decision_log.jsonl` in the same commit that closes the task.
3. For `REUSE_EXISTING` and `WRITE_SCRIPT`, reference at least one cataloged
   `artifact_id` and record the exact verification performed.
4. Add or update catalog entries when reusable code is introduced, moved,
   retired, or its test command changes.
5. Validate before commit:

   ```bash
   python3 .codex/hooks/automation_registry.py validate
   ```

The validator is read-only. A valid record does not prove that a test passed;
the `verification` field must name the observed test/check, and Git history is
the authoritative commit evidence.

## Schemas

Every artifact contains `artifact_id`, `name`, `path`, `purpose`, `entrypoint`,
`inputs`, `outputs`, `tests`, `test_command`, `status`, and `tags`.

Every decision contains `decision_id`, `task_id`, `decided_at`, `recorded_at`,
`mode`, `reason`, `artifact_ids`, and `verification`. Timestamps use RFC 3339
with a known timezone. A later decision may supersede an earlier decision for
the same task by adding `supersedes_decision_id`; both lines remain immutable.
