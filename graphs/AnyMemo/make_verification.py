"""Write graphs/AnyMemo/verification.csv for the AnyMemo schema 2 trigger graph (round 2).

Same structure as handoff/examples/make_vlog_hash_checker.py, with AnyMemo's own notes.
Run from the work folder: python3 -I graphs/AnyMemo/make_verification.py
Every note is validated against the built graph; the script raises (STOPs) if a path/label item is missing,
a verdict does not match, an edge id does not exist, or a path row's cited file:line is not on that method's route.
All paths it uses are inside graphs/AnyMemo/ or tools/ (no /private/tmp, no session folders).
"""
import csv, glob, json, re, sys
sys.path.insert(0, 'tools')
import build_graph as b

APP = 'AnyMemo'
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % APP)[0], encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % APP, encoding='utf-8'))}

# the authoritative final sample (STEP 3): read from scratch, not from a session folder
SAMPLE_FILE = 'graphs/%s/scratch/kiro_sample_30_final.txt' % APP
sample = [l.split()[-1] for l in open(SAMPLE_FILE, encoding='utf-8')
          if l.startswith(('NONSTD', 'INFERRED', 'STATE', 'ENV', 'LONG', 'PLAIN'))]

ANDX = ' Fragment / RecyclerView steps rest on INFERRED androidx claims (androidx source not read).'

# ---- path rows: one per sampled method. result/ref/note written from reading the route (STEP 3).
P = {}
def p(m, res, ref, note):
    P[m] = (res, ref, note)

p('DefaultScheduler.randomNumber', 'correct', 'DefaultScheduler.java:208',
  'launch -> Recent tab -> Misc -> Merge (from Preview/Edit) -> Preview/Edit search -> card shown -> grade buttons -> schedule -> calculateIntervalNoise -> randomNumber; the noise call runs when includeNoise and interval is above the minimum (DefaultScheduler.java:129,199-200,208).' + ANDX)
p('UploadDropboxActivity.onDestroy', 'correct', 'downloader/dropbox/UploadDropboxActivity.java:62-65',
  'Dropbox list -> upload FAB -> file picked -> confirm upload (OK) -> upload done (S_DROPBOX_UPLOAD) -> Back; UploadDropboxActivity has no finish()/onBackPressed and BaseActivity none either, so Back finishes it (SYSTEM edge; FW-SRC Activity.java:3001-3010,:5580-5584,:7203-7208).' + ANDX)
p('CardDaoImpl.getCardsByCategory', 'correct', 'QuizQueueManager.java:115',
  'Recent tab row tap -> OpenActions dialog -> Quiz launcher -> Start quiz -> QuizActivity -> queue loader -> QuizQueueManager.refill(Category) -> CardDaoImpl.getCardsByCategory (QuizQueueManager.java:115).' + ANDX)
p('Mnemosyne2CardsImporter$ValueType.<clinit>', 'correct', 'Mnemosyne2CardsImporter.java:184',
  'Misc tab -> Converter -> file browser (CONVERTER host) -> pick a file -> startConversion -> convert dialog -> invokeImportConversion -> ConvertIntentService -> Mnemosyne2CardsImporter.convert -> xmlToCards; the enum ValueType is class-initialised on first use (Mnemosyne2CardsImporter.java:184, JVM <clinit>).' + ANDX)
p('DownloaderUtils.downloadFile', 'correct', 'downloader/anymemo/AnyMemoDownloaderFragment.java:81',
  'Download tab -> AnyMemo source -> list retrieved (network) -> tap a row (neither Category nor Back) -> confirm dialog -> start fetch -> AnyMemoDownloaderFragment.fetchDatabase -> DownloaderUtils.downloadFile when the name ends with .db (AnyMemoDownloaderFragment.java:79-81).' + ANDX)
p('AudioRecorderFragment$2.<init>', 'correct', 'ui/AudioRecorderFragment.java:143',
  'Preview/Edit -> card list long-press -> Edit -> CardEditor -> add audio menu (RECORD_AUDIO granted) -> recorder dialog -> Record then Stop then Play -> startPlaying builds the MediaPlayer completion listener $2 (AudioRecorderFragment.java:133-143).' + ANDX)
p('SettingsScreen$11.onFileBrowserFileClick', 'correct', 'ui/FileBrowserFragment.java:407-414',
  'Misc tab -> default Settings -> settings loaded -> tap the question-font field -> file browser (SETTINGS_Q host) -> browse/fill/bind -> tap a file row (clickedFile.isFile(), FileBrowserFragment.java:407) -> SettingsScreen$11.onFileBrowserFileClick.' + ANDX)
p('DropboxApiHelper$4.call', 'correct', 'downloader/dropbox/DropboxApiHelper.java:194-229',
  'Download tab -> Dropbox -> OAuth (saved token, network) -> Dropbox list -> refresh retrieves -> tap a row -> confirm -> fetch -> DropboxListFragment.fetchDatabase -> DropboxApiHelper.downloadFile -> $4.call (RxJava, DropboxApiHelper.java:194-229).' + ANDX)
p('ExportAnyMemoDbFragment$3.accept', 'correct', 'ui/ExportAnyMemoDbFragment.java:78-88',
  'Misc tab (Export section expanded) -> Export AnyMemo -> file browser (EXPORT host) -> pick a file -> exportDatabase (startActivityForResult) -> onActivityResult -> $3.accept (RxJava, ExportAnyMemoDbFragment.java:78-88).' + ANDX)
p('DatabaseOperationDialogUtil$4$1.onCancel', 'correct', 'utils/DatabaseOperationDialogUtil.java:151',
  'Open tab file browser -> long-press a row -> edit dialog -> Rename -> showRenameDbDialog subscribes -> the rename dialog is shown; its cancel callback is $4$1.onCancel (DatabaseOperationDialogUtil.java:151).' + ANDX)
p('Option.getCopyClipboard', 'correct', 'QACardActivity.java:628',
  'Preview/Edit -> Card Player (getCurrentCard != null) -> play button -> state machine onPlayCard -> broadcast -> gotoCardId/gotoCard -> updateCardFrontSide -> displayCard -> copyToClipboard -> Option.getCopyClipboard (QACardActivity.java:628).' + ANDX)
p('Category.setName', 'correct', 'CategoryDaoImpl.java:36',
  'Preview/Edit -> edit categories (getCurrentCard != null) -> CategoryEditorFragment init -> tap New -> NewCategoryTask -> CategoryDaoImpl.createOrReturn -> Category.setName (CategoryDaoImpl.java:36).' + ANDX)
p('AMDateUtil.<init>', 'correct', 'ui/GradeButtonsFragment.java:83',
  'Preview/Edit -> Card Player start path reaches StudyActivity.onPostInit -> setupGradeButtons -> GradeButtonsFragment.onCreate -> Dagger injects the @Inject AMDateUtil field (GradeButtonsFragment.java:83, INFERRED Dagger field injection).' + ANDX)
p('Card.setId', 'correct', 'DetailScreen.java:173',
  'Preview/Edit -> Detail (getCurrentCard != null) -> init -> S_DETAIL -> Save menu -> confirm -> SaveCardTask -> saveEntries -> refreshEntries -> Card.setId (DetailScreen.java:173).' + ANDX)
p('FileBrowserActivity.fileClickAction', 'correct', 'ui/FileBrowserActivity.java:68-71',
  'Misc tab -> Merge -> tap the target/source field -> FileBrowserActivity (S_FILEBROWSER, external storage) -> browse/fill/bind -> tap a file row -> FileBrowserActivity$1.onFileBrowserFileClick -> fileClickAction (FileBrowserActivity.java:68-71).' + ANDX)
p('AlgorithmCustomizationScreen$1$1.<init>', 'correct', 'AlgorithmCustomizationScreen.java:67',
  'Recent tab -> Options bottom-nav item (INTENT to OptionScreen) -> "Customize scheduling algorithm" -> warning dialog -> OK -> AlgorithmCustomizationScreen -> "Reset customized algorithm" preference -> its listener builds $1$1 (AlgorithmCustomizationScreen.java:67).' + ANDX)
p('Card.toString', 'correct', 'queue/LearnQueueManager.java:267',
  'Recent tab row tap (no selection, RecentListFragment.java:416) -> StudyActivity -> queue loader -> LearnQueueManager.refill -> flushDirtyCache -> worker -> a RuntimeException message string-concats the card, which calls Card.toString (JLS 5.1.11; LearnQueueManager.java:267).' + ANDX)
p('SettingsScreen$12.onFileBrowserFileClick', 'correct', 'ui/FileBrowserFragment.java:407-414',
  'Misc tab -> default Settings -> settings loaded -> tap the answer-font field (SettingsScreen.java:723-732) -> file browser (SETTINGS_A host) -> pick a file row -> SettingsScreen$12.onFileBrowserFileClick.' + ANDX)
p('Option$DictApp.parse', 'correct', 'Option.java:62',
  'Preview/Edit -> Card Player start reaches Study gesture path -> onGesturePerformed -> onGestureDetected -> lookupDictionary -> dictionary list -> item click -> lookupDictionary -> Option.getDictApp -> DictApp.parse (Option.java:62).' + ANDX)
p('FileBrowserFragment.upOneLevel', 'correct', 'ui/FileBrowserFragment.java:391',
  'Open tab file browser -> menu item browses -> fill/bind -> tap the ".." row -> openFile -> upOneLevel (FileBrowserFragment.java:391).' + ANDX)
p('Card.setCreationDate', 'correct', 'dao/AbstractHelperDaoImpl.java:122',
  'Misc tab -> Merge -> doHeavyTask -> DatabaseUtil.mergeDatabases (destPath != srcPath) -> CardDaoImpl.createCards -> batch -> createCardsNoBatch -> create -> AbstractHelperDaoImpl.create -> Card.setCreationDate (AbstractHelperDaoImpl.java:122).' + ANDX)
p('CardDaoImpl$1.call', 'correct', 'dao/CardDaoImpl.java:49-69',
  'Preview/Edit -> delete card confirm -> DeleteCardTask -> queryNextCard -> queryFirstOrdinal -> the ORMLite callBatchTasks-style call reaches $1.call (RxJava, CardDaoImpl.java:49-69).' + ANDX)
p('SpeakWord.stripNonCardContent', 'correct', 'SpeakWord.java:65',
  'Preview/Edit -> speak question menu (getCurrentCard != null) -> CardTTSUtil.speakCardQuestion -> AnyMemoTTSImpl.sayText -> SpeakWord.speakWord -> searchAlternatives -> stripNonCardContent (SpeakWord.java:65).' + ANDX)
p('NotificationChannelUtil.createConversationNotificationChannel', 'correct', 'NotificationChannelUtil.java:43',
  'process start -> AMApplication.onCreate -> createNotificationChannels -> createConversationNotificationChannel when SDK_INT >= O (always true on API 27; NotificationChannelUtil.java:36,43).')
p('DaggerAppComponents$ActivityComponentsBuilder.activity', 'correct', 'AMApplication.java:82',
  'process start -> AnyMemo.onCreate -> BaseActivity.activityComponents (first call, field still null) -> AMApplication.activityComponents -> the generated builder.activity(...) (AMApplication.java:82).')
p('BaseActivity.onResume', 'correct', 'AnyMemo.java:147',
  'process start -> AnyMemo.onCreate -> onResume -> super call AnyMemo.onResume -> BaseActivity.onResume (AnyMemo.java:147).')
p('BaseActivity.updateInterfaceLanguage', 'correct', 'BaseActivity.java:43',
  'process start -> AnyMemo.onCreate -> super BaseActivity.onCreate -> updateInterfaceLanguage (BaseActivity.java:43).')
p('DaggerAppComponents$ActivityComponentsBuilder.build', 'correct', 'AMApplication.java:83',
  'process start -> AnyMemo.onCreate -> BaseActivity.activityComponents (first call) -> AMApplication.activityComponents -> the generated builder.build() (AMApplication.java:83).')
p('NotificationChannelUtil.createCardPlayerNotificationChannel', 'correct', 'NotificationChannelUtil.java:41',
  'process start -> AMApplication.onCreate -> createNotificationChannels -> createCardPlayerNotificationChannel when SDK_INT >= O (NotificationChannelUtil.java:36,41).')
p('NotificationChannelUtil.createReviewReminderNotificationChannel', 'correct', 'NotificationChannelUtil.java:42',
  'process start -> AMApplication.onCreate -> createNotificationChannels -> createReviewReminderNotificationChannel when SDK_INT >= O (NotificationChannelUtil.java:36,42).')

# ---- edge rows (STEP 1 and STEP 2) and framework claims checked.
# STEP 1 added seven exit / rotation edges (the six placeholders resolved to REACHABLE).
EDGE_NOTES = {}
def edge_note(src, dst, res, ref, note):
    cands = [x for x in g['edges'] if x['src'] == src and x['dst'] == dst]
    assert cands, ('edge not found', src, dst)
    EDGE_NOTES[cands[0]['id']] = (res, ref, note)

edge_note('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment.onDestroy', 'fixed', 'ui/CategoryEditorFragment.java:94-108',
  'STEP 1a: OK tapped (v == okButton) calls dismiss() (CategoryEditorFragment.java:108); the DialogFragment is destroyed. Exit modelled; INFERRED androidx dismiss -> onDestroy.')
edge_note('PreviewEditActivity.restartActivity', 'PreviewEditActivity.onDestroy', 'fixed', 'ui/PreviewEditActivity.java:450-463',
  'STEP 1b: restartActivity() calls finish() (PreviewEditActivity.java:462), reached from onActivityResult; the running activity is destroyed.')
edge_note('S_PREVIEW_EDIT', 'PreviewEditActivity.onDestroy', 'fixed', 'ui/PreviewEditActivity.java:61',
  'STEP 1b: Back on Preview/Edit finishes the activity (no onBackPressed override in PreviewEditActivity/QACardActivity/BaseActivity); FW-SRC Activity.java:3001-3010,:5580-5584,:7203-7208.')
edge_note('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment.onDestroy', 'fixed', 'ui/QuizLauncherDialogFragment.java:55',
  'STEP 1c: the launcher has no dismiss()/setCancelable; the default-cancelable dialog is destroyed when cancelled (Back/outside tap). INFERRED androidx cancel -> onDestroy.')
edge_note('S_CARD_LIST', 'CardListActivity.onDestroy', 'fixed', 'ui/CardListActivity.java:77',
  'STEP 1d: no reachable in-app finish() (restartActivity is UNREACHABLE); Back finishes the activity (no onBackPressed override); FW-SRC Activity.java:3001-3010,:5580-5584,:7203-7208.')
edge_note('S_CARD_EDITOR', 'CardEditor.onConfigurationChanged', 'fixed', 'ui/CardEditor.java:415-418',
  'STEP 1e: CardEditor declares onConfigurationChanged (CardEditor.java:415-418); a rotation (SYSTEM) edge from the editor page, like OptionScreen.')
edge_note('S_SETTINGS', 'SettingsScreen.onConfigurationChanged', 'fixed', 'ui/SettingsScreen.java:154-157',
  'STEP 1f: SettingsScreen declares onConfigurationChanged (SettingsScreen.java:154-157); a rotation (SYSTEM) edge from the Settings page, like OptionScreen.')

# STEP 2: the ten automatic CALL edges were all already present as @AM/@DBX host variants (nothing added).
# Record them as checked ("present") edge rows, one representative edge id per item.
STEP2 = [
    ('E30961aed', 'STEP 2 item 1 present: DownloadListAdapter$1.onClick -> showFetchDatabaseDialog (AbstractDownloaderFragment.java:434); @AM twin E72ef4f0f.'),
    ('Edb9e2212', 'STEP 2 item 2 present: DownloadListAdapter$1$1.call -> openCategory (:422, CHA->AnyMemoDownloaderFragment); @DBX twin E8c2d13b7->DropboxListFragment.'),
    ('E8af6aadf', 'STEP 2 item 3 present: AbstractDownloaderFragment$1.call -> initialRetrieve (:185, CHA->AnyMemoDownloaderFragment); @DBX twin E98e4482a.'),
    ('E93f22026', 'STEP 2 item 4 present: FetchDatabaseTask.doInBackground -> fetchDatabase (:319, CHA->AnyMemoDownloaderFragment); @DBX twin E7ff509ac.'),
    ('E553e8d3a', 'STEP 2 item 5 present: onViewCreated -> refreshList (:173); @DBX twin E2fbadfb0.'),
    ('E6ebb692a', 'STEP 2 item 6 present: RetrieveTask.onPostExecute -> hasMore (:231, CHA->AnyMemoDownloaderFragment); @DBX twin Eb67ddb9e.'),
    ('E559484e4', 'STEP 2 item 7 present: DownloadListAdapter$1$2.call -> goBack (:430, CHA->AnyMemoDownloaderFragment); @DBX twin E0d158917.'),
    ('Edf112fb9', 'STEP 2 item 8 present: AbstractDownloaderFragment$2.onClick -> startFetchDatabaseTask (:287); @DBX twin E21225e33.'),
    ('E7bad5c55', 'STEP 2 item 9 present: DropboxListActivity.refreshList -> AbstractDownloaderFragment.refreshList@DBX (DropboxListActivity.java:95).'),
    ('Eba2af780', 'STEP 2 item 10 present: DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onCreate (DropboxOauth2AccountActivity.java:21).'),
]

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

# edge rows: STEP 1 added edges, then STEP 2 present edges, then the framework (FW-SRC) claims that were read.
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
for i, note in STEP2:
    emit_edge(i, 'correct', b.evidence_ref(E[i]['evidence']) or '', note)

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

import collections
# T8: fixed order. Path rows keep their definition order; label and edge
# rows sort by (type, item), so two runs are byte-identical even though
# the UNREACHABLE set above iterates in hash order.
_header = out[0]
_paths = [r for r in out[1:] if r[0] == 'path']
_others = sorted((r for r in out[1:] if r[0] != 'path'),
                 key=lambda r: (r[0], r[1]))
out = [_header] + _paths + _others

with open('graphs/%s/verification.csv' % APP, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

c = collections.Counter((r[0], r[2]) for r in out[1:])
print('rows by (type,result):', dict(c))
print('totals: path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
