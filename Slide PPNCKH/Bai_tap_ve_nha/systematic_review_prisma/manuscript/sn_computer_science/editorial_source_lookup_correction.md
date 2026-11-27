## TASK
Correct the primary-source and version-evidence failures in HK261 public lookup task 01a21c52-100e-7a50-afbd-184b571116b8.
## REQUIRED WORK
1. Return IDEA's exact publication type from the publisher or Crossref only. Omit the DBLP assertion.
2. Return the WCNC related DOI as a bibliographic link. Use the label accepted manuscript only if explicitly supported by a primary source. Mark the publisher PDF and textual comparison unresolved when inaccessible.
3. Return HAO bibliographic identity and explicit partition or recovery scope from the ACM publisher or Crossref only. Omit Semantic Scholar and unverified negative counts. Distinguish an abstention from proof of absence.
## REQUIRED OUTPUT
Three keyed records IDEA, WCNC, HAO. Each has title, authors, year, venue, DOI, claims with primary URL and exact locator, and an unresolved field.
## ACCEPTANCE CRITERIA
Exactly 3 distinct keys, 0 normalized duplicate titles or DOIs, 0 excluded source classes, 0 unsupported quantitative assertions, 0 unsupported version labels and 1 unresolved field per record.
## BOUNDARIES
Public sources only. No project files, login, contact, publishing, new corpus search, or eligibility decision. Report missing evidence explicitly and do not fabricate any fields.
