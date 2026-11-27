## TASK
Adjudicate study linkage for the HK261 supplemental inclusion checkpoint under P07.

## REQUIRED WORK
1. Use only protocol_restart.md P07, the accepted screening and locked linkage ledgers, and original PDFs at restart_2026_11_26/fulltext_retrieval/pdf/<ID>.pdf in the attached HK261 folder. Verify access by reading a body page before extraction. The 21 added IDs are R0014 R0036 R0038 R0043 R0058 R0064 R0075 R0077 R0080 R0090 R0092 R0106 R0107 R0110 R0113 R0118 R0125 R0137 R0145 R0223 R0292.
2. Compare their publication metadata against each other and the existing 25 IDs in restart_2026_11_26/study_linkage/report_study_map.csv. Flag version claims or identity-level signals. Read both originals for each of these 11 candidates: R0014/R0003, R0014/R0010, R0014/R0015, R0014/R0059, R0014/R0062, R0036/R0048, R0075/R0080, R0110/R0074, R0118/R0083, R0137/R0045, R0106/R0054. Add other pairs with plausible identity-level signals. Preserve the 25 baseline dispositions unless direct new evidence calls a particular relation into question.
3. Decide each pair SAME_STUDY, DISTINCT, or UNRESOLVED using P07. For a merge require an explicit version relationship or two-sided evidence of the same underlying investigation with an established relationship. Shared authors, topic, method family, platform, or citation alone do not suffice. State any access or evidence gap explicitly.
4. Use 1-based physical PDF pages and short contiguous body excerpts without ellipses. Identify any additional credible candidate. State whether internal workers were used and their disjoint assignments. Read-only.

## REQUIRED OUTPUT
Compact JSONL, with 21 identity records and at least 11 pair records. Identity schema: {"kind":"identity","id":"R0014","title":"...","authors":"...","year":2024,"venue":"...","doi":"...","identity":{"source":"restart_2026_11_26/fulltext_retrieval/pdf/R0014.pdf","page":1,"section":"Title","quote":"..."}}. Pair schema: {"kind":"pair","a":"R0014","b":"R0062","decision":"DISTINCT","signal":"...","reason":"...","evidence_a":{"source":"...","page":1,"section":"...","quote":"..."},"evidence_b":{"source":"...","page":1,"section":"...","quote":"..."}}. End with a JSON summary naming returned keys, unresolved keys and concrete reasons, workers and assignments or parent-only, and completion status. Never represent examples as findings.

## ACCEPTANCE CRITERIA
A1. All 21 expected identities exactly once or explicit shortfall. All identity metadata has title, authors, year, venue, DOI or DOI_NOT_FOUND, and PDF identity locator. Zero duplicates after DOI/title normalization.
A2. All 11 required comparisons plus any additional credible pairs exactly once. Every assessment has evidence from both originals, each with file, physical page, section and contiguous excerpt. Zero unsupported claims or quantitative claims.
A3. Every SAME_STUDY has a two-sided relationship under P07. Every UNRESOLVED and every access shortfall names its cause. Zero missing or duplicate pairs or undisclosed shortfalls.
A4. One read-only native Task, no external processing of PDFs. Codex checks every adopted original-PDF locator and decision.

## BOUNDARIES
Use only the 46 current eligible reports. Do not re-screen, touch the three awaiting reports or R0116, use the historical corpus, extract operational content from R0063, report performance numbers, draft prose or edit any file.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
