# LibreTorrent batch 108 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 108. Source checked: already-fetched local copies in ~/workspace/b107-108-src/; no connector fetch needed, no 429. No Phase-1 label-change revision note was found in this file, so samples only.
- Rows checked (8): samples 1, 6, 11, 16, 21, 26, 31, 36.
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | SessionLogFilterDialog.onResume | REACHABLE INFERRED | PASS | Body SessionLogFilterDialog.java:69-86 (back-key listener :74); shown by LogActivity.java:254-255 (newInstance :254, show :255 in showFilterDialog); DialogFragment lifecycle dispatch, not printed. |
| 6 | MainActivity.getCurrentDetailFragment | REACHABLE SOURCE | PASS | MainActivity.java:450 (subscribeMsgViewModel torrents-deleted handler); def :687-695. |
| 11 | MainActivity.lambda$initDrawer$0 | REACHABLE INFERRED | PASS | Registered MainActivity.java:233 setOnGroupCollapseListener; body :234-235 saveGroupExpandState(groupPosition, false); library listener dispatch, not printed. |
| 16 | MainActivity.lambda$setInitSelection$11 | REACHABLE INFERRED | PASS | Filter MainActivity.java:515-516 in setInitSelection's Observable chain (`item instanceof TagItem && info.id == selectedTagId`); Rx dispatch, not printed. |
| 21 | MainActivity.lambda$subscribeNeedStartEngine$7 | REACHABLE INFERRED | PASS | Filter MainActivity.java:466 `.filter((needStart) -> needStart)` in subscribeNeedStartEngine :463-468; Rx dispatch, not printed. |
| 26 | MainActivity.onCreateOptionsMenu | REACHABLE INFERRED | PASS | Body MainActivity.java:698-705 (inflateMenu, initSearch :701, setOnMenuItemClickListener :702); framework menu lifecycle dispatch, not printed. |
| 31 | MainActivity.onOptionsItemSelected | REACHABLE INFERRED | PASS | Registered MainActivity.java:702 `setOnMenuItemClickListener(this::onOptionsItemSelected)`; body :738-759 (log branch :754-755 → showLog()); menu dispatch, not printed. |
| 36 | MainActivity.saveGroupExpandState | REACHABLE SOURCE | PASS | MainActivity.java:235 and :239 (drawer collapse/expand listeners); def :559-580. |

## Totals

- PASS: 8 / FAIL: 0 (of 8 checked).
- Proposed corrections: none.
