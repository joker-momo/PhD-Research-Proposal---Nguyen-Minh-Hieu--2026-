# Protocol Amendment 006 — Reproducible OpenAlex Compensatory Search

**Date:** 2026-11-26
**Recorded at:** 2026-11-26T14:53:39+07:00
**Applies to:** Protocol version 0.1 after Amendments 001–005
**Timing:** Before the first formal OpenAlex compensatory search.

## Change

The review adds two reproducible OpenAlex title-and-abstract searches using the
same high-recall and complementary concept blocks as query set 1.3. The search
window is 2021-01-01 through the execution date and the API language filter is
English. The high-recall query uses OpenAlex's stemmed title/abstract search.
The complementary query uses exact title/abstract search because it contains
wildcards, which OpenAlex rejects in its stemmed search mode.

The searches are executed by the committed `prisma_openalex_search.py` tool.
Each run retains the exact query, API-interpreted query, filters, request URLs,
cursor-page count, API-reported total, raw JSON, normalized CSV, duplicate
diagnostics, timestamps and SHA-256 checksums. Publication types are exported
broadly and the journal/conference eligibility rule is enforced during
screening because OpenAlex types are not equivalent to the facets of the four
planned core platforms.

## Reason

The authenticated Clarivate session provides Web of Science Free View but not
Web of Science Core Collection Documents search. Consequently, neither planned
WoS Core query can be executed or exported. OpenAlex was already named in the
protocol as a supplementary discovery source and offers a documented public API
that permits an auditable compensatory search without bypassing access controls.

## Prospective effect

- OpenAlex results are labelled `supplementary_compensatory_search` and undergo
  the same deduplication and eligibility assessment as other records.
- The two unexecuted WoS Core runs remain explicitly blocked with null counts;
  OpenAlex results are never renamed or represented as WoS Core results.
- The six completed core-platform searches and their counts/exports are not
  changed.
- The compensatory search reduces discovery risk but does not establish that
  OpenAlex coverage is equivalent to Web of Science Core Collection.
- This amendment does not resolve the missing ACM record-level exports.

## Integrity boundary

Recording this amendment creates no formal search result, count, export or
screening decision. Formal counts exist only after the committed tool completes
both variants and the generated evidence bundles pass checksum and count
reconciliation.
