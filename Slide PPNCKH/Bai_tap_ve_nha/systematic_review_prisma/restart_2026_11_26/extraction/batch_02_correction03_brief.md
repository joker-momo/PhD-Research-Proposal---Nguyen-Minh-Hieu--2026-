# TASK
Resolve eight remaining source checks and one schema confirmation for P08 batch 02. Parent: e891c230-d182-4bfa-8068-1cba64226569. Prior correction: 009b3595-4bfd-4683-96af-6d2f3136fa7f.

# REQUIRED WORK
1. Read P08 and open the four specified PDFs directly in the attached directory. Before processing, provide a short exact contiguous body quote and 1-based physical page from one of these PDFs. Do not substitute metadata or a snippet. If parent access fails, stop and list the affected report IDs and reasons. Use workers only if verified to share the parent attachment; otherwise parent handles all IDs. Use only one reader assignment per report.
2. For C01, C09 and C10, report inspected physical page (an integer), the actual section checked and a short verbatim section heading, with reason for NOT_REPORTED. If you cannot establish absence from inspected text, use UNVERIFIED and explain. For observations cite one true contiguous excerpt on the identified physical page.
3. For C02, C03, C04, C05 and C07, locate the exact value in text or a legible table. Use separate table locator (label plus row and column) and one exact contiguous short excerpt on that physical page, e.g. the caption text as printed, without concatenating separate table columns. Do not copy simulated or rounded plot estimates as exact numbers. Use UNVERIFIED with reason for any number lacking exact support. Report units, conditions, workload, baseline and denominator where applicable; when inapplicable, write NOT_APPLICABLE with a short reason.
4. Return SCHEMA with exactly the two unresolved objects and their fields below. Array wrapping and field-name preservation are deterministic at merge; do not rename or return the 14 existing P08 fields.

# REQUIRED OUTPUT
One P08_DELEGATION JSON line with subagent_status (USED_CONFIRMED, UNAVAILABLE, UNCONFIRMED), reason and assignments [{"worker":"parent","report_ids":["R0054","R0062","R0095","R0121"]}] if the parent works alone. One P08_ACCESS JSON line with pdf_path, page, excerpt. Then one compact independently parseable JSON object per key between standalone P08_FIX_BEGIN and P08_FIX_END. Each source object has key, report_id and replacement. Allowed field statuses: OBSERVED, NOT_REPORTED, NOT_YET_ASSESSED, NOT_ACCESSIBLE, UNVERIFIED. Allowed measured statuses: OBSERVED, UNVERIFIED. Example of exact field schema shape with illustration only, never return this fake key or evidence:
{"key":"EXAMPLE","report_id":"EXAMPLE","replacement":{"subtopic":"code_and_data","status":"UNVERIFIED","finding":"","page":null,"locator":"","excerpt":"","reason":"Body could not be read."}}
Metric replacement keys: metric, value, units, baseline, denominator, workload, conditions, page, locator, excerpt, status, reason. SCHEMA format: {"key":"SCHEMA","r0121_unresolved":[{"field":"code_and_data","reason":"actual reason","checked":"actual file and page/section"},{"field":"funding_and_conflicts","reason":"actual reason","checked":"actual file and page/section"}]}. End with P08_SUMMARY JSON containing returned_keys and unresolved_keys (arrays). If parent access fails, instead return P08_ACCESS containing status NOT_ACCESSIBLE and report_ids with reasons, zero invented rows.

# ACCEPTANCE CRITERIA
A1: One access quote on the declared body page; exactly eight specified source keys plus SCHEMA if access passes, 0 extra/duplicate, 4 assigned IDs exactly once. Identity retained from locked metadata, no new records.
A2: Every OBSERVED or NOT_REPORTED entry has an actual PDF and a matching short verbatim anchor on the identified physical page. All unresolved items are explicit.
A3: Every exact value has traceable original value, precision, units, workload and conditions, plus applicable denominator and baseline. Unsupported numerical claims = 0.
A4: Codex independently checks 100% of assertions proposed for adoption against the actual source, including table cells and exact scope. Provenance mismatch = 0.
A5: Schema and enums valid, two structured R0121 explanations, correct returned and unresolved key summary and no unconfirmed claim of worker use.

# BOUNDARIES
Attached project and named PDFs only. No external searches, file edits, prose, new evidence keys, operational details for sensitive applications, or Batch 01. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.

## Allowed keys
- R0054, `restart_2026_11_26/fulltext_retrieval/pdf/R0054.pdf`: C01 failure/recovery, C02 normalized holdout cost, C03 active admission, C04 data rate.
- R0062, `restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf`: C05 collaborative inference frame rate.
- R0095, `restart_2026_11_26/fulltext_retrieval/pdf/R0095.pdf`: C07 average decision time.
- R0121, `restart_2026_11_26/fulltext_retrieval/pdf/R0121.pdf`: C09 code/data, C10 funding/conflicts, SCHEMA.
