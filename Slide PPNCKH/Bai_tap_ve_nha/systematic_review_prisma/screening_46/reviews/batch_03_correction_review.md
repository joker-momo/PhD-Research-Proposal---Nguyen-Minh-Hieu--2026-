# S16 identity correction review — REJECTED evidence serialization

Task ID: 01a212f3-36d0-7480-9dc7-f509f80112f5
Reviewer: Codex
Reviewed at: 2026-11-25T13:49:46.901108+00:00

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| C1 | yes | PASS |1/1 S16;0 duplicates/shortfall|
| C2 | yes | PASS |Crossref independently fetched: title,3 authors,2026 July issue,Journal of Systems Architecture176:103804,DOI match;online date explicitly UNVERIFIED|
| C3 | yes | FAIL |10 evidence objects; indices5 and9 use ellipses rather than literal text; index6 concatenates noncontiguous XML elements; index0 byline normalization mismatch; evidence1,2,3,4,8 text-matched|
| C4 | yes | PASS |Published identity supported by Crossref and arXiv DOI link;issueJuly2026 within cutoff;content equivalence NOT_ASSUMED|
| C5 | yes | PASS |0 declared mutations;unresolved publisher-PDF/online-date/family issues explicit;no new performance effects|

Saved independent verification: results/batch_03_correction_crossref.json and
results/batch_03_correction_arxiv.xml. arXiv landing page also opened and shows
related DOI, title,3 authors,and v3 date8April2026. These substantiate identity;
source evidence fields must still meet the literal quote contract before use.

Required follow-up: return the same one-record schema with literal evidence
entries. Replace composite author snippet by individually located author-field
values or literal contiguous slices; replace composite XML by exact single
arxiv:doi element and separate date elements. Use supplied extracted page1 text
for exact author snippet or quote title alone. Remove nonliteral HTTP snippet;
report access failure as unresolved with raw task response locator. No other
scientific finding or identity change required. Every quote max45 words.
