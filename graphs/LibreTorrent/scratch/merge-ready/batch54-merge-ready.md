**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

## Revision note — open-close pass 2026-11-01

**Counts before: 35 REACHABLE proposed / 0 UNREACHABLE / 5 OPEN. Counts after: 40 / 0 / 0.**
All five OPEN rows flip to REACHABLE SOURCE on freshly printed source in this pass (see
"Flips in this open-close pass" below). No other row's label changes. Fresh source for this
pass (branch work-2026-10-31, GitHub connector only, one file at a time with ~25 s pauses,
no fresh HTTP 429), saved in `~/workspace/b5354-openclose-src/`:
`core/model/TorrentEngine.java` (1659 lines, SHA 17d06efe1076675af0c41a6c929e8d2f04eabb68),
`core/system/FileSystemFacadeImpl.java` (444 lines, SHA 3e67b0c6d0a2930d0d5f54ec3abf03eb75c31435),
`ui/filemanager/FileManagerViewModel.java` (393 lines, SHA 98399f0a95eb2adb07f5e5f97427197c3025981f),
`ui/filemanager/FileManagerDialog.java` (692 lines, SHA 62c879b92cff8341dc1f26b1fd235902c6050c8b),
`core/storage/FeedRepositoryImpl.java` (226 lines, SHA 20f94942d1147a21f97775ce882ad526068cd8c8),
`ui/feeds/FeedViewModel.java` (172 lines, SHA c72f614afd02a3df5661d72532693d7444c8a388),
`ui/feeds/FeedActivity.java` (412 lines, SHA 90d659739ba7f136f1c0b97e1d2163f0c3227f84).
**TorrentEngine freshness closed:** the fresh TorrentEngine print matches the earlier
local-copy lines exactly (facade L132, getFD L380, createFile L980, write L984, deleteFile
L1154, getDirAvailableBytes L1200, cleanTempDir L1225), so the "TE lines are local-copy
lines" caveat in the original file no longer applies to those citations.
**Batch-4 interaction re-checked, NOT flipped:** batch-4 row 15 (`isValidFatFilename`,
UNREACHABLE proposed INFERRED) is a different method from row 9; FileManagerViewModel calls
`buildValidFatFilename`, not `isValidFatFilename`, so row 15's caller is still missing and
row 15 is unchanged by this pass. Build: not run. C1: not run.

# LibreTorrent batch 54 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.
No connector `search_code` 0-result was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 54 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Prior work (Agent 16 proposal) was used as an INPUT / lead list only; every row below was
  re-judged against printed source, and fourteen rows were FLIPPED from that proposal on
  evidence printed in this pass (rows 1, 2, 13, 14, 17, 21, 22, 23, 25, 28, 29, 30, 31, 40 —
  see "Flips in this pass"). All other rows carry the Agent 16 verdicts, re-checked against
  the same printed citations.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 54 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order.
Rows 1–3 are the tail of `DefaultFsModule` (continued from batch 53), rows 4–6
`FileDescriptorWrapperImpl`, rows 7–34 `FileSystemFacadeImpl`, rows 35–36 `FsModuleResolverImpl`,
rows 37–40 `SafFileSystem` (Uri overloads only; the `FakePath` overloads are different rows).

## Printed source used

Base path (omitted in citations):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Fresh connector fetches in THIS pass, branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b5354-55-src/` (no fresh HTTP 429 hit in this pass; one clean
file-not-found, not a 429 — see below):
- `core/model/session/IPFilterParser.java` — full, 270 lines, fresh.
- `ui/detailtorrent/DetailTorrentViewModel.java` — full, fresh.
- `ui/createtorrent/CreateTorrentViewModel.java` — full, fresh.
- `core/model/session/TorrentDownloadImpl.java` — full, fresh.
- `core/utils/Utils.java` — full, fresh.
- `ui/feeds/FeedActivity.java` — full, fresh.
- `core/model/session/TorrentSessionImpl.java` — full, fresh.
- `ui/addtorrent/AddTorrentViewModel.java` — full, fresh.
- Clean miss (not a 429, not retried in a loop): `ui/feed/FeedActivity.java` does not exist;
  the feeds activity lives at `ui/feeds/FeedActivity.java` (fetched fresh above).

Re-read from prior passes, flagged as such (Agent 16 printed these in full; not freshly
re-fetched in this pass except where noted above):
- `core/system/DefaultFsModule.java` (133 lines), `core/system/FileDescriptorWrapperImpl.java`
  (59 lines), `core/system/FileSystemFacadeImpl.java` (444 lines),
  `core/system/FsModuleResolverImpl.java` (~51 lines), `core/system/SafFileSystem.java`
  (549 lines), `core/system/SafFsModule.java` (162 lines),
  `core/system/SystemFacadeHelper.java` (~47 lines),
  `core/storage/TorrentRepositoryImpl.java` (172 lines),
  `ui/settings/sections/StorageSettingsFragment.java` (296 lines),
  `ui/settings/sections/NetworkSettingsFragment.java`.
- `TorrentEngine.java` — local copy only, NOT freshly fetched in this pass or in Agent 16's
  pass; merger must re-print it from the branch before merge. All TorrentEngine line numbers
  below are local-copy lines.

Abbreviations: `DFM` = `DefaultFsModule.java`, `FDWI` = `FileDescriptorWrapperImpl.java`,
`FSFI` = `FileSystemFacadeImpl.java`, `FMRI` = `FsModuleResolverImpl.java`,
`SFS` = `SafFileSystem.java`, `SFM` = `SafFsModule.java`, `SFH` = `SystemFacadeHelper.java`,
`TRI` = `TorrentRepositoryImpl.java`, `TE` = local `TorrentEngine.java`.

## Route anchors (printed)

1. **Facade singleton.** `SFH.getFileSystemFacade` L39–45 constructs
   `new FileSystemFacadeImpl(appContext, new FsModuleResolverImpl(appContext))`.
   Called by `StorageSettingsFragment.onCreate` L89, `NetworkSettingsFragment` L109,
   `TE` constructor L132 (local copy).
2. **Resolver dispatch.** `FMRI.resolveFsByUri` L42–50 returns the SAF module iff
   `Utils.isSafPath(...)` (L43), the default module iff `Utils.isFileSystemPath(uri)` (L45).
   Every `FSFI` dispatch method calls it first (e.g. `getFD` L62, `deleteFile` L112,
   `createFile` L203, `getDirAvailableBytes` L272, `getDirPath` L420, `getFilePath` L432,
   `getParentDirUri` L440).
3. **TorrentEngine filesystem use (local copy).** `TE` L132 obtains the facade; calls
   `fs.getFD` L380, `fs.createFile` L980, `fs.write(byte[])` L984, `fs.deleteFile` L1154,
   `fs.getDirAvailableBytes` L1200, `fs.cleanTempDir` L1225.
4. **Settings fragments.** Storage `onCreate` L89 (facade) + L99/L126/L153/L180/L271
   (`getDirPath`); Network L109 (facade) + L208/L396 (`getFilePath`).
5. **Repository filesystem use.** `TRI.getSessionFile` L110 and `TRI.getTorrentDataDir` L146
   call `SystemFacadeHelper.getFileSystemFacade(...).isStorageReadable()`.
6. **SAF chain.** `SFM.delete` L84–89 calls `SFS.getInstance(...).delete(filePath)` (L88);
   `SFM.fileExists` L136–139 calls `SFS.getInstance(...).exists(filePath)` (L138);
   `SFM.openFD` L92–95 and `DFM.openFD` L85–88 both construct `new FileDescriptorWrapperImpl(...)`.
   `SFS.getInstance` L72–82 constructs the singleton at L77; `SFS.<init>` is L84–87, private.

## Flips in this pass (vs Agent 16 proposal — all fourteen OPEN → REACHABLE)

1. **Row 1 `DefaultFsModule.getParentDirUri` → REACHABLE INFERRED** and
   **row 23 `FileSystemFacadeImpl.getParentDirUri` → REACHABLE SOURCE.**
   Fresh `CreateTorrentViewModel.java` L357: `savePath = fs.getParentDirUri(seedPath)`.
   The facade method dispatches via `fsModule.getParentDirUri(filePath)` (`FSFI` L442);
   the file-URI branch selects `DefaultFsModule`, the SAF branch selects `SafFsModule`
   (batch 55 row 29, same facade call). Module dispatch is INFERRED. This also flips
   batch-55 rows 7 and 29 (same chain, SAF side).
2. **Row 2 `DefaultFsModule.makeFileSystemPath` → REACHABLE INFERRED.**
   Via row 29 below: `FSFI.makeFileSystemPath(Uri,String)` L254–260 calls
   `fsModule.makeFileSystemPath(uri, relativePath)` (L259); module dispatch INFERRED,
   file-URI branch = `DefaultFsModule`, SAF branch = `SafFsModule` (batch 55 row 30).
3. **Row 13 `FileSystemFacadeImpl.fileExists` → REACHABLE SOURCE.**
   Fresh `IPFilterParser.java`: `parseFile` L59–63 calls `fs.fileExists(path)` (L63).
   This also flips batch-53 row 35 (file-URI module side) and row 40 below (SAF side)
   on the same facade call. `parseFile`'s own caller (`TorrentSessionImpl` L731 in the
   batch-34 local copy) was NOT freshly fetched in this pass; the label rests on the
   freshly printed `IPFilterParser` call site, not on that trunk line.
4. **Row 14 `FileSystemFacadeImpl.getDefaultDownloadPath` → REACHABLE SOURCE.**
   Fresh `Utils.java` L644: `path = (TextUtils.isEmpty(path) ? fs.getDefaultDownloadPath() : path)`.
5. **Row 17 `FileSystemFacadeImpl.getExtension` → REACHABLE SOURCE.**
   Fresh `DetailTorrentViewModel.java` L399, in `makeOpenFileIntent`:
   `String extension = fs.getExtension(fileName)`.
   (Row 18 does NOT flip with it: `getExtension` reads the `EXTENSION_SEPARATOR` field
   directly, it does not call `getExtensionSeparator()` — see row 18.)
6. **Row 21 `FileSystemFacadeImpl.getFileUri(Uri,String)` → REACHABLE SOURCE.**
   Fresh `TorrentDownloadImpl.java` L1299:
   `return fs.getFileUri(torrent.downloadPath, "." + ti.infoHash() + ".parts")`.
   (Agent 16 noted only that `FSFI.createFile` calls the *module* method directly; the
   facade overload has this separate printed caller.)
7. **Row 22 `FileSystemFacadeImpl.getFileUri(String,Uri)` → REACHABLE SOURCE.**
   Fresh `DetailTorrentViewModel.java` L275:
   `Uri path = fs.getFileUri(relativePath, torrent.downloadPath)`.
   This also flips batch-53 row 40 (file-URI module side) on the same facade call.
8. **Row 25 `FileSystemFacadeImpl.getUserDirPath` → REACHABLE SOURCE.**
   Fresh `FeedActivity.java` L266 and L282:
   `new FileManagerConfig(fs.getUserDirPath(), ...)`.
9. **Row 28 `FileSystemFacadeImpl.makeFileSystemPath(Uri)` → REACHABLE SOURCE** and
   **row 29 `FileSystemFacadeImpl.makeFileSystemPath(Uri,String)` → REACHABLE SOURCE.**
   Fresh `TorrentSessionImpl.java` L341 (`fs.makeFileSystemPath(params.downloadPath)`)
   and L407 (`fs.makeFileSystemPath(torrent.downloadPath)`) call the 1-arg overload;
   fresh `TorrentDownloadImpl.java` L1229 (`fs.makeFileSystemPath(path)`) calls it too.
   The 1-arg overload delegates to the 2-arg overload at `FSFI` L250
   (`return makeFileSystemPath(uri, null)`), so row 29 is reached by a printed internal
   call from a reachable method — SOURCE under the per-row convention (a printed line
   names the method). This also flips row 2 above and batch-55 row 30 (SAF module side).
10. **Row 30 `FileSystemFacadeImpl.makeTempFile` → REACHABLE SOURCE.**
    Fresh `AddTorrentViewModel.java` L253: `File httpTmp = v.fs.makeTempFile(".torrent")`.
11. **Row 31 `FileSystemFacadeImpl.normalizeFileSystemPath` → REACHABLE SOURCE.**
    Fresh `Utils.java` L646: `Uri.parse(fs.normalizeFileSystemPath(path))`; also fresh
    `AddTorrentViewModel.java` L259: `v.fs.normalizeFileSystemPath(httpTmp.getAbsolutePath())`.
12. **Row 40 `SafFileSystem.exists(Uri)` → REACHABLE INFERRED.**
    Via row 13: `FSFI.fileExists` → `SFM.fileExists` L136–139 → `SFS.exists` L330–341;
    SAF-path gate applies (resolver L43 selects the SAF module for SAF URIs). Module
    dispatch is INFERRED, consistent with row 39 (`SFS.delete`) in Agent 16's convention.


## Flips in this open-close pass (2026-11-01 — all five OPEN → REACHABLE SOURCE)

1. **Row 9 `buildValidFatFilename`:** fresh `FileManagerViewModel.createFile` L248–253 calls
   `fs.buildValidFatFilename(fileName)` (L253, inside `appendExtension(...)`); `createFile`
   is called by `FileManagerDialog.createFile` L570–583 (`viewModel.createFile(fileName)`
   L583, from dialog branches L348/L508); the dialog ViewModel is obtained L135–140.
   The old "only printed caller is isValidFatFilename" claim is superseded: `isValidFatFilename`
   L332–334 *calls* buildValidFatFilename, it is not a route into it from outside, and the
   new caller is a direct printed call. (Batch-4 row 15 unchanged — see revision note.)
2. **Row 18 `getExtensionSeparator`:** fresh `FileManagerViewModel.appendExtension`
   L229–243 calls `fs.getExtensionSeparator()` (L243); `appendExtension` is called from
   `fileExists` L224 and `createFile` L253, and `createFile` by `FileManagerDialog` L583
   as in (1). Row 17's field-direct read is now irrelevant: a direct caller is printed.
3. **Row 27 `isValidFatFilenameChar`:** printed internal call from reachable
   `buildValidFatFilename` L351 (row 9, flipped in this pass) — SOURCE under the per-row
   convention (printed internal call from a reachable method, as rows 24/29).
4. **Row 32 `trimFilename`:** printed internal call from reachable `buildValidFatFilename`
   L360 (row 9, flipped in this pass) — SOURCE on the same ground as row 27.
5. **Row 33 `write(CharSequence,Charset,Uri)`:** fresh chain `FeedActivity.backupFeeds`
   L346–357 → `viewModel.saveFeedsSync(file)` L349 → `FeedViewModel.saveFeedsSync`
   L135–137 → `repo.serializeAllFeeds(file)` → `FeedRepositoryImpl.serializeAllFeeds`
   L144–147 → facade `.write(String, StandardCharsets.UTF_8, file)` L147, i.e. this
   overload (CharSequence, Charset, Uri), not the byte[] overload (row 34, TE L984).

## Strict-entry caveat (explicit)

Every REACHABLE route below is anchored at `TorrentService` → `TorrentEngine`, at a settings
fragment, at `TorrentRepositoryImpl`, or at a ViewModel/Activity/IPFilterParser call site
freshly printed in this pass. The launcher-to-service step, the fragment-attachment steps,
and the callers of the `TorrentRepositoryImpl` methods themselves were NOT freshly printed
in this pass, so under a strict launcher-entry rule all REACHABLE rows revert to OPEN.
Rows 37–39 additionally require the SAF-path gate (STATE data: the URI is a SAF path, so the
resolver's L43 branch selects the SAF module); on a file-system URI the same facade calls run
the `DefaultFsModule` branch instead (batch 53).

## Undecided conventions recorded per row, NOT decided

- **`confirmed_by` convention:** SOURCE = a printed direct app-to-app call site naming the
  method (including a printed internal call from a reachable method in the same class, as
  rows 24 and 29); INFERRED = reached only through unprinted framework/library/generated
  dispatch (FsModule interface dispatch, JVM class initialisation, try-with-resources
  compiler dispatch) where the registration or dispatch code is printed. This is the
  per-row convention, not the whole-route convention used in some earlier batches; labels
  are unaffected, only `confirmed_by` would change at merge under the whole-route convention.
  Note: batch 55's proposal used SOURCE for SafFsModule rows reached via the same facade
  calls; this file keeps Agent 16's INFERRED for the analogous `SafFileSystem` rows (37–40)
  — the merger must pick one convention for module-dispatch rows across batches 53–55.
- **`buildValidFatFilename` group (rows 9, 27, 32) — RESOLVED in open-close pass 2026-11-01:**
  rows 9, 27, 32 are now REACHABLE SOURCE on fresh printed callers (see "Flips in this
  open-close pass"). The batch-4 graph claim for `isValidFatFilename` is a different method
  and was not relied on for these flips; batch-4 row 15 is unchanged (see revision note).

## Per-row verdicts

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 1 | `DefaultFsModule.getParentDirUri` | REACHABLE | INFERRED | **FLIPPED in this pass.** Def `DFM` L127–132. Dispatcher: `FSFI.getParentDirUri` (row 23), freshly called by `CreateTorrentViewModel` L357. File-URI branch INFERRED. |
| 2 | `DefaultFsModule.makeFileSystemPath` | REACHABLE | INFERRED | **FLIPPED in this pass.** Def `DFM` L121–124. Dispatcher: `FSFI.makeFileSystemPath(Uri,String)` (row 29) L259; facade reachable via `TorrentSessionImpl` L341/:407 and `TorrentDownloadImpl` L1229 (all fresh). Module dispatch INFERRED. |
| 3 | `DefaultFsModule.openFD` | REACHABLE | INFERRED | Def `DFM` L85–88 `return new FileDescriptorWrapperImpl(appContext, path)`. Dispatcher: `FSFI.getFD` L60–65 calls `fsModule.openFD(path)` L64; facade reachable via `TE` L380 (local copy). File-URI branch INFERRED. |
| 4 | `FileDescriptorWrapperImpl.<init>` | REACHABLE | SOURCE | Def `FDWI` L39–43. Constructed by `DFM.openFD` L87 and by `SFM.openFD` L94; both modules are reached via `FSFI.getFD` (row 19, via `TE` L380 local copy). |
| 5 | `FileDescriptorWrapperImpl.close` | REACHABLE | INFERRED | Def `FDWI` L54–58. No printed source line names `close()`; it runs via Java try-with-resources: `FSFI.write` L224 and L236 (`try (FileDescriptorWrapper w = getFD(destFile))`) and `TE` L380 (local copy, `try (FileDescriptorWrapper w = fs.getFD(file))`) generate the close call on block exit. Compiler dispatch, hence INFERRED, not SOURCE. |
| 6 | `FileDescriptorWrapperImpl.open` | REACHABLE | SOURCE | Def `FDWI` L46–51. Called by `FSFI.write(byte[])` L225 and `FSFI.write(CharSequence)` L237 (`w.open("rw")`), and by `TE` L380–381 (local copy, `w.open("r")` on the wrapper from `fs.getFD`). The `FSFI.write(byte[])` chain alone anchors it via `TE` L980–984 (local copy). |
| 7 | `FileSystemFacadeImpl.<clinit>` | REACHABLE | INFERRED | Static fields `FSFI` L44–47 (`TAG`, `EXTENSION_SEPARATOR`, `TEMP_DIR`). JVM class initialisation runs on first use of the class; first construction is printed (`SFH` L41–42, called by Storage L89, Network L109, `TE` L132 local copy). JVM dispatch, hence INFERRED. |
| 8 | `FileSystemFacadeImpl.<init>` | REACHABLE | SOURCE | Def `FSFI` L52–57. Constructed by `SFH.getFileSystemFacade` L41–42; helper called by Storage fragment L89, Network fragment L109, `TE` L132 (local copy). |
| 9 | `FileSystemFacadeImpl.buildValidFatFilename` | REACHABLE | SOURCE | **FLIPPED in this open-close pass (2026-11-01).** Def `FSFI` L343–363 (fresh print). Fresh caller: `FileManagerViewModel.createFile` L248–253 calls `fs.buildValidFatFilename(fileName)` (L253); `createFile` called by `FileManagerDialog.createFile` L570–583 (`viewModel.createFile(fileName)` L583). Batch-4 row 15 (`isValidFatFilename`) NOT flipped by this — different method, caller still missing. |
| 10 | `FileSystemFacadeImpl.cleanTempDir` | REACHABLE | SOURCE | Def `FSFI` L296–303. Called by `TE.cleanTemp` L1225 (local copy) `fs.cleanTempDir()`. |
| 11 | `FileSystemFacadeImpl.createFile` | REACHABLE | SOURCE | Def `FSFI` L199–218. Called by `TE.saveTorrentFile` L980 (local copy) `fs.createFile(destDir, name, true)`. |
| 12 | `FileSystemFacadeImpl.deleteFile` | REACHABLE | SOURCE | Def `FSFI` L110–115. Called by `TE` L1154 (local copy) `fs.deleteFile(uri)` (watch-dir delete branch). |
| 13 | `FileSystemFacadeImpl.fileExists` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L153–158. Fresh `IPFilterParser.parseFile` L63 `fs.fileExists(path)`. Flips together with batch-53 row 35 and row 40 below on the same facade call. |
| 14 | `FileSystemFacadeImpl.getDefaultDownloadPath` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L80–90. Fresh `Utils.java` L644 `fs.getDefaultDownloadPath()`. |
| 15 | `FileSystemFacadeImpl.getDirAvailableBytes` | REACHABLE | SOURCE | Def `FSFI` L268–282. Called by `TE` L1200 (local copy) `fs.getDirAvailableBytes(downloadPath)`. |
| 16 | `FileSystemFacadeImpl.getDirPath` | REACHABLE | SOURCE | Def `FSFI` L418–423. Called by Storage fragment `onCreate` L99 (also L126, L153, L180, L271). |
| 17 | `FileSystemFacadeImpl.getExtension` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L312–325. Fresh `DetailTorrentViewModel.java` L399 `fs.getExtension(fileName)` (in `makeOpenFileIntent`). |
| 18 | `FileSystemFacadeImpl.getExtensionSeparator` | REACHABLE | SOURCE | **FLIPPED in this open-close pass (2026-11-01).** Def `FSFI` L68–71 (fresh print). Fresh caller: `FileManagerViewModel.appendExtension` L229–243 calls `fs.getExtensionSeparator()` (L243); `appendExtension` called from `fileExists` L224 and `createFile` L253, `createFile` by `FileManagerDialog` L583. |
| 19 | `FileSystemFacadeImpl.getFD` | REACHABLE | SOURCE | Def `FSFI` L60–65. Called by `TE` L380 (local copy) `fs.getFD(file)`, and internally by both `FSFI.write` overloads (L224, L236). |
| 20 | `FileSystemFacadeImpl.getFilePath` | REACHABLE | SOURCE | Def `FSFI` L430–435. Called by Network fragment L208 and L396. |
| 21 | `FileSystemFacadeImpl.getFileUri(Uri,String)` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L122–136. Fresh `TorrentDownloadImpl.java` L1299 `fs.getFileUri(torrent.downloadPath, "." + ti.infoHash() + ".parts")`. (`FSFI.createFile` calls the *module* method directly at L205/L213, not this facade method — that was Agent 16's only printed chain; this row has its own facade caller.) |
| 22 | `FileSystemFacadeImpl.getFileUri(String,Uri)` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L144–150. Fresh `DetailTorrentViewModel.java` L275 `fs.getFileUri(relativePath, torrent.downloadPath)`. Flips together with batch-53 row 40 on the same facade call. |
| 23 | `FileSystemFacadeImpl.getParentDirUri` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L438–443. Fresh `CreateTorrentViewModel.java` L357 `fs.getParentDirUri(seedPath)`. |
| 24 | `FileSystemFacadeImpl.getTempDir` | REACHABLE | SOURCE | Def `FSFI` L285–293. Called internally by `FSFI.cleanTempDir` L298 and by `FSFI.makeTempFile` L308; `cleanTempDir` is reachable via `TE` L1225 (local copy), so this internal call anchors it. |
| 25 | `FileSystemFacadeImpl.getUserDirPath` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L98–107. Fresh `FeedActivity.java` L266 and L282 `new FileManagerConfig(fs.getUserDirPath(), ...)`. |
| 26 | `FileSystemFacadeImpl.isStorageReadable` | REACHABLE | SOURCE | Def `FSFI` L185–191. Called by `TRI.getSessionFile` L110 and `TRI.getTorrentDataDir` L146 via the `SFH` facade singleton. Trunk caveat: the callers of those repository methods were not freshly printed in this pass (see Strict-entry caveat). |
| 27 | `FileSystemFacadeImpl.isValidFatFilenameChar` | REACHABLE | SOURCE | **FLIPPED in this open-close pass (2026-11-01).** Def `FSFI` L365–384 (private, fresh print). Printed internal call from reachable `buildValidFatFilename` L351 (row 9, flipped in this pass) — SOURCE under the per-row convention (printed internal call from a reachable method). |
| 28 | `FileSystemFacadeImpl.makeFileSystemPath(Uri)` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L248–251 (delegates to the 2-arg overload at L250). Fresh `TorrentSessionImpl.java` L341 and L407, and fresh `TorrentDownloadImpl.java` L1229, all call the 1-arg overload. |
| 29 | `FileSystemFacadeImpl.makeFileSystemPath(Uri,String)` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L254–260. Reached by printed internal call `FSFI` L250 from row 28 (reachable, fresh callers above). Also dispatches to the module method at L259 (row 2 / batch-55 row 30). |
| 30 | `FileSystemFacadeImpl.makeTempFile` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L306–309 (calls `getTempDir` L308, row 24). Fresh `AddTorrentViewModel.java` L253 `v.fs.makeTempFile(".torrent")`. |
| 31 | `FileSystemFacadeImpl.normalizeFileSystemPath` | REACHABLE | SOURCE | **FLIPPED in this pass.** Def `FSFI` L404–411. Fresh `Utils.java` L646 `fs.normalizeFileSystemPath(path)` and fresh `AddTorrentViewModel.java` L259 `v.fs.normalizeFileSystemPath(httpTmp.getAbsolutePath())`. |
| 32 | `FileSystemFacadeImpl.trimFilename` | REACHABLE | SOURCE | **FLIPPED in this open-close pass (2026-11-01).** Def `FSFI` L386–397 (private, fresh print). Printed internal call from reachable `buildValidFatFilename` L360 (row 9, flipped in this pass) — SOURCE on the same ground as row 27. |
| 33 | `FileSystemFacadeImpl.write(CharSequence,Charset,Uri)` | REACHABLE | SOURCE | **FLIPPED in this open-close pass (2026-11-01).** Def `FSFI` L232–241 (fresh print). Fresh chain: `FeedActivity.backupFeeds` L346–357 → `viewModel.saveFeedsSync(file)` L349 → `FeedViewModel.saveFeedsSync` L135–137 → `repo.serializeAllFeeds(file)` → `FeedRepositoryImpl.serializeAllFeeds` L144–147 → facade `.write(String, UTF_8, file)` L147, i.e. this overload, not the byte[] overload (row 34). |
| 34 | `FileSystemFacadeImpl.write(byte[],Uri)` | REACHABLE | SOURCE | Def `FSFI` L221–229. Called by `TE.saveTorrentFile` L984 (local copy) `fs.write(bencode, path)` with `byte[] bencode` (L974). |
| 35 | `FsModuleResolverImpl.<init>` | REACHABLE | SOURCE | Def `FMRI` L35–39 (constructs `SafFsModule` L37, `DefaultFsModule` L38). Constructed by `SFH.getFileSystemFacade` L41–42; helper called by Storage L89, Network L109, `TE` L132 (local copy). |
| 36 | `FsModuleResolverImpl.resolveFsByUri` | REACHABLE | SOURCE | Def `FMRI` L42–50. Called by every `FSFI` dispatch method, including reachable ones: `getFD` L62, `deleteFile` L112, `createFile` L203, `getDirAvailableBytes` L272, `getDirPath` L420, `getFilePath` L432. |
| 37 | `SafFileSystem.<clinit>` | REACHABLE | INFERRED | Static fields `SFS` L66 (`CACHE_MAX_SIZE`), L68 (`INSTANCE`), L70 (`CACHE`). JVM class initialisation on first use; first use is printed via `SFM` methods calling `SFS.getInstance` (e.g. `SFM.delete` L86, `SFM.fileExists` L138), reached through the SAF branch of `FMRI.resolveFsByUri` (L43) from reachable facade methods (`deleteFile`, `getFD`). SAF-path gate applies. |
| 38 | `SafFileSystem.<init>` | REACHABLE | INFERRED | Def `SFS` L84–87, private. Called only by `SFS.getInstance` L77; `getInstance` called by `SFM.delete` L86 and `SFM.fileExists` L138, reached via the SAF branch from reachable facade `deleteFile` (via `TE` L1154, local copy). SAF-path gate applies. |
| 39 | `SafFileSystem.delete(Uri)` | REACHABLE | INFERRED | Def `SFS` L310–313. Called by `SFM.delete` L86–88 (`fs.delete(filePath)`); `SFM.delete` runs via `FSFI.deleteFile` L114 interface dispatch; facade reachable via `TE` L1154 (local copy). SAF-path gate applies (resolver L43 selects the SAF module for SAF URIs). |
| 40 | `SafFileSystem.exists(Uri)` | REACHABLE | INFERRED | **FLIPPED in this pass.** Def `SFS` L330–341. Via row 13: fresh `IPFilterParser.parseFile` L63 → `FSFI.fileExists` → `SFM.fileExists` L136–139 → `SFS.exists`. SAF-path gate applies. Flips together with row 13 and batch-53 row 35 on the same facade call. |

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order, method names and JVM descriptors matching
  the plan copy row for row.**
- **40 REACHABLE proposed / 0 UNREACHABLE / 0 OPEN (after open-close pass 2026-11-01; was 35/0/5).**
- REACHABLE rows: 1–40 (all).
  Of these: SOURCE 31 / INFERRED 9.
- OPEN rows: none.
- **0 rows verified for merge.** No UNREACHABLE is claimed: no saved full-repo grep was run
  in this pass, and absence from the printed subset is not evidence of absence.

## What the merger still needs

1. ~~Saved full-repo grep for the 5 former OPEN rows~~ — DONE in open-close pass 2026-11-01
   by printed callers, not by grep; no OPEN rows remain in this batch.
2. ~~Fresh branch re-print of `TorrentEngine.java`~~ — DONE in open-close pass 2026-11-01
   (fresh print SHA 17d06efe…, 1659 lines; TE lines verified identical to the local-copy
   lines cited above).
3. Printed launcher-to-`TorrentService` step, fragment-attachment steps, and
   `TorrentRepositoryImpl` callers if the strict-entry rule is applied.
4. Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
