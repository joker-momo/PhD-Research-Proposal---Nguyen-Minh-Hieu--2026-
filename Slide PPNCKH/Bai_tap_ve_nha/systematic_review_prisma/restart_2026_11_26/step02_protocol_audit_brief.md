# TASK
Audit the internal consistency and operational completeness of restart protocol draft1.0 against the user-approved16-step plan, using only the supplied files. Return structured findings, not manuscript prose. This is step02; do not execute query audit, searching, record screening or later steps.

# REQUIRED WORK
1. Read approved_plan.md, protocol_restart.md and step01_inventory.md in the attached isolated context copy.
2. Check exactly12 topics: T01 scope/RQ mapping; T02 multi-UAV/inference eligibility; T03 date/version rules; T04 source/WoS boundaries; T05 metadata/dedup/provenance; T06 title-abstract and retrieval; T07 full-text decisions/reasons; T08 AI/human roles; T09 report-study linkage; T10 extraction; T11 appraisal; T12 synthesis/writing/sequence/integrity.
3. For every topic identify exact supporting or conflicting text with supplied filename, section and a short exact quote. Check operational ambiguities including preprints/short reports, search-date cutoff, missing abstract versus notretrieved, and uncertain family independence. Separate a policy choice from a requirement actually stated in the approvedplan.
4. Return all material inconsistencies found, or explicit noissue for each topic. A finding must link both documents if it claims a conflict. Recommend only atomic field/rule corrections, not polished replacement prose. If a decision needs userapproval, mark it; do not decide it yourself.
5. Do not invent external facts. This bounded consistency audit requires no scholarly discovery; scholarly_records must be empty and not-applicable reason supplied. State unresolved items explicitly.

# REQUIRED OUTPUT
One valid JSON object, without markdown fences:
{"task_id":"restart-02-protocol-audit","checks":[{"id":"T01","status":"CONSISTENT|ISSUE|UNRESOLVED","locators":[{"file":"protocol_restart.md","section":"P01","quote":"exact excerpt"}],"finding":"bounded observation","required_correction":null,"requires_user_approval":false}],"unresolved_items":[],"scholarly_records":[],"scholarly_records_not_applicable":"No scholarly discovery requested; supplied-file protocol consistency audit only","actions_taken":{"external_searches":0,"records_screened":0,"project_files_changed":0,"final_prose_written":false}}
Exactly12 checks T01–T12 once each. Keep findings concise and factual; do not put narrative before/after JSON. Use exact locators and quotes rather than URLs for supplied evidence.

# ACCEPTANCE CRITERIA
C1: Valid JSON; checks has exactly12 unique IDs T01–T12; no omitted topic.
C2: Every check has all schemafields and at least1 existing supplied-file section+verbatim quote; every claimed cross-document conflict has locators to both documents.
C3: Every ISSUE has a concrete nonempty required_correction; every UNRESOLVED also appears in unresolved_items; CONSISTENT has null correction.
C4: All12 findings are supported by their supplied-file locators; unsupported factual/quantitative claims=0. No external PRISMA/journal rule is invented as an approvedplan requirement.
C5: Old46 labels/extraction/candidatepool imported=0; fixedincludedtarget=0; WoS remains notsearched/null; only four approved discovery sources.
C6: No actual search, screening, metadata enrichment, project-file edits or finalprose writing; actions_taken exactly reflects zero/false.
C7: All unresolved methodological conflicts explicit; any recommended approvedscope/sequence change has requires_user_approval=true; no silently adopted change.
C8: Scholarly records=0 with explicit N/A reason, as no discovery is requested. Thus title/authors/year/venue/DOI schema is inapplicable to this audit; do not fabricate records to satisfy it. DuplicatecheckIDs=0.
C9: Return only research audit notes/structured evidence; source context unchanged. Codex independently checks all criteria and bridgecontext hashes before adoption.

# BOUNDARIES
Use only the three attached context files, read-only. No browser/network research needed. Do not access liveHK261, other folders, secrets, credentials or private messages. Do not edit context/project files, draft manuscript text, execute searches, screen records, alter PRISMA counts, resuscitate old46 decisions or invoke another backend. This task cannot authorize deviation from the user's approvedplan. Missing evidence must be stated, never guessed.
