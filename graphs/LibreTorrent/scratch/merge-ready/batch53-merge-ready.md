# LibreTorrent batch 53 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.
No connector `search_code` 0-result was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 53 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Prior work (Agent 16 proposal) was used as an INPUT / lead list only; every row below was
  re-judged against printed source, and three rows were FLIPPED from that proposal on fresh
  evidence printed in this pass (rows 2, 35, 40 — see "Flips in this pass"). All other rows
  carry the Agent 16 verdicts, re-checked against the same printed citations.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 53 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order.
Rows 1–32 are Room-generated `TorrentDao_Impl` (not in `final_java_only`); rows 33–40 are
hand-written `DefaultFsModule`.

## Printed source used

Base path (omitted in citations):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Fresh connector fetches in THIS pass, branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b5354-55-src/` (no fresh HTTP 429 hit in this pass):
- `core/storage/dao/TorrentDao.java` — full, 77 lines. This is the path Agent 16 missed
  (its two guesses `core/storage/TorrentDao.java` and `core/model/data/TorrentDao.java` failed
  cleanly); the correct path is `core/storage/dao/TorrentDao.java`, confirmed by the batch-52
  proposal's SHA `1a079658…` reference.
- `core/model/session/IPFilterParser.java` — full, 270 lines (used for batch 54, noted here
  because it closes the fileExists chain that flips row 35).
- `ui/detailtorrent/DetailTorrentViewModel.java` — full, fresh (used for batch 54, noted here
  because it closes the getFileUri chain that flips row 40).

Re-read from prior passes, flagged as such (Agent 16 printed these in full; not freshly
re-fetched in this pass except where noted above):
- `core/system/DefaultFsModule.java` (133 lines), `core/system/FileSystemFacadeImpl.java`
  (444 lines), `core/system/FsModuleResolverImpl.java` (~51 lines),
  `core/system/SystemFacadeHelper.java` (~47 lines), `core/system/SafFsModule.java` (162 lines),
  `core/storage/TorrentRepositoryImpl.java` (172 lines),
  `ui/settings/sections/StorageSettingsFragment.java` (296 lines),
  `ui/settings/sections/NetworkSettingsFragment.java`.
- `TorrentEngine.java` — local copy only (`~/workspace/ground-truth-work/libretorrent/src/`),
  NOT freshly fetched in this pass or in Agent 16's pass; merger must re-print it from the
  branch before merge. All TorrentEngine line numbers below are local-copy lines.

Abbreviations: `DFM` = `DefaultFsModule.java`, `FSFI` = `FileSystemFacadeImpl.java`,
`FMRI` = `FsModuleResolverImpl.java`, `SFH` = `SystemFacadeHelper.java`,
`TRI` = `TorrentRepositoryImpl.java`, `TE` = local `TorrentEngine.java`.

## Route anchors (printed)

1. **Room DAO interface calls.** `TRI` calls `db.torrentDao().<method>` at: `add` L57,
   `update` L62, `delete` L67, `getTorrentById` L72, `getTorrentByIdSingle` L77,
   `observeTorrentById` L82, `getAllTorrents` L87, `replaceTags` L127, `addTag` L132,
   `deleteTag` L137. The generated `TorrentDao_Impl` implements the same-named interface
   method, so an interface call is an INFERRED dispatch to the `_Impl` method (Room-generated
   class, body not in `final_java_only`).
2. **Filesystem facade singleton.** `SFH.getFileSystemFacade` L39–45 constructs
   `new FileSystemFacadeImpl(appContext, new FsModuleResolverImpl(appContext))`.
   Called by `StorageSettingsFragment.onCreate` L89, `NetworkSettingsFragment` L109, and
   `TE` constructor L132 (local copy).
3. **Resolver dispatch.** `FMRI.<init>` L35–39 constructs `new SafFsModule` (L37) and
   `new DefaultFsModule` (L38). `FMRI.resolveFsByUri` L42–50 returns the SAF module iff
   `Utils.isSafPath(...)` (L43), the default module iff `Utils.isFileSystemPath(uri)` (L45).
   Facade-to-module calls are therefore INFERRED interface dispatch, branch-chosen by URI type.
4. **TorrentEngine filesystem use (local copy).** `TE` constructor L132 obtains the facade;
   `TE` calls `fs.getFD` L380, `fs.createFile` L980, `fs.write` L984, `fs.deleteFile` L1154,
   `fs.getDirAvailableBytes` L1200, `fs.cleanTempDir` L1225.

## Flips in this pass (vs Agent 16 proposal — all three OPEN → REACHABLE)

1. **Row 2 `TorrentDao_Impl.deleteTagsByTorrentId` OPEN → REACHABLE INFERRED.**
   Fresh `TorrentDao.java`: `@Transaction replaceTags` (L67–70) calls
   `deleteTagsByTorrentId(torrentId)` (L68) and `addTags(infoList)` (L69).
   `replaceTags` is itself called by `TRI.replaceTags` L122–128
   (`db.torrentDao().replaceTags(torrentId, tagInfoList)`). The generated `_Impl`
   method is therefore reached through the hand-written transaction; dispatch from the
   transaction body to the generated impl is INFERRED (generated source not in upload).
   This is the same shape as batch-52 row 39 (`TorrentDao_Impl.addTags`, REACHABLE via
   the same transaction). It does NOT identify any `$N` adapter — see row group 10–32.
2. **Row 35 `DefaultFsModule.fileExists` OPEN → REACHABLE INFERRED.**
   Fresh `IPFilterParser.java`: `parseFile` L59–63 calls `fs.fileExists(path)` (L63).
   `FSFI.fileExists` L153–158 dispatches via `fsModule.fileExists(filePath)` (L157);
   the file-URI branch selects `DefaultFsModule` (`FMRI` L45–46), the SAF branch selects
   `SafFsModule` (batch 54 row 40 / batch 55 row 22, same facade call). Module dispatch
   is INFERRED. `parseFile` itself is called by `TorrentSessionImpl` L731 in the batch-34
   local copy — that line was NOT freshly fetched in this pass; merger re-print it if a
   fresh trunk anchor is required. The label does not depend on it: the facade call site
   in `IPFilterParser` is freshly printed.
3. **Row 40 `DefaultFsModule.getFileUri(String,Uri)` OPEN → REACHABLE INFERRED.**
   Fresh `DetailTorrentViewModel.java`: L275 `fs.getFileUri(relativePath, torrent.downloadPath)`.
   `FSFI.getFileUri(String,Uri)` L144–150 dispatches via
   `fsModule.getFileUri(relativePath, dir)` (L149); the file-URI branch selects
   `DefaultFsModule`, the SAF branch selects `SafFsModule` (batch 55 row 28, same facade
   call, already REACHABLE there). Module dispatch is INFERRED.

## Strict-entry caveat (explicit)

Every REACHABLE route below is anchored at `TorrentService` → `TorrentEngine`, at a settings
fragment, or at `TorrentRepositoryImpl`. The launcher-to-service step, the fragment-attachment
steps, and the callers of the `TorrentRepositoryImpl` methods themselves were NOT freshly
printed in this pass, so under a strict launcher-entry rule all REACHABLE rows revert to OPEN.
The `TorrentDao_Impl` rows additionally rest on Room-generated dispatch (INFERRED), not on
printed generated source.

## Undecided conventions recorded per row, NOT decided

- **Room `$N` mapping (rows 10–32):** per the task note, all `TorrentDao_Impl$1–$8` rows
  stay OPEN unless `$N` identity is confirmed against generated source or bytecode.
  `TorrentDao.java` declaration order (add, update, delete, getAllTorrents, getTorrentById,
  getTorrentByIdSingle, observeTorrentById, addTags, deleteTagsByTorrentId, addTag, deleteTag)
  is recorded as a LEAD ONLY for a canonical-order mapping (as batches 51–52 inferred for
  other DAOs); it is NOT adopted here, because declaration order is not generated source or
  bytecode, and the `$7`/`$8` Single/Flowable callables plus the `$N.finalize()` rows
  (see below) cannot be pinned by order alone.
- **Room Callable `finalize()` (rows 29, 32):** GC-only reasoning — only the JVM GC can invoke
  `finalize()` on a created Callable, so these rows are OPEN, not `no_trigger_in_app`;
  a project rule is still needed (same as batches 51–52).
- **`confirmed_by` convention:** SOURCE = a printed direct app-to-app call site naming the
  method; INFERRED = reached only through unprinted framework/library/generated dispatch
  (Room dispatch, FsModule interface dispatch, JVM class initialisation) where the
  registration or dispatch code is printed. This is the per-row convention, not the
  whole-route convention used in some earlier batches; labels are unaffected, only
  `confirmed_by` would change at merge under the whole-route convention.

## Per-row verdicts

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 1 | `TorrentDao_Impl.deleteTag` | REACHABLE | INFERRED | Interface call `TRI.deleteTag` L136–138 `db.torrentDao().deleteTag(...)`; Room dispatch to `_Impl.deleteTag` INFERRED (generated class not in upload). |
| 2 | `TorrentDao_Impl.deleteTagsByTorrentId` | REACHABLE | INFERRED | **FLIPPED in this pass.** Fresh `TorrentDao.java` `replaceTags` L67–70 calls `deleteTagsByTorrentId` L68; `replaceTags` called by `TRI.replaceTags` L122–128. Generated-impl dispatch INFERRED. |
| 3 | `TorrentDao_Impl.getAllTorrents` | REACHABLE | INFERRED | Interface call `TRI.getAllTorrents` L86–88 `db.torrentDao().getAllTorrents()`; Room dispatch INFERRED. |
| 4 | `TorrentDao_Impl.getRequiredConverters` | OPEN | — | No printed app call. Lead only: Room framework may call this during database build/open, but Room source was not printed, so this stays OPEN, not INFERRED REACHABLE (consistent with the batch-48 treatment of the equivalent `AppDatabase` converter method as OPEN). Needs printed Room dispatch or saved full-repo grep. |
| 5 | `TorrentDao_Impl.getTorrentById` | REACHABLE | INFERRED | Interface call `TRI.getTorrentById` L71–73; Room dispatch INFERRED. |
| 6 | `TorrentDao_Impl.getTorrentByIdSingle` | REACHABLE | INFERRED | Interface call `TRI.getTorrentByIdSingle` L76–78; Room dispatch INFERRED. |
| 7 | `TorrentDao_Impl.observeTorrentById` | REACHABLE | INFERRED | Interface call `TRI.observeTorrentById` L81–83; Room dispatch INFERRED. |
| 8 | `TorrentDao_Impl.replaceTags` | REACHABLE | INFERRED | Interface call `TRI.replaceTags` L122–128 `db.torrentDao().replaceTags(torrentId, tagInfoList)`; Room dispatch INFERRED. (Note: the hand-written `TorrentDao.replaceTags` body itself is batch-52 row 35, SOURCE; this row is its generated `_Impl` counterpart.) |
| 9 | `TorrentDao_Impl.update` | REACHABLE | INFERRED | Interface call `TRI.updateTorrent` L61–63 `db.torrentDao().update(torrent)`; Room dispatch INFERRED. |
| 10 | `TorrentDao_Impl$1.<init>` | OPEN | — | Generated inner class; its identity (which DAO method / adapter it serves) is NOT printed. Room dispatch alone does not identify `$1`. Confirm `$N` mapping against generated source or bytecode before any flip. |
| 11 | `TorrentDao_Impl$1.bind` | OPEN | — | Same as row 10: `$1` identity unprinted. |
| 12 | `TorrentDao_Impl$1.createQuery` | OPEN | — | Same as row 10: `$1` identity unprinted. |
| 13 | `TorrentDao_Impl$2.<init>` | OPEN | — | Same as row 10: `$2` identity unprinted. |
| 14 | `TorrentDao_Impl$2.bind` | OPEN | — | Same as row 10. |
| 15 | `TorrentDao_Impl$2.createQuery` | OPEN | — | Same as row 10. |
| 16 | `TorrentDao_Impl$3.<init>` | OPEN | — | Same as row 10: `$3` identity unprinted. |
| 17 | `TorrentDao_Impl$3.bind` | OPEN | — | Same as row 10. |
| 18 | `TorrentDao_Impl$3.createQuery` | OPEN | — | Same as row 10. |
| 19 | `TorrentDao_Impl$4.<init>` | OPEN | — | Same as row 10: `$4` identity unprinted. |
| 20 | `TorrentDao_Impl$4.bind` | OPEN | — | Same as row 10. |
| 21 | `TorrentDao_Impl$4.createQuery` | OPEN | — | Same as row 10. |
| 22 | `TorrentDao_Impl$5.<init>` | OPEN | — | Same as row 10: `$5` identity unprinted. |
| 23 | `TorrentDao_Impl$5.bind` | OPEN | — | Same as row 10. |
| 24 | `TorrentDao_Impl$5.createQuery` | OPEN | — | Same as row 10. |
| 25 | `TorrentDao_Impl$6.<init>` | OPEN | — | Same as row 10: `$6` identity unprinted (no `bind` row, so it is a query adapter, but which query is unprinted). |
| 26 | `TorrentDao_Impl$6.createQuery` | OPEN | — | Same as row 25. |
| 27 | `TorrentDao_Impl$7.<init>` | OPEN | — | Same as row 10: `$7` identity unprinted (call/finalize shape suggests a Single/Flowable callable, but which DAO query is unprinted). |
| 28 | `TorrentDao_Impl$7.call` | OPEN | — | Same as row 27. |
| 29 | `TorrentDao_Impl$7.finalize` | OPEN | — | Same as row 27; plus the Callable `finalize()` rule is undecided (GC-only, not `no_trigger_in_app` on this evidence). |
| 30 | `TorrentDao_Impl$8.<init>` | OPEN | — | Same as row 10: `$8` identity unprinted. |
| 31 | `TorrentDao_Impl$8.call` | OPEN | — | Same as row 30. |
| 32 | `TorrentDao_Impl$8.finalize` | OPEN | — | Same as row 30; plus the Callable `finalize()` rule is undecided. |
| 33 | `DefaultFsModule.<init>` | REACHABLE | SOURCE | Def `DFM` L35–38. Constructed by `FMRI.<init>` L38 `new DefaultFsModule(appContext)`; resolver constructed by `SFH` L41–42; helper called by Storage fragment L89, Network fragment L109, `TE` L132 (local copy). |
| 34 | `DefaultFsModule.delete` | REACHABLE | INFERRED | Def `DFM` L79–82. Dispatcher: `FSFI.deleteFile` L110–115 calls `fsModule.delete(path)` L114; facade reachable via `TE` L1154 (local copy). Resolver file-path branch (`FMRI` L45–46) selects the default module; SAF branch selects `SafFsModule` instead, so this row is the file-URI branch, INFERRED. |
| 35 | `DefaultFsModule.fileExists` | REACHABLE | INFERRED | **FLIPPED in this pass.** Fresh `IPFilterParser.parseFile` L63 `fs.fileExists(path)` → `FSFI.fileExists` L153–158 → `fsModule.fileExists` L157; file-URI branch selects `DefaultFsModule`. Flips together with batch-54 row 13 (facade) and row 40 (SAF side) on the same facade call. |
| 36 | `DefaultFsModule.getDirAvailableBytes` | REACHABLE | INFERRED | Def `DFM` L91–106. Dispatcher: `FSFI.getDirAvailableBytes` L268–282 calls `fsModule.getDirAvailableBytes(dir)` L274; facade reachable via `TE` L1200 (local copy). File-URI branch INFERRED. |
| 37 | `DefaultFsModule.getDirPath` | REACHABLE | INFERRED | Def `DFM` L47–50. Dispatcher: `FSFI.getDirPath` L418–423 calls `fsModule.getDirPath(dir)` L422; facade reachable via Storage fragment `onCreate` L99 (also L126, L153, L180, L271). File-URI branch INFERRED. |
| 38 | `DefaultFsModule.getFilePath` | REACHABLE | INFERRED | Def `DFM` L53–56. Dispatcher: `FSFI.getFilePath` L430–435 calls `fsModule.getFilePath(filePath)` L434; facade reachable via Network fragment L208 and L396. File-URI branch INFERRED. |
| 39 | `DefaultFsModule.getFileUri(Uri,String,boolean)` | REACHABLE | INFERRED | Def `DFM` L59–66. Direct module call (not via facade): `FSFI.createFile` L199–218 calls `fsModule.getFileUri(dir, fileName, false)` L205 and `(..., true)` L213; `createFile` reachable via `TE` L980 (local copy). Module interface dispatch INFERRED. |
| 40 | `DefaultFsModule.getFileUri(String,Uri)` | REACHABLE | INFERRED | **FLIPPED in this pass.** Fresh `DetailTorrentViewModel.java` L275 `fs.getFileUri(relativePath, torrent.downloadPath)` → `FSFI.getFileUri(String,Uri)` L144–150 → `fsModule.getFileUri(relativePath, dir)` L149; file-URI branch selects `DefaultFsModule`, SAF branch selects `SafFsModule` (batch 55 row 28, same facade call). Module dispatch INFERRED. |

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order, method names and JVM descriptors matching
  the plan copy row for row.**
- **16 REACHABLE proposed / 0 UNREACHABLE / 24 OPEN.**
- REACHABLE rows: 1, 2, 3, 5, 6, 7, 8, 9, 33, 34, 35, 36, 37, 38, 39, 40.
  Of these: SOURCE 1 (row 33) / INFERRED 15.
- OPEN rows: 4, 10–32 (all 23 `TorrentDao_Impl$N` rows).
- **0 rows verified for merge.** No UNREACHABLE is claimed: no saved full-repo grep was run
  in this pass, and absence from the printed subset is not evidence of absence.

## What the merger still needs

1. Saved full-repo grep for all 24 OPEN rows, in priority order: `getRequiredConverters`,
   the `TorrentDao_Impl$1`–`$8` mapping (generated source or bytecode — declaration order
   alone does not close these rows).
2. Printed DAO interface file — DONE in this pass (`TorrentDao.java`, fresh), which closed
   row 2; no further interface print is owed for this batch.
3. Fresh branch re-print of `TorrentEngine.java` (all `TE` lines above are local-copy lines)
   and, if a fresh trunk anchor is required, `TorrentSessionImpl` L731 (`IPFilterParser.parseFile` caller).
4. Printed launcher-to-`TorrentService` step and fragment-attachment steps if the strict-entry
   rule is applied (all REACHABLE rows revert to OPEN under a strict rule).
5. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
