# IEEE Xplore Interface Verification

**Recorded at:** 2026-11-26T13:33:49+07:00
**Verifier:** Codex, using the user's running Chrome session through read-only accessibility-tree and screenshot inspection
**Execution status:** No query submitted; no results page opened; no count or export obtained
**Readiness:** `READY_FOR_S02_WITH_RESULTS_PAGE_FACET_CHECK`

## Observed interfaces

| URL | Locator observed | Observation |
|---|---|---|
| `https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/command-search` | `Using Command Search`, steps 1–3; `Summary of Data Fields`, row `All Metadata` | Command Search accepts a quoted field name followed by a colon; exact phrases use double quotation marks; `All Metadata` includes abstract, index terms and bibliographic citation data; Boolean expressions and parentheses are supported under the documented nesting rules. |
| `https://ieeexplore.ieee.org/search/advanced/command` | Live `Command Search` tab | The page states that operators must be uppercase, data-field names must precede each search term, and each search clause may contain at most 25 terms. The query box was left empty and `Search` remained disabled. |
| `https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/search-tips#searching-with-wildcard-characters` | `Searching with Wildcard Characters`; `Search Clauses` | A search may use up to 10 wildcards; at least three characters must precede/use a wildcard; `*` may appear at the end of a word; wildcards may be used with Boolean operators and within quoted phrases. A clause may contain up to 25 terms. |

## S-01 gap verdicts

| Gap | Verdict | Objective evidence |
|---|---|---|
| Quoted `"All Metadata":` field prefix | PASS | Official help gives quoted field-name-plus-colon syntax, and the data-field table contains `All Metadata`. |
| Exact phrase behavior | PASS | Official help states that double quotes request an exact phrase within a field. |
| Parentheses and Boolean behavior | PASS | Command Search help documents uppercase Boolean operators, precedence and grouping with parentheses. |
| Complementary-query wildcards | PASS | The query uses four trailing wildcards (`partition*`, `offload*`, `schedul*`, `assign*`), below the observed maximum of 10; every prefix has at least three characters. |
| Search-clause term cap | PASS | Each OR group in the two planned queries has fewer than the observed maximum of 25 terms. |
| Year 2021–2026 facet | BLOCKED_UNTIL_S02_RESULTS_PAGE | No query was submitted, so a results-page facet was not observed. |
| `Journals` and `Conferences` facets | BLOCKED_UNTIL_S02_RESULTS_PAGE | No query was submitted, so results-page content facets were not observed. |
| English-language facet | BLOCKED_UNTIL_S02_RESULTS_PAGE | No query was submitted, so a results-page language facet was not observed. |

## S-02 execution rule

The two IEEE query strings are cleared for entry. During S-02, record the actual result-page facets before applying them. If any planned year, content-type or language facet is absent, preserve and export the broader result set permitted by IEEE Xplore, record the missing facet as a limitation, and enforce the corresponding eligibility rule during screening. Do not infer a filtered count.

## Integrity boundary

The live page displayed institutional and personal sign-in options; this verification did not sign in, transmit credentials, submit a query, open search results or test export. It proves syntax/interface visibility only, not institutional entitlement or retrieval completion.
