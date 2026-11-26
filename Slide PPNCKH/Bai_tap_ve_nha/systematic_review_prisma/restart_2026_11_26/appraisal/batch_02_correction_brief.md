# TASK

Resolve five remaining P09 Batch 02 keys from native Gemini.app task be0b8973-d10e-419c-8698-dc00069feb3c, context a45bbde6-c714-4162-b075-1c3d57e2784b.

# REQUIRED WORK

1. Remain in the native parent Task without workers. Read P09 in `restart_2026_11_26/protocol_restart.md` and only R0010.pdf, R0015.pdf, R0019.pdf and R0022.pdf in the authorized project's `restart_2026_11_26/fulltext_retrieval/pdf/`. All originals passed earlier access probes. Report the ID and reason if access is now unavailable. Use direct original PDF viewing or local PyMuPDF when available, local MinerU then Marker only for persistent layout issues, and verify against the original page.
2. Recheck only the following five keys. Use physical pages and exact original section identifiers. Keep each quotation short and on one visible line wherever possible. Reuse prior verified report identities in the Batch 02 brief and locked P08.
   - R0010/D01: original p.3 §IV identifies the DRL allocation mechanism; the first response put its quotation on p.4. Use the actual p.3 line “pipeline collaborative DNN inference based on DRL, outlined”, p.4 Algorithm 1 title, or equivalent exact body anchor. Keep p.2/p.3 system and objective locators where needed.
   - R0015/D07: check static link and reachability assumptions on p.6 §IV.A and the stated intended scope and dynamic-network future work on p.7 §V. Describe the limitation without assuming the report claims validation under actual dynamic links. NO requires direct evidence of inadequacy relative to the claims. PARTIAL is allowed for demonstrated modeling and a specific untested condition.
   - R0015/D08: exact p.7 §V quote “time requirements. One promising future work would be using” or a shorter intact phrase and the p.6–7 results that bound the scope. The printed “real-time” wraps across a line. Contrast the exact bodies of the runtime claim, scope, and any missing evaluation criterion.
   - R0019/D09: identify all material examined, including p.9–11 §§III.C–IV settings and p.15 §V/end matter. A single end-matter locator cannot support a claim that both methods and end matter were examined. Cite a reading locator for each inspected section, using null quotation for silence. Any named third-party tool is distinct from an author release.
   - R0022/D08: use p.5 §IV experiment setup and p.6 §V conclusion. Distinguish results bounded to the simulation from a statement that the method “shows promise for real-world deployments”; the latter is not a field-validation claim. Use the exact scope and confirm whether the claimed breadth exceeds that described.
3. Limit each rationale to 30 words and use concise qualitative wording. Retain units and conditions if using a numerical result, otherwise omit numerical magnitudes. Report tools used and explicit unresolved keys.

# REQUIRED OUTPUT

Return one JSONL object per fixed key in this schema:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"The setup names the workload, but the random seed is unreported.","locators":[{"page":4,"section":"Methods, Setup","quote":"an exact short body phrase"},{"page":5,"section":"Methods, Setup","quote":null}]}
Allowed judgments: YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE, NOT_YET_ASSESSED. End with one object containing returned_keys, unresolved, workers_used=false, and tools. End with P09_B02_CORRECTION_COMPLETE on its own line.

# ACCEPTANCE CRITERIA

- Exactly five distinct authorized keys or explicitly documented shortfall, zero repeats, extra keys and invalid enums.
- All edited rationales and short exact quotes match original page(s)/section(s). Zero unsupported raw quantities or assertions about scope, uncertainties, or unavailable information. For NOT_REPORTED locate each searched section.
- One parent Task, zero workers or changes to project files. List unavailable original PDFs/tools and all unresolved keys.

# BOUNDARIES

No further records, no external discovery, no uploads or project edits, and no rewriting accepted keys.

Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
