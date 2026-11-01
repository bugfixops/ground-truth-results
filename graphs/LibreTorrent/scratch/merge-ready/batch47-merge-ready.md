# LibreTorrent batch 47 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 47 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-47 proposal
  (`~/workspace/libretorrent-batch47-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-judged against printed source in this pass, and no prior verdict
  was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 47 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-47 rows are `TODO_CANDIDATE_REACHABLE` in the plan, in plan order.
The table below follows plan order exactly; it matches the prior proposal's order.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b474849-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `core/settings/SettingsRepositoryImpl.java` (1,435 lines, fresh this pass) — definitions
  confirmed at the same lines as the prior proposal: `vibrationNotify()` :316-318,
  `vibrationNotify(boolean)` :322-328, `ledIndicatorColorNotify()` :342-344,
  `watchDir()` :773-775, `watchDir(boolean)` :779-785, `watchDirDeleteFile()` :799-801,
  `watchDirDeleteFile(boolean)` :805-811; `Default` field `vibrationNotify` :47,
  `ledIndicatorColorNotify` :53-55, `watchDir` :118, `watchDirDeleteFile` :124.
- `core/sorting/BaseSorting.java` (77 lines, fresh this pass) — `<init>` :52-56,
  `getDirection` :58-61, `getColumnName` :63-66, `toString` :68-76, `Direction` enum :26-40.
- No fresh HTTP 429 was hit in this pass. No `search_code` result was used as evidence
  of absence anywhere in this file.

Caller files NOT freshly re-fetched in this pass (prior-session prints, flagged here so
the merger can re-print them if it wants fresh citations): `core/model/TorrentEngine.java`,
`service/TorrentService.java`, `core/utils/Utils.java`, `ui/main/MainActivity.java`,
`ui/main/MainFragment.java`, `ui/main/MainViewModel.java`, `core/RepositoryHelper.java`,
`ui/settings/SettingsFragment.java`, `core/sorting/TorrentSorting.java`,
`core/sorting/TorrentSortingComparator.java`. Caller line numbers below are from those
prior prints, consistent with the freshly confirmed definitions; no contradictory fresh
evidence appeared in this pass.

## Entry trunk (strict-entry caveat)

Routes below anchor at TorrentEngine / TorrentService / MainActivity / MainViewModel.
The launcher → TorrentService / MainActivity step was NOT re-printed in this pass
(same caveat as batches 19–26). If merge requires a printed launcher step, the
REACHABLE rows below revert to OPEN on that point alone; the in-app chains are printed.
- TorrentEngine obtains the settings repository: `core/model/TorrentEngine.java:133`
  (`pref = RepositoryHelper.getSettingsRepository(appContext)`), and
  `RepositoryHelper.java:60-64` constructs `SettingsRepositoryImpl`.
- TorrentService obtains it: `service/TorrentService.java:108`, `init()` calls
  `makeForegroundNotify()` (:113, :120) and `setFilterAndSorting()` (:138-139).
- Main list sorting: `ui/main/MainViewModel.java:51-52` constructs the default comparator;
  `ui/main/MainFragment.java:293` and `:341` pass `viewModel.getSorting()` to RxJava `.sorted(...)`.

## Table

`confirmed_by`: SOURCE = a direct app-to-app call site naming the method is printed in
app source (including a printed fallback-argument evaluation inside a reachable getter);
INFERRED = the method is reached only through unprinted framework/library dispatch
(JVM class initialisation, anonymous-enum construction, RxJava `.sorted()` →
`Comparator.compare`) where the registration or first use is printed. This is the
per-row convention, not the whole-route convention used in some earlier batches;
labels are unaffected, only `confirmed_by` would change at merge if the merger adopts
the whole-route convention.

| # | Method | Label | confirmed_by | Printed citation / reason |
|---|---|---|---|---|
| 1 | SettingsRepositoryImpl.vibrationNotify() | OPEN | — | Definition :316-318 freshly confirmed. No caller printed in the fetched corpus (prior-session grep of TorrentEngine, TorrentService, Utils, MainActivity/Fragment, SettingsFragment: zero hits). Needs a saved full-repo grep before any UNREACHABLE claim. |
| 2 | SettingsRepositoryImpl.vibrationNotify(boolean) | OPEN | — | Definition :322-328 freshly confirmed (writes `pref_key_vibration_notify`). No printed caller; settings UI is PreferenceFragmentCompat (`SettingsFragment.java`, prior print) which writes SharedPreferences directly, not via this setter. Needs full-repo grep. |
| 3 | SettingsRepositoryImpl.watchDir() | REACHABLE | SOURCE | `TorrentEngine.java:1053`, `:1582`, `:1588` (`if (pref.watchDir())`). Definition :773-775 freshly confirmed. |
| 4 | SettingsRepositoryImpl.watchDir(boolean) | OPEN | — | Definition :779-785 freshly confirmed. No printed caller (same PreferenceFragmentCompat note as row 2). Needs full-repo grep. |
| 5 | SettingsRepositoryImpl.watchDirDeleteFile() | REACHABLE | SOURCE | `TorrentEngine.java:1152` (`if (pref.watchDirDeleteFile())`). Definition :799-801 freshly confirmed. |
| 6 | SettingsRepositoryImpl.watchDirDeleteFile(boolean) | OPEN | — | Definition :805-811 freshly confirmed. No printed caller. Needs full-repo grep. |
| 7 | SettingsRepositoryImpl$Default.<clinit> | REACHABLE | INFERRED | JVM class initialisation on first `Default` access; many reachable getters evaluate `Default` fields/methods (e.g. :318, :331, :344, :645, :710). Nested-class `<clinit>` itself not printed. |
| 8 | SettingsRepositoryImpl$Default.dirToWatch(Context) | REACHABLE | SOURCE | Fallback argument in reachable getter `dirToWatch()` :786-788; getter called at `TorrentEngine.java:1117`. |
| 9 | SettingsRepositoryImpl$Default.encryptInConnectionsMode(Context) | REACHABLE | SOURCE | Fallback in getter :643-645; getter called at `TorrentEngine.java:1109` and inside `readSessionSettings()` :228. |
| 10 | SettingsRepositoryImpl$Default.encryptOutConnectionsMode(Context) | REACHABLE | SOURCE | Fallback in getter :656-658; getter called at `TorrentEngine.java:1113` and inside `readSessionSettings()` :229. |
| 11 | SettingsRepositoryImpl$Default.foregroundNotifySorting(Context) | REACHABLE | SOURCE | Fallback in getter :373-376; getter called at `Utils.java:896` (`getForegroundNotifySorting`), called from `TorrentService.java:139`. |
| 12 | SettingsRepositoryImpl$Default.foregroundNotifyStatusFilter(Context) | REACHABLE | SOURCE | Fallback in getter :355-358; getter called at `Utils.java:877` (`getForegroundNotifyFilter`), called from `TorrentService.java:138`. |
| 13 | SettingsRepositoryImpl$Default.ledIndicatorColorNotify(Context) | OPEN | — | Only printed call site is inside getter :342-344 (freshly confirmed), and that getter (`ledIndicatorColorNotify()`, not itself a batch-47 row) has NO printed caller in the fetched corpus. Conditional on the getter; stays OPEN. Do not flip on the getter definition alone. |
| 14 | SettingsRepositoryImpl$Default.moveAfterDownloadIn(Context) | REACHABLE | SOURCE | Fallback in getter :734-736; getter called at `TorrentEngine.java:1317`. |
| 15 | SettingsRepositoryImpl$Default.saveTorrentFilesIn(Context) | REACHABLE | SOURCE | Fallback in getter :760-762; getter called at `TorrentEngine.java:1275` and `:1432`. |
| 16 | SettingsRepositoryImpl$Default.saveTorrentsIn(Context) | REACHABLE | SOURCE | Fallback in getter :708-710; getter called at `TorrentEngine.java:1185`. |
| 17 | SettingsRepositoryImpl$Default.theme(Context) | REACHABLE | SOURCE | Fallback in getter `theme()` :329-331; getter called at `Utils.java:371` (`getThemePreference`), used by `Utils.getAppTheme` :375, applied at `MainActivity.java:137` (`setTheme(Utils.getAppTheme(...))`). |
| 18 | BaseSorting.<init>(String, Direction) | REACHABLE | SOURCE | Called by `TorrentSorting.<init>` :113-116 (`super(...)`); `TorrentSorting` constructed at `MainViewModel.java:51-52` and throughout `Utils.getForegroundNotifySorting`. BaseSorting definition freshly confirmed. |
| 19 | BaseSorting.getColumnName() | REACHABLE | SOURCE | Called at `TorrentSortingComparator.java:43` (`sorting.getColumnName()`). |
| 20 | BaseSorting.getDirection() | REACHABLE | SOURCE | Called at `TorrentSortingComparator.java:44` (`sorting.getDirection()`). |
| 21 | BaseSorting.toString() | OPEN | — | Definition :68-76 freshly confirmed. No printed caller, log, or concatenation site in the fetched corpus. Needs full-repo grep; do NOT infer from `Object.toString` alone. |
| 22 | BaseSorting$Direction.<clinit> | REACHABLE | INFERRED | JVM enum initialisation on first use of `Direction.ASC`/`DESC`, printed at `MainViewModel.java:51-52` and in every `Utils.getForegroundNotifySorting` construction. |
| 23 | TorrentSorting.<init>(SortingColumns, Direction) | REACHABLE | SOURCE | `MainViewModel.java:51-52` (`new TorrentSorting(SortingColumns.none, Direction.ASC)`); also all `Utils.getForegroundNotifySorting` branches. |
| 24 | TorrentSorting$SortingColumns.<clinit> | REACHABLE | INFERRED | JVM enum initialisation on first use of a `SortingColumns` constant, printed at `MainViewModel.java:51-52` and `Utils.java:892+`. |
| 25 | TorrentSorting$SortingColumns.fromValue(String) | REACHABLE | SOURCE | Called at `TorrentSortingComparator.java:43`. |
| 26 | TorrentSorting$SortingColumns$1.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `none`; instances created at enum `<clinit>` (row 24). Numbering by declaration order, NOT verified against bytecode — merger must confirm. |
| 27 | TorrentSorting$SortingColumns$1.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `none` branch :28-35 returns 0; reached via `Comparator.compare` → `fromValue("none").compare(...)` when column name is `none` (default comparator, `MainViewModel.java:51-52`; `Utils` final branch). Virtual dispatch not printed from library source. |
| 28 | TorrentSorting$SortingColumns$2.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `name`; created at enum `<clinit>`. |
| 29 | TorrentSorting$SortingColumns$2.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `name` branch :36-46; reached via `fromValue("name").compare(...)`; `Utils` name asc/desc branches construct this column. |
| 30 | TorrentSorting$SortingColumns$3.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `size`; created at enum `<clinit>`. |
| 31 | TorrentSorting$SortingColumns$3.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `size` branch :47-57; reached via `fromValue("size").compare(...)`; `Utils` size asc/desc branches. |
| 32 | TorrentSorting$SortingColumns$4.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `progress`; created at enum `<clinit>`. |
| 33 | TorrentSorting$SortingColumns$4.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `progress` branch :58-68; reached via `fromValue("progress").compare(...)`; `Utils` progress asc/desc branches. |
| 34 | TorrentSorting$SortingColumns$5.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `ETA`; created at enum `<clinit>`. |
| 35 | TorrentSorting$SortingColumns$5.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `ETA` branch :69-79; reached via `fromValue("ETA").compare(...)`; `Utils` ETA asc/desc branches. |
| 36 | TorrentSorting$SortingColumns$6.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `peers`; created at enum `<clinit>`. |
| 37 | TorrentSorting$SortingColumns$6.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `peers` branch :80-90; reached via `fromValue("peers").compare(...)`; `Utils` peers asc/desc branches. |
| 38 | TorrentSorting$SortingColumns$7.<init>(String, int) | REACHABLE | INFERRED | Anonymous enum subclass for `dateAdded`; created at enum `<clinit>`. |
| 39 | TorrentSorting$SortingColumns$7.compare(TorrentInfo, TorrentInfo, Direction) | REACHABLE | INFERRED | `dateAdded` branch :91-101; reached via `fromValue("dateAdded").compare(...)`; `Utils` dateAdded asc/desc branches. |
| 40 | TorrentSortingComparator.<init>(TorrentSorting) | REACHABLE | SOURCE | `MainViewModel.java:51-52`; also every `Utils.getForegroundNotifySorting` return. |

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **34 REACHABLE proposed / 0 UNREACHABLE proposed / 6 OPEN.**
- OPEN rows: 1, 2, 4, 6, 13, 21. No row was flipped to UNREACHABLE: no saved full-repo
  grep was run in this pass, so absence of a printed caller was never treated as proof
  of absence.

## Gaps the merger must close before merging

1. Saved full-repo grep (rule F/C5, class-name based) for the 6 OPEN rows — especially
   whether any other file calls the setters, `vibrationNotify()`,
   `ledIndicatorColorNotify()`, or `BaseSorting.toString()`. Only a grep hit flips
   OPEN → REACHABLE; a clean grep is what would justify UNREACHABLE, and that
   judgement belongs to the merger, not this file.
2. Bytecode confirmation of the `$1`–`$7` anonymous-enum numbering.
3. Printed launcher → MainActivity / TorrentService step, if the strict-entry rule is
   applied at merge.
4. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.

## Strict-entry caveat

No launcher entry was printed in this pass. Under a strict launcher-entry rule all
34 REACHABLE rows above revert to OPEN on that point alone; the in-app chains are printed.
