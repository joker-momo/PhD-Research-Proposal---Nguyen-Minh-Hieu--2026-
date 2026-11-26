# S-01 query-validation acceptance review

**Reviewed result:** `../s01_query_validation_result.json`
**Parent brief:** `../briefs/s01_query_validation_brief.md`
**Reviewer:** Codex
**Reviewed at:** 2026-11-26T13:14:38+07:00
**Disposition:** `REJECTED_NEEDS_TARGETED_CORRECTION`

The returned JSON remains quarantined. Criteria 4 and 10 fail because two
non-`BLOCKED` filter conclusions do not have matching official evidence and one
of them contradicts the result's own unresolved-items list. No query revision
is adopted into the protocol or query translations.

## Criterion-by-criterion verdict

| Criterion | Verdict | Objective evidence |
|---|---|---|
| 1. Exactly four unique platforms | PASS | 4 records and 4 unique platform names: IEEE Xplore, ACM Digital Library, Scopus and Web of Science Core Collection. |
| 2. Exactly eight unique query IDs | PASS | 8 records; all required IDs occur exactly once; duplicates=0 and missing IDs=0. |
| 3. Official documentation or exact block | PASS | Scopus and WoS official pages were independently reachable. IEEE Web Command Search returned HTTP 418 and both IEEE queries are `BLOCKED`. ACM syntax guidance was inaccessible/HTTP 403 and both ACM queries are `BLOCKED`; exact unresolved behavior is listed. |
| 4. Verdicts, four filter verdicts and evidence for every non-blocked conclusion | FAIL | All 8 query verdicts and 32 filter verdicts are present. However, `WOS_HR` and `WOS_COMP` set `language=PASS` while no evidence row supports the English-language filter and an unresolved item says it still requires verification. `SCOPUS_HR` and `SCOPUS_COMP` set `collection_or_scope=PASS`, but their evidence rows do not establish that conclusion. Four non-blocked filter conclusions therefore lack conclusion-matched official evidence. |
| 5. Complete corrections for `REVISE`; no unexplained `PASS` changes | PASS | 4 `REVISE` queries each contain a complete corrected query and at least one changed token/filter; 0 `PASS` queries and 0 malformed revision records. |
| 6. ACM short-paper assessment | PASS | Exactly one assessment; verdict `REMOVE_FILTER`; it applies Amendment 003's substantive-content rule and uses no page-count threshold. |
| 7. Seed-matrix dimensions and validity | PASS | Independent CSV check: 20 rows, 20 normalized unique DOI values, 8 query columns, 160 cells, duplicates=0, missing=0 and invalid values=0. |
| 8. Eight calculated expected-match counts | PASS | Counts independently reproduced as 9, 8, 1, 0, 14, 8, 14 and 8; sum=62 `EXPECTED_MATCH` cells. |
| 9. Zero executed-search/access/result claims | PASS | `database_result_counts_claimed=0`; 4/4 platform `access_or_export_claimed=false`; the JSON reports no executed result count or export completion. |
| 10. Official URL+locator for every factual syntax/filter claim; unsupported quantitative claims=0 | FAIL | The same four `language`/`collection_or_scope` conclusions identified under criterion 4 lack matching source support. The WoS `language=PASS` values also conflict with the unresolved statement that the Language control still needs verification. Matrix quantities were independently reproduced and are supported. |
| 11. Explicit unresolved items | PASS | 5 unresolved items explicitly cover IEEE, ACM, WoS subscription/language, date-boundary behavior and the scholarly-record N/A boundary. |
| 12. Scholarly-record discovery marked N/A | PASS | Requested scholarly records=0 is explicitly represented as `NOT_APPLICABLE`; no bibliographic-record fields were silently omitted. |
| 13. Gemini made no project/manuscript writes | PASS | `project_files_modified=0`; output is one JSON object and contains no manuscript prose. |

**Mandatory total:** 11 PASS, 2 FAIL. Because mandatory acceptance requires
13/13 PASS, the result is rejected pending a linked correction.

## Independent source checks

- IEEE Metadata API documentation, `Search Parameters`, confirms metadata
  Boolean/wildcard constraints but not the blocked Xplore Web Command Search
  behavior: <https://developer.ieee.org/docs/read/Metadata_API_details>.
- IEEE Web Command Search documentation could not be fetched during review
  (HTTP 418):
  <https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/command-search>.
- ACM `Search Tools` and `Article Types` pages returned HTTP 403 to the review
  client, consistent with retaining the affected ACM conclusions as blocked:
  <https://libraries.acm.org/training-resources/search-tools> and
  <https://libraries.acm.org/acmopen/article-types>.
- Scopus `How can I best use the Advanced search?` documents `TITLE-ABS-KEY`,
  `DOCTYPE`, `LANGUAGE`, `PUBYEAR AFT/BEF` and the `INDEX` database field:
  <https://www.elsevier.support/scopus/answer/how-can-i-best-use-the-advanced-search>.
- WoS `Search Rules`, `Advanced Search Field Tags`, `Document Types` and
  `Core Collection Search Fields` document quotation/lemmatization, `TS=`,
  `PY=`, document types and the Language refinement respectively:
  <https://webofscience.zendesk.com/hc/en-us/articles/25350084904721-Search-Rules>,
  <https://webofscience.zendesk.com/hc/en-us/articles/26916347018257-Web-of-Science-Core-Collection-Advanced-Search-Field-Tags>,
  <https://webofscience.zendesk.com/hc/en-us/articles/26916283577745-Document-Types>, and
  <https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields>.

## Provenance gate

The user-pasted JSON contains the research task ID but no A2A provider task or
context identifier. The original brief did not place that identifier in the
JSON schema, so this is not counted as an extra failure among criteria 1--13.
It nevertheless leaves the project-level dispatch provenance gate unresolved.
The corrective task must be sent through the approved router so Codex can
record its provider task/context ID separately.
