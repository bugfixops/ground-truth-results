## REVISION 2026-11-01 — OPEN-close round 2, group G7 (batches 50-53), labels only

Counts before = counts after: 16 REACHABLE / 0 UNREACHABLE / 24 OPEN. Label changes in this pass: 0. The 24 OPEN rows are one converter row, 21 SET rows, and two finalize rows; their conditional flips are recorded below and in the rows themselves. Nothing was flipped, because every OPEN row depends on a convention (Room $N SET-vs-STRICT, finalize (vi), or converters (xiii)) that this pass does not decide. This batch is the STRICT-applied counterpart to batches 51-52, which already apply SET: under SET, the 21 rows below flip together to REACHABLE INFERRED with no further source print needed for the flip itself, because set membership is fully verified here. Under STRICT they stay OPEN. The merger must apply ONE rule project-wide; harmonizing 51-52 (already SET) with 53 (STRICT) in either direction changes 21 rows here and/or 46 rows across batches 50-52 (50: 3, 51: 25, 52: 18).

Set-membership verification (fresh prints, this pass) — the core deliverable for this batch. TorrentDao.java (77 lines) operations: add :40 (@Insert Torrent), update :43 (@Update Torrent), delete :46 (@Delete Torrent), getAllTorrents :49 (@Query plain List), getTorrentById :52 (@Query plain Torrent), getTorrentByIdSingle :55 (@Query Single Torrent), observeTorrentById :58 (@Query Flowable Torrent), addTags :61 (@Insert List TorrentTagInfo), deleteTagsByTorrentId :64 (@Query DELETE), replaceTags :67-70 (@Transaction concrete method calling deleteTagsByTorrentId :68 and addTags :69), addTag :73 (@Insert TorrentTagInfo), deleteTag :76 (@Delete TorrentTagInfo). TorrentRepositoryImpl.java calls at DAO-interface level: add :57, update :62, delete :67, getTorrentById :72, getTorrentByIdSingle :77, observeTorrentById :82, getAllTorrents :87, replaceTags :127, addTag :132, deleteTag :137. Every TorrentDao operation is therefore called, directly or (for addTags and deleteTagsByTorrentId) through the concrete replaceTags transaction body, which is itself called by the repository. The two plain-select methods that generate no helper class (getAllTorrents, getTorrentById) are recorded here for completeness; the prior revision note's operation list omitted them because they are not $N-relevant, which is correct, not an error.
- Bind-adapter set $1-$5 (rows 10-24): plan bind descriptors, in $ order, are Torrent, TorrentTagInfo, Torrent, TorrentTagInfo, Torrent (multiset Torrent x3, TorrentTagInfo x2 — exactly as the prior revision note claimed; verified against the plan in this pass, no correction needed). Adapters per entity plus operation type: insertion Torrent (add, repository :57), insertion TorrentTagInfo (serves both addTags via replaceTags and addTag :132, exactly as addFeed/addFeeds share one FeedChannel insertion adapter in batch 51), update Torrent (update :62), deletion Torrent (delete :67), deletion TorrentTagInfo (deleteTag :137). That is 5 adapters for the 6 insert/update/delete methods, because addTags and addTag share one adapter; a per-method count of 6 would contradict the plan, which contains exactly 5 bind sets. All five adapters' operations are called, so every $1-$5 row is a SET member regardless of which $N serves which adapter. No membership error found.
- Statement set $6 (rows 25-26, <init> plus createQuery only, no bind): deleteTagsByTorrentId is the sole @Query method that is neither a plain select nor an Rx method, so it is the sole SharedSQLiteStatement candidate (same shape as batch-51 $5-$7). It is called through TorrentDao.replaceTags :68, called by TorrentRepositoryImpl.replaceTags :127. This set has size 1 and is pinned, not merely set-assigned, subject only to the SET-vs-STRICT convention question itself (no generated source pins $6 individually).
- Callable set $7-$8 (rows 27-28, 30-31, plus finalize rows 29/32): plan call descriptors both return Torrent. The sole Torrent-returning Rx methods are getTorrentByIdSingle (TorrentDao:55, repository :77) and observeTorrentById (TorrentDao:58, repository :82), both called. So every $7/$8 <init>/call row is a SET member. Count check: 5 bind adapters + 1 statement + 2 Callables = 8 helper classes = plan $1-$8 exactly; there is no missing or extra $ class in this batch.
- Correction note (no label effect): the rows below previously recorded only that $N identity is unprinted. That remains true for individual $N identity, but it must not be read as "set membership unknown": membership is now verified as above, and the rows carry their conditional flips in this pass.

Conditional table (this batch, complete — 24 OPEN rows):
- Row 4 TorrentDao_Impl.getRequiredConverters: stays OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, flipping together with 50/27, 51/6, and 52/11. Note the dossier wording variance, recorded not resolved: the 50-52 files' flip text names the trio without naming 53/4 explicitly, while the Room grep summary lists all four DAO rows (plus sibling 48/14) as flipping together on a printed dispatch. This pass treats all four DAO converter rows as one set; the merger should confirm the same treatment for 53/4 when it rules on (xiii).
- Rows 10-28 and 30-31 (21 rows: $1-$5 <init>/bind/createQuery, $6 <init>/createQuery, $7/$8 <init>/call): stay OPEN. Conditional flip: REACHABLE INFERRED if and only if the merger adopts the Room $N SET convention (the convention already applied in batches 51-52). No further source print is needed for that flip; membership is verified above.
- Rows 29 and 32 TorrentDao_Impl$7/$8.finalize: stay OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route. Their enclosing Callables are rows 27-28 and 30-31, SET members verified above, so membership is not in doubt; the blocker is purely the (vi) rule. Under SET alone (without (vi)) these two rows stay OPEN; under (vi) alone the merger must still state whether set membership suffices for these two rows, whose <init>/call rows are OPEN under STRICT — the dossier's cumulative SET+finalize+converters figure (196/0/4 for batches 48+50-53) counts them on top of SET, and this pass does not choose between those readings. These rows are NOT no_trigger_in_app and must never be flipped to UNREACHABLE on zero app-code hits.
- No other OPEN row exists in this batch. Group OPEN accounting: converters 4 + finalize 10 + batch-53 SET 21 = 35 OPEN rows across batches 50-53, every one accounted for in its batch's conditional table.

Source for this pass (copies in ~/workspace/b50515253-openclose2-src/, connector-reconstructed 2026-11-01 05:18-05:21 copies copied verbatim, no new GitHub connector fetch in this pass because no needed file was missing locally; no fresh HTTP 429): AppDatabase.java SHA c673131c64be, FastResumeDao.java 3e6fcd70d6f2, FeedDao.java 2c8c954d738ca, TagInfoDao.java 61aee6239368, TorrentDao.java f24aab9a09ff2, FeedRepositoryImpl.java 1c5e193a62d1, TagRepositoryImpl.java d579b631ed85, TorrentRepositoryImpl.java fe8717338997. The core/storage/dao/ directory listing contains exactly those four DAO files, no generated Impl file. A grep over the round-2 source copies finds zero occurrences of finalize, getRequiredConverters, or Impl dispatch in app source; zero hits are never used as evidence of absence, and no generated source was printed, so no Impl identity is pinned individually. Framework note (recorded, not invented): the fw_src walked path fw_src/android-8.1.0_r1/libcore/ojluni/src/main/java/java/ contains only io and util, no lang/, hence no printed Object.java finalization dispatch exists in the branch; no framework citation is claimed. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another agent's file. No project convention was decided in this pass.


**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

## Revision note — open-close pass 2026-11-01 (NO label changes)

**Counts before and after: 16 REACHABLE proposed / 0 UNREACHABLE / 24 OPEN. No row flips
in this pass.** Every OPEN row was re-examined against freshly printed source in this pass
(branch work-2026-10-31, GitHub connector only, one file at a time with ~25 s pauses, no
fresh HTTP 429), saved in `~/workspace/b5354-openclose-src/`:
`core/model/TorrentEngine.java` (1659 lines, SHA 17d06efe1076675af0c41a6c929e8d2f04eabb68),
`core/storage/dao/TorrentDao.java` (77 lines, SHA 1a079658ca7f8fc36d609e4e61c21a8f08e7def8),
`core/storage/TorrentRepositoryImpl.java` (172 lines, SHA 0f01eff0a7613bfa2ecdb3052e7914ba9f00bd54),
plus the batch-54 files listed in that file's revision note.
**TorrentEngine freshness closed:** the fresh TorrentEngine print matches the earlier
local-copy lines exactly (facade L132, getFD L380, createFile L980, write L984, deleteFile
L1154, getDirAvailableBytes L1200, cleanTempDir L1225), so the "TE lines are local-copy
lines" caveat in the original file no longer applies to those citations.
**Why the $N rows (10–32, except finalize rows 29/32) do NOT flip here, despite a strong
set argument:** fresh `TorrentDao.java` shows the DAO operations (@Insert add/addTags/addTag,
@Update update, @Delete delete/deleteTag, @Query deleteTagsByTorrentId, @Query Single
getTorrentByIdSingle, @Query Flowable observeTorrentById) and fresh `TorrentRepositoryImpl.java`
calls every one of them (add L57, update L62, delete L67, getTorrentByIdSingle L77,
observeTorrentById L82, replaceTags L127 → deleteTagsByTorrentId, addTag L132, deleteTag
L137); and the plan bind-type multiset for $1–$5 (Torrent, TagInfo, Torrent, TagInfo,
Torrent) exactly matches the entity adapters for add/update/delete/addTag/deleteTag, with
$6 (createQuery only) matching the deleteTagsByTorrentId statement and $7/$8
(RoomSQLiteQuery, call → Torrent) matching the two Rx query methods. Under the Room $N
**set** convention used in batches 51–52, all $N non-finalize rows would flip together to
REACHABLE INFERRED. Under the **strict** identity rule, they stay OPEN, because no printed
generated source or bytecode pins which $N serves which operation. The strict-vs-set
convention is undecided project-wide and this pass does not decide it, so the rows stay
OPEN with the set argument recorded here for the merger — they are the single largest
remaining OPEN block in this batch and flip as a set the moment the merger adopts the set
convention, with no further source print needed for the flip itself.
**Row 4 `getRequiredConverters` stays OPEN:** no printed app call and no printed Room
dispatch; a full app-tree grep showing zero app-code callers would not close it either,
because the generated dispatch that might call it is unprinted — same ground as batches
50–52. **Rows 29/32 `finalize` stay OPEN:** Callable finalize is GC-only; the project rule
is undecided (convention vi), so they are not `no_trigger_in_app` on this evidence.
Build: not run. C1: not run.

# LibreTorrent batch 53 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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
| 4 | `TorrentDao_Impl.getRequiredConverters` | OPEN | — | No printed app call. Lead only: Room framework may call this during database build/open, but Room source was not printed, so this stays OPEN, not INFERRED REACHABLE (consistent with the batch-48 treatment of the equivalent `AppDatabase` converter method as OPEN). Needs printed Room dispatch or saved full-repo grep. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, together with 50/27, 51/6, 52/11, 53/4. No label change in this pass; no convention decided.] |
| 5 | `TorrentDao_Impl.getTorrentById` | REACHABLE | INFERRED | Interface call `TRI.getTorrentById` L71–73; Room dispatch INFERRED. |
| 6 | `TorrentDao_Impl.getTorrentByIdSingle` | REACHABLE | INFERRED | Interface call `TRI.getTorrentByIdSingle` L76–78; Room dispatch INFERRED. |
| 7 | `TorrentDao_Impl.observeTorrentById` | REACHABLE | INFERRED | Interface call `TRI.observeTorrentById` L81–83; Room dispatch INFERRED. |
| 8 | `TorrentDao_Impl.replaceTags` | REACHABLE | INFERRED | Interface call `TRI.replaceTags` L122–128 `db.torrentDao().replaceTags(torrentId, tagInfoList)`; Room dispatch INFERRED. (Note: the hand-written `TorrentDao.replaceTags` body itself is batch-52 row 35, SOURCE; this row is its generated `_Impl` counterpart.) |
| 9 | `TorrentDao_Impl.update` | REACHABLE | INFERRED | Interface call `TRI.updateTorrent` L61–63 `db.torrentDao().update(torrent)`; Room dispatch INFERRED. |
| 10 | `TorrentDao_Impl$1.<init>` | OPEN | — | Generated inner class; its identity (which DAO method / adapter it serves) is NOT printed. Room dispatch alone does not identify `$1`. Confirm `$N` mapping against generated source or bytecode before any flip. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 11 | `TorrentDao_Impl$1.bind` | OPEN | — | Same as row 10: `$1` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 12 | `TorrentDao_Impl$1.createQuery` | OPEN | — | Same as row 10: `$1` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 13 | `TorrentDao_Impl$2.<init>` | OPEN | — | Same as row 10: `$2` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 14 | `TorrentDao_Impl$2.bind` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 15 | `TorrentDao_Impl$2.createQuery` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 16 | `TorrentDao_Impl$3.<init>` | OPEN | — | Same as row 10: `$3` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 17 | `TorrentDao_Impl$3.bind` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 18 | `TorrentDao_Impl$3.createQuery` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 19 | `TorrentDao_Impl$4.<init>` | OPEN | — | Same as row 10: `$4` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 20 | `TorrentDao_Impl$4.bind` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 21 | `TorrentDao_Impl$4.createQuery` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 22 | `TorrentDao_Impl$5.<init>` | OPEN | — | Same as row 10: `$5` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 23 | `TorrentDao_Impl$5.bind` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 24 | `TorrentDao_Impl$5.createQuery` | OPEN | — | Same as row 10. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 25 | `TorrentDao_Impl$6.<init>` | OPEN | — | Same as row 10: `$6` identity unprinted (no `bind` row, so it is a query adapter, but which query is unprinted). [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 26 | `TorrentDao_Impl$6.createQuery` | OPEN | — | Same as row 25. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 27 | `TorrentDao_Impl$7.<init>` | OPEN | — | Same as row 10: `$7` identity unprinted (call/finalize shape suggests a Single/Flowable callable, but which DAO query is unprinted). [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 28 | `TorrentDao_Impl$7.call` | OPEN | — | Same as row 27. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 29 | `TorrentDao_Impl$7.finalize` | OPEN | — | Same as row 27; plus the Callable `finalize()` rule is undecided (GC-only, not `no_trigger_in_app` on this evidence). [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] |
| 30 | `TorrentDao_Impl$8.<init>` | OPEN | — | Same as row 10: `$8` identity unprinted. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 31 | `TorrentDao_Impl$8.call` | OPEN | — | Same as row 30. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff the merger adopts the Room $N SET convention (as already applied in batches 51-52). Set membership verified in the round-2 note above. No label change in this pass.] |
| 32 | `TorrentDao_Impl$8.finalize` | OPEN | — | Same as row 30; plus the Callable `finalize()` rule is undecided. [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] |
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
3. ~~Fresh branch re-print of `TorrentEngine.java`~~ — DONE in open-close pass 2026-11-01
   (fresh print SHA 17d06efe…, 1659 lines; TE lines verified identical to the local-copy
   lines cited above). Still owed if a fresh trunk anchor is required:
   `TorrentSessionImpl` L731 (`IPFilterParser.parseFile` caller).
4. Printed launcher-to-`TorrentService` step and fragment-attachment steps if the strict-entry
   rule is applied (all REACHABLE rows revert to OPEN under a strict rule).
5. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
