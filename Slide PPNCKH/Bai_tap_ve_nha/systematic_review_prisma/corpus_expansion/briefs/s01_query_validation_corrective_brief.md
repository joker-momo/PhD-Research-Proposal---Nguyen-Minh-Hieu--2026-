# S-01 Corrective Research Brief — Evidence Alignment Only

**Brief ID:** `S01-QUERY-VALIDATION-CORRECTION-v1`
**Parent brief:** `S01-QUERY-VALIDATION-v1`
**Parent result:** `../s01_query_validation_result.json`
**Codex review:** `../reviews/s01_query_validation_acceptance.md`
**Owner of research notes:** `GEMINI_RESEARCH`
**Owner of acceptance and project writes:** `CODEX_WRITING`

## TASK

Return one complete corrected replacement for the rejected S-01 JSON by fixing
only the unsupported or internally contradictory Scopus collection/scope and
Web of Science language-filter verdicts and evidence.

## REQUIRED WORK

1. Read the parent brief, parent result and Codex acceptance review listed
   above. Preserve every parent field not affected by criteria 4 and 10.
2. For `WOS_HR` and `WOS_COMP`, either provide official Web of Science evidence
   with a non-empty locator that directly supports the English-language filter
   and retain `language=PASS`, or change the verdict to `BLOCKED` and state the
   exact unresolved evidence. The filter verdict and `unresolved_items` must not
   contradict each other.
3. For `SCOPUS_HR` and `SCOPUS_COMP`, either provide official Scopus evidence
   with a non-empty locator that directly supports `collection_or_scope=PASS`,
   or change that filter verdict to `BLOCKED` and state the exact unresolved
   evidence. Do not infer platform scope without documentation.
4. Return the full eight-query JSON using the original S-01 schema, not a patch
   fragment. Recalculate no matrix values unless a mechanical recheck finds an
   actual discrepancy; report any discrepancy instead of silently changing it.
5. Keep the four IEEE/ACM query verdicts blocked unless newly reachable official
   documentation directly resolves the already listed syntax/filter gaps.

## REQUIRED OUTPUT

Return exactly one JSON object conforming to the full schema in
`s01_query_validation_brief.md`. Use task ID
`S01-QUERY-VALIDATION-v1` and a new RFC 3339 `checked_at` timestamp. Return all
4 platform records, all 8 query records, the ACM assessment, complete seed audit,
all unresolved items, `database_result_counts_claimed=0`, and
`project_files_modified=0`.

## ACCEPTANCE CRITERIA

1. Platform records=4 and query records=8; missing or duplicate query IDs=0.
2. `WOS_HR.language` and `WOS_COMP.language` each have exactly one conclusion
   matched by at least one official URL+locator evidence row; contradictions
   between those verdicts and `unresolved_items`=0.
3. `SCOPUS_HR.collection_or_scope` and `SCOPUS_COMP.collection_or_scope` each
   have exactly one conclusion matched by at least one official URL+locator
   evidence row.
4. Unsupported non-`BLOCKED` syntax/filter conclusions=0 across all 8 queries.
5. Original seed audit remains 20 unique DOI rows, 8 query columns, 160 cells,
   duplicates=0, missing=0, invalid values=0 and expected-match sum=62.
6. Database result counts, executed-search claims, access/export claims and
   unsupported quantitative claims each equal 0.
7. Project files modified by Gemini=0; manuscript prose written=0; output
   objects=1.
8. All 13 mandatory criteria from the parent brief pass after Codex's new
   criterion-by-criterion review.

## BOUNDARIES

- Read-only research correction. Do not edit, create, move or delete project
  files and do not write manuscript prose.
- Do not execute database searches, report result counts, claim access/export
  success or infer missing behavior.
- Use only official IEEE, ACM, Elsevier/Scopus and Clarivate/Web of Science
  documentation for platform syntax/filter claims.
- Do not expand into S-02--S-05, E-04, E-06, X-01, X-03, X-04 or X-05.
- Missing evidence must produce `BLOCKED` plus an explicit unresolved item;
  never manufacture a `PASS` conclusion.
- Return a complete corrected JSON object only. Codex alone issues acceptance.
