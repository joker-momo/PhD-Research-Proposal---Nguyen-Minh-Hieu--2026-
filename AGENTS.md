@/Users/joker/.codex/RTK.md

# HK261 worktree entry point

For HK261/PRISMA work, first read
`Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md`
and every required file in its manifest. This applies after restart, compaction,
and model changes. Do not mix coursework with the dissertation roadmap.

Before EACH new task, publish exactly these five fields:
TASK: one concrete task
OWNER: CODEX_WRITING or GEMINI_RESEARCH
OWNED_PATHS: explicit paths
BINARY_ACCEPTANCE: countable or binary checks
PRE_TASK_GIT_STATUS: branch, staged/modified/untracked counts, preceding commit

Immediately after those five governance fields, publish exactly one separate
decision line:

`CODE_FIRST_DECISION: REUSE_EXISTING | WRITE_SCRIPT | MANUAL -- one-sentence reason`

For every task, evaluate execution in this order: (1) verify and reuse an
existing script/tool/API/CLI, (2) write or extend a small deterministic,
testable and reusable script, then (3) perform the work manually only when code
is unsafe, unavailable, dominated by human judgment/communication, or costs
more than the one-off task. Automate deterministic subtasks even when the
overall task remains manual. Do not write code merely to satisfy this rule or
build a framework for a one-off action. New automation must define inputs and
outputs, avoid secrets, handle errors explicitly, be idempotent where practical,
have focused tests, and be committed as a reusable project artifact. The
router's recommendation is advisory; the acting agent owns and records the
final decision.

Before writing code, search the durable registry with
`python3 .codex/hooks/automation_registry.py search "<task keywords>"`. The
task-closing commit must append the final decision and verification evidence to
`systematic_review_prisma/automation/decision_log.jsonl`. Every reused or newly
written code artifact must have an active entry in `artifact_catalog.json` with
its repository-relative path, entrypoint, inputs/outputs, tests and tags. A
changed decision is appended with `supersedes_decision_id`; never rewrite or
delete accepted history. Run `python3 .codex/hooks/automation_registry.py
validate` before commit. The current task state, event log and active code-first
decision must agree before recognized A2A dispatch.

Run Git status immediately before starting. Any staged, modified, or untracked
residue in `systematic_review_prisma/`, `.codex/`, or this `AGENTS.md` BLOCKS the
next task and any A2A dispatch. The exact pre-existing user-owned residue outside
those paths is an authorized baseline: preserve it and never add to, erase,
stash, or hide it. Finish, validate, inspect the diff, stage explicit owned
paths, and commit the current task first. Record its SHA and verify clean owned
scopes. Preparing a new brief is a Codex writing task: commit it before dispatch.

Codex owns all writing/editing, project files, acceptance reviews, Git, and final
text. Gemini via the approved A2A router owns research, discovery, extraction,
factual verification, classification, and structured evidence synthesis. A
research worker must not edit project files or write final prose. Each A2A brief
must have TASK, REQUIRED WORK, REQUIRED OUTPUT, ACCEPTANCE CRITERIA, BOUNDARIES.
Accept evidence only after a criterion-by-criterion PASS/FAIL review has all
mandatory criteria PASS. A correction is the same research task, with its brief
committed before retry. Never equate transport completion with acceptance.

Project hook configuration and verification limits: `.codex/hooks/README.md`.
Hooks are an additional guardrail; manually enforce these rules even if hooks
are untrusted, skipped, unavailable, or the tool path bypasses interception.

## Advisory skill router

On each user prompt, `.codex/hooks/skill_router.py` may suggest at most one
primary skill and two non-overlapping supporting skills. An explicitly named,
installed skill has first priority. If it reports `SKILLS: none`, continue with
the stated reason. The router is advisory and must never block uncertain input.

Before acting, read every selected `SKILL.md` completely at the printed
`READ_FULL_SKILL_MD` path. Do not treat the router output as proof that this was
done. `academic-pipeline` orchestrates academic work and must not be co-loaded
with an equivalent research pipeline. Research/discovery/verification remains
Gemini-owned through the approved A2A route; writing/editing remains Codex-owned.
For lawful paper retrieval, use `paper-lookup`, then
`lawful-paper-pdf-retriever`, then `nature-downloader`. Never automatically
select a retriever whose default flow includes unauthorized sources.

## Timestamp rule (user request: 2026-11-25T23:02:44+07:00)

Every new task/work record must have `started_at` and `updated_at`, plus
`completed_at` when completed or rejected. Every new event-log entry must have
`timestamp`. Use RFC 3339 with seconds and a known timezone, default
Asia/Ho_Chi_Minh (`+07:00`). Future timestamps, date-only values and relative
phrases are not valid event times. Planned deadlines belong in separate fields.
Never infer an unknown historical time; retain immutable raw/accepted history
and label missing historical time explicitly rather than rewriting provenance.

Keep exactly one `HK261_TASK_STATE` JSON comment block in each current handoff
and task queue. Both blocks must match: `task_id`, `status` (`active`, `completed`,
`rejected`, `blocked`), `started_at`, `updated_at`, and `completed_at` when finished.
Require started_at <= completed_at <= updated_at <= current time (omit the
completion comparison for unfinished work). Manifest `updated_at` and the last
`MUST_READ_AI_AGENT/events.jsonl` entry must match the current task's updated_at;
the last event task_id must also match. Append log entries, never overwrite them.
Update these artifacts in the same task commit. Use a fresh time for the actual
update; do not use a planned commit or dispatch time as an observed event.

The read-only gate blocks recognized A2A dispatch for invalid timestamps, in
addition to dirty owned scopes and stale status documents. Non-A2A commands
remain available to finish and repair the current task. Direct tests do not prove
live hook activation; manual enforcement remains mandatory.
