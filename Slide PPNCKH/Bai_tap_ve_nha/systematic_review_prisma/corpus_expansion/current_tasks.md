# Current research tasks

Updated_at: 2026-11-26T08:00:01+07:00

This queue records accepted work boundaries, not
provider transport alone. Codex owns writing, acceptance, project edits, and Git.
Gemini 3.8 Flash is the primary read-only research worker; the confined
`gpt-5.6-luna`/low fallback is permitted only for recognized provider quota.

Canonical execution workspace: `/Volumes/JokerData/PhD/PhD Research Proposal -
Nguyen Minh Hieu (2026) (v3)` on `main`. The split-brain migration was promoted
through merge `5cde697`; 92/92 evidence checksums pass, 46/46 manifest records
resolve, and Batch 04 correction 02 is accepted; earlier outputs remain rejected. The user authorized a path-scoped
clean-tree policy: residue in the project, repository `.codex/`, or repository
`AGENTS.md` blocks A2A, while the authorized 51-entry external baseline is preserved
without blocking dispatch.

## Active queue

| Package | Records | Status | Accepted evidence | Next action |
|---|---:|---|---|---|
| Screening batch 01 | S01-S06 | accepted working screening | 5 INCLUDE, 1 EXCLUDE; gate `screening_46/reviews/batch_01_combined_gate.md`; commit `531a54e` | Preserve; reconcile versions/study families later |
| Screening batch 02 | S07-S12 | accepted working screening | 6 INCLUDE; 48/48 source-page checks; gate `screening_46/reviews/batch_02_combined_gate.md`; commit `c3c6c08` | Preserve; reconcile versions/study families later |
| Screening batch 03 | S13-S18 | accepted working screening | 6 INCLUDE; 48/48 batch locators plus 30/30 S16 correction locators; gate `screening_46/reviews/batch_03_combined_gate.md`; commit `fc8944f` | Preserve S16 version limits; reconcile later |
| Screening batch 04 | S19-S20, C01-C04 | accepted working screening, correction 02 | 3 INCLUDE, 3 UNCERTAIN; 48/48 locators; `screening_46/reviews/batch_04_correction_02_review.md` | Preserve uncertainty; proceed to batch 05 after commit/merge/cleanup |
| Timestamp standardization | logs/status/hooks | completed and merged at `1f04299` | requested_at 2026-11-25T23:02:44+07:00; 17 gate tests + 18 skill-router tests PASS | Preserve timestamp checks in every subsequent task |
| Screening batch 05 | C05-C10 | accepted working screening with targeted correction | 1 INCLUDE, 5 UNCERTAIN; 48/48 combined locators; `screening_46/reviews/batch_05_correction_review.md` | Preserve unresolved dates/version/scope; batch 06 next after commit/merge/cleanup |
| Screening batch 06 | C11-C16 | accepted working screening | 4 INCLUDE, 2 UNCERTAIN; 48/48 locators; `screening_46/reviews/batch_06_review.md` | Preserve dates/roles/families; batch 07 after commit/merge/cleanup |
| Screening batch 07 | C17-C21 | retry accepted working screening | 3 INCLUDE, 1 EXCLUDE, 1 UNCERTAIN; 40/40 locators; `screening_46/reviews/batch_07_retry_review.md` | Preserve failed primary; batch 08 after commit/merge/cleanup |
| Consolidation | 46 reports | completed working ledger | 46 source-identical records; 136 unresolved occurrences; `screening_46/consolidated/validation.md` | Commit brief for nine dates and C08 identity/version |
| Screening batch 08 | C22-C25, SNCS | correction accepted working screening | 4 INCLUDE, 1 UNCERTAIN; 32 corrected / 40 combined locators; `screening_46/reviews/batch_08_correction_review.md` | Consolidate 46-report ledger, then reconcile |

## Reconciliation next task

Scope correction is rejected and quarantined. Gemini primary
`01a21556-4587-7524-8edb-d2d9ec56465d` returned only quota; approved router used
fixed gpt-5.6-luna/low fallback `01a21559-eec5-7109-9445-388ddba4e2e1`.
Fallback corrects3 semantic issues but passes only17/20 quote locators; A2/C1 FAIL.
Reviews: `screening_46/reconciliation/reviews/scope_01_correction_review.md` and
`scope_01_correction_primary_review.md`. After commit/merge/cleanup, prepare a
small correction for exactly C06_E4,SNCS_E2,SNCS_E3 (no other edits); then recheck
combined20 quotes and full gate. No active provider task. Overlay stays36/2/8.
Decision: `reconciliation-scope-01-correction-v1`, REUSE_EXISTING.

## Measured progress

- Frozen retrieval inventory: 46 reports.
- Accepted working full-text screening: 46/46 reports.
- Working decisions: 32 INCLUDE, 2 EXCLUDE, 12 UNCERTAIN in batches 01-08.
- Remaining in this campaign: 0 reports.
- Existing scope_01 provider task: completed, rejected A2/A4; no active provider task.
- Batch 08 correction accepted; all C1–C6 PASS; 5 combined working decisions.
- Batch 04 dispatch count: 1 primary and 2 corrections; accepted-result count 1.
- Latest Batch 04 mandatory failures: 0; all C1–C6 PASS.
- Manuscript changes from batches 01-08: zero.
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

The canonical `main` checkout retains the original 50 pre-existing, out-of-project dirty
status entries plus the user-authorized .gitignore change (51 current entries). They are user-owned: do
not reset, stash, clean, delete, or overwrite them. The project itself is
integrated; all agents must work from the root checkout after migration cleanup.
The authorized hook checks only this project, repository `.codex/`, and
repository `AGENTS.md`; those scopes must be clean before dispatch. The external
baseline is not permission to create new residue outside the owned scopes.


## Historical concurrent baseline update

User confirmed preservation of the concurrent root .gitignore addition (*.json); it is outside this task. Original 50 entries remain unchanged. Current authorized external status: 51 entries, SHA-256 18f05fa66cb8057d1db255731324438c0519d98b9f09d55991c1b538787105f3.

## Current Git baseline

External baseline committed at `643f8ed`; canonical repository verified fully
clean (zero status entries). The previous 51-entry baseline is historical.
Correction brief is ready; route only after this task closes.

<!-- HK261_TASK_STATE
{
  "task_id": "reconciliation-scope-01-correction",
  "status": "rejected",
  "started_at": "2026-11-26T07:51:45+07:00",
  "updated_at": "2026-11-26T08:00:01+07:00",
  "completed_at": "2026-11-26T08:00:01+07:00"
}
-->
