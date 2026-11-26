# Current Handoff Compatibility Pointer

The single canonical current-state record is `current_state.json`. Validate or
render it without loading historical handoff prose:

```bash
python3 .codex/hooks/project_state.py validate
python3 .codex/hooks/project_state.py show
```

Immutable progress history remains in `events.jsonl`,
`../automation/decision_log.jsonl`, and Git. The complete pre-migration handoff
is preserved at
`history/CURRENT_HANDOFF.pre-state-v1.2026-11-26.md`.

Do not copy current task metadata back into this file. Update
`current_state.json`, append one event and append the code-first decision in the
same task-closing commit.
