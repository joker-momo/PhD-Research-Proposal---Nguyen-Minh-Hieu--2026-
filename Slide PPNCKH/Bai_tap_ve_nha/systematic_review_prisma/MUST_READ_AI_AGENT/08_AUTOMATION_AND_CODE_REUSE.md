# Automation Evidence and Code Reuse

Every agent must search the existing automation registry before writing new
code for an HK261 task:

```bash
python3 .codex/hooks/automation_registry.py search "<task keywords>"
```

The canonical store is `../automation/`:

- `artifact_catalog.json` tells an agent where reusable code lives, what it
  does, how to invoke it, its inputs/outputs, and which tests verify it.
- `decision_log.jsonl` is append-only evidence of each task's
  `REUSE_EXISTING`, `WRITE_SCRIPT`, or `MANUAL` decision.
- `README.md` defines both schemas and the update workflow.

## Completion gate

A task-closing commit must append one active decision for its `task_id`.
`REUSE_EXISTING` and `WRITE_SCRIPT` require one or more cataloged artifact IDs
and concrete verification evidence. `MANUAL` may use an empty artifact list but
must still record verification and explain why automation was unsuitable.

When a decision changes, append a new record with
`supersedes_decision_id`. Never rewrite or delete the earlier record. Register
new reusable code in the catalog in the same task commit. Git history supplies
the immutable commit SHA and diff; the registry supplies discovery and the
semantic link between task, decision, code and test evidence.

Before commit, run:

```bash
python3 .codex/hooks/automation_registry.py validate
```

The task gate checks the registry before recognized A2A dispatch. Hooks remain
an additional guardrail, so agents must enforce the registry workflow manually
even when hook activation is unavailable.

Do not store credentials, tokens, copied third-party proprietary code, generated
build output, or one-off scratch files in the catalog. Retired code remains in
Git history; mark its catalog status `retired` and point agents to its supported
replacement when one exists.
