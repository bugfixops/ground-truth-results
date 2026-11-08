# Spot-check — batch 49 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 49/1 DatabaseMigration$RoomDatabaseMigration.\<init\>(Context) — REACHABLE SOURCE — PASS. Definition DatabaseMigration.java:131-136 (fresh); constructed at DatabaseMigration.java:49 in getMigrations, called from AppDatabase.java:84 in buildDatabase, via getInstance (AppDatabase.java:69-79) via RepositoryHelper.java:47,56,72. Fresh-install-safe (stated in row).
- 49/6 DatabaseMigration$RoomDatabaseMigration.findTorrentDataDir(String) — REACHABLE SOURCE — PASS. Definition DatabaseMigration.java:246-257; called at DatabaseMigration.java:195 inside copyFastResumeData, guarded by torrentDataExists at :192. GATE as row 2 (stated in row).
- 49/11 FeedRepositoryImpl.\<clinit\> — REACHABLE INFERRED — PASS. No source def (JVM static initialiser for TAG :50 and constants :52-54, freshly confirmed); runs on first use of the class; class constructed at RepositoryHelper.java:55-56 and its constants read at FeedActivity.java:271-272,286.
- 49/16 FeedRepositoryImpl.deleteFeed(FeedChannel) — REACHABLE SOURCE — PASS. Definition FeedRepositoryImpl.java:102-105 (fresh); caller AddFeedViewModel.java:133.
- 49/21 FeedRepositoryImpl.getAllFeeds() — REACHABLE SOURCE — PASS. Definition FeedRepositoryImpl.java:132-135 (fresh); caller FeedFetcherWorker.java:100.
- 49/26 FeedRepositoryImpl.getItemsByFeedIdSingle(long) — REACHABLE SOURCE — PASS. Definition FeedRepositoryImpl.java:204-207 (fresh); caller FeedItemsViewModel.java:89.
- 49/31 FeedRepositoryImpl.markAsUnread(String) — REACHABLE SOURCE — PASS. Definition FeedRepositoryImpl.java:186-189 (fresh); caller FeedItemsViewModel.java:131.
- 49/36 FeedRepositoryImpl$1.\<init\>(FeedRepositoryImpl) — REACHABLE INFERRED — PASS. No source def: synthetic anonymous subclass of TypeToken\<ArrayList\<FeedChannel\>\> created at FeedRepositoryImpl.java:160 (fresh) inside deserializeFeeds (row 19); its constructor runs whenever row 19 runs; the $1 numbering is the javac anonymous-class numbering, INFERRED, not printed from bytecode (stated in row).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
