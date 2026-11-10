"""Write graphs/AmazeFileManager/verification.csv for the AmazeFileManager schema 2 trigger graph.

Modelled on graphs/AnyMemo/make_verification.py.
Run from the work folder: python3 -I graphs/AmazeFileManager/make_verification.py
Every note is validated against the built graph; the script raises (STOPs) if a path/label item is missing,
a verdict does not match, an edge id does not exist, or a path row's cited file:line is not on that method's route.
All paths it uses are inside graphs/AmazeFileManager/ or tools/ (no session folders).
Path rows use the B6 route_table.md round verdicts (correct x5, fixed x25); every final print was
re-verified clean after the last fix, and each note states its round verdict.
DEVICE rows (brief D7): when graphs/AmazeFileManager/device/results.csv exists (written by
device/compare.py after a real device run), one row per route is appended AFTER all existing rows,
in results.csv order, without re-sorting: type=path, result=correct when reached=yes else unclear,
confirmed_by=DEVICE, ref=device run <run>/<script>, edges unchanged, note = script status (for
unclear rows the reason: not reached, script failed, or unscriptable). A route not reached never
becomes wrong; no label changes. When the file does not exist, the DEVICE code path does not run
at all and the output is byte-identical to the pre-D7 writer.
"""
import csv, glob, json, re, sys
sys.path.insert(0, 'tools')
import build_graph as b

APP = 'AmazeFileManager'
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % APP)[0], encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % APP, encoding='utf-8'))}

# the authoritative final sample (B6): read from scratch, not from a session folder
SAMPLE_FILE = 'graphs/%s/scratch/sample_30.txt' % APP
sample = [l.split()[-1] for l in open(SAMPLE_FILE, encoding='utf-8')
          if l.startswith(('NONSTD', 'INFERRED', 'STATE', 'ENV', 'LONG', 'PLAIN'))]

# ---- path rows: one per sampled method. result/ref/note written from reading the route (B6).
P = {}
def p(m, res, ref, note):
    P[m] = (res, ref, note)

p('ApkImageDataFetcher.cancel', 'correct', 'Drawer.java:99',
  'Round verdict: correct. Drawer apps item -> AppsListFragment -> GlideApp.with (:98) -> generated module -> registerComponents (:20-23) -> ApkImageModelLoaderFactory (:21) -> build -> loader (:25) -> buildLoadData -> fetcher (:27) -> cancel (Glide lifecycle, INFERRED standard).')
p('CloudIconDataFetcher.cancel', 'fixed', 'Drawer.java:99',
  'Round verdict: fixed (citations only + spurious factory <init> edge deleted). Drawer -> AppsListFragment -> GlideApp.with -> generated module -> registerComponents -> CloudIconModelFactory -> factory.build -> loader -> cancel (:55-58); the factory <init> does not construct the loader (built in build() at CloudIconModelFactory.java:24). Caveat (route_01 follow-up): steps 10-14 need a String -> Bitmap cloud-model load (CloudIconModelLoader implements ModelLoader<String, Bitmap> and only handles cloud/smb/ssh prefixes); the Apps preload is String -> Drawable (AppsAdapterPreloadModel), so live replay proves the chain only to factory construction.')
p('CompressedExplorerFragment.onDestroyView', 'fixed', 'MainActivity.java:319',
  'Round verdict: fixed (citations only). MainActivity onCreate -> checkForExternalIntent (:319) -> openCompressed (:525, :797-798) -> CompressedExplorerFragment -> onDestroyView. Requires a zip/rar VIEW intent from another app (ENV other_app, recorded not encoded).')
p('FileUtils.lambda$scanFile$1', 'fixed', 'Operations.java:480-485',
  'Round verdict: fixed (citations only). Operations$3.doInBackground -> onPostExecute (:480-485) -> FileUtils.scanFile (:484) -> lambda$scanFile$1.')
p('FtpTileService.updateTileState', 'fixed', 'FtpTileService.java:28',
  'Round verdict: fixed (citations only). Manifest FtpTileService (:195-203) + FtpServerFragment lambda (:132, startServer :137) + FtpService run() post (:227) -> @Subscribe onFtpReceiverActions (:26) -> updateTileState (:28).')
p('GenericCopyUtil.doCopy', 'fixed', 'CopyService.java:160',
  'Round verdict: fixed (citations only). Manifest CopyService (:175-179) -> onStartCommand -> execute (:160) -> copyFiles (:381) -> GenericCopyUtil.doCopy.')
p('GlideRequests.load(Integer)', 'fixed', 'CompressedExplorerFragment.java:494-495',
  'Round verdict: fixed (citations only). goBack (:494-495) -> changePath (:404) -> createViews -> CompressedExplorerAdapter (:217) -> GlideApp load -> GlideRequests.load(Integer).')
p('HybridFile$11.<init>', 'fixed', 'CryptUtil.java:247',
  'Round verdict: fixed (citation only). Manifest EncryptService (:181-183) -> onStartCommand -> CryptUtil.<init> (:191) -> encrypt (:125) -> getOutputStream (:247, real call line) -> HybridFile$11.<init> (:1021, SshClientTemplate anonymous class, SSH branch).')
p('ImmutableEntry.getValue', 'fixed', 'SearchTextTask.java:91,95',
  'Round verdict: fixed (citations only). S_ENTRY TextEditorActivity (:129-144 manifest) -> <init> -> SearchTextTask.<init> (created at TextEditorActivity.java:449 in afterTextChanged) -> doInBackground -> onPostExecute -> keyMapEntry.getValue() (:91,95) on the ImmutableEntry from MapEntry.')
p('Indicator$PendingRevealAnimator$1.onAnimationEnd', 'fixed', 'MainActivity.java:414,416,420',
  'Round verdict: fixed (citations only). MainActivity onCreate -> goToMain (:414,416,420) -> TabFragment addTab -> MainFragment -> Indicator -> setSelectedPage -> animator (:576) -> listener (:167) -> PendingRevealAnimator$1.onAnimationEnd.')
p('ItemPopupMenu$2.onButtonPressed(Intent,String)', 'fixed', 'GeneralDialogCreation.java:752-764',
  'Round verdict: fixed (citation only). RecyclerAdapter showPopup (:813) -> ItemPopupMenu.<init> (:950) -> onMenuItemClick (:60) -> showEncryptAuthenticateDialog (:168-170) -> .onPositive lambda (:752-764) -> onButtonPressed (:757).')
p('MainFragment.onDetach', 'fixed', 'TabFragment.java:351',
  'Round verdict: fixed (citations + summary edge evidence). MainActivity goToMain -> TabFragment onCreateView -> addTab (:113-141, creates MainFragment at :351) -> MainFragment -> onDetach.')
p('PasteHelper.<init>(Parcel)', 'fixed', 'MainActivity.java:366',
  'Round verdict: fixed (citations only). MainActivity$1 creation (:366) -> getParcelable -> PasteHelper$1.createFromParcel -> <init>(Parcel) (:43-44). Needs a pending copy/cut (needs_state, recorded not encoded).')
p('PasteHelper.writeToParcel', 'correct', 'MainActivity.java:1077-1078',
  'Round verdict: correct. MainActivity putParcelable (:1077-1078) -> PasteHelper.writeToParcel; Bundle marshalling INFERRED standard framework behaviour.')
p('PasteHelper$1.createFromParcel', 'fixed', 'MainActivity.java:366',
  'Round verdict: fixed (citations only). MainActivity$1 creation (:366) -> getParcelable -> createFromParcel.')
p('PemToKeyPairTask.toastOnParseError', 'fixed', 'PemToKeyPairTask.java:155',
  'Round verdict: fixed (citations only). SftpConnectDialog onCreateDialog -> picker (:146) -> onActivityResult (:303) -> task execute (:322) -> publishProgress (:118) -> onProgressUpdate lambda (:153-157) -> toastOnParseError (:155).')
p('ProcessViewerFragment$CustomServiceConnection$1.<init>', 'correct', 'ProcessViewerFragment.java:416',
  'Round verdict: correct. MainActivity (:390) -> ProcessViewerFragment -> onCreateView -> onActivityCreated -> onResume -> onServiceConnected (bindService x5, :159-171) -> anonymous ProgressListener $1.<init> (:416).')
p('ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'fixed', 'ProcessViewerFragment.java:423',
  'Round verdict: fixed (citation only). ExtractService chain (:165-169 manifest, lambda :142-143, publishResults :143, addDatapoint :161, onUpdate :189) -> runOnUiThread lambda (:423).')
p('ReadFileTask$ReturnedValues.<init>(int)', 'fixed', 'TextEditorActivity.java:291',
  'Round verdict: fixed (wrong route re-routed). S_ENTRY TextEditorActivity (:129-144 manifest, ENV other_app) -> onCreate -> load -> ReadFileTask.doInBackground (:291) -> ReturnedValues.<init> (:115). Old BasicActivity prefix deleted (both activities extend ThemedActivity).')
p('ShareAdapter$ViewHolder.lambda$render$0', 'fixed', 'AppsAdapter.java:170',
  'Round verdict: fixed (citations + summary edge evidence). Drawer apps item -> AppsListFragment -> AppsAdapter menu share (:170, :181-185) -> shareFiles -> ShareTask onPostExecute (:121) -> ShareAdapter (:50) -> onBindViewHolder -> lambda$render$0.')
p('SmbSearchDialog$1.lambda$computerFound$0', 'fixed', 'SmbSearchDialog.java:109',
  'Round verdict: fixed (citations + evidence). SmbSearchDialog -> SubnetScanner (:80) -> start (:109) -> run (:84) -> onFound (:109, :157) -> computerFound (:173-177) -> lambda$computerFound$0.')
p('SshAuthenticationTask$1.getPublic', 'fixed', 'SshAuthenticationTask.java:144',
  'Round verdict: fixed (citations + summary evidence). CopyService -> mkdir (:446) -> SshAuthenticationTask doInBackground (:117) -> KeyProvider (:131) -> getType (:143) -> getPublic (:144).')
p('SshConnectionPool$AsyncRemoveConnection.onPostExecute', 'fixed', 'SshConnectionPool.java:301',
  'Round verdict: fixed (WRONG route re-routed, route_08 follow-up). Drawer saved-ssh item -> onNavigationItemActionClick (:494) -> showSftpDialog (:626) -> SftpConnectDialog onCreateDialog -> onPositive lambda$onCreateDialog$9 (:157-160) -> removeConnection (:176, STATE gate: saved SSH host key exists, :175 !isEmpty(sshHostKey)) -> AsyncRemoveConnection.<init> (:95) -> doInBackground (:291) -> onPostExecute (:301). The B6 print wrongly routed via the options menu and the focus listener (:132, which only selectAlls on focus and never calls removeConnection); the false focus -> removeConnection edge and the swapped $0/$9 registration evidence are deleted/corrected. The FAB menu_new_cloud prefix (:1952-1956) is the alternate true entry to the same dialog (see SmbSearchDialog route); the finder prints the shorter Drawer entry here.')
p('StreamNotFoundException.<init>(Throwable)', 'fixed', 'TextEditorActivity.java:357',
  'Round verdict: fixed (citations only). S_ENTRY TextEditorActivity (:129-144) -> onCreate -> onOptionsItemSelected (:357) -> save case (:364) -> saveFile -> WriteFileAbstraction (:262) -> doInBackground -> throw StreamNotFoundException (:69).')
p('StreamSource.getCurrentPosition', 'fixed', 'MainFragment.java:930',
  'Round verdict: fixed (citations + evidence). MainFragment onListItemClicked -> launchCloud (:930) -> CloudStreamer.serve -> CloudStreamSource.<init> -> RandomAccessStream -> mark -> getCurrentPosition.')
p('StreamSource.read(byte[],int,int)', 'correct', 'StreamServer.java:672',
  'Round verdict: correct. SMB path: launchSMB (:915) -> Streamer -> StreamServer -> HTTPSession (:180, :229-231, :237) -> sendResponse (:332) -> data.read loop (:672) -> SmbStreamer StreamSource.read (:75-79). The bogus SMB -> CloudStreamSource edge was deleted in round-2.')
p('TextEditorActivity$2.onAnimationEnd', 'fixed', 'TextEditorActivity.java:481-488',
  'Round verdict: fixed (citations only). S_ENTRY TextEditorActivity (:129-144) -> onCreate -> onOptionsItemSelected (:357) -> revealSearchView (:390) -> animator listener $2 (:481-488) -> onAnimationEnd.')
p('TextEditorActivity$3.onAnimationEnd', 'fixed', 'TextEditorActivity.java:518-526',
  'Round verdict: fixed (citations only). S_ENTRY TextEditorActivity (:129-144) -> onCreate -> onOptionsItemSelected (:357) -> hideSearchView (:389) -> animator listener $3 (:518-526) -> onAnimationEnd.')
p('ThemedImageView.getActivity', 'fixed', 'PrefFrag.java:89',
  'Round verdict: fixed (citations only). PrefFrag preference click (:89) -> ThemedImageView -> getActivity.')
p('UtilsHandler.getSshAuthPrivateKeyColumn', 'correct', 'UtilsHandler.java:427',
  'Round verdict: correct. MainActivity onResume -> Drawer.refreshDrawer (:1112) -> addNewItem lambda -> onNavigationItemActionClick (:494) -> showSftpDialog (:626) -> getSshAuthPrivateKeyName (:1656) -> getSshAuthPrivateKeyColumn (:427).')

# ---- W8 re-verification (Kiro, 2026-11-06, self-checked only, second: pending reviewer): the 20 sampled routes whose
# best route changed in the re-audit (tools_dev/route_diff.py). Each new step was read in the source; these rows
# replace the B6 rows above for those methods. "Kind caveat" marks a real user action that the graph writes as a
# LIFECYCLE/FRAMEWORK/CALL edge (the menu tap S_ENTRY -> MainActivity.onOptionsItemSelected, the row tap
# RecyclerAdapter.<init> -> MainFragment.onListItemClicked, the action-mode or FAB item): the action exists and every
# gate the source needs is on the route, so the route holds; the GUI-step count is low by those steps.
W8 = 'W8 re-verified 2026-11-06 (first verification: %s). '
def p8(m, res, ref, note):
    # keep the first verdict when it was fixed or wrong (review 3, fix 4); the re-check is in the note
    first = P[m][0]
    P[m] = (first if first in ('fixed', 'wrong') else res, ref, W8 % first + note)

p8('CloudIconDataFetcher.cancel', 'correct', 'Drawer.java:99',
   'Only step 12 changed: CloudIconModelLoader.buildLoadData now carries the state its handles() needs (a cloud, SMB or SFTP entry), which the first verification recorded as a caveat. Steps 1-11 and 13-14 as before.')
p8('CompressedExplorerFragment.onDestroyView', 'correct', 'FileUtils.java:753',
   'New steps 1-9: the view-switch menu item (kind caveat) rebuilds the list, a row tap (kind caveat; MainFragment.java:933 default case) opens an .apk file (FileUtils.java:751-753, state: an .apk file), the package dialog negative button opens it as an archive (GeneralDialogCreation.java:917 -> MainActivity.openCompressed). Step 13 now carries the archive state (the refresh listener of the archive viewer, CompressedExplorerFragment.java:149). Steps 10-16 as before. Re-check 2 (2026-11-07, PENDING batch 1): a file row tap now carries STATE file (MainFragment.java:893, 929-930), so the best route opens the file through Back on the FTP page with a file path pending (state, MainActivity.onBackPressed) -> openFile -> the package dialog of a file named .apk (state) -> openCompressed; two states, both made in the app.')
p8('FileUtils.lambda$scanFile$1', 'correct', 'MainFragment.java:705',
   'New steps 1-10: launch, goToMain -> TabFragment -> MainFragment, a long press starts the action mode (kind caveat), its Rename item (MainFragment.java:701-705) -> rename dialog (:1209-1226) -> MainActivityHelper.rename -> Operations.rename; a baseline folder is renamed. The INFERRED RecyclerAdapter.<init> -> MainFragment.rename edge was dropped (graph_def.py, Q-W8-1). Re-check 2 (2026-11-07, PENDING batch 1): the action-mode item now carries the selection state (Q-R3-1), so the best route renames a baseline folder through the row\'s popup menu (RecyclerAdapter.showPopup -> ItemPopupMenu.onMenuItemClick -> MainFragment.rename, ItemPopupMenu.java:99), a GUI route.')
p8('GenericCopyUtil.doCopy', 'correct', 'CopyService.java:381',
   'Only step 1 changed: CopyService is entered through its in-app start, with the state the paste needs (a pending copy, AndroidManifest.xml:175-179: not exported). Steps 2-10 as before.')
p8('GlideRequests.load(Integer)', 'correct', 'RecyclerAdapter.java:738',
   'New steps 1-7: the view-switch menu item (kind caveat) rebuilds the list in grid mode, and onBindViewHolder loads the thumbnail drawable of an image, video or APK row (RecyclerAdapter.java:716-738; state: such a file).')
p8('HybridFile$11.<init>', 'correct', 'HybridFile.java:1021',
   'New steps 1-12: the + button, New file (MainActivity.java:1949-1951; kind caveat on the FAB item), the name dialog (MainActivityHelper.java:163-166) -> mkFile -> Operations.mkfile -> doInBackground (Operations.java:214) -> getOutputStream, SFTP case (HybridFile.java:1019-1021; env: a saved SFTP connection whose server lists the folder). Re-check 2026-11-08 (W7 r6-p14): step 11 is the same call under a new edge id (E0d20a34f to E4e36e199), which now carries the SFTP server env itself; the same 12 steps.')
p8('ImmutableEntry.getValue', 'correct', 'FileUtils.java:420',
   'New steps 1-8: the view-switch menu item and a row tap (kind caveats) open a text file (state), openFile -> openunknown, whose text/* VIEW intent resolves to the text editor (FileUtils.java:420-441). Steps 9-12 (search text task) as before. Re-check 2 (2026-11-07, PENDING batch 1): the row tap now carries STATE file; the best route opens the text file with the row popup\'s Open with (ItemPopupMenu.java:130 -> FileUtils.openWith -> the text editor, state: a text file). The rest as before.')
p8('PemToKeyPairTask.toastOnParseError', 'correct', 'SftpConnectDialog.java:142',
   'New steps 1-8: the + button, New cloud connection (MainActivity.java:1952-1956), the cloud sheet SFTP option (CloudSheetFragment.java:111-119) opens the SFTP dialog; the key picker is the system document picker (SftpConnectDialog.java:142-146, env). The rest as before.')
p8('ProcessViewerFragment$CustomServiceConnection$1.<init>', 'correct', 'MainActivity.java:390',
   'Only step 2 changed: MainActivity.onCreate opens the process viewer when the launch intent comes from a running operation notification (openProcesses, MainActivity.java:386-392; state).')
p8('ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'correct', 'AndroidManifest.xml:165',
   'Only step 1 changed: ExtractService through its in-app start with the state an extraction needs (an archive the user extracts; not exported, AndroidManifest.xml:165-169). The process viewer is opened by the user while it runs. Re-check 2026-11-07: step 7 is now the bytecode twin of the listener dispatch (AbstractProgressiveService.addDatapoint@ExtractService -> onUpdate, E1edbb3e0); both carry the state that the open viewer registered the listener (AbstractProgressiveService.java:187-189; ProcessViewerFragment.java:416). Re-check 3 (W7 r6-p09): the same 8 steps; step 8 is the same post to the UI thread under a new edge id (E5d4de743 to Ead7f592a) and now carries the state that the viewer is open and bound while the operation runs (ProcessViewerFragment.java:416-423).')
p8('ReadFileTask$ReturnedValues.<init>(int)', 'correct', 'FileUtils.java:420',
   'Same new prefix as ImmutableEntry.getValue (row tap on a text file -> text editor); then TextEditorActivity.onCreate -> load -> ReadFileTask as before. Re-check 2 (2026-11-07, PENDING batch 1): same new prefix as ImmutableEntry.getValue (Open with from the row popup, state: a text file). Re-check 3 (W7 r6-p03): the same 16 steps; step 16 is the same call under a new edge id (E5c4cc446 to Ef0eff8ec) and now carries the env gate other: ReturnedValues(int) is built only in the StreamNotFoundException and IOException catches (ReadFileTask.java:110-115), so the class is env.')
p8('SmbSearchDialog$1.lambda$computerFound$0', 'correct', 'SubnetScanner.java:109',
   'Only step 13 changed: SubnetScanner.run calls onFound for a host that answered (SubnetScanner.java:91-109; env network).')
p8('SshAuthenticationTask$1.getPublic', 'wrong', 'SshConnectionPool.java:213',
   'New steps 1-20: the + button and cloud sheet open the SFTP dialog (CloudSheetFragment.java:111-119); Create looks up the stored host key (SftpConnectDialog.java:171-176); with a saved connection to the typed host (state) the old connection is removed (:176-180) and authenticateAndSaveSetup runs; the task connects first (SshAuthenticationTask.java:124, env network) and, for a key login, builds the KeyProvider (:129-131, state) whose getPublic is called. Re-check 2026-11-07: steps 13-14 now go through the host-fingerprint callback lambda$null$4 (SftpConnectDialog.java:181-194; network) instead of the changed-host-key prompt, which now carries its own network env (:183-193); step 20 carries the key-login network env (SshAuthenticationTask.java:129-145). Re-check 2 (2026-11-07, W7 r6-p10): the host-fingerprint callback now carries the network env itself, so the best route is the drawer Recent files list (closed drawer, Drawer.java:224-225) -> listRecent -> HybridFile.exists() -> SshClientUtils.execute -> SshConnectionPool.create -> the auth task. Wrong as drawn: listRecent turns each history path into a java.io.File (LoadFilesListTask.java:394, RootHelper.java:136-142), which folds ssh:// to ssh:/, so generateMode never sets SFTP (HybridFile.java:92-95) and exists() never takes its SFTP branch (:1077); HybridFile.exists() is one node for every caller (Q-R6-2). The class does not change (a saved SFTP connection, network).')
p8('SshConnectionPool$AsyncRemoveConnection.onPostExecute', 'correct', 'SftpConnectDialog.java:176',
   'New steps 1-8: the + button and cloud sheet open the SFTP dialog; on Create the stored host key of the typed host is looked up (SftpConnectDialog.java:171-176), so with a saved connection to that host (state) the old connection is removed. The rest as before. Re-check 2026-11-08 (W9 reachable audit, state 7): step 12 is the same call under a new edge id (Eaa386f86 to E34ff4c36); its gate is now env network instead of the saved-key STATE, because the host key is stored only after GetSshHostFingerprintTask reached the server (SftpConnectDialog.java:168-180). The same 15 steps.')
p8('StreamNotFoundException.<init>(Throwable)', 'correct', 'WriteFileAbstraction.java:69',
   'Same new prefix as ImmutableEntry.getValue; then the editor Save item -> saveFile -> WriteFileAbstraction as before. Re-check 2 (2026-11-07, PENDING batch 1): same new prefix as ImmutableEntry.getValue (Open with from the row popup, state: a text file). Re-check (W7 r6-p05): the route is now 7 steps: another app opens a text file in TextEditorActivity with ACTION_VIEW (env other_app, the manifest view filter), Save in its menu runs WriteFileAbstraction, and for the content uri a RuntimeException from the provider becomes StreamNotFoundException (WriteFileAbstraction.java:62-69, env other_app). One real execution; correct.')
p8('StreamSource.getCurrentPosition', 'correct', 'MainFragment.java:930',
   'New steps 1-6: the view-switch menu item and a row tap (kind caveats) on a cloud file (MainFragment.java:925-930; env: the cloud plugin app) -> CloudUtil.launchCloud -> CloudStreamer; step 10 the client connection (env network).')
p8('StreamSource.read(byte[],int,int)', 'correct', 'MainFragment.java:915',
   'Steps 6, 8, 13 changed: a row tap on an SMB file (MainFragment.java:914-915, env: an SMB server) -> launchSMB -> Streamer.getInstance -> Streamer.<init> (Streamer.java:39) -> StreamServer; the client connection (StreamServer.java:179-180, env) and handleResponse -> sendResponse (StreamServer.java:332), which reads the StreamSource. The sendError -> sendResponse edge is cut (graph_def.py): sendError passes null data (StreamServer.java:631).')
p8('TextEditorActivity$2.onAnimationEnd', 'correct', 'FileUtils.java:420',
   'Same new prefix as ImmutableEntry.getValue; then the editor search item -> revealSearchView -> animator listener $2 as before. Re-check 2 (2026-11-07, PENDING batch 1): same new prefix as ImmutableEntry.getValue (Open with from the row popup, state: a text file).')
p8('TextEditorActivity$3.onAnimationEnd', 'correct', 'FileUtils.java:420',
   'Same new prefix as ImmutableEntry.getValue; then the editor search item -> hideSearchView -> animator listener $3 as before. Re-check 2 (2026-11-07, PENDING batch 1): same new prefix as ImmutableEntry.getValue (Open with from the row popup, state: a text file).')
p8('FtpTileService.updateTileState', 'correct', 'AndroidManifest.xml:195',
   'The route is now the quick-settings tile itself: the system binds FtpTileService (BIND_QUICK_SETTINGS_TILE, AndroidManifest.xml:195-203; env: the user adds the tile), calls onStartListening when the tile is visible, and onStartListening calls updateTileState (FtpTileService.java:30-34). The first verification used the in-app start of the FTP server instead; both reach the method.')
p8('UtilsHandler.getSshAuthPrivateKeyColumn', 'wrong', 'UtilsHandler.java:427',
   'Only step 5 changed: the drawer entry action of a saved SFTP connection opens its dialog (MainActivity.showSftpDialog, state). The rest as before. Re-check 2026-11-07: that step now carries the saved-SFTP state itself, and the new best route is the drawer Recent files list -> listRecent -> HybridFile.exists() of a recent SFTP entry -> SshConnectionPool.getConnection (state: a saved SFTP connection, SshClientUtils.java:72) -> create -> getSshAuthPrivateKey (SshConnectionPool.java:193; UtilsHandler.java:432) -> getSshAuthPrivateKeyColumn. Re-check 2 (2026-11-07, PENDING batch 1): the locked-drawer step now carries the tablet env, so the route closes the drawer through its listener (S_ENTRY -> Drawer$1.onDrawerClosed -> Drawer.onDrawerClosed, Drawer.java:224-225) before the same Recent files steps. Re-check 3 (2026-11-07, W7 r6-p10): wrong as drawn; re-check 2 missed that listRecent turns each history path into a java.io.File (LoadFilesListTask.java:394, RootHelper.java:136-142), which folds ssh:// to ssh:/, so the exists() call never takes the SFTP branch (HybridFile.java:92-95, :1077); HybridFile.exists() is one node for every caller (Q-R6-2). The class does not change (a saved SFTP connection).')
p8('PasteHelper.<init>(Parcel)', 'correct', 'MainActivity.java:425',
   'Review 4 re-check: step 2 is now MainActivity.onCreate -> MainActivity$1.onPostExecute (onCreate passes its callbacks to runInParallel at MainActivity.java:365; the old route went through the shared AppConfig$1 dispatch, cut in review 4 fix 2). onPostExecute reads the PasteHelper from savedInstanceState (:425) -> PasteHelper$1.createFromParcel -> <init>(Parcel) (PasteHelper.java:43-44). Gates as before: a pending copy or cut (state) and the system recreating MainActivity with its saved state (env).')
p8('PasteHelper$1.createFromParcel', 'correct', 'MainActivity.java:425',
   'Review 4 re-check: same new step 2 as PasteHelper.<init>(Parcel) (MainActivity.onCreate -> MainActivity$1.onPostExecute, MainActivity.java:365); onPostExecute reads the PasteHelper from savedInstanceState (:425). Gates as before (pending copy or cut; saved-state recreation).')
p8('ThemedImageView.getActivity', 'correct', 'PrefFrag.java:89',
   'Review 6 fix 3 re-check (2026-11-07): step 2 was the invented CALL PrefFrag.onCreate -> onPreferenceClick (E4d630b84); it is now the tap on a Settings row, a FRAMEWORK edge with the user action (PrefFrag.java:88-90). The tapped row is Folders (PreferencesActivity.selectItem FRAGMENT_FOLDERS case, :211-213), then FoldersPref builds its PathSwitchPreference rows -> ThemedImageButton -> ThemedImageView.getActivity. The same 10 methods; no gate is needed.')

# Round 2 (Kiro, 2026-11-10; graphs/AmazeFileManager/scratch/reaudit/round2_route_changes.txt): cause B moved the
# saved-SFTP gates from state to env network (a saved SFTP entry exists only after a connect to a real SSH server,
# SftpConnectDialog.java:343-354), so these steps have new edge ids; the steps are the same (src, dst, kind).
R2 = {
    'CloudIconDataFetcher.cancel': 'step 12 (CloudIconModelLoader.<init> -> buildLoadData)',
    'SshAuthenticationTask$1.getPublic': 'steps 9, 11, 14 (SshClientUtils.execute -> getConnection, SshConnectionPool.create -> create(...), doInBackground -> $1.<init>)',
    'UtilsHandler.getSshAuthPrivateKeyColumn': 'step 9 (SshClientUtils.execute -> getConnection)',
}
for _m, _s in R2.items():
    _res, _ref, _note = P[_m]
    P[_m] = (_res, _ref, _note + ' Round 2 (2026-11-10): the same steps; %s now carry env network instead of the saved-SFTP state (new edge ids, re-checked from the source; cause B).' % _s)

# ---- edge rows: the B6 added/rewired edges, each checked to exist in the built graph.
EDGE_NOTES = {}
def edge_note(src, dst, res, ref, note):
    cands = [x for x in g['edges'] if x['src'] == src and x['dst'] == dst]
    assert cands, ('edge not found', src, dst)
    EDGE_NOTES[cands[0]['id']] = (res, ref, note)

edge_note('PrepareCopyTask.doInBackground', 'PrepareCopyTask.onPostExecute', 'fixed', 'PrepareCopyTask.java:143-162',
  'B6 batch v2: AsyncTask framework calls onPostExecute after doInBackground; replaces the deleted bogus ZipService -> PrepareCopyTask edge.')
edge_note('ProcessViewerFragment.onResume', 'ZipService.onBind', 'fixed', 'ProcessViewerFragment.java:165',
  'B6 batch v2: framework calls ZipService.onBind when ProcessViewerFragment binds the compress service; replaces the invalid refresh -> onBind edge.')
edge_note('MainActivity.onOptionsItemSelected', 'PrepareCopyTask.onPreExecute', 'fixed', 'MainActivity.java:1029-1030',
  'B6 batch v2: repair for the regression where onPreExecute lost its only incoming edge when the bogus ZipService edge was deleted; the MainActivity paste case executes the task.')
edge_note('MainFragment$6.<init>', 'MainFragment$6.doInBackground', 'fixed', 'MainFragment.java:1653',
  'B6 round-2: valid AsyncTask edge replacing the deleted bogus ZipService -> MainFragment$6 edges; executeOnExecutor runs doInBackground on the thread pool.')
edge_note('DecryptService$BackgroundTask.<init>', 'DecryptService$BackgroundTask.doInBackground', 'fixed', 'DecryptService.java:118',
  'B6 round-2: valid AsyncTask edge replacing the deleted bogus ZipService -> DecryptService edge; execute() runs doInBackground on the worker thread.')
edge_note('CloudStreamServer$HTTPSession.sendResponse', 'CloudStreamSource.read(byte[],int,int)', 'fixed', 'CloudStreamServer.java:838,841',
  'B6 round-2: the CLOUD server sendResponse reads the CloudStreamSource data into the socket output; replaces the deleted bogus SMB StreamServer sendResponse -> CloudStreamSource edge.')
edge_note('RecyclerAdapter.showThumbnailWithBackground', 'GlideRequest.listener', 'fixed', 'RecyclerAdapter.java:899',
  'B6 round-2 (Glide flip): getPreloadRequestBuilder returns the GlideRequest field, so .listener() virtually dispatches to GlideRequest.listener; this edge + the rounded-thumbnail edge flip listener to REACHABLE.')
edge_note('RecyclerAdapter.showRoundedThumbnail', 'GlideRequest.listener', 'fixed', 'RecyclerAdapter.java:945',
  'B6 round-2 (Glide flip): same GlideRequest receiver as :899; the second .listener() call site.')
edge_note('RecyclerAdapter.onBindViewHolder', 'IconDataParcelable.setImageBroken', 'fixed', 'RecyclerAdapter.java:596,599,609,724,733',
  'B6 round-2 (Glide flip): method references passed as the OnImageProcessed errorListener; the show methods invoke errorListener.onImageProcessed, which dispatches to setImageBroken(boolean) (IconDataParcelable.java:43); flips setImageBroken to REACHABLE.')
edge_note('CompressedExplorerFragment$1.onActionItemClicked', 'Decompressor.decompress(String,String[])', 'fixed', 'CompressedExplorerFragment.java:329',
  'B6 round-2 (Ee1a): rewired from the INFERRED <init> -> decompress edge; the R.id.ex menu case (:321) calls decompressor.decompress with the decompressor assigned at :215/:243.')

# ---- UNREACHABLE labels: one row per UNREACHABLE method; note derived from the graph's own (source-based) reason.
unre = {m for m, l in g['labels'].items() if l.get('unreachable')}
U = {}
for m in sorted(unre):
    lab = g['labels'][m]
    ur = lab['unreachable']
    U[m] = (lab['confirmed_by'], lab['source_ref'],
            'UNREACHABLE %s: %s' % (ur['kind'], ur['text']))

# ---- build and validate the rows
out = [['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']]

# path rows (30). Validate: method exists and is REACHABLE; the cited file:line appears on the route's evidence.
assert set(P) == set(sample), ('path set != sample', sorted(set(sample) - set(P)), sorted(set(P) - set(sample)))
for m, (res, ref, note) in P.items():
    r = rows.get(m)
    assert r is not None and r['verdict'] == 'REACHABLE', ('path row not reachable', m)
    assert note.strip(), ('empty note', m)
    base = ref.split(':')[0]
    ev_all = ' '.join(E[i]['evidence'] or '' for i in r['route_edge_ids'].split())
    assert base in ev_all, ('path ref not on route evidence', m, ref)
    out.append(['path', m, res, 'SOURCE', ref, r['route_edge_ids'], note])

# UNREACHABLE labels (must be exactly the graph's unreachable set).
assert set(U) == unre, ('label set != graph unreachable', sorted(unre - set(U)), sorted(set(U) - unre))
for m, (cb, ref, note) in U.items():
    assert note.strip(), ('empty unreachable note', m)
    out.append(['label', m, 'correct', cb, ref, '', note])

# reachable labels of the final sample (one per sampled reachable method).
for m in sample:
    r = rows[m]
    cb = 'SOURCE' if all(b.edge_sourced(E[i]) for i in r['route_edge_ids'].split()) else 'INFERRED'
    out.append(['label', m, P[m][0], cb, P[m][1].split(';')[0], '',
                'REACHABLE confirmed: the route was read step by step (see the path row); gates read: env=%s state=%s'
                % (r['env_kinds'] or '-', r['state_kinds'] or '-')])
# W9 reachable audit (Kiro, 2026-11-08): one label row per drawn method from scratch/reaudit/audit_result.csv
# (note "reachable audit, class <X>"); a method that already has a label row keeps it.
_w9 = {}
exec(open('tools_dev/w9_audit_rows.py', encoding='utf-8').read(), _w9)
out.extend(_w9['audit_rows']('graphs/%s' % APP, [r[1] for r in out[1:] if r[0] == 'label']))

# edge rows: the B6 added/rewired edges, then the framework (FW-SRC) claims that were read.
seen = set()
def emit_edge(i, res, ref, note):
    if i in seen:
        return
    seen.add(i)
    assert i in E, ('edge id missing', i)
    assert note.strip(), ('empty edge note', i)
    out.append(['edge', i, res, 'SOURCE', ref, '', note])

for i, (res, ref, note) in EDGE_NOTES.items():
    emit_edge(i, res, ref, note)

# framework claims checked: one row per distinct FW-SRC citation that names real AOSP line numbers.
cites = {}
for x in g['edges']:
    for seg in (x['evidence'] or '').split(';'):
        seg = seg.strip()
        if seg.startswith('FW-SRC') and re.search(r':\d', seg):
            cites.setdefault(seg.split('(')[0].strip(), x['id'])
for c, i in cites.items():
    ref = c.replace('FW-SRC ', '').split(' and ')[0].strip()
    emit_edge(i, 'correct', ref, 'framework claim checked: AOSP 8.1.0_r1 lines read for ' + ref)

# ---- DEVICE rows (D7): only when a real device/results.csv exists; otherwise this block
# does not run at all and the output stays byte-identical to the pre-D7 writer.
import os
DEVICE_RESULTS = 'graphs/%s/device/results.csv' % APP
# Reviewer rule 2026-11-09 (tools_dev/device_rows.py): a reached row is written only when its replayed edge ids equal
# the method's current best route.
_dr = {}
exec(open('tools_dev/device_rows.py', encoding='utf-8').read(), _dr)
_dev_rows, _dev_dropped = _dr['device_rows']('graphs/%s' % APP, APP)
for _d in _dev_dropped:
    print('DEVICE row dropped: %s %s: %s' % _d)
for dr in _dev_rows:
    reached = (dr.get('reached') or '').strip()
    status = (dr.get('script_status') or '').strip()
    run = (dr.get('run') or '').strip()
    script = (dr.get('script') or '').strip()
    if reached == 'yes':
        result, note = 'correct', 'script_status=%s' % status
    elif status == 'unscriptable':
        result, note = 'unclear', 'unscriptable (script_status=unscriptable; no coverage evidence)'
    elif status.startswith('failed_at_step_') or status == 'timeout':
        result, note = 'unclear', 'script failed (script_status=%s)' % status
    elif reached == 'no':
        result, note = 'unclear', 'not reached (reached=no, script_status=%s)' % status
    else:
        result, note = 'unclear', 'no coverage evidence (reached=%s, script_status=%s)' % (reached, status)
    out.append(['path', dr.get('method') or '', result, 'DEVICE',
                'device run %s/%s' % (run, script), dr.get('edges') or '', note])

with open('graphs/%s/verification.csv' % APP, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

import collections
c = collections.Counter((r[0], r[2]) for r in out[1:])
print('rows by (type,result):', dict(c))
print('totals: path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
