# Batch 55 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch55-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b5354-55-src/`, `~/workspace/ruleF-src/`,
  `~/workspace/overnight/stream-A/corpus/`). No connector fetch was needed; no 429; no missing file.
- Rows checked (10): sample 1, 6, 11, 16, 21, 26, 31, 36 + the two flips in this pass 7, 29.
- Batch Counts verified mechanically from the label column: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN.
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `SafFileSystem.getDir(DocumentFile,String,boolean)` | REACHABLE SOURCE | PASS | SafFileSystem.java:291 (private def); called from getFile(FakePath) at :277 and :279 (verified); chain via SafFsModule getFileUri(String,Uri) :77-80 → getFile(FakePath) :240. SAF branch correctly noted. |
| 6 `SafFileSystem.getInstance(Context)` | REACHABLE SOURCE | PASS | SafFileSystem.java:72-82 (def); Utils.java:658 `SafFileSystem.getInstance(appContext).isSafPath(path)`; SafFsModule methods delegate through it (e.g. :73, :160). SOURCE correct. |
| 7 `SafFileSystem.getParentDirUri(Uri)` | REACHABLE SOURCE | PASS | SafFileSystem.java:533 (def); fresh chain verified: CreateTorrentViewModel.java:357 `fs.getParentDirUri(seedPath)` → FileSystemFacadeImpl :438-442 → SafFsModule :158-161 → here (:160). The flip in this pass is justified; file-URI branch correctly assigned to batch-54 row 1. |
| 11 `SafFileSystem.stat(DocumentFile)` | REACHABLE SOURCE | PASS | Private stat at SafFileSystem.java:487-493 (verified); callers verified: stat(Uri,String) :439, statSafRoot :454, stat(Uri) :469, stat(FakePath) :484. SOURCE correct. |
| 16 `SafFileSystem$FakePath.safRoot()` | REACHABLE SOURCE | PASS | FakePath.safRoot() at SafFileSystem.java:147-150; called from getFile(FakePath) :264, exists :351, mkdirs :512 regions (each `DocumentFile.fromTreeUri(appContext, path.safRoot())` verified). SOURCE correct. |
| 21 `SafFsModule.delete(Uri)` | REACHABLE SOURCE | PASS | SafFsModule.java:84 (def) / :88 delegate to SafFileSystem.delete; FileSystemFacadeImpl.deleteFile :110-114; callers TorrentSessionImpl.java:318, TorrentEngine.java:1154, TorrentDownloadImpl.java:465 (all verified in ruleF copies). SAF branch correctly noted. |
| 26 `SafFsModule.getFilePath(Uri)` | REACHABLE SOURCE | PASS | SafFsModule.java:63 (def) / :65 `stat(Uri)`; FileSystemFacadeImpl.getFilePath :430-434; SaveLogWorker.java:97 `fs.getFilePath(filePath)` (verified). SOURCE correct. |
| 29 `SafFsModule.getParentDirUri(Uri)` | REACHABLE SOURCE | PASS | SafFsModule.java:158 (def) / :160 delegate; same fresh CreateTorrentViewModel :357 chain as row 7. The flip in this pass is justified. |
| 31 `SafFsModule.openFD(Uri)` | REACHABLE SOURCE | PASS | SafFsModule.java:92-95 (def); FileSystemFacadeImpl.getFD :60-64; fresh IPFilterParser.java:72 `fs.getFD(path)` verified in the fresh b5354-55 print; TorrentEngine :380 also verified. Distinct from the SafFileSystem.openFD overloads (batch 4) as the row notes. SOURCE correct. |
| 36 `SystemFacadeImpl.getAppVersionName()` | REACHABLE SOURCE | PASS | SystemFacadeImpl.java:72 (def); MainActivity.java:784-785 and TorrentSessionImpl.java:887 (both verified). SOURCE correct. |

## Totals

- PASS: 10, FAIL: 0 (of 10 checked).
- Proposed corrections: none. Both flips in this pass (rows 7, 29) re-derive from the fresh CreateTorrentViewModel print.
