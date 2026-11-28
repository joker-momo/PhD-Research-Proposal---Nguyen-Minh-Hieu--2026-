@/Users/joker/.codex/RTK.md

# HK261 PRISMA agent contract

Read
`Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md`,
then the manifest core and matching route. Keep HK261 separate from the
dissertation roadmap.

Before each new task, publish exactly:

```text
TASK: one concrete task
OWNER: CODEX_WRITING or GEMINI_RESEARCH
OWNED_PATHS: explicit paths
BINARY_ACCEPTANCE: countable or binary checks
PRE_TASK_GIT_STATUS: branch, staged/modified/untracked counts, preceding commit
CODE_FIRST_DECISION: REUSE_EXISTING | WRITE_SCRIPT | MANUAL -- one sentence
```

## Git workflow and user approval

1. **B1 — Check Git before starting.** Record the branch and HEAD. Check
   `git status --short`, the unstaged diff, and the staged diff. Start only
   with zero staged, unstaged, or untracked changes. If any exist, warn the
   user and pause. Preserve existing work.
2. **B2 — Isolate the task.** Create a new, descriptively named branch and a
   separate worktree from the current committed main branch.
3. **B3 — Make and commit the change.** Edit only the agreed scope, stage
   explicit paths, audit the diff for leftovers and secrets, and run relevant
   checks. Use descriptive commit subjects that state the action and affected
   area. Add a commit body when needed to explain the reason or provenance.
   For Gemini.app phases, keep setup and batch checkpoints on the phase branch.
4. **B4 — Request approval.** Show the user the branch, commit ID, change
   summary, and verification results. Wait for explicit approval of that
   revision before merging into main.
5. **B5 — Revise when requested.** Return to B3 on the same branch and worktree.
   Commit the revisions with a descriptive message, then repeat B4. Approval
   applies to the revision shown to the user.
6. **B6 — Audit, integrate, and clean up after approval.** Review every changed
   file and check both worktrees. Remove only confirmed task leftovers. Commit
   cleanup and rerun affected checks. If cleanup or integration preparation
   changes the approved deliverables, repeat B4. Use a fast-forward-only
   merge when possible. If main has diverged, preserve both histories and
   resolve integration safely on the task branch. Verify the integrated
   result and confirm the approved commits are reachable from main before
   removing the clean task worktree and deleting the merged branch without
   force. Confirm main is clean and report the integrated commit ID.

Advance an HK261 phase only after its acceptance gate and B4 approval pass.

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
it at phase setup, batch acceptance/rejection and phase completion, and append
a matching event to `events.jsonl`. Keep the active decision ID consistent.
Save each Gemini.app bridge receipt with its batch review. Validate with
`python3 .codex/hooks/project_state.py validate`; render with `... show`.
`CURRENT_HANDOFF.md` and `corpus_expansion/current_tasks.md` are compatibility
pointers, not independent state. Git, events and decisions preserve history.

Use RFC 3339 seconds with a known timezone, normally `+07:00`. Record
`started_at`, `updated_at`, and `completed_at` for completed/rejected work. Do
not invent historical times. The latest event must match the current task and
state `updated_at`.

## Ownership and A2A

Codex owns writing/editing, project files, acceptance, Git and final text.
Gemini through the approved Gemini.app bridge or legacy router owns read-only
research, discovery, extraction, verification, classification and structured
synthesis. Each brief must contain TASK, REQUIRED WORK, REQUIRED OUTPUT,
ACCEPTANCE CRITERIA and BOUNDARIES with numeric/binary checks. Codex must issue
a criterion-by-criterion PASS/FAIL review; use research only when every
mandatory criterion passes.
Use the mandatory no-fabrication clause and independent source verification
in HK261's `MUST_READ_AI_AGENT/04_A2A_DELEGATION.md`.
For Gemini.app, commit the brief first and authorize only the next batch in
canonical state. Use the checkpoint fields in the delegation rules.

## Skills and hooks

The advisory router selects at most one primary and two non-overlapping support
skills; an explicitly named installed skill wins. Read every selected
`SKILL.md` completely. Do not co-load equivalent pipelines. Lawful retrieval
priority is `paper-lookup` -> `lawful-paper-pdf-retriever` ->
`nature-downloader`; never auto-select unauthorized retrieval.

Hooks are guardrails, not a security boundary. Live activation remains
unverified, so manually enforce this contract. Hook details and tiered test
commands live in `.codex/hooks/README.md`.
