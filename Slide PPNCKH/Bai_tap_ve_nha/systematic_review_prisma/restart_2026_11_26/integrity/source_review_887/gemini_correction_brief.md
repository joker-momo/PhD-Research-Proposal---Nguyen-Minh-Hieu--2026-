## TASK

Correct only previously failed or missing keys explicitly listed in the attached HK261 targets.json.

## REQUIRED WORK

1. Open HKF-118.pdf itself and check physical page 2. Report one exact body-text anchor, title and section. If direct PDF access fails, record the failure and stop.
2. From targets.json, read each report's failed or missing keys, reasons and attached PDF page map. Check the relevant original page objects in the supplied PDFs visually, including figures, formulas and table captions/cells. Map physical page numbers in each attached subset back to full original physical page numbers via `attachment_physical_to_original_physical`, which is indexed from 1.
3. For each requested key, independently decide what the supplied pages support. Preserve numerical units, signs, explicit approximations, row/column labels, comparator, conditions and denominator. A readable number printed next to a bar is a printed numerical label. Extractor omissions are not scientific omissions. If a required page or detail is unavailable, report the gap. Report original contradictions without averaging or resolving them by guesswork.
4. For appraisal, begin the finding with YES, PARTIAL, NO, NOT_REPORTED or NOT_APPLICABLE. Choose the separate outer status according to evidence completeness from the allowed values below. For coverage, begin the finding with VERIFIED_EXACT, PLOT_ONLY, or PRINTED_UNRESOLVED.
5. Give one metadata line per target report checked, from the supplied original first page. Give title, authors, year, venue and DOI, or explicit UNKNOWN or DOI_NOT_FOUND.

## REQUIRED OUTPUT

First write PREFLIGHT and a JSON object with file, title, page, section and quote. Then emit one JSON object per requested key. Keep the finding to 45 words where possible, JSON-escape embedded quotation marks, and include exact contiguous evidence. The following is a schema example. Use only actual IDs, keys, values and original physical locations from attachments.

```json
{"id":"HKF-118","kind":"appraisal","key":"D01","status":"PARTIAL","finding":"PARTIAL: Evidence statement","evidence":[{"page":2,"section":"Exact section or figure/table locator","quote":"short exact contiguous text or printed cells"}],"note":"Verified scope or specific evidence gap."}
```

Outer status must be VERIFIED, PARTIAL, NOT_REPORTED or UNRESOLVED. For unreadable pages and missing evidence, include the supplied source and original page checked if known, plus the exact limitation in note. Use empty evidence only for a documented access gap. List identities once outside the JSONL as `HKF-nnn | Title: … | Authors: … | Year: … | Venue: … | DOI: …`. Finish with total returned, all unresolved keys and END_HK261_SOURCE_BATCH.

## ACCEPTANCE CRITERIA

- One exact PDF preflight anchor on physical page 2. Every requested key once or enumerated in the shortfall. Zero malformed, unexpected or duplicate keys.
- One scholarly identity per accessible target report with required fields. Zero duplicate normalized DOI/title for distinct reports or explicit family relationships.
- Every factual claim has a verifiable attached-file locator, original physical page and short original quotation or printed value. Quantitative claims include units and scope. Zero unsupported quantitative findings or unreported gaps. Each candidate conclusion remains subject to independent Codex verification.

## BOUNDARIES

Read only the attached files. Use native PDF reading on the supplied subsets. Do not open other folders, transfer the attachments, use other websites or write to the project, including R1/R2. Do not extract operational military, combat, targeting or weapon details, scenarios or effect metrics. Restrict any dual-use report to non-operational bibliographic and scholarly assessment. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
