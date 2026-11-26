## TASK
Correct exactly three quote locators in rejected parent 01a21559-eec5-7109-9445-388ddba4e2e1 (context 01a21559-eec5-71bd-88ad-9cb52a8ec751). This is a local excerpt-verification task, not a new eligibility assessment.

## REQUIRED WORK
1. Read the preserved parent JSON and review below, then canonical source text for C06 and SNCS. Do not edit any file. Use PYTHONDONTWRITEBYTECODE=1 for Python inspection.
2. Replace exactly C06_E4: current opening sentence is a paraphrase, not an exact quote. Read C06 p20 lines1031–1048; select one contiguous 1–40-word excerpt from the Only-A3C baseline/environment passage. Keep context separate from verbatim quote; do not concatenate separate sentences after deleting intervening text.
3. Replace exactly SNCS_E2: current excerpt has43 words. Select a shorter contiguous 1–40-word excerpt at p17 lines1353–1358 that supports the hierarchical UAV setup. No ellipses or paraphrase inside quote.
4. Replace exactly SNCS_E3: the video/Jetson/YoloV8 text is at p17 lines1398–1402, not p19. Preserve the inline [48] citation if it lies inside the quote. Select one contiguous 1–40-word excerpt and correct page/line range.
5. Verify all3 excerpts against supplied text using whitespace/ligature normalization only. Return metadata for the two source reports copied exactly from parent. Do not reproduce or change the other17 quotes, any status/gate/decision/interpretation, or publication metadata. If a target cannot be verified return it unresolved rather than fabricate.

## REQUIRED OUTPUT
One JSON object without fences:
{"task":"scope_01_locators","parent_task_id":"01a21559-eec5-7109-9445-388ddba4e2e1","sources":[{"id":"C06","title":string,"authors":array,"year":integer,"venue":string,"doi":string},{"id":"SNCS","title":string,"authors":array,"year":integer,"venue":string,"doi":string}],"replacements":[{"report_id":string,"evidence_id":string,"file":string,"page":integer,"line_range":[integer,integer],"quote":string}],"unresolved":[],"shortfall":[],"project_files_changed":0,"final_prose_written":false}
Replacements exactly in order C06_E4,SNCS_E2,SNCS_E3. file is the canonical project-relative text path; use PDF page markers, not printed article page numbers. No explanatory prose outside JSON.

## ACCEPTANCE CRITERIA
L1: Exactly3 replacements with the requested IDs/order,0 duplicate IDs,0 extras; parent ID exact; exactly2 source records C06,SNCS with title/authors/year/venue/DOI (or DOI_NOT_FOUND) equal parent,0 normalized DOI/title duplicates.
L2: 3/3 contiguous quote/page/line matches; each1–40 whitespace-delimited words; no invented, concatenated, shortened-by-omission or paraphrased quotation; all factual output has supplied-file locator; unsupported quantitative claims=0.
L3: Replacement objects have only required fields and valid source paths; exactly3 evidence objects will change when Codex combines them into the preserved parent. Other17 quotes and all5 records' non-evidence data remain byte-value-equivalent; combined checker must pass20/20 locators.
L4: unresolved and shortfall arrays explicit; if missing evidence document it and do not imply success. project_files_changed=0 and final_prose_written=false. No new eligibility/date/identity/family claim.
L5: Original combined A1–A6/C1–C2 are rechecked by Codex after combination; provider completion alone does not accept evidence.

## BOUNDARIES
Read-only supplied full texts only; no web, downloads, project writes, shell mutations, Git, submission, email, protocol or corpus changes. No secrets. Publication window remains2021-01-01..2026-11-25. Do not write final prose. Codex owns combination and acceptance. Quote correction does not settle C06/SNCS uncertainty or human adjudication.
Parent JSON: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reconciliation/results/scope_01_correction_fallback.json
Review: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/reconciliation/reviews/scope_01_correction_review.md
C06 text: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/C06.txt
SNCS text: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/screening_46/text/SNCS.txt
