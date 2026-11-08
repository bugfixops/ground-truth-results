# Spot-check — batch 48 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (2)

- 48/7 AppDatabase_Impl.clearAllTables() — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L5 D31: zero `clearAllTables` hits in all 281 app Java files and all 73 res-layout XML, saved at greps/L5/grep_48_07_clearAllTables.txt; zero in test/androidTest other-sourcesets; Room print shows clearAllTables() as an abstract PUBLIC API with no internal caller in the init/open path printed, so the only possible caller is app code, and app code has none). Stale prose: "stays OPEN IF the merger holds the Room-family caveat that zero app-tree hits alone never flip a Room row (generated dispatch unprinted)". The Phase 3 verdict did not hold that caveat; it flipped the row.
- 48/19 AppDatabase_Impl$1.dropAllTables(SupportSQLiteDatabase) — UNREACHABLE closed_by_configuration INFERRED — PASS. Per L5 D31: zero `dropAllTables`, `fallbackToDestructiveMigration`, `fallbackToDestructiveMigrationOnDowngrade`, `allowDestructiveMigration*`, `onDowngrade` hits in all 281 app Java files + 73 res-layout + test/androidTest (saved at greps/L5/grep_48_19_dropAllTables.txt); printed buildDatabase (AppDatabase.java :81-86) uses .addMigrations(DatabaseMigration.getMigrations(appContext)) only, with NO destructive-migration fallback configured, so the only library path to dropAllTables (downgrade/destructive migration) is closed by this database's configuration. Work prose is conditional framing ("CONDITIONAL, not flipped: flips to UNREACHABLE closed_by_configuration INFERRED IF the merger rules that the printed build configuration … plus the app-tree zero together exclude the downgrade/destructive trigger") — that condition is exactly what the L5 verdict rules, and the prose contains no "stays OPEN" sentence and no present-tense assertion that the row is OPEN; it is therefore PASS, borderline, and recorded here as such so the parent can re-judge the framing if it wishes. Kind and confirmed_by are correct.

## Sample rows (8)

- 48/1 TorrentSortingComparator.compare(TorrentInfo,TorrentInfo) — REACHABLE INFERRED — PASS. RxJava .sorted(comparator) at MainFragment.java:293 and :341, and at TorrentService.java:287 and :304; library .sorted() → Comparator.compare dispatch is not printed from RxJava source, hence INFERRED, not SOURCE.
- 48/6 AppDatabase_Impl.\<init\>() — REACHABLE INFERRED — PASS. Room-generated subclass constructor, created by Room.databaseBuilder(…).build() at AppDatabase.java:83-85; generated source not in the upload.
- 48/11 AppDatabase_Impl.feedDao() — REACHABLE INFERRED — PASS. Changed from prior proposal's OPEN in this pass: freshly printed FeedRepositoryImpl.java calls db.feedDao() at :86, :92, :98, :104, :110, :116, :122, :128, :134, :140, :170, :176, :182, :188, :194, :200, :206, :212, :218, :224; virtual dispatch to the Impl override.
- 48/16 AppDatabase_Impl.torrentDao() — REACHABLE INFERRED — PASS. Printed app calls to the abstract method at TorrentRepositoryImpl.java:57, :62, :67, :72, :77, :82, :87, :127, :132, :137; virtual dispatch to the Impl override.
- 48/21 AppDatabase_Impl$1.onOpen(SupportSQLiteDatabase) — REACHABLE INFERRED — PASS. Room/SQLite callback on every database open (generated callback dispatch, hence INFERRED).
- 48/26 DatabaseMigration.getMigrations(Context) — REACHABLE SOURCE — PASS. Called at AppDatabase.java:84 inside buildDatabase; definition freshly confirmed :43-55.
- 48/31 DatabaseMigration$3.\<init\>(int,int) — REACHABLE INFERRED — PASS. Anonymous Migration(3, 4) field :75, initialised at \<clinit\>.
- 48/36 DatabaseMigration$5.migrate(SupportSQLiteDatabase) — REACHABLE INFERRED — PASS. Body :93-99 (creates TagInfo / TorrentTagInfo + indexes); Room upgrade from v6. STATE gate: existing v6 database (stated in row).

Totals: checked 10 (2 changed + 8 sample-only) — PASS 9, FAIL-prose 1, FAIL-label 0.
