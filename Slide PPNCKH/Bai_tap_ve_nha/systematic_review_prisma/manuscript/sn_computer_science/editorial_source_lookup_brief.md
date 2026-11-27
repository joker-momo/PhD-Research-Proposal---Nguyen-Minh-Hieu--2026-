# HK261 editorial source lookup

TASK
Check seven public bibliographic or scope leads for the HK261 editorial revision.

REQUIRED WORK
1. Find authoritative publication/proceedings and review-type evidence for Sun et al., IDEA (ACM MobiSys 2022 demonstration), and version identity for DOI 10.1109/WCNC55385.2023.10118908.
2. Open Zenodo DOI 10.5281/zenodo.20445205 and identify the version and any peer-reviewed publication relation.
3. Check the official venue and credible index/publisher sources for the 2026 Hemasri and Reddy SNN paper in American Journal of AI Cyber Computing Management. Distinguish missing proof from an adverse finding.
4. Identify the Dhuheir et al. IWCMC 2021 candidate about resource-constrained UAV swarms and whether its public full text demonstrates neural inference across multiple UAVs.
5. Check publisher source scopes for 10.1145/3786145 and 10.1007/s11633-022-1391-7. Return exact pointers supporting explicit treatment of neural network partitioning, MoE or recovery if observed.

REQUIRED OUTPUT
Return seven records keyed IDEA, WCNC, ZENODO, HEMASRI, DHUHEIR, HAO, REN. Fields: record_id, title, authors, year, venue, doi or DOI_NOT_FOUND, claims[] with claim_or_decision, source, locator and short exact excerpt or exact metadata field, unresolved[].

ACCEPTANCE CRITERIA
Seven distinct requested keys or an explicit per-key shortfall; zero duplicate DOI/title records; every factual assertion has an opened primary URL, locator and support; every bibliographic record has identity fields or an explicit unresolved field; zero unsupported numerical assertions; all unresolved items explicit. Primary publisher, author-repository, or registry sources only. No primary inclusion or exclusion decision.

BOUNDARIES
Public internet only; no local project or PDFs, file changes, communication with authors, login, proxy or new corpus searches. No invitation to draft prose. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
