# Batch 54 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch54-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b5354-openclose-src/`, `~/workspace/b5354-55-src/`,
  `~/workspace/ruleF-src/`, `~/workspace/overnight/stream-A/corpus/`). No connector fetch was needed; no 429; no missing file.
- Rows checked (13): sample 1, 6, 11, 16, 21, 26, 31, 36 + the five 2026-11-01 open-close flips 9, 18, 27, 32, 33.
- Batch Counts verified mechanically from the label column: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN — matches the
  open-close header (before: 35/0/5).
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `DefaultFsModule.getParentDirUri` | REACHABLE INFERRED | PASS | DefaultFsModule.java:127 (def); FileSystemFacadeImpl.java:438-442 dispatch; CreateTorrentViewModel.java:357 `fs.getParentDirUri(seedPath)` (fresh print). File-URI branch INFERRED, correct. |
| 6 `FileDescriptorWrapperImpl.open` | REACHABLE SOURCE | PASS | FileDescriptorWrapperImpl.java:46 `open(mode)`; FileSystemFacadeImpl write(byte[]) `w.open("rw")` :225 and write(CharSequence) :237; TorrentEngine.java:380-381 `w.open("r")`; TE saveTorrentFile chain :980-984. Printed calls throughout, so SOURCE is correct. |
| 9 `FileSystemFacadeImpl.buildValidFatFilename` | REACHABLE SOURCE | PASS | FileManagerViewModel.java:253 `appendExtension(fs.buildValidFatFilename(fileName))` (fresh); FileManagerDialog.java:583 `viewModel.createFile(fileName)`. Direct printed call — the open-close flip is justified. Batch-4 row 15 (`isValidFatFilename`) correctly NOT flipped: different method (FSFI :334 calls buildValidFatFilename, not vice versa). |
| 11 `FileSystemFacadeImpl.createFile` | REACHABLE SOURCE | PASS | FileSystemFacadeImpl.java:199 (def); TorrentEngine.java:980 `fs.createFile(destDir, name, true)` in saveTorrentFile (fresh TE print). SOURCE correct. |
| 16 `FileSystemFacadeImpl.getDirPath` | REACHABLE SOURCE | PASS | FileSystemFacadeImpl.java:418 (def); StorageSettingsFragment.java:99, :126, :153, :180, :271 — all five cited call sites verified exactly in the corpus/ruleF copy. SOURCE correct. |
| 18 `FileSystemFacadeImpl.getExtensionSeparator` | REACHABLE SOURCE | PASS | FileManagerViewModel.java:243 `fs.getExtensionSeparator()` inside appendExtension (:229-243); appendExtension called from fileExists :224 and createFile :253; createFile by FileManagerDialog :583. Direct printed call — flip justified. |
| 21 `FileSystemFacadeImpl.getFileUri(Uri,String)` | REACHABLE SOURCE | PASS | FileSystemFacadeImpl.java:122 (def); TorrentDownloadImpl.java:1299 `fs.getFileUri(torrent.downloadPath, "." + ti.infoHash() + ".parts")` (fresh). SOURCE correct; the row correctly distinguishes this facade method from the module-level call inside createFile (:205/:213). |
| 26 `FileSystemFacadeImpl.isStorageReadable` | REACHABLE SOURCE | PASS | FileSystemFacadeImpl.java:185 (def); TorrentRepositoryImpl.java:110 (`getSessionFile`) and :146 (`getTorrentDataDir`) via SystemFacadeHelper. SOURCE correct; the row's own strict-entry caveat (callers of those repository methods not freshly printed) is preserved, not hidden. |
| 27 `FileSystemFacadeImpl.isValidFatFilenameChar` | REACHABLE SOURCE | PASS | Private method FSFI :365-384; printed internal call from reachable buildValidFatFilename at :351 (verified by grep). SOURCE under the file's per-row convention (printed internal call from a reachable method), consistently applied with rows 24/29 as cited. |
| 31 `FileSystemFacadeImpl.normalizeFileSystemPath` | REACHABLE SOURCE | PASS | FileSystemFacadeImpl.java:404 (def); Utils.java:646 `fs.normalizeFileSystemPath(path)`; AddTorrentViewModel.java:259 `v.fs.normalizeFileSystemPath(httpTmp.getAbsolutePath())` (fresh). SOURCE correct. |
| 32 `FileSystemFacadeImpl.trimFilename` | REACHABLE SOURCE | PASS | Private method FSFI :386-397; printed internal call from reachable buildValidFatFilename at :360 (verified by grep). Same convention as row 27. |
| 33 `FileSystemFacadeImpl.write(CharSequence,Charset,Uri)` | REACHABLE SOURCE | PASS | FileSystemFacadeImpl.java:232-241 (def); chain verified: FeedActivity backupFeeds :346-357 → `viewModel.saveFeedsSync(file)` :349 → FeedViewModel.saveFeedsSync :135-137 → FeedRepositoryImpl.serializeAllFeeds :144-147 → facade `.write(String, UTF_8, file)` :147. This is the CharSequence overload, not the byte[] overload (row 34) — flip justified. |
| 36 `FsModuleResolverImpl.resolveFsByUri` | REACHABLE SOURCE | PASS | FsModuleResolverImpl.java:42-50 (def, SAF/file-system branch); every cited FSFI dispatch line verified exactly: getFD :62, deleteFile :112, createFile :203, getDirAvailableBytes :272, getDirPath :420, getFilePath :432. SOURCE correct. |

## Totals

- PASS: 13, FAIL: 0 (of 13 checked).
- Proposed corrections: none. All five open-close flips re-derive cleanly from fresh prints.
