## TASK
Independently screen the 136 masked HK261 PDF reports against the supplied E1–E7 criteria.

## REQUIRED WORK
1. Verify access first: open HKF-001.pdf, read a body page, and report one exact 5–9-word contiguous excerpt, physical page and section. If inaccessible, report the access blocker, list the unresolved range and stop.
2. If accessible, read HKF-001.pdf through HKF-136.pdf individually. Use PDF text extraction with physical page breaks (local PyMuPDF or Poppler if available) and inspect original pages for exact quotes, complex tables or ambiguity. Apply HK261-E1-E7.txt and its precedence. Track unknown peer review or date as unresolved when the PDF gives insufficient evidence. Choose internal non-overlapping assignments if actual workers are supported, and report their ID ranges and use; otherwise process within the parent Task.
3. For each inclusion, point to the assessed neural-inference assignment and its evaluation with separate source anchors. For exclusions, point to the first established eligibility failure in protocol priority. For awaiting records, point to the exact missing evidence. Use PDF metadata for title, author, year, venue and DOI; report UNKNOWN or DOI_NOT_FOUND when absent. Record probable duplicate editions separately. Distinct same-paper records must be listed by ID and flagged, not quietly dropped.
4. Reconcile all 136 once in one consolidated response. If the output limit approaches, prefer supplying all compact rows, with any unresolved IDs listed explicitly.

## REQUIRED OUTPUT
Start with the access test and worker-use statement. Then one compact JSONL object per packet ID, exactly this schema:
{"id":"HKF-001","title":"Title as printed","authors":["A Author"],"year":2025,"venue":"Venue as printed","doi":"DOI_NOT_FOUND","decision":"AWAITING_CLASSIFICATION","primary":"E7","gates":"PPPPPPU","evidence":[{"page":2,"section":"Methods","quote":"exact contiguous source words"}],"why":"Publication type remains unverified."}
Decision enum INCLUDE, EXCLUDE, AWAITING_CLASSIFICATION. Primary E1..E7 or empty string for INCLUDE. In gates, order is E1 through E7 with P=pass, F=fail, U=unresolved. When a PDF is inaccessible provide its ID, UNKNOWN metadata, pending decision, seven U codes, empty evidence and exact access problem. Evidence source filename is id plus .pdf. End with returned/accessible/unresolved counts, explicit unresolved IDs, normalized duplicate DOI/title flags, worker assignments and END_HK261_136.

## ACCEPTANCE CRITERIA
Exactly 136 unique requested IDs or documented shortfall. Every inspected ID has all required fields and a physical page and contiguous quote supporting the decision. Every asserted fact has an original supplied-file locator. Each record names title, authors, year, venue, DOI or explicit DOI_NOT_FOUND. Zero duplicate emitted rows after normalizing DOI/title and retaining cross-referenced record IDs when needed. Zero unsupported quantitative claims. List every unresolved ID. Each positive decision requires a method and an evaluation anchor. AI decisions cannot be represented as human decisions.

## BOUNDARIES
Read only the attached masked PDF folder and the attached criteria text. No project writes, communications, browsing, internet downloads, uploads of PDFs, reuse of other reviewers' decisions, or generation of manuscript material. Do not describe operational deployment details outside the screening rationale.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
