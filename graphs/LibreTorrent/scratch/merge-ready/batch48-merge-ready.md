# LibreTorrent batch 48 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 48 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-48 proposal
  (`~/workspace/libretorrent-batch48-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against printed source in this pass, and no prior verdict
  was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 48 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-48 rows are `TODO_CANDIDATE_REACHABLE` in the plan, in plan order.
The table below follows plan order exactly. NOTE: plan order differs from the prior
proposal's order at rows 4–5 — plan row 4 is `AppDatabase.buildDatabase`, plan row 5 is
`AppDatabase.getInstance`; the prior proposal listed them in the opposite order. The
labels are the same for both (REACHABLE SOURCE), but the merger must use plan order here.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b474849-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `core/storage/FeedRepositoryImpl.java` (226 lines, fresh this pass) — `db.feedDao()` calls
  at :86, :92, :98, :104, :110, :116, :122, :128, :134, :140, :170, :176, :182, :188, :194,
  :200, :206, :212, :218, :224. This CLOSES prior OPEN row 11 (see table).
- `core/storage/TagRepositoryImpl.java` (77 lines, fresh this pass) — `db.tagInfoDao()` calls
  at :40, :45, :50, :55, :60, :65, :70, :75; definitions `delete` :49-51, `getByName` :54-56,
  `getByTorrentId` :74-76, matching the prior proposal exactly. This CLOSES prior OPEN
  row 15 (see table).
- `ui/main/MainViewModel.java` (189 lines, fresh this pass) — `setSort` definition :89-95
  (with `sorting.getSorting().getColumnName()` at :91); NO caller of `setSort` appears in
  this file. Row 2 therefore stays OPEN (see table).
- `core/storage/DatabaseMigration.java` (297 lines, fresh this pass) — `getMigrations` :43-55
  returns in order `MIGRATION_1_2` (:57), `MIGRATION_2_3` (:66), `MIGRATION_3_4` (:75),
  `new RoomDatabaseMigration(appContext)` (:49, named class, batch 49), `MIGRATION_5_6` (:83),
  `MIGRATION_6_7` (:92), `MIGRATION_7_8` (:102), `MIGRATION_8_9` (:109).
- No fresh HTTP 429 was hit in this pass. No `search_code` result was used as evidence
  of absence anywhere in this file.

Caller files NOT freshly re-fetched in this pass (prior-session prints, flagged here):
`core/sorting/TorrentSortingComparator.java`, `core/storage/AppDatabase.java`,
`core/RepositoryHelper.java`, `core/model/TorrentEngine.java`,
`core/storage/TorrentRepositoryImpl.java`, `ui/main/MainFragment.java`,
`service/TorrentService.java`. Caller line numbers below are from those prior prints,
consistent with the freshly confirmed definitions; no contradictory fresh evidence
appeared in this pass. `AppDatabase_Impl.java` and `AppDatabase_Impl$1` were NOT printed
(Room-generated code, absent from `final_java_only`, generated at build time) — all
`_Impl` / `_Impl$1` rows below are therefore INFERRED library/generated dispatch, never
SOURCE, and Room's own source was not printed.

## Entry trunk (strict-entry caveat)

- `TorrentEngine` calls `RepositoryHelper.getTorrentRepository` and `getTagRepository` at
  `core/model/TorrentEngine.java:130-131`; `MainViewModel.java:74` calls `getTagRepository`.
- `RepositoryHelper.java:43-47` (`getTorrentRepository`), `:53-56` (`getFeedRepository`),
  `:68-72` (`getTagRepository`) each call `AppDatabase.getInstance(appContext)`.
- `AppDatabase.java:69-79` (`getInstance`, double-checked singleton) calls `buildDatabase`
  (:74); `buildDatabase` :81-86 calls
  `Room.databaseBuilder(appContext, AppDatabase.class, DATABASE_NAME).addMigrations(DatabaseMigration.getMigrations(appContext)).build()`.
- `Room.databaseBuilder(...).build()` is the library entry that creates the generated
  `AppDatabase_Impl` instance (INFERRED — Room source not printed). The launcher →
  TorrentService / MainActivity step was NOT re-printed in this pass; under a strict-entry
  rule these rows revert to OPEN on that point alone.

## Table

`confirmed_by`: SOURCE = a direct app-to-app call site naming the method is printed in
app source; INFERRED = the method is reached only through unprinted framework/library
dispatch (Room-generated dispatch, RxJava `.sorted()` → `Comparator.compare`, JVM class
initialisation) where the registration or first use is printed. This is the per-row
convention, not the whole-route convention used in some earlier batches; labels are
unaffected, only `confirmed_by` would change at merge if the merger adopts the
whole-route convention.

| # | Method | Label | confirmed_by | Printed citation / reason |
|---|---|---|---|---|
| 1 | TorrentSortingComparator.compare(TorrentInfo, TorrentInfo) | REACHABLE | INFERRED | RxJava `.sorted(comparator)` at `MainFragment.java:293` and `:341`, and at `TorrentService.java:287` and `:304` (foreground notify list, comparator from `Utils.getForegroundNotifySorting`). Library `.sorted()` → `Comparator.compare` dispatch is not printed from RxJava source, hence INFERRED, not SOURCE. Definition `TorrentSortingComparator.java:40-45` (delegates to `SortingColumns.fromValue(...).compare(...)`). |
| 2 | TorrentSortingComparator.getSorting() | OPEN | — | Only printed call site is inside `MainViewModel.setSort` at `MainViewModel.java:91` (freshly confirmed: `sorting.getSorting().getColumnName()`), and no printed caller of `setSort` was found in the fetched corpus (sorting-dialog fragment not fetched; fresh `MainViewModel.java` contains no `setSort` caller). Conditional on `setSort`; stays OPEN pending a printed `setSort` caller. |
| 3 | AppDatabase.<init>() | REACHABLE | INFERRED | Abstract-class constructor, invoked by the generated `AppDatabase_Impl.<init>` (row 6) when Room builds the database. Impl source not printed. |
| 4 | AppDatabase.buildDatabase(Context) | REACHABLE | SOURCE | Called at `AppDatabase.java:74` inside `getInstance`. (Plan order: row 4 is `buildDatabase`, row 5 is `getInstance` — see Membership note.) |
| 5 | AppDatabase.getInstance(Context) | REACHABLE | SOURCE | `RepositoryHelper.java:47`, `:56`, `:72`. |
| 6 | AppDatabase_Impl.<init>() | REACHABLE | INFERRED | Room-generated subclass constructor, created by `Room.databaseBuilder(...).build()` at `AppDatabase.java:83-85`. Generated source not in the upload. |
| 7 | AppDatabase_Impl.clearAllTables() | OPEN | — | Room public API; no printed app caller, and Room does not call it during a normal open. Needs full-repo grep. |
| 8 | AppDatabase_Impl.createInvalidationTracker() | REACHABLE | INFERRED | Room framework creates the tracker for observed DAO queries; repositories observe torrents (e.g. `TorrentRepositoryImpl` observe methods call `db.torrentDao().observe...`, :82). Room source not printed, hence INFERRED. Weaker than rows 10/16 — merger should confirm against Room source. |
| 9 | AppDatabase_Impl.createOpenHelper(DatabaseConfiguration) | REACHABLE | INFERRED | Room framework calls this during database build/open to obtain the `RoomOpenHelper` (whose callbacks are rows 17–24). Room source not printed. |
| 10 | AppDatabase_Impl.fastResumeDao() | REACHABLE | INFERRED | Printed app calls to the abstract method at `TorrentRepositoryImpl.java:92` (`db.fastResumeDao().add(...)`) and `:97` (`db.fastResumeDao().getByTorrentId(...)`); virtual dispatch to the Impl override. |
| 11 | AppDatabase_Impl.feedDao() | REACHABLE | INFERRED | **CHANGED from prior proposal's OPEN in this pass.** Freshly printed `FeedRepositoryImpl.java` calls `db.feedDao()` at :86, :92, :98, :104, :110, :116, :122, :128, :134, :140, :170, :176, :182, :188, :194, :200, :206, :212, :218, :224; virtual dispatch to the Impl override. The prior proposal had not fetched `FeedRepositoryImpl.java`; that gap is now closed. |
| 12 | AppDatabase_Impl.getAutoMigrations(Map) | OPEN | — | Room internal; no auto-migrations are declared on `AppDatabase` (`@Database` :42-52 lists entities and version 9 only). No printed Room call. |
| 13 | AppDatabase_Impl.getRequiredAutoMigrationSpecs() | OPEN | — | Room internal; no printed Room call, no auto-migration specs declared. |
| 14 | AppDatabase_Impl.getRequiredTypeConverters() | OPEN | — | Room internal validation of `@TypeConverters({UriConverter.class})` (:53); Room call not printed, so kept OPEN rather than inferred. |
| 15 | AppDatabase_Impl.tagInfoDao() | REACHABLE | INFERRED | **CHANGED from prior proposal's OPEN in this pass.** Freshly printed `TagRepositoryImpl.java` calls `db.tagInfoDao()` at :40, :45, :50, :55, :60, :65, :70, :75; virtual dispatch to the Impl override. The prior proposal had not fetched `TagRepositoryImpl.java`; that gap is now closed. |
| 16 | AppDatabase_Impl.torrentDao() | REACHABLE | INFERRED | Printed app calls to the abstract method at `TorrentRepositoryImpl.java:57`, `:62`, `:67`, `:72`, `:77`, `:82`, `:87`, `:127`, `:132`, `:137`; virtual dispatch to the Impl override. |
| 17 | AppDatabase_Impl$1.<init>(AppDatabase_Impl, int) | REACHABLE | INFERRED | Constructed by generated `createOpenHelper` (row 9) during Room build/open. |
| 18 | AppDatabase_Impl$1.createAllTables(SupportSQLiteDatabase) | REACHABLE | INFERRED | Called by Room's `onCreate` path on first creation (fresh install, the standard configuration). |
| 19 | AppDatabase_Impl$1.dropAllTables(SupportSQLiteDatabase) | OPEN | — | Room calls this only on downgrade / destructive paths; no printed trigger in this pass. Needs Room-source or grep evidence; not claimed. |
| 20 | AppDatabase_Impl$1.onCreate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Room/SQLite first-open callback for a fresh database. |
| 21 | AppDatabase_Impl$1.onOpen(SupportSQLiteDatabase) | REACHABLE | INFERRED | Room/SQLite callback on every database open. |
| 22 | AppDatabase_Impl$1.onPostMigrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Room migration callback, STATE gate: existing database at an older version being upgraded (see rows 27–40). Gate recorded, not decided — see Migration gate note below. |
| 23 | AppDatabase_Impl$1.onPreMigrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Room migration callback, same STATE gate as row 22. |
| 24 | AppDatabase_Impl$1.onValidateSchema(SupportSQLiteDatabase) | REACHABLE | INFERRED | Room schema-validation callback on open. |
| 25 | DatabaseMigration.<clinit> | REACHABLE | INFERRED | JVM class initialisation on first access (via `getMigrations`, row 26); static `MIGRATION_*` fields :57–109 freshly confirmed. |
| 26 | DatabaseMigration.getMigrations(Context) | REACHABLE | SOURCE | Called at `AppDatabase.java:84` inside `buildDatabase`. Definition freshly confirmed :43-55. |
| 27 | DatabaseMigration$1.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(1, 2)` field :57, initialised at `<clinit>` (row 25). |
| 28 | DatabaseMigration$1.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :59-63 (`ALTER TABLE torrents ...`); invoked by Room when upgrading a version-1 database. STATE gate: existing v1 database. Gate recorded, not decided — see below. |
| 29 | DatabaseMigration$2.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(2, 3)` field :66, initialised at `<clinit>`. |
| 30 | DatabaseMigration$2.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :67-72 (creates `feeds` / `feed_items`); Room upgrade from v2. STATE gate: existing v2 database. |
| 31 | DatabaseMigration$3.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(3, 4)` field :75, initialised at `<clinit>`. |
| 32 | DatabaseMigration$3.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :76-80 (`ALTER TABLE torrents ADD COLUMN error`); Room upgrade from v3. STATE gate: existing v3 database. |
| 33 | DatabaseMigration$4.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(5, 6)` field :83, initialised at `<clinit>`. (Note the gap: 4→5 is the named `RoomDatabaseMigration`, batch 49, not a `$` class.) |
| 34 | DatabaseMigration$4.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :84-89 (`ADD COLUMN visibility`); Room upgrade from v5. STATE gate: existing v5 database. |
| 35 | DatabaseMigration$5.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(6, 7)` field :92, initialised at `<clinit>`. |
| 36 | DatabaseMigration$5.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :93-99 (creates `TagInfo` / `TorrentTagInfo` + indexes); Room upgrade from v6. STATE gate: existing v6 database. |
| 37 | DatabaseMigration$6.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(7, 8)` field :102, initialised at `<clinit>`. |
| 38 | DatabaseMigration$6.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :103-106 (`ADD COLUMN sequentialDownload`); Room upgrade from v7. STATE gate: existing v7 database. |
| 39 | DatabaseMigration$7.<init>(int, int) | REACHABLE | INFERRED | Anonymous `Migration(8, 9)` field :109, initialised at `<clinit>`. |
| 40 | DatabaseMigration$7.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Body :110-113 (`ADD COLUMN firstLastPiecePriority`); Room upgrade from v8. STATE gate: existing v8 database. |

## Migration gate note — recorded, NOT decided (applies to rows 22–23 and 28, 30, 32, 34, 36, 38, 40)

Every `$n.migrate` row above, and the `onPreMigrate`/`onPostMigrate` callbacks, rest on a
STATE `data` gate: "existing database at an older version" (app upgrade, not fresh install).
That gate is what makes these reachable despite the fresh-install default: the trigger is
a real, in-app database version, not a hypothetical external condition. **If the project
rule is strictly fresh-install-only, those `migrate` rows and rows 22–23 flip together to
UNREACHABLE** (kind to be decided at merge; the internal chains themselves are printed,
so this is a gate decision, not a missing-caller decision). The `$n.<init>` rows do NOT
flip on that rule: they run at `DatabaseMigration.<clinit>` whenever `getMigrations`
builds the array, fresh install included. Do not merge the `migrate` rows without
resolving this gate question. This file does NOT decide it.

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **34 REACHABLE proposed / 0 UNREACHABLE proposed / 6 OPEN.**
- OPEN rows: 2, 7, 12, 13, 14, 19. Changed from the prior proposal (32/0/8) by the two
  fresh-print closures above (rows 11 and 15, OPEN → REACHABLE INFERRED). No row was
  flipped to UNREACHABLE: no saved full-repo grep was run in this pass, so absence of
  a printed caller was never treated as proof of absence.

## Gaps the merger must close before merging

1. Printed `MainViewModel.setSort` caller (row 2) — the sorting-dialog fragment was not
   fetched in this pass.
2. Printed Room source for `createOpenHelper` / `createInvalidationTracker` / `$1`
   callback dispatch (rows 8, 9, 17–24 are INFERRED on standard Room behaviour, not on
   printed Room lines).
3. Saved full-repo grep for OPEN rows 2, 7, 12, 13, 14, 19 before any OPEN → UNREACHABLE
   judgement.
4. Bytecode confirmation of `$1`–`$7` numbering in `DatabaseMigration$1`–`$7`.
5. Printed launcher → TorrentService / MainActivity step, if the strict-entry rule is
   applied at merge.
6. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
7. Migration gate decision (above) before merging any `migrate` row.

## Strict-entry caveat

No launcher entry was printed in this pass. Under a strict launcher-entry rule all
34 REACHABLE rows above revert to OPEN on that point alone; the in-app chains are printed.
