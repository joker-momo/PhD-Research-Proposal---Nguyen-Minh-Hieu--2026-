# Session Handoff Template

Use this structure at the end of every material work session. Update
`CURRENT_HANDOFF.md` when project-level status, canonical paths, counts, blockers,
or next actions changed.

```markdown
# Session handoff

started_at: [actual RFC 3339 time with timezone]
updated_at: [actual RFC 3339 time with timezone]
completed_at: [actual RFC 3339 time when finished; omit while active]
Agent/model:
Task:
Code-first decision: [REUSE_EXISTING | WRITE_SCRIPT | MANUAL -- reason]
Branch/worktree:

## Completed
- [Concrete output with path]

## Acceptance gate
| Criterion | PASS/FAIL | Objective evidence |
|---|---|---|

## Evidence used
- [Source/report ID, DOI, and file/page/table/section locator]

## Files changed
- [Path: reason]

## Verification performed
- [Command/check and observed result]
- [For REUSE_EXISTING: tool verification; for WRITE_SCRIPT: focused tests; for
  MANUAL: why automation was unsuitable and any automated substeps]

## Intentionally not changed
- [Out-of-scope path or decision]

## Unresolved and quarantined
- [Exact missing evidence or failed criterion]

## User confirmation required
- [Authorship, metadata, deadline, submission, or other decision]

## A2A continuity
- Primary task/context ID:
- Fallback task/context ID, if any:
- Review path and verdict:

## Git state
- Baseline pre-existing changes preserved:
- Agent-owned changes committed:
- Merge verification:
- Remaining agent-created branches/worktrees: 0

## Next exact action
1. [One measurable task with completion rule]
```

Never write “done”, “verified”, “ready”, or “submitted” without the concrete
evidence path and the gate that supports that status.

Copy the current task metadata into exactly one JSON comment block in both
CURRENT_HANDOFF.md and current_tasks.md (replace values with observed times):

```text
<!-- HK261_TASK_STATE
{"task_id":"task-name","status":"completed","started_at":"<RFC3339>","updated_at":"<RFC3339>","completed_at":"<RFC3339>"}
-->
```

Use the same updated_at in context_manifest.yaml and append one event with
`timestamp`, `task_id`, and `event` to events.jsonl. Actual time is required;
placeholders in this template must never enter current state. Historical unknown
timestamps remain explicitly unknown, never estimated as midnight.
