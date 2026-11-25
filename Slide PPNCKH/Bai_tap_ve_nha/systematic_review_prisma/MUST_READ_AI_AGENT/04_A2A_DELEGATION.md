# A2A Delegation

## Ownership

Codex owns all writing, editing, acceptance, project files, Git, and final
user-facing communication. A research agent may return structured evidence only.

## Required route

Do not use raw `a2a send` for ordinary project research. Use the verified router
in `/Users/joker/.config/a2a-cli/agents/gemini-research`.

First resolve the current primary URL:

```bash
rtk a2a-serve status \
  --dir /Users/joker/.config/a2a-cli/agents/gemini-research \
  --url
```

Then dispatch the validated brief:

```bash
rtk /Users/joker/.config/a2a-cli/agents/gemini-research/scripts/a2a-route \
  --brief /absolute/path/to/brief.md \
  --project a2a-continuity \
  --primary-agent-url http://127.0.0.1:51698 \
  --wait-timeout 10m
```

Replace the example primary URL with the resolved value. Do not redispatch merely
because a monitoring call timed out; resume the existing task by ID.

## Routing contract

- Primary: configured Gemini 3.8 Flash research agent.
- Fallback: fixed `gpt-5.6-luna`, reasoning effort `low`, web search enabled,
  read-only sandbox, approval `never`, ephemeral execution, response storage
  disabled.
- Fallback is authorized only for a recognized provider-quota notice, including
  Gemini's known case where the transport says `TASK_STATE_COMPLETED` but the
  artifact contains its standard quota message.
- No fallback for network errors, schema errors, ordinary task failure, poor
  evidence, or a failed review gate.
- No automatic model or effort escalation.
- Reconcile with targeted `task get` by task ID. Do not rely on `task list` for
  the fallback endpoint and never read or mutate `server.db`.

## Mandatory brief

Before every delegated task, record all five headings:

1. `TASK`: one concrete research/synthesis task.
2. `REQUIRED WORK`: numbered atomic actions.
3. `REQUIRED OUTPUT`: exact JSON/schema/field structure.
4. `ACCEPTANCE CRITERIA`: binary or numeric tests.
5. `BOUNDARIES`: prohibited actions, source/date limits, and instructions to
   report missing evidence rather than invent it.

Unless inapplicable, require:

- exact requested record count or documented shortfall;
- source URL or supplied-file locator for every factual claim;
- title, authors, year, venue, and DOI or `DOI_NOT_FOUND` for each scholarly
  record;
- zero duplicates after DOI/title normalization;
- zero unsupported quantitative claims;
- explicit unresolved items.

Both primary and fallback receive the same validated brief. A read-only worker
must not be told to download or save project files; it returns lawful URLs and
evidence for Codex to handle.

## Review gate

After each result, Codex writes a criterion-by-criterion table containing
`PASS` or `FAIL` plus objective counts, missing fields, invalid dates,
duplicates, locators, and identifier failures. Use the result only if every
mandatory criterion passes. Otherwise send a linked corrective brief naming the
failed criteria. Never silently fill a substantial research gap.

Canonical A2A operating rules:

- `/Users/joker/.config/a2a-cli/agents/gemini-research/continuity/OPERATING_RULES.md`
- `/Users/joker/.config/a2a-cli/agents/gemini-research/continuity/CURRENT_STATE.md`
- `../corpus_expansion/a2a_routing_policy_2026-11-25.md`
