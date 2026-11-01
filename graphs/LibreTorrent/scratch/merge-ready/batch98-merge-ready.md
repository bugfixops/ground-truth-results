# LibreTorrent batch 98 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready proposal only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 98 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Source task: re-derive from printed source. The prior batch-98 proposal (`~/workspace/libretorrent-batch98-proposal.md`) was used as an INPUT, not a result; membership and the table below were checked against the plan and against printed source in this pass (see Re-derivation check).

## Membership — verified first, not guessed

Exactly the 40 rows for batch 98 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE` in the plan (generator candidates, not evidence), in plan order:
FeedItemsFragment rows 1-3, FeedItemsListItem rows 4-6, FeedItemsViewModel rows 7-22, FeedActivity rows 23-40.
Method names, JVM descriptors and order were checked against the plan in this pass and match the table below row for row.

## Printed source used

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
- `ui/feeditems/FeedItemsFragment.java` — saved at `~/workspace/b9798-src/FeedItemsFragment.java` (329 lines; SHA c612894b…). Re-checked in this pass at :80-97 (newInstance/setFeedId), :159-165 (onStart), :202-210 (subscribeAdapter/observeFeedItems), :325-328 (finish).
- `ui/feeditems/FeedItemsListItem.java` — freshly connector-fetched in the prior pass, saved at `~/workspace/b9798-src/FeedItemsListItem.java` (SHA fc8b837c…). Re-checked in this pass at :28-35 (<init>), :51-54 (equals), :56-74 (equalsContent).
- `ui/feeditems/FeedItemsViewModel.java` — freshly connector-fetched in the prior pass, saved at `~/workspace/b9798-src/FeedItemsViewModel.java` (SHA d034625f…). Re-checked in this pass at :55-61 (<init>), :71-95 (clearData/setFeedId/observe*), :113-135 (markAllAsRead/markAsRead/markAsUnread and their $0/$1/$2 runnables), :136-155 (runFetchWorker/observeWorkResult).
- `ui/feeds/FeedActivity.java` — freshly connector-fetched in the prior pass, saved at `~/workspace/b9798-src/FeedActivity.java` (SHA 90d65973…, 412 lines). Re-checked in this pass at :91-107 (onCreate), :203-224 (showFeedItems trunk), :345-375 (backupFeeds/fromCallable :348-350, restoreFeedsBackup/fromCallable :361) and :389-403 (ActivityResult callbacks).
- `ui/feeditems/FeedItemsActivity.java` — freshly connector-fetched in the prior pass, saved at `~/workspace/b9798-src/FeedItemsActivity.java` (SHA 951104d8…, 67 lines); used only for the trunk (its own methods are batch-96 rows, not judged here). Re-checked at :42-60.
Line numbers below are from those files (FIF = FeedItemsFragment.java, FILI = FeedItemsListItem.java, FIVM = FeedItemsViewModel.java, FA = FeedActivity.java).

## Re-derivation check in this pass (not a copy)

- Plan membership: 40/40 rows, sequence 1-40 intact, descriptors match the plan. Counts below were mechanically verified from the table in this pass.
- Spot-checks re-read in this pass and holding: FILI <init> :28-35, equals :51-54 (super.equals), equalsContent :56-74; FIVM <init> :55-61, clearData :71-75, setFeedId :77-80, observeItemsByFeedId :82-85, getItemsByFeedIdSingle :87-90, observeRefreshStatus :92-95, markAllAsRead :113-120 with $0 runnable :118, markAsRead :122-127 with $1 runnable :124, markAsUnread :129-134 with $2 runnable :131, runFetchWorker :136-144 (enqueue :140, observeForever :142-143), observeWorkResult :146-154; FA onCreate :91-107, showFeedItems :203-224, backupFeeds fromCallable :348-350 (saveFeedsSync), restoreFeedsBackup fromCallable :361 (restoreFeedsSync), ActivityResult callbacks :389-403; FIF setFeedId :94-97, subscribeAdapter :202-206, subscribeRefreshStatus via onStart :159-165.
- No row was changed from the prior proposal in this pass and no row is OPEN: every row has a printed definition plus a printed direct caller, registration, or framework/library dispatch with registration printed (see table). Lambda $ numbering is source-order matched to plan signatures, not bytecode-verified; labels are unaffected.
- Cross-batch leads, NOT judged here and flipping nothing in this batch: FA:349 is a printed caller for `FeedViewModel.saveFeedsSync` and FA:361 for `FeedViewModel.restoreFeedsSync` (both batch 101, left OPEN there); FA:174 `observeFeedItemsOpened` and FA:410 `feedItemsClosed()` (via FeedActivity.onFragmentFinished, itself called by FIF.finish :327) are printed call sites for MsgFeedViewModel rows batch 101 left OPEN. Those rows still need their own merger re-check.

## Shared trunk / strict-entry caveat (applies to every REACHABLE row below) — UNDECIDED convention, recorded not decided

FeedItemsFragment route, printed: FA.showFeedItems :203-219 (two-pane: newInstance :207, transaction replace :215-218) and :220-224 (single-pane: Intent to FeedItemsActivity :221-223, whose onCreate finds the layout-declared fragment by id and calls setFeedId :54-58). FeedActivity route: framework activity lifecycle (onCreate FA:91-107, initLayout :102, ViewModelProvider :96-99).
**The in-app starter of FeedActivity itself was NOT printed in this pass** (same gap as batch 99, where FeedActivity is manifest-declared at AndroidManifest.xml:174 but its starter was not printed). Under a strict launcher-entry rule every REACHABLE row below reverts to OPEN until that starter is printed. Rows are proposed REACHABLE on the FeedActivity/FeedItemsActivity-anchored trunk above, the convention used by sibling detail/feed batches. The merger must pick one strict-entry convention for all batches; this file does not decide it.

## confirmed_by convention (stated so the merger can reconcile it) — UNDECIDED convention, recorded not decided

SOURCE = a direct app-code call site naming the method is printed (including a direct internal call, a method reference, and a lambda body that names it).
INFERRED = reached only through unprinted framework/library dispatch (activity/fragment lifecycle, Rx, LiveData, ActivityResult, DiffUtil, ViewModelProvider, view/menu click listeners) with the definition and registration printed.
This is the per-row convention, not the whole-route convention used in some earlier batches; labels are unaffected, only confirmed_by would change at merge if the merger adopts the whole-route convention.

## Counts — proposed, not verified (mechanically verified from the table)

- REACHABLE proposed: 40 / 40 (SOURCE 19, INFERRED 21)
- UNREACHABLE proposed: 0
- OPEN: 0 / 40
- Verified for merge: 0 / 40

No UNREACHABLE row is claimed: no saved full-repo grep was run, and connector search_code was not used as evidence of absence.

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | FeedItemsFragment.setFeedId(long)V | REACHABLE | SOURCE | FIF:83 newInstance body calls fragment.setFeedId(feedId); also FeedItemsActivity:58 feedItemsFragment.setFeedId(getIntent().getLongExtra(TAG_FEED_ID, -1)). Body FIF:94-97. |
| 2 | FeedItemsFragment.subscribeAdapter()V | REACHABLE | SOURCE | FIF:163 onStart body calls subscribeAdapter(). Body FIF:202-206 (getAllFeedItemsSingle :204, observeFeedItems :205). |
| 3 | FeedItemsFragment.subscribeRefreshStatus()V | REACHABLE | SOURCE | FIF:164 onStart body calls subscribeRefreshStatus(). Body FIF:238-243 (viewModel.observeRefreshStatus() :240, swipeContainer::setRefreshing :242). |
| 4 | FeedItemsListItem.<init>(FeedItem)V | REACHABLE | SOURCE | FIF:214 map(FeedItemsListItem::new) in observeFeedItems and FIF:229 map(FeedItemsListItem::new) in getAllFeedItemsSingle. Body FILI:28-35 (super(...) :30-31, read/fetchDate :33-34). |
| 5 | FeedItemsListItem.equals(Object)Z | REACHABLE | INFERRED | FeedItemsAdapter$1.areItemsTheSame body calls oldItem.equals(newItem) (FeedItemsAdapter.java:118, batch 97 evidence); DiffUtil dispatch to that callback on submitList is library code, not printed. Body FILI:51-54 (super.equals). Same convention as batch 113 drawer.TagItem.equals (INFERRED via DiffUtil). |
| 6 | FeedItemsListItem.equalsContent(Object)Z | REACHABLE | INFERRED | FeedItemsAdapter$1.areContentsTheSame body calls oldItem.equalsContent(newItem) (FeedItemsAdapter.java:111); DiffUtil dispatch unprinted. Body FILI:56-74. |
| 7 | FeedItemsViewModel.<init>(Application)V | REACHABLE | INFERRED | FIF:123 new ViewModelProvider(activity).get(FeedItemsViewModel.class); ViewModelProvider instantiates via this ctor, dispatch unprinted. Body FIVM:55-61 (super, repo, feedId = -1). |
| 8 | FeedItemsViewModel.clearData()V | REACHABLE | SOURCE | FIF:127 viewModel.clearData() in onViewCreated (two-pane branch). Body FIVM:71-75. |
| 9 | FeedItemsViewModel.getItemsByFeedIdSingle()Single | REACHABLE | SOURCE | FIF:225 viewModel.getItemsByFeedIdSingle() in getAllFeedItemsSingle. Body FIVM:87-90 (repo.getItemsByFeedIdSingle). |
| 10 | FeedItemsViewModel.lambda$markAllAsRead$0()V | REACHABLE | INFERRED | FIVM:118 Completable.fromRunnable lambda (repo.markAsReadByFeedId(...)) inside markAllAsRead. Rx/Completable dispatch unprinted. |
| 11 | FeedItemsViewModel.lambda$markAsRead$1(String)V | REACHABLE | INFERRED | FIVM:124 Completable.fromRunnable lambda (repo.markAsRead(itemId)) inside markAsRead. Rx dispatch unprinted. |
| 12 | FeedItemsViewModel.lambda$markAsUnread$2(String)V | REACHABLE | INFERRED | FIVM:131 Completable.fromRunnable lambda (repo.markAsUnread(itemId)) inside markAsUnread. Rx dispatch unprinted. |
| 13 | FeedItemsViewModel.markAllAsRead()V | REACHABLE | SOURCE | FIF:314 viewModel.markAllAsRead() in onOptionsItemSelected (mark-as-read menu). Body FIVM:113-120 (feedId == -1 guard :115-116, runnable :118). |
| 14 | FeedItemsViewModel.markAsRead(String)V | REACHABLE | SOURCE | FIF:257 viewModel.markAsRead(item.id) (onItemMenuClicked), FIF:273 (openArticle), FIF:290 (openDownloadUrl). Body FIVM:122-127. |
| 15 | FeedItemsViewModel.markAsUnread(String)V | REACHABLE | SOURCE | FIF:259 viewModel.markAsUnread(item.id) in onItemMenuClicked. Body FIVM:129-134. |
| 16 | FeedItemsViewModel.observeItemsByFeedId()Flowable | REACHABLE | SOURCE | FIF:210 viewModel.observeItemsByFeedId() in observeFeedItems. Body FIVM:82-85 (repo.observeItemsByFeedId). |
| 17 | FeedItemsViewModel.observeRefreshStatus()Observable | REACHABLE | SOURCE | FIF:240 viewModel.observeRefreshStatus() in subscribeRefreshStatus. Body FIVM:92-95 (returns refreshStatus subject). |
| 18 | FeedItemsViewModel.observeWorkResult(WorkInfo)V | REACHABLE | INFERRED | FIVM:143 observeForever(this::observeWorkResult) in runFetchWorker; LiveData dispatch unprinted (also referenced at :151 removeObserver). Body FIVM:146-154 (finished check, refreshStatus.onNext). |
| 19 | FeedItemsViewModel.onCleared()V | REACHABLE | INFERRED | FIVM:64-69 body (super, disposables.clear). ViewModel lifecycle dispatch unprinted; ViewModel is obtained at FIF:123. |
| 20 | FeedItemsViewModel.refreshChannel()V | REACHABLE | SOURCE | FIF:155 swipe-refresh lambda calls viewModel.refreshChannel(); FIF:312 onOptionsItemSelected calls viewModel.refreshChannel() (refresh menu). Body FIVM:97-111 (feedId == -1 guard :99-100, WorkRequest build :102-108, runFetchWorker :110). |
| 21 | FeedItemsViewModel.runFetchWorker(WorkRequest)V | REACHABLE | SOURCE | FIVM:110 refreshChannel body calls runFetchWorker(work). Body FIVM:136-144 (refreshStatus.onNext(true) :138, WorkManager enqueue :140, observeForever :142-143). WorkManager dispatch to FeedFetcherWorker is INFERRED elsewhere (batch 71), not part of this row. |
| 22 | FeedItemsViewModel.setFeedId(long)V | REACHABLE | SOURCE | FIF:128 viewModel.setFeedId(feedId) in onViewCreated. Body FIVM:77-80. |
| 23 | FeedActivity.<clinit>()V | REACHABLE | INFERRED | FA:75 TAG = FeedActivity.class.getSimpleName(), a non-constant static initialiser; runs on first use of the class. JVM dispatch unprinted. |
| 24 | FeedActivity.<init>()V | REACHABLE | INFERRED | Framework instantiates the manifest-declared activity (manifest:174 per batch 99, not re-printed here); no app-code `new FeedActivity()` exists or is needed. Activity instantiation dispatch unprinted. |
| 25 | FeedActivity.backupFeeds(Uri)V | REACHABLE | SOURCE | FA:385 backupFeeds(data.getData()) inside the backupFeedsChoose ActivityResult callback body (:375-386). Body FA:346-357 (fromCallable -> saveFeedsSync :349, success Toast :353-356, error handler :356). Cross-note (not judged here): :349 is a printed caller for FeedViewModel.saveFeedsSync, which batch 101 left OPEN. |
| 26 | FeedActivity.backupFeedsChooseDialog()V | REACHABLE | SOURCE | FA:254 onOptionsItemSelected body calls backupFeedsChooseDialog() (backup menu). Body FA:262-276 (FileManagerDialog intent :264-275, backupFeedsChoose.launch :275). |
| 27 | FeedActivity.backupFeedsErrorDialog(Throwable)V | REACHABLE | SOURCE | FA:370 restoreFeedsBackup subscribe error handler this::backupFeedsErrorDialog; also FA:381 backupFeedsErrorDialog(null) inside the backupFeedsChoose callback. Body FA:292-304. |
| 28 | FeedActivity.getCurrentFeedItemsFragment()FeedItemsFragment | REACHABLE | SOURCE | FA:185 getCurrentFeedItemsFragment() in subscribeMsgViewModel (feeds-deleted lambda). Body FA:227-236 (two-pane guard :229-230, findFragmentById :233, instanceof check :235). |
| 29 | FeedActivity.initLayout()V | REACHABLE | SOURCE | FA:102 onCreate body calls initLayout(). Body FA:109-119 (showBlankFragment :111, toolbar setup :112-118, nav-click lambda :116). |
| 30 | FeedActivity.lambda$backupFeeds$4(Uri)Object | REACHABLE | INFERRED | FA:348-350 fromCallable lambda inside backupFeeds (viewModel.saveFeedsSync(file), return true). Rx/Completable dispatch unprinted. |
| 31 | FeedActivity.lambda$backupFeeds$5()V | REACHABLE | INFERRED | FA:353-356 subscribe success lambda inside backupFeeds (Toast "backup_feeds_successfully"). Rx dispatch unprinted. |
| 32 | FeedActivity.lambda$initLayout$0(View)V | REACHABLE | INFERRED | FA:116 toolbar setNavigationOnClickListener lambda (v) -> finish(). View-click dispatch unprinted. |
| 33 | FeedActivity.lambda$new$8(ActivityResult)V | REACHABLE | INFERRED | FA:375-386 backupFeedsChoose ActivityResult callback (field initialiser FA:373-387, registerForActivityResult). ActivityResult dispatch unprinted; body calls backupFeeds :385 and backupFeedsErrorDialog :381. |
| 34 | FeedActivity.lambda$new$9(ActivityResult)V | REACHABLE | INFERRED | FA:391-402 restoreFeedsBackupChoose ActivityResult callback (field initialiser FA:389-403). ActivityResult dispatch unprinted; body calls restoreFeedsBackup :401 and restoreFeedsBackupErrorDialog :397. |
| 35 | FeedActivity.lambda$restoreFeedsBackup$6(Uri)[J | REACHABLE | INFERRED | FA:361 fromCallable lambda inside restoreFeedsBackup (viewModel.restoreFeedsSync(file)). Rx dispatch unprinted. Cross-note (not judged here): :361 is a printed caller for FeedViewModel.restoreFeedsSync, which batch 101 left OPEN. |
| 36 | FeedActivity.lambda$restoreFeedsBackup$7([J)V | REACHABLE | INFERRED | FA:364-370 subscribe success lambda inside restoreFeedsBackup (Toast, viewModel.refreshFeeds :369). Rx dispatch unprinted. |
| 37 | FeedActivity.lambda$subscribeAlertDialog$1(BaseAlertDialog$Event)V | REACHABLE | INFERRED | FA:141-168 event lambda subscribed at FA:140-141 (dialogViewModel.observeEvents). Rx dispatch unprinted; body handles POSITIVE/NEGATIVE_BUTTON_CLICKED for the two error-report dialogs. |
| 38 | FeedActivity.lambda$subscribeMsgViewModel$2(Boolean)V | REACHABLE | INFERRED | FA:180 observeFeedItemsClosed subscribe lambda (__) -> showBlankFragment(), subscribed at FA:178-180. Rx dispatch unprinted. Cross-note (not judged here): FA:174 observeFeedItemsOpened and FA:410 feedItemsClosed() are printed call sites for MsgFeedViewModel rows batch 101 left OPEN. |
| 39 | FeedActivity.lambda$subscribeMsgViewModel$3(List)V | REACHABLE | INFERRED | FA:184-188 observeFeedsDeleted subscribe lambda (ids) -> showBlankFragment if the current fragment's feed was deleted, subscribed at FA:182-184. Rx dispatch unprinted. |
| 40 | FeedActivity.onCreate(Bundle)V | REACHABLE | INFERRED | FA:91-107 body (theme :93, ViewModelProvider :96-99, setContentView :101, initLayout :102, fragment-manager lookup of the two error-report dialogs :104-106). Activity lifecycle dispatch unprinted. |

## Caveats / still owed before merge

1. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here, never claimed passed.
2. No saved full-repo grep was run in this pass; no connector search_code result was used as evidence of absence. No row was flipped to UNREACHABLE.
3. Lambda $ numbering is source-order matched to plan signatures, not bytecode-verified.
4. No fresh HTTP 429 was hit in this pass (this pass worked from printed source saved in `~/workspace/b9798-src/` and the local plan copy; no new connector fetch was required to close any row, and none was retried in a loop).
5. Scope kept exactly: this batch only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis, no push, no graph edits.
