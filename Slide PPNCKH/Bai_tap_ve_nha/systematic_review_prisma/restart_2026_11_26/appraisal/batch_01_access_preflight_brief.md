# TASK

Run parent-only PDF access preflight for the five P09 Batch 01 reports after the access failure in task `ddbb7eda-d194-4a22-bbe0-820cb63d9644`, context `ee4e00b0-a377-4126-a4e2-2db4436c6f78`. This is a new narrow correction, not a repeat appraisal.

# REQUIRED WORK

1. Stay in this parent Gemini.app Task. Do not call, delegate to, or wait for any worker. The previous worker handoff lost access to the attached local project; inspect the PDFs using the original parent local connected-folder tools, within this turn.
2. Read just the specified body page of each attached PDF and return an exact short contiguous phrase from there. Read the actual PDF. Do not get phrases from the P08 table, memory, any web page or a similarly titled document. Use local PyMuPDF if available. Use local MinerU then Marker only if page layout prevents reliable direct reading and tools are available. If no PDF-reading tool is available, report it immediately per ID.
3. Use physical PDF page numbering (1-based). Exclude headers, title, abstract, references, watermarks and uploader notices. List the real access tool/error for any failed ID. Never claim access without a page excerpt.

| Report | Physical page | Project-relative PDF |
|---|---:|---|
| R0001 | 2 | restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf |
| R0002 | 7 | restart_2026_11_26/fulltext_retrieval/pdf/R0002.pdf |
| R0003 | 5 | restart_2026_11_26/fulltext_retrieval/pdf/R0003.pdf |
| R0006 | 6 | restart_2026_11_26/fulltext_retrieval/pdf/R0006.pdf |
| R0009 | 8 | restart_2026_11_26/fulltext_retrieval/pdf/R0009.pdf |

# REQUIRED OUTPUT

Exactly five JSONL records. Synthetic schema example:
{"report_id":"RTEST","access":"READ","pdf_path":"relative/report.pdf","physical_page":2,"section":"Methods","quote":"a contiguous phrase from the source","tool":"parent local file reader","reason":null}
Only READ or NOT_ACCESSIBLE. For NOT_ACCESSIBLE keep the requested path, use null for physical_page/section/quote and provide the actual reason. Finish with `P09_B01_PARENT_PREFLIGHT_COMPLETE` on its own line (inside the bridge result envelope). Identity metadata is unchanged from the committed batch brief and locked P08.

# ACCEPTANCE CRITERIA

- 5 exact unique requested IDs, zero extras, zero workers.
- 5/5 READ across the exact requested paths and pages, and 5/5 matching non-abstract body excerpts. If any fails, list exact ID, tool, and reason so Codex can attest shortfall; no full appraisal result is requested.
- Zero invented quotes, page numbers, access claims or substantive judgments.

# BOUNDARIES

Parent only. Do not search the internet, launch workers, edit or upload any file, assess domains, or alter P08. Read only the named five PDFs.
