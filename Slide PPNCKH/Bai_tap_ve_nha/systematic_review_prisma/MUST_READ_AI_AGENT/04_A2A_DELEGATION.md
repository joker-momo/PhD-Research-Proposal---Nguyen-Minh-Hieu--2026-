# A2A Delegation

## Ownership

Codex owns all writing, editing, acceptance, project files, Git, and final
user-facing communication. A research agent may return structured evidence only.

## Gemini.app route for the approved restart plan

Use Gemini.app Task mode through the existing native bridge. Use the approved
project folder and identify the exact files in the brief. Maintain a stable
message ID from the committed phase manifest. Execute one literal `bridge send`
per tool call with an absolute `--brief` path inside the active HK261
worktree and the committed `--message-id`. Before sending, check that the
approved folder exposes the required committed inputs.

The phase setup or preceding review commit must include `current_state.json`
and its matching event. Use these fields:

- `task.checkpoint_path`: project-relative path to the phase manifest (setup)
  or the previous batch's PASS/FAIL review. Commit the named file with state.
- `next_task.status`: `ready` and `next_task.owner`: `GEMINI_RESEARCH`.
- `next_task.dispatch_brief`: project-relative path to the committed brief.
- `next_task.message_id`: the exact stable ID used in the bridge call.

Read an existing task with `bridge get TASK_ID`. If the initial receipt was
lost, recover it using the same command and identical arguments and message
ID. A new ID is reserved for a newly authorized batch or linked correction.
Append the actual task/context identifiers and timestamps with the review.

## Legacy router

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

## Dispatch precondition and ownership persistence

Before dispatch, publish TASK, OWNER, OWNED_PATHS, BINARY_ACCEPTANCE, and
PRE_TASK_GIT_STATUS, following `03_WORKFLOW_AND_GATES.md`. A dirty project
worktree blocks both `a2a-route` and direct `a2a send`; the latter remains
prohibited for ordinary research even when clean. Commit brief preparation
before dispatch. Inspect the research project's owned scopes before sending.

Codex owns all writing/editing, plans, documents, publication tables, project
mutations, acceptance, and Git. Gemini/fixed quota fallback owns research,
discovery, verification, extraction, comparison, classification, and structured
synthesis only. Do not silently switch research ownership after a failed result.
Do not dispatch a second batch while collecting/reviewing the first is uncommitted.

The root hook recognizes literal Gemini.app bridge and legacy dispatch;
it cannot guarantee detection of every indirect script, alias, interactive stdin,
remote/MCP route, or opted-out tool path. It also requires Codex hook trust.
Until runtime activation is verified, claim only the direct subprocess tests,
not that all dispatch is automatically blocked. See `.codex/hooks/README.md` at
the repository root. The agent must independently enforce the same gate.

## Timestamp evidence before dispatch

Apply the timestamp rule in `03_WORKFLOW_AND_GATES.md`: validate
`current_state.json` and its matching latest event. Record actual provider
start/completion times and task/context IDs. A completed provider event is not
an acceptance event; give Codex review its own observed timestamp.
