# LibreTorrent batch 101 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 101. Source checked: already-fetched local copies in ~/workspace/b101102-src/ (FeedFragment.java, FeedViewModel.java, FeedActivity.java, MsgFeedViewModel.java); no connector fetch needed, no 429.
- Rows checked (11): samples 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase-1-changed rows 27, 29, 35 (OPEN → REACHABLE in the merge-ready pass; row 31 is both a sample and a changed row).
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided; strict-entry caveat in the merge-ready file is noted, not re-decided.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | FeedFragment.subscribeAlertDialog | REACHABLE SOURCE | PASS | FeedFragment.java:209 `subscribeAlertDialog()` in onStart. |
| 6 | FeedFragment$2.<init> | REACHABLE SOURCE | PASS | FeedFragment.java:146 `selectionTracker.addObserver(new SelectionTracker.SelectionObserver<FeedChannelItem>() {`. |
| 11 | FeedFragment$3.onCreateActionMode | REACHABLE INFERRED | PASS | Body FeedFragment.java:371-378 (def :371); ActionMode framework dispatch, registration via the callback field (row 9). |
| 16 | FeedViewModel.deleteFeeds | REACHABLE SOURCE | PASS | FeedFragment.java:452 `.doOnSuccess(viewModel::deleteFeeds)`; def FeedViewModel.java:85-90. |
| 21 | FeedViewModel.observeRefreshStatus | REACHABLE SOURCE | PASS | FeedFragment.java:335 `viewModel.observeRefreshStatus()`; def FeedViewModel.java:130-133. |
| 26 | FeedViewModel.refreshFeeds | REACHABLE SOURCE | PASS | FeedFragment.java:491 `viewModel.refreshFeeds(ids)`; def FeedViewModel.java:105-116, runFetchWorker :115. |
| 27 | FeedViewModel.restoreFeedsSync | REACHABLE SOURCE | PASS | FeedActivity.java:361 `viewModel.restoreFeedsSync(file)` inside restoreFeedsBackup; launcher restoreFeedsBackupChoose :389-401 calls restoreFeedsBackup :401; def FeedViewModel.java:140-145. |
| 29 | FeedViewModel.saveFeedsSync | REACHABLE SOURCE | PASS | FeedActivity.java:349 `viewModel.saveFeedsSync(file)` inside backupFeeds :346-357; def FeedViewModel.java:135-139. |
| 31 | MsgFeedViewModel.feedItemsClosed | REACHABLE SOURCE | PASS | FeedActivity.java:410 `msgViewModel.feedItemsClosed()` inside onFragmentFinished :406-411 (FeedItemsFragment two-pane branch); def MsgFeedViewModel.java:45-47. |
| 35 | MsgFeedViewModel.observeFeedItemsOpened | REACHABLE SOURCE | PASS | FeedActivity.java:174 `msgViewModel.observeFeedItemsOpened()` subscribed in subscribeMsgViewModel :172-180, called from onStart :127; def MsgFeedViewModel.java:40-42. |
| 36 | MsgFeedViewModel.observeFeedsDeleted | REACHABLE SOURCE | PASS | FeedFragment.java:295 `msgViewModel.observeFeedsDeleted()`; def MsgFeedViewModel.java:60-63. |

## Totals

- PASS: 11 / FAIL: 0 (of 11 checked).
- Proposed corrections: none.
