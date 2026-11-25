## TASK

Correct C03 domain9 analytical-evidence appraisal and identity,plus supply a direct C07 method locator,after rejected task01a21268-bab5-74de-9d97-ba4eb27fef96.

## REQUIRED WORK

1. Read /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/corpus_expansion/domain9_reaudit_batch3_notes.json and domain9_reaudit_batch3_review.md. Read the actual C03/C07 source texts at /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/sources/extracted_text_for_review/new6/C03.txt and C07.txt and identities in interim_26report/eligibility_reaudit.csv after project onboarding.
2. For C03 copy full supplied identity exactly:title,Artem Kasianchuk and Halyna Lastivka,year2026,venue as supplied,DOI10.23939/ictee2026.02.144. If source spelling differs,document alias rather than silently substitute.
3. Apply literal domain9 "Code, data, traces, or sufficient implementation details are available." to what C03 ACTUALLY DID:an analytical numerical calculation. Check if its equations,inputs,units and evaluation procedures suffice to independently reconstruct the reported calculation. Do not downgrade merely for lacking a future NS-3/OMNeT++ experiment that was not part of its current results. If partial/no is justified,name the specific missing component needed for the reported calculation with a source locator;otherwise yes can be supported without public code. Missing physical/packet validation belongs to other domains and must remain a limitation.
4. For C07 preserve copied identity and q9 partial if supported;add one original algorithm/implementation locator and retain at least one evaluation locator. Do not claim publisher-version equivalence or repository replay.
5. Return exactly2 records C03/C07 with at least2 body locators each,explicit study_specific_artifact_located and unresolved items. Change no other domain or eligibility.

## REQUIRED OUTPUT

One JSON object with records:[{study_id,title,authors:[...],year,venue,doi,identity_locator,source_file,evidence:[{locator,observation}],q9_verdict,q9_rationale,study_specific_artifact_located,unresolved_items:[]}],summary:{requested:2,returned:2,duplicates:0,files_written:0},corrections:[{criterion,correction,source_locator}].

## ACCEPTANCE CRITERIA

U1: Exactly2 records C03/C07,identities matching supplied table including full authors and venue;normalized duplicates0;all absolute paths exist.
U2: Each has at least2 in-range body locators;C07 explicitly includes algorithm/implementation and evaluation evidence.
U3: C03 rationale judges the actual analytical calculation. A partial/no must identify a reconstruction-critical missing component,not only absent code or prospective validation. Public-code availability is a separate field.
U4: Every factual claim has exact supplied-source locator;unsupported quantities0;unresolved arrays present;0 changed other-domain/eligibility;one JSON object;worker writes0.

## BOUNDARIES

Read-only evidence correction/classification only;no final prose,publication tables,project/scratch writes,downloads,credentials,private data or invented evidence. Gemini primary;recognized quota only authorizes identical brief on gpt-5.6-luna/low;no escalation.
