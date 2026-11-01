# LibreTorrent batch 50 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch50-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only —
  `~/workspace/b505152-src/` (TagRepositoryImpl, TorrentRepositoryImpl, FastResumeDao,
  FeedRepositoryImpl, DetailTorrentViewModel, TorrentEngine, RepositoryHelper, AppDatabase).
  No connector fetch was needed; no merge-ready file was edited; no label was flipped.
- Rows checked (9): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase 1c flip row 27.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TagRepositoryImpl.getByTorrentIdAsync | REACHABLE SOURCE | PASS | Caller DetailTorrentViewModel.java:144 `tagRepo.getByTorrentIdAsync(torrentId)`; def TagRepositoryImpl.java:69-70 (`db.tagInfoDao().getByTorrentIdAsync`). |
| 6 | TorrentRepositoryImpl.<clinit> | REACHABLE INFERRED | PASS | Non-constant TAG = `getSimpleName()` at TorrentRepositoryImpl.java:41; first use printed: constructed at RepositoryHelper.java:46-47. <clinit>-on-first-use convention (ix), accepted under D11, as filed. |
| 11 | TorrentRepositoryImpl.deleteTag | REACHABLE SOURCE | PASS | Caller DetailTorrentViewModel.java:156 `repo.deleteTag(torrentId, info)`; def TorrentRepositoryImpl.java:136-138 (`db.torrentDao().deleteTag`). |
| 16 | TorrentRepositoryImpl.getTorrentById | REACHABLE SOURCE | PASS | Callers TorrentEngine.java:767,:840 (and TorrentSessionImpl.java:280,:335,:384 per the file); def TorrentRepositoryImpl.java:71-73 (`db.torrentDao().getTorrentById`). |
| 21 | TorrentRepositoryImpl.updateTorrent | REACHABLE SOURCE | PASS | Caller TorrentEngine.java:1262 `repo.updateTorrent(torrent)`; def TorrentRepositoryImpl.java:61-63 (`db.torrentDao().update`). |
| 26 | FastResumeDao_Impl.getByTorrentId | REACHABLE INFERRED | PASS | Generated implementation of FastResumeDao.getByTorrentId (FastResumeDao.java:17, @Query); via TorrentRepositoryImpl.java:97 (`db.fastResumeDao().getByTorrentId`); upstream caller TorrentSessionImpl.java:1686 `repo.getFastResumeById(id)`. Room dispatch INFERRED, as filed. |
| 27 | FastResumeDao_Impl.getRequiredConverters | REACHABLE INFERRED (Phase 1c D3c flip) | PASS | Under adopted D3c (database-build assumption, extended set, explicitly including 50/27): Room generated _Impl validation calls getRequiredConverters at database build on the printed build AppDatabase.java:81-85 (`Room.databaseBuilder...build()`). Filed REACHABLE INFERRED stands under D3c. No printed app call exists (as the file itself states); the verdict rests on D3c, not on a printed call site. |
| 31 | FeedDao_Impl.<init> | REACHABLE INFERRED | PASS | Generated class (not in the tree, as filed). Constructed when feedDao() (AppDatabase.java:65) is first called; accessor called by every FeedRepositoryImpl method (e.g. FeedRepositoryImpl.java:86,:92). Room dispatch INFERRED, as filed. |
| 36 | FeedDao_Impl.deleteFeeds | REACHABLE INFERRED | PASS | Generated implementation of FeedDao.deleteFeeds (FeedDao.java:64); via FeedRepositoryImpl.java:110 (`db.feedDao().deleteFeeds`); caller FeedViewModel.java:87 `repo.deleteFeeds(feeds)`. Room dispatch INFERRED, as filed. |

## Totals

- Checked: 9. PASS: 9. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: row 27's verdict depends entirely on D3c; if D3c were rejected, row 27 would
  revert to OPEN (per the file's own conditional table), not to UNREACHABLE. This
  spot-check applies D3c as adopted and does not re-decide it.
