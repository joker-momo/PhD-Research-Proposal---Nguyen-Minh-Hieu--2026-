# TASK
Correct only the failed evidence-format and source-traceability checks for HK261 R0082/R0113/R0292 after native Gemini.app task 87d030f1-4539-4ce8-9509-f1dad8172f0c.

# REQUIRED WORK
1. Read the body of the three exact PDFs under restart_2026_11_26/fulltext_retrieval/pdf/ and protocol_restart.md §P03 at restart_2026_11_26/protocol_restart.md. Recheck R0082 §I p2, R0113 p7–13, R0292 §§4–5.2 pp3–5. For each, provide one genuinely contiguous body quote of 5–12 words with physical PDF page (1-based); use actual accessible PDF tooling, verify any table cited on the original page, or report limitations.
2. R0082: IEEE Xplore document 10118908 versus arXiv 2305.15858v1, and official IEEE Author Center Understand Peer Review (https://conferences.ieeeauthorcenter.ieee.org/understand-peer-review/). Distinguish official peer-review evidence from publisher full-text access and report these as separate claims.
3. R0113: mark E3/E4 and E7 gaps separately if unresolved. Author Guidelines §8 versus Policies and official article 771. Do not infer that no peer review occurred. No numbers from figures, tables or editorial timing.
4. R0292: one exact official DroNet 2025 Program Session 3 field, and one short exact Macquarie Research output field/excerpt. Clearly distinguish institutional classification from ACM/workshop review-process confirmation. Do not use HotCRP acceptance counts, third-party sources, arXiv from a different article, or a nearby ACM paper.
5. Include only one recommendation per ID with open criteria and one checked-source shortfall. Keep parent-only if workers unavailable; report actual use.

# REQUIRED OUTPUT
Return strict compact JSONL, no fences, four lines total, at most 4500 characters. Three single-line record objects using the schema below, then one footer exactly shaped as {"complete":true,"unresolved_ids":["R0082"],"workers_used":false,"worker_assignments":{}} with actual values. Use straight ASCII JSON delimiters, omit nested double quotation marks in excerpts by choosing shorter contiguous text, no literal newlines inside objects. One exact local PDF anchor + up to two primary web entries per record. Shape:
{"id":"R0082","title":"source title","authors":["source author"],"year":2023,"venue":"source venue","doi":"10.1109/WCNC55385.2023.10118908","local_access":"VERIFIED","recommendation":"AWAITING_CLASSIFICATION","criteria_open":["E7"],"gap":"one short verified reason","checked_unresolved_source":"exact URL or path, or empty string if resolved","evidence":[{"claim":"one fact","source":"actual URL or project-relative supplied path","locator":"physical PDF p. 2, section","excerpt":"five to twelve contiguous source words"}]}
Use DOI_NOT_FOUND if no complete DOI. Use INCLUDE / EXCLUDE / AWAITING_CLASSIFICATION only; use VERIFIED / NOT_ACCESSIBLE only for local_access.

# ACCEPTANCE CRITERIA
Exactly three distinct row IDs plus one machine-parseable footer, zero unsupported numbers (identity year and identifiers allowed), zero duplicate DOI/title, mandatory metadata on 3/3. Independent checks for identity, all evidence source paths/URLs and exact excerpts/locators. No evidence merged across fields. Explicit unresolved IDs/criteria and sources, and actual worker accounting. Answer comprehensiveness is limited to these specific fields.

# BOUNDARIES
Read-only using the approved folder. No editing, no forwarding or uploading files, no logins, no access circumvention or contact, no eligibility changes. Use only the named documents and primary publication sources. Return evidence for Codex and the author, not manuscript prose.
Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
