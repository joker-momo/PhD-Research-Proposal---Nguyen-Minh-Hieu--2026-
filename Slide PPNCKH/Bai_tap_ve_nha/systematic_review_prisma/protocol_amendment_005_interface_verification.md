# Protocol Amendment 005 — IEEE and ACM Interface Verification

**Date:** 2026-11-26
**Recorded at:** 2026-11-26T13:33:49+07:00
**Applies to:** Protocol version 0.1 after Amendments 001–004
**Timing:** Before the first formal IEEE Xplore or ACM Digital Library search.

## Change

Official help and the current live pre-search interfaces establish that the version 1.2 IEEE and ACM query strings use supported Boolean, exact-phrase and wildcard constructs. IEEE Command Search supports the quoted `All Metadata` field, the planned queries remain below its 25-term-per-clause and 10-wildcard limits, and each wildcard prefix meets the three-character minimum. ACM Advanced Search supports the planned Boolean and quoted-phrase constructs and the four trailing wildcards outside phrases.

For the formal ACM core search, the selected scope is `The ACM Full-Text collection` with `Search Within = Anywhere`. A search of `The ACM Guide to Computing Literature`, if later justified, is supplementary and must be logged separately rather than silently merged with the core run.

The inspected pre-search pages did not expose every planned results filter. ACM's observed custom date controls use month and year, not an exact day. During S-02/S-03, the operator must record whether the year, content-type and language facets actually appear. If a required facet or exact-day boundary is unavailable, the review will preserve and export the broader permitted result set, document the limitation, and apply the corresponding English-language/report-type/date rule during screening. Short Paper records remain eligible for substantive assessment under Amendment 003.

## Reason

Amendment 004 correctly blocked IEEE and ACM until direct interface verification. That verification now resolves the query-syntax, wildcard and ACM-scope uncertainties without executing a search. Retaining execution-time facet checks and a predefined broader-export fallback prevents an unavailable interface filter from becoming an undocumented protocol deviation.

## Effect on completed work

- Version 1.3 changes the execution profile, not the eight query strings accepted under S-01.
- IEEE S-02 and ACM S-03 may start under their immutable raw-export and search-log contracts.
- No query was submitted, no result or export count was observed, and no raw export was created when this amendment was recorded.
- No current 46-report corpus decision or count changes.

## Integrity boundary

The IEEE session displayed sign-in routes and the ACM session displayed Basic Edition with a Premium/sign-in route. This amendment does not claim authenticated institutional entitlement, successful export, search completion or final PRISMA identification counts. Those claims require S-02/S-03 evidence.
