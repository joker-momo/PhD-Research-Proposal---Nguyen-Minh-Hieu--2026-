# Batch 05 primary review

Task ID: 01a214da-74a9-74ab-a88f-449c80dc162d
Context ID: 01a214da-74aa-7975-88c9-8994a83eee30
Reviewer: Codex
Reviewed at: 2026-11-26T05:48:14+07:00
started_at: 2026-11-26T05:36:31+07:00
updated_at: 2026-11-26T05:48:14+07:00
completed_at: 2026-11-26T05:48:14+07:00

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| A1 exact records | yes | PASS | 6/6 required IDs; shortfall 0; duplicate IDs 0 |
| A2 identity/schema | yes | PASS | Identity fields and nonempty reasons 6/6; normalized DOI/title duplicates 0; duplicate authors 0; C08 explicitly marked preprint/DOI_NOT_FOUND with unverified journal lookup recorded as unresolved |
| A3 located evidence/quote format | yes | FAIL | 48/48 page/quote matches and 0 mechanical errors, but only 47/48 quotes meet 10–45 words: C08 date_window is 5 whitespace-delimited words. This is a brief-format failure, not a false date |
| A4 protocol-consistent decisions | yes | FAIL | Mechanical truth-table errors 0, but 2 semantic issues: C06 does not distinguish main three-UAV setup from single-UAV baseline ablations; C08 invokes preprint eligibility without establishing protocol 4.1(7)'s unique-recent-evidence condition or verified publication linkage |
| A5 bounded classification | yes | PASS | Located classifications 6/6; physical fleet claims 0; percentage-improvement extraction 0; single-drone physical checks remain separate from multi-drone simulation/emulation |
| A6 date/ownership/uncertainty | yes | PASS | Four UNCERTAIN records explicit; C07/C08 proposed INCLUDE dates within window; unresolved arrays 6/6; declared project mutations 0; manuscript prose 0 |

Verdict: **REJECTED_A3_A4**. No Batch 05 decision is adopted. Accepted progress
remains 24/46 reports: 20 INCLUDE, 1 EXCLUDE, 3 UNCERTAIN.

## Targeted corrections

1. C06: re-read Section 5.1, p. 15 (three UAVs, four terminals per UAV), the main
   Section 5.2 results and single-UAV Only-A3C/Only-PPO ablations on pp. 20–21.
   Page 21 explicitly introduces a separate Only-PPO experiment. A single-UAV
   ablation does not itself contradict a multi-UAV main setup. Reassess the two
   uncertain gates and primary reason using the complete experimental hierarchy;
   if uncertainty remains, name the missing main-evaluation fact rather than
   treating the baseline configuration as the whole study. This does not order
   an INCLUDE outcome or amend the scope.
2. C08: protocol 4.1(7) permits preprints only for unique recent evidence. The
   supplied PDF identifies arXiv:2412.20860v2, dated 24 April 2025, but does not
   establish its relationship to the input journal DOI. Do not assume peer review
   or the preprint exception. Reassess primary_full_report/decision and retain
   unresolved version linkage unless supplied evidence resolves it.
3. C08 date quote: retain its accurate five-word date stamp. The corrective
   brief may explicitly allow a shorter isolated date stamp (up to 45 words),
   recording this as an output-format clarification; never manufacture a longer
   quote by joining noncontiguous source text. The original brief remains failed.

The follow-up should return exactly two complete corrected records (C06,C08)
with 16 identity/alignment/gate evidence blocks, linked to this task. Four other
records remain preserved but unadopted until the combined six-record gate passes.
No manuscript, protocol, inclusion count or final PRISMA arithmetic changes.
