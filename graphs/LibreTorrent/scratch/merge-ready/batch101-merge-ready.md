# LibreTorrent batch 101 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's files.**
**Build: not run. C1: not run. Sampler: not run. Full-repo grep: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No connector `search_code` result was used anywhere in this file, and no `search_code` 0 was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 101 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Membership: exactly the 40 rows for batch 101 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (plan git blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order. Method names/descriptors checked row-for-row against that plan copy in this pass.
- Prior work used as INPUT only: `~/workspace/libretorrent-batch101-proposal.md` (36 REACHABLE proposed / 0 UNREACHABLE / 4 OPEN). Every row below was re-judged in this pass; the 4 OPEN rows are upgraded below on newly printed callers, not copied.
- Fresh connector fetches in this pass, one file at a time with ~25 s pauses, branch `work-2026-10-31`, saved in `~/workspace/b101102-src/` (no fresh HTTP 429 hit): `ui/feeds/FeedFragment.java` (519 lines), `ui/feeds/FeedViewModel.java` (172 lines), `ui/feeds/MsgFeedViewModel.java` (64 lines), `ui/feeds/FeedActivity.java` (412 lines), `ui/filemanager/FileManagerAdapter.java` (176 lines). All fresh line numbers match the earlier local copies for the same files, which raises confidence in the corpus but does not replace the merger's spot-check.
- True git clone: MISSING check, never passed — a true git clone fails in this VM (no credential device); all work here is via the GitHub connector on branch `work-2026-10-31`, not a local git checkout.
- confirmed_by convention in this file (per-row, NOT decided): SOURCE = a printed direct app-code call site naming the method (including an in-app method-reference subscription and a `provider.get()` instantiation site); INFERRED = the method runs only through unprinted framework/library dispatch (RecyclerView, SelectionTracker, ActionMode, ViewModel lifecycle, RxJava, JVM class initialisation) where definition and registration are printed. Under a whole-route INFERRED convention, SOURCE rows crossing unprinted dispatch would read INFERRED; labels are unaffected.
- Strict-entry caveat: routes anchor at FeedFragment lifecycle / FeedActivity / FileManagerDialog, not at a printed launcher step. The step that attaches FeedFragment to its host activity was NOT printed in this pass (FeedActivity's printed code manages FeedItemsFragment/blank in its container, not FeedFragment). Under a strict launcher-entry rule all REACHABLE rows revert to OPEN. The merger must pick one strict-entry convention for all batches; it is NOT decided here.
- Lambda / anonymous numbering: $ numbers are source-order / plan-signature matches from the input proposal and fresh source, NOT bytecode-verified; a swap within a group would not change any label.
- Why no UNREACHABLE here: every row now has a printed caller or a printed enclosing REACHABLE method. No row is proposed UNREACHABLE, and no OPEN row remains, so no full-repo grep is needed to close this batch — but a saved full-repo grep would still be the merger's check that no additional caller contradicts a row (none is claimed here).

## Table

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 1 | `FeedFragment.subscribeAlertDialog ()V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:209 `subscribeAlertDialog()` in onStart; body :310-332 subscribes dialogViewModel.observeEvents(). |
| 2 | `FeedFragment.subscribeMsgViewModel ()V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:210 in onStart; body :286-309 subscribes msgViewModel observables. |
| 3 | `FeedFragment.subscribeRefreshStatus ()V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:211 in onStart; body :333-337 subscribes viewModel.observeRefreshStatus(). |
| 4 | `FeedFragment$1.<init> (FeedFragment)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:122 `new DefaultItemAnimator() {` in onViewCreated; animator set at :130. |
| 5 | `FeedFragment$1.canReuseUpdatedViewHolder (ViewHolder)Z` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:124-126 returns true; invoked by RecyclerView when it runs the animator set at :130. Framework dispatch, not printed from fw_src. |
| 6 | `FeedFragment$2.<init> (FeedFragment)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:146 `selectionTracker.addObserver(new SelectionTracker.SelectionObserver<FeedChannelItem>() {`. |
| 7 | `FeedFragment$2.onSelectionChanged ()V` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:148-169; invoked by SelectionTracker on selection change; starts ActionMode at :153. Framework dispatch, not printed from fw_src. |
| 8 | `FeedFragment$2.onSelectionRestored ()V` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:172-178; invoked by SelectionTracker on restore (after onRestoreInstanceState :182). Framework dispatch. |
| 9 | `FeedFragment$3.<init> (FeedFragment)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:353 anonymous `new ActionMode.Callback()` field initialiser. |
| 10 | `FeedFragment$3.onActionItemClicked (ActionMode,MenuItem)Z` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:380-404; invoked by the framework ActionMode started at :153/:176 via startSupportActionMode(actionModeCallback). |
| 11 | `FeedFragment$3.onCreateActionMode (ActionMode,Menu)Z` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:371-378; same ActionMode framework dispatch as row 10. |
| 12 | `FeedFragment$3.onDestroyActionMode (ActionMode)V` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:405-409; same ActionMode framework dispatch as row 10. |
| 13 | `FeedFragment$3.onPrepareActionMode (ActionMode,Menu)Z` | REACHABLE | INFERRED | FRESH: body FeedFragment.java:356-369; same ActionMode framework dispatch as row 10. |
| 14 | `FeedViewModel.<init> (Application)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:112 `provider.get(FeedViewModel.class)`; constructor body FeedViewModel.java:60-65 (RepositoryHelper.getFeedRepository). Framework instantiation via the printed get() call. |
| 15 | `FeedViewModel.copyFeedUrlToClipboard (FeedChannel)Z` | REACHABLE | SOURCE | FRESH: FeedFragment.java:473 `viewModel.copyFeedUrlToClipboard(it.next())`; body FeedViewModel.java:92-103. |
| 16 | `FeedViewModel.deleteFeeds (List)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:452 method reference `.doOnSuccess(viewModel::deleteFeeds)`; body FeedViewModel.java:85-90. |
| 17 | `FeedViewModel.getAllFeedsSingle ()Single` | REACHABLE | SOURCE | FRESH: FeedFragment.java:273 `viewModel.getAllFeedsSingle()`; body FeedViewModel.java:75-78. |
| 18 | `FeedViewModel.lambda$deleteFeeds$0 (List)V` | REACHABLE | INFERRED | FRESH: Runnable `() -> repo.deleteFeeds(feeds)` at FeedViewModel.java:87 inside Completable.fromRunnable, subscribed :87-89 on Schedulers.io(). RxJava thread/dispatch not printed. |
| 19 | `FeedViewModel.lambda$markAsReadFeeds$1 (List)V` | REACHABLE | INFERRED | FRESH: Runnable `() -> repo.markAsReadByFeedId(feedIdList)` at FeedViewModel.java:149 inside Completable.fromRunnable, subscribed :149-150 on Schedulers.io(). RxJava dispatch not printed. |
| 20 | `FeedViewModel.markAsReadFeeds (List)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:517 `.subscribe(viewModel::markAsReadFeeds)`; body FeedViewModel.java:147-151. |
| 21 | `FeedViewModel.observeRefreshStatus ()Observable` | REACHABLE | SOURCE | FRESH: FeedFragment.java:335 `viewModel.observeRefreshStatus()`; body FeedViewModel.java:130-133 returns refreshStatus subject. |
| 22 | `FeedViewModel.observeWorkResult (WorkInfo)V` | REACHABLE | SOURCE | FRESH: method reference registered FeedViewModel.java:160 `observeForever(this::observeWorkResult)` in runFetchWorker; removed :167-168; body :163-171. |
| 23 | `FeedViewModel.observerAllFeeds ()Flowable` | REACHABLE | SOURCE | FRESH: FeedFragment.java:258 `viewModel.observerAllFeeds()`; body FeedViewModel.java:80-83. |
| 24 | `FeedViewModel.onCleared ()V` | REACHABLE | INFERRED | FRESH: body FeedViewModel.java:68-73 (disposables.clear()); invoked by the ViewModel framework when the provider is cleared. Lifecycle dispatch not printed from fw_src. |
| 25 | `FeedViewModel.refreshAllFeeds ()V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:185 swipe-refresh listener `() -> viewModel.refreshAllFeeds()`; body FeedViewModel.java:118-128 builds ACTION_FETCH_ALL_CHANNELS work and calls runFetchWorker :127. |
| 26 | `FeedViewModel.refreshFeeds ([J)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:491 `viewModel.refreshFeeds(ids)`; body FeedViewModel.java:105-116 builds ACTION_FETCH_CHANNEL_LIST work and calls runFetchWorker :115. |
| 27 | `FeedViewModel.restoreFeedsSync (Uri)[J` | REACHABLE | SOURCE | UPGRADED in this pass (was OPEN in input proposal): FRESH: FeedActivity.java:361 `viewModel.restoreFeedsSync(file)` inside restoreFeedsBackup :359-370, reached via the restoreFeedsBackupChoose ActivityResultLauncher :389-401 (result data -> restoreFeedsBackup :401); definition FeedViewModel.java:140-145. This closes the input proposal's stated missing evidence (an import/restore caller). |
| 28 | `FeedViewModel.runFetchWorker (WorkRequest)V` | REACHABLE | SOURCE | FRESH: called FeedViewModel.java:115 (refreshFeeds) and :127 (refreshAllFeeds); body :153-161 enqueues WorkManager work and observes its LiveData. |
| 29 | `FeedViewModel.saveFeedsSync (Uri)V` | REACHABLE | SOURCE | UPGRADED in this pass (was OPEN in input proposal): FRESH: FeedActivity.java:349 `viewModel.saveFeedsSync(file)` inside backupFeeds :346-357, reached via the backupFeedsChoose ActivityResultLauncher :373-385 (result data -> backupFeeds :385); definition FeedViewModel.java:135-139. This closes the input proposal's stated missing evidence (an export/backup caller). |
| 30 | `MsgFeedViewModel.<init> ()V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:113 `provider.get(MsgFeedViewModel.class)`; class has only the implicit no-arg constructor (MsgFeedViewModel.java:29-64, no explicit constructor). |
| 31 | `MsgFeedViewModel.feedItemsClosed ()V` | REACHABLE | SOURCE | UPGRADED in this pass (was OPEN in input proposal): FRESH: FeedActivity.java:410 `msgViewModel.feedItemsClosed()` inside onFragmentFinished :406-411 (two-pane case, finished fragment is FeedItemsFragment); definition MsgFeedViewModel.java:45-47. This closes the input proposal's stated missing evidence (a FeedItems-side lifecycle caller); the caller file is FeedActivity, not a separate FeedItemsFragment file. |
| 32 | `MsgFeedViewModel.feedItemsOpened (J)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:345 `msgViewModel.feedItemsOpened(item.id)` in onItemClicked; body MsgFeedViewModel.java:35-38. |
| 33 | `MsgFeedViewModel.feedsDeleted (List)V` | REACHABLE | SOURCE | FRESH: FeedFragment.java:458 `.subscribe(msgViewModel::feedsDeleted)`; body MsgFeedViewModel.java:55-58. |
| 34 | `MsgFeedViewModel.observeFeedItemsClosed ()Observable` | REACHABLE | SOURCE | FRESH: FeedFragment.java:288 `msgViewModel.observeFeedItemsClosed()`; body MsgFeedViewModel.java:50-53. |
| 35 | `MsgFeedViewModel.observeFeedItemsOpened ()Observable` | REACHABLE | SOURCE | UPGRADED in this pass (was OPEN in input proposal): FRESH: FeedActivity.java:174 `msgViewModel.observeFeedItemsOpened()` subscribed in subscribeMsgViewModel :172-180, called from onStart :127; definition MsgFeedViewModel.java:40-42. This closes the input proposal's stated missing evidence (a FeedItems-side subscriber); the subscriber is FeedActivity's showFeedItems path (:176). |
| 36 | `MsgFeedViewModel.observeFeedsDeleted ()Observable` | REACHABLE | SOURCE | FRESH: FeedFragment.java:295 `msgViewModel.observeFeedsDeleted()`; body MsgFeedViewModel.java:60-63. |
| 37 | `FileManagerAdapter.<clinit> ()V` | REACHABLE | INFERRED | FRESH: static field initialisers FileManagerAdapter.java:57 (directoryFirstCmp lambda) and :96 (diffCallback) run at JVM class load when the adapter class is first used (constructed batch 102, FileManagerDialog.java:196). JVM class-init dispatch, not a printed call site. |
| 38 | `FileManagerAdapter.<init> (List,ClickListener)V` | REACHABLE | SOURCE | FRESH: FileManagerDialog.java:196 `adapter = new FileManagerAdapter(viewModel.config.highlightFileTypes, this)`; body FileManagerAdapter.java:64-70 (super(diffCallback)). |
| 39 | `FileManagerAdapter.lambda$static$0 (FileManagerNode,FileManagerNode)I` | REACHABLE | INFERRED | FRESH: comparator lambda FileManagerAdapter.java:57-62; used by FileManagerAdapter.java:91 `list.sort(directoryFirstCmp)` in submitList. Comparator invocation is library (sort) dispatch, not printed. |
| 40 | `FileManagerAdapter.onBindViewHolder (ViewHolder,int)V` | REACHABLE | INFERRED | FRESH: body FileManagerAdapter.java:82-85 calls holder.bind(...); invoked by RecyclerView when binding rows of the adapter set at FileManagerDialog.java:197 (setAdapter). Framework dispatch, not printed from fw_src. |

## Counts

- **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN** (SOURCE 27 / INFERRED 13).
- Change vs input proposal (36/0/4): rows 27, 29, 31, 35 all OPEN → REACHABLE SOURCE on fresh FeedActivity.java prints above. No other row changed label.

## Still owed before merge

- Main-agent spot-check 1 in 5, `py_compile`, build, Mac build/C1 — all not run, never claimed passed.
- Printed host-activity step that attaches FeedFragment (strict-entry rule, above).
- No saved full-repo grep is needed to close this batch (no OPEN rows remain), but the merger's spot-check should still re-print at least one caller file fresh if it requires fresh evidence for every row; all definition/caller files above are fresh in this pass except where a row's citation is explicitly internal to a fresh file.
