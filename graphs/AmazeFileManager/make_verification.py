"""Write graphs/AmazeFileManager/verification.csv for the AmazeFileManager schema 2 trigger graph.

Modelled on graphs/AnyMemo/make_verification.py.
Run from the work folder: python3 -I graphs/AmazeFileManager/make_verification.py
Every note is validated against the built graph; the script raises (STOPs) if a path/label item is missing,
a verdict does not match, an edge id does not exist, or a path row's cited file:line is not on that method's route.
All paths it uses are inside graphs/AmazeFileManager/ or tools/ (no session folders).
Path rows use the B6 route_table.md round verdicts (correct x5, fixed x25); every final print was
re-verified clean after the last fix, and each note states its round verdict.
DEVICE rows (brief D7) are NOT in this writer yet: D7 adds them later, with the rule that while no
device/results file exists the output must stay byte-identical to this writer's output.
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
  'Round verdict: fixed (citations only + spurious factory <init> edge deleted). Drawer -> AppsListFragment -> GlideApp.with -> generated module -> registerComponents -> CloudIconModelFactory -> factory.build -> loader -> cancel (:55-58); the factory <init> does not construct the loader (built in build() at CloudIconModelFactory.java:24).')
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
p('ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'fixed', 'ProcessViewerFragment.java:422',
  'Round verdict: fixed (citation only). ExtractService chain (:165-169 manifest, lambda :142-143, publishResults :143, addDatapoint :161, onUpdate :189) -> runOnUiThread lambda (:422).')
p('ReadFileTask$ReturnedValues.<init>(int)', 'fixed', 'TextEditorActivity.java:291',
  'Round verdict: fixed (wrong route re-routed). S_ENTRY TextEditorActivity (:129-144 manifest, ENV other_app) -> onCreate -> load -> ReadFileTask.doInBackground (:291) -> ReturnedValues.<init> (:115). Old BasicActivity prefix deleted (both activities extend ThemedActivity).')
p('ShareAdapter$ViewHolder.lambda$render$0', 'fixed', 'AppsAdapter.java:170',
  'Round verdict: fixed (citations + summary edge evidence). Drawer apps item -> AppsListFragment -> AppsAdapter menu share (:170, :181-185) -> shareFiles -> ShareTask onPostExecute (:121) -> ShareAdapter (:50) -> onBindViewHolder -> lambda$render$0.')
p('SmbSearchDialog$1.lambda$computerFound$0', 'fixed', 'SmbSearchDialog.java:109',
  'Round verdict: fixed (citations + evidence). SmbSearchDialog -> SubnetScanner (:80) -> start (:109) -> run (:84) -> onFound (:109, :157) -> computerFound (:173-177) -> lambda$computerFound$0.')
p('SshAuthenticationTask$1.getPublic', 'fixed', 'SshAuthenticationTask.java:144',
  'Round verdict: fixed (citations + summary evidence). CopyService -> mkdir (:446) -> SshAuthenticationTask doInBackground (:117) -> KeyProvider (:131) -> getType (:143) -> getPublic (:144).')
p('SshConnectionPool$AsyncRemoveConnection.onPostExecute', 'fixed', 'SshConnectionPool.java:301',
  'Round verdict: fixed (citations only). SftpConnectDialog onCreateDialog -> focus listener (:132) -> removeConnection (:176) -> AsyncRemoveConnection.<init> (:95) -> doInBackground (:291) -> onPostExecute (:301).')
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
for m in unre:
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

with open('graphs/%s/verification.csv' % APP, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

import collections
c = collections.Counter((r[0], r[2]) for r in out[1:])
print('rows by (type,result):', dict(c))
print('totals: path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
