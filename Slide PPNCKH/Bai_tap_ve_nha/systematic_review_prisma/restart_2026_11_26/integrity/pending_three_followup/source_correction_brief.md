# TASK
Recheck four exact source fields only for the prior HK261 follow-up 133c68cc-d77f-4cb1-9cdd-ad4a5f613097, with emphasis on the now-identified DroNet review rule.

# REQUIRED WORK
1. Check R0292 review rule in the first paragraph of https://sites.google.com/view/dronet2025/submissions, exact sentence supplied for comparison: DroNet follows a single-blinded review process.
2. Check R0292 identity in Technical Program Session #3 at https://sites.google.com/view/dronet2025/program, exact title supplied for comparison: Continuous Marine Monitoring via Autonomous UAV Handoff. Combine the verified fields only in the recommendation footer; record whether E7 is still open.
3. Check R0082 Related DOI field only at https://arxiv.org/abs/2305.15858v1. Keep Xplore full-text access separate and report that gap in the footer if unresolved.
4. Check R0113 article-level DOI metadata field only at https://ajaccm.com/journal/index.php/ajaccm/article/view/771 (check citation_doi or displayed DOI). Report the exact value as published and retain E3/E4/E7 if still unresolved, using the previously verified PDF assessment. Do not reopen PDFs for this web-only correction.

# REQUIRED OUTPUT
Exactly four JSONL evidence objects, one per field, then one JSONL footer. Each evidence object is {"key":"R0292_REVIEW","source":"named URL","locator":"precise location","status":"VERIFIED","excerpt":"exact short text"}; required keys R0292_REVIEW, R0292_PROGRAM, R0082_RELATED_DOI, R0113_ARTICLE_DOI. Allowed statuses VERIFIED, NOT_ACCESSIBLE, UNVERIFIED. For unresolved entries use empty excerpt. Footer shape {"complete":true,"R0082":["E7"],"R0113":["E3","E4","E7"],"R0292":[],"r0292_recommendation":"INCLUDE","workers_used":false,"worker_assignments":{}} with actual values and recommendation INCLUDE or AWAITING_CLASSIFICATION. Keep it compact and schema-only with no extra prose. Reuse verified bibliographic identities from the prior result.

# ACCEPTANCE CRITERIA
Exactly four unique requested keys and one footer, each source located once and no extra claims or unverified numbers. Exact primary source excerpt/field matches and explicit status for any inaccessible source. E7 decision must account for both R0292 sources. Supplied comparison text by itself is not proof of opening. No changes to S2 or PRISMA.

# BOUNDARIES
Read-only, only the listed source URLs, no project edits, credentials, workarounds, outreach, or PDF transfer. Parent gathers the four sources and reports any access limitation.
Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
