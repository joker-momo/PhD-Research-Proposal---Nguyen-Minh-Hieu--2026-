# S-01 corrected query-validation acceptance review

**Reviewed result:** `../s01_query_validation_corrected_result.json`
**Parent correction brief:** `../briefs/s01_query_validation_corrective_brief.md`
**Prior rejected result:** `../s01_query_validation_result.json`
**Reviewer:** Codex
**Reviewed at:** 2026-11-26T13:22:53+07:00
**Disposition:** `SCIENTIFICALLY_ACCEPTED_USER_RELAYED`
**Attachment SHA-256:** `a17bbfca001a37332c9370fc0fff4a2464df0e2e615fbacd043f14b059b0d556`

The corrected JSON passes all 13 parent criteria and all 8 corrective criteria.
It may be used as accepted S-01 research evidence. The result was relayed by
the user and contains no transport-level Gemini/A2A task or context identifier;
therefore this review does not claim that the approved A2A router performed the
task. Git plus the attachment hash preserve the received evidence exactly.

## Parent criteria

| Criterion | Verdict | Objective evidence |
|---|---|---|
| 1. Exactly four unique platforms | PASS | 4 records and 4 unique required platform names. |
| 2. Exactly eight unique query IDs | PASS | All 8 required IDs occur exactly once; missing=0 and duplicates=0. |
| 3. Official documentation or exact block | PASS | Scopus and WoS official documentation is reachable. IEEE Web Command Search remains HTTP 418/blocked and ACM syntax guidance remains inaccessible to the review client; all four affected IEEE/ACM queries remain explicitly `BLOCKED`. |
| 4. Verdicts, four filter verdicts and conclusion-matched evidence | PASS | 8 query verdicts and 32 filter verdicts are present. WoS English-language support now has an official `Language` locator in both queries; Scopus scope now has an official `INDEX` plus `TITLE-ABS-KEY` locator in both queries. Unsupported non-blocked conclusions=0. |
| 5. Complete corrections for `REVISE`; no unexplained `PASS` changes | PASS | 4 `REVISE` queries each contain a complete corrected query and explicit changed tokens/filters; malformed revision records=0. |
| 6. ACM short-paper assessment | PASS | Exactly one `REMOVE_FILTER` assessment; it uses Amendment 003's substantive-content rule and no page-count threshold. |
| 7. Seed-matrix dimensions and validity | PASS | Independent CSV check: 20 normalized unique DOI rows, 8 query columns, 160 non-empty allowed-value cells, duplicates=0, missing=0 and invalid=0. |
| 8. Eight expected-match counts | PASS | Independently reproduced counts are 9, 8, 1, 0, 14, 8, 14 and 8; sum=62. |
| 9. Zero executed-search/access/result claims | PASS | `database_result_counts_claimed=0`; all 4 `access_or_export_claimed=false`; executed-search and export-completion claims=0. |
| 10. Official URL+locator for each factual syntax/filter claim | PASS | The four former gaps now have official URLs and exact locators; unsupported quantitative claims=0. |
| 11. Explicit unresolved items | PASS | 5 unresolved items remain explicit and no longer contradict the accepted WoS language-filter evidence. |
| 12. Scholarly-record discovery marked N/A | PASS | Requested scholarly records=0 is explicitly `NOT_APPLICABLE`. |
| 13. No Gemini project/manuscript writes | PASS | `project_files_modified=0`; one JSON object; manuscript prose=0. |

**Parent total:** 13 PASS, 0 FAIL.

## Corrective criteria

| Criterion | Verdict | Objective evidence |
|---|---|---|
| 1. Four platforms and eight queries | PASS | 4/4 platforms and 8/8 unique required query IDs. |
| 2. WoS language evidence and consistency | PASS | `WOS_HR` and `WOS_COMP` each cite the official `Web of Science Core Collection Search Fields` page, locator `Language`; language-related unresolved contradiction count=0. |
| 3. Scopus collection/scope evidence | PASS | `SCOPUS_HR` and `SCOPUS_COMP` each cite the official Advanced Search page at `Document -> Database (INDEX)` and `TITLE-ABS-KEY`. |
| 4. Unsupported non-blocked conclusions | PASS | Count=0 after direct source and internal-consistency review. |
| 5. Seed audit unchanged | PASS | 20×8=160, expected-match sum=62, duplicates=0, missing=0 and invalid=0. |
| 6. Prohibited claims | PASS | Result counts, executed searches, access/export success and unsupported quantitative claims each=0. |
| 7. Read-only structured output | PASS | Project writes by Gemini=0, manuscript prose=0 and output objects=1. |
| 8. Parent acceptance | PASS | All 13 parent criteria pass in the table above. |

**Corrective total:** 8 PASS, 0 FAIL.

## Independent official-source confirmation

- Scopus documents `TITLE-ABS-KEY` and the database field `INDEX`, including
  `INDEX(medline)`/`AND NOT INDEX(medline)` behavior:
  <https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search>.
- WoS documents a `Language` refinement whose default is `All languages` and
  whose selectable list includes `English`:
  <https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields>.
- WoS retains the documented `PY=` and Proceedings Paper boundaries:
  <https://webofscience.zendesk.com/hc/en-us/articles/26916347018257-Web-of-Science-Core-Collection-Advanced-Search-Field-Tags>
  and
  <https://webofscience.zendesk.com/hc/en-us/articles/26916283577745-Document-Types>.

## Provenance boundary

The returned JSON has the research task ID `S01-QUERY-VALIDATION-v1` but no
provider transport task/context ID. Provenance is therefore recorded as
`USER_RELAYED_ATTACHMENT`, not `A2A_ROUTER_VERIFIED`. This does not change the
13/13 scientific acceptance result, but future status reports must not claim
that S-01 was dispatched through or completed by the approved A2A router.
