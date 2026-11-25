# Current research tasks

Updated 25 November 2026. This queue records accepted work boundaries, not
provider transport alone. Codex owns writing, acceptance, project edits, and Git.
Gemini 3.8 Flash is the primary read-only research worker; the confined
`gpt-5.6-luna`/low fallback is permitted only for recognized provider quota.

Canonical execution workspace: `/Volumes/JokerData/PhD/PhD Research Proposal -
Nguyen Minh Hieu (2026) (v3)` on `main`. The split-brain migration was promoted
through merge `5cde697`; 92/92 evidence checksums pass, 46/46 manifest records
resolve, and Batch 04 remains undispatched. The repository-wide clean-tree hook
currently blocks Batch 04 because the preserved root baseline has 50 status
entries; no A2A research task may start until the user resolves or explicitly
changes that policy.

## Active queue

| Package | Records | Status | Accepted evidence | Next action |
|---|---:|---|---|---|
| Screening batch 01 | S01-S06 | accepted working screening | 5 INCLUDE, 1 EXCLUDE; gate `screening_46/reviews/batch_01_combined_gate.md`; commit `531a54e` | Preserve; reconcile versions/study families later |
| Screening batch 02 | S07-S12 | accepted working screening | 6 INCLUDE; 48/48 source-page checks; gate `screening_46/reviews/batch_02_combined_gate.md`; commit `c3c6c08` | Preserve; reconcile versions/study families later |
| Screening batch 03 | S13-S18 | accepted working screening | 6 INCLUDE; 48/48 batch locators plus 30/30 S16 correction locators; gate `screening_46/reviews/batch_03_combined_gate.md`; commit `fc8944f` | Preserve S16 version limits; reconcile later |
| Screening batch 04 | S19-S20, C01-C04 | blocked; not dispatched | 0 accepted batch-04 decisions | Resolve/authorize the 50-entry root baseline policy, then rerun clean/fresh gate |
| Screening batch 05 | C05-C10 | not started | none | Wait for batch 04 commit and clean gate |
| Screening batch 06 | C11-C16 | not started | none | Wait for batch 05 commit and clean gate |
| Screening batch 07 | C17-C21 | not started | none | Wait for batch 06 commit and clean gate |
| Screening batch 08 | C22-C25, SNCS | not started | none | Wait for batch 07 commit and clean gate |

## Measured progress

- Frozen retrieval inventory: 46 reports.
- Accepted working full-text screening: 18/46 reports.
- Working decisions: 17 INCLUDE, 1 EXCLUDE, 0 UNCERTAIN in batches 01-03.
- Remaining in this campaign: 28 reports.
- Active A2A research task: none.
- Batch 04 dispatch count: zero.
- Batch 04 blocker count: 1 repository-wide clean-tree policy conflict.
- Manuscript changes from batches 01-03: zero.
- Accepted brief mutations from refresh tooling: zero; any batch with a
  transport, result, or review artifact is immutable to the producer.

These are report-level working decisions, not final eligible-study or PRISMA
counts. Final human adjudication, version/study-family reconciliation, formal
database searches, extraction/appraisal, and submission metadata remain separate
gates.

## Status-update rule

Every task-closing or task-changing commit must update both this file and
`MUST_READ_AI_AGENT/CURRENT_HANDOFF.md`. A clean worktree is insufficient when
these status documents are older than the latest project commit. Recognized A2A
dispatch is blocked until both conditions pass.

The canonical `main` checkout retains 50 pre-existing, out-of-project dirty
status entries exactly as snapshotted before migration. They are user-owned: do
not reset, stash, clean, delete, or overwrite them. The project itself is
integrated; all agents must work from the root checkout after migration cleanup.
The current hook examines the whole repository, not only agent-owned paths, so
those preserved entries block dispatch by design. Do not bypass the hook or
change its scope without explicit user authorization.
