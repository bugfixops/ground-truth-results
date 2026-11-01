# Batch 51 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch51-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b505152-openclose-src/`, `~/workspace/b505152-src/`,
  `~/workspace/overnight/stream-A/corpus/`). No connector fetch was needed; no 429; no missing file.
- Rows checked (10): sample 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1c flips 18, 24 (row 6 is both sample and flip).
- Batch Counts verified mechanically from the label column: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN — matches the Phase 1c header.
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `FeedDao_Impl.getFeedById` | REACHABLE INFERRED | PASS | FeedDao.java:67 `getFeedById`; FeedRepositoryImpl.java:116 `db.feedDao().getFeedById(id)`; AddFeedViewModel.java:131 `repo.getFeedById(feedId)`. Generated dispatch unprinted, so INFERRED is correct. |
| 6 `FeedDao_Impl.getRequiredConverters` | REACHABLE INFERRED | PASS* | Label matches the Phase 1c application of DECISIONS.md D3c (database-build assumption, extended set). AppDatabase.java:69-79 `getInstance`, :81-87 `buildDatabase` (Room.databaseBuilder…build()), abstract DAO getters :61-67; no `getRequiredConverters` declaration in any DAO print. *Conditional on D3c standing; this spot-check does not decide the convention. Text note: the row body still contains the pre-flip sentence "stays OPEN" alongside the [APPLIED D3c] tag — label is correct, rationale text needs cleanup by the coordinator (no label change). |
| 11 `FeedDao_Impl.observeItemsByFeedId` | REACHABLE INFERRED | PASS | FeedDao.java:97; FeedRepositoryImpl.java:200; FeedItemsViewModel.java:84 `repo.observeItemsByFeedId(feedId)`. INFERRED correct (Room dispatch unprinted). |
| 16 `FeedDao_Impl$10.<init>` | REACHABLE INFERRED | PASS | SET membership holds: the four List-returning Rx methods are all called via the repository — observeAllFeeds :128, getAllFeedsSingle :140, observeItemsByFeedId :200, getItemsByFeedIdSingle :206 (FeedDao :73, :79, :97, :100). Individual $10 identity is expressly not claimed. Revert-at-risk under STRICT noted in the file, not decided here. |
| 18 `FeedDao_Impl$10.finalize` | REACHABLE INFERRED | PASS* | Enclosing Callable (row 16) verified REACHABLE above; label matches Phase 1c D3b (finalize-as-GC-route F1). *Conditional on D3b standing. Pre-flip "Needs a project rule" sentence remains in the body alongside the [APPLIED D3b] tag — text cleanup only. |
| 21 `FeedDao_Impl$11.finalize` | REACHABLE INFERRED | PASS* | Same as row 18; enclosing Callable row 19 is a $10-$12 set member per the repository lines above. *Conditional on D3b. Same stale-sentence text note. |
| 24 `FeedDao_Impl$12.finalize` | REACHABLE INFERRED | PASS* | Same as row 18; enclosing Callable row 22 is a set member per the repository lines above. *Conditional on D3b. Same stale-sentence text note. |
| 26 `FeedDao_Impl$2.bind` | REACHABLE INFERRED | PASS | FeedItem bind adapter for addItems: FeedDao.java:82 `addItems`, FeedRepositoryImpl.java:170 `db.feedDao().addItems(items)`. SET treatment (row 25 route); individual $ identity not claimed. |
| 31 `FeedDao_Impl$4.<init>` | REACHABLE INFERRED | PASS | Update-or-deletion adapter for FeedChannel: updateFeed FeedDao:58 / repository :98, deleteFeed :61 / :104, deleteFeeds :64 / :110 — both operations called, so the adapter runs whichever it serves. |
| 36 `FeedDao_Impl$6.<init>` | REACHABLE INFERRED | PASS | SharedSQLiteStatement set: deleteItemsOlderThan FeedDao:85 / repository :176, markAsRead :88 / :182, markAsUnread :91 / :188 — all three called. |

## Totals

- PASS: 10, FAIL: 0 (of 10 checked).
- Proposed corrections: none to any label. Text cleanups only: delete the superseded "stays OPEN" sentence in row 6 and the "Needs a project rule" sentences in rows 18, 21, 24 (the [APPLIED D3b/D3c] tags already record the flips).
