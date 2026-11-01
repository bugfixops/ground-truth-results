# Spot-check — batch 52 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 52/1 FeedDao_Impl$8.call — REACHABLE INFERRED — PASS. getFeedByIdSingle Callable call(); pinned, not merely set-assigned: its descriptor returns FeedChannel, and getFeedByIdSingle (FeedDao.java:70, fresh) is the ONLY Rx method returning a single FeedChannel; runs when the Single from FeedRepositoryImpl.getFeedByIdSingle (FeedRepositoryImpl.java:122, fresh) is subscribed.
- 52/6 TagInfoDao_Impl.\<init\> — REACHABLE INFERRED — PASS. Generated class, no printed def; constructed when tagInfoDao() (AppDatabase.java:67, fresh) is first called; TagRepositoryImpl calls db.tagInfoDao() in every method (TagRepositoryImpl.java:40,45,50,55,60,65,70,75, fresh); dispatch unprinted, hence INFERRED.
- 52/11 TagInfoDao_Impl.getRequiredConverters — REACHABLE INFERRED — PASS. The cell's final substantive statement is the applied decision: "[APPLIED 2026-11-01 D3c: OPEN → REACHABLE INFERRED per DECISIONS.md]". Earlier "stays OPEN (batch-48/53 precedent)" history and the OPEN-CLOSE2 conditional text are superseded by that applied decision (same pattern as 51/6).
- 52/16 TagInfoDao_Impl$1.\<init\> — REACHABLE INFERRED — PASS. Insertion adapter for TagInfo, constructed in the _Impl constructor; TagInfoDao inserts TagInfo only via insert (TagInfoDao.java:39, fresh); runs on every insert (TagRepositoryImpl.java:40, fresh; caller AddTagViewModel.java:69, fresh); no printed generated def, INFERRED; strict-$N-rule note stated in row.
- 52/21 TagInfoDao_Impl$2.createQuery — REACHABLE INFERRED — PASS. Returns the TagInfo DELETE SQL (row 19 route) or UPDATE SQL (if $2 is the update adapter) on every delete/update — either way it runs, per row 19; no printed generated def, INFERRED; strict-$N-rule note stated in row.
- 52/26 TagInfoDao_Impl$4.call — REACHABLE INFERRED — PASS. Runs when the Flowable/Single from row 25's method is subscribed (Rx step INFERRED); no printed generated def; strict-$N-rule note stated in row.
- 52/31 TagInfoDao_Impl$6.\<init\> — REACHABLE INFERRED — PASS. Callable for a List-returning Rx query (set note at row 25; proposal lead order: getByTorrentIdAsync); created when TagRepositoryImpl.getByTorrentIdAsync runs (TagRepositoryImpl.java:70, fresh; caller DetailTorrentViewModel.java:144, fresh) under the lead order, and under any set assignment its method is called.
- 52/36 TorrentDao_Impl.\<init\> — REACHABLE INFERRED — PASS. Generated subclass constructor, created when torrentDao() is first called (same TorrentRepositoryImpl call sites as row 34, fresh); generated source not in the upload, hence INFERRED.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
