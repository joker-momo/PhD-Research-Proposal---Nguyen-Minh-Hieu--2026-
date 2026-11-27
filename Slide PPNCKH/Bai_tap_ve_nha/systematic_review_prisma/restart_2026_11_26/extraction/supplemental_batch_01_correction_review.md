# Supplemental P08 batch 01 correction review

Native Task `f80b8621-d974-443f-9f92-5e29c0dd7895`, original correction retrieved by UUID. The bridge reported completion and verified that its chat was deleted. Source checks use the seven manifest-pinned original PDFs. Extraction acceptance remains open.

| Criterion | Verdict | Evidence |
|---|---|---|
| Scope, field schema and declared output | PASS | 47/47 unique keys: 46 fields and the R0058 access row. Zero missing, duplicate, extra or unparseable rows. One summary and the expected last-line marker. |
| Original PDF access and identity | PASS | 7/7 SHA-256 values match. The R0058 access excerpt matches physical p. 19 (§6.1), clearing the earlier access excerpt failure. |
| Original page and exact excerpt | FAIL | 45/48 non-null locators match on the stated physical page after PDF text normalization. The other two locators mark inspected absence and still require semantic review. Three quoted locators fail, at the keys below. |
| Evidence gaps, scope and numerical content | FAIL | The response reports no unresolved keys despite three failed locators. It adds no separate quantity rows. The original and corrected field findings still need semantic comparison against the PDF before using them, including estimates embedded in qualitative fields. |
| Native task, read-only workflow and recovery | PASS | One saved UUID, completed output retrieved from that UUID. Parent reports no workers. Native cleanup receipt records verified deletion. |

## Failed locator keys

| Report and key | Reported physical locator | What the original check found |
|---|---|---|
| R0014 evaluation | p. 11, §VIII.A | The quoted Jetson wording matches p. 10; the setup paragraph continues on p. 11. Use separate exact phrases from the two physical pages to support the evaluation settings. |
| R0058 architecture | p. 5, §3.1 | The supplied phrase did not match p. 5 or any other extracted physical page. Obtain a matching phrase for the node roles and separately support the decentralized coordination claim if retained. |
| R0058 mobility_continuity | p. 10, §4.1 | The supplied retry phrase did not match any extracted physical page. Verify the retry, buffering, fallback and speed claims independently or narrow the field to supported scope. |

The [raw payload](supplemental_batch_01_correction_raw.json) and [mechanical output](supplemental_batch_01_correction_mechanical.json) preserve all keys and checks. The 44 keys without automated failures have not yet been accepted. The next source review can evaluate those 44 keys in bounded groups and finalize a targeted correction scope. No P08 reports are locked by this checkpoint.
