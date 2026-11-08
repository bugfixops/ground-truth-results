# LibreTorrent batch 89 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 89 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. DetailTorrentViewModel exposes Rx streams, torrent operations, and file-tree helpers; source includes local callbacks and engine calls. This bounded pass does not verify the complete fragment entry path, subscription, dispatch, and conditional routes for each target. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `DetailTorrentViewModel.lambda$addTag$0` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 2 | `DetailTorrentViewModel.lambda$applyPriority$3` | `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/filetree/TorrentContentFileTree;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 3 | `DetailTorrentViewModel.lambda$applyPriority$4` | `(Lorg/proninyaroslav/libretorrent/core/model/filetree/FilePriority;Lorg/proninyaroslav/libretorrent/core/model/filetree/TorrentContentFileTree;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 4 | `DetailTorrentViewModel.lambda$getFilePath$2` | `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;Landroid/content/Context;)Landroid/net/Uri;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 5 | `DetailTorrentViewModel.lambda$removeTag$1` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 6 | `DetailTorrentViewModel.lambda$startMakeFileTree$5` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 7 | `DetailTorrentViewModel.lambda$updateFiles$6` | `([J[D)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 8 | `DetailTorrentViewModel.makeFileTree` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 9 | `DetailTorrentViewModel.makeMagnet` | `(Z)Ljava/lang/String;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 10 | `DetailTorrentViewModel.makeOpenFileIntent` | `(Ljava/lang/String;Landroid/net/Uri;)Landroid/content/Intent;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 11 | `DetailTorrentViewModel.observeAdvancedTorrentInfo` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 12 | `DetailTorrentViewModel.observeFreeSpaceError` | `()Lio/reactivex/Observable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 13 | `DetailTorrentViewModel.observePeers` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 14 | `DetailTorrentViewModel.observePieces` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 15 | `DetailTorrentViewModel.observeTags` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 16 | `DetailTorrentViewModel.observeTorrent` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 17 | `DetailTorrentViewModel.observeTorrentInfo` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 18 | `DetailTorrentViewModel.observeTorrentInfoPair` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 19 | `DetailTorrentViewModel.observeTorrentMetaInfo` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 20 | `DetailTorrentViewModel.observeTrackers` | `()Lio/reactivex/Flowable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 21 | `DetailTorrentViewModel.onCleared` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 22 | `DetailTorrentViewModel.pauseResumeTorrent` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 23 | `DetailTorrentViewModel.removeTag` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)Lio/reactivex/Completable;` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 24 | `DetailTorrentViewModel.replaceTrackers` | `(Ljava/util/List;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 25 | `DetailTorrentViewModel.setSpeedLimit` | `(II)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 26 | `DetailTorrentViewModel.setTorrentId` | `(Ljava/lang/String;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 27 | `DetailTorrentViewModel.startMakeFileTree` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 28 | `DetailTorrentViewModel.upToParentDirectory` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 29 | `DetailTorrentViewModel.updateChildren` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 30 | `DetailTorrentViewModel.updateCurDir` | `(Lorg/proninyaroslav/libretorrent/core/model/filetree/TorrentContentFileTree;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 31 | `DetailTorrentViewModel.updateFiles` | `([J[D)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 32 | `DetailTorrentViewModel.updateInfo(AdvancedTorrentInfo)` | `(Lorg/proninyaroslav/libretorrent/core/model/data/AdvancedTorrentInfo;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 33 | `DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo)` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;Lorg/proninyaroslav/libretorrent/core/model/data/TorrentInfo;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 34 | `DetailTorrentViewModel.updateInfo(TorrentMetaInfo)` | `(Lorg/proninyaroslav/libretorrent/core/model/data/metainfo/TorrentMetaInfo;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 35 | `DetailTorrentViewModel$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 36 | `DetailTorrentViewModel$1.lambda$onPropertyChanged$0` | `(Landroid/net/Uri;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 37 | `DetailTorrentViewModel$1.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 38 | `DetailTorrentViewModel$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel;)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 39 | `DetailTorrentViewModel$2.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |
| 40 | `MsgDetailTorrentViewModel.<init>` | `()V` | OPEN | ViewModel methods and local Rx/engine calls are present; app-entry/observer route is not verified end-to-end for every row. |

## Evidence
- `DetailTorrentViewModel.java:81` class; observable accessors around 147-192; updateInfo overloads around 199-218.
- File-tree helpers and routing around 226-333; operations at 349-398; async tree/update methods around 522-607.
- Local calls establish relationships, not full end-to-end route proof.

