# Spot-check — batch 50 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 50/1 TagRepositoryImpl.getByTorrentIdAsync — REACHABLE SOURCE — PASS. Definition TagRepositoryImpl.java:69-70 (db.tagInfoDao().getByTorrentIdAsync); caller DetailTorrentViewModel.java:144 (fresh).
- 50/6 TorrentRepositoryImpl.\<clinit\> — REACHABLE INFERRED — PASS. No source def (JVM static initialiser; non-constant TAG = getSimpleName() at TorrentRepositoryImpl.java:41, fresh); runs on first use of the class; class constructed at RepositoryHelper.java:46-47 (fresh). \<clinit\>-on-first-use convention (ix) noted as undecided project-wide in the row; here first use (construction) IS printed.
- 50/11 TorrentRepositoryImpl.deleteTag — REACHABLE SOURCE — PASS. Definition TorrentRepositoryImpl.java:136-138 (db.torrentDao().deleteTag); caller DetailTorrentViewModel.java:156 (fresh).
- 50/16 TorrentRepositoryImpl.getTorrentById — REACHABLE SOURCE — PASS. Definition TorrentRepositoryImpl.java:71-73 (db.torrentDao().getTorrentById); callers TorrentEngine.java:767,840 and TorrentSessionImpl.java:280,335,384 (fresh).
- 50/21 TorrentRepositoryImpl.updateTorrent — REACHABLE SOURCE — PASS. Definition TorrentRepositoryImpl.java:61-63 (db.torrentDao().update); callers TorrentEngine.java:1262 and TorrentSessionImpl.java:1524 (fresh).
- 50/26 FastResumeDao_Impl.getByTorrentId — REACHABLE INFERRED — PASS. Generated implementation of FastResumeDao.getByTorrentId (FastResumeDao.java:17, @Query, fresh); via TorrentRepositoryImpl.java:97 (row 14, fresh); upstream caller TorrentSessionImpl.java:1686 (fresh); Room dispatch unprinted, hence INFERRED.
- 50/31 FeedDao_Impl.\<init\> — REACHABLE INFERRED — PASS. Generated class, no printed def; constructed when feedDao() (AppDatabase.java:65, fresh) is first called; that accessor is called by every FeedRepositoryImpl method (e.g. FeedRepositoryImpl.java:86,92,104, fresh); dispatch unprinted, hence INFERRED.
- 50/36 FeedDao_Impl.deleteFeeds — REACHABLE INFERRED — PASS. Generated implementation of FeedDao.deleteFeeds (FeedDao.java:64, fresh); via FeedRepositoryImpl.java:110 (fresh); caller FeedViewModel.java:87 (fresh); Room dispatch unprinted, hence INFERRED.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
