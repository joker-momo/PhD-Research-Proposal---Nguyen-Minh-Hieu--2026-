# Public source lookup review

Initial A2A task `01a21c52-100e-7a50-afbd-184b571116b8`, context
`01a21c52-1014-7952-8ad4-044ca498543a`. The router initially timed out
(exit 5). Original-task recovery returned completed status and one artifact.
The following review governs adoption of that artifact.

| Gate | Verdict | Evidence |
| --- | --- | --- |
| Exact target keys | PASS | Seven headings corresponding to IDEA, WCNC, ZENODO, HEMASRI, DHUHEIR, HAO and REN, each with a bibliographic record. |
| Bibliographic fields | PASS | All seven provide title, author list, year, venue and DOI, or `DOI_NOT_FOUND` for HEMASRI. |
| Duplicates | PASS | Seven distinct normalized titles and six distinct primary DOIs, with the seventh explicit as absent. |
| Primary-source-only evidence | FAIL | IDEA includes a DBLP search assertion and HAO includes Semantic Scholar metadata. These are outside the requested publisher, author-repository and registry classes. |
| Source-backed version and quantitative assertions | FAIL | WCNC's arXiv related-DOI link establishes bibliography linkage, but no two-text comparison supports the label “accepted-version”. HAO incorporates counts and an absence search over registry metadata without preserving a sufficient source locator to verify the scope of that negative assertion. |
| Explicit unresolved statements and eligibility boundary | PASS | Seven records contain an unresolved field. No included/excluded disposition was returned. |

The artifact did not pass the adoption gate. The editorial PDF uses
independently checked publisher, author-repository and registry sources
plus locally matched PDF evidence. The correction request below limits the
follow-up to the failed criteria.

The targeted correction request is archived in
[editorial_source_lookup_correction.md](editorial_source_lookup_correction.md).
The legacy dispatcher rejected the corrective attempt at its pre-dispatch
Git checkpoint. The comparison therefore relies on the independent source
checks. In particular, the ACM site and Crossref confirm the IDEA report
type and Hao publication identity. The arXiv metadata expressly links
the LLHR conference DOI without establishing text equivalence, and the
publisher version was unavailable through the authorized public route.
