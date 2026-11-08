# LibreTorrent batch 109 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 109. Source checked: already-fetched local copies in ~/workspace/b109-110-src/; no connector fetch needed, no 429. No Phase-1 label-change revision note was found in this file, so samples only.
- Rows checked (8): samples 1, 6, 11, 16, 21, 26, 31, 36.
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided. Launcher trunk (Manifest MAIN/LAUNCHER → MainActivity → MainFragment) is as filed and was not re-derived here beyond the sampled rows.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | MainActivity.showBlankFragment | REACHABLE SOURCE | PASS | MainActivity.java:192 in initLayout (also :444, :452); def :676. |
| 6 | MainActivity.subscribeNeedStartEngine | REACHABLE SOURCE | PASS | MainActivity.java:387 in onStart; def :463. |
| 11 | MainActivity$1.onNotificationResult | REACHABLE INFERRED | PASS | Callback method MainActivity.java:167 in the PermissionManager.Callback anonymous class constructed :153; PermissionManager dispatch, not printed. |
| 16 | MainActivity$3.lambda$onTagMenuClicked$0 | REACHABLE INFERRED | PASS | Success lambda of the deleteTag subscribe inside onTagMenuClicked, MainActivity.java:326-345 (success branch captures local `item`, TagItem, matching the (TagItem)V descriptor); Rx dispatch, not printed. |
| 21 | MainActivity$4.onQueryTextChange | REACHABLE INFERRED | PASS | Listener method MainActivity.java:725 (`viewModel.setSearchQuery`); registered via setOnQueryTextListener :714; SearchView dispatch, not printed. |
| 26 | MainFragment.createTorrentDialog | REACHABLE SOURCE | PASS | MainFragment.java:423 in the FAB listener branch (main_fab_create_torrent); def :561 (starts CreateTorrentActivity). |
| 31 | MainFragment.getAllTorrentsSingle | REACHABLE SOURCE | PASS | MainFragment.java:330 subscribe lambda in subscribeForceSortAndFilter; def :333. |
| 36 | MainFragment.lambda$forceAnnounceTorrents$16 | REACHABLE INFERRED | PASS | Map lambda in forceAnnounceTorrents, MainFragment.java:613-615 (`selection -> selection.torrentId`); def of enclosing method :608; Rx map dispatch, not printed. |

## Totals

- PASS: 8 / FAIL: 0 (of 8 checked).
- Proposed corrections: none.
