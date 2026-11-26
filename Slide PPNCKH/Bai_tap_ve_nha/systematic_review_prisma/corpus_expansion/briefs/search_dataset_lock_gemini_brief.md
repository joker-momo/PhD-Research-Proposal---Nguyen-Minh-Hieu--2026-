# Gemini Research Brief: Search Dataset Lock Audit

**Task ID:** `SEARCH-DATASET-LOCK-AUDIT-v1`

## TASK

Independently audit the supplied search-evidence snapshot against official
methodological and provider documentation, then recommend whether and how the
HK261 PRISMA search dataset can be frozen without representing an unavailable
or counts-only source as an imported record source.

## REQUIRED WORK

1. Verify from official PRISMA/PRISMA-S guidance what must be reported when an
   information source is planned but unavailable, when a protocol deviation
   occurs, and when a supplementary discovery source is used.
2. Verify from official provider documentation the relevant capability
   boundaries of ACM Digital Library Basic Edition, Web of Science Free View
   versus Web of Science Core Collection, OpenAlex, and Research Horizon
   Navigator. Do not infer a capability that the official source does not state.
3. Reconcile exactly the ten supplied query-variant states below. Preserve every
   reported/exported count and null exactly; do not replace local evidence with
   web snippets.
4. Assign one disposition to each of the six named sources using only these
   values: `INCLUDE_IN_RECORD_CORPUS`, `SEARCH_EVIDENCE_ONLY_NO_RECORDS`,
   `UNAVAILABLE_NOT_SEARCHED`, `SUPPLEMENTARY_DISCOVERY_ONLY`, or
   `NOT_EXECUTED_EXCLUDE_FROM_FREEZE`.
5. Reconcile the arithmetic for importable records. Distinguish exported rows,
   within-source cross-query union, observed counts without records, and final
   unique records after future cross-platform deduplication.
6. Return one evidence-bounded recommendation: either `FREEZE_NOW` with an exact
   frozen source set and required disclosure, or `DO_NOT_FREEZE` with the
   smallest concrete prerequisite that remains. Evaluate Research Horizon
   Navigator separately; it has not been executed for this review.

### Supplied local evidence snapshot

Treat these as supplied-file facts to audit, not as web claims. Local locators
are relative to `systematic_review_prisma/`.

| Row ID | Source | Variant | Reported | Exported | Status | Primary locator |
|---|---|---|---:|---:|---|---|
| IEEE-HR | IEEE Xplore | high_recall | 42 | 42 | complete | `sources/raw/core_searches/ieee_xplore_high_recall_export_2026-11-26.csv` |
| IEEE-COMP | IEEE Xplore | complementary | 21 | 21 | complete | `sources/raw/core_searches/ieee_xplore_complementary_export_2026-11-26.csv` |
| ACM-HR | ACM Digital Library | high_recall | 79 | 0 | search complete; Basic Edition export blocked | `sources/raw/core_searches/acm_high_recall_2026-11-26.json` |
| ACM-COMP | ACM Digital Library | complementary | 325 | 0 | search complete; Basic Edition export blocked | `sources/raw/core_searches/acm_complementary_2026-11-26.json` |
| SCOPUS-HR | Scopus | high_recall | 77 | 77 | complete | `sources/raw/core_searches/scopus_high_recall_export_2026-11-26.csv` |
| SCOPUS-COMP | Scopus | complementary | 33 | 33 | complete | `sources/raw/core_searches/scopus_complementary_export_2026-11-26.csv` |
| WOS-HR | Web of Science Core Collection | high_recall | null | 0 | Core search unavailable after sign-in; Free View only | `sources/raw/core_searches/web_of_science_free_view_recheck_2026-11-26.json` |
| WOS-COMP | Web of Science Core Collection | complementary | null | 0 | Core search unavailable after sign-in; Free View only | `sources/raw/core_searches/web_of_science_free_view_recheck_2026-11-26.json` |
| OPENALEX-HR | OpenAlex | high_recall | 85 | 85 | complete supplementary compensatory | `sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_high_recall_2026-11-26_raw.json` |
| OPENALEX-COMP | OpenAlex | complementary | 26 | 26 | complete supplementary compensatory | `sources/raw/core_searches/openalex_compensatory_2026-11-26/openalex_complementary_2026-11-26_raw.json` |

Additional accepted local facts:

- IEEE plus Scopus exported rows before cross-query/cross-platform
  deduplication: `173`.
- OpenAlex exported rows before cross-query deduplication: `111`; cross-query
  overlap: `9`; OpenAlex union IDs: `102`.
- Total currently importable rows before any cross-platform deduplication:
  `284` (`173 + 111`). This is not a unique-record count.
- ACM observed totals sum to `404`, but overlap is unknown and zero ACM records
  were exported; `404` must not be added to imported or unique records.
- Web of Science reported totals remain `null`; zero counts were inferred.
- Research Horizon Navigator was assessed but not executed and produced zero
  records for this review.
- `sources/raw/core_searches/checksums.sha256` verifies all supplied evidence;
  checksum verification remains Codex-owned.
- OpenAlex is explicitly not Web of Science Core Collection and Amendment 006
  does not claim equivalent coverage.

## REQUIRED OUTPUT

Return exactly one valid JSON object with this schema and no prose outside it:

```json
{
  "task_id": "SEARCH-DATASET-LOCK-AUDIT-v1",
  "checked_at": "RFC3339 timestamp with timezone",
  "scholarly_record_count": 0,
  "scholarly_record_fields_applicability": "NOT_APPLICABLE_NO_SCHOLARLY_RECORD_DISCOVERY",
  "query_variant_audit": [
    {
      "row_id": "one of the ten supplied row IDs",
      "reported_total": "integer or null exactly as supplied",
      "exported_total": "integer exactly as supplied",
      "local_locator": "exact supplied locator",
      "admissibility": "IMPORTABLE_RECORDS | COUNTS_ONLY_NOT_IMPORTABLE | UNAVAILABLE_NO_COUNT",
      "finding": "bounded factual statement"
    }
  ],
  "source_dispositions": [
    {
      "source": "one of IEEE Xplore, ACM Digital Library, Scopus, Web of Science Core Collection, OpenAlex, Research Horizon Navigator",
      "disposition": "one allowed disposition",
      "record_rows_admitted": 0,
      "reason": "bounded reason",
      "official_source_urls": ["https://..."]
    }
  ],
  "arithmetic": {
    "ieee_scopus_exported_rows": 173,
    "openalex_exported_rows": 111,
    "currently_importable_rows": 284,
    "openalex_cross_query_overlap": 9,
    "openalex_union_ids": 102,
    "acm_observed_counts_not_importable": 404,
    "wos_reported_totals": [null, null],
    "cross_platform_unique_records": null
  },
  "methodological_findings": [
    {
      "claim": "one claim",
      "official_source_url": "https://...",
      "source_class": "official_guideline | official_provider_documentation",
      "implication": "bounded implication for this freeze"
    }
  ],
  "recommendation": {
    "decision": "FREEZE_NOW | DO_NOT_FREEZE",
    "frozen_record_sources": ["source names"],
    "search_evidence_only_sources": ["source names"],
    "excluded_unexecuted_sources": ["source names"],
    "required_protocol_action": "exact action or NONE",
    "required_disclosure": ["exact bounded disclosures"],
    "next_step": "one concrete next action"
  },
  "unresolved_items": ["explicit item"],
  "unsupported_quantitative_claims": []
}
```

## ACCEPTANCE CRITERIA

1. `query_variant_audit` contains exactly 10 objects and exactly the ten supplied
   row IDs; missing or extra IDs = 0.
2. All 20 reported/exported values and all 10 local locators equal the supplied
   snapshot exactly; altered values = 0.
3. `source_dispositions` contains exactly six objects and each named source
   appears exactly once; duplicate sources = 0.
4. Arithmetic equals `173`, `111`, `284`, `9`, `102`, `404`, `[null,null]`, and
   `cross_platform_unique_records=null`; unsupported unique-count claims = 0.
5. At least four distinct official URLs are supplied, including at least one
   official reporting guideline and official documentation for ACM/Clarivate;
   non-official blogs, search snippets, Reddit and AI-generated pages = 0.
6. Every provider-capability or reporting-method claim has one official URL;
   claims without a URL = 0.
7. OpenAlex/RHN claims of being a WoS Core search or coverage-equivalent to WoS
   Core = 0.
8. ACM `404` is never reported as imported or unique records; WoS null totals are
   never converted to zero results; violations = 0.
9. `recommendation` selects exactly one decision and names every source in
   exactly one of the three source arrays; omitted/duplicated sources = 0.
10. Missing evidence and unresolved decisions are explicit; silently omitted
    unresolved items = 0; fabricated counts, records, searches or capabilities = 0.

## BOUNDARIES

- Read-only research only. Do not edit project files, create manuscript prose,
  alter Git, submit searches, download files, or communicate externally.
- Do not request, receive, expose or infer credentials, cookies, tokens, private
  account data or institutional access details.
- Do not claim to have opened local locators. They are supplied facts; only
  Codex verifies local files and checksums.
- Do not execute a new database search or treat Research Horizon Navigator as
  executed. Do not use OpenAlex or RHN as a renamed WoS Core search.
- Use official guideline/provider sources for methodological and capability
  claims. If official documentation is unavailable, mark the item unresolved.
- Do not discover scholarly records in this task. Therefore title/authors/year/
  venue/DOI fields are inapplicable and `scholarly_record_count` must be zero.
- Do not invent a final deduplicated record count. Cross-platform deduplication
  has not yet occurred.
