# TASK
Locate primary results blocks for 46 already-included HK261 reports to support independent quantitative extraction.

# REQUIRED WORK
1. Verify direct PDF access by reading one full body page of the first report. If no report text is accessible, return the exact access error.
2. For each listed PDF, locate the main evaluation pages and identify the table, figure or section labels that present the system outcomes. Distinguish blocks with at least one visibly printed outcome value from graphical-only and ambiguous blocks. Identify analytical, simulated, emulated, physical or mixed settings only where the PDF supports them.
3. Return one compact entry for each of the 46 IDs, sorted in the supplied order. If worker support exists, allocate each report to exactly one worker and reconcile one reply. Report actual worker use and the assigned IDs. If its availability is unconfirmed, process in the parent.

# REQUIRED OUTPUT
Return compact JSONL. A successful entry is {"id":"R0001","status":"READ","pages":"3-4","anchors":"III.B, Figs. 2–3","formats":"plot","setting":"simulation","excerpt":"short exact contiguous body phrase"}. Allowed status READ, NOT_ACCESSIBLE, UNVERIFIED. For inaccessible/unverified rows use `reason` and explicit observed fields as available. Allowed formats are `printed`, `plot`, `printed+plot`, `ambiguous`, `none`. Use physical PDF page numbers starting at 1. Reference paths are fixed by the supplied ID list. Include one short verbatim contiguous excerpt from the locator for each READ row. Do not include numeric outcome values or bibliographic records. End with a returned count, unresolved IDs, worker assignments and END marker.

# ACCEPTANCE CRITERIA
Exactly 46 expected IDs with zero duplicate or unexpected IDs, or an explicit list of shortfalls. Every READ row has a role-specific evaluation locator and contiguous verbatim excerpt and accounts for the actual types of presentation in the result blocks. Every setting comes from the supplied original. Unsupported numbers or facts equal zero. There are no newly discovered or asserted bibliographic records. Codex will open the PDF, verify identity, pages and excerpt and confirm content and relevance for 100% of any entries proposed for adoption. Flag unresolved entries and missing fields rather than filling them.

# BOUNDARIES
Only read the listed authorized PDFs from the attached canonical HK261 folder. Use local PDF reading and page rendering supported by your environment. If you cannot read a body page or render an inaccessible table, report the limitation and affected IDs. No internet, no writing or editing files, no retrospective decisions about inclusion, no drafting RQ5. Keep the task in the parent when workers cannot read the supplied files. Verify claims against the actual PDF, not layout-losing snippets.

Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.

## Authorized input
- R0001 restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf
- R0002 restart_2026_11_26/fulltext_retrieval/pdf/R0002.pdf
- R0003 restart_2026_11_26/fulltext_retrieval/pdf/R0003.pdf
- R0006 restart_2026_11_26/fulltext_retrieval/pdf/R0006.pdf
- R0009 restart_2026_11_26/fulltext_retrieval/pdf/R0009.pdf
- R0010 restart_2026_11_26/fulltext_retrieval/pdf/R0010.pdf
- R0014 restart_2026_11_26/fulltext_retrieval/pdf/R0014.pdf
- R0015 restart_2026_11_26/fulltext_retrieval/pdf/R0015.pdf
- R0019 restart_2026_11_26/fulltext_retrieval/pdf/R0019.pdf
- R0022 restart_2026_11_26/fulltext_retrieval/pdf/R0022.pdf
- R0029 restart_2026_11_26/fulltext_retrieval/pdf/R0029.pdf
- R0036 restart_2026_11_26/fulltext_retrieval/pdf/R0036.pdf
- R0038 restart_2026_11_26/fulltext_retrieval/pdf/R0038.pdf
- R0043 restart_2026_11_26/fulltext_retrieval/pdf/R0043.pdf
- R0044 restart_2026_11_26/fulltext_retrieval/pdf/R0044.pdf
- R0045 restart_2026_11_26/fulltext_retrieval/pdf/R0045.pdf
- R0048 restart_2026_11_26/fulltext_retrieval/pdf/R0048.pdf
- R0054 restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf
- R0058 restart_2026_11_26/fulltext_retrieval/pdf/R0058.pdf
- R0059 restart_2026_11_26/fulltext_retrieval/pdf/R0059.pdf
- R0062 restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf
- R0063 restart_2026_11_26/fulltext_retrieval/pdf/R0063.pdf
- R0064 restart_2026_11_26/fulltext_retrieval/pdf/R0064.pdf
- R0068 restart_2026_11_26/fulltext_retrieval/pdf/R0068.pdf
- R0071 restart_2026_11_26/fulltext_retrieval/pdf/R0071.pdf
- R0073 restart_2026_11_26/fulltext_retrieval/pdf/R0073.pdf
- R0074 restart_2026_11_26/fulltext_retrieval/pdf/R0074.pdf
- R0075 restart_2026_11_26/fulltext_retrieval/pdf/R0075.pdf
- R0077 restart_2026_11_26/fulltext_retrieval/pdf/R0077.pdf
- R0080 restart_2026_11_26/fulltext_retrieval/pdf/R0080.pdf
- R0083 restart_2026_11_26/fulltext_retrieval/pdf/R0083.pdf
- R0089 restart_2026_11_26/fulltext_retrieval/pdf/R0089.pdf
- R0090 restart_2026_11_26/fulltext_retrieval/pdf/R0090.pdf
- R0092 restart_2026_11_26/fulltext_retrieval/pdf/R0092.pdf
- R0095 restart_2026_11_26/fulltext_retrieval/pdf/R0095.pdf
- R0106 restart_2026_11_26/fulltext_retrieval/pdf/R0106.pdf
- R0107 restart_2026_11_26/fulltext_retrieval/pdf/R0107.pdf
- R0110 restart_2026_11_26/fulltext_retrieval/pdf/R0110.pdf
- R0113 restart_2026_11_26/fulltext_retrieval/pdf/R0113.pdf
- R0118 restart_2026_11_26/fulltext_retrieval/pdf/R0118.pdf
- R0121 restart_2026_11_26/fulltext_retrieval/pdf/R0121.pdf
- R0125 restart_2026_11_26/fulltext_retrieval/pdf/R0125.pdf
- R0137 restart_2026_11_26/fulltext_retrieval/pdf/R0137.pdf
- R0145 restart_2026_11_26/fulltext_retrieval/pdf/R0145.pdf
- R0223 restart_2026_11_26/fulltext_retrieval/pdf/R0223.pdf
- R0292 restart_2026_11_26/fulltext_retrieval/pdf/R0292.pdf
