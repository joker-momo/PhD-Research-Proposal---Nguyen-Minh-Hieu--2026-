## TASK

Reassess literal protocol domain9 for exactly7 remaining prior studies S18,S20,C02,C03,C04,C07,C08.

## REQUIRED WORK

1. Complete /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md and its required manifest. Read protocol.md section10 and interim_26report/eligibility_reaudit.csv for complete bibliographic identities.
2. Read original supplied full texts using these existing paths relative to the project: S18=sources/extracted_text_for_review/original20/10.1109_JIOT.2026.3685675.txt;S20=sources/extracted_text_for_review/original20/20_10.1109_ICWS72778.2026.00067.txt;C02=sources/extracted_text_for_review/new6/C02.txt;C03=sources/extracted_text_for_review/new6/C03.txt;C04=sources/extracted_text_for_review/new6/C04.txt;C07=sources/extracted_text_for_review/new6/C07.txt;C08=sources/extracted_text_for_review/new6/C08.txt.
3. Inspect methods/algorithms,evaluation configuration and artifact/data statements. Domain9 is "Code, data, traces, or sufficient implementation details are available." yes=public artifacts or report detail sufficient for complete independent implementation;partial=usable detail but missing implementation components;no=neither usable artifacts nor adequate implementation detail located;UNRESOLVED=unreadable/insufficient inspected evidence.
4. Distinguish standard public datasets,descriptive implementation information,and study-specific artifacts actually located. C08 links https://github.com/dream-lab/ocularone-scheduler;this was identity-checked,not replayed. Repository availability alone need not imply complete reproducibility.
5. Return exact copied bibliographic identities from the supplied CSV,zero duplicated author names. For each7 return at least2 original full-text method/evaluation locators,usable implementation components,source-located missing components and domain9 rationale. No other domain or eligibility changes.

## REQUIRED OUTPUT

Exactly1 JSON object:
{"records":[{"study_id":"S18|S20|C02|C03|C04|C07|C08","title":"...","authors":["..."],"year":2026,"venue":"...","doi":"...or DOI_NOT_FOUND","identity_locator":"interim_26report/eligibility_reaudit.csv:study_id=...","source_file":"existing absolute txt path","evidence":[{"locator":"file line/section/page/algorithm","observation":"..."}],"q9_verdict":"yes|partial|no|UNRESOLVED","q9_rationale":"source-located usable and missing components","study_specific_artifact_located":"yes|no|not_located","unresolved_items":[]}],"summary":{"requested":7,"returned":7,"duplicates":0,"unresolved_ids":[],"files_written":0}}

## ACCEPTANCE CRITERIA

T1: Exactly7 requested IDs;complete title,authors,year,venue,DOI/missing marker and identity-table locators for7;normalized DOI/title duplicates0;duplicate author names0.
T2: All7 absolute source paths exist and spell Bai_tap_ve_nha correctly;each adjudicated record has at least2 method/evaluation body locators within source;0 abstract-only judgments.
T3: All7 q9 rationales apply literal protocol and distinguish implementation descriptions from located study-specific artifacts;every positive artifact claim includes its URL/inspected evidence;C08 code not represented as replayed.
T4: Every factual claim has supplied-file or primary URL locator;unsupported scientific quantities0;missing evidence explicitly unresolved;0 other-domain/eligibility changes;one JSON object,counts agree,worker writes0.

## BOUNDARIES

Read-only research/classification only;no manuscript prose,publication tables,project/scratch edits,downloads,credentials or private files. Publication scope2021-01-01..2026-11-25. Preserve source-version caveats. Missing evidence must not be invented. Gemini primary;recognized quota only may use identical brief on gpt-5.6-luna/low;no escalation.
