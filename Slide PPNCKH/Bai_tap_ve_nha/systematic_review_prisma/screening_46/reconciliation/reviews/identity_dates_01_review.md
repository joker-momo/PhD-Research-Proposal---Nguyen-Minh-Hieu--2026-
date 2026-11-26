# Identity/date reconciliation 01 — rejected

Task ID: 01a21521-896b-7bdf-8bcb-1b0cfda69f2f
Context ID: 01a21521-896c-7042-b5c5-e7d4a480a8a0
Reviewer: Codex
Reviewed at: 2026-11-26T07:08:34+07:00
started_at: 2026-11-26T06:54:09+07:00
updated_at: 2026-11-26T07:08:34+07:00
completed_at: 2026-11-26T07:08:34+07:00

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| A1 coverage/schema | yes | PASS | 10/10 requested IDs; no missing fields, duplicates or extras; shortfall empty |
| A2 identities/attempts | yes | PASS | 10 complete identities; 24 timestamped attempts; 10 publisher and 10 Crossref attempts plus C08 arXiv; normalized DOI/title duplicates 0; 10/10 Crossref metadata subsets independently match live responses |
| A3 claim/source fidelity | yes | FAIL | 7/10 local excerpts are not contiguous source quotations; C03 content_equivalence=verified has only bibliographic support; C08 calls its 14-word title a 13-word title |
| A4 date/decision logic | yes | PASS | 10 date verdicts; 4 YES and 6 UNCERTAIN; no administrative date substituted for publication; month/year precision retained; other gates preserved |
| A5 C08 linkage boundary | yes | PASS | 1 explicit assessment; matching ordered authors/title/journal evidence and missing DOI relation disclosed; numerical equivalence not_assumed and unique recent preprint eligibility not_established |
| A6 ownership/boundaries | yes | PASS | project_files_changed=0, final_prose_written=false; canonical 51-entry external baseline unchanged; no new scope/family decision adopted |

Verdict: **REJECTED_A3 / QUARANTINED**. Accept zero records from this result.
The prior 46-report ledger remains 32 INCLUDE, 2 EXCLUDE, 12 UNCERTAIN.

## Failed targets and required corrections

1. Sources C03_LOCAL_TXT, C05_LOCAL_TXT, C09_LOCAL_TXT, C10_LOCAL_TXT,
   C13_LOCAL_TXT, C14_LOCAL_TXT and C19_LOCAL_TXT: replace each excerpt with one
   exact contiguous passage and its precise line/page locator. C05/C09/C10/
   C14/C19 remove the intervening author-version warning between acceptance
   and DOI sentences without an omission marker. C13 combines the header and
   received-date sentence at line 35. C03 combines issue/header material from
   different pages. Keep bibliographic facts in metadata_fields; do not present
   assembled summaries as exact source excerpts.
2. C03 version_linkage.content_equivalence: the claimed verified equivalence is
   not established by matching title, abstract, pagination and ORCIDs. Use
   not_assumed with the bounded bibliographic-match explanation, unless an
   actual full-text/numerical comparison is supplied. This task does not require
   that new comparison.
3. C08 version_linkage.limitation: its supplied title has 14 whitespace-delimited
   words, not 13. Remove the unnecessary count or correct it with reproducible
   counting. This does not invalidate the verified title/author match itself.

## Independent checks and limits

- 10/10 Crossref metadata subsets match source responses. Initial HTTP429 on
  S19/C14 resolved on one later attempt, retained in source_checks.json.
- Literal local excerpts match 3/10 (S19,S20,C08), fail 7/10 after NFKC/alphanumeric
  normalization; source text remains unchanged.
- Five additional publisher/arXiv/LinkingHub responses were retrieved. These
  support bounded bibliographic checks; they do not establish full-text parity.
- Proposed date resolutions S19/S20/C03/C08 are not adopted while A3 fails.
- Six IEEE dates remain year-only/UNCERTAIN. Missing publisher access remains
  a limitation, not evidence for a fabricated publication day.

Source artifacts: `../results/identity_dates_01.json`, raw transport, source
checks and `identity_dates_01_source_audit/`. Original provider result is immutable.
Next: commit quarantine, prepare a narrowly scoped corrective brief, commit it,
then route the correction and recheck every mandatory criterion.
