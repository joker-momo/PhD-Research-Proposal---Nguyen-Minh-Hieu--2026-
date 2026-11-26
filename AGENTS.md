@/Users/joker/.codex/RTK.md

# HK261 PRISMA agent contract

For HK261 work, read
`Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md`,
then the manifest core and only the route matching the task. Do not mix this
coursework with the dissertation roadmap.

Before each new task, publish exactly:

```text
TASK: one concrete task
OWNER: CODEX_WRITING or GEMINI_RESEARCH
OWNED_PATHS: explicit paths
BINARY_ACCEPTANCE: countable or binary checks
PRE_TASK_GIT_STATUS: branch, staged/modified/untracked counts, preceding commit
CODE_FIRST_DECISION: REUSE_EXISTING | WRITE_SCRIPT | MANUAL -- one sentence
```

Run Git status first. Residue in this project, `.codex/`, or `AGENTS.md` blocks
new work and A2A dispatch. Preserve unrelated user work. Use a dedicated
branch/worktree, explicit staging, relevant tests, dead-code/secret/diff audit,
an atomic commit, fast-forward integration and branch/worktree cleanup. Never
start a second task before the first is committed and its owned scopes are clean.

## Code-first and durable evidence

Search before coding:
`python3 .codex/hooks/automation_registry.py search "<task keywords>"`.
Prefer a verified existing tool, then a small deterministic tested script, then
manual work only for unsafe, judgment-heavy or uneconomical automation. Do not
overengineer. Record the final decision in `automation/decision_log.jsonl`,
register reused/new code in `artifact_catalog.json`, and run
`python3 .codex/hooks/automation_registry.py validate` before commit. Logs are
append-only; supersede a decision instead of rewriting it.

## Current state and history

`MUST_READ_AI_AGENT/current_state.json` is the only current-state source. Update
it in every task-closing or task-changing commit, append one matching event to
`events.jsonl`, and keep the active decision ID consistent. Validate with
`python3 .codex/hooks/project_state.py validate`; render with `... show`.
`CURRENT_HANDOFF.md` and `corpus_expansion/current_tasks.md` are compatibility
pointers, not independent state. Git, events and decisions preserve history.

Use RFC 3339 seconds with a known timezone, normally `+07:00`. Record
`started_at`, `updated_at`, and `completed_at` for completed/rejected work. Do
not invent historical times. The latest event must match the current task and
state `updated_at`.

## Ownership and A2A

Codex owns writing/editing, project files, acceptance, Git and final text.
Gemini through the approved router owns read-only research, discovery,
extraction, verification, classification and structured synthesis. Each brief
must contain TASK, REQUIRED WORK, REQUIRED OUTPUT, ACCEPTANCE CRITERIA and
BOUNDARIES with numeric/binary checks. Codex must issue a criterion-by-criterion
PASS/FAIL review; use research only when every mandatory criterion passes.
Commit a brief before dispatch and a result/review before the next task.

## Skills and hooks

The advisory router selects at most one primary and two non-overlapping support
skills; an explicitly named installed skill wins. Read every selected
`SKILL.md` completely. Do not co-load equivalent pipelines. Lawful retrieval
priority is `paper-lookup` -> `lawful-paper-pdf-retriever` ->
`nature-downloader`; never auto-select unauthorized retrieval.

Hooks are guardrails, not a security boundary. Live activation remains
unverified, so manually enforce this contract. Hook details and tiered test
commands live in `.codex/hooks/README.md`.
