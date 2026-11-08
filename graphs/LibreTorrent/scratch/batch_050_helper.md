# LibreTorrent batch 50 source audit

Membership is exactly the 40 batch 50 rows printed at the top of `batch_050_helper_printed.txt`. The evidence includes the repository implementations and interfaces, `UriConverter`, database construction context, direct caller search, and source-inventory searches for generated Room DAO implementations. The generated `FastResumeDao_Impl` and `FeedDao_Impl` sources are not present in the uploaded Java tree; their methods remain OPEN rather than being reconstructed from Room behavior. The other repository/converter methods also remain OPEN because complete entry-to-method paths, including Room dispatch for DAO calls, were not traced end-to-end. No missing caller match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `TagRepositoryImpl.getByTorrentIdAsync(String)Single` | OPEN | `TagRepositoryImpl.java:69+`; repository body/callers printed, Room DAO execution and complete entry path unresolved. |
| 2 | `TagRepositoryImpl.insert(TagInfo)V` | OPEN | `TagRepositoryImpl.java:39+`; body/callers printed, complete UI-to-repository route unresolved. |
| 3 | `TagRepositoryImpl.observeAll()Flowable` | OPEN | `TagRepositoryImpl.java:59+`; body/callers printed, subscription/delivery path unresolved. |
| 4 | `TagRepositoryImpl.observeByTorrentId(String)Flowable` | OPEN | `TagRepositoryImpl.java:64+`; body/callers printed, subscription/delivery path unresolved. |
| 5 | `TagRepositoryImpl.update(TagInfo)V` | OPEN | `TagRepositoryImpl.java:44+`; body/callers printed, complete UI-to-repository route unresolved. |
| 6 | `TorrentRepositoryImpl.<clinit>()V` | OPEN | Repository class source printed; class initialization via app entry was not traced. |
| 7 | `TorrentRepositoryImpl.<init>(Context,AppDatabase)V` | OPEN | Constructor and `RepositoryHelper` construction context printed; complete app startup route unresolved. |
| 8 | `TorrentRepositoryImpl.addFastResume(FastResume)V` | OPEN | `TorrentRepositoryImpl.java:91+`; body/callers printed; full session-to-storage entry route unresolved. |
| 9 | `TorrentRepositoryImpl.addTag(String,TagInfo)V` | OPEN | `TorrentRepositoryImpl.java:131+`; body/callers printed; complete UI-to-storage route unresolved. |
| 10 | `TorrentRepositoryImpl.addTorrent(Torrent)V` | OPEN | `TorrentRepositoryImpl.java:56+`; body/callers printed; complete session-to-storage route unresolved. |
| 11 | `TorrentRepositoryImpl.deleteTag(String,TagInfo)V` | OPEN | `TorrentRepositoryImpl.java:136+`; body/callers printed; complete UI-to-storage route unresolved. |
| 12 | `TorrentRepositoryImpl.deleteTorrent(Torrent)V` | OPEN | `TorrentRepositoryImpl.java:66+`; body/callers printed; complete session/UI route unresolved. |
| 13 | `TorrentRepositoryImpl.getAllTorrents()List` | OPEN | `TorrentRepositoryImpl.java:86+`; body/callers printed; complete startup/session route unresolved. |
| 14 | `TorrentRepositoryImpl.getFastResumeById(String)FastResume` | OPEN | `TorrentRepositoryImpl.java:96+`; body/callers printed; complete restore route unresolved. |
| 15 | `TorrentRepositoryImpl.getSessionFile()String` | OPEN | `TorrentRepositoryImpl.java:109+`; body/callers printed; complete session startup route unresolved. |
| 16 | `TorrentRepositoryImpl.getTorrentById(String)Torrent` | OPEN | `TorrentRepositoryImpl.java:71+`; body/callers printed; complete session/UI route unresolved. |
| 17 | `TorrentRepositoryImpl.getTorrentByIdSingle(String)Single` | OPEN | `TorrentRepositoryImpl.java:76+`; body/callers printed; Rx subscription path unresolved. |
| 18 | `TorrentRepositoryImpl.observeTorrentById(String)Flowable` | OPEN | `TorrentRepositoryImpl.java:81+`; body/callers printed; Rx subscription/delivery path unresolved. |
| 19 | `TorrentRepositoryImpl.replaceTags(String,List)V` | OPEN | `TorrentRepositoryImpl.java:122+`; body/callers printed; complete UI-to-storage route unresolved. |
| 20 | `TorrentRepositoryImpl.saveSession(byte[])V` | OPEN | `TorrentRepositoryImpl.java:101+`; body/callers printed; complete session shutdown route unresolved. |
| 21 | `TorrentRepositoryImpl.updateTorrent(Torrent)V` | OPEN | `TorrentRepositoryImpl.java:61+`; body/callers printed; complete session update route unresolved. |
| 22 | `UriConverter.fromUri(Uri)String` | OPEN | `UriConverter.java:36+`; converter body printed; Room conversion dispatch and entry route unresolved. |
| 23 | `UriConverter.toUri(String)Uri` | OPEN | `UriConverter.java:30+`; converter body printed; Room conversion dispatch and entry route unresolved. |
| 24 | `FastResumeDao_Impl.<init>(RoomDatabase)V` | OPEN | Generated-source search printed no uploaded implementation; Room construction dispatch unavailable for source confirmation. |
| 25 | `FastResumeDao_Impl.add(FastResume)V` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 26 | `FastResumeDao_Impl.getByTorrentId(String)FastResume` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 27 | `FastResumeDao_Impl.getRequiredConverters()List` | OPEN | Generated implementation source absent from upload; Room converter dispatch unresolved. |
| 28 | `FastResumeDao_Impl$1.<init>(FastResumeDao_Impl,RoomDatabase)V` | OPEN | Generated implementation/adapter source absent from upload; Room statement adapter route unresolved. |
| 29 | `FastResumeDao_Impl$1.bind(SupportSQLiteStatement,FastResume)V` | OPEN | Generated implementation source absent from upload; Room statement binding dispatch unresolved. |
| 30 | `FastResumeDao_Impl$1.createQuery()String` | OPEN | Generated implementation source absent from upload; Room statement adapter route unresolved. |
| 31 | `FeedDao_Impl.<init>(RoomDatabase)V` | OPEN | Generated-source search printed no uploaded implementation; Room construction dispatch unavailable for source confirmation. |
| 32 | `FeedDao_Impl.addFeed(FeedChannel)long` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 33 | `FeedDao_Impl.addFeeds(List)long[]` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 34 | `FeedDao_Impl.addItems(List)V` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 35 | `FeedDao_Impl.deleteFeed(FeedChannel)V` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 36 | `FeedDao_Impl.deleteFeeds(List)V` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 37 | `FeedDao_Impl.deleteItemsOlderThan(long)V` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 38 | `FeedDao_Impl.findItemsExistingTitles(List)List` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 39 | `FeedDao_Impl.getAllFeeds()List` | OPEN | Generated implementation source absent from upload; complete DAO route unresolved. |
| 40 | `FeedDao_Impl.getAllFeedsSingle()Single` | OPEN | Generated implementation source absent from upload; Rx/Room DAO dispatch unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
