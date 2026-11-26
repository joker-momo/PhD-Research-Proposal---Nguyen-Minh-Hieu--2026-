# TASK
Audit the eight executed HK261 query variants against the accepted restart protocol and official platform documentation. Return structured evidence only.

# REQUIRED WORK
1. In the attached live HK261 review directory, read restart_2026_11_26/protocol_restart.md and restart_2026_11_26/step01_inventory.json. Each query_evidence entry names its corresponding local run artifact. Read those eight artifacts and the ACM capture manifest cited in corpus_expansion/acm_record_capture_2026-11-26.json.
2. For IEEE Xplore, ACM Digital Library, Scopus, and OpenAlex, check the fields, Boolean syntax, language, publication type, and time filters against the accepted protocol. Verify platform behavior against the platform's own documentation when accessible. Distinguish documented behavior from local observations and unresolved assumptions.
3. For each high_recall and complementary variant, compare the exact executed query to the protocol topics. Explain any avoidable coverage trap and distinguish a required correction from an explicit downstream filter or coverage limitation. Use current inputs only. Do not run or change queries.
4. For ACM distinguish the two reported hit counts and later row capture from the blocked native citation export. For IEEE and Scopus preserve the timestamp basis. Treat OpenAlex as supplementary and WoS as unavailable/unsearched, with a null count.

# REQUIRED OUTPUT
One JSON object with keys runs, platforms, unresolved, wos_reported_total, actions, scholarly_records, scholarly_records_not_applicable. runs contains eight objects with platform, variant, local_locator, count, observed_at, timestamp_basis, query_field, filters, verdict (RETAIN, REVISE, or UNRESOLVED), rationale, and proposed_edit (null unless REVISE). platforms contains four objects with platform, official_url (null with access reason if unavailable), official_support (brief description identifying the relevant documentation section), and limitations. unresolved explicitly lists missing or conflicting evidence. actions is {"formal_queries_executed":0,"project_edits":0,"records_screened":0}. scholarly_records is [] because no paper discovery is requested.

# ACCEPTANCE CRITERIA
C1. Valid JSON with exactly eight unique platform/variant pairs and four unique platform summaries.
C2. All eight local locators, recorded times, and counts match the archived evidence. ACM capture is 79 and 325 positions, not a native export. WoS total is null.
C3. Every platform claim is supported by an official documentation URL and relevant section or clearly marked as a local observation or unresolved. Unsupported factual and quantitative claims equal zero.
C4. One verdict per variant. Every REVISE has a specific edit and rationale tied to the protocol. Missing evidence is listed. No estimates of true recall or completeness.
C5. No formal queries, edits, screening, or historical 46-report calibration. No scholarly records with an explicit not-applicable reason.

# BOUNDARIES
Read the named project documents and the files they cite for the eight executed searches. Use public official platform documentation for verification. Read only; do not edit project files, access other folders, open credentials, create manuscript text, run formal database searches, or use Web of Science.
