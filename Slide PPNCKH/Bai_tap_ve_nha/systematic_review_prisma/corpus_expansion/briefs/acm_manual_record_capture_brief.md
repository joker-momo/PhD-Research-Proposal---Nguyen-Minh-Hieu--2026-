# ACM manual record-capture brief

## TASK

Capture and normalize every result position returned by the two accepted ACM Digital Library searches in the user's authenticated Basic Edition browser session.

## REQUIRED WORK

1. Preserve the displayed query, date filter, collection, page URL and capture time.
2. Capture all 79 high-recall and 325 complementary result positions without bypassing authentication or CAPTCHA controls.
3. Normalize title, year, record type, authors, venue, DOI or explicit `DOI_NOT_FOUND`, URL or explicit `URL_NOT_FOUND`, query variant, page and rank.
4. Preserve repeated source rows at their displayed ranks and report duplicate identifiers for the next deduplication task.
5. Generate checksums, a manifest and deterministic QA output.

## REQUIRED OUTPUT

- Raw page captures for 17 complementary pages and 4 high-recall pages.
- Two normalized JSON files and one combined CSV.
- A manifest, checksum ledger, QA report, result note and Codex acceptance review.

## ACCEPTANCE CRITERIA

1. Query variants captured: exactly 2/2.
2. Result positions captured: exactly 79/79 and 325/325.
3. Rank sequence: contiguous with zero duplicate ranks in both variants.
4. Missing titles: 0; missing or out-of-range years: 0.
5. Every row has a DOI value or explicit marker, URL value or explicit marker, and source-page URL or raw-file locator.
6. Repeated DOI/title identities are counted and retained as source evidence, not silently discarded.
7. Parser unit tests: 100% pass; generated checksum verification: 100% pass.
8. Unsupported quantitative claims: 0; unresolved items are explicit.

## BOUNDARIES

Do not bypass CAPTCHA, scrape an unauthenticated endpoint, infer missing metadata, change the accepted queries, classify relevance, deduplicate source positions, alter the existing 46-report screening decisions, or claim that Web of Science was searched. Credentials and session tokens must not be persisted or delegated.
