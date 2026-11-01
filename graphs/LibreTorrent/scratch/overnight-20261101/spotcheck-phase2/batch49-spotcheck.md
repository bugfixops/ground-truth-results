# LibreTorrent batch 49 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch49-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only —
  `~/workspace/b474849-src/` (DatabaseMigration, FeedRepositoryImpl, TagRepositoryImpl) and
  the 281-file corpus in `~/workspace/overnight/stream-A/corpus/java/`. No connector fetch
  was needed; no merge-ready file was edited; no label was flipped.
- Rows checked (8): sample 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated
  2026-11-01 Phase 1 revision note listing label changes, so no extra Phase 1 rows apply.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | DatabaseMigration$RoomDatabaseMigration.<init>(Context) | REACHABLE SOURCE | PASS | Constructed at DatabaseMigration.java:49 `new RoomDatabaseMigration(appContext)` in getMigrations (called from AppDatabase.java:84 buildDatabase). Def :131-136 (`super(4, 5)` at :133 in the local copy). Fresh-install-safe, as filed. |
| 6 | DatabaseMigration$RoomDatabaseMigration.findTorrentDataDir(String) | REACHABLE SOURCE | PASS | Called at DatabaseMigration.java:195 inside copyFastResumeData, guarded by torrentDataExists at :192. Def :246-257. Migration STATE gate (pre-existing v4 DB) carried from the file, not decided here. |
| 11 | FeedRepositoryImpl.<clinit> | REACHABLE INFERRED | PASS | Static material FeedRepositoryImpl.java:50 (TAG = getSimpleName()) and :52-54 (SERIALIZE_FILE_FORMAT, SERIALIZE_MIME_TYPE, FILTER_SEPARATOR); class constructed at RepositoryHelper.java:55-56. JVM init INFERRED, as filed. |
| 16 | FeedRepositoryImpl.deleteFeed(FeedChannel) | REACHABLE SOURCE | PASS | Caller AddFeedViewModel.java:133 `repo.deleteFeed(channel)`; def FeedRepositoryImpl.java:102-105 (`db.feedDao().deleteFeed`). |
| 21 | FeedRepositoryImpl.getAllFeeds() | REACHABLE SOURCE | PASS | Caller FeedFetcherWorker.java:100 `repo.getAllFeeds()`; def FeedRepositoryImpl.java:132-135. |
| 26 | FeedRepositoryImpl.getItemsByFeedIdSingle(long) | REACHABLE SOURCE | PASS | Caller FeedItemsViewModel.java:89 `repo.getItemsByFeedIdSingle(feedId)`; def FeedRepositoryImpl.java:204-207. |
| 31 | FeedRepositoryImpl.markAsUnread(String) | REACHABLE SOURCE | PASS | Caller FeedItemsViewModel.java:131 `repo.markAsUnread(itemId)`; def FeedRepositoryImpl.java:186-189. |
| 36 | FeedRepositoryImpl$1.<init> | REACHABLE INFERRED | PASS | Anonymous TypeToken subclass created at FeedRepositoryImpl.java:160 (`new TypeToken<ArrayList<FeedChannel>>(){}`) inside deserializeFeeds (row 19); ctor runs whenever row 19 runs. $1 numbering is javac numbering, not bytecode-verified (caveat carried from the file; label passes). |

## Totals

- Checked: 8. PASS: 8. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: rows 2-10 (RoomDatabaseMigration internals) were not in this batch's check set;
  row 6's migration STATE gate (fresh-install-only rule would flip rows 2-10) is recorded
  in the file and was not decided by this spot-check.
