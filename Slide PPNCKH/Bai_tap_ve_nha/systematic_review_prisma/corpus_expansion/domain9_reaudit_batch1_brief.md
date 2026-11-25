## TASK

Reassess protocol domain9 for exactly8 existing studies S01,S02,S04,S05,S06,S07,S08,S09 using their supplied original full texts.

## REQUIRED WORK

1. Complete project onboarding: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md and required manifest. Use only public scholarly sources. Read protocol.md section10, interim_26report/eligibility_reaudit.csv and quality_appraisal_eligible.csv for identities and original ratings.
2. For these8 IDs locate readable source text in sources/extracted_text_for_review/original20/ using the pdf_file stem in eligibility_reaudit.csv. The originals are supplied published or author reports; retain source-version limitations. Read methods/algorithms plus evaluation configuration and code/data statements. Do not rely only on abstract or old rating.
3. Apply the literal domain9: "Code, data, traces, or sufficient implementation details are available." yes=public artifacts or report detail sufficient for a complete independent implementation; partial=some usable algorithm/configuration details but missing artifacts or implementation components; no=neither usable artifacts nor adequate implementation detail located. Do not equate absent GitHub with no. This is a clarification within the fixed criterion, not a change to eligibility.
4. Return each record's title,all authors,year,venue,DOI from the supplied identity table, source file and at least2 methods/evaluation locators, descriptive implementation components, remaining missing components, public_artifact_found and q9_verdict/rationale.
5. Report unreadable/missing evidence explicitly as q9_verdict=UNRESOLVED. Do not invent absence. Change no other domain or eligibility decision.

## REQUIRED OUTPUT

Exactly1 JSON object:
{"records":[{"study_id":"S01","title":"...","authors":["..."],"year":2021,"venue":"...","doi":"...or DOI_NOT_FOUND","identity_locator":"interim_26report/eligibility_reaudit.csv:study_id=S01","source_file":"absolute supplied txt path","evidence":[{"locator":"section/page/algorithm/table","observation":"descriptive implementation detail or scoped missing item"}],"q9_verdict":"yes|partial|no|UNRESOLVED","q9_rationale":"source-located rationale","public_artifact_found":"yes|no|not_located","unresolved_items":[]}],"summary":{"requested":8,"returned":8,"duplicates":0,"unresolved_ids":[],"files_written":0}}
No Markdown or final prose.

## ACCEPTANCE CRITERIA

G1: Exactly8 records with requested IDs or explicit documented shortfall; every requested ID present even if UNRESOLVED.
G2: Title,all authors,year,venue,DOI/missing marker and identity table locator present for each8;0 normalized duplicate DOI/title records.
G3: Each adjudicated record has absolute supplied source file and at least2 body locators spanning implementation and evaluation;0 abstract-only adjudications; missing texts=UNRESOLVED.
G4: Each q9 verdict distinguishes descriptive implementation detail from repository availability;0 changes to other domains/eligibility; public_artifact_found separate.
G5: Every factual observation has supplied-file locator;unsupported quantitative scientific claims=0;unresolved_items array for8 records;summary counts agree;files_written=0.

## BOUNDARIES

Read-only source extraction/classification only;no manuscript prose,publication tables,project edits,downloads/scratch writes,credentials,private data or new experiments. Date scope2021-01-01..2026-11-25;use supplied versions without asserting inaccessible publisher equivalence. Missing evidence must be reported rather than invented. Gemini primary;quota-only identical brief fallback gpt-5.6-luna/low;no model/effort escalation.
