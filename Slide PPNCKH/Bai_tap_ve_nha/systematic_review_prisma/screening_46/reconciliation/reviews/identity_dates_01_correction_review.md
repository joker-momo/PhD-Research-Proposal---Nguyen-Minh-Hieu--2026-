# Identity/date correction — accepted working evidence

Task ID: 01a21534-cf0f-7825-81f1-c0a6a12a89cd
Context ID: 01a21534-cf11-7330-8722-9e61e8d15364
Parent task ID: 01a21521-896b-7bdf-8bcb-1b0cfda69f2f
Reviewer: Codex
Reviewed at: 2026-11-26T07:18:56+07:00
started_at: 2026-11-26T07:15:12+07:00
updated_at: 2026-11-26T07:18:56+07:00
completed_at: 2026-11-26T07:18:56+07:00

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| C1 bounded coverage | yes | PASS | 7/7 requested source IDs and 2/2 record IDs; parent correct; combined 10 records / 25 sources |
| C2 literal source quotes | yes | PASS | 7/7 corrected quotes match reported lines and PDF pages; lengths 13,23,23,23,12,23,23 words; combined local matches 10/10; timestamps valid |
| C3 bounded interpretation | yes | PASS | C03 content_equivalence=not_assumed; C08 unsupported title count removed; 0 unsupported equivalence/count assertions after correction |
| C4 preservation | yes | PASS | Only seven excerpts/locators plus correction check times, C03 equivalence/limitation and C08 limitation changed; all dates, decisions, identities and unresolved arrays unchanged |
| C5 original gate | yes | PASS | Original A1–A6 rechecked below; 4 INCLUDE + 6 UNCERTAIN remain working report proposals, not final human decisions |
| C6 ownership | yes | PASS | project_files_changed=0; final_prose_written=false; shortfall empty; no web/downloads or source mutations |
| A1 coverage/schema | yes | PASS | 10 requested unique records; 25 unique source IDs; original required fields preserved |
| A2 identities/attempts | yes | PASS | 10 complete identities, 24 recorded attempts; 10/10 independently retrieved Crossref metadata subsets match; normalized DOI/title duplicates 0 |
| A3 claim/source fidelity | yes | PASS | 10/10 local excerpts now match; corrected page/line ranges checked; 15 archived remote-source response hashes valid; 0 unsupported content-equivalence or title-count claims |
| A4 date/decision logic | yes | PASS | 4 source-supported date YES, 6 year-only UNCERTAIN; administrative dates not used as publication; technical gates unchanged |
| A5 C08 linkage | yes | PASS | Title/ordered authors/venue and arXiv acceptance comment support bibliographic linkage; missing DOI relation and unverified numerical parity retained; preprint uniqueness not established |
| A6 ownership/boundaries | yes | PASS | Original and correction declare 0 project mutations; 0 final prose; no new scope/family decisions |

Verdict: **ACCEPTED_WORKING_BIBLIOGRAPHIC_RECONCILIATION** for the explicit
combined derivative `../results/identity_dates_01_accepted.json` only. Primary
result remains rejected and immutable; correction never retroactively accepts it.

## Accepted scope and remaining limits

- S19/S20: deposited July 2026 publication month resolves date-window uncertainty;
  exact online day and S19 track/full-report concerns remain explicit.
- C03: publisher/Crossref publication evidence falls before cutoff; bibliographic
  match does not establish full-text or numerical equivalence.
- C08: journal identity is linked to the supplied author preprint; evidence remains
  tied to that local version. Do not claim verified Version of Record parity.
- C05/C09/C10/C13/C14/C19: six date verdicts remain UNCERTAIN. The new evidence
  does not authorize inventing an exact day or treating download stamps as dates.
- Report-level overlay gives 36 INCLUDE + 2 EXCLUDE + 8 UNCERTAIN across 46.
  C06 and SNCS remain scope-uncertain. Human adjudication, study-family mapping,
  formal searches, extraction, appraisal and manuscript synchronization remain.
- The 46-report base ledger remains immutable at 32/2/12; consume it with this
  dated overlay. No final study count or manuscript result is asserted.
