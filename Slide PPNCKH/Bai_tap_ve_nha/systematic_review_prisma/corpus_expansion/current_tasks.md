# Current Research Queue Compatibility Pointer

The canonical current task and next research task are stored once in
`../MUST_READ_AI_AGENT/current_state.json`. Render the human-readable snapshot
with:

```bash
python3 .codex/hooks/project_state.py show
```

The full pre-migration queue is preserved at
`history/current_tasks.pre-state-v1.2026-11-26.md`. Accepted research evidence
continues to live in its dated result and review artifacts; this pointer is not
an evidence ledger.
