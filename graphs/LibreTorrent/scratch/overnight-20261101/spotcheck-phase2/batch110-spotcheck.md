# LibreTorrent batch 110 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 110. Source checked: already-fetched local copies in ~/workspace/b109-110-src/; no connector fetch needed, no 429. No Phase-1 label-change revision note was found in this file, so samples only.
- Rows checked (8): samples 1, 6, 11, 16, 21, 26, 31, 36.
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided. Lambda numbering is source-order inferred, not bytecode-verified; labels are unaffected by a swap within a group.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | MainFragment.lambda$getAllTorrentsSingle$7 | REACHABLE INFERRED | PASS | Error consumer of the getAllTorrentsSingle subscribe, MainFragment.java:333-348; Rx error dispatch, not printed. |
| 6 | MainFragment.lambda$showAddTorrentMenu$0 | REACHABLE INFERRED | PASS | `v.post(...)` lambda in showAddTorrentMenu, MainFragment.java:216-220 (register/open/unregister context menu); captured `v` matches the (View) descriptor; View-posting dispatch, not printed. |
| 11 | MainFragment.lambda$subscribeTorrentsDeleted$8 | REACHABLE INFERRED | PASS | Filter lambda in subscribeTorrentsDeleted, MainFragment.java:352-362 (opened-item id match); Rx dispatch, not printed. |
| 16 | MainFragment.onCreateContextMenu | REACHABLE INFERRED | PASS | Framework callback MainFragment.java:393-398 (inflates R.menu.main_context); framework dispatch, not printed. |
| 21 | MainFragment.onSaveInstanceState | REACHABLE INFERRED | PASS | Lifecycle method MainFragment.java:271-278 (saves torrentListState + selection); framework dispatch, not printed. |
| 26 | MainFragment.openFileErrorDialog | REACHABLE SOURCE | PASS | Called in the lambda$new$18 body, MainFragment.java:628 (non-OK / null-data path, :619-637); def :541. |
| 31 | MainFragment.subscribeAdapter | REACHABLE SOURCE | PASS | MainFragment.java:237 in onStart; def :280 (calls observeTorrents). |
| 36 | MainFragment$1.<init> | REACHABLE SOURCE | PASS | `new DefaultItemAnimator() {...}` in onViewCreated, MainFragment.java:142-147; animator set via setItemAnimator :150. |

## Totals

- PASS: 8 / FAIL: 0 (of 8 checked).
- Proposed corrections: none.
