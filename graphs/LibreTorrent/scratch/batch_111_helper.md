# LibreTorrent batch 111 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 111 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. MainFragment has action-mode handlers and calls into MainViewModel; the ViewModel exposes torrent operations, streams, filters, and engine controls. However this bounded pass did not verify every route back to the app's entry point, activity/fragment lifecycle and framework action-mode dispatch. All rows remain OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `MainFragment$3.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/main/MainFragment;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 2 | `MainFragment$3.onActionItemClicked` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/MenuItem;)Z` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 3 | `MainFragment$3.onCreateActionMode` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 4 | `MainFragment$3.onDestroyActionMode` | `(Landroidx/appcompat/view/ActionMode;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 5 | `MainFragment$3.onPrepareActionMode` | `(Landroidx/appcompat/view/ActionMode;Landroid/view/Menu;)Z` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 6 | `MainViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 7 | `MainViewModel.deleteTag` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Lio/reactivex/Completable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 8 | `MainViewModel.deleteTorrents` | `(Ljava/util/List;Z)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 9 | `MainViewModel.forceAnnounceTorrents` | `(Ljava/util/List;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 10 | `MainViewModel.forceRecheckTorrents` | `(Ljava/util/List;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 11 | `MainViewModel.getAllTorrentsInfoSingle` | `()Lio/reactivex/Single;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 12 | `MainViewModel.getFilter` | `()Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 13 | `MainViewModel.getSorting` | `()Lorg/proninyaroslav/libretorrent/core/sorting/TorrentSortingComparator;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 14 | `MainViewModel.lambda$deleteTag$2` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 15 | `MainViewModel.lambda$getFilter$1` | `(Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;)Z` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 16 | `MainViewModel.lambda$new$0` | `(Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;)Z` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 17 | `MainViewModel.observeAllTorrentsInfo` | `()Lio/reactivex/Flowable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 18 | `MainViewModel.observeForceSortAndFilter` | `()Lio/reactivex/Observable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 19 | `MainViewModel.observeNeedStartEngine` | `()Lio/reactivex/Flowable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 20 | `MainViewModel.observeTags` | `()Lio/reactivex/Flowable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 21 | `MainViewModel.observeTorrentsDeleted` | `()Lio/reactivex/Flowable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 22 | `MainViewModel.pauseAll` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 23 | `MainViewModel.pauseResumeTorrent` | `(Ljava/lang/String;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 24 | `MainViewModel.requestStopEngine` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 25 | `MainViewModel.resetSearch` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 26 | `MainViewModel.restartForegroundNotification` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 27 | `MainViewModel.resumeAll` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 28 | `MainViewModel.setDateAddedFilter` | `(Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;Z)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 29 | `MainViewModel.setSearchQuery` | `(Ljava/lang/String;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 30 | `MainViewModel.setSort` | `(Lorg/proninyaroslav/libretorrent/core/sorting/TorrentSortingComparator;Z)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 31 | `MainViewModel.setStatusFilter` | `(Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;Z)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 32 | `MainViewModel.setTagFilter` | `(Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;Z)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 33 | `MainViewModel.startEngine` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 34 | `MainViewModel.stopEngine` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 35 | `MsgMainViewModel.<init>` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 36 | `MsgMainViewModel.observeTorrentDetailsClosed` | `()Lio/reactivex/Observable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 37 | `MsgMainViewModel.observeTorrentDetailsOpened` | `()Lio/reactivex/Observable;` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 38 | `MsgMainViewModel.torrentDetailsClosed` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 39 | `MsgMainViewModel.torrentDetailsOpened` | `(Ljava/lang/String;)V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |
| 40 | `TorrentListAdapter.<clinit>` | `()V` | OPEN | Main fragment/ViewModel local callers and action-mode callbacks appear in source; complete entry and lifecycle routes were not verified for each row. |

## Evidence
- `MainFragment.java:287-389`: torrent list setup, message subscriptions, and local pause/details calls.
- `MainFragment.java:460-501`: action-mode callbacks and dialog launching.
- `MainViewModel.java:48-186`: state/stream and operation methods.
- `MsgMainViewModel.java:28-50`: opened/closed subject methods.
The source evidence is partial, not full route verification.

