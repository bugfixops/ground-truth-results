**GREP-FLIP RE-CHECK 2026-11-01 (Stream A Phase 1): rows 1, 2, 13 SURVIVED — labels unchanged, still UNREACHABLE closed_by_api_level INFERRED. Re-checked against the COMPLETE tree enumerated via the GitHub connector: 281 Java files (252 org.proninyaroslav.libretorrent + 28 com.ernieyu.feedparser + 1 org.nanohttpd.NanoHTTPD) plus 73 layout XML files (69 res/layout + 2 layout-large-land-notouch + 2 layout-sw600dp-land). New greps: `~/workspace/overnight/stream-A/greps/recheck-47-56-57_local252.txt` (252-file re-run) and `~/workspace/overnight/stream-A/greps/recheck-47-56-57_complete-tree-plus-xml.txt` (101 freshly fetched files: 28 feedparser + 1 nanohttpd + 73 XML, zero target-pattern hits in every one). No ungated caller of vibrationNotify(), vibrationNotify(boolean), or ledIndicatorColorNotify() (getter or Default(Context) overload) exists in the complete tree or XML; the gates re-verified are AppearanceSettingsFragment :118-119 (SDK < O, false at API 27) for initLegacyNotifySettings and TorrentNotifier :276 (SDK >= O early return, true at API 27) for applyLegacyNotifySettings. Row 13 still flips together with batch 44 row 17 (not edited here). No other row changed. Counts mechanically verified, unchanged: 40 rows, 36 REACHABLE / 3 UNREACHABLE / 1 OPEN. Build: not run. C1: not run. No push.**

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**OPEN-CLOSE REVISION 2026-11-01 (round 2, G6): rows 1, 2, 13 OPEN -> UNREACHABLE closed_by_api_level INFERRED on the saved full-tree grep now on file (see below); row 21 stays OPEN (implicit-toString caveat, see its conditional table). Counts 36/0/4 -> 36/3/1. No row flipped to REACHABLE. Build: not run. C1: not run. Fresh source for this pass: saved grep `~/workspace/b414748-openclose2-src/full_tree_grep_414748.txt` §§A-C,J over all 252 app Java files in `~/workspace/ruleF-src/` (connector-reconstructed tree, 252/252 .java at grep time); gate lines re-checked in that tree (AppearanceSettingsFragment gate :118-119, TorrentNotifier early return :276). No GitHub connector fetch was needed in this pass (all target files already present locally); no fresh 429. Original file backed up at `~/workspace/libretorrent-merge-backup-pre-openclose2/batch47-merge-ready.md` before this edit.**

**OPEN-CLOSE REVISION 2026-11-01: rows 4 and 6 OPEN -> REACHABLE SOURCE on freshly printed StorageSettingsFragment.java (296 lines, SHA 213e8440…, onPreferenceChange :281/:287, ungated onCreate bindings :170/:197). Rows 1, 2, 13 stay OPEN with a closed_by_api_level LEAD recorded (not flipped — no saved full-repo grep); row 21 stays OPEN, no printed caller. Counts 34/0/6 -> 36/0/4. No row flipped to UNREACHABLE. Build: not run. C1: not run. Fresh source in ~/workspace/b444748-openclose-src/.**

# LibreTorrent batch 47 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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
| 1 | SettingsRepositoryImpl.vibrationNotify() | UNREACHABLE closed_by_api_level | INFERRED | Definition :316-318 freshly confirmed. Saved full-tree grep §A (252 app Java files, `~/workspace/b414748-openclose2-src/full_tree_grep_414748.txt`): the ONLY call statements are GATED — AppearanceSettingsFragment.java:187 inside initLegacyNotifySettings (gate :118-119, SDK < O, false at API 27) and TorrentNotifier.java:286 inside applyLegacyNotifySettings (early return :276 at SDK >= O, before :286). At API 27 neither statement executes. Method-vs-branch rule applied exactly as in batches 44/45/46/73-74: the gate is on the call sites, not merely in this getter's body. CHANGED 2026-11-01 round 2 OPEN -> UNREACHABLE. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED, no new caller. Flips back to REACHABLE on any printed ungated caller. |
| 2 | SettingsRepositoryImpl.vibrationNotify(boolean) | UNREACHABLE closed_by_api_level | INFERRED | Definition :322-328 freshly confirmed. Saved full-tree grep §A: the ONLY call statement is AppearanceSettingsFragment.java:247 (onPreferenceChange branch), whose listener is bound only inside initLegacyNotifySettings (:185-189, vibration binding :188), gated at :118-119 (SDK < O). At API 27 the branch never fires. CHANGED 2026-11-01 round 2 OPEN -> UNREACHABLE. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED, no new caller or ungated listener binding. Flips back to REACHABLE on any printed ungated caller (including an ungated listener binding). Settings UI persistence alone is not a route. |
| 3 | SettingsRepositoryImpl.watchDir() | REACHABLE | SOURCE | `TorrentEngine.java:1053`, `:1582`, `:1588` (`if (pref.watchDir())`). Definition :773-775 freshly confirmed. |
| 4 | SettingsRepositoryImpl.watchDir(boolean) | REACHABLE | SOURCE | StorageSettingsFragment.java:281 (onPreferenceChange, pref_key_watch_dir branch): `pref.watchDir((boolean) newValue)`; listener bound in ungated onCreate at :170 (watchDir.setChecked + bindOnPreferenceChangeListener). Definition SettingsRepositoryImpl.java:779. CHANGED 2026-11-01 OPEN -> REACHABLE. |
| 5 | SettingsRepositoryImpl.watchDirDeleteFile() | REACHABLE | SOURCE | `TorrentEngine.java:1152` (`if (pref.watchDirDeleteFile())`). Definition :799-801 freshly confirmed. |
| 6 | SettingsRepositoryImpl.watchDirDeleteFile(boolean) | REACHABLE | SOURCE | StorageSettingsFragment.java:287 (onPreferenceChange, pref_key_watch_dir_delete_file branch): `pref.watchDirDeleteFile((boolean) newValue)`; listener bound in ungated onCreate at :197. Definition SettingsRepositoryImpl.java:805. CHANGED 2026-11-01 OPEN -> REACHABLE. |
| 7 | SettingsRepositoryImpl$Default.<clinit> | REACHABLE | INFERRED | JVM class initialisation on first `Default` access; many reachable getters evaluate `Default` fields/methods (e.g. :318, :331, :344, :645, :710). Nested-class `<clinit>` itself not printed. |
| 8 | SettingsRepositoryImpl$Default.dirToWatch(Context) | REACHABLE | SOURCE | Fallback argument in reachable getter `dirToWatch()` :786-788; getter called at `TorrentEngine.java:1117`. |
| 9 | SettingsRepositoryImpl$Default.encryptInConnectionsMode(Context) | REACHABLE | SOURCE | Fallback in getter :643-645; getter called at `TorrentEngine.java:1109` and inside `readSessionSettings()` :228. |
| 10 | SettingsRepositoryImpl$Default.encryptOutConnectionsMode(Context) | REACHABLE | SOURCE | Fallback in getter :656-658; getter called at `TorrentEngine.java:1113` and inside `readSessionSettings()` :229. |
| 11 | SettingsRepositoryImpl$Default.foregroundNotifySorting(Context) | REACHABLE | SOURCE | Fallback in getter :373-376; getter called at `Utils.java:896` (`getForegroundNotifySorting`), called from `TorrentService.java:139`. |
| 12 | SettingsRepositoryImpl$Default.foregroundNotifyStatusFilter(Context) | REACHABLE | SOURCE | Fallback in getter :355-358; getter called at `Utils.java:877` (`getForegroundNotifyFilter`), called from `TorrentService.java:138`. |
| 13 | SettingsRepositoryImpl$Default.ledIndicatorColorNotify(Context) | UNREACHABLE closed_by_api_level | INFERRED | Definition SettingsRepositoryImpl.java:53 freshly confirmed. Saved full-tree grep §B: the SOLE call statement is the fallback argument inside getter ledIndicatorColorNotify() at :342-344 (`Default.ledIndicatorColorNotify(appContext)`); no other file calls the Default (Context) overload (the :250 site calls the (int) setter, not this method). That getter is itself closed_by_api_level (batch 44 row 17): its only call statements are AppearanceSettingsFragment.java:180 (initLegacy, gated :118-119) and TorrentNotifier.java:290 (applyLegacy, early return :276 before :290), neither executing at API 27 — so the fallback argument is never evaluated at API 27. CHANGED 2026-11-01 round 2 OPEN -> UNREACHABLE. Re-check 2026-11-01 complete-tree+XML (281 Java + 73 XML, greps above): SURVIVED, no new caller of the getter or of the Default(Context) overload. Flips together with batch 44 row 17: any printed ungated caller of the getter flips both rows to REACHABLE. |
| 14 | SettingsRepositoryImpl$Default.moveAfterDownloadIn(Context) | REACHABLE | SOURCE | Fallback in getter :734-736; getter called at `TorrentEngine.java:1317`. |
| 15 | SettingsRepositoryImpl$Default.saveTorrentFilesIn(Context) | REACHABLE | SOURCE | Fallback in getter :760-762; getter called at `TorrentEngine.java:1275` and `:1432`. |
| 16 | SettingsRepositoryImpl$Default.saveTorrentsIn(Context) | REACHABLE | SOURCE | Fallback in getter :708-710; getter called at `TorrentEngine.java:1185`. |
| 17 | SettingsRepositoryImpl$Default.theme(Context) | REACHABLE | SOURCE | Fallback in getter `theme()` :329-331; getter called at `Utils.java:371` (`getThemePreference`), used by `Utils.getAppTheme` :375, applied at `MainActivity.java:137` (`setTheme(Utils.getAppTheme(...))`). |
| 18 | BaseSorting.<init>(String, Direction) | REACHABLE | SOURCE | Called by `TorrentSorting.<init>` :113-116 (`super(...)`); `TorrentSorting` constructed at `MainViewModel.java:51-52` and throughout `Utils.getForegroundNotifySorting`. BaseSorting definition freshly confirmed. |
| 19 | BaseSorting.getColumnName() | REACHABLE | SOURCE | Called at `TorrentSortingComparator.java:43` (`sorting.getColumnName()`). |
| 20 | BaseSorting.getDirection() | REACHABLE | SOURCE | Called at `TorrentSortingComparator.java:44` (`sorting.getDirection()`). |
| 21 | BaseSorting.toString() | UNREACHABLE | INFERRED | Definition BaseSorting.java:70-76 (fresh tree print; prior file cited :70-77 including the closing class brace). Saved full-tree grep §§C,J: NO explicit `.toString()` on a BaseSorting/TorrentSorting object, no Log/concat/String.valueOf site for a sorting object (the one §J concat hit, Utils.java:924, concatenates a String `val`, not a sorting object). TorrentSorting instances are constructed widely (MainViewModel.java:51-52, Utils.java:808-834, 898-922) but only getColumnName()/getDirection() are ever read on them (TorrentSortingComparator.java:43-44). The only toString hits in the sorting files are unrelated enum toStrings (BaseSorting.java:33 Direction.toString, TorrentSorting.java:106 column.toString). CONDITIONAL, not flipped (see below): flips to UNREACHABLE no_trigger_in_app INFERRED IF the merger adopts the app-tree-grep standard for toString (the standard under which batch 41 TorrentStream.toString was flipped on a similar supplementary log/concat grep); stays OPEN IF the merger holds the settings-family caveat that an implicit/framework toString (e.g. a library logging a sorting object) cannot be excluded from an app-Java-only corpus. That choice is the merger's, not made here. A printed explicit/implicit toString caller flips it to REACHABLE. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
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
- **36 REACHABLE proposed / 3 UNREACHABLE proposed (rows 1, 2, 13, all closed_by_api_level, all INFERRED; changed 2026-11-01 round 2) / 1 OPEN (row 21 only).**
- OPEN row: 21 only (rows 1, 2, 13 closed 2026-11-01 round 2; rows 4 and 6 closed 2026-11-01 round 1). No row was flipped to REACHABLE in round 2.

## Gaps the merger must close before merging

1. API-gate consistency check (batches 44/45/46/73-74 must match): rows 1, 2, 13 now
   rest on the saved full-tree grep in `~/workspace/b414748-openclose2-src/full_tree_grep_414748.txt`
   §§A-B plus the method-vs-branch rule as stated in batches 44, 74, 115. If the merger
   rejects that rule, rows 1, 2, 13 revert to OPEN (they do not flip to REACHABLE on
   rejection alone, since no ungated caller is printed). Row 13 flips together with
   batch 44 row 17 in either direction.
2. Row 21 (BaseSorting.toString): the conditional in its row — app-tree-grep standard
   (→ UNREACHABLE no_trigger_in_app) vs implicit/framework-toString caveat (→ stays OPEN).
   A printed toString caller flips it to REACHABLE under either reading.
3. Bytecode confirmation of the `$1`–`$7` anonymous-enum numbering.
4. Printed launcher → MainActivity / TorrentService step, if the strict-entry rule is
   applied at merge.
5. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.
2. Bytecode confirmation of the `$1`–`$7` anonymous-enum numbering.
3. Printed launcher → MainActivity / TorrentService step, if the strict-entry rule is
   applied at merge.
4. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run here.

## Strict-entry caveat

No launcher entry was printed in this pass. Under a strict launcher-entry rule all
34 REACHABLE rows above revert to OPEN on that point alone; the in-app chains are printed.
