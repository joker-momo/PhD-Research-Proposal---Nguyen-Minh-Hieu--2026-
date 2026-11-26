# Core Database Access Readiness

**Recorded at:** 2026-11-26T13:03:38+07:00
**Scope:** G-04/S-01 preparation only
**Status:** `USER_CONFIRMED_4_OF_4; OFFICIAL_LOGIN_EXPORT_NOT_YET_VERIFIED`

The user confirmed that institutional access is available for all four planned core databases. This is an entitlement/readiness statement, not evidence that a final search has been executed.

| Core source | User-confirmed access | Previous project evidence | Official login/search route verified for final run | Export verified | Search completion |
|---|---:|---|---:|---:|---|
| IEEE Xplore | yes | Public attempt recorded HTTP 420 before results | pending | pending | `UNEXECUTED` |
| ACM Digital Library | yes | Public attempt encountered Cloudflare verification | pending | pending | `UNEXECUTED` |
| Scopus | yes | Prior log marked institutional access pending | pending | pending | `UNEXECUTED` |
| Web of Science Core Collection | yes | Prior log marked institutional access pending | pending | pending | `UNEXECUTED` |

## Gate before S-02–S-05

For each source, the user/Codex session must open the official institutional route, confirm the correct collection, verify that an export control is available and record the permitted export format/cap. A source becomes `ACCESS_ROUTE_VERIFIED` only after those four facts are observed. It becomes `SEARCH_COMPLETE` only after the exact final query, filters, local timestamp, reported total, exported total, immutable raw file, checksum and limitation are recorded.

If a confirmed entitlement cannot be used during execution, record the actual failure. Do not infer a result count. A source-set replacement or omission requires a prospective protocol amendment before the source is changed.
