## TASK

Correct only the invalid S05/S07 source paths and clarify S08 artifact scope from rejected domain9 task01a2124e-1c10-794a-bf75-dcfb07e93780.

## REQUIRED WORK

1. Read /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/corpus_expansion/domain9_reaudit_batch1_notes.json and domain9_reaudit_batch1_review.md. Complete the original project's mandatory onboarding before source work.
2. Return exactly3 records S05,S07,S08. For S05 and S07 verify actual full-text files in /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/sources/extracted_text_for_review/original20/; the prior absolute paths misspelled Bai_tap_ve_nha as Bai_tap_ve_ha. Supply existing absolute file paths and preserve or correct body locators after inspecting them.
3. For S08 distinguish a standard dataset named/declared public in the paper from an actually located study-specific implementation/data/trace artifact. Return public_dataset_statement separately from study_specific_artifact_located. Do not treat an unlinked Data Availability declaration as a repository actually opened.
4. Preserve complete source-located title,authors,year,venue,DOI and q9_verdict/rationale for all3. Apply literal protocol code/data/traces OR sufficient implementation details. Report unresolved items. No changes to the5 other ratings or eligibility.

## REQUIRED OUTPUT

Exactly1 JSON object:
{"records":[{"study_id":"S05|S07|S08","title":"...","authors":["..."],"year":2022,"venue":"...","doi":"...","identity_locator":"...","source_file":"existing absolute txt path","evidence":[{"locator":"file line/section locator","observation":"..."}],"q9_verdict":"yes|partial|no|UNRESOLVED","q9_rationale":"...","public_dataset_statement":"source-located claim or not_located","study_specific_artifact_located":"yes|no","unresolved_items":[]}],"summary":{"requested":3,"returned":3,"duplicates":0,"files_written":0},"corrections":[{"field":"...","correction":"...","source_locator":"..."}]}

## ACCEPTANCE CRITERIA

H1: Exactly3 records S05,S07,S08,all bibliographic fields and supplied identity locators present;normalized duplicates0.
H2: All3 absolute source_file paths exist;at least2 body locators per record spanning methods/evaluation;the2 Bai_tap_ve_ha typos removed.
H3: S08 standard-dataset statement separate from study_specific_artifact_located;any yes for located artifact requires its exact repository URL and inspected evidence;unlinked declaration alone cannot establish located study-specific artifact.
H4: Every factual claim has supplied-file locator;unsupported quantitative scientific claims0;unresolved arrays for3;no changed eligibility/other domain;files_written0;one JSON object.

## BOUNDARIES

Read-only structured source correction only;no final prose,project/scratch edits,downloads,private materials,credentials or invented evidence. Gemini primary;recognized quota only may route unchanged brief to gpt-5.6-luna/low;no escalation. Missing evidence is explicit.
