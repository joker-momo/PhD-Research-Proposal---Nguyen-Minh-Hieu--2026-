# Session Handoff Template

Use this structure at the end of every material work session. Update
`CURRENT_HANDOFF.md` when project-level status, canonical paths, counts, blockers,
or next actions changed.

```markdown
# Session handoff

Timestamp:
Agent/model:
Task:
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
