# Current Handoff

**updated_at:** 2026-11-26T08:02:12+07:00

**Goal version:** HK261-PRISMA-SNCS-v2; adopted_at: 2026-11-25T23:03:52+07:00.
The active goal is PRISMA 2020, SN Computer Science and official Springer Nature
LaTeX, continuing autonomously through evidence, search, reconciliation,
extraction/appraisal, synthesis, integrity, PDF validation and submission
preparation. Submission and email require all gates plus explicit authorization.

**State through promotion commit:** `5cde6977766c8c083b7e2cb039b862aa8b4d4695`.
The final handoff commit is the latest commit touching this file; resolve it with
`git log -1 --format=%H -- MUST_READ_AI_AGENT/CURRENT_HANDOFF.md`.

**Authority:** current navigation summary. Git history and accepted review gates
remain the evidence record. If this file conflicts with a canonical artifact,
stop and reconcile the conflict before starting or delegating another task.

## Accepted current state

- Active target: SN Computer Science.
- Canonical manuscript: `manuscript/sn_computer_science/main.tex` and
  `references.bib`; the PDF is compiled from LaTeX. Word is historical.
- Canonical manuscript dataset remains 27 assessed reports = 24 included + 1
  excluded + 2 uncertain. The full-corpus screening below has not yet been
  reconciled into this dataset or manuscript.
- Current manuscript snapshot remains 17 pages and 34 cited references.
- Current consistent nine-domain snapshot remains 216 judgments = 100 yes +
  110 partial + 6 no. Domain 9 aggregate is withheld pending reassessment.
- Formal database identification, final PRISMA reconciliation, human
  adjudication, and submission gates remain incomplete.
- Gemini 3.8 Flash is the primary read-only research worker. Recognized provider
  quota may route the unchanged brief to the confined `gpt-5.6-luna`/low
  fallback. Codex remains the acceptance and Git authority.

## Full-corpus screening checkpoint

- Frozen intake: 46 supplied reports, S01-S20, C01-C25, and SNCS. This is a
  retrieval inventory, not an eligible-study count.
- Batch 01, S01-S06: accepted working screening, 5 INCLUDE + 1 EXCLUDE (S03
  demo). Combined gate: `screening_46/reviews/batch_01_combined_gate.md`.
  Acceptance commit: `531a54e`.
- Batch 02, S07-S12: accepted working screening, 6 INCLUDE. Combined gate:
  `screening_46/reviews/batch_02_combined_gate.md`. Acceptance commit:
  `c3c6c08`.
- Batch 03, S13-S18: accepted working screening, 6 INCLUDE. S16 has a verified
  published identity, while numerical/content equivalence between the supplied
  author copy and Version of Record is not assumed. Combined gate:
  `screening_46/reviews/batch_03_combined_gate.md`. Acceptance commit:
  `fc8944f`.
- Batch 04, S19-S20/C01-C04: accepted working screening from correction 02,
  3 INCLUDE + 3 UNCERTAIN. Task `01a21380-a2ee-78e9-a775-c310e8dc9541`;
  gate `screening_46/reviews/batch_04_correction_02_review.md`, 48/48 locators.
  Primary and first correction remain rejected; the accepted replacement fixes
  C03's analytical-eligibility interpretation while retaining date uncertainty.
- Batch 05, C05–C10: accepted working screening using the targeted C06/C08
  correction and four unchanged primary records. Gate:
  `screening_46/reviews/batch_05_correction_review.md`; 16/16 corrected and
  48/48 combined locators; 1 INCLUDE + 5 UNCERTAIN.
- Batch 06, C11–C16: accepted working screening, 4 INCLUDE + 2 UNCERTAIN.
  Gate `screening_46/reviews/batch_06_review.md`; 48/48 locators. C13/C14
  publication dates remain unresolved; C11 relay and C16 jammer roles bounded.
- Batch 07 retry, C17–C21: accepted working screening, 3 INCLUDE, 1 EXCLUDE
  (C18 generic DAG workload), 1 UNCERTAIN (C19 date). Gate
  `screening_46/reviews/batch_07_retry_review.md`; 40/40 locators.
  Failed primary preserved at `800a2ff`; retry adopted separately.
- Batch 08 correction accepted: 4 INCLUDE + 1 UNCERTAIN (SNCS scope).
  Gate `screening_46/reviews/batch_08_correction_review.md`; corrected 32/32
  and combined 40/40 quotes. Primary remains rejected and preserved.
- Progress: 46/46 reports through an accepted working gate; 32 INCLUDE,
  2 EXCLUDE, 12 UNCERTAIN; 0 unscreened in this frozen intake.
  No provider task is active.
- These working decisions are not final human adjudication, unique-study counts,
  final PRISMA arithmetic, or permission to change manuscript conclusions.

## Evidence accepted versus quarantined

- Usable working evidence: only the eight accepted derivative batch files and
  their combined PASS gates.
- Quarantined but retained for audit: original rejected batch outputs, rejected
  corrections, provider raw JSON, and any result without a complete Codex PASS
  table.
- No working-screening result may enter synthesis until report versions,
  study-family overlap, extraction, appraisal, and database reconciliation are
  completed for the applicable evidence.

## Critical unresolved work

1. The 46-report consolidation is complete; next prepare the committed
   identity/date/version reconciliation brief. Timestamp
   standardization is merged at `1f04299` (35/35 tests PASS).
2. Reconcile all accepted working decisions with report versions, study families,
   the canonical 27-report dataset, extraction, and quality appraisal.
3. Execute/export/reconcile IEEE Xplore, ACM Digital Library, Scopus, and Web of
   Science searches with complete audit logs.
4. Resolve S19 publication type, C06 runtime-orchestration scope, the SNCS
   exclusion ledger, retractions, overlaps, and numerical-result provenance.
5. Update synthesis, manuscript, references, and PRISMA flow only from accepted,
   reconciled evidence; then rebuild and inspect the PDF.
6. Obtain verified author order, consent, HCMUT email, affiliations, identifiers,
   contributions, funding, conflicts, data availability, and AI disclosure.
7. Obtain the examination date; calculate the course deadline only after it is
   known.
8. Submit only after all gates pass; archive the manuscript ID/receipt and
   forward the required course evidence after explicit user authorization.

## Git and continuity state

- Canonical workspace: `/Volumes/JokerData/PhD/PhD Research Proposal - Nguyen
  Minh Hieu (2026) (v3)` on branch `main`. Codex, Antigravity, Claude, Grok, and
  any later agent must use this checkout; the former hidden research worktree is
  retired after the final review.
- The split histories were reconciled by non-force merge `5cde697`. The root
  checkout was promoted with `git merge --ff-only`; no user-owned sibling was
  moved, reset, stashed, or overwritten.
- The live project contains the portable evidence pack: 46 PDFs + 46 extracted
  texts, with 92/92 SHA-256 checks passing and all 46 manifest records resolving
  from project-relative locators.
- All 60 research-owned paths classified `KEEP_RESEARCH` but previously absent
  from the promoted root are preserved at their original relative paths and in
  the rollback pack; `migration/keep_research_preservation.tsv` records their
  hashes. This includes 13 ignored raw research transports.
- The six exact source versions cited by the canonical 27-report dataset now
  resolve under `sources/preserved_candidate_fulltext/`, including the C06 PMC
  HTML. The three local evidence files named by `formal_search_log_v0.2.csv`
  are restored under `sources/raw/` and `sources/normalized/`.
- Accepted Batch 01-03 derivatives remain byte-identical audit records. Eight
  embedded historical worktree locator occurrences map to four hash-verified
  canonical files through `migration/historical_locator_mapping.tsv`; do not
  rewrite the accepted JSON to modernize those historical strings.
- The refresh producer preserves every brief with a transport/result/review
  artifact, validates all undispatched brief inputs before metadata publication,
  and uses same-filesystem atomic replacement when recovering missing text.
- The obsolete live `sources/candidate_fulltext` symlink is absent. Its original
  tree and target evidence remain recoverable under
  `/Volumes/JokerData/PhD/HK261-reconciliation-backups/2026-11-25-split-brain/`;
  the exact live pre-promotion project is
  `root_project_live_before_promotion/`.
- The pre-existing root dirty baseline remains unchanged outside this project:
  the original 50 entries still match the Task 1 snapshot, with the authorized
  .gitignore addition making 51 current entries. Do not reset, stash,
  clean, delete, or overwrite them.
- The user authorized a baseline-aware status guard. It blocks recognized A2A
  dispatch when Git residue exists in this project, repository `.codex/`, or
  repository `AGENTS.md`, or when the latest project commit is newer than
  `CURRENT_HANDOFF.md` and `current_tasks.md`. It does not hardcode a porcelain
  count or treat the exact preserved external baseline as task residue.
- Automatic hook activation remains unverified in the Codex runtime; manual
  clean-tree and freshness checks remain mandatory.
- Batch 04 correction 02 is accepted as working screening; both earlier outputs
  remain rejected and retained. No research task is active.

## Current submission verdict

**NOT READY and NOT SUBMITTED.** A successful build or accepted interim batch
does not satisfy research, author-approval, portal, or course-evidence gates.

## User confirmation required

- Author metadata/approval, verified HCMUT email and student ID, exact
  examination date, declarations, and explicit authorization for submission and
  email forwarding.

## Next exact action

Three-locator corrective brief ready at
`screening_46/reconciliation/briefs/scope_01_locators.md`. After commit/merge/cleanup,
route once via Gemini-first router; quota-only fixed fallback remains permitted.
Return exactly C06_E4,SNCS_E2,SNCS_E3 plus2 unchanged source identities. Combine
only these3 evidence objects with preserved fallback and recheck all20 quotes,
original A1–A6/C1–C2 and new L1–L5. No other record data may change.
Parent `01a21559-eec5-7109-9445-388ddba4e2e1` remains rejected; no active provider.
Working overlay36/2/8 unchanged. Decision `reconciliation-scope-01-locators-brief-v1`
is MANUAL; deterministic heading/ID/schema assertions passed.

## Current bibliographic overlay

`screening_46/reconciliation/results/identity_dates_01_accepted.json` and
`identity_dates_01_screening_overlay.json` resolve S19,S20,C03,C08 at the working
gate. C1–C6 and A1–A6 PASS; primary result stays quarantined. Current report-level
working total: 36 INCLUDE / 2 EXCLUDE / 8 UNCERTAIN; base ledger remains immutable
at 32/2/12. Six IEEE dates remain uncertain; C06/SNCS scope remains uncertain.
Provider scope_01 completed and was rejected; correction pending. These are not final independent-study or PRISMA counts.

## Current Git baseline

The 51 external entries were committed separately at `643f8ed`; no HK261 path
changed in that cleanup. Canonical status was empty before this task. Historical
50/51-entry descriptions above describe the former baseline only; the current
baseline is zero entries, SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
The boundary hold has been released by the coordinating handoff.

<!-- HK261_TASK_STATE
{
  "task_id": "reconciliation-scope-01-locators-brief",
  "status": "completed",
  "started_at": "2026-11-26T08:02:12+07:00",
  "updated_at": "2026-11-26T08:02:12+07:00",
  "completed_at": "2026-11-26T08:02:12+07:00"
}
-->
