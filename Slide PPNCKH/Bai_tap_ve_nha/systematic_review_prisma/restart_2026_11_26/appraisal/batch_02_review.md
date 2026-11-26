# Batch 02 · Appraisal source review

Reviewed at `2026-11-27T01:09:07+07:00`. Native Gemini.app Task `be0b8973-d10e-419c-8698-dc00069feb3c`, context `a45bbde6-c714-4162-b075-1c3d57e2784b`. Sent once.

| Criterion | Verdict | Evidence |
|---|---|---|
| Expected appraisal keys and correct JSONL | PASS | 50/50 distinct expected keys, 0 missing, duplicated, extra or malformed. |
| Original PDF access | PASS | 5/5 probe passages match the exact physical page of the SHA-256-verified original PDF. |
| Source locators | FAIL | Raw output provided 130 locators and 99 exact quoted locators. R0010/D01 attributes an algorithm description from p.3 to p.4. R0015/D08 needs a short verbatim p.7 quotation that avoids line-wrap hyphenation. R0019/D09 lacks an inspected Methods/settings locator. |
| Judgments match the evidence | FAIL | R0015/D07 assigns NO without demonstrating inadequate modeling relative to the specific claims, and R0022/D08 treats future promise as overclaiming without comparing the original evaluation scope. No unsupported numerical results were adopted. |
| Unresolved and worker/tool disclosures | PASS | 0 provider-reported unresolved keys, 0 workers reported, one parent response and tool limitations disclosed. Codex isolated the five exceptions above. |
| Durable result and chat cleanup | PASS | One dispatch, raw result saved, bridge verified empty new chat after deleting the exact UUID. |

All 50 keys were checked against the original source. PyMuPDF renders cover R0019 p.11 Table II, R0022 pp.5–6 Figures 3–6 and R0029 p.5 Figures 4–5. The raw response remains quarantined. The 45 other keys are held for final integration. The accepted scope remains 5/25 reports and 50/250 judgments overall.
