# Protocol Amendment 004 — Query Validation and Prospective Execution Rules

**Date:** 2026-11-26
**Recorded at:** 2026-11-26T13:26:57+07:00
**Applies to:** Protocol version 0.1 after Amendments 001–003
**Timing:** Before any formal search of IEEE Xplore, ACM Digital Library, Scopus, or Web of Science Core Collection.

## Basis

This amendment adopts only the query and filter revisions that passed the S-01 scientific acceptance gate. The accepted evidence is preserved in `corpus_expansion/s01_query_validation_corrected_result.json`, and the criterion-by-criterion Codex review is preserved in `corpus_expansion/reviews/s01_query_validation_correction_acceptance.md`.

The S-01 result was relayed by the user and archived with its attachment hash. It does not contain an A2A provider task or context identifier, and this amendment does not represent it as an approved-router execution.

## Changes

1. `final_query_translations.md` version 1.2 becomes the prospective canonical query set.
2. Both Scopus queries use the documented `PUBYEAR AFT 2020 AND PUBYEAR BEF 2027` operators and embed `LANGUAGE(english)`. The document types remain `(DOCTYPE(ar) OR DOCTYPE(cp))`.
3. Both Web of Science queries add the quoted plural variants needed when lemmatization is disabled, embed the provisional 2021–2026 window as `(PY=(2021-2025) OR PY=2026)`, and require the execution log to identify the active Core Collection editions, including whether `CPCI-S` is enabled.
4. ACM `Short Paper` records are no longer excluded by publication-type filter alone. Research Articles and Short Papers proceed to substantive eligibility screening under Amendment 003; Demonstrations, Extended abstracts, Posters, and Work in Progress records remain excluded when they lack the required substantive method-and-results content.
5. IEEE Xplore and ACM Digital Library queries remain `BLOCKED_PENDING_AUTHENTICATED_UI_VERIFICATION`. No formal run may begin until the unresolved Web interface syntax, wildcard, scope, language, year, and content-type behaviors identified in version 1.2 have been verified and recorded.

## Reason

S-01 found platform-specific differences that affect reproducibility and recall. The former Scopus syntax omitted the language restriction from the query and did not use the documented year operators. Quoted Web of Science phrases required explicit plural variants, and its year and edition scope needed to be made reproducible. The former ACM instruction to exclude Short Papers conflicted with Amendment 003 and ACM's article-type definition. IEEE and ACM Web UI behavior could not be established from the official materials reached during S-01, so treating those queries as executable would overstate the evidence.

## Prospective effect

- These changes apply to the first formal run and every later rerun of the affected platforms.
- No database search was executed when this amendment was recorded.
- No database result count, export count, access event, or search timestamp is created by this amendment.
- No existing decision in the 46-report corpus changes, and the current include/exclude/uncertain counts remain unchanged.
- The seed-query coverage matrix remains a sensitivity-planning artifact; it is not database execution evidence.

## Execution gate

The next task is authenticated-interface verification for IEEE Xplore and ACM Digital Library. That verification must record the interface, selected scope/facets, exact supported syntax, evidence locator, verifier, and RFC 3339 timestamp. Formal searching and result export are a separate task and must not be inferred from successful interface verification.

## Integrity boundary

This amendment does not claim exhaustive retrieval, platform access, search completion, export completion, or final PRISMA identification counts. Any future deviation from version 1.2 after a formal run requires a new dated amendment and reruns of every affected query.
