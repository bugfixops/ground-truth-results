# Stream A Phase 2 spot-check — 98 — UNVERIFIED spot-check, NOT a merge decision
Scope: batch 98 only, LibreTorrent labels only. Source file checked: ~/workspace/overnight/stream-A/work/batch98-merge-ready.md (UNVERIFIED proposal, not a result).
Method: each row below was re-derived from printed source, searched in already-fetched local copies first (~/workspace/overnight/stream-A/corpus/, 281 app-Java files; ~/workspace/b9192-src/; ~/workspace/b90929495969799102-openclose-src/; ~/workspace/overnight/stream-A/greps/). No merge-ready file was edited, no tick written, no push made. Build/sampler/C1: not run (not this task).
Verdict rule used: PASS = the row's label is correct and its controlling evidence (including any dated 2026-11-01 revision note in the file, which supersedes older row text) locates the route. FAIL = the label is wrong, or the stated evidence mislocates the route (wrong caller/branch) with no superseding note. Two things are NOT failed: (a) confirmed_by SOURCE vs INFERRED on lifecycle/framework rows — both are permitted values and the classification convention is not decided here; (b) lambda/anonymous $ numbering, which the work files themselves state is source-order, NOT bytecode-verified, and a swap within a group would not change any label. Off-by-one definition spans are noted as corrections, not failures. A row turning on an undecided project convention is left as-is and flagged, never decided here.
No fresh 429 occurred in this pass (4 connector fetches, batch 99 only, one at a time with ~30 s pauses; no token used).

Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. No Phase-1 label change is listed in this file's dated 2026-11-01 notes, so no extra rows apply.

- Row 1 FeedItemsFragment.setFeedId — PASS (REACHABLE, SOURCE). Called from newInstance :83 and from FeedItemsActivity :58; body :94-97.
- Row 6 FeedItemsListItem.equalsContent — PASS (REACHABLE, INFERRED). Called from FeedItemsAdapter$1.areContentsTheSame :111; body :56-74; DiffUtil dispatch INFERRED.
- Row 11 FeedItemsViewModel.lambda$markAsRead$1 — PASS (REACHABLE, INFERRED). Completable.fromRunnable lambda :124 (repo.markAsRead(itemId)) inside markAsRead; Rx dispatch INFERRED.
- Row 16 FeedItemsViewModel.observeItemsByFeedId — PASS (REACHABLE, SOURCE). Called from FeedItemsFragment :210; body :82-85 (repo.observeItemsByFeedId).
- Row 21 FeedItemsViewModel.runFetchWorker — PASS (REACHABLE, SOURCE). Called from refreshChannel :110; body :136-144 (refreshStatus.onNext :138, WorkManager enqueue :140, observeForever :142-143). WorkManager dispatch to FeedFetcherWorker is INFERRED elsewhere (batch 71) and is not part of this row.
- Row 26 FeedActivity.backupFeedsChooseDialog — PASS (REACHABLE, SOURCE). Called from onOptionsItemSelected backup menu :254; body :262-276 (FileManagerDialog intent :264-275, backupFeedsChoose.launch :275).
- Row 31 FeedActivity.lambda$backupFeeds$5 — PASS (REACHABLE, INFERRED). Subscribe success lambda :353-356 (Toast "backup_feeds_successfully"); Rx dispatch INFERRED.
- Row 36 FeedActivity.lambda$restoreFeedsBackup$7 — PASS (REACHABLE, INFERRED). Subscribe success lambda :364-370 (Toast, viewModel.refreshFeeds :369); Rx dispatch INFERRED.

Totals: 8 rows checked — 8 PASS, 0 FAIL.
Proposed corrections: none.
