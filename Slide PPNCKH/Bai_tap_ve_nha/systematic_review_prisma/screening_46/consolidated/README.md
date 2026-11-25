# Consolidated working screening: 46 reports

This is an administrative derivative of eight accepted screening batches.
It copies accepted decisions and evidence without making new research decisions.
The frozen intake contains 46 reports: 32 INCLUDE, 2 EXCLUDE and 12 UNCERTAIN.
These are working report decisions, not final eligible studies or PRISMA counts.

## Files

- `decision_ledger.json`: full accepted records, original JSON pointers, batch
  review links, source hashes and commits. Human adjudication remains PENDING;
  final eligibility and study IDs remain null.
- `decision_ledger.csv`: 46-row navigation table with identity, decision,
  non-YES gates and pointers. The JSON retains all detailed evidence.
- `unresolved_queue.csv`: 136 verbatim unresolved occurrences, including nested
  version-reconciliation notes. Repeated historical notes are intentionally kept
  at distinct pointers; 136 is not a count of distinct scientific problems.
- `provenance_manifest.json`: source/result hashes and observed task timestamps.
- `validation.md`: binary checks of this transcription, not a scientific review.

## Eligibility questions carried forward

| Gate needing resolution | Reports | Count |
|---|---|---:|
| Publication date | S19, S20, C03, C05, C09, C10, C13, C14, C19 | 9 |
| Multi-UAV / collaborative-inference scope | C06, SNCS | 2 |
| Published identity or conditional preprint eligibility | C08 | 1 |

Other version, evaluation and family questions remain open even for INCLUDE
records. Shared authors do not establish study equivalence or independence.
Zero normalized DOI/title duplicates is a record-level check, not proof of
independent studies. No accepted historical source was rewritten.

## Next sequence

1. Commit a Gemini brief for the nine unresolved dates and C08 identity/version.
2. Review every returned claim and preserve unresolved access/date evidence.
3. Obtain source-grounded scope and study-family reconciliation, including the
   already flagged included reports and earlier conference companions.
4. Reconcile the historical 27-report dataset and formal database exports;
   complete extraction and appraisal before changing manuscript conclusions.

The fixed search cutoff remains 2026-11-25. New searching must log the actual
run date and follow the protocol if the final search cutoff is updated.
