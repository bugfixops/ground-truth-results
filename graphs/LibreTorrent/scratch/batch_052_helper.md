# LibreTorrent batch 52 source audit

Membership is exactly the 40 plan rows printed at the top of `batch_052_helper_printed.txt`. Evidence includes the DAO interfaces, repository wrappers, `AppDatabase`, `RepositoryHelper`, caller search, and generated Room source inventory. The generated `FeedDao_Impl`, `TagInfoDao_Impl`, and `TorrentDao_Impl` classes are absent from the uploaded Java source. Their methods remain OPEN rather than being reconstructed from Room behavior. The abstract `TorrentDao.replaceTags` also stays OPEN because its implementation and the full application route are unresolved. No missing caller match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `FeedDao_Impl$8.call()FeedChannel` | OPEN | `FeedDao_Impl` generated-source search has no uploaded match; Room query callback route unresolved. |
| 2 | `FeedDao_Impl$8.finalize()V` | OPEN | Generated class source absent; query cleanup/finalization route unavailable for source confirmation. |
| 3 | `FeedDao_Impl$9.<init>(FeedDao_Impl,RoomSQLiteQuery)V` | OPEN | Generated class source absent; Room query adapter construction route unresolved. |
| 4 | `FeedDao_Impl$9.call()List` | OPEN | Generated class source absent; Room query callback route unresolved. |
| 5 | `FeedDao_Impl$9.finalize()V` | OPEN | Generated class source absent; query cleanup/finalization route unavailable for source confirmation. |
| 6 | `TagInfoDao_Impl.<init>(RoomDatabase)V` | OPEN | Generated implementation source absent; Room database construction dispatch unresolved. |
| 7 | `TagInfoDao_Impl.delete(TagInfo)V` | OPEN | Generated implementation source absent; complete repository/UI route unresolved. |
| 8 | `TagInfoDao_Impl.getByName(String)TagInfo` | OPEN | Generated implementation source absent; complete repository/UI route unresolved. |
| 9 | `TagInfoDao_Impl.getByTorrentId(String)List` | OPEN | Generated implementation source absent; complete repository route unresolved. |
| 10 | `TagInfoDao_Impl.getByTorrentIdAsync(String)Single` | OPEN | Generated implementation source absent; Room/Rx dispatch route unresolved. |
| 11 | `TagInfoDao_Impl.getRequiredConverters()List` | OPEN | Generated implementation source absent; Room converter lookup unresolved. |
| 12 | `TagInfoDao_Impl.insert(TagInfo)V` | OPEN | Generated implementation source absent; complete repository/UI route unresolved. |
| 13 | `TagInfoDao_Impl.observeAll()Flowable` | OPEN | Generated implementation source absent; Room/Rx subscription path unresolved. |
| 14 | `TagInfoDao_Impl.observeByTorrentId(String)Flowable` | OPEN | Generated implementation source absent; Room/Rx subscription path unresolved. |
| 15 | `TagInfoDao_Impl.update(TagInfo)V` | OPEN | Generated implementation source absent; complete repository/UI route unresolved. |
| 16 | `TagInfoDao_Impl$1.<init>(TagInfoDao_Impl,RoomDatabase)V` | OPEN | Generated adapter source absent; Room statement setup route unresolved. |
| 17 | `TagInfoDao_Impl$1.bind(SupportSQLiteStatement,TagInfo)V` | OPEN | Generated adapter source absent; Room statement binding route unresolved. |
| 18 | `TagInfoDao_Impl$1.createQuery()String` | OPEN | Generated adapter source absent; Room statement adapter route unresolved. |
| 19 | `TagInfoDao_Impl$2.<init>(TagInfoDao_Impl,RoomDatabase)V` | OPEN | Generated adapter source absent; Room statement setup route unresolved. |
| 20 | `TagInfoDao_Impl$2.bind(SupportSQLiteStatement,TagInfo)V` | OPEN | Generated adapter source absent; Room statement binding route unresolved. |
| 21 | `TagInfoDao_Impl$2.createQuery()String` | OPEN | Generated adapter source absent; Room statement adapter route unresolved. |
| 22 | `TagInfoDao_Impl$3.<init>(TagInfoDao_Impl,RoomDatabase)V` | OPEN | Generated adapter source absent; Room statement setup route unresolved. |
| 23 | `TagInfoDao_Impl$3.bind(SupportSQLiteStatement,TagInfo)V` | OPEN | Generated adapter source absent; Room statement binding route unresolved. |
| 24 | `TagInfoDao_Impl$3.createQuery()String` | OPEN | Generated adapter source absent; Room statement adapter route unresolved. |
| 25 | `TagInfoDao_Impl$4.<init>(TagInfoDao_Impl,RoomSQLiteQuery)V` | OPEN | Generated query adapter source absent; Room query dispatch unresolved. |
| 26 | `TagInfoDao_Impl$4.call()List` | OPEN | Generated query adapter source absent; Room query callback route unresolved. |
| 27 | `TagInfoDao_Impl$4.finalize()V` | OPEN | Generated query adapter source absent; query cleanup/finalization route unavailable for source confirmation. |
| 28 | `TagInfoDao_Impl$5.<init>(TagInfoDao_Impl,RoomSQLiteQuery)V` | OPEN | Generated query adapter source absent; Room query dispatch unresolved. |
| 29 | `TagInfoDao_Impl$5.call()List` | OPEN | Generated query adapter source absent; Room query callback route unresolved. |
| 30 | `TagInfoDao_Impl$5.finalize()V` | OPEN | Generated query adapter source absent; query cleanup/finalization route unavailable for source confirmation. |
| 31 | `TagInfoDao_Impl$6.<init>(TagInfoDao_Impl,RoomSQLiteQuery)V` | OPEN | Generated query adapter source absent; Room query dispatch unresolved. |
| 32 | `TagInfoDao_Impl$6.call()List` | OPEN | Generated query adapter source absent; Room query callback route unresolved. |
| 33 | `TagInfoDao_Impl$6.finalize()V` | OPEN | Generated query adapter source absent; query cleanup/finalization route unavailable for source confirmation. |
| 34 | `TorrentDao.<init>()V` | OPEN | Abstract DAO declaration printed; generated implementation and full construction route unresolved. |
| 35 | `TorrentDao.replaceTags(String,List)V` | OPEN | DAO declaration printed; generated implementation and full repository/UI route unresolved. |
| 36 | `TorrentDao_Impl.<init>(RoomDatabase)V` | OPEN | Generated implementation source absent; Room database construction dispatch unresolved. |
| 37 | `TorrentDao_Impl.add(Torrent)V` | OPEN | Generated implementation source absent; complete repository/session route unresolved. |
| 38 | `TorrentDao_Impl.addTag(TorrentTagInfo)V` | OPEN | Generated implementation source absent; complete repository/session route unresolved. |
| 39 | `TorrentDao_Impl.addTags(List)V` | OPEN | Generated implementation source absent; complete repository/session route unresolved. |
| 40 | `TorrentDao_Impl.delete(Torrent)V` | OPEN | Generated implementation source absent; complete repository/session route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
