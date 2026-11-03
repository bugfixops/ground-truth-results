# LibreTorrent B6 — Final Route Table (judged)

- Base graph: branch commit `a9e8b93d`, graph_def blob `564da867`
  (4732 methods, 7293 edges, R3882 / U764 / UNRES86), byte-reproducing
  the audited D5 build.
- Sample: seed **20261025**, drawn with
  `python3 -I tools/verify_sample.py LibreTorrent 30 20261025`.
  **27 routes, not 30**: the STATE stratum pool is EMPTY (0 methods with
  STATE gates), so its quota of 3 went unfilled. Strata filled:
  NONSTD 4/4, INFERRED 4/4, ENV 6/6, LONG 6/6, PLAIN 7/7.
  Confirmatory second sampler run cmp-identical.
- Steps total: **407**. Distinct edges on the 27 routes: **294**
  (recomputed from methods.csv route_edge_ids union, not copied from
  the sampler header alone; the recomputation matches the header).
- Judging standard: every step needs BOTH action TRUE (src actually
  calls/reaches dst as drawn, on printed lines) AND operative condition
  TRUE (if/catch/for conditions, guards, STATE/ENV preconditions
  satisfiable in ONE execution: fresh install, API 27, instrumented
  debug build). A step failing either is FALSE.
- Verdict vocabulary: CORRECT / WRONG / UNCLEAR / BLOCKED (finding, no
  verdict). No FIXED verdicts arise: no in-place fixes were applied in
  this task, so WRONG routes stay WRONG with reasons. No redraw: the
  first draw IS the final draw; any post-B6 label work by the
  merger/gate redraws then.
- Counts: **CORRECT 19 / WRONG 8 / UNCLEAR 0 / BLOCKED 0**.
  Rate = (FIXED + WRONG) / (CORRECT + FIXED + WRONG)
  = (0 + 8) / (19 + 0 + 8) = **8/27 ≈ 0.2963**.
  UNCLEAR and BLOCKED (both 0) are excluded from the denominator and
  reported separately.
- Audit trail: every route judged by a helper and independently audited
  (A1–A5). Two routes were overturned on audit and went to a fresh
  re-judge plus re-audit: G1_02 (helper WRONG → auditor CORRECT →
  re-judge CORRECT → re-audit PASS) and G5_03 (helper CORRECT →
  auditor WRONG → re-judge WRONG → re-audit PASS). The superseded
  original judgments (G1_02 WRONG, G5_03 CORRECT) are NOT used in this
  table. All other routes: helper verdict confirmed on audit.
- Caveat screens (run mechanically by the lead and independently by
  every helper, auditor, re-judge, and re-audit): 59/32 edge `Ea751b47d`
  appears in ZERO sampled routes and is never claimed as a verified
  route; ZERO drawn-step edges touch any of the 86 UNRESOLVED methods
  (list: `b6/caveats/unresolved_86.txt`). Caveat-2 premise-history
  note for route 2 (havePiece): see the row note and the Findings
  section below.
- UNVERIFIABLE steps (generated-Room-code gaps, both explicitly
  non-decisive): FeedDao_Impl$1.bind step 14; FeedDao_Impl$11.finalize
  step 19. No route was left unjudgeable; no label change is claimed.

## Table (sampler order)

| # | Method | Stratum | Steps | Verdict | Reason (WRONG: decisive step; CORRECT: decisive premise where non-obvious) |
|---|--------|---------|-------|---------|-----------------------------------------------------------------------------|
| 1 | TrackerInfo.infoHashStatus | NONSTD | 31 | CORRECT | TRACKERS page created only on tab select; initial page INFO; fragment inflation confirmed in activity_detail_torrent.xml. |
| 2 | TorrentDownloadImpl.havePiece | NONSTD | 21 | CORRECT | Step 3 edge `Eec7bf268` (onStartCommand → init) TRUE via a shutdown-first service instance: shutdown actions are handled before the CAS (TorrentService.java:183-187), so a pause/resume tap reaches the CAS still false and calls init(). Auditor + re-judge + re-audit agree. See Findings for the premise-history disclosure and caveat-2 ruling (i). |
| 3 | FeedDao_Impl$11.finalize | NONSTD | 20 | WRONG | Decisive step 20, edge `E8756175a` ($11.<init> → $11.finalize) FALSE: no program code calls finalize from a constructor; the graph's own trigger admits GC finalization, which is nondeterministic and not guaranteed in one execution. (Step 19 UNVERIFIABLE, generated Room code absent from the upload, non-decisive.) |
| 4 | PathResolver.join | NONSTD | 22 | WRONG | Decisive steps 11 + 12 FALSE. Step 11, edge `Eaf40c0ee` (onOptionsItemSelected → createFile): the dialog on this prefix was launched by MainFragment in FILE_CHOOSER_MODE, where onPrepareOptionsMenu hides the ok menu and the ok branch calls returnDirectoryUri(), not createFile(). Step 12, edge `E40039873`: that dialog's result returns to MainFragment.torrentFileChoose, never to CreateTorrentDialog.choosePathToSave. The route conflates MainFragment's file-chooser launch with CreateTorrentDialog's separate SAVE_FILE_MODE launch. |
| 5 | SafFileSystem$FakePath.normalizeRelativePath | INFERRED | 15 | CORRECT | Exported AddTorrentActivity add flow; decode completed so the Add menu item is visible; fresh non-duplicate torrent; content-scheme SAF download directory routing via FsModuleResolverImpl to SafFsModule, whose FakePath constructor unconditionally calls normalizeRelativePath (SafFileSystem.java:101). |
| 6 | AddTagViewModel$TagAlreadyExistsException.<init> | INFERRED | 15 | WRONG | Decisive step 12, edge `E18ed1c0f` (lambda$initAlertDialog$2 → addTag) FALSE: the drawn cancel-button listener calls finish(CANCEL) at AddTagDialog.java:190-192 and never calls addTag(); addTag is reachable only via the positive/add button listener at line 187, which this route does not draw. |
| 7 | FeedDao_Impl$1.bind | INFERRED | 14 | WRONG | Decisive step 8, edge `E4a063e93` (onShow lambda → edit-click lambda) FALSE: step 2's newInstance(Uri) puts the dialog in ADD mode (initParams → initAddMode), where the onShow listener registers addButton to addChannel, not the EDIT edit-button listener. Steps 9 and 12 also inconsistent: updateChannel is EDIT-only, and applyParams(false) calls updateFeed, not addFeed (line 189 runs only when newChannel == true). The route mixes an ADD prefix, an EDIT middle, and an ADD tail. (Step 14 UNVERIFIABLE, generated Room code absent, non-decisive.) |
| 8 | BaseElement.getUri | INFERRED | 19 | WRONG | Decisive step 11, edge `Ed9eb3987` (FeedFetcherWorker.doWork → fetchChannel) FALSE: step 9 fixes the work input to ACTION_FETCH_ALL_CHANNELS, under which doWork dispatches to fetchChannels (plural), not directly to fetchChannel; printed line 94 belongs to the incompatible ACTION_FETCH_CHANNEL case. Later steps are individually sound but the route as drawn is not one real execution. |
| 9 | AdvancedPeerInfo.isUtp | ENV | 30 | CORRECT | Non-two-pane user taps a listed torrent, opens detail, selects the Peers tab; peers flowable builds a PeerInfo for a connected peer, whose constructor unconditionally calls peer.isUtp() (PeerInfo.java:110). |
| 10 | SettingsRepositoryImpl.proxyLogin(String) | ENV | 13 | WRONG | Decisive step 7, edge `Ee988584f` (SettingsFragment.setFragment → NetworkSettingsFragment.onCreate) FALSE: the setFragment invocation reached in step 6 commits AppearanceSettingsFragment at SettingsFragment.java:94-95, not Network; Network arrives only via the unprinted network-header click path (prefClickListener → openPreference). The isLargeScreen guard is satisfiable but cannot change which fragment step 6 committed. |
| 11 | TorrentEngine$5.lambda$onTorrentMoving$4 | ENV | 17 | CORRECT | Notification-button tap PAUSE_ALL (not SHUTDOWN_APP, which returns before init) in a fresh service process; .torrent-file add; that torrent finishing; "move after download" enabled to a different folder; live running session. Step 6's libtorrent4j hook rests on the explicit app-side hook contract (@Override onBeforeStart plus super.start(params) plus the onAfterStart hook comment; library source not in the upload), judged TRUE on that basis. |
| 12 | FixedRingBuffer$FixedRingBufferIterator.<init> | ENV | 12 | CORRECT | Step 10's "None" guard hides addedFilters > 0, which holds on a fresh install because DHT/Peer/Portmap/Torrent log filters all default true, so forceFilterBuf, the for-each iterator call (which fires even on an empty buffer), and the iterator constructor all follow from a launcher start. |
| 13 | AddLinkDialog.checkUrlField | ENV | 18 | CORRECT | FAB add-link action, explicit AddLinkActivity intent, first-time dialog show, onShow, Add-button tap, non-empty link in addLink; dialog_add_link.xml line 28 binds android:text="@={viewModel.link}", satisfying both addLink's viewModel.link guard and checkUrlField's binding-text guard. |
| 14 | SaveLogWorker.lambda$showSuccessToast$1 | ENV | 15 | CORRECT | Two hidden conditions both satisfiable: session logging enabled so the save-log menu group is visible via onPrepareOptionsMenu (true by default in the debug build: SESSION_LOGGING=true), and a valid writable save file from FileManagerDialog so the worker's try block reaches showSuccessToast. |
| 15 | BencodeFileItem$1.<init> | LONG | 12 | CORRECT | Opening a valid .torrent via VIEW drives decode to Utils.getFileList, whose first use of BencodeFileItem triggers <clinit>, which instantiates the CREATOR anonymous class, the file's only anonymous class (BencodeFileItem.java:95-109). |
| 16 | TorrentDownloadImpl.pieces | LONG | 27 | CORRECT | Unselected listed torrent tapped, detail activity opens on a phone layout, user navigates to the Pieces tab, pieces Flowable subscription drives getPieces to the live task's pieces(). MainFragment and MainActivity obtain MsgMainViewModel from the same activity-scoped ViewModelProvider, so PublishSubject delivery holds. |
| 17 | SafFileSystem.getParentDirUri | LONG | 18 | WRONG | Decisive step 17, edge `Effae07fc` (FileSystemFacadeImpl.getParentDirUri → SafFsModule.getParentDirUri) FALSE: reaching FINISHED at step 14 requires a successful build, and makeBuilder() throws "SAF doesn't supported" for any non-file seed path (CreateTorrentViewModel.java:186-187), so the seed on this execution is necessarily file://; the in-app picker only ever returns Uri.fromFile results, so no mid-build re-pick can supply a SAF seed; the facade resolver dispatches to DefaultFsModule, never SafFsModule. Step 18 is not reached via this prefix. |
| 18 | TorrentCriticalWork.lambda$emitChangedEvent$0 | LONG | 12 | CORRECT | Notification shutdown PendingIntent to SHUTDOWN_APP broadcast to shutdown/stopEngine/doStop/requestStop; a live torrent's saveResumeData passes its 10 s throttle (lastSaveResumeTime starts at 0) and valid-handle branch; setSaveResume unconditionally emits via the submitted lambda. |
| 19 | SafFileSystem$FakePath.safRoot | LONG | 26 | WRONG | Decisive step 23, edge `E58e81758` (FileSystemFacadeImpl.getFileUri(String,Uri) → SafFsModule.getFileUri(String,Uri)) FALSE: step 23 strictly requires torrent.downloadPath to be content:// (resolver: FileSystemFacadeImpl.java:144-150 via FsModuleResolverImpl.java:42-49, isSafPath true exactly for scheme content), but on a fresh install no in-app action can make it content:// — the storage-settings picker is dirChooseDialog (StorageSettingsFragment.java:227-239) launching the in-app FileManagerDialog, whose only URI returns are Uri.fromFile (FileManagerViewModel.java:269,272-282,295); default saveTorrentsIn is file:// (SettingsRepositoryImpl.java:102-103); whole-app grep for ACTION_OPEN_DOCUMENT_TREE / ACTION_OPEN_DOCUMENT / ACTION_GET_CONTENT returns only two comment hits (SafFileSystem.java:43,56); alternative-source search (per-torrent add-time dir, feed torrents, watch-dir scan, create-torrent save path, detail-view dir change, move-after-download, DB restore migration writing 'file://' || path_to_download, external-intent torrents where a content:// source file is not a content:// save path) found none. Steps 24-26 are TRUE in isolation but NOT REACHED via this prefix. Auditor + re-judge + re-audit agree. |
| 20 | TorrentSessionImpl.lambda$deleteTorrent$0 | LONG | 15 | CORRECT | Print-omitted guards jointly satisfiable: engine running, session not stopping, and a repo torrent with no live task taking deleteTorrent's notify branch (e.g. a failed restore leaves the torrent listed with an error and no task, LoadTorrentTask.run catch setting torrent.error with no task created), with listeners present from onBeforeStart so notifyListeners executes the lambda body. |
| 21 | DefaultFsModule.<init> | PLAIN | 8 | CORRECT | Fresh-launch singleton chain with first-call guards holding; MainApplication.onCreate body read in full, no return before line 70. |
| 22 | SafFsModule.<init> | PLAIN | 8 | CORRECT | Fresh-launch singleton chain verified line by line, ending in FsModuleResolverImpl's unconditional `new SafFsModule(appContext)` (line 37). |
| 23 | FileSystemFacadeImpl.<init> | PLAIN | 7 | CORRECT | Same chain, ending in SystemFacadeHelper's `new FileSystemFacadeImpl(...)` under the fileSystemFacade == null guard on first access. |
| 24 | MainApplication.increaseCursorWindowSize | PLAIN | 2 | CORRECT | MainApplication.onCreate calls it unconditionally at line 68, no early return before it; the body try/catch means the call occurs even if reflection fails. |
| 25 | TorrentNotifier.makeNotifyChans | PLAIN | 2 | CORRECT | MainApplication.onCreate unconditionally calls it at line 70; API 27 clears the SDK-O guard. |
| 26 | MainApplication.<init> | PLAIN | 1 | CORRECT | Framework Instrumentation.newApplication instantiates the manifest-declared application class (public, implicit no-arg constructor). |
| 27 | FsModuleResolverImpl.<init> | PLAIN | 7 | CORRECT | First-launch singleton chain through TorrentNotifier and SettingsRepositoryImpl reaches SystemFacadeHelper.getFileSystemFacade, whose null-guard branch constructs FsModuleResolverImpl as a constructor argument (SystemFacadeHelper.java:42-43). |

## Findings

- Caveat violations on drawn steps: NONE. 59/32 edge `Ea751b47d` in zero
  sampled routes; zero drawn-step edges touch any of the 86 UNRESOLVED
  methods.
- Caveat-2 premise-history disclosure (route 2, havePiece): the CORRECT
  verdict's shutdown-first premise depends on methods listed in
  `unresolved_86.txt` as SETUP HISTORY, not as drawn route steps:
  SchedulerReceiver.<init>, SchedulerReceiver.onReceive,
  SchedulerReceiver.onStopApp, TorrentService.<init>,
  TorrentService.onCreate, TorrentService.initPendingIntents,
  Utils.lambda$startServiceBackground$0. The re-audit ruled (i): the
  caveat attaches ONLY to drawn route steps — wording (a "sampled
  route" routing through / touching), the BLOCKED screen as defined and
  applied across all groups (drawn-step src/dst ∩ unresolved_86.txt),
  and purpose (the 86 lack a graph path, so the caveat bars resting a
  verdict on the graph's say-so about them; here every premise link was
  verified directly from source, not from the graph; T1 shows UNRESOLVED
  means pathless — BFS skips non-standard dispatches like alarm
  delivery — not unexecutable). Load-bearing, stated plainly: without
  the premise chain, step 3 fails as the first helper judged. Residual
  risk, plainly: the premise methods' launch-reachability is not
  graph-proven, so step 3 rests on source reading plus standard
  platform behaviour (AlarmManager, framework service creation).
  Contingency (recorded, NOT adopted): if the gate instead adopts rule
  (ii) — caveat attaches to any method the verdict's execution depends
  on — route 2 becomes a BLOCKED finding with no verdict, held pending
  T1 resolution of the premise methods; counts would then be
  CORRECT 18 / WRONG 8 / BLOCKED 1, rate 8/26 ≈ 0.3077.
- Label issues blocking a verdict: NONE (apart from the route-2
  contingency above, which is a caveat-scope question, not a label
  question). No route was BLOCKED; no verdict was invented; no label
  change is claimed.
- Fix directions (NOT verdicts, NOT applied): BaseElement.getUri via
  fetchChannels; SettingsRepositoryImpl.proxyLogin via the network-header
  click path; SafFileSystem.getParentDirUri / safRoot needing a
  content:// SAF URI prefix that no in-app action can supply. Any
  post-B6 label work by the merger/gate redraws the sample then.

## Sources

- Sample: `b6/tree/graphs/LibreTorrent/scratch/sample_30.txt`.
- Prints: `b6/tree/graphs/LibreTorrent/scratch/route_print/` (27 files).
- Judgments: `b6/judging/` — final versions: G1_01, G1_02R, G1_03,
  G1_04, G1_05, G2_01–G2_06, G3_01–G3_07, G4_01–G4_05, G5_01, G5_02,
  G5_03R, G5_04. (G1_02 original and G5_03 original are SUPERSEDED and
  must not be used.)
- Audits: `b6/audit/AUDIT_G1.md`, `AUDIT_G2.md`, `AUDIT_G3.md`,
  `AUDIT_G4.md`, `AUDIT_G5.md`, `AUDIT_G1_02R.md`, `AUDIT_G5_03R.md`.
- Methods/edges: `b6/tree/graphs/LibreTorrent/out/methods.csv`,
  `b6/tree/graphs/LibreTorrent/out/libretorrent_trigger_graph.json`.
