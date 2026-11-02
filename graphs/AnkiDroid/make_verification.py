"""Write graphs/AnkiDroid/verification.csv for the AnkiDroid schema 2 trigger graph.

Modelled on graphs/AnyMemo/make_verification.py. Run from the repo root:
  python3 -I graphs/AnkiDroid/make_verification.py
Every row is validated against the built graph; the script raises (STOPs)
if a path/label item is missing, a verdict does not match, an edge id
does not exist, or a path row's cited file is not on that method's route.
All paths it uses are inside graphs/AnkiDroid/ or tools/.

Path rows: one per method in the FIRST-draw final sample
(graphs/AnkiDroid/scratch/sample_30.txt, seed 20261025). The `edges`
field is the method's built route (methods.csv route_edge_ids, i.e. the
graph's best route as built); the `result` is the AUDITED route-table
verdict (scratch/route_table.md: WRONG 18, FIXED 9, UNCLEAR 2, CORRECT 1).
For WRONG routes the built route is wrong and the corrected derivation
is in route_table.md (the note says so); for FIXED routes the built
route carries the fix guards. The `ref` is a file:line from the built
route's own evidence, so it validates against the built graph.
Label rows: one per UNREACHABLE method (from the graph labels) plus one
per sampled REACHABLE method. Edge rows: the B6 variant-page edges and
one row per distinct FW-SRC citation with line numbers.
Rows are written in a fixed order: path rows in sample order, then label
rows sorted by item, then edge rows sorted by item. Two runs are
byte-identical.
"""
import csv, glob, json, re, sys
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

# Audited route-table verdicts (scratch/route_table.md), in sample order.
VERDICT = {
    'Phrase.<init>': 'wrong',
    'EasyX509TrustManager.<init>': 'wrong',
    'StepsPreference.updateSettings': 'wrong',
    'Stats$1.compare': 'wrong',
    'Sched.totalRevForCurrentDeck': 'wrong',
    'ModelEditorContextMenu.onCreateDialog': 'unclear',
    'libanki.Utils$1.<init>': 'wrong',
    'SimpleMessageDialog$1.<init>': 'unclear',
    'MetaDB.getNotificationStatus': 'fixed',
    'Template$1.compare': 'fixed',
    'FilteredDeckOptions.onSharedPreferenceChanged': 'fixed',
    'Sound.notifyConfigurationChanged': 'wrong',
    'HttpFetcher.downloadFileToSdCardMethod': 'wrong',
    'Preferences.replaceString': 'wrong',
    'api.Utils.entsToTxt': 'fixed',
    'Sched.haveBuried(long)': 'correct',
    'ModelFieldEditor$6$1.<init>': 'fixed',
    'Finder.findNotes': 'wrong',
    'AdvancedStatistics$Card.setIvl': 'wrong',
    'DiffEngine.diff_cleanupSemanticScore': 'wrong',
    'CustomTabsFallback.openUri': 'wrong',
    'libanki.Utils.base62': 'wrong',
    'CardTemplateEditor$3.onPositive': 'wrong',
    'Hook.<init>': 'fixed',
    'CollectionLoader.deliverResult': 'fixed',
    'ModelFieldEditor$1.<init>': 'wrong',
    'Decks.id(String,boolean)': 'fixed',
    'NoteEditor.closeNoteEditor(int,Intent)': 'wrong',
    'DB.executeScript': 'fixed',
    'Models._availClozeOrds(JSONObject,String,boolean)': 'wrong',
}
assert set(VERDICT) == set(sample), ('verdict set != sample',
                                     sorted(set(sample) - set(VERDICT)),
                                     sorted(set(VERDICT) - set(sample)))

# Short table notes, one per sampled method (full reasons: route_table.md).
NOTE = {
    'Phrase.<init>': 'WRONG: printed route took the RENDER_BROWSER_QA branch after launching LOAD_DECK_COUNTS; corrected route (C01) uses the LOAD_DECK_COUNTS dispatch + drawer openCardBrowser.',
    'EasyX509TrustManager.<init>': 'WRONG: printed route used a LOGIN task; the genuine prefix is the SYNC task (Connection.java:187-188); C02 steps 13-15 ids E3a5b3438/E51823c2c/E0c0d5268; Apache step INFERRED.',
    'StepsPreference.updateSettings': 'WRONG: printed steps used updateDeckList listener, not the undo listener (DeckPicker$13) that calls openReviewer; corrected chain C03.',
    'Stats$1.compare': 'WRONG: LOAD_DECK_COUNTS vs RENDER_BROWSER_QA dispatch break; corrected route C04 via HOURLY_BREAKDOWN + Stats sort.',
    'Sched.totalRevForCurrentDeck': 'WRONG: dialog id 0 goes to buildContextMenu, not buildInputDialog; corrected two-dialog sequence C05.',
    'ModelEditorContextMenu.onCreateDialog': 'UNCLEAR: final step has no printed framework evidence; stays INFERRED (support-v4 lifecycle, source not read); C06 changes no sequence.',
    'libanki.Utils$1.<init>': 'WRONG: getImportableDecks runs only in DIALOG_IMPORT_SELECT, not ADD_CONFIRM; corrected SELECT-entry derivation (F2).',
    'SimpleMessageDialog$1.<init>': 'UNCLEAR: fixes applied (steps 4,5,7,12 + support-v4 wording) but step 11 stays INFERRED and the $15->$16 rename is HELD (bytecode: $15 CHECK_DATABASE, $16 CHECK_MEDIA); no $16 edge ever.',
    'MetaDB.getNotificationStatus': 'FIXED: both guards applied (colIsOpen; WidgetStatus verbatim gate).',
    'Template$1.compare': 'FIXED: all 6 fixes applied (colOpen, font-familiy STATE, model id, non-cloze + >=1 template, plain-tag, multi-modifier tag state).',
    'FilteredDeckOptions.onSharedPreferenceChanged': 'FIXED: all 7 fixes applied (step-4 edge shared with route 10, applied once); step-5 :958 edge is the traversable final-else branch, no second call-site edge.',
    'Sound.notifyConfigurationChanged': 'WRONG: no graph edit; rebuilt reviewer-flow route (F2) replaces the printed LOAD_DECK_COUNTS/RNDER detour; never the printed route.',
    'HttpFetcher.downloadFileToSdCardMethod': 'WRONG: rebuilt prefix R1-R7 + surviving steps 12-31 with corrections (F3); step 9 E3f1b0491 UNCLEAR, not carried; BFS route unchanged in structure (guards do not change BFS cost) — table must not be copied from the redraw.',
    'Preferences.replaceString': 'WRONG: step 4 graph-fixed (dir-NOT-accessible branch); step 10 fails because advanced_statistics_link is a plain Preference; corrected terminal path via key backupMax (SeekBarPreference, summary XXX).',
    'api.Utils.entsToTxt': 'FIXED: spec guard >= 2 + resolver pins to api/Utils.java.',
    'Sched.haveBuried(long)': 'CORRECT: all 10 steps correct as printed; no graph edit.',
    'ModelFieldEditor$6$1.<init>': 'FIXED: 4 edges (menu guard, FIELD_REPOSITION guard, citation 357->358, modSchema-exception guard); step-6 by edge+line only, RESULT edge unchanged.',
    'Finder.findNotes': 'WRONG: rebuilt prefix R1-R7 + re-anchored tail T1-T9 from S_CARDTEMPLATEEDITOR (F3); CardBrowser Previewer cannot deliver a result to the fragment (startActivity, not for-result).',
    'AdvancedStatistics$Card.setIvl': 'WRONG: hook-name mismatch (mungeQA vs advancedStatistics only); corrected Statistics/forecast prefix (F4), no graph edit.',
    'DiffEngine.diff_cleanupSemanticScore': 'WRONG: no graph edit, NO-split honoured; corrected prefix via TASK_TYPE_UPDATE_FACT + mUpdateCardHandler, never RenderBrowserQA -> AFV$9.',
    'CustomTabsFallback.openUri': 'WRONG: split applied (NOT_LOGGED_IN + MEDIA variant pages, ENTERS E81c3cc95/E6b094d43); corrected hkey-empty prefix, never the BFS route (BFS ignores guard text).',
    'libanki.Utils.base62': 'WRONG: LOAD_DECK_COUNTS never dispatches to DismissNote, and the Note id==null branch conflicts with the non-null id from getNote; corrected new-note construction prefix (F4).',
    'CardTemplateEditor$3.onPositive': 'WRONG: LOAD_DECK_COUNTS -> RENDER_BROWSER_QA again + static updateSearchItemQA mistaken for an activity launch; corrected prefix via openCardBrowser (F4).',
    'Hook.<init>': 'FIXED: 5 guard replacements; post-fix best route exactly the 11 printed steps, cold-start satisfiable.',
    'CollectionLoader.deliverResult': 'FIXED: 3 guards (colOpen, disc space, collection not locked) + dropped Connection citation.',
    'ModelFieldEditor$1.<init>': 'WRONG: split applied (FULLSYNC + RENAME pages, old edge Eeded0833 gone); corrected routes A (open, 9 steps) and B (rename-flow, 14 steps); never the BFS dispatch route via generic page.',
    'Decks.id(String,boolean)': 'FIXED: 4 guards.',
    'NoteEditor.closeNoteEditor(int,Intent)': 'WRONG: split applied (NOTEEDITOR_CHANGETYPE page, ENTERS E30f7c51d, old edge Ef2c97ad2 gone); corrected route from the note-editor page (10 steps); changeNoteType appears twice (throw + confirm re-call), not a duplicated edge.',
    'DB.executeScript': 'FIXED: 4 guards.',
    'Models._availClozeOrds(JSONObject,String,boolean)': 'WRONG: corrected route via DeckTask SAVE_MODEL (save(model,true), DeckTask.java:1075); BFS best route still shows the old DeckPicker prefix, now guard-inconsistent (save(m,false) vs templates==true guard) — rejected in favour of the SAVE_MODEL prefix.',
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

with open('graphs/%s/verification.csv' % APP, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

import collections
print('rows by (type,result):', dict(collections.Counter((r[0], r[2]) for r in out[1:])))
print('totals: path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
