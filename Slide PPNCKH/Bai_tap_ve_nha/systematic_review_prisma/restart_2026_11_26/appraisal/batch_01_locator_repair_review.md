# Batch 01 · Locator repair and final integration

Reviewed at `2026-11-27T01:02:32+07:00`. Native Gemini.app Task `8a5f0cb9-1977-4914-a564-e3e8e449bbe8` and context `688ff68a-6073-4e0a-8149-80b142b4b94b`. One dispatch.

| Criterion | Raw Gemini result | Final batch | Evidence |
|---|---|---|---|
| Scope and JSONL | PASS | PASS | 6/6 targeted keys. Integrated 34 unaffected initial keys, 10 keys from the first targeted correction and six keys from this return. Final 50/50 distinct keys, zero duplicate/missing/extra. |
| Original full-text access and provenance | PASS | PASS | Original access probes previously checked on 5/5 PDFs, backed by locked P08 path and SHA-256 per row. Parent Task only. |
| Original-PDF page and exact wording | FAIL | PASS | Five of six raw keys contain layout/typographic mismatches. Codex preserved the rejected verbatim response, clipped each offending locator on the same PDF page, and rendered five affected paper regions via PyMuPDF 1.26.7. All 117 final locators checked, including 88 exact quotes and 29 inspected section locators. Zero mismatched final quotes. |
| Judgment support and quantity provenance | PASS | PASS | Rechecked all 50 original-source rationales, with explicit corrections of scope under `review_edit`. No new measurement values used. R0006/D08 pertains exclusively to the reported scenario and coverage language on p.6. |
| Tool, unresolved and independence disclosures | PASS | PASS | Zero unresolved final keys, no workers or independent human reviewer claimed, no summed score or screening changes. |
| Durable receipt and chat cleanup | PASS | PASS | One send, full result kept, exact UUID deletion verified by bridge. |

The raw locator-repair output failed the literal-quotation criterion and is quarantined as received. Batch PASS applies only to the integrated, independently verified judgments. The five clipped passages were demonstrably equivalent on the same original pages. No appraisal classification was inferred from a repaired transcription. All four future briefs specify parent-only access and shorter literal quotes based on the observed failure. This does not change the locked P08 corpus or the ten P09 domains.
