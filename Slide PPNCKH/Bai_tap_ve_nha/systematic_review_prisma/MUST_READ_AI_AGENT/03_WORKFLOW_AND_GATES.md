# Workflow and Gates

## Session start gate

1. Complete the manifest reading order.
2. Read only the task-relevant canonical files from `06_FILE_MAP.md`.
3. Inspect Git status/branches and record pre-existing changes.
4. State one concrete task and measurable completion criteria.
5. Identify whether the task is writing/editing (Codex) or research/synthesis
   (eligible for routed delegation).
6. Report current evidence boundary and any missing user decision.

## Project workflow

| Stage | Gate before advancing |
|---|---|
| Requirements | Every official and later user requirement maps to an artifact/action |
| Protocol | RQs, eligibility, information sources, extraction, appraisal, and synthesis are fixed or amended prospectively |
| Discovery | Exact query, platform, date, filters, returned/exported counts, raw file, and limitation recorded |
| Deduplication | Zero duplicate records after DOI/title normalization; preprint/published families linked |
| Screening | Every record has a decision; every excluded full text has one primary reason; uncertainty remains explicit |
| Full-text intake | Identity/version/readability checked; lawful provenance logged |
| Extraction | Every required field has evidence locator or `not reported` |
| Quality appraisal | Ten domains completed with rationale for every included study |
| PRISMA reconciliation | Record/report/study arithmetic passes with zero unexplained difference |
| Synthesis | Every RQ claim maps to accepted included-study evidence; heterogeneous outcomes are not pooled without compatibility/variance |
| Manuscript | Methods-Results-Discussion-Introduction agree; Title/Abstract/Keywords updated after substantive changes |
| Integrity/build | Zero placeholders/unverified citations/fabricated values; LaTeX builds; PDF pages inspected |
| Author approval | Authors, order, affiliations, email, contributions, declarations, and final text approved |
| Submission | Live route verified; submitted files/metadata match; manuscript ID and receipt archived |
| Course evidence | Correct recipient, subject, name, student ID, manuscript ID, and receipt forwarded |

## Manuscript drafting order

Use the user's HCMUT workflow order for drafting, while preserving the journal's
section order in the final manuscript:

1. Authors and roles.
2. Abstract draft.
3. Keywords.
4. Title.
5. Methods.
6. Results.
7. Discussion.
8. Introduction.
9. Conclusion.
10. Acknowledgements/declarations.
11. References.
12. Appendix.

Iterate Methods -> Results -> Discussion -> Introduction until all claims and
measurements agree. Never repair a scientific mismatch only by rewriting prose.

## Change and review gate

For every material change:

1. Work on a dedicated branch/worktree.
2. Change only task-owned paths.
3. Run relevant validation/build/audit.
4. Inspect diff for dead files, debug output, placeholders, secrets, unsupported
   claims, and unrelated edits.
5. Commit atomically with an intent-revealing message.
6. Fast-forward merge, verify the merged result, delete the task branch/worktree.
7. Update `CURRENT_HANDOFF.md` if status, canonical paths, counts, blockers, or
   next actions changed.

## Status language

Use only evidence-bounded labels:

- `accepted`: all mandatory criteria PASS after Codex review.
- `unreviewed`: provider/task completed but no full gate yet.
- `rejected`: at least one mandatory criterion FAILS.
- `uncertain`: evidence does not support a final eligibility/claim decision.
- `historical`: retained for audit but not current source of truth.
