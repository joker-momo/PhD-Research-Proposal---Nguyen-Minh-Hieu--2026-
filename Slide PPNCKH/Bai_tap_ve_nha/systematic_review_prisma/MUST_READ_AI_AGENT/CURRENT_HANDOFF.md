# Current Handoff

**Snapshot date:** 25 November 2026

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
- Progress: 18/46 reports reviewed through an accepted working gate; 17 INCLUDE,
  1 EXCLUDE, 28 not yet screened in this campaign.
- Batch 04 has not been dispatched. Its committed brief passed the objective
  input/contract gate in `screening_46/reviews/batch_04_brief_gate.md`: 5/5
  headings, 6/6 IDs, 18/18 locators, and 6/6 PDF/checksum checks. No research
  task is currently active.
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
  50/50 porcelain-status entries match the Task 1 snapshot. Do not reset, stash,
  clean, delete, or overwrite them.
- The user authorized a baseline-aware status guard. It blocks recognized A2A
  dispatch when Git residue exists in this project, repository `.codex/`, or
  repository `AGENTS.md`, or when the latest project commit is newer than
  `CURRENT_HANDOFF.md` and `current_tasks.md`. It does not hardcode a porcelain
  count or treat the exact preserved external baseline as task residue.
- Automatic hook activation remains unverified in the Codex runtime; manual
  clean-tree and freshness checks remain mandatory.
- Batch 04 remains undispatched and no research provider task is active. The
  clean-tree policy blocker is resolved and the Batch 04 brief gate is PASS.
  `scripts/run_screening_batches.py` now uses the same three owned scopes as the
  task gate; its baseline-aware unit tests cover all three Git states outside the
  scope and all three owned paths. Dispatch is ready after this task is committed,
  merged, and the clean/fresh gate passes on `main`.

## Current submission verdict

**NOT READY and NOT SUBMITTED.** A successful build or accepted interim batch
does not satisfy research, author-approval, portal, or course-evidence gates.

## User confirmation required

- Author metadata/approval, verified HCMUT email and student ID, exact
  examination date, declarations, and explicit authorization for submission and
  email forwarding.

## Next exact action

Dispatch Batch 04 when:

1. the path-scoped hook reports clean owned scopes;
2. `CURRENT_HANDOFF.md` and `current_tasks.md` are fresh at the latest project
   commit;
3. the five pre-task fields are published; and
4. batch 04's committed brief and brief gate remain byte-identical/PASS.
