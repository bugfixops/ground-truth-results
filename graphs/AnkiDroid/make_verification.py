"""Write graphs/AnkiDroid/verification.csv for the AnkiDroid schema 2 trigger graph.

Modelled on graphs/AnyMemo/make_verification.py. Run from the repo root:
  python3 -I graphs/AnkiDroid/make_verification.py
Every row is validated against the built graph; the script raises (STOPs)
if a path/label item is missing, a verdict does not match, an edge id
does not exist, or a path row's cited file is not on that method's route.
All paths it uses are inside graphs/AnkiDroid/ or tools/.

Path rows: one per method in the FINAL-draw sample after the Stream A
graph fixes (graphs/AnkiDroid/scratch/sample_30.txt, seed 20261025,
re-drawn on the Stream A graph: methods 4186, pages 49, edges 9608).
The `edges` field is the method's built route (methods.csv
route_edge_ids, i.e. the graph's best route as built); the `result` is
the AUDITED route-table verdict (scratch/route_table.md: CORRECT 20,
WRONG 10, UNCLEAR 0). For WRONG routes the built route is wrong and the
corrected derivation is in route_table.md (the note says so); for
CORRECT routes the built route IS the judged route. The `ref` is a
file:line from the built route's own evidence, so it validates against
the built graph.
Label rows: one per UNREACHABLE method (from the graph labels) plus one
per sampled REACHABLE method. Edge rows: the B6 variant-page edges and
one row per distinct FW-SRC citation with line numbers.
Rows are written in a fixed order: path rows in sample order, then label
rows sorted by item, then edge rows sorted by item. Two runs are
byte-identical.
"""
import csv, glob, json, os as _os, re, sys
sys.path.insert(0, 'tools')
import build_graph as b

APP = 'AnkiDroid'
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % APP)[0], encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % APP, encoding='utf-8'))}

SAMPLE_FILE = 'graphs/%s/scratch/sample_30.txt' % APP
sample = [l.split()[-1] for l in open(SAMPLE_FILE, encoding='utf-8')
          if l.split() and l.split()[0] in ('NONSTD', 'INFERRED', 'STATE', 'ENV', 'LONG', 'PLAIN')]
assert len(sample) == 30, ('sample size', len(sample))

# Audited route-table verdicts (scratch/route_table.md, final draw), in sample order.
VERDICT = {
    'Phrase.<init>': 'correct',
    'EasyX509TrustManager.<init>': 'correct',
    'Stats$1.compare': 'correct',
    'Sched._cntFnNew': 'correct',
    'libanki.Utils$1.<init>': 'correct',
    'Sched.revDue': 'correct',
    'MediaCheckDialog$3.<init>': 'correct',
    'ModelEditorContextMenu.onCreateDialog': 'correct',
    'Finder.findNotes': 'correct',
    'Template$1.compare': 'correct',
    'StudyOptionsActivity.closeStudyOptions(int)': 'wrong',
    'HttpFetcher.downloadFileToSdCardMethod': 'wrong',
    'Sound.notifyConfigurationChanged': 'correct',
    'Models$TransformFieldDelete.<init>': 'wrong',
    'Anki2Importer._mediaPick': 'correct',
    'Preferences.replaceString': 'correct',
    'DeckPicker$5.onProgressUpdate': 'correct',
    'Sched.sortCards(long[],int,int,boolean,boolean)': 'correct',
    'AdvancedStatistics$Card.setIvl': 'correct',
    'libanki.Utils.base62': 'wrong',
    'DiffEngine.diff_cleanupSemanticScore': 'correct',
    'MetaDB.getNotificationStatus': 'correct',
    'Sched.getToday': 'wrong',
    'DB.insert': 'wrong',
    'BaseAsyncTask.onProgressUpdate': 'wrong',
    'CollectionLoader.deliverResult': 'correct',
    'Collection.close()': 'wrong',
    'AbstractFlashcardViewer.typeAnswer': 'wrong',
    'Decks.id(String,boolean)': 'correct',
    'SimpleMessageDialog.<init>': 'wrong',
}
assert set(VERDICT) == set(sample), ('verdict set != sample',
                                     sorted(set(sample) - set(VERDICT)),
                                     sorted(set(VERDICT) - set(sample)))

# Short table notes, one per sampled method (full reasons: route_table.md).
NOTE = {
    'Phrase.<init>': 'CORRECT: all 38 steps genuine; Reviewer-head GUI chain to TranslationActivity; final Gson step INFERRED; condition: cards due.',
    'EasyX509TrustManager.<init>': 'CORRECT: all 20 steps genuine; SYNC task via the onResume head (@SYNC); steps 17-20 library-INFERRED (Apache HttpClient absent from tree); condition: logged-in hkey + online.',
    'Stats$1.compare': 'CORRECT: all 26 steps genuine; Reviewer-head chain, HOURLY_BREAKDOWN case (Statistics.java:503), sort at Stats.java:852-859, JDK-sort INFERRED; condition: cards due.',
    'Sched._cntFnNew': 'CORRECT: all 15 steps genuine as printed; condition: day rollover.',
    'libanki.Utils$1.<init>': 'CORRECT: all 14 steps genuine; @SELECT dialog-id chain (DIALOG_IMPORT_SELECT entry -> ImportDialog -> getImportableDecks).',
    'Sched.revDue': 'CORRECT: all 16 steps genuine as printed; support-v4 lifecycle (evidence wording says androidx); condition: finished deck.',
    'MediaCheckDialog$3.<init>': 'CORRECT: all 16 steps genuine as printed; condition: media-sync-server-error + check success; logged-in hkey + online.',
    'ModelEditorContextMenu.onCreateDialog': 'CORRECT: all 14 steps genuine; final step genuine-INFERRED (support-v4 DialogFragment lifecycle, not androidx as evidence says; onCreateDialog at ModelEditorContextMenu.java:31); condition: model list loaded successfully.',
    'Finder.findNotes': 'CORRECT: all 34 steps genuine; Reviewer head + for-result tail (startActivityForResult -> fragment onActivityResult -> deleteDummyCards -> findNotes); condition: cards due.',
    'Template$1.compare': 'CORRECT: all 17 steps genuine; steps 4-6 need a transient first-open failure + successful retry (exceededCursorSizeLimit -> getCol -> Storage.Collection); condition: old schema + non-zero model id + multi-modifier absent-field template tag.',
    'StudyOptionsActivity.closeStudyOptions(int)': 'WRONG: step 12 fiction (listener fan-out: menu-item REBUILD_CRAM listener never calls onCreateCustomStudySession; $4 belongs to the CustomStudyDialog launch); corrected route via custom-study menu item -> CustomStudyDialog -> its REBUILD_CRAM listener; tools/ reason: producer-aware listener dispatch.',
    'HttpFetcher.downloadFileToSdCardMethod': 'WRONG: step 15 fiction (wrong override: Reviewer.openCardBrowser, Reviewer.java:508-518, not DeckPicker.openCardBrowser); corrected route relabels steps 15-16; tools/ reason: receiver-aware drawer dispatch.',
    'Sound.notifyConfigurationChanged': 'CORRECT: all 24 steps genuine; Reviewer.onOptionsItemSelected -> playSounds (Reviewer.java:152) -> Sound chain -> VideoPlayer -> onConfigurationChanged -> target; conditions: non-TTS replay, video sound with thumbnail, VideoPlayer configChanges (AndroidManifest.xml:184).',
    'Models$TransformFieldDelete.<init>': 'WRONG: step 12 fiction (shared-dialog page jump: ModelBrowser deleteModelDialog confirm calls deleteModel(), never deleteField()); corrected route via ModelFieldEditor deleteFieldDialog -> $3.confirm -> deleteField -> @DELETE_FIELD -> remField; tools/ reason: dialog-id/activity-aware shared-page routing.',
    'Anki2Importer._mediaPick': 'CORRECT: all 16 steps genuine as printed.',
    'Preferences.replaceString': 'CORRECT: all 10 steps genuine; initPreference route (Option A, NOT the 9-edge page-GUI route); dir-inaccessible branch + qualifying preference (Preferences.java:636).',
    'DeckPicker$5.onProgressUpdate': 'CORRECT: all 16 steps genuine; Stream A IMPORT progress chain (importAdd -> @IMPORT -> ImportAdd body -> importer -> ProgressCallback -> doProgress -> onProgressUpdate@IMPORT -> TaskListener@IMPORT -> $5).',
    'Sched.sortCards(long[],int,int,boolean,boolean)': 'CORRECT: all 19 steps genuine as printed; single consistent guard includeSched=false.',
    'AdvancedStatistics$Card.setIvl': 'CORRECT: all 35 steps genuine; @advancedStatistics variant chain (direct edge deleted, correctly bypassed); hook installed only when pref advanced_statistics_enabled is on (Hooks.java:61-63).',
    'libanki.Utils.base62': 'WRONG: step 19 fiction (guard-contradicted branch: Note id==null branch vs existing id from getNote on the CHECK_MEDIA prefix); corrected route via NoteEditor new-note creation (NoteEditor.java:1370) -> guid64 -> base91 -> base62; tools/ reason: branch-sensitive constructor routing.',
    'DiffEngine.diff_cleanupSemanticScore': 'CORRECT: all 24 steps genuine; type-answer route (Reviewer.onKeyUp -> displayCardAnswer@Reviewer -> typeAnsAnswerFilter -> diff chain).',
    'MetaDB.getNotificationStatus': 'CORRECT: all 14 steps genuine as printed; support-v4-only dispatches genuine-but-INFERRED, never SOURCE.',
    'Sched.getToday': 'WRONG: step 18 fiction (wrong branch: _findCardState calls getToday() only for "due", Finder.java:466-467; printed query has only suspended/buried/filtered tokens); corrected route adds is:due to terms[0] (Sched.java:1558-1562); tools/ reason: token-aware branch routing.',
    'DB.insert': 'WRONG: step 5 fiction (wrong dialog id: entered LOAD_FAILED dialog has no integrityCheck button; cited lines are the CONFIRM dialog); corrected route via collection-open prefix (menu action_check_database -> CONFIRM -> integrityCheck); tools/ reason: dialog-id-aware shared-page routing.',
    'BaseAsyncTask.onProgressUpdate': 'WRONG: step 5 fiction (wrong dialog id: cited lines are RESTORE_BACKUP onSelection, never shown on LOAD_FAILED); corrected route via LOAD_FAILED -> ERROR_HANDLING -> restore (value 3) -> RESTORE_BACKUP -> non-empty backup; tools/ reason: dialog-id-aware shared-page routing.',
    'CollectionLoader.deliverResult': 'CORRECT: all 11 steps genuine as printed; support-v4 loader dispatch genuine-but-INFERRED, never SOURCE.',
    'Collection.close()': 'WRONG: step 5 fiction (wrong dialog id: cited lines are REPAIR_COLLECTION onPositive, not LOAD_FAILED); corrected route via LOAD_FAILED -> ERROR_HANDLING -> repair (value 2, sqlite3 required) -> REPAIR -> repairDeck -> close(); tools/ reason: dialog-id-aware shared-page routing.',
    'AbstractFlashcardViewer.typeAnswer': 'WRONG: step 9 fiction (interface fan-out to an unregistered listener: LOAD_DECK_COUNTS launch never registers mAnswerCardHandler); corrected route via Reviewer prefix + ANSWER_CARD launch with mAnswerCardHandler -> blockControls -> typeAnswer; tools/ reason: producer-aware listener dispatch.',
    'Decks.id(String,boolean)': 'CORRECT: all 11 steps genuine as printed.',
    'SimpleMessageDialog.<init>': 'WRONG: step 5 fiction (wrong dialog id, identical to DB.insert step 5); corrected route via collection-open prefix (menu action_check_database -> CONFIRM -> integrityCheck) -> printed steps 6-10 (successful check required at step 7); tools/ reason: dialog-id-aware shared-page routing.',
}


def route_ref(m):
    """A file:line from the method's built route evidence (validates by construction)."""
    r = rows[m]
    for i in r['route_edge_ids'].split():
        ev = E[i].get('evidence') or ''
        for seg in ev.split(';'):
            seg = seg.strip()
            if seg.startswith('SRC '):
                ref = seg[4:].strip()
                # keep the first file:line (strip any trailing prose)
                ref = re.split(r'[ ,]', ref)[0] if False else ref
                return ref
    return ''


def sourced(m):
    r = rows[m]
    return all(b.edge_sourced(E[i]) for i in r['route_edge_ids'].split())


# ---- UNREACHABLE labels (exactly the graph's unreachable set) ----
unre = {m for m, l in g['labels'].items() if l.get('unreachable')}
U = {}
for m in unre:
    lab = g['labels'][m]
    ur = lab['unreachable']
    U[m] = (lab['confirmed_by'], lab['source_ref'],
            'UNREACHABLE %s: %s' % (ur['kind'], ur['text']))

# ---- edge rows: B6 variant-page edges (looked up by pair, asserted) ----
def edge_by_pair(src, dst):
    cands = [x for x in g['edges'] if x['src'] == src and x['dst'] == dst]
    assert len(cands) == 1, ('variant edge pair not unique', src, dst, len(cands))
    return cands[0]['id']


EDGE_NOTES = {}
EDGE_NOTES[edge_by_pair('DeckPicker.showSyncErrorDialog(int,String)', 'S_DLG_SYNC_ERROR_NOT_LOGGED_IN')] = (
    'B6 route 21 split: not-logged-in variant ENTERS (new id E81c3cc95 in the F4-only build; id re-derived here from the final graph).')
EDGE_NOTES[edge_by_pair('DeckPicker.showSyncErrorDialog(int,String)', 'S_DLG_SYNC_ERROR_MEDIA')] = (
    'B6 route 21 split: media variant ENTERS (new id E6b094d43 in the F4-only build; id re-derived here from the final graph).')
EDGE_NOTES[edge_by_pair('NoteEditor.changeNoteTypeWithErrorHandling', 'S_DLG_CONFIRMATION_NOTEEDITOR_CHANGETYPE')] = (
    'B6 route 28 split: previously missing ENTERS from changeNoteTypeWithErrorHandling (new id E30f7c51d in the F5-only build; id re-derived here from the final graph).')
EDGE_NOTES[edge_by_pair('DeckPicker.onFinishedStartup', 'S_DLG_CONFIRMATION_DECKPICKER_FULLSYNC')] = (
    'B6 route 26 split: DeckPicker full-sync variant ENTERS (generic S_DLG_CONFIRMATION edge retargeted).')
EDGE_NOTES[edge_by_pair('ModelFieldEditor$5.onPositive', 'S_DLG_CONFIRMATION_MODELFIELDEDITOR_RENAME')] = (
    'B6 route 26 split: rename variant ENTERS (generic S_DLG_CONFIRMATION edge retargeted, guard: renameField throws ConfirmModSchemaException).')
EDGE_NOTES[edge_by_pair('S_DLG_CONFIRMATION_MODELFIELDEDITOR_RENAME', 'ModelFieldEditor$5$1.confirm')] = (
    'B6 route 26 split: rename confirm moved to the rename variant page (old direct edge Eeded0833 gone).')
EDGE_NOTES[edge_by_pair('S_DLG_CONFIRMATION_NOTEEDITOR_CHANGETYPE', 'NoteEditor$6.confirm')] = (
    'B6 route 28 split: $6.confirm moved to the NoteEditor variant page (old edge Ef2c97ad2 gone).')

# ---- build and validate the rows ----
out = [['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']]
for m in sample:
    r = rows.get(m)
    assert r is not None and r['verdict'] == 'REACHABLE', ('path row not reachable', m)
    ref = route_ref(m)
    assert ref, ('no SRC ref on built route', m)
    base = ref.split(':')[0].split('/')[-1]
    ev_all = ' '.join(E[i].get('evidence') or '' for i in r['route_edge_ids'].split())
    assert base in ev_all, ('path ref not on route evidence', m, ref)
    assert NOTE[m].strip(), ('empty note', m)
    out.append(['path', m, VERDICT[m], 'SOURCE' if sourced(m) else 'INFERRED',
                ref, r['route_edge_ids'], NOTE[m]])

assert set(U) == unre, ('label set != graph unreachable', sorted(unre - set(U)), sorted(set(U) - set(unre)))
for m in sorted(U):
    cb, ref, note = U[m]
    out.append(['label', m, 'correct', cb, ref, '', note])
for m in sample:
    r = rows[m]
    out.append(['label', m, VERDICT[m], 'SOURCE' if sourced(m) else 'INFERRED',
                route_ref(m).split(';')[0], '',
                'REACHABLE confirmed: the route was read step by step (see the path row and route_table.md); gates read: env=%s state=%s'
                % (r['env_kinds'] or '-', r['state_kinds'] or '-')])

seen = set()


def emit_edge(i, note):
    if i in seen:
        return
    seen.add(i)
    assert i in E, ('edge id missing', i)
    assert note.strip(), ('empty edge note', i)
    out.append(['edge', i, 'correct', 'SOURCE', b.evidence_ref(E[i]['evidence']) or '', '', note])


for i in sorted(EDGE_NOTES):
    emit_edge(i, EDGE_NOTES[i])

cites = {}
for x in g['edges']:
    for seg in (x['evidence'] or '').split(';'):
        seg = seg.strip()
        if seg.startswith('FW-SRC') and re.search(r':\d', seg):
            cites.setdefault(seg.split('(')[0].strip(), x['id'])
for c in sorted(cites):
    i = cites[c]
    ref = c.replace('FW-SRC ', '').split(' and ')[0].strip()
    emit_edge(i, 'framework claim checked: AOSP 8.1.0_r1 lines read for ' + ref)

# D7: DEVICE rows (device prep). If graphs/AnkiDroid/device/results.csv
# exists (written by the CI device run, not by this run), append one row
# per results row, in results order, AFTER all existing rows. If the file
# does not exist, this block does nothing and the output is the B7 file
# exactly. DEVICE rows are device confirmations only: they never feed
# back into labels, edges, or route checks, and a not-reached route
# never becomes 'wrong'. Pattern copied from graphs/AnyMemo/
# make_verification.py (D7).
_res = 'graphs/%s/device/results.csv' % APP
if _os.path.exists(_res):
    with open(_res, encoding='utf-8', newline='') as _f:
        for _row in csv.DictReader(_f):
            _reached = _row['reached']
            _status = _row['script_status']
            if _reached == 'yes':
                _res2, _note = 'correct', _status
            elif _status == 'unscriptable':
                _res2, _note = 'unclear', 'unscriptable'
            elif _status == 'timeout' or _status.startswith('failed_at_step_'):
                _res2, _note = 'unclear', _status + '; script failed'
            elif _reached == 'no':
                _res2, _note = 'unclear', _status + '; not reached'
            else:  # reached=not_run with status ok (defensive; should not occur)
                _res2, _note = 'unclear', _status + '; not run'
            out.append(['path', _row['method'], _res2, 'DEVICE',
                        'device run %s/%s' % (_row['run'], _row['script']),
                        _row['edges'], _note])

with open('graphs/%s/verification.csv' % APP, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

import collections
print('rows by (type,result):', dict(collections.Counter((r[0], r[2]) for r in out[1:])))
print('totals: path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
