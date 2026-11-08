# LibreTorrent batch 101 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 101 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. FeedFragment and FeedViewModel show local observable/worker scheduling logic; FileManagerAdapter contains RecyclerView binding and click callbacks. This bounded audit did not trace all app-entry routes, WorkManager dispatch, or all adapter callback cases. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `FeedFragment.subscribeAlertDialog` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 2 | `FeedFragment.subscribeMsgViewModel` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 3 | `FeedFragment.subscribeRefreshStatus` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 4 | `FeedFragment$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedFragment;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 5 | `FeedFragment$1.canReuseUpdatedViewHolder` | `(Landroidx/recyclerview/widget/RecyclerView$ViewHolder;)Z` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 6 | `FeedFragment$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedFragment;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 7 | `FeedFragment$2.onSelectionChanged` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 8 | `FeedFragment$2.onSelectionRestored` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 9 | `FeedFragment$3.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/feeds/FeedFragment;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 10 | `FeedFragment$3.onActionItemClicked` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/MenuItem;)Z` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 11 | `FeedFragment$3.onCreateActionMode` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 12 | `FeedFragment$3.onDestroyActionMode` | `(Landroidx/appcompat/view/ActionMode;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 13 | `FeedFragment$3.onPrepareActionMode` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 14 | `FeedViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 15 | `FeedViewModel.copyFeedUrlToClipboard` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)Z` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 16 | `FeedViewModel.deleteFeeds` | `(Ljava/util/List;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 17 | `FeedViewModel.getAllFeedsSingle` | `()Lio/reactivex/Single;` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 18 | `FeedViewModel.lambda$deleteFeeds$0` | `(Ljava/util/List;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 19 | `FeedViewModel.lambda$markAsReadFeeds$1` | `(Ljava/util/List;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 20 | `FeedViewModel.markAsReadFeeds` | `(Ljava/util/List;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 21 | `FeedViewModel.observeRefreshStatus` | `()Lio/reactivex/Observable;` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 22 | `FeedViewModel.observeWorkResult` | `(Landroidx/work/WorkInfo;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 23 | `FeedViewModel.observerAllFeeds` | `()Lio/reactivex/Flowable;` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 24 | `FeedViewModel.onCleared` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 25 | `FeedViewModel.refreshAllFeeds` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 26 | `FeedViewModel.refreshFeeds` | `([J)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 27 | `FeedViewModel.restoreFeedsSync` | `(Landroid/net/Uri;)[J` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 28 | `FeedViewModel.runFetchWorker` | `(Landroidx/work/WorkRequest;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 29 | `FeedViewModel.saveFeedsSync` | `(Landroid/net/Uri;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 30 | `MsgFeedViewModel.<init>` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 31 | `MsgFeedViewModel.feedItemsClosed` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 32 | `MsgFeedViewModel.feedItemsOpened` | `(J)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 33 | `MsgFeedViewModel.feedsDeleted` | `(Ljava/util/List;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 34 | `MsgFeedViewModel.observeFeedItemsClosed` | `()Lio/reactivex/Observable;` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 35 | `MsgFeedViewModel.observeFeedItemsOpened` | `()Lio/reactivex/Observable;` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 36 | `MsgFeedViewModel.observeFeedsDeleted` | `()Lio/reactivex/Observable;` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 37 | `FileManagerAdapter.<clinit>` | `()V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 38 | `FileManagerAdapter.<init>` | `(Ljava/util/List;Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerAdapter$ViewHolder$ClickListener;)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 39 | `FileManagerAdapter.lambda$static$0` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerNode;Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerNode;)I` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |
| 40 | `FileManagerAdapter.onBindViewHolder` | `(Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerAdapter$ViewHolder;I)V` | OPEN | Local feed fragment/ViewModel or adapter code exists; full entry and WorkManager/selection callback routes were not verified. |

## Evidence
- `FeedFragment.java:209-211`: subscribes to alert/message/refresh sources; action-mode callbacks around 124-405.
- `FeedViewModel.java:75-168`: feed queries, mutations, refresh scheduling, persistence and WorkInfo observation.
- `MsgFeedViewModel.java:29-60`: event subjects and observe/send methods.
- `FileManagerAdapter.java:50-130`: adapter construction, holder binding and click callback.
These source-local calls do not establish full routes for the target methods.

