# OpenAlex PRISMA Search Tool — Short Design

## Intent

Replace repetitive manual web searching with a reproducible, auditable search
run over a lawful public scholarly API. The output supplements the planned core
database searches and must never be labelled as a Web of Science Core
Collection result.

## Goals

- Run the two accepted UAV–edge query concepts over OpenAlex title/abstract
  fields for 2021-01-01 through the actual search date.
- Preserve the exact query, interpreted OpenAlex query, filters, cursor pages,
  raw records, normalized CSV, counts, duplicate diagnostics, timestamps and
  SHA-256 checksums.
- Use deterministic, dependency-free Python with unit-tested pagination,
  validation, normalization and evidence-bundle creation.

## Non-goals

- Bypassing authentication, CAPTCHA, paywalls or database licences.
- Claiming that OpenAlex has the same coverage as Web of Science.
- Automating eligibility decisions, full-text assessment or synthesis.
- Silently changing the eight already planned core-database runs.

## Approaches considered

1. Browser extension: useful for an authenticated tab, but fragile against DOM
   changes and weak for repeatable multi-page evidence capture.
2. Browser automation: can reproduce UI actions, but cannot create licensed
   WoS Core access and is unnecessarily brittle for a public API.
3. Standalone OpenAlex CLI: selected because the API documents Boolean phrase
   searching, date/language filtering and cursor pagination, and its raw JSON
   responses can be archived directly.

## Constraints and evidence boundary

The complementary query contains wildcards and therefore uses OpenAlex's exact
title/abstract search parameter. The high-recall query uses the stemmed
title/abstract parameter. Publication type is exported broadly and deferred to
screening because OpenAlex types do not exactly reproduce the journal/conference
facets of the licensed databases. Any formal use as compensation for unavailable
WoS access requires a dated protocol amendment and an explicit limitation.
