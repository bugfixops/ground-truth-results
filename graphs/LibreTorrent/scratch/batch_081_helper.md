# LibreTorrent batch 81 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 81 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. Source shows an AddTorrentPagerAdapter and AddTorrentViewModel with decode, file-tree, selection, tag, and torrent-add operations. Activity/fragment observers are candidate callers, but this bounded pass does not verify the complete route and guards for every target. Leave all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `AddTorrentMutableParams.setStorageFreeSpace` | `(J)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 2 | `AddTorrentMutableParams.toString` | `()Ljava/lang/String;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 3 | `AddTorrentPagerAdapter.<init>` | `(Landroidx/fragment/app/FragmentActivity;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 4 | `AddTorrentPagerAdapter.createFragment` | `(I)Landroidx/fragment/app/Fragment;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 5 | `AddTorrentPagerAdapter.getItemCount` | `()I` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 6 | `AddTorrentViewModel.<clinit>` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 7 | `AddTorrentViewModel.<init>` | `(Landroid/app/Application;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 8 | `AddTorrentViewModel.addTag` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 9 | `AddTorrentViewModel.addTorrent` | `()Z` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 10 | `AddTorrentViewModel.cancelFetchMagnet` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 11 | `AddTorrentViewModel.checkFreeSpace` | `()Z` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 12 | `AddTorrentViewModel.chooseDirectory` | `(Ljava/lang/String;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 13 | `AddTorrentViewModel.finish` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 14 | `AddTorrentViewModel.getChildren` | `(Lorg/proninyaroslav/libretorrent/core/model/filetree/BencodeFileTree;)Ljava/util/List;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 15 | `AddTorrentViewModel.getCurrentTags` | `()Ljava/util/List;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 16 | `AddTorrentViewModel.getDecodeState` | `()Landroidx/lifecycle/LiveData;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 17 | `AddTorrentViewModel.getSelectedFileIndexes` | `()Ljava/util/Set;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 18 | `AddTorrentViewModel.lambda$addTorrent$5` | `(Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams;[Ljava/lang/Exception;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 19 | `AddTorrentViewModel.lambda$new$0` | `(Ljava/lang/Boolean;)Z` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 20 | `AddTorrentViewModel.lambda$new$1` | `(Ljava/lang/Boolean;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 21 | `AddTorrentViewModel.lambda$observeFetchedMetadata$3` | `(Lorg/proninyaroslav/libretorrent/core/model/data/metainfo/TorrentMetaInfo;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 22 | `AddTorrentViewModel.lambda$observeFetchedMetadata$4` | `(Ljava/lang/Throwable;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 23 | `AddTorrentViewModel.lambda$startDecode$2` | `(Landroid/net/Uri;Ljava/lang/Boolean;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 24 | `AddTorrentViewModel.makeFileTree` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 25 | `AddTorrentViewModel.observeFetchedMetadata` | `(Lio/reactivex/Single;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 26 | `AddTorrentViewModel.observeTags` | `()Lio/reactivex/Observable;` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 27 | `AddTorrentViewModel.onCleared` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 28 | `AddTorrentViewModel.removeTag` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 29 | `AddTorrentViewModel.restartForegroundNotification` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 30 | `AddTorrentViewModel.selectFile` | `(Ljava/lang/String;Z)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 31 | `AddTorrentViewModel.startDecode` | `(Landroid/net/Uri;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 32 | `AddTorrentViewModel.startDecodeTask` | `(Landroid/net/Uri;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 33 | `AddTorrentViewModel.upToParentDirectory` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 34 | `AddTorrentViewModel.updateChildren` | `()V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 35 | `AddTorrentViewModel.updateCurDir` | `(Lorg/proninyaroslav/libretorrent/core/model/filetree/BencodeFileTree;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 36 | `AddTorrentViewModel$1.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 37 | `AddTorrentViewModel$1.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 38 | `AddTorrentViewModel$2.<init>` | `(Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 39 | `AddTorrentViewModel$2.lambda$onPropertyChanged$0` | `(Landroid/net/Uri;)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |
| 40 | `AddTorrentViewModel$2.onPropertyChanged` | `(Landroidx/databinding/Observable;I)V` | OPEN | Local view-model/pager operations exist; complete route from activity entry through observers/callbacks was not verified row by row. |

## Evidence
- `AddTorrentPagerAdapter.java`: class and `createFragment`/item count at lines 28, 41, 53.
- `AddTorrentViewModel.java`: class line 78; tag/decode accessors and lifecycle lines 149-197; metadata and tree operations 328-454; `addTorrent` line 466 and free-space check at 548; finish/cancel around 558-565.
- These source-local methods and calls do not establish every target's complete app-entry route.

