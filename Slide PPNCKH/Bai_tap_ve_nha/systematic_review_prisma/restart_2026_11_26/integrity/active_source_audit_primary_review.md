# Step 16 native source audit, primary response

Native task `78bde50a-7fb8-46d6-822f-9cd3cb26147f`. Bridge result saved before the matching chat was deleted. The bridge verified a new blank chat after deletion. Provider status became complete at 2026-11-27T15:19:08+07:00.

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Schema, identities and DOI keys | PASS | 47 parseable reference rows, one summary and standalone marker. There are 46 expected DOIs, one R0113 DOI_NOT_FOUND marker, zero duplicate IDs and zero missing rows. |
| First-party identity coverage | FAIL | Six rows have matching identity and scoped publisher or institutional evidence. R0001 relies on an author profile for article identity. 37 identities are unresolved and three are reported as mismatches. |
| Notice evidence | FAIL | 40 source-notice rows are unresolved, principally because native browsing could not open Crossref registry endpoints. Six accepted-for-correction-exclusion rows are supported by named first-party sources and the independent checks. R0058 has a scoped provider notice check and still requires identity correction. |
| Unknowns and mechanics | PASS | Unresolved items have row-level explanations and are present in the summary. No notice URLs were asserted as confirmed formal notices. |
| Adoption | FAIL | Quarantine the primary payload as a decision source. Link a correction for its 41 incomplete rows and verify the resulting composite before adoption. |
| Transport and cleanup | PASS | The raw payload includes the exact UUID, one artifact, source markers and verified deletion of the matching completed chat. |

The six rows outside the correction are R0059, R0063, R0073, R0074, R0113 and prisma2020. The independent check corroborates their bibliographic identities and source-bounded notice dispositions. For the 41 correction rows, supply first-party snapshots with exact DOI records, per-DOI reverse checks and the matched Retraction Watch scope. The original and registry checkpoints resolve R0006 article-level pagination, R0009 deposited name segmentation and R0058 online versus issue dating.
