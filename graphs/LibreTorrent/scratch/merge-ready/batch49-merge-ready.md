**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 49 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 49 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-49 proposal
  (`~/workspace/libretorrent-batch49-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against printed source in this pass, and no prior verdict
  was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 49 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-49 rows are `TODO_CANDIDATE_REACHABLE` in the plan, in plan order.
The table below follows plan order exactly; it matches the prior proposal's order.
Groups: `DatabaseMigration$RoomDatabaseMigration` rows 1–10; `FeedRepositoryImpl` rows 11–36;
`TagRepositoryImpl` rows 37–40.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b474849-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `core/storage/DatabaseMigration.java` (297 lines, fresh this pass) — `getMigrations` :43-55
  with `new RoomDatabaseMigration(appContext)` at :49; `RoomDatabaseMigration` class
  :131-136 (`super(4, 5)`), `migrate` :139-177 (creates Room tables :144-151, copies old
  tables :154-163, then `advancedMigration` :172), `advancedMigration` :179-183
  (`removeSessionFile(); copyFastResumeData(database);`).
- `core/storage/FeedRepositoryImpl.java` (226 lines, fresh this pass) — definitions
  confirmed at the same lines as the prior proposal: `<init>` :59-63,
  `getFilterSeparator` :78-81, `addFeed` :84-87, `addFeeds` :90-93, `updateFeed` :96-99,
  `deleteFeed` :102-105, `deleteFeeds` :108-111, `getFeedById` :114-117,
  `getFeedByIdSingle` :120-123, `observeAllFeeds` :126-129, `getAllFeeds` :132-135,
  `getAllFeedsSingle` :138-141, `serializeAllFeeds` :144-148, `deserializeFeeds` :151-165
  (anonymous `TypeToken` at :160), `addItems` :168-171, `deleteItemsOlderThan` :174-177,
  `markAsRead` :180-183, `markAsUnread` :186-189, `markAsReadByFeedId` :192-195,
  `observeItemsByFeedId` :198-201, `getItemsByFeedIdSingle` :204-207,
  `getItemsIdByFeedId` :210-213, `findItemsExistingTitles` :216-219, `getItemsById` :222-224;
  static initialiser material `TAG` :50, `SERIALIZE_FILE_FORMAT` :52,
  `SERIALIZE_MIME_TYPE` :53, `FILTER_SEPARATOR` :54.
- `core/storage/TagRepositoryImpl.java` (77 lines, fresh this pass) — definitions confirmed
  at the same lines as the prior proposal: `<init>` :34-36, `delete` :49-51,
  `getByName` :54-56, `getByTorrentId` :74-76; `db.tagInfoDao()` calls at :40, :45, :50,
  :55, :60, :65, :70, :75.
- No fresh HTTP 429 was hit in this pass. No `search_code` result was used as evidence
  of absence anywhere in this file.

Caller files NOT freshly re-fetched in this pass (prior-session prints, flagged here):
`core/RepositoryHelper.java`, `core/storage/AppDatabase.java`, `core/storage/dao/FeedDao.java`,
`FeedViewModel.java`, `FeedItemsViewModel.java`, `AddFeedViewModel.java`,
`FeedFetcherWorker.java`, `FeedDownloaderWorker.java`, `FeedActivity.java`,
`TorrentEngine.java`, `MainViewModel.java`, `AddTagViewModel.java`,
`DetailTorrentViewModel.java`. Caller line numbers below are from those prior prints,
consistent with the freshly confirmed definitions; no contradictory fresh evidence
appeared in this pass.

## Printed route anchors (shared trunk)

1. **Repository construction.** `RepositoryHelper.java` `getTorrentRepository` :43-47 constructs
   `new TorrentRepositoryImpl(appContext, AppDatabase.getInstance(appContext))`;
   `getFeedRepository` :52-56 constructs `new FeedRepositoryImpl(appContext,
   AppDatabase.getInstance(appContext))`; `getTagRepository` :69-72 constructs
   `new TagRepositoryImpl(AppDatabase.getInstance(appContext))`.
   These getters are called from printed ViewModels/Workers/Engine, e.g.
   `TorrentEngine.java:130-131` (`getTorrentRepository`, `getTagRepository`),
   `FeedViewModel.java:64`, `FeedItemsViewModel.java:59`, `AddFeedViewModel.java:63`,
   `FeedFetcherWorker.java:77`, `FeedDownloaderWorker.java:79`,
   `DetailTorrentViewModel.java:109,114`, `MainViewModel.java:74`,
   `AddTagViewModel.java:42`.
2. **Database construction / migration registration.** `AppDatabase.java` `getInstance` :69-79
   → `buildDatabase` :81-85: `Room.databaseBuilder(...).addMigrations(
   DatabaseMigration.getMigrations(appContext)).build()`.
   `DatabaseMigration.java` `getMigrations` :43-55 (freshly confirmed), :49
   `new RoomDatabaseMigration(appContext)`.
3. **Interface dispatch note.** Repository callers below call the interface
   (`FeedRepository` / `TagRepository`); the concrete object assigned in
   `RepositoryHelper.java` is the `*Impl` in this batch, so virtual dispatch to the Impl
   body is standard Java dispatch to a printed concrete class — not a library dispatch.
   Rows are therefore marked SOURCE where both the caller line and the Impl body are printed.
   (Contrast: Room-generated dispatch in batch 50 is marked INFERRED.)
4. **Strict-entry caveat.** Routes anchor at ViewModels / Workers / TorrentEngine, not at
   a launcher entry printed in this pass. Who launches the feed/tag UI or enqueues the
   feed workers was not re-printed here, so under a strict launcher-entry rule these rows
   would be OPEN. This does not change the proposed counts, following the batch 22/23 precedent.

## Migration gate note — recorded, NOT decided (applies to rows 2–10)

`DatabaseMigration.java` `RoomDatabaseMigration` is `Migration(4, 5)` (freshly confirmed
:131-136, `super(4, 5)`). Room invokes `migrate()` only when opening a database whose
stored version is 4 (stepping 4→5 toward the current version 9, `AppDatabase.java:51`).
On a **fresh install** Room creates version 9 directly and `migrate()` never runs.
The verdicts for rows 2–10 therefore rest on a STATE `data` gate — "a pre-existing
version-4 database is present at first DB open" — with Room dispatch to `migrate`
INFERRED (Room source not printed). **If the project rule is strictly fresh-install-only,
rows 2–10 flip together to UNREACHABLE** (kind to be decided at merge; the internal
chain itself is printed, so this is a gate decision, not a missing-caller decision).
Row 1 (`<init>`) does NOT flip: it runs whenever `getMigrations` builds the array,
fresh install included. Do not merge rows 2–10 without resolving this gate question.
This file does NOT decide it. The same gate question applies to batch 48's `$n.migrate`
rows; the two batches must be decided consistently.

## Table

`confirmed_by`: SOURCE = a direct app-to-app call site naming the method is printed in
app source (including a printed internal call site where the calling method is itself
SOURCE-anchored); INFERRED = the method is reached only through unprinted
framework/library dispatch (Room invoking a registered `Migration`, JVM class
initialisation, javac anonymous-class construction) where the registration or first use
is printed. This is the per-row convention, not the whole-route convention used in some
earlier batches; labels are unaffected, only `confirmed_by` would change at merge if the
merger adopts the whole-route convention.

| # | Method | Label | confirmed_by | Route / citation |
|---|---|---|---|---|
| 1 | DatabaseMigration$RoomDatabaseMigration.<init>(Context) | REACHABLE | SOURCE | Def `DatabaseMigration.java:131-136` (fresh). Constructed at `DatabaseMigration.java:49` in `getMigrations`, called from `AppDatabase.java:84` in `buildDatabase`, via `getInstance` (`AppDatabase.java:69-79`) via `RepositoryHelper.java:47,56,72`. Fresh-install-safe — does NOT flip under a fresh-install-only rule. |
| 2 | DatabaseMigration$RoomDatabaseMigration.addFastResume(SupportSQLiteDatabase, String, byte[]) | REACHABLE | SOURCE | Def `DatabaseMigration.java:290-295`. Called at `DatabaseMigration.java:206-208` inside `copyFastResumeData`, inside the row-8 chain below. GATE: pre-existing v4 DB (see gate note); Room dispatch to `migrate` INFERRED. Flips if fresh-install-only. |
| 3 | DatabaseMigration$RoomDatabaseMigration.advancedMigration(SupportSQLiteDatabase) | REACHABLE | SOURCE | Def `DatabaseMigration.java:179-183` (fresh: `removeSessionFile(); copyFastResumeData(database);`). Called at `DatabaseMigration.java:172` inside `migrate` (try block, :171-176). GATE as row 2. Flips if fresh-install-only. |
| 4 | DatabaseMigration$RoomDatabaseMigration.backupTorrent(File) | REACHABLE | SOURCE | Def `DatabaseMigration.java:259-275`. Called at `DatabaseMigration.java:202` (no fast-resume file) and `:211` (exception path) inside `copyFastResumeData`. GATE as row 2. Flips if fresh-install-only. |
| 5 | DatabaseMigration$RoomDatabaseMigration.copyFastResumeData(SupportSQLiteDatabase) | REACHABLE | SOURCE | Def `DatabaseMigration.java:185-227`. Called at `DatabaseMigration.java:182` from `advancedMigration`. GATE as row 2. Flips if fresh-install-only. |
| 6 | DatabaseMigration$RoomDatabaseMigration.findTorrentDataDir(String) | REACHABLE | SOURCE | Def `DatabaseMigration.java:246-257`. Called at `DatabaseMigration.java:195` inside `copyFastResumeData`, guarded by `torrentDataExists` at `:192`. GATE as row 2. Flips if fresh-install-only. |
| 7 | DatabaseMigration$RoomDatabaseMigration.getTorrentIdList(SupportSQLiteDatabase) | REACHABLE | SOURCE | Def `DatabaseMigration.java:277-288` (query `SELECT id from Torrent`, :281). Called at `DatabaseMigration.java:187` at the top of `copyFastResumeData`. GATE as row 2. Flips if fresh-install-only. |
| 8 | DatabaseMigration$RoomDatabaseMigration.migrate(SupportSQLiteDatabase) | REACHABLE | INFERRED | Def `DatabaseMigration.java:139-177` (fresh: creates Room tables :144-151, copies old tables :154-163, then `advancedMigration` :172). No app call site: Room framework invokes a registered `Migration` on version step 4→5; registration printed (`AppDatabase.java:84`, `DatabaseMigration.java:49`). GATE: pre-existing v4 DB; flips with rows 2–10 if fresh-install-only. |
| 9 | DatabaseMigration$RoomDatabaseMigration.removeSessionFile() | REACHABLE | SOURCE | Def `DatabaseMigration.java:229-236`. Called at `DatabaseMigration.java:181` from `advancedMigration`. GATE as row 2. Flips if fresh-install-only. |
| 10 | DatabaseMigration$RoomDatabaseMigration.torrentDataExists(String) | REACHABLE | SOURCE | Def `DatabaseMigration.java:238-244`. Called at `DatabaseMigration.java:192` inside `copyFastResumeData` loop. GATE as row 2. Flips if fresh-install-only. |
| 11 | FeedRepositoryImpl.<clinit> | REACHABLE | INFERRED | No source def (JVM static initialiser for `TAG` :50 and constants :52-54, freshly confirmed). Runs on first use of the class; class is constructed at `RepositoryHelper.java:55-56` and its constants are read at `FeedActivity.java:271-272,286` (`SERIALIZE_FILE_FORMAT`, `SERIALIZE_MIME_TYPE`). |
| 12 | FeedRepositoryImpl.<init>(Context, AppDatabase) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:59-63` (fresh). Constructed at `RepositoryHelper.java:55-56`, called via `getFeedRepository` from `FeedViewModel.java:64`, `FeedFetcherWorker.java:77`, `FeedDownloaderWorker.java:79`, etc. |
| 13 | FeedRepositoryImpl.addFeed(FeedChannel) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:84-87` (fresh, `db.feedDao().addFeed`). Caller `AddFeedViewModel.java:189` (`repo.addFeed(channel)`). |
| 14 | FeedRepositoryImpl.addFeeds(List) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:90-93` (fresh). Caller `FeedViewModel.java:144` (`repo.addFeeds(feeds)`). |
| 15 | FeedRepositoryImpl.addItems(List) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:168-171` (fresh). Caller `FeedFetcherWorker.java:172` (`repo.addItems(items)`). |
| 16 | FeedRepositoryImpl.deleteFeed(FeedChannel) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:102-105` (fresh). Caller `AddFeedViewModel.java:133` (`repo.deleteFeed(channel)`). |
| 17 | FeedRepositoryImpl.deleteFeeds(List) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:108-111` (fresh). Caller `FeedViewModel.java:87` (`repo.deleteFeeds(feeds)`). |
| 18 | FeedRepositoryImpl.deleteItemsOlderThan(long) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:174-177` (fresh). Caller `FeedFetcherWorker.java:209` (`repo.deleteItemsOlderThan(keepDateBorderTime)`). |
| 19 | FeedRepositoryImpl.deserializeFeeds(Uri) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:151-165` (fresh; Gson parse, anonymous `TypeToken` at :160 — see row 36). Caller `FeedViewModel.java:142` (`repo.deserializeFeeds(file)`). |
| 20 | FeedRepositoryImpl.findItemsExistingTitles(List) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:216-219` (fresh). Caller `FeedFetcherWorker.java:202` (`repo.findItemsExistingTitles(titles)`). |
| 21 | FeedRepositoryImpl.getAllFeeds() | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:132-135` (fresh). Caller `FeedFetcherWorker.java:100` (`repo.getAllFeeds()`). |
| 22 | FeedRepositoryImpl.getAllFeedsSingle() | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:138-141` (fresh). Caller `FeedViewModel.java:77` (`repo.getAllFeedsSingle()`). |
| 23 | FeedRepositoryImpl.getFeedById(long) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:114-117` (fresh). Callers `AddFeedViewModel.java:131` and `FeedFetcherWorker.java:150`. |
| 24 | FeedRepositoryImpl.getFeedByIdSingle(long) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:120-123` (fresh). Caller `AddFeedViewModel.java:151` (`repo.getFeedByIdSingle(feedId)`). |
| 25 | FeedRepositoryImpl.getFilterSeparator() | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:78-81` (fresh, returns `FILTER_SEPARATOR` :54). Caller `FeedFetcherWorker.java:261` (`filter.split(repo.getFilterSeparator())`). |
| 26 | FeedRepositoryImpl.getItemsByFeedIdSingle(long) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:204-207` (fresh). Caller `FeedItemsViewModel.java:89` (`repo.getItemsByFeedIdSingle(feedId)`). |
| 27 | FeedRepositoryImpl.getItemsById(String...) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:222-224` (fresh, `db.feedDao().getItemsById`). Caller `FeedDownloaderWorker.java:100` (`repo.getItemsById(ids)`). |
| 28 | FeedRepositoryImpl.getItemsIdByFeedId(long) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:210-213` (fresh). Caller `FeedFetcherWorker.java:191` (`repo.getItemsIdByFeedId(id)`). |
| 29 | FeedRepositoryImpl.markAsRead(String) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:180-183` (fresh). Callers `FeedFetcherWorker.java:221` and `FeedItemsViewModel.java:124`. |
| 30 | FeedRepositoryImpl.markAsReadByFeedId(List) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:192-195` (fresh). Callers `FeedItemsViewModel.java:118` and `FeedViewModel.java:149`. |
| 31 | FeedRepositoryImpl.markAsUnread(String) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:186-189` (fresh). Caller `FeedItemsViewModel.java:131` (`repo.markAsUnread(itemId)`). |
| 32 | FeedRepositoryImpl.observeAllFeeds() | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:126-129` (fresh). Caller `FeedViewModel.java:82` (`repo.observeAllFeeds()`). |
| 33 | FeedRepositoryImpl.observeItemsByFeedId(long) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:198-201` (fresh). Caller `FeedItemsViewModel.java:84` (`repo.observeItemsByFeedId(feedId)`). |
| 34 | FeedRepositoryImpl.serializeAllFeeds(Uri) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:144-148` (fresh, via `getAllFeeds()` :147). Caller `FeedViewModel.java:137` (`repo.serializeAllFeeds(file)`). |
| 35 | FeedRepositoryImpl.updateFeed(FeedChannel) | REACHABLE | SOURCE | Def `FeedRepositoryImpl.java:96-99` (fresh). Callers `AddFeedViewModel.java:190`, `FeedFetcherWorker.java:160,181`. |
| 36 | FeedRepositoryImpl$1.<init>(FeedRepositoryImpl) | REACHABLE | INFERRED | No source def: synthetic anonymous subclass of `TypeToken<ArrayList<FeedChannel>>` created at `FeedRepositoryImpl.java:160` (fresh) inside `deserializeFeeds` (row 19). Its constructor runs whenever row 19 runs; the `$1` numbering is the javac anonymous-class numbering, INFERRED, not printed from bytecode — merger must confirm against bytecode if disputed. |
| 37 | TagRepositoryImpl.<init>(AppDatabase) | REACHABLE | SOURCE | Def `TagRepositoryImpl.java:34-36` (fresh). Constructed at `RepositoryHelper.java:72`, called via `getTagRepository` from `TorrentEngine.java:131`, `DetailTorrentViewModel.java:114`, `MainViewModel.java:74`, `AddTagViewModel.java:42`. |
| 38 | TagRepositoryImpl.delete(TagInfo) | REACHABLE | SOURCE | Def `TagRepositoryImpl.java:49-51` (fresh, `db.tagInfoDao().delete`). Caller `MainViewModel.java:187` (`tagRepo.delete(info)`). |
| 39 | TagRepositoryImpl.getByName(String) | REACHABLE | SOURCE | Def `TagRepositoryImpl.java:54-56` (fresh). Caller `AddTagViewModel.java:65` (`tagRepo.getByName(info.name)`). |
| 40 | TagRepositoryImpl.getByTorrentId(String) | REACHABLE | SOURCE | Def `TagRepositoryImpl.java:74-76` (fresh, `db.tagInfoDao().getByTorrentId`). Callers `TorrentEngine.java:771,821` (`tagRepo.getByTorrentId(id)` / `(torrent.id)`). |

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN.**
- confirmed_by: SOURCE 37, INFERRED 3 (rows 8, 11, 36).
- No UNREACHABLE verdict is claimed for any row: no saved full-repo grep was run
  (no full checkout in this VM), so absence of a printed caller was never treated
  as proof of absence — and in fact every row has a printed caller above.
- Not claimed: build, sampler, grep, C1. No `graph_def.py` / `out/` change.
- Merger must resolve the migration gate question above before merging rows 2–10,
  and must confirm the `$1` anonymous-class numbering against bytecode if disputed.

## Gaps the merger must close before merging

1. Migration gate decision (above) — rows 2–10 flip together to UNREACHABLE if the
   project rule is strictly fresh-install-only; row 1 does not flip. Decide
   consistently with batch 48's `$n.migrate` rows.
2. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
3. Printed launcher → ViewModel/Worker entry step, if the strict-entry rule is applied
   at merge (all 40 rows revert to OPEN on that point alone under a strict rule).
4. Bytecode confirmation of row 36's `$1` numbering if disputed.

## Strict-entry caveat

No launcher entry was printed in this pass. Under a strict launcher-entry rule all
40 REACHABLE rows above revert to OPEN on that point alone; the in-app chains are printed.
