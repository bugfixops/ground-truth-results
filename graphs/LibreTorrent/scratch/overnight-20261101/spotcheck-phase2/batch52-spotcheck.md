# Batch 52 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch52-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b505152-openclose-src/`, `~/workspace/b505152-src/`,
  `~/workspace/ruleF-src/`). No connector fetch was needed; no 429; no missing file.
- Rows checked (13): sample 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1c flips 2, 5, 27, 30, 33 (row 11 is both sample and flip).
- Batch Counts verified mechanically from the label column: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN — matches the Phase 1c header.
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `FeedDao_Impl$8.call` | REACHABLE INFERRED | PASS | Pinned, not merely set-assigned: `getFeedByIdSingle` (FeedDao.java:70) is the only Rx method returning a single FeedChannel; FeedRepositoryImpl.java:122; AddFeedViewModel.java:151. Rx subscription unprinted, so INFERRED is correct. |
| 2 `FeedDao_Impl$8.finalize` | REACHABLE INFERRED | PASS* | Enclosing Callable batch-51 row 40 (pinned $8) verified REACHABLE; label matches Phase 1c D3b. *Conditional on D3b standing. Pre-flip "Needs a project rule" sentence remains alongside the [APPLIED D3b] tag — text cleanup only. |
| 5 `FeedDao_Impl$9.finalize` | REACHABLE INFERRED | PASS* | Enclosing Callable row 3 is a List-Rx set member (repository :128, :140, :200, :206). *Conditional on D3b. Same stale-sentence text note. |
| 6 `TagInfoDao_Impl.<init>` | REACHABLE INFERRED | PASS | AppDatabase.java:67 `tagInfoDao()`; TagRepositoryImpl.java:40, :45, :50, :55, :60, :65, :70, :75 all call `db.tagInfoDao()`. Generated dispatch unprinted, so INFERRED is correct. |
| 11 `TagInfoDao_Impl.getRequiredConverters` | REACHABLE INFERRED | PASS* | Label matches Phase 1c D3c, same AppDatabase build print as batch 51 row 6 (buildDatabase :81-87). *Conditional on D3c standing. Same stale "stays OPEN" sentence text note. |
| 16 `TagInfoDao_Impl$1.<init>` | REACHABLE INFERRED | PASS | Insertion adapter for TagInfo: TagInfoDao.java:39 `insert`; TagRepositoryImpl.java:40; AddTagViewModel.java:69 `tagRepo.insert(info)`. |
| 21 `TagInfoDao_Impl$2.createQuery` | REACHABLE INFERRED | PASS | Either DELETE or UPDATE adapter: delete TagRepositoryImpl.java:50, update :45 — both called, so createQuery runs whichever adapter $2 is. |
| 26 `TagInfoDao_Impl$4.call` | REACHABLE INFERRED | PASS | Row 25's List-Rx method is called via TagRepositoryImpl (observeAll :60, observeByTorrentId :65, getByTorrentIdAsync :70); Rx subscription unprinted, so INFERRED is correct. |
| 27 `TagInfoDao_Impl$4.finalize` | REACHABLE INFERRED | PASS* | Enclosing Callable row 25, set member per row 26 evidence. *Conditional on D3b. Same stale-sentence text note. |
| 30 `TagInfoDao_Impl$5.finalize` | REACHABLE INFERRED | PASS* | Enclosing Callable row 28, set member per TagRepositoryImpl :60/:65/:70. *Conditional on D3b. Same stale-sentence text note. |
| 31 `TagInfoDao_Impl$6.<init>` | REACHABLE INFERRED | PASS | Callable for a List-Rx query; TagRepositoryImpl.java:70 `getByTorrentIdAsync`, caller DetailTorrentViewModel.java:144. Under any set assignment its method is called. |
| 33 `TagInfoDao_Impl$6.finalize` | REACHABLE INFERRED | PASS* | Enclosing Callable row 31 verified above. *Conditional on D3b. Same stale-sentence text note. |
| 36 `TorrentDao_Impl.<init>` | REACHABLE INFERRED | PASS | `torrentDao()` called throughout TorrentRepositoryImpl (verified :57, :62, :67, :72, :77, :82, :87, :127, :132, :137). Generated source unprinted, so INFERRED is correct. |

## Totals

- PASS: 13, FAIL: 0 (of 13 checked).
- Proposed corrections: none to any label. Text cleanups only: superseded "stays OPEN" / "Needs a project rule" sentences in rows 2, 5, 11, 27, 30, 33.
