# TASK

Correct exactly 9 P09 appraisal keys screened by Codex from the completed Batch 04 native Gemini.app task 2e19b1a7-4fc2-4202-9e5b-a86a91e1ca2c (context 1828a7ac-c2ee-4dff-a59a-d2b9fcb22228).

# REQUIRED WORK

1. Read only the named project-relative original PDFs under `restart_2026_11_26/fulltext_retrieval/pdf/` in the attached canonical HK261 directory, confirm access by exact body quotations in the output, and report inaccessible IDs with a reason. The locked P08 and P09 protocol in `restart_2026_11_26/` give identity and domain definitions. Use the parent only. Use local PyMuPDF if available, then local MinerU/Marker only if layout needs it. State tools actually used.
2. Address exactly these nine keys. Re-read the cited pages and reason from the source. The values below are physical one-based PDF page locators, not printed journal labels:
   - `R0062/D07`: pp5–6, separate what the paper actually calls its embedded prototype from the absence of documented actual flight-network validation. Do not introduce “benchtop” unless expressly supported.
   - `R0062/D08`: p7 Conclusion and pp5–6 proof of concept or challenges. Bound what was demonstrated without assuming the physical deployment setup or calling follow-up work completed.
   - `R0063/D04`: distinguish the comparator inventory from the principal comparison and the selected cross-play subset in §5.2.1 p13. Do not imply one identical test protocol for all listed comparators. Use qualitative methodological language and avoid unnecessary mission details.
   - `R0063/D06`: locate independent trials in §5.2.1 p13, qualify by evaluated experiment, and distinguish dispersion printed in specific tables from training-seed details or broader independent repeat counts. Do not claim that all Tables 5–12 lack dispersion. Use qualitative language.
   - `R0063/D07`: use §§5.1 and 6 pp11 and 20 to distinguish simulated dynamics and the limits of transfer to physical deployment. Omit unsupported numeric timing and unnecessary operational detail.
   - `R0068/D06`: prior convergence quotation is on physical p10, not p11. Verify caption or results text and distinction between episode-based curves and independent repeated runs.
   - `R0068/D08`: show that the paper explicitly labels simulation, distinguish broadly phrased applications, and identify follow-up on factors left untested without asserting simulation bounds were absent.
   - `R0068/D10`: p1 author/title footnote is research funding, p15 is publication Open Access funding, p13 Conclusion identifies untested aspects. Check end matter for conflict reporting without inferring conflict or absence of conflict.
   - `R0073/D05`: p9 §5.1 and p11 §5.2. Replace the quote broken by end-of-line hyphenation with a short exact contiguous clause on one printed line. Preserve latency and resilience metric scope.
3. Give exactly one compact source-grounded replacement per key. Link source page and present exact words. Use PARTIAL for a documented mixed case and NOT_REPORTED only with checked sections. One consolidated result, no workers, no changes to the 41 keys outside this list.

# REQUIRED OUTPUT

Compact JSONL. Exact fields and enums: report_id, domain, judgment (YES / PARTIAL / NO / NOT_REPORTED / NOT_APPLICABLE / NOT_YET_ASSESSED), rationale, and locators, each with page, section and short exact contiguous quote (null only for inspected absence). Project-relative PDF is identified by report ID above. Synthetic format example:
{"report_id":"RTEST","domain":"D05","judgment":"YES","rationale":"The declared timing metric measures the defined test target.","locators":[{"page":4,"section":"Simulation Setup","quote":"simulation time was recorded for each run"}]}
End with one summary object with returned_keys (array of IDs), unresolved (array with IDs and reason), tools and workers_used (boolean). End with `P09_B04_CORRECTION_COMPLETE` alone on a line.

# ACCEPTANCE CRITERIA

9/9 exact keys, 0 duplicate/extra/malformed keys, and 0 unlocated factual assertions. Every decision cites a physical page and rationale. All non-null quotes must match the exact PDF/page and support the relevant rationale. Zero unsupported numerical facts, scope attributions, or inferences from silence. List unresolved keys explicitly. Preserve other 41 keys.

# BOUNDARIES

Read-only named project inputs, no external upload, no workers, no changes to any project file, no final prose, no new reports. Use already verified P08 metadata and no abstract evidence. Limit the output to methodological appraisal.

Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
