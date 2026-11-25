# Batch 04 result review

Date: 25 November 2026

Primary task ID: `01a21367-17e7-767c-b5cb-b595ef2ccb56`

Context ID: `01a21367-17e8-732c-bc2a-905c28d3b471`

Provider result status: completed transport, **unaccepted research evidence**.

## Acceptance gate

| Criterion | Verdict | Objective evidence |
|---|---|---|
| A1 exact record set | PASS | 6/6 unique records in the required set: S19, S20, C01, C02, C03, C04; shortfall array empty; silent omissions 0 |
| A2 identity/schema/duplicates | FAIL | DOI/title duplicates 0, duplicated author names 0, and all six identity blocks are present, but `primary_reason` is empty for 6/6 records; current mechanical schema therefore reports six A2 errors |
| A3 six gates and literal evidence | FAIL | Exactly 6 gates per report and 48 evidence blocks were returned; 44/48 page/quote checks match. Four fail: S19 `date_window` p.1, S20 `date_window` p.1, C01 `multi_uav_evaluated` p.21, C03 `multi_uav_evaluated` p.7 |
| A4 decision logic | PASS | Mechanical checker reports no decision-logic error: 3 UNCERTAIN and 3 INCLUDE agree with the returned gate states; excluded-record count is 0 |
| A5 located alignment/evaluation and forbidden claims | PASS | Alignment and evaluative-evidence locators match for 6/6 reports; physical multi-UAV flight classifications 0; percentage-improvement extraction 0; unsupported physical-flight claims 0 |
| A6 uncertainty/date/mutation boundary | PASS | All 6 records contain nonempty unresolved arrays; S19, S20, and C03 remain UNCERTAIN on date; other included dates fall within 2021–2026; `project_files_changed=0` |

Overall verdict: **REJECTED_A2_A3**. The three proposed INCLUDE decisions and
three UNCERTAIN decisions remain quarantined and must not enter the accepted
working corpus, synthesis, PRISMA counts, or manuscript.

## Required correction

1. Return a nonempty, factual `primary_reason` for all six records. For INCLUDE,
   state that all six gates are YES; for UNCERTAIN, name the unresolved gate.
2. Replace each of the four failed page/quote locators with an exact contiguous
   10–45 word quote from the supplied page, or correct the page/status when the
   supplied report does not support the claim.
3. Reassess the semantics of C01 and C03 `multi_uav_evaluated`; a device-only or
   generic-neighbor quote is insufficient unless the cited source passage
   establishes the evaluated multi-UAV system.
4. Preserve the 44 passing locators unless source re-reading proves one wrong.
   Report every new uncertainty rather than inventing evidence.

The correction requires a separately committed brief and a new routed research
task linked to the primary task above. Codex must rerun the full mechanical and
semantic gate before accepting any Batch 04 decision.
