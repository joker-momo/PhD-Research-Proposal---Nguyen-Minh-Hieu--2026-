# Session Handoff Template

Do not create another current-state document. Update `current_state.json`,
append one matching event to `events.jsonl`, and append the task's final
decision to `../automation/decision_log.jsonl` in the same commit.

Required `current_state.json` task fields:

```json
{
  "task_id": "task-name",
  "owner": "CODEX_WRITING",
  "status": "completed",
  "started_at": "RFC3339-with-timezone",
  "updated_at": "RFC3339-with-timezone",
  "completed_at": "RFC3339-with-timezone",
  "decision_id": "task-name-v1"
}
```

Also update `next_task`, current evidence counts, blockers and user
confirmations only when they changed. Validate:

```bash
python3 .codex/hooks/project_state.py validate
python3 .codex/hooks/automation_registry.py validate
```

For a human summary run `python3 .codex/hooks/project_state.py show`; do not
commit that output as a second source of truth. A session note may exist for a
material investigation, but it must point to the canonical state, objective
PASS/FAIL evidence, changed paths, tests, commit SHA and next measurable action.
