# LibreTorrent B6 — route notes (final table only)

Source: the B6 final route table (`b6/route_table.md`), built from
the FINAL judgments only (G1_01, G1_02R, G1_03, G1_04, G1_05,
G2_01–G2_06, G3_01–G3_07, G4_01–G4_05, G5_01, G5_02, G5_03R, G5_04)
and the table audit (PASS, all 8 checks). The superseded originals
G1_02 and G5_03 are NOT used here.

## Summary

- Base: branch commit `a9e8b93d`, graph_def blob `564da867`,
  4732 methods / 7293 edges / R3882 / U764 / UNRES86.
- Sample: seed 20261025, 27 routes, 407 steps, 294 distinct edges.
- Final counts: CORRECT 19 / WRONG 8 / UNCLEAR 0 / BLOCKED 0.
- Rate: (FIXED + WRONG) / (CORRECT + FIXED + WRONG)
  = (0 + 8) / (19 + 0 + 8) = 8/27 ≈ 0.2963.
- FIXED = 0. B6 did NOT fix WRONG routes in place (FIXED = 0): the
  8 WRONG routes stay WRONG with their decisive-step reasons; fix
  directions in the B6 report are NOT applied here.
- No device result is claimed in this step: device work comes AFTER
  logs, and no device ROUTES rows, scripts, or DEVICE rows were built
  here.

## Why 27, not 30

Strata filled: NONSTD 4/4, INFERRED 4/4, ENV 6/6, LONG 6/6,
PLAIN 7/7. The STATE stratum pool is empty (0 STATE-gated methods in all 4732 rows), which is why the sample is 27, not 30 — do NOT pad it to 30. The first draw IS the final draw; there was no redraw,
and a confirmatory second sampler run was cmp-identical.

## Caveat screens

- The 59/32 edge Ea751b47d appears in ZERO sampled routes and is
  never claimed as a verified route. All 407 drawn steps have 0
  src/dst touches of unresolved_86.txt.
- Two drawn steps are UNVERIFIABLE (generated Room code absent from
  the upload), both explicitly non-decisive: FeedDao_Impl$1.bind
  step 14 and FeedDao_Impl$11.finalize step 19. No route was left
  unjudgeable on their account.
- No label changes in this step: labels stay R3882/U764/UNRES86
  unless a separate audited T1 execution (NOT this task) changes
  them.

## Route 2 ruling and contingency (carried in full)

TorrentDownloadImpl.havePiece is CORRECT under ruling (i) — the
caveat attaches ONLY to drawn route steps, and its shutdown-first
premise chain (SchedulerReceiver/TorrentService/Utils setup methods,
all in unresolved_86.txt) was verified directly from source, not
from the graph, so it is setup history, not a drawn step.
Contingency, NOT adopted: if the gate adopts rule (ii) (caveat
attaches to any method the verdict depends on), route 2 becomes
BLOCKED with no verdict, counts become CORRECT 18 / WRONG 8 /
BLOCKED 1, rate 8/26 ≈ 0.3077. Both the adopted ruling and the exact
alternative disposition are carried here; the contingency is not
adopted.

## Table (sampler order)

| # | Method | Stratum | Steps | Verdict | Decisive reason summary |
|---|--------|---------|-------|---------|--------------------------|
| 1 | TrackerInfo.infoHashStatus | NONSTD | 31 | CORRECT | TRACKERS page created only on tab select; initial page INFO; fragment inflation confirmed in activity_detail_torrent.xml. |
| 2 | TorrentDownloadImpl.havePiece | NONSTD | 21 | CORRECT | Step 3 edge Eec7bf268 TRUE via a shutdown-first service instance: shutdown actions handled before the CAS (TorrentService.java:183-187), so a pause/resume tap reaches the CAS still false and calls init(). See ruling above. |
| 3 | FeedDao_Impl$11.finalize | NONSTD | 20 | WRONG | Decisive step 20, edge E8756175a FALSE: no program code calls finalize from a constructor; the graph's own trigger admits GC finalization, nondeterministic and not guaranteed in one execution. Step 19 UNVERIFIABLE, non-decisive. |
| 4 | PathResolver.join | NONSTD | 22 | WRONG | Decisive steps 11 + 12 FALSE: step 11 edge Eaf40c0ee — the dialog on this prefix was launched by MainFragment in FILE_CHOOSER_MODE, where the ok branch calls returnDirectoryUri(), not createFile(); step 12 edge E40039873 — the dialog result returns to MainFragment.torrentFileChoose, never to CreateTorrentDialog.choosePathToSave. Conflates two launches. |
| 5 | SafFileSystem$FakePath.normalizeRelativePath | INFERRED | 15 | CORRECT | Exported AddTorrentActivity add flow; decode completed so the Add menu item is visible; fresh non-duplicate torrent; content-scheme SAF download directory routing via FsModuleResolverImpl to SafFsModule, whose FakePath constructor unconditionally calls normalizeRelativePath (SafFileSystem.java:101). |
| 6 | AddTagViewModel$TagAlreadyExistsException.<init> | INFERRED | 15 | WRONG | Decisive step 12, edge E18ed1c0f FALSE: the drawn cancel-button listener calls finish(CANCEL) at AddTagDialog.java:190-192 and never calls addTag(); addTag is reachable only via the positive/add button listener at line 187, which this route does not draw. |
| 7 | FeedDao_Impl$1.bind | INFERRED | 14 | WRONG | Decisive step 8, edge E4a063e93 FALSE: step 2's newInstance(Uri) puts the dialog in ADD mode, where the onShow listener registers addButton to addChannel, not the EDIT edit-button listener. Steps 9 and 12 also inconsistent: updateChannel is EDIT-only, and applyParams(false) calls updateFeed, not addFeed. Mixes an ADD prefix, an EDIT middle, and an ADD tail. Step 14 UNVERIFIABLE, non-decisive. |
| 8 | BaseElement.getUri | INFERRED | 19 | WRONG | Decisive step 11, edge Ed9eb3987 FALSE: step 9 fixes the work input to ACTION_FETCH_ALL_CHANNELS, under which doWork dispatches to fetchChannels (plural), not directly to fetchChannel; printed line 94 belongs to the incompatible ACTION_FETCH_CHANNEL case. |
| 9 | AdvancedPeerInfo.isUtp | ENV | 30 | CORRECT | Non-two-pane user taps a listed torrent, opens detail, selects the Peers tab; peers flowable builds a PeerInfo for a connected peer, whose constructor unconditionally calls peer.isUtp() (PeerInfo.java:110). |
| 10 | SettingsRepositoryImpl.proxyLogin(String) | ENV | 13 | WRONG | Decisive step 7, edge Ee988584f FALSE: the setFragment invocation reached in step 6 commits AppearanceSettingsFragment at SettingsFragment.java:94-95, not Network; Network arrives only via the unprinted network-header click path. The isLargeScreen guard is satisfiable but cannot change which fragment step 6 committed. |
| 11 | TorrentEngine$5.lambda$onTorrentMoving$4 | ENV | 17 | CORRECT | Notification-button tap PAUSE_ALL (not SHUTDOWN_APP, which returns before init) in a fresh service process; .torrent-file add; that torrent finishing; "move after download" enabled to a different folder; live running session. |
| 12 | FixedRingBuffer$FixedRingBufferIterator.<init> | ENV | 12 | CORRECT | Step 10's "None" guard hides addedFilters > 0, which holds on a fresh install because DHT/Peer/Portmap/Torrent log filters all default true, so forceFilterBuf, the for-each iterator call (which fires even on an empty buffer), and the iterator constructor all follow from a launcher start. |
| 13 | AddLinkDialog.checkUrlField | ENV | 18 | CORRECT | FAB add-link action, explicit AddLinkActivity intent, first-time dialog show, onShow, Add-button tap, non-empty link in addLink; dialog_add_link.xml line 28 binds android:text="@={viewModel.link}", satisfying both addLink's viewModel.link guard and checkUrlField's binding-text guard. |
| 14 | SaveLogWorker.lambda$showSuccessToast$1 | ENV | 15 | CORRECT | Two hidden conditions both satisfiable: session logging enabled so the save-log menu group is visible via onPrepareOptionsMenu (true by default in the debug build: SESSION_LOGGING=true), and a valid writable save file from FileManagerDialog so the worker's try block reaches showSuccessToast. |
| 15 | BencodeFileItem$1.<init> | LONG | 12 | CORRECT | Opening a valid .torrent via VIEW drives decode to Utils.getFileList, whose first use of BencodeFileItem triggers <clinit>, which instantiates the CREATOR anonymous class, the file's only anonymous class (BencodeFileItem.java:95-109). |
| 16 | TorrentDownloadImpl.pieces | LONG | 27 | CORRECT | Unselected listed torrent tapped, detail activity opens on a phone layout, user navigates to the Pieces tab, pieces Flowable subscription drives getPieces to the live task's pieces(). MainFragment and MainActivity obtain MsgMainViewModel from the same activity-scoped ViewModelProvider, so PublishSubject delivery holds. |
| 17 | SafFileSystem.getParentDirUri | LONG | 18 | WRONG | Decisive step 17, edge Effae07fc FALSE: reaching FINISHED at step 14 requires a successful build, and makeBuilder() throws "SAF doesn't supported" for any non-file seed path (CreateTorrentViewModel.java:186-187), so the seed on this execution is necessarily file://; the in-app picker only ever returns Uri.fromFile results, so no mid-build re-pick can supply a SAF seed; the facade resolver dispatches to DefaultFsModule, never SafFsModule. Step 18 is not reached via this prefix. |
| 18 | TorrentCriticalWork.lambda$emitChangedEvent$0 | LONG | 12 | CORRECT | Notification shutdown PendingIntent to SHUTDOWN_APP broadcast to shutdown/stopEngine/doStop/requestStop; a live torrent's saveResumeData passes its 10 s throttle (lastSaveResumeTime starts at 0) and valid-handle branch; setSaveResume unconditionally emits via the submitted lambda. |
| 19 | SafFileSystem$FakePath.safRoot | LONG | 26 | WRONG | Decisive step 23, edge E58e81758 FALSE: step 23 strictly requires torrent.downloadPath to be content:// (resolver: FileSystemFacadeImpl.java:144-150 via FsModuleResolverImpl.java:42-49, isSafPath true exactly for scheme content), but on a fresh install no in-app action can make it content:// — the storage-settings picker is dirChooseDialog (StorageSettingsFragment.java:227-239) launching the in-app FileManagerDialog, whose only URI returns are Uri.fromFile (FileManagerViewModel.java:269,272-282,295); default saveTorrentsIn is file:// (SettingsRepositoryImpl.java:102-103); whole-app grep for ACTION_OPEN_DOCUMENT_TREE / ACTION_OPEN_DOCUMENT / ACTION_GET_CONTENT returns only two comment hits (SafFileSystem.java:43,56). Steps 24-26 are TRUE in isolation but NOT REACHED via this prefix. |
| 20 | TorrentSessionImpl.lambda$deleteTorrent$0 | LONG | 15 | CORRECT | Print-omitted guards jointly satisfiable: engine running, session not stopping, and a repo torrent with no live task taking deleteTorrent's notify branch (e.g. a failed restore leaves the torrent listed with an error and no task), with listeners present from onBeforeStart so notifyListeners executes the lambda body. |
| 21 | DefaultFsModule.<init> | PLAIN | 8 | CORRECT | Fresh-launch singleton chain with first-call guards holding; MainApplication.onCreate body read in full, no return before line 70. |
| 22 | SafFsModule.<init> | PLAIN | 8 | CORRECT | Fresh-launch singleton chain verified line by line, ending in FsModuleResolverImpl's unconditional `new SafFsModule(appContext)` (line 37). |
| 23 | FileSystemFacadeImpl.<init> | PLAIN | 7 | CORRECT | Same chain, ending in SystemFacadeHelper's `new FileSystemFacadeImpl(...)` under the fileSystemFacade == null guard on first access. |
| 24 | MainApplication.increaseCursorWindowSize | PLAIN | 2 | CORRECT | MainApplication.onCreate calls it unconditionally at line 68, no early return before it; the body try/catch means the call occurs even if reflection fails. |
| 25 | TorrentNotifier.makeNotifyChans | PLAIN | 2 | CORRECT | MainApplication.onCreate unconditionally calls it at line 70; API 27 clears the SDK-O guard. |
| 26 | MainApplication.<init> | PLAIN | 1 | CORRECT | Framework Instrumentation.newApplication instantiates the manifest-declared application class (public, implicit no-arg constructor). |
| 27 | FsModuleResolverImpl.<init> | PLAIN | 7 | CORRECT | First-launch singleton chain through TorrentNotifier and SettingsRepositoryImpl reaches SystemFacadeHelper.getFileSystemFacade, whose null-guard branch constructs FsModuleResolverImpl as a constructor argument (SystemFacadeHelper.java:42-43). |

## WRONG routes stay WRONG

The 8 WRONG routes (rows 3, 4, 6, 7, 8, 10, 17, 19) stay WRONG
with the decisive-step reasons in the table above. B6 did NOT fix
WRONG routes in place (FIXED = 0); fix directions in the B6 report
are NOT applied here. No label changes in this step: labels stay
R3882/U764/UNRES86 unless a separate audited T1 execution (NOT this
task) changes them.
