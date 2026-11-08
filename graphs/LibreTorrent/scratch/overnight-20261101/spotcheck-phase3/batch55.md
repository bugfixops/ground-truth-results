# Spot-check — batch 55 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 55/1 SafFileSystem.getDir(DocumentFile,String,boolean) — REACHABLE SOURCE — PASS. Private (:291-303); called from SafFileSystem.getFile(FakePath,boolean) :277 and :279 (last-node fallback / intermediate dirs); chain: facade getFileUri(String,Uri) → SafFsModule :77-80 → getFileUri(FakePath) → getFile(FakePath) :240 → here; SAF branch.
- 55/6 SafFileSystem.getInstance(Context) — REACHABLE SOURCE — PASS. :72-82; called from Utils.isSafPath (:658), from every SafFsModule method, and from FsModuleResolverImpl's SAF test chain; any facade call triggers the resolver → isSafPath → here.
- 55/11 SafFileSystem.stat(DocumentFile) — REACHABLE SOURCE — PASS. Private (:487-493); called from stat(Uri) :469, stat(Uri,String) :439, statSafRoot :454, stat(FakePath) :484; inherits row 10/12 routes.
- 55/16 SafFileSystem$FakePath.safRoot() — REACHABLE SOURCE — PASS. :147-150; called from getFile(FakePath) :264, exists(FakePath) :351, mkdirs :512 — inherits row 5 chain.
- 55/21 SafFsModule.delete(Uri) — REACHABLE SOURCE — PASS. :84-89 (delegates to SafFileSystem.delete(Uri) :310); called from FileSystemFacadeImpl.deleteFile :110-114, called from TorrentSessionImpl fs.deleteFile(…) (:318), TorrentDownloadImpl (:465), TorrentEngine (:1154); SAF branch.
- 55/26 SafFsModule.getFilePath(Uri) — REACHABLE SOURCE — PASS. :63-68 (calls stat(Uri) :65); called from FileSystemFacadeImpl.getFilePath :430-434 ← SaveLogWorker :97; SAF branch.
- 55/31 SafFsModule.openFD(Uri) — REACHABLE SOURCE — PASS. :92-95 (returns FileDescriptorWrapperImpl); called from FileSystemFacadeImpl.getFD :60-64 ← TorrentEngine :380, TorrentSessionImpl :296/:360, SaveLogWorker :89, IPFilterParser :72 — IPFilterParser CONFIRMED FRESH in this pass (IPFilterParser.java L72, fs.getFD(path) in parseFile's try-with-resources).
- 55/36 SystemFacadeImpl.getAppVersionName() — REACHABLE SOURCE — PASS. :72-83; called from MainActivity SystemFacadeHelper.getSystemFacade(…).getAppVersionName() (:784-785) and TorrentSessionImpl system.getAppVersionName() (:887).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
