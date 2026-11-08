# AmazeFileManager — B6 fix log

Every fix applied during B6 route checking, in order. "Lines printed" are the
source lines read to justify the fix. Scripts: `fix_b6.py` (batch v2),
`fix_b6_round2.py`, `fix_b6_round3.py`, `fix_b6_round4.py` (in the merger
work dir, never pushed). Backups: `backup-pre-B6fix/`, `backup-pre-B6fix2/`,
`backup-pre-B6fix3/`, `backup-pre-B6fix4/`.

## Batch v2 (fix_b6.py; rebuild 2: methods 2981, 2510/471, errors 0)

Manifest ENTRY citations, systematic shift (AndroidManifest.xml, module root
`app/src/main/AndroidManifest.xml`, printed in full):
- ExtractService :143-147 -> :165-169; ZipService :148-152 -> :170-174;
  CopyService :153-157 -> :175-179; EncryptService :159-161 -> :181-183;
  DecryptService :163-165 -> :185-187; FtpService :167-172 -> :189-194;
  FtpTileService :174-182 -> :195-203; FtpReceiver :184-192 -> :205-213
  (both START and STOP variants).
Drawer: implements clause :97 -> :99; listener line 164 -> 165.
FtpTileService: onStopListening :35-38 -> :38-42; onFtpReceiverActions ->
updateTileState :24 -> :28. FtpServerFragment: onResume register :397 -> :393;
onCreateView lambda creation :127 -> :132; startServer call :132 -> :137;
stopServer :139 -> :144. FtpNotification update -> build :84-85 -> :88-89.
FtpService EventBus edge evidence extended with the post site
(FtpService.java:227 in run() + @Subscribe :26).
CompressedExplorerFragment: goBack -> changePath :476 -> :494-495;
onCreate -> checkForExternalIntent :313 -> :319; checkForExternalIntent ->
openCompressed :519 -> :525, :799-801 -> :797-798.
MainActivity: onCreate -> goToMain :411,415,418 -> :414,416,420;
onCreate -> MainActivity$1 :372-427 -> :366. TabFragment -> MainFragment
edge given real evidence (TabFragment.java:113-141 + :351; was "(need to read)").
PasteHelper: createFromParcel -> `<init>(Parcel)` :38 -> :43-44.
FileUtils/Operations: doInBackground -> onPostExecute :486-493 -> :480-485;
onPostExecute -> scanFile :491-493 -> :484. ItemPopupMenu listener :58 -> :60.
CopyService: onStartCommand execute :159 -> :160; copyFiles :382 -> :381;
CopyService -> mkdir given real evidence (CopyService.java:446).
CryptUtil `<init>` -> encrypt :124 -> :125. SftpConnectDialog: class decl
:74 -> :75; onCreateDialog decl :123 -> :102; picker :334 -> :146;
onActivityResult decl :473 -> :303; task execute :321 -> :322.
PemToKeyPairTask: publishProgress :120 -> :118; onProgressUpdate lambda
:155-160 -> :153-157; toast call :158 -> :155.
PrepareCopyTask: onPostExecute -> onEndDialog :172 -> :162 (and duplicate
mod/01.py:5058 :145 -> :162); onEndDialog -> showDialog :218 -> :225.
SubnetScanner: construction :77 -> SmbSearchDialog.java:80; `<init>` -> run
evidence -> SmbSearchDialog.java:109 start + SubnetScanner.java:84 run;
run -> onFound :116 -> :109; onFound -> computerFound given evidence
SubnetScanner.java:173-177. SshAuthenticationTask: doInBackground decl
:107 -> :117; KeyProvider creation :130 -> :131; getType :100 -> :143;
getPublic call :141 -> :144. PrefFrag listener :92-94 -> :89.
Indicator: setViewPager listener :166 -> :167; animator call :571-575 -> :576.
CloudStream: HTTPSession thread :330-338 -> :330-339; run -> handleResponse
:358-361 -> :346; handleResponse -> serve given real evidence
(CloudStreamServer.java:491); launchCloud given MainFragment.java:930;
RecyclerAdapter -> onListItemClicked given :531,701; AppsAdapter -> shareFiles
given :170,:181-185; ShareTask edge trigger text fixed to ShareTask.onPostExecute;
ShareAdapter onBindViewHolder :61 -> :50. Streamer: super call :34 -> :33;
HTTPSession construction :179 -> :180; thread :222-224 -> :229-231;
handleResponse :229 -> :237. launchSMB :912 -> :915.
Apk factory: registerComponents :22 -> :21; build -> loader :23 -> :25.
CloudIconDataFetcher cancel :52-54 -> :55-58 (BOTH defs, graph_def.py:1889
and :4964).

Deletions (batch v2):
- BOTH `CloudIconModelFactory.<init>` -> `CloudIconModelLoader.<init>` defs
  (graph_def.py:1651 and :4985): `<init>` constructs no loader; the loader
  is constructed in build() at CloudIconModelFactory.java:24.
- mod/01.py:2514 + :2522 (bogus ZipService -> PrepareCopyTask
  onPostExecute/onPreExecute): ZipService never touches PrepareCopyTask.
- mod/01.py:3895 (invalid CustomServiceConnection$1.refresh -> ZipService.onBind):
  a progress callback does not cause onBind.

Source change (batch v2):
- graph_def.py:1185 `MainActivity.onActivityResult` -> `MainActivity.onOptionsItemSelected`
  (target PrepareCopyTask.doInBackground, evidence :1029 kept; the paste case
  at MainActivity.java:1029-1030 executes the task).

Additions (batch v2):
- PrepareCopyTask.doInBackground -> onPostExecute (FRAMEWORK, AsyncTask completion).
- ProcessViewerFragment.onResume -> ZipService.onBind (FRAMEWORK, via bindService:165).
- MainActivity.onOptionsItemSelected -> PrepareCopyTask.onPreExecute (FRAMEWORK;
  repair for the regression where onPreExecute lost its only incoming edge
  when :2522 was deleted; PrepareCopyTask.java:83-86 defines onPreExecute).

Dropped-method routes fixed in batch v2 (not in the final table):
- FtpNotification.buildNotification: Drawer :97/:164 -> :99/:165; EventBus
  registration :397 -> :393; updateNotification -> buildNotification
  :84-85 -> :88-89.
- PrepareCopyTask.lambda$showDialog$1: full re-route via the MainActivity
  paste case (see source change + additions above); paste case requires a
  pending PasteHelper (needs_state, recorded in route_table.md notes).
- StreamSource.open: RecyclerAdapter -> onListItemClicked :531,701;
  launchSMB :912 -> :915; super call :34 -> :33; HTTPSession construction
  :179 -> :180; thread :222-224 -> :229-231; handleResponse :229 -> :237.
- ZipService.onDestroy: full re-route via ProcessViewerFragment binding
  (S_ENTRY -> MainActivity.onCreate -> ProcessViewerFragment -> onCreateView
  -> onActivityCreated -> onResume -> ZipService.onBind -> onDestroy);
  manifest citation :143-147 -> :165-169.

## Round-2 (fix_b6_round2.py; rebuild 4: methods 2981, 2512/469, errors 0)

ZipService.execute cross-task sweep (the builder linked
ZipService$CompressAsyncTask.execute to every onPostExecute/doInBackground
it found; only its own compressFile edge is legitimate):
- Deleted: ZipService -> DecryptService$BackgroundTask.doInBackground,
  ZipService -> EncryptService$BackgroundTask.doInBackground,
  ZipService -> EncryptService$BackgroundTask.onPostExecute,
  ZipService -> MainFragment$6.doInBackground,
  ZipService -> MainFragment$6.onPostExecute. (The only other executor
  with execute -> onPostExecute/doInBackground edges was ZipService itself;
  verified by full-graph grep.)
- Added (required to keep the chains alive): MainFragment$6.<init> ->
  MainFragment$6.doInBackground (ASYNC, MainFragment.java:1653
  executeOnExecutor); DecryptService$BackgroundTask.<init> ->
  DecryptService$BackgroundTask.doInBackground (ASYNC, DecryptService.java:118
  execute; basename citation form — the `asynchronous/services/` form failed
  check 2 with "file not held", fixed before rebuild 4).
- EncryptService chain already valid via mod/01.py:662/664/668, so the
  getProgressHandler route re-computed via EncryptService's own chain
  (S_ENTRY -> EncryptService.<init> :181-183 -> onCreate -> onStartCommand
  -> BackgroundTask.<init> -> doInBackground -> onPostExecute ->
  finalizeNotification -> getProgressHandler).

CloudStreamSource.read:
- Deleted the bogus SMB StreamServer$HTTPSession.sendResponse ->
  CloudStreamSource.read(byte[],int,int) edge (INFERRED; the SMB server's
  data is a SmbStreamer StreamSource, never a CloudStreamSource — the two
  classes are siblings under RandomAccessStream).
- Added the faithful CloudStreamServer$HTTPSession.sendResponse ->
  CloudStreamSource.read(byte[],int,int) edge (CALL, CloudStreamServer.java:838
  open, :841 read loop; consistent with the existing sendResponse -> close
  edge at mod/01.py:509).

Ee1a:
- Rewired CompressedExplorerFragment.<init> -> Decompressor.decompress
  (String,String[]) (INFERRED, "framework calls extractFiles after
  construction" — false) to CompressedExplorerFragment$1.onActionItemClicked
  -> Decompressor.decompress(String,String[]) (CALL, SRC
  fragments/CompressedExplorerFragment.java:329; decompressor assigned
  :215/:243; guard item R.id.ex :321, menu :307). The @RarDecompressor
  variant edge (mod/01.py:6638) already existed.

Glide flips (printed app source; both methods UNREACHABLE -> REACHABLE):
- GlideRequest.listener: UNREACHABLE entry deleted (its reason, "no call
  sites found in app source", is refuted by RecyclerAdapter.java:899,:945).
  getPreloadRequestBuilder returns the GlideRequest field
  (GlideApp.with().asDrawable().centerCrop() at RecyclerPreloadModelProvider
  :30, then .load()), so .listener() virtually dispatches to
  GlideRequest.listener. Added edges showThumbnailWithBackground ->
  listener (:899) and showRoundedThumbnail -> listener (:945).
- IconDataParcelable.setImageBroken: UNREACHABLE entry deleted (its reason,
  "GREP no setImageBroken calls in app src", is refuted by the method
  references). setImageBroken(boolean) (IconDataParcelable.java:43) matches
  OnImageProcessed.onImageProcessed(boolean) (RecyclerAdapter.java:1030);
  the references at RecyclerAdapter.java:596,599,609,724,733 are passed as
  the errorListener and invoked via errorListener.onImageProcessed at
  :864,883,895,912,930,941. Added edge onBindViewHolder -> setImageBroken.
- Held (NOT flipped): GlideRequests.as (needs build-generated
  GlideRequests.java, not on disk; INFERRED delegation not added per
  SOURCE-only rule); GlideOptions 5 methods (zero app-source references on
  full-tree grep — kept UNREACHABLE); GlideRequest.clone already REACHABLE
  (AppsAdapterPreloadModel.java:45 `return request.clone().load(item);`
  confirmed at :45, not :44).
- E89e2cedd (SftpConnectDialog.lambda$null$2 -> GetSshHostFingerprintTask.execute):
  no such edge exists in the current graph (only $2 -> `<init>` /
  doInBackground / $3 / $4 edges); the :178 task creation + :199 execute
  inside the removeConnection callback (:176, guard !isEmpty(sshHostKey)
  :175) are modeled by the existing $2 links. No change; the $2-vs-$6
  lambda numbering question stays OPEN (needs bytecode/class-file order).

Citation fixes (round-2 new routes):
- ProcessViewerFragment$CustomServiceConnection$1.onUpdate ->
  lambda$onUpdate$0: ProcessViewerFragment.java:421 -> :422 (runOnUiThread lambda).
- SftpConnectDialog.onCreateDialog -> lambda$onCreateDialog$9: :131 -> :132
  (focus-change listener).
- lambda$onCreateDialog$9 -> SshConnectionPool.removeConnection: :179 -> :176.
- removeConnection -> AsyncRemoveConnection.<init>: SshConnectionPool.java:98 -> :95.
- AsyncRemoveConnection.<init> -> doInBackground: :218 -> :291.
- AsyncRemoveConnection.doInBackground -> onPostExecute: :304-307 -> :301.

## Round-3 (fix_b6_round3.py; rebuild 5: methods 2981, 2512/469, errors 0)

ReadFileTask$ReturnedValues re-route (wrong prefix):
- Deleted 4 false BasicActivity edges: TextEditorActivity.<init> ->
  BasicActivity.<init>; BasicActivity.<init> -> TextEditorActivity.onCreate;
  DatabaseViewerActivity.<init> -> BasicActivity.<init>;
  BasicActivity.<init> -> DatabaseViewerActivity.onCreate. Both activities
  extend ThemedActivity (printed TextEditorActivity.java:87,
  DatabaseViewerActivity.java:64), not BasicActivity. Safe: onCreate keeps
  its own `<init>` -> onCreate edges (:948, :924); BasicActivity.<init>
  keeps many other incoming edges. New route: S_ENTRY ->
  TextEditorActivity.<init> -> onCreate -> load -> ReadFileTask.doInBackground
  -> ReturnedValues (ENV other_app).
- Flagged (NOT changed, not on sampled routes): the wider BasicActivity
  cluster (e.g. BasicActivity -> MainActivity.onCreate, BasicActivity ->
  PreferencesActivity.onCreate) uses the same pattern, but MainActivity
  extends PermissionsActivity (:157) and PreferencesActivity extends
  ThemedActivity (:58); that cluster needs its own audit.

Citation fixes (round-3 new routes):
- CryptUtil.encrypt -> HybridFile.getOutputStream: CryptUtil.java:246
  (blank) -> :247 (the BufferedOutputStream/targetFile.getOutputStream call).
- GeneralDialogCreation.showEncryptAuthenticateDialog ->
  lambda$showEncryptAuthenticateDialog$16: :760-772 -> :752-764 (the
  .onPositive registration + body).

## Round-4 (fix_b6_round4.py; rebuild 6: methods 2981, 2512/469, errors 0)

- S_ENTRY -> TextEditorActivity.<init> manifest citation :115-125 -> :129-144
  (the old range showed the previous activity's tail + PreferencesActivity;
  the TextEditorActivity block is name :131, ACTION_VIEW + text/* :136-138).
  One edge fix, shared by all 5 TextEditorActivity routes in the final draw.
- TextEditorActivity.onCreate -> onOptionsItemSelected: :355 (blank) -> :357
  (method declaration).
- SearchTextTask.onPostExecute -> ImmutableEntry.getValue: :67-69 (shows the
  ImmutableEntry constructor) -> :91,95 (keyMapEntry.getValue() on the
  ImmutableEntry from MapEntry; MapEntry built at :67, getKey() at :88,
  getValue() at :91 and :95).
- TextEditorActivity.<init> -> SearchTextTask.<init>: false 'find' clause
  replaced with the true site — SearchTextTask created at
  TextEditorActivity.java:449 in afterTextChanged (searchBox callback).
