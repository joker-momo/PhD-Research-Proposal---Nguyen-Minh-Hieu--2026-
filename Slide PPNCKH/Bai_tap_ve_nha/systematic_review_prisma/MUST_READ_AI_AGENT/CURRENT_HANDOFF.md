# Current Handoff

**Snapshot date:** 25 November 2026

**State through commit:** `fc8944f3240441b927532fcb6623c9e85e3ca571`

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
- Progress: 18/46 reports reviewed through an accepted working gate; 17 INCLUDE,
  1 EXCLUDE, 28 not yet screened in this campaign.
- Batch 04 has not been dispatched. No research task is currently active.
- These working decisions are not final human adjudication, unique-study counts,
  final PRISMA arithmetic, or permission to change manuscript conclusions.

## Evidence accepted versus quarantined

- Usable working evidence: only the three accepted derivative batch files and
  their combined PASS gates.
- Quarantined but retained for audit: original rejected batch outputs, rejected
  corrections, provider raw JSON, and any result without a complete Codex PASS
  table.
- No working-screening result may enter synthesis until report versions,
  study-family overlap, extraction, appraisal, and database reconciliation are
  completed for the applicable evidence.

## Critical unresolved work

1. Screen batches 04-08 serially with one committed brief/result/review task at a
   time and a clean-tree gate between tasks.
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

- The research worktree stopped clean at `fc8944f`; the main thread was idle and
  batch 04 was not dispatched when this snapshot task began.
- Status synchronization runs on its own task branch/worktree. The status guard
  blocks recognized A2A dispatch when either Git is dirty or the latest project
  commit is newer than `CURRENT_HANDOFF.md` and `current_tasks.md`.
- Automatic hook activation remains unverified in the Codex runtime; manual
  clean-tree and freshness checks remain mandatory.
- Integration into `main` is not yet safe: the primary `main` checkout contains
  pre-existing user modifications and many untracked project files, and `main`
  also has a unique CodeGraph commit. Do not reset, stash, delete, or overwrite
  that baseline. Reconcile it explicitly before fast-forward integration.

## Current submission verdict

**NOT READY and NOT SUBMITTED.** A successful build or accepted interim batch
does not satisfy research, author-approval, portal, or course-evidence gates.

## User confirmation required

- Resolution of the pre-existing dirty `main` checkout before the accumulated
  research branch can be integrated and removed safely.
- Later: author metadata/approval, verified HCMUT email and student ID, exact
  examination date, declarations, and explicit authorization for submission and
  email forwarding.

## Next exact action

After this status-synchronization task is committed and the integration baseline
is resolved, prepare/verify the batch 04 task boundary and dispatch only when:

1. the active worktree is clean;
2. `CURRENT_HANDOFF.md` and `current_tasks.md` are fresh at the latest project
   commit;
3. the five pre-task fields are published; and
4. batch 04's committed brief has measurable acceptance criteria.
