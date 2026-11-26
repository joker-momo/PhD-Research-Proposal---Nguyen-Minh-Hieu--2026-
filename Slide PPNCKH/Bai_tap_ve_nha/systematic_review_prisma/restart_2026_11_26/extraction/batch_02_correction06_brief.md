# TASK
Correct only the inherited P08 outcomes field for R0068, R0074 and R0121. Original parent e891c230-d182-4bfa-8068-1cba64226569, latest correction e6c139ad-e556-47be-a24a-da94c4de1a9f. Do not return other fields or amend any earlier verified numeric key.

# REQUIRED WORK
1. Open R0068.pdf, R0074.pdf and R0121.pdf directly under restart_2026_11_26/fulltext_retrieval/pdf/ in the attached project. For each report return the exact relative path and one 8–18 word contiguous body quote under an actual section heading and on a 1-based physical PDF page, or cite the access failure. The parent can handle three files. Only use workers that can be verified to open them; no overlapping assignment.
2. K01, R0068: check physical pages 10–13 (Section VI and conclusion). Exclude three PP percentages found only in the abstract (~29%, ~23%, ~9%). Return source-located qualitative comparisons only if verified, preserving comparable algorithms and test conditions. Explicitly list the percentages as withheld, without supplying them as results or deriving replacements from plots.
3. K02, R0074: open Section 4.2, physical pages 16–17. Narrow the finding about running the 70B model to what the full text shows. Distinguish compared methods that succeeded from cloud-edge baselines that failed in that scenario. Zero unsupported exclusivity. Do not repeat already verified timing entries.
4. K03, R0121: split the compound outcome into single evidence statements. Check body tables and the surrounding results, including physical page 7. If reporting a number, give exact printed value, units, relevant baseline and denominator, workload, conditions and a true exact quote or printed row locator. Underlying table cells can be cited independently. Withhold ratios or outcomes whose only direct anchor is the abstract. Do not compute novel percentages or ratios.

# REQUIRED OUTPUT
One line P08_DELEGATION followed by JSON with subagent_status (USED_CONFIRMED, UNAVAILABLE, UNCONFIRMED), reason and assignments [{worker,report_ids}]. One line P08_ACCESS followed by JSON with reports [{report_id,pdf_path,status,page,section,excerpt,reason}]. Access status OBSERVED or NOT_ACCESSIBLE; for the latter use page:null, concise reason, empty excerpt and section.
Between standalone lines P08_FIX_BEGIN and P08_FIX_END return precisely 3 compact JSONL objects, one per key. All asserted facts must be atomic. Exact schema example (illustration only):
{"key":"K01","report_id":"R0068","field":"outcomes_latency_energy_communication_accuracy_reliability_and_scalability","assertions":[{"status":"OBSERVED","finding":"one outcome only","page":11,"locator":"VI-B.2, exact location","excerpt":"short verbatim contiguous excerpt","quantitative":null}],"withheld":[{"topic":"one unsupported result","reason":"only sourced by abstract","checked":"physical pages and section"}]}
Status OBSERVED only for assertions proven by body evidence. Put unresolved facts in withheld, not assertions. If quantitative is non-null, it has exactly {value,units,baseline,denominator,workload,conditions}. All are nonempty strings. Use one short exact contiguous excerpt per assertion and a precise table row/column locator when relevant. End with P08_SUMMARY JSON listing returned_keys and unresolved_keys, then standalone P08_COMPLETE.

# ACCEPTANCE CRITERIA
A1: 3 keys exactly once, 3 locked report IDs as specified, 0 extras or duplicates, 0 overlap. Three access dispositions.
A2: 100% of observed assertions from verified body pages, exact source excerpts and locators checked independently. 0 abstract-only results.
A3: K01 excludes all 3 unsupported percentages. K02 contains 0 exclusivity claims contradicted by physical pages 16–17. K03 is atomic and has 0 unsupported quantitative subcomponents.
A4: 0 invented values, precision, units, baselines or conditions. Unknown or unsupported content explicitly withheld. Names and terms follow their source.
A5: Exactly three independently parseable JSONL rows with the exact field name. End markers and summaries match. One parent Task; truthful worker disclosure.

# BOUNDARIES
Read only the three authorized PDFs. No external search, edits, narrative prose, duplication of PASS keys, new report IDs or operational details. The abstract can only explain why a numeric assertion is withheld. Report gaps rather than guessing.
