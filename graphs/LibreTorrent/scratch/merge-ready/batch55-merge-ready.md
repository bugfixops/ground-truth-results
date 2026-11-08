**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 55 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.
No connector `search_code` 0-result was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 55 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Prior work (Agent 17 proposal) was used as an INPUT / lead list only; every row below was
  re-judged against printed source, and the two OPEN rows were FLIPPED from that proposal on
  evidence freshly printed in this pass (rows 7 and 29 — see "Flips in this pass").
  All other rows carry the Agent 17 verdicts, re-checked against the same printed citations.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 55 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order.

## Printed source used

Base path (omitted in citations):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Fresh connector fetches in THIS pass, branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b5354-55-src/` (no fresh HTTP 429 hit in this pass):
- `ui/createtorrent/CreateTorrentViewModel.java` — full, fresh (closes rows 7 and 29).
- `core/model/session/IPFilterParser.java` — full, 270 lines, fresh (confirms row 22's
  facade chain: `parseFile` L63 `fs.fileExists(path)`).
- `ui/detailtorrent/DetailTorrentViewModel.java` — full, fresh (confirms rows 25, 28 and
  the facade chains for rows 4, 5, 24, 30 via `getDirPath`/`getFileUri`/`getDirAvailableBytes`
  call sites at :275, :358, :453–454 in the Agent 17 local copies — the fresh file's
  `getFileUri` call at :275 matches the local copies exactly).

Re-read from prior passes, flagged as such (Agent 17 printed these in full in its pass;
not freshly re-fetched in this pass except where noted above):
- `core/system/SafFileSystem.java` (549 lines), `core/system/SafFsModule.java` (162 lines),
  `core/system/SystemFacadeHelper.java` (47 lines), `core/system/SystemFacadeImpl.java`
  (84 lines), `core/system/FileSystemFacadeImpl.java` (444 lines),
  `core/system/FsModuleResolverImpl.java` (51 lines),
  `core/urlnormalizer/NormalizeUrl.java` (423 lines; only its `<clinit>` and `doNormalize`
  rows are in this batch).
- Local printed copies consulted for callers in the Agent 17 pass, NOT freshly re-fetched
  in this pass: `TorrentEngine.java` (TorrentService-anchored route from batches 19–23),
  `TorrentSessionImpl.java`, `TorrentDownloadImpl.java` (but see fresh fetches above for
  `TorrentDownloadImpl` — its `getFileUri` L1299 and `makeFileSystemPath` L1229 were freshly
  printed in this pass and match the Agent 17 local-copy lines), `AddTorrentViewModel.java`
  (but see fresh fetch above for its `makeTempFile`/`normalizeFileSystemPath` lines),
  `DetailTorrentViewModel.java` (fresh above), `SaveLogWorker.java`, `IPFilterParser.java`
  (fresh above), `MainActivity.java`, `Utils.java` (but see fresh fetch above for
  `Utils` L644/L646). Caller line numbers from any remaining local-only copy are flagged
  "local copy" in the table; the merger must re-check those lines against the branch at merge.
  No label in this batch rests solely on an unflagged local-copy line: the two flipped rows
  rest on a freshly printed caller, and every other row's definition and immediate dispatch
  were printed in the Agent 17 pass.

## Shared route / dispatch (applies to most rows below)

1. **Service anchor (from prior batches, not freshly re-printed here).**
   `TorrentService.onCreate` gets `TorrentEngine.getInstance`;
   `TorrentEngine.<init>` (local copy) calls `SystemFacadeHelper.getFileSystemFacade(appContext)`
   (:132) and `SystemFacadeHelper.getSystemFacade(appContext)` (:138).
2. **Facade dispatch (printed in the Agent 17 pass).**
   `SystemFacadeHelper.getFileSystemFacade` (:39–46) builds `FileSystemFacadeImpl` with
   `FsModuleResolverImpl` (:42–43). `FsModuleResolverImpl.resolveFsByUri` (:42–49): if
   `Utils.isSafPath(appContext, uri)` return the `SafFsModule` (constructed :37); else if
   file-system path return the default module; else throw `UnknownUriException`.
   `Utils.isSafPath` (local copy :657–658) is `SafFileSystem.getInstance(appContext).isSafPath(path)`.
3. **SAF-branch condition.** Every `SafFsModule`/`SafFileSystem` row below runs only when the
   uri passed through the facade is a SAF (content-scheme) uri, so the resolver picks
   `safModule`. That is a data condition on the caller's uri (e.g. a user-chosen SAF
   download dir), not a separate gate in the graph sense; it is noted on each row as
   "SAF branch". The interface dispatch `FileSystemFacadeImpl` → `FsModule` is printed code,
   so the Agent 17 proposal marked SafFsModule rows SOURCE; this file RETAINS that
   convention for batch 55 (see "Undecided conventions") — it differs from batches 53–54,
   where the analogous module-dispatch rows are INFERRED, and the merger must pick one
   convention across batches 53–55. Labels are unaffected by that choice.

## Flips in this pass (vs Agent 17 proposal — both OPEN → REACHABLE SOURCE)

1. **Row 7 `SafFileSystem.getParentDirUri` → REACHABLE SOURCE** and
   **row 29 `SafFsModule.getParentDirUri` → REACHABLE SOURCE.**
   Fresh `CreateTorrentViewModel.java` L357: `savePath = fs.getParentDirUri(seedPath)`.
   Chain: `FileSystemFacadeImpl.getParentDirUri` L438–442 → `fsModule.getParentDirUri(filePath)`
   (L442) → `SafFsModule.getParentDirUri` L158–161 →
   `SafFileSystem.getInstance(appContext).getParentDirUri(filePath)` (L160) →
   `SafFileSystem.getParentDirUri` L533–548. The SAF branch applies (resolver L43);
   the file-URI branch runs `DefaultFsModule.getParentDirUri` instead (batch 54 row 1,
   same facade call, flipped in that file). This also flips batch-54 rows 1 and 23
   (facade and file-URI sides) on the same facade call. Agent 17's "no printed caller of
   the facade method in the local corpus" is superseded by this freshly printed caller;
   the rows are NOT flipped on a grep — they are flipped on a printed call site.

## Strict-entry caveat (explicit)

All routes above anchor at `TorrentService`/`TorrentEngine` or at ViewModel/`Utils` call
sites; the launcher entry itself and the launcher-to-`TorrentService` step were not freshly
re-printed in this pass, so under a strict launcher-entry rule all REACHABLE rows revert
to OPEN. The `TorrentService` → `TorrentEngine` step and the settings-fragment attachment
steps are the same caveat carried from batches 53–54.

## Undecided conventions recorded per row, NOT decided

- **`confirmed_by` convention (batch 55):** SOURCE = a printed direct app-to-app call site
  naming the method, including a printed module-code call naming a `SafFileSystem` method
  and a printed facade call naming a `SafFsModule` method's facade counterpart; INFERRED =
  reached only through unprinted framework/JVM dispatch (`NormalizeUrl.<clinit>`, JVM class
  initialisation). This RETAINS the Agent 17 convention for this batch. It DIFFERS from
  batches 53–54 in this pass, where module-dispatch rows are INFERRED: e.g. batch-54 row 40
  (`SafFileSystem.exists`) is INFERRED in its file, while the analogous batch-55 row 22
  (`SafFsModule.fileExists`) is SOURCE here. The merger must pick one convention for
  module-dispatch rows across batches 53–55; labels do not change either way.
- **SAF-branch data condition:** noted per row as "SAF branch"; it is a URI-type condition
  on the caller's data, not a project gate decision, and it does not close any row.
- **`Utils`-trigger note (rows 35, 37, 38):** `Utils`'s own entry trigger was not freshly
  re-printed in this pass; these rows are proposed REACHABLE on the printed `Utils` call
  sites (local copies), same convention as other batches. Merger re-print `Utils` call sites
  if a fresh trunk anchor is required.

## Per-row verdicts

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | SafFileSystem.getDir(DocumentFile,String,boolean) | REACHABLE | SOURCE | Private (:291–303). Called from `SafFileSystem.getFile(FakePath,boolean)` :277 and :279 (last-node fallback / intermediate dirs). Chain: facade `getFileUri(String,Uri)` → SafFsModule :77–80 → `getFileUri(FakePath)` → `getFile(FakePath)` :240 → here. SAF branch. |
| 2 | SafFileSystem.getFile(DocumentFile,String,boolean) | REACHABLE | SOURCE | Private (:248–260). Called from `getFileUri(Uri,String,boolean)` :216 and from `getFile(FakePath)` :274. Chains via SafFsModule `getFileUri` overloads (rows 27/28). SAF branch. |
| 3 | SafFileSystem.getFile(FakePath,boolean) | REACHABLE | SOURCE | Private (:262–289). Called from `getFileUri(FakePath,boolean)` :240. Chain: facade `getFileUri(String,Uri)` → SafFsModule :77–80 → `getFileUri(FakePath)` :235 → here. SAF branch. |
| 4 | SafFileSystem.getFileUri(Uri,String,boolean) | REACHABLE | SOURCE | :207–222. Called from SafFsModule `getFileUri(Uri,String,boolean)` :71–74, which is called from `FileSystemFacadeImpl.getFileUri(Uri,String)` :122–129 and `createFile` :205/:213. Facade callers printed in local copies: `TorrentDownloadImpl` `fs.getFileUri(torrent.downloadPath, ".parts")` (:1299) — CONFIRMED FRESH in this pass (`TorrentDownloadImpl.java` L1299, same line) — and `TorrentEngine` `fs.createFile(destDir, name, true)` (:980, local copy). SAF branch. |
| 5 | SafFileSystem.getFileUri(FakePath,boolean) | REACHABLE | SOURCE | :235–246. Called from SafFsModule `getFileUri(String,Uri)` :77–80, called from `FileSystemFacadeImpl.getFileUri(String,Uri)` :144–149, called from `DetailTorrentViewModel` `fs.getFileUri(relativePath, torrent.downloadPath)` (:275) — CONFIRMED FRESH in this pass (`DetailTorrentViewModel.java` L275, same line). SAF branch. |
| 6 | SafFileSystem.getInstance(Context) | REACHABLE | SOURCE | :72–82. Called from `Utils.isSafPath` (local copy :658), from every SafFsModule method below, and from `FsModuleResolverImpl`'s SAF test chain. Any facade call triggers the resolver → `isSafPath` → here. |
| 7 | SafFileSystem.getParentDirUri(Uri) | REACHABLE | SOURCE | **FLIPPED in this pass.** :533–548. Fresh `CreateTorrentViewModel.java` L357 `fs.getParentDirUri(seedPath)` → facade `getParentDirUri` :438–442 → SafFsModule :158–161 → here (L160). SAF branch; file-URI branch is batch-54 row 1. |
| 8 | SafFileSystem.isSafPath(Uri) | REACHABLE | SOURCE | :191–198. Called from `Utils.isSafPath` (local copy :657–658), called from `FsModuleResolverImpl.resolveFsByUri` :43 — i.e. on every `FileSystemFacadeImpl` call (e.g. `TorrentEngine.<init>` facade acquisition, local copy :132). |
| 9 | SafFileSystem.makeSafRootDir(Uri) | REACHABLE | SOURCE | :369–373. Called from SafFsModule `getDirAvailableBytes` :103, called from `FileSystemFacadeImpl.getDirAvailableBytes` :268–274, called from `TorrentEngine` (:1200, local copy), `AddTorrentViewModel` (:357), `DetailTorrentViewModel` (:453), `TorrentDownloadImpl` (:415) — local copies. SAF branch. |
| 10 | SafFileSystem.stat(Uri) | REACHABLE | SOURCE | :459–470. Called from SafFsModule `getName` :49 and `getFilePath` :65. `getFilePath` chain: `FileSystemFacadeImpl.getFilePath` :430–434 ← `SaveLogWorker` `fs.getFilePath(filePath)` (:97, local copy). SAF branch. |
| 11 | SafFileSystem.stat(DocumentFile) | REACHABLE | SOURCE | Private (:487–493). Called from `stat(Uri)` :469, `stat(Uri,String)` :439, `statSafRoot` :454, `stat(FakePath)` :484. Inherits row 10/12 routes. |
| 12 | SafFileSystem.statSafRoot(Uri) | REACHABLE | SOURCE | :444–455. Called from SafFsModule `getDirPath` :57, called from `FileSystemFacadeImpl.getDirPath` :418–422, called from `AddTorrentViewModel` `fs.getDirPath(dirPath)` (:358) and `DetailTorrentViewModel` (:454) — local copies. SAF branch. |
| 13 | SafFileSystem$FakePath.<init>(Uri,String) | REACHABLE | SOURCE | :98–102 (calls `normalizeRelativePath` :101). Called from SafFsModule `getFileUri(String,Uri)` :80 and `makeFileSystemPath` :153. `makeFileSystemPath` chain: `FileSystemFacadeImpl.makeFileSystemPath` :254–259 ← `TorrentSessionImpl` (:341, :407) and `TorrentDownloadImpl` (:1229) — the latter CONFIRMED FRESH in this pass (`TorrentDownloadImpl.java` L1229, same line); `TorrentSessionImpl` lines are local copies. |
| 14 | SafFileSystem$FakePath.makeRelativePathNodes() | REACHABLE | SOURCE | :140–145. Called from `getFile(FakePath)` :268, `exists(FakePath)` :355, `mkdirs` :516 — all reached via the row 5 / facade chains above. |
| 15 | SafFileSystem$FakePath.normalizeRelativePath(String) | REACHABLE | SOURCE | Private (:104–110). Called from `FakePath.<init>` :101 — inherits row 13 route. |
| 16 | SafFileSystem$FakePath.safRoot() | REACHABLE | SOURCE | :147–150. Called from `getFile(FakePath)` :264, `exists(FakePath)` :351, `mkdirs` :512 — inherits row 5 chain. |
| 17 | SafFileSystem$FakePath.serialize() | REACHABLE | SOURCE | Private (:132–138). Called only from `toString` :166 — inherits row 18 route. |
| 18 | SafFileSystem$FakePath.toString() | REACHABLE | SOURCE | :164–167 (calls `serialize()` :166). Called from `getFileUri(FakePath)` :237 (cache key), `exists(FakePath)` :346, `mkdirs` :507, `stat(FakePath)` :476, and SafFsModule `makeFileSystemPath` :153–154 (row 30 chain). |
| 19 | SafFileSystem$Stat.<init>(String,boolean,long,long) | REACHABLE | SOURCE | :177–184. Called from `stat(DocumentFile)` :491–492 — inherits rows 10–12 routes. |
| 20 | SafFsModule.<init>(Context) | REACHABLE | SOURCE | :40–43. Called from `FsModuleResolverImpl.<init>` :37, called from `SystemFacadeHelper.getFileSystemFacade` :42–43 — inherits row 32 route. |
| 21 | SafFsModule.delete(Uri) | REACHABLE | SOURCE | :84–89 (delegates to `SafFileSystem.delete(Uri)` :310). Called from `FileSystemFacadeImpl.deleteFile` :110–114, called from `TorrentSessionImpl` `fs.deleteFile(...)` (:318), `TorrentDownloadImpl` (:465), `TorrentEngine` (:1154) — all local copies. SAF branch. |
| 22 | SafFsModule.fileExists(Uri) | REACHABLE | SOURCE | :136–139 (delegates to `SafFileSystem.exists(Uri)` :330). Called from `FileSystemFacadeImpl.fileExists` :153–157, called from `IPFilterParser` `fs.fileExists(path)` (:63) — CONFIRMED FRESH in this pass (`IPFilterParser.java` L63, same line). SAF branch. (Batch-54 row 40, the `SafFileSystem.exists` side of this call, is INFERRED in its file under that batch's convention — see "Undecided conventions".) |
| 23 | SafFsModule.getAvailableBytes(FileDescriptor) | REACHABLE | SOURCE | Private (:124–133, `Os.fstatvfs`). Called from `getDirAvailableBytes` :109 — inherits row 24 route. |
| 24 | SafFsModule.getDirAvailableBytes(Uri) | REACHABLE | SOURCE | :98–114 (calls `makeSafRootDir` :103 and `getAvailableBytes` :109). Called from `FileSystemFacadeImpl.getDirAvailableBytes` :268–274 ← `TorrentEngine` :1200, `AddTorrentViewModel` :357, `DetailTorrentViewModel` :453, `TorrentDownloadImpl` :415 (local copies). SAF branch. |
| 25 | SafFsModule.getDirPath(Uri) | REACHABLE | SOURCE | :55–60 (calls `statSafRoot` :57). Called from `FileSystemFacadeImpl.getDirPath` :418–422 ← `AddTorrentViewModel` :358, `DetailTorrentViewModel` :454 — local copies. SAF branch. |
| 26 | SafFsModule.getFilePath(Uri) | REACHABLE | SOURCE | :63–68 (calls `stat(Uri)` :65). Called from `FileSystemFacadeImpl.getFilePath` :430–434 ← `SaveLogWorker` :97 (local copy). SAF branch. |
| 27 | SafFsModule.getFileUri(Uri,String,boolean) | REACHABLE | SOURCE | :71–74. Called from `FileSystemFacadeImpl.getFileUri(Uri,String)` :122–129 and `createFile` :205/:213 — facade callers as row 4, including fresh `TorrentDownloadImpl.java` L1299. SAF branch. |
| 28 | SafFsModule.getFileUri(String,Uri) | REACHABLE | SOURCE | :77–81 (builds `FakePath` :80). Called from `FileSystemFacadeImpl.getFileUri(String,Uri)` :144–149 ← `DetailTorrentViewModel` :275 — CONFIRMED FRESH in this pass. SAF branch. |
| 29 | SafFsModule.getParentDirUri(Uri) | REACHABLE | SOURCE | **FLIPPED in this pass.** :158–161. Fresh `CreateTorrentViewModel.java` L357 `fs.getParentDirUri(seedPath)` → facade :438–442 → here → `SafFileSystem.getParentDirUri` (row 7). SAF branch; file-URI branch is batch-54 row 1. |
| 30 | SafFsModule.makeFileSystemPath(Uri,String) | REACHABLE | SOURCE | :151–155 (builds `FakePath` :153, calls `toString` :154). Called from `FileSystemFacadeImpl.makeFileSystemPath` :254–259 ← `TorrentSessionImpl` :341/:407, `TorrentDownloadImpl` :1229 — the latter CONFIRMED FRESH in this pass. SAF branch. |
| 31 | SafFsModule.openFD(Uri) | REACHABLE | SOURCE | :92–95 (returns `FileDescriptorWrapperImpl`). Called from `FileSystemFacadeImpl.getFD` :60–64 ← `TorrentEngine` :380, `TorrentSessionImpl` :296/:360, `SaveLogWorker` :89, `IPFilterParser` :72 — `IPFilterParser` CONFIRMED FRESH in this pass (`IPFilterParser.java` L72, `fs.getFD(path)` in `parseFile`'s try-with-resources); other callers are local copies. SAF branch. Note: this is distinct from `SafFileSystem.openFD` overloads (batch 4, not this batch). |
| 32 | SystemFacadeHelper.getFileSystemFacade(Context) | REACHABLE | SOURCE | :39–46. Called from `TorrentEngine.<init>` (:132), `AddTorrentViewModel` (:131), `SaveLogWorker` (:68), `DetailTorrentViewModel` (:110), `Utils.getTorrentDownloadPath` (:642) — all local copies. |
| 33 | SystemFacadeHelper.getSystemFacade(Context) | REACHABLE | SOURCE | :31–37 (builds `SystemFacadeImpl` :34). Called from `TorrentEngine.<init>` (:138), `MainActivity` (:784), `Utils` (:158, :165, :197, :205) — all local copies. |
| 34 | SystemFacadeImpl.<init>(Context) | REACHABLE | SOURCE | :38–41. Called from `SystemFacadeHelper.getSystemFacade` :34 — inherits row 33 route. |
| 35 | SystemFacadeImpl.getActiveNetworkInfo() | REACHABLE | SOURCE | :44–49. Called via the `SystemFacade` interface from `Utils.checkConnectivity` (:159), `isNetworkTypeAllowed` (:189), `isRoaming` (:211) — local copy. `Utils`'s own entry trigger was not re-printed in this pass; row is proposed REACHABLE on the printed Utils call sites, same convention as other batches. |
| 36 | SystemFacadeImpl.getAppVersionName() | REACHABLE | SOURCE | :72–83. Called from `MainActivity` `SystemFacadeHelper.getSystemFacade(...).getAppVersionName()` (:784–785) and `TorrentSessionImpl` `system.getAppVersionName()` (:887) — local copies. |
| 37 | SystemFacadeImpl.getNetworkCapabilities() | REACHABLE | SOURCE | :53–61. Called from `Utils.isNetworkTypeAllowed` (:174), `isMetered` (:199), `isRoaming` (:208) — local copy; same Utils-trigger note as row 35. |
| 38 | SystemFacadeImpl.isActiveNetworkMetered() | REACHABLE | SOURCE | :64–69. Called from `Utils.isNetworkTypeAllowed` (:183) and `isMetered` (:201) — local copy; same Utils-trigger note as row 35. |
| 39 | NormalizeUrl.<clinit>() | REACHABLE | INFERRED | Static block `NormalizeUrl.java:36–40` initialises `DEFAULT_PORT_LIST`. JVM class initialisation runs on first active use of the class; first printed use is `DetailTorrentFragment` `new NormalizeUrl.Options()` (:719, local copy) / `NormalizeUrl.normalize(...)` (:726). Dispatch is JVM, hence INFERRED, not SOURCE. |
| 40 | NormalizeUrl.doNormalize(String,Options) | REACHABLE | SOURCE | Private (`NormalizeUrl.java:191–302`). Called from `NormalizeUrl.normalize(String,Options)` :182, called from `DetailTorrentFragment` `NormalizeUrl.normalize(url, options)` (:726, local copy; options built :719 with only `decode=false` changed). |

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order, method names and JVM descriptors matching
  the plan copy row for row.**
- **40 REACHABLE proposed / 0 UNREACHABLE / 0 OPEN.**
- Of the REACHABLE rows: SOURCE 39 / INFERRED 1 (row 39 only).
- **0 rows verified for merge.** No UNREACHABLE is claimed: no saved full-repo grep was run
  in this pass, and absence from the printed subset is not evidence of absence.

## What is still owed before merge

- Re-check of the local-copy caller line numbers (TorrentEngine, TorrentSessionImpl,
  SaveLogWorker, MainActivity, Utils, DetailTorrentFragment, AddTorrentViewModel call sites
  not freshly fetched in this pass) against the branch at merge time. The two flipped rows
  do NOT depend on local copies — their caller (`CreateTorrentViewModel` L357) was freshly
  fetched in this pass.
- Printed launcher-to-`TorrentService` step (strict-entry caveat inherited from prior batches):
  all routes above anchor at `TorrentService`/`TorrentEngine` or at ViewModel/`Utils` call
  sites; the launcher entry itself was not freshly re-printed here.
- Merger's convention choice for module-dispatch `confirmed_by` across batches 53–55
  (SOURCE here for SafFsModule rows vs INFERRED in batches 53–54) — labels unaffected.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
