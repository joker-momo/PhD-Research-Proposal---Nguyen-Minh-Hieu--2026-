# S-01 Research Brief — Validate Platform Queries and Seed Coverage

**Brief ID:** `S01-QUERY-VALIDATION-v1`
**Prepared at:** 2026-11-26T13:03:38+07:00
**Owner of research notes:** `GEMINI_RESEARCH`
**Owner of acceptance and project writes:** `CODEX_WRITING`
**ARS routing:** bounded Stage-1 research function; use deep-research behavior only, not the full academic pipeline
**Dispatch status:** `READY_AFTER_COMMIT; NOT_YET_DISPATCHED`

## TASK

Validate the syntax, field operators, Boolean/wildcard behavior and proposed interface refinements of the eight planned queries for IEEE Xplore, ACM Digital Library, Scopus and Web of Science, then audit the existing 20-seed × 8-query expectation matrix without executing or claiming any database search.

## REQUIRED WORK

1. Read the supplied `final_query_translations.md`, `protocol.md`, Amendments 001–003 and `seed_query_coverage_matrix.csv`.
2. Identify exactly eight queries using these IDs: `IEEE_HR`, `IEEE_COMP`, `ACM_HR`, `ACM_COMP`, `SCOPUS_HR`, `SCOPUS_COMP`, `WOS_HR`, `WOS_COMP`.
3. For each platform, consult current official platform documentation for field codes, phrase searching, Boolean grouping, wildcard/truncation, publication-year constraints, document-type filters, language filters and collection/scope selection.
4. Compare each exact planned query and its interface filters with the official documentation. Assign `PASS`, `REVISE` or `BLOCKED`. If `REVISE`, return a complete corrected query and list every changed token/filter. If evidence is unavailable, use `BLOCKED` and state what is missing.
5. Explicitly assess whether ACM's instruction `Do not include Short-Paper` conflicts with Amendment 003 by potentially excluding substantively complete primary-research reports. Do not decide eligibility from page count.
6. Audit the seed matrix mechanically and semantically: 20 unique DOI rows, eight named query columns, 160 expectation cells, allowed values only `EXPECTED_MATCH`/`EXPECTED_MISS`, zero duplicate DOI rows and zero missing cells. Explain that expectations are calibration hypotheses, not proof of platform indexing or executed searches.
7. For every syntax/filter conclusion, include an official documentation URL and the exact heading/section or quoted field/operator name used as evidence. List every unresolved item explicitly.

## REQUIRED OUTPUT

Return one JSON object and no manuscript prose. Use this schema:

```json
{
  "task_id": "S01-QUERY-VALIDATION-v1",
  "checked_at": "RFC3339 timestamp with timezone",
  "platforms": [
    {
      "platform": "IEEE Xplore|ACM Digital Library|Scopus|Web of Science Core Collection",
      "official_documentation": [
        {
          "url": "https://...",
          "locator": "page heading or section name",
          "supports": ["field syntax", "wildcard", "filter", "collection"]
        }
      ],
      "access_or_export_claimed": false
    }
  ],
  "queries": [
    {
      "query_id": "one of the eight required IDs",
      "platform": "platform name",
      "verdict": "PASS|REVISE|BLOCKED",
      "unsupported_or_ambiguous_constructs": [],
      "corrected_query": "complete query or null",
      "changed_tokens_or_filters": [],
      "filter_verdicts": {
        "publication_year": "PASS|REVISE|BLOCKED",
        "document_type": "PASS|REVISE|BLOCKED",
        "language": "PASS|REVISE|BLOCKED",
        "collection_or_scope": "PASS|REVISE|BLOCKED"
      },
      "evidence": [
        {"url": "https://...", "locator": "official heading/section", "claim": "bounded syntax/filter claim"}
      ]
    }
  ],
  "acm_short_paper_assessment": {
    "verdict": "KEEP_FILTER|REMOVE_FILTER|BLOCKED",
    "reason": "evidence-bounded explanation",
    "official_evidence": [{"url": "https://...", "locator": "heading/section"}],
    "protocol_effect": "none or explicit prospective query/filter change required"
  },
  "seed_matrix_audit": {
    "unique_doi_rows": 20,
    "query_columns": 8,
    "expectation_cells": 160,
    "duplicate_doi_rows": 0,
    "missing_cells": 0,
    "invalid_values": [],
    "per_query_expected_match_counts": {
      "IEEE_HR": 0,
      "IEEE_COMP": 0,
      "ACM_HR": 0,
      "ACM_COMP": 0,
      "SCOPUS_HR": 0,
      "SCOPUS_COMP": 0,
      "WOS_HR": 0,
      "WOS_COMP": 0
    },
    "interpretation_boundary": "expected sensitivity only; no indexing or search-execution claim"
  },
  "unresolved_items": [],
  "database_result_counts_claimed": 0,
  "project_files_modified": 0
}
```

The eight `per_query_expected_match_counts` values must be calculated from the supplied matrix, not copied from the zero-valued schema example.

## ACCEPTANCE CRITERIA

1. Platform records = exactly 4, one for each required platform; duplicate platform records = 0.
2. Query records = exactly 8; all eight required IDs present exactly once; duplicate or missing query IDs = 0.
3. Every platform has at least one reachable official documentation URL and a non-empty locator, or its affected queries are `BLOCKED` with the exact access failure documented.
4. Every query has one verdict, four filter verdicts and at least one official evidence row for each non-`BLOCKED` syntax/filter conclusion.
5. Every `REVISE` query has one complete corrected query and at least one explicit changed token/filter; every `PASS` query has `corrected_query=null` and zero unexplained changes.
6. ACM short-paper assessment is present exactly once and addresses Amendment 003 without a page-count rule.
7. Seed audit reports exactly 20 unique DOI rows, 8 query columns and 160 non-empty expectation cells; duplicate DOI rows = 0; missing cells = 0; invalid values = 0.
8. Eight per-query expected-match counts are calculated; their sum equals the number of `EXPECTED_MATCH` cells in the supplied matrix.
9. Database result counts claimed = 0; executed-search claims = 0; access/export completion claims = 0.
10. Every factual platform-syntax/filter claim has an official URL plus locator; unsupported quantitative claims = 0.
11. Unresolved items are listed explicitly; silent omissions = 0.
12. Scholarly-record discovery is outside this task, so requested scholarly records = 0 and missing DOI/title/author/venue metadata criterion is `NOT_APPLICABLE`, not silently ignored.
13. Project files modified by Gemini = 0; final manuscript prose written by Gemini = 0.

## BOUNDARIES

- Do not execute the eight database searches, report result counts, claim that a seed is indexed or claim that access/export succeeded.
- Do not edit, create, move or delete project files; return research notes only.
- Do not modify the protocol, query file or seed matrix. Proposed changes belong only in the returned JSON.
- Use official platform/provider documentation for syntax and filter claims. Library blogs, SEO pages, AI summaries and search-result snippets may not substitute for official documentation.
- Do not perform E-04, E-06, X-01, X-03, X-04, X-05, manuscript writing or any later batch.
- Do not infer missing behavior. Report `BLOCKED` or add an unresolved item when official evidence is insufficient.
- Do not include credentials, institutional login details, private messages or local secrets.
- Preserve the date scope 2021 through the eventual final search date. The current 2026 upper-bound expressions are provisional execution-window syntax and must not be represented as evidence that 2026 is complete.
- Return one JSON object conforming to the schema. No PASS/FAIL acceptance decision: Codex alone performs the criterion review.
