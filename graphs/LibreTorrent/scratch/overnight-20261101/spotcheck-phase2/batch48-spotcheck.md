# LibreTorrent batch 48 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch48-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only — the 281-file
  corpus in `~/workspace/overnight/stream-A/corpus/java/`, `~/workspace/b505152-src/AppDatabase.java`,
  `~/workspace/b474849-src/` repositories, and `~/workspace/b444748-openclose-src/MainViewModel.java`
  / `MainActivity.java`. No connector fetch was needed; no merge-ready file was edited;
  no label was flipped.
- Rows checked (14): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase 1c flip row 14, Phase 1
  open-close row 2, plus must-include OPEN rows 7, 12, 13, 19.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentSortingComparator.compare | REACHABLE INFERRED | PASS | Def TorrentSortingComparator.java:40-45 (delegates to SortingColumns.fromValue(...).compare(...)); RxJava `.sorted(comparator)` at MainFragment.java:293,:341 and TorrentService.java:287,:304 per the file (library dispatch, hence INFERRED). Comparator body itself verified in corpus at :40-45. |
| 2 | TorrentSortingComparator.getSorting() | REACHABLE SOURCE (Phase 1 open-close flip) | PASS | MainViewModel.java:91 (setSort, force branch) `sorting.getSorting().getColumnName()`; called from MainActivity.java:619 `viewModel.setSort(..., true)` (drawer callback registered :250). The :594 setSort(..., false) call does not call getSorting, as filed. Def TorrentSortingComparator.java:35. |
| 6 | AppDatabase_Impl.<init> | REACHABLE INFERRED | PASS | Generated class (not in the tree, as filed). Created by `Room.databaseBuilder(...).build()` at AppDatabase.java:81-85 (buildDatabase, called from getInstance :69-79). INFERRED generated dispatch, as filed. |
| 7 | AppDatabase_Impl.clearAllTables() | OPEN — MUST-INCLUDE, left OPEN under D3c | PASS (OPEN stands, not flipped) | Corpus-wide grep: zero `clearAllTables` hits tree-wide; normal open path (AppDatabase.java:81-85, databaseBuilder + addMigrations + build) does not call it. D3c explicitly does not flip this row. Left OPEN as filed; an app-tree zero alone does not close a generated-dispatch row. |
| 11 | AppDatabase_Impl.feedDao() | REACHABLE INFERRED | PASS | FeedRepositoryImpl.java calls `db.feedDao()` at :86,:92,:98,:104,:110,:116,:122,:128,:134,:140,:170,:176,:182,:188,:194,:200,:206,:212,:218,:224 (b474849-src copy, first eight verified directly); virtual dispatch to the Impl override, hence INFERRED. |
| 12 | AppDatabase_Impl.getAutoMigrations(Map) | OPEN — MUST-INCLUDE, left OPEN under D3c | PASS (OPEN stands, not flipped) | AppDatabase.java:42-52 declares entities + version 9 only, no auto-migrations; corpus grep: zero `@AutoMigration` / `getAutoMigrations` hits. D3c explicitly does not flip this row (no declared auto-migration to validate). Left OPEN as filed. |
| 13 | AppDatabase_Impl.getRequiredAutoMigrationSpecs() | OPEN — MUST-INCLUDE, left OPEN under D3c | PASS (OPEN stands, not flipped) | Same evidence as row 12: no auto-migration specs declared, corpus grep zero hits. D3c explicitly does not flip this row. Left OPEN as filed. |
| 14 | AppDatabase_Impl.getRequiredTypeConverters() | REACHABLE INFERRED (Phase 1c D3c flip) | PASS | Under adopted D3c (database-build assumption, extended set, explicitly including 48/14): Room generated _Impl validation calls getRequiredTypeConverters at database build on the printed build AppDatabase.java:81-85, validating the printed `@TypeConverters({UriConverter.class})` at AppDatabase.java:53. Filed REACHABLE INFERRED stands under D3c. |
| 16 | AppDatabase_Impl.torrentDao() | REACHABLE INFERRED | PASS | TorrentRepositoryImpl.java calls `db.torrentDao()` at :57,:62,:67,:72,:77,:82,:87,:127,:132,:137 (corpus); virtual dispatch to the Impl override, hence INFERRED. |
| 19 | AppDatabase_Impl$1.dropAllTables() | OPEN — MUST-INCLUDE, left OPEN under D3c | PASS (OPEN stands, not flipped) | Corpus grep: zero `dropAllTables`, `fallbackToDestructiveMigration`, `onDowngrade` hits; buildDatabase :81-85 uses addMigrations only, no destructive fallback. D3c explicitly does not flip this row. Left OPEN as filed; the generated $1 dispatch is unprinted. |
| 21 | AppDatabase_Impl$1.onOpen | REACHABLE INFERRED | PASS | Room/SQLite callback on every database open, per the file's disclosed Room-behaviour basis (generated source unprinted, hence INFERRED, not SOURCE). No contrary printed evidence found; label passes on the same convention as the sibling $1 rows. |
| 26 | DatabaseMigration.getMigrations(Context) | REACHABLE SOURCE | PASS | Called at AppDatabase.java:84 inside buildDatabase (`addMigrations(DatabaseMigration.getMigrations(appContext))`). Def DatabaseMigration.java:43-55. |
| 31 | DatabaseMigration$3.<init> | REACHABLE INFERRED | PASS | Anonymous Migration(3, 4) field DatabaseMigration.java:75, initialised at <clinit> (row 25). |
| 36 | DatabaseMigration$5.migrate | REACHABLE INFERRED | PASS | Migration(6, 7) body DatabaseMigration.java:93-99 (creates TagInfo / TorrentTagInfo + indexes); Room upgrade from v6. STATE-gate caveat carried from the file (existing v6 database, not fresh install) — the gate question is recorded, not decided, by this spot-check; the internal chain re-derives as filed. |

## Totals

- Checked: 14. PASS: 14. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Note: rows 7, 12, 13, 19 are counted as PASS only in the sense that "OPEN as filed"
  re-derives; they are not closed by this spot-check, and D3c's explicit non-flip list
  (48/7, 48/12, 48/13, 48/19) was respected.
