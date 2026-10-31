# LibreTorrent batch 53 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, exact `batch == 53` rows only. Count: 40.

Status summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. All unresolved because the available source shows local declaration/use but no complete hand-authored route from an app entry point. Generated Room implementation is not present as Java source; Room/library dispatch remains unverified. DefaultFsModule has a direct constructor call in FsModuleResolverImpl, but full app-entry route and individual dispatch paths are not established here, so those methods remain OPEN.

| Plan row | JVM method | Descriptor | Status | Evidence / remaining route gap |
|---:|---|---|---|---|
| 1 | `TorrentDao_Impl.deleteTag` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TorrentTagInfo;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 2 | `TorrentDao_Impl.deleteTagsByTorrentId` | `(Ljava/lang/String;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 3 | `TorrentDao_Impl.getAllTorrents` | `()Ljava/util/List;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 4 | `TorrentDao_Impl.getRequiredConverters` | `()Ljava/util/List;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 5 | `TorrentDao_Impl.getTorrentById` | `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 6 | `TorrentDao_Impl.getTorrentByIdSingle` | `(Ljava/lang/String;)Lio/reactivex/Single;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 7 | `TorrentDao_Impl.observeTorrentById` | `(Ljava/lang/String;)Lio/reactivex/Flowable;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 8 | `TorrentDao_Impl.replaceTags` | `(Ljava/lang/String;Ljava/util/List;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 9 | `TorrentDao_Impl.update` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 10 | `TorrentDao_Impl$1.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomDatabase;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 11 | `TorrentDao_Impl$1.bind` | `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 12 | `TorrentDao_Impl$1.createQuery` | `()Ljava/lang/String;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 13 | `TorrentDao_Impl$2.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomDatabase;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 14 | `TorrentDao_Impl$2.bind` | `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TorrentTagInfo;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 15 | `TorrentDao_Impl$2.createQuery` | `()Ljava/lang/String;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 16 | `TorrentDao_Impl$3.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomDatabase;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 17 | `TorrentDao_Impl$3.bind` | `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 18 | `TorrentDao_Impl$3.createQuery` | `()Ljava/lang/String;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 19 | `TorrentDao_Impl$4.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomDatabase;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 20 | `TorrentDao_Impl$4.bind` | `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TorrentTagInfo;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 21 | `TorrentDao_Impl$4.createQuery` | `()Ljava/lang/String;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 22 | `TorrentDao_Impl$5.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomDatabase;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 23 | `TorrentDao_Impl$5.bind` | `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 24 | `TorrentDao_Impl$5.createQuery` | `()Ljava/lang/String;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 25 | `TorrentDao_Impl$6.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomDatabase;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 26 | `TorrentDao_Impl$6.createQuery` | `()Ljava/lang/String;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 27 | `TorrentDao_Impl$7.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 28 | `TorrentDao_Impl$7.call` | `()Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 29 | `TorrentDao_Impl$7.finalize` | `()V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 30 | `TorrentDao_Impl$8.<init>` | `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 31 | `TorrentDao_Impl$8.call` | `()Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 32 | `TorrentDao_Impl$8.finalize` | `()V` | OPEN | Target is generated Room DAO implementation/internal adapter; complete hand-authored app-entry route not established. |
| 33 | `DefaultFsModule.<init>` | `(Landroid/content/Context;)V` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 34 | `DefaultFsModule.delete` | `(Landroid/net/Uri;)Z` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 35 | `DefaultFsModule.fileExists` | `(Landroid/net/Uri;)Z` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 36 | `DefaultFsModule.getDirAvailableBytes` | `(Landroid/net/Uri;)J` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 37 | `DefaultFsModule.getDirPath` | `(Landroid/net/Uri;)Ljava/lang/String;` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 38 | `DefaultFsModule.getFilePath` | `(Landroid/net/Uri;)Ljava/lang/String;` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 39 | `DefaultFsModule.getFileUri(Uri,String,boolean)` | `(Landroid/net/Uri;Ljava/lang/String;Z)Landroid/net/Uri;` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |
| 40 | `DefaultFsModule.getFileUri(String,Uri)` | `(Ljava/lang/String;Landroid/net/Uri;)Landroid/net/Uri;` | OPEN | Target is generated app implementation method; complete hand-authored app-entry route not established. |

## Evidence
- Printed app source shows `TorrentDao` declarations/transaction helper at `app/src/main/java/org/proninyaroslav/libretorrent/core/storage/dao/TorrentDao.java:37-77`; generated `TorrentDao_Impl.java` is absent from source tree (compiled class files exist only under build intermediates, not used as source evidence).
- Printed `DefaultFsModule.java:31-133` shows constructor and method bodies. `FsModuleResolverImpl.java:38` constructs the module, but a full entry route was not traced.
- `FeedDao` precedent is not used for membership. No coverage data was consulted.

