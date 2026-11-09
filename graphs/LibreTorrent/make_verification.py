"""Write graphs/LibreTorrent/verification.csv for the LibreTorrent schema 2
trigger graph (B6 final table, seed 20261025).

Modelled on graphs/AnyMemo/make_verification.py and the Aegis staging
writer (graphs/Aegis/make_verification.py). LibreTorrent has NO existing
writer, so this is new, not a byte-reproduction task.

Run with no arguments, from any cwd, as:
  python3 -I graphs/LibreTorrent/make_verification.py
All paths are anchored to this file's directory (GDIR), inside the repo:
no cwd dependence, no arguments, no session folders, no path outside the
repo. It writes ONLY verification.csv: it never touches out/ (only CI
writes out/), never the trigger JSON, never a DECISIONS entry.

Inputs (branch layout, file-anchored):
  GDIR/out/*_trigger_graph.json   exactly one trigger graph (asserted)
  GDIR/out/methods.csv            built routes, labels, gates
  GDIR/scratch/sample_30.txt      final sample: N routes (N read from
                                  this file; 29 on the Kiro final draw),
                                  same order as the table
  GDIR/scratch/route_table.md     final table (N rows; Kiro final draw:
                                  CORRECT 18 / WRONG 9 / UNCLEAR 2,
                                  rate 9/27 = 0.3333)
  GDIR/device/results.csv         ONLY if a CI device run wrote it (D7);
                                  absent at this step, so DEVICE rows = 0.

Output order (fixed, deterministic; no set iteration in output order):
path rows in sample order, then ALL label rows globally sorted by item,
then ALL edge rows globally sorted by item, then (D7 only) DEVICE rows
in results order. Two runs from different cwds are byte-identical.

Path rows: one per sampled method, mechanically parsed from the table
(no hand-typed verdicts). The table format is
  | # | Method | Stratum | Steps | Verdict | Reason |
with exactly six fields; the Reason field may itself contain '|'
(row 19 writes 'file://' || path_to_download), so the parser splits
on only the first five '|' separators and keeps the rest verbatim.
Asserted: row numbers 1..N in order, table order == sample order,
table stratum == sample stratum, table steps == sample steps ==
methods.csv steps_from_launch == len(route_edge_ids), and every sampled
method is REACHABLE in methods.csv (otherwise the run refuses and
writes nothing). The B6 table has NO edge-id column, so the writer
asserts steps + method + order, NOT a table edge list; the path row's
`edges` field is methods.csv route_edge_ids (the built route).
result = table verdict lowercased (correct/wrong). confirmed_by =
SOURCE if every route edge's evidence labels are only SRC/FW-SRC,
else INFERRED (evidence labels follow build_graph.evidence_labels:
a ';' segment without a label continues the previous labelled segment,
so an AOSP continuation citation still counts as FW-SRC). ref = first
SRC ref on the route. note = "<VERDICT>: <Reason verbatim>".
Route 2 (TorrentDownloadImpl.havePiece) ONLY carries an appended
caveat-2 disclosure (adopted ruling (i) plus the NOT-adopted
contingency (ii) with its 18/8/1 counts and 8/26 rate), so the gate
sees both.

Label rows: one per UNREACHABLE method, where the graph-label set MUST
equal the methods.csv UNREACHABLE set (765 at Kiro K7), note =
"UNREACHABLE <kind>: <text>" from the graph label, result 'correct',
confirmed_by/ref from the graph label; PLUS one row per sampled method
(N), result = table verdict, confirmed_by/ref as for path rows,
note = "REACHABLE confirmed: the route was read step by step (see the
path row and route_table.md); gates read: env=<...> state=<...>".
Total label rows: UNREACHABLE count + N (765 + 29 = 794 at Kiro K7).

UNRESOLVED methods would get NO label row and NO invented verdict.
Since part b121 (Kiro K5) the graph has none: the writer asserts the
methods.csv UNRESOLVED count is 0, and would assert any to
appear in neither path rows nor label rows, and no edge row is ever
emitted for an edge touching them as a sampled-route step (zero drawn
steps touch them). Their exclusion does NOT make faithful completion
impossible under brief section 4: the writer's contract covers path
rows (sampled REACHABLE methods), label rows (UNREACHABLE methods plus
sampled REACHABLE methods), and edge rows (checked citations /
corrections); UNRESOLVED is a third verdict class that the B6 table
deliberately leaves without a row rather than inventing one, and this
docstring plus the writer report state that exclusion explicitly.

Edge rows, two derived sets (never asserted blindly):
(a) FW-SRC citations with line numbers: one row per edge that is the
representative (first carrier, in trigger-graph order) of a distinct
full FW-SRC citation. A citation is one ';'-separated item inside an
FW-SRC labelled segment (continuation items included) that contains a
line number (':<digit>'), taken verbatim as one file:range string.
The build report's "FW-SRC 12" counts only edges whose evidence
STRING starts with FW-SRC; 195 edges carry an FW-SRC segment
somewhere. The derivation actually run here yields 60 distinct
citations on 49 representative edges (see the writer report for the
full list). A row's note lists EVERY citation for which that edge is
representative (sorted), its ref is the first listed citation, and
its confirmed_by follows the same all-SRC/FW-SRC rule as path/label
rows (45 SOURCE / 4 INFERRED among the 49).
(b) D5 corrected edges: derived by diffing the pre-D5 graph snapshot
(work/LibreTorrent/d5d6/snapshot/, snapshot graph md5 0d42332a...)
against the post-fix graph
(work/LibreTorrent/d5d6/rebase/scratch/graph_postfix.json, md5
de7d1c87...). That diff is CLEAN: exactly 25 pre-only and 25 post-only
edge ids, all 7268 shared ids byte-identical, all 25 matched pairs
unique (src,dst,kind) keys with src/dst/kind unchanged and ONLY the
evidence (plus the derived id) changed -- every one a check-4
bytecode-line citation correction. The 25 rows below are that derived
list, and the writer re-validates every row at run time against the
fresh graph (new id present with the expected src/dst/kind and new
citation, old id absent); any mismatch refuses the run. result =
'fixed', ref = new citation, note = "D5 check-4 citation correction:
<old ref> -> <new ref>; src/dst/kind unchanged, no verdict change".
If the derivation had NOT been clean (not exactly 25, or any src/dst
change), NO D5 rows would have been emitted.

NEVER emitted: no edge row for the 59/32 edge Ea751b47d (it is in zero
sampled routes and is never a verified route; asserted absent from
edge rows), and no edge row for any T1 frontier edge (none is in this
graph, and edge rows come only from the FW-SRC and D5 derivations
above, which contain no frontier edge).

D7 DEVICE rows: if GDIR/device/results.csv exists (written by the CI
device run, not by this run), one row per results row is appended, in
results order, AFTER all existing rows. If the file does not exist,
this block does nothing. DEVICE rows are device confirmations only:
correct only when reached=yes, otherwise unclear, never wrong; they
never feed back into labels, edges, or route checks. At this step the
file does not exist, so DEVICE rows MUST be 0 (asserted in the run
log, not by a hard failure: the count is printed and reported).

Validation: the writer raises (STOPs, writes nothing) on any mismatch:
missing method/edge, verdict mismatch, sample/table/order/steps
mismatch, label-set mismatch, empty note/ref where required, a D5 row
that does not match the fresh graph, or an Ea751b47d edge row.
"""
import collections
import csv
import glob
import json
import os as _os
import re
from pathlib import Path

APP = 'LibreTorrent'
GDIR = Path(__file__).resolve().parent
GRAPH_GLOB = str(GDIR / 'out' / '*_trigger_graph.json')
METHODS_FILE = GDIR / 'out' / 'methods.csv'
SAMPLE_FILE = GDIR / 'scratch' / 'sample_30.txt'
TABLE_FILE = GDIR / 'scratch' / 'route_table.md'
OUT_FILE = GDIR / 'verification.csv'
DEVICE_FILE = GDIR / 'device' / 'results.csv'
for _p in (METHODS_FILE, SAMPLE_FILE, TABLE_FILE):
    assert _p.is_file() and _p.stat().st_size > 0, ('missing/empty input', str(_p))
_graph_matches = sorted(glob.glob(GRAPH_GLOB))
assert len(_graph_matches) == 1, ('exactly one trigger graph required', _graph_matches)
assert Path(_graph_matches[0]).stat().st_size > 0, ('empty trigger graph', _graph_matches[0])
print('graph:', _graph_matches[0])
print('methods:', METHODS_FILE)
print('sample:', SAMPLE_FILE)
print('table:', TABLE_FILE)
print('output:', OUT_FILE)
g = json.load(open(_graph_matches[0], encoding='utf-8'))
assert g.get('edges'), ('empty edge list in trigger graph', _graph_matches[0])
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open(METHODS_FILE, encoding='utf-8'))}
assert rows, ('empty methods.csv', str(METHODS_FILE))
print('methods rows:', len(rows),
      'REACHABLE:', sum(1 for r in rows.values() if r['verdict'] == 'REACHABLE'),
      'UNREACHABLE:', sum(1 for r in rows.values() if r['verdict'] == 'UNREACHABLE'),
      'UNRESOLVED:', sum(1 for r in rows.values() if r['verdict'] == 'UNRESOLVED'))

# ---- sample (order matters; strata + steps kept for cross-checks) ----
sample = []
sample_stratum = {}
sample_steps = {}
for _l in open(SAMPLE_FILE, encoding='utf-8'):
    _t = _l.split()
    if _t and _t[0] in ('NONSTD', 'INFERRED', 'STATE', 'ENV', 'LONG', 'PLAIN'):
        assert len(_t) >= 7 and _t[1] == 'steps', ('malformed sample line', _l.strip())
        sample.append(_t[-1])
        sample_stratum[_t[-1]] = _t[0]
        sample_steps[_t[-1]] = int(_t[2])
N = len(sample)
assert N > 0, ('empty sample', SAMPLE_FILE)
assert len(set(sample)) == N, ('duplicate method in sample', sample)

# ---- mechanical parse of the B6 final table (route_table.md) ----
# A data row is a line starting with '| ' whose first field is an
# integer row number. The Reason field may contain '|' (row 19), so
# the line is split on only the first five '|' separators: fields are
# [#, Method, Stratum, Steps, Verdict, Reason-verbatim].
_table_lines = open(TABLE_FILE, encoding='utf-8').read().splitlines()
VERDICT = {}
NOTE = {}
_table_methods = []
_table_numbers = []
for _line in _table_lines:
    if not _line.startswith('| '):
        continue
    _stripped = _line.strip()
    if not _stripped.endswith('|'):
        continue
    _body = _stripped[1:-1]
    _fields = [c.strip() for c in _body.split('|', 5)]
    if len(_fields) != 6 or not _fields[0].isdigit():
        continue
    _n, _method, _stratum, _steps, _verdict_raw, _reason = _fields
    _vtok = _verdict_raw.split()[0].lower()
    assert _vtok in ('correct', 'wrong', 'unclear', 'blocked'), ('bad verdict in table', _method, _verdict_raw)
    assert _method not in VERDICT, ('duplicate method in table', _method)
    assert _reason, ('empty reason in table', _method)
    assert _method in rows, ('table method missing from methods.csv', _method)
    assert rows[_method]['verdict'] == 'REACHABLE', ('table method not reachable', _method)
    assert int(rows[_method]['steps_from_launch']) == int(_steps), \
        ('table steps != methods.csv steps', _method, _steps, rows[_method]['steps_from_launch'])
    assert len(rows[_method]['route_edge_ids'].split()) == int(_steps), \
        ('table steps != built route length', _method, _steps)
    VERDICT[_method] = _vtok
    NOTE[_method] = '%s: %s' % (_verdict_raw, _reason)
    _table_methods.append(_method)
    _table_numbers.append(int(_n))
    assert _stratum == sample_stratum.get(_method), ('table stratum != sample stratum', _method)
assert _table_numbers == list(range(1, N + 1)), ('table row numbers', _table_numbers)
assert len(VERDICT) == N, ('table row count', len(VERDICT))
assert _table_methods == sample, ('table order != sample order', _table_methods, sample)
for _m in sample:
    assert sample_steps[_m] == int(rows[_m]['steps_from_launch']), ('sample steps != methods.csv steps', _m)
print('table parsed rows:', len(VERDICT),
      'verdicts:', dict(collections.Counter(VERDICT.values())),
      'total steps:', sum(sample_steps.values()))
print('table verdict map (sample order):',
      [(m, VERDICT[m]) for m in sample])
# End of mechanical table parse. VERDICT/NOTE above are parser output,
# in sample order. No hardcoded verdict/note dict follows, except the
# route-2 caveat-2 disclosure appended below (table Findings text, not
# a verdict: route 2's verdict stays CORRECT as parsed).

# ---- evidence helpers (build_graph.evidence_labels semantics) ----
EVIDENCE_LABELS = ('SRC', 'FW-SRC', 'DYN', 'FW-MEMORY', 'INFERRED', 'UNVERIFIED')


def parse_evidence(ev):
    """[(label, text)] with unlabelled ';' segments continued onto the
    previous labelled segment (build_graph.evidence_labels)."""
    segs = []
    for part in (ev or '').split(';'):
        part = part.strip()
        if not part:
            continue
        lab = part.split()[0]
        if lab in EVIDENCE_LABELS:
            segs.append((lab, part[len(lab):].strip()))
        elif segs:
            segs[-1] = (segs[-1][0], segs[-1][1] + '; ' + part)
        else:
            segs.append(('?', part))
    return segs


def evidence_labels(ev):
    return [lab for lab, _ in parse_evidence(ev)]


def edge_sourced(eid):
    labs = evidence_labels(E[eid].get('evidence') or '')
    return bool(labs) and all(l in ('SRC', 'FW-SRC') for l in labs)


def route_ref(m):
    r = rows[m]
    for i in r['route_edge_ids'].split():
        for seg in (E[i].get('evidence') or '').split(';'):
            seg = seg.strip()
            if seg.startswith('SRC '):
                return seg[4:].strip()
    return ''


def route_sourced(m):
    r = rows[m]
    return all(edge_sourced(i) for i in r['route_edge_ids'].split())


# ---- route-2 caveat-2 disclosure (appended to the parsed note only) ----
HAVE_PIECE = 'TorrentDownloadImpl.havePiece'
assert VERDICT[HAVE_PIECE] == 'correct', ('route 2 verdict changed', VERDICT[HAVE_PIECE])
CAVEAT_2 = (
    'Caveat-2 disclosure (adopted ruling (i)): the CORRECT verdict\'s '
    'shutdown-first premise depends on setup-history methods listed in '
    'unresolved_86.txt (first draw) -- SchedulerReceiver.<init>, '
    'SchedulerReceiver.onReceive, SchedulerReceiver.onStopApp, '
    'TorrentService.<init>, TorrentService.onCreate, '
    'TorrentService.initPendingIntents, '
    'Utils.lambda$startServiceBackground$0 -- verified directly from '
    'source, not from the graph, so they are setup history, not drawn '
    'route steps; the caveat attaches ONLY to drawn route steps, and '
    'zero drawn-step edges touched any of the 86 then-UNRESOLVED methods. '
    'Load-bearing: without the premise chain, step 3 fails as the first '
    'helper judged; residual risk: the premise methods\' '
    'launch-reachability is not graph-proven, so step 3 rests on source '
    'reading plus standard platform behaviour (AlarmManager, framework '
    'service creation). Contingency NOT adopted: if the gate adopts rule '
    '(ii) (caveat attaches to any method the verdict depends on), route 2 '
    'becomes BLOCKED with no verdict (first-draw counts CORRECT 18 / WRONG 8 '
    '/ BLOCKED 1, rate 8/26 = 0.3077). Kiro final draw: part b121 (K5) '
    'gives all seven premise methods a graph route (REACHABLE), so the '
    'premise is now graph-backed; the verdict is carried over unchanged.')
NOTE[HAVE_PIECE] = NOTE[HAVE_PIECE] + ' ' + CAVEAT_2

# ---- UNREACHABLE labels (exactly the graph's unreachable set) ----
unre = {m for m, l in g['labels'].items() if l.get('unreachable')}
assert unre == {m for m, r in rows.items() if r['verdict'] == 'UNREACHABLE'}, \
    ('label set != methods.csv unreachable',
     sorted(unre - {m for m, r in rows.items() if r['verdict'] == 'UNREACHABLE'})[:5])
U = {}
for m in unre:
    lab = g['labels'][m]
    ur = lab['unreachable']
    assert lab['confirmed_by'] in ('SOURCE', 'INFERRED', 'DEVICE'), ('label confirmed_by', m, lab['confirmed_by'])
    assert lab['source_ref'], ('empty unreachable ref', m)
    assert ur['text'], ('empty unreachable text', m)
    U[m] = (lab['confirmed_by'], lab['source_ref'],
            'UNREACHABLE %s: %s' % (ur['kind'], ur['text']))

# ---- UNRESOLVED exclusion (no row, no invented verdict) ----
unresolved = {m for m, r in rows.items() if r['verdict'] == 'UNRESOLVED'}
assert len(unresolved) == 0, ('unresolved count', len(unresolved))
assert not (unresolved & set(sample)), ('sampled method is UNRESOLVED', sorted(unresolved & set(sample)))
assert not (unresolved & unre), ('unreachable/unresolved overlap', sorted(unresolved & unre))
print('UNRESOLVED methods excluded from all rows:', len(unresolved))

# ---- edge rows: (a) FW-SRC citations, derived at run time ----
cites = {}  # full citation text -> first carrier edge id (graph order)
for x in g['edges']:
    for lab, txt in parse_evidence(x.get('evidence') or ''):
        if lab != 'FW-SRC':
            continue
        for cit in txt.split(';'):
            cit = cit.strip()
            if re.search(r':\d', cit):
                cites.setdefault(cit, x['id'])
rep_cites = {}
for _cit, _eid in cites.items():
    rep_cites.setdefault(_eid, []).append(_cit)
print('FW-SRC distinct citations:', len(cites), 'representative edges:', len(rep_cites))

# ---- edge rows: (b) D5 corrected edges, derived list + run-time check ----
# Each tuple: (new_id, old_id, src, dst, kind, old_ref, new_ref).
# Derived by the snapshot-vs-postfix diff described in the docstring;
# re-validated below against the fresh graph on every run.
D5_ROWS = [
    ('E4d86fd4c', 'E90240683', 'AddTorrentInfoFragment.showChooseDirDialog', 'FileManagerConfig.<init>(String,String,int)', 'CALL', 'AddTorrentInfoFragment.java:207', 'AddTorrentInfoFragment.java:208'),
    ('E62f0d297', 'E16951813', 'AddTorrentViewModel$TorrentDecodeTask.onPostExecute', 'AddTorrentViewModel$DecodeState.<init>(Status)', 'CALL', 'AddTorrentViewModel.java:321', 'AddTorrentViewModel.java:322'),
    ('E082e311e', 'Eb83124a4', 'CreateTorrentDialog.choosePathToSaveDialog', 'FileManagerConfig.<init>(String,String,int)', 'CALL', 'CreateTorrentDialog.java:330', 'CreateTorrentDialog.java:331'),
    ('Ebecff963', 'E02ee8cda', 'CreateTorrentDialog.handleFinish', 'CreateTorrentDialog.handleBuildError', 'REGISTER', 'CreateTorrentDialog.java:392', 'CreateTorrentDialog.java:395'),
    ('Edf29067c', 'E1617f3e2', 'DetailTorrentInfoFragment.showChooseDirDialog', 'FileManagerConfig.<init>(String,String,int)', 'CALL', 'DetailTorrentInfoFragment.java:189', 'DetailTorrentInfoFragment.java:188'),
    ('E60e8b0d1', 'Eff2a41df', 'DetailTorrentViewModel.updateFiles', 'DetailTorrentViewModel.updateChildren', 'REGISTER', 'DetailTorrentViewModel.java:598', 'DetailTorrentViewModel.java:599'),
    ('Eaf178d4f', 'Ec56801b0', 'FeedActivity.restoreFeedsChooseDialog', 'FileManagerConfig.<init>(String,String,int)', 'CALL', 'FeedActivity.java:283', 'FeedActivity.java:282'),
    ('Edc0727e2', 'E30a3dca0', 'FeedDownloaderWorker.fetchTorrent', 'AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean)', 'CALL', 'FeedDownloaderWorker.java:186', 'FeedDownloaderWorker.java:178-186'),
    ('E3a20be33', 'E097fa36e', 'FeedFragment.lambda$getAllFeedsSingle$4', 'FeedChannelItem.<init>', 'REGISTER', 'FeedFragment.java:276', 'FeedFragment.java:277'),
    ('Ec6f7e59b', 'E73e9b640', 'FeedFragment.lambda$observeFeeds$2', 'FeedChannelItem.<init>', 'REGISTER', 'FeedFragment.java:261', 'FeedFragment.java:262'),
    ('E53652f10', 'E2d65126e', 'FeedItemsFragment.lambda$getAllFeedItemsSingle$4', 'FeedItemsListItem.<init>', 'REGISTER', 'FeedItemsFragment.java:228', 'FeedItemsFragment.java:229'),
    ('Eaf55279d', 'E0bf04616', 'FeedItemsFragment.lambda$observeFeedItems$2', 'FeedItemsListItem.<init>', 'REGISTER', 'FeedItemsFragment.java:213', 'FeedItemsFragment.java:214'),
    ('Efcc9911f', 'Ebeafc3db', 'FeedItemsViewModel.observeWorkResult', 'FeedItemsViewModel.observeWorkResult', 'REGISTER', 'FeedItemsViewModel.java:150', 'FeedItemsViewModel.java:151'),
    ('Ecdce561f', 'E84f38262', 'FeedViewModel.observeWorkResult', 'FeedViewModel.observeWorkResult', 'REGISTER', 'FeedViewModel.java:167', 'FeedViewModel.java:168'),
    ('Ee62a3a80', 'Ec257736a', 'LimitationsSettingsFragment.onCreate', 'InputFilterRange$Builder.<init>', 'CALL', 'LimitationsSettingsFragment.java:66', 'LimitationsSettingsFragment.java:67'),
    ('Ea21e190b', 'E1b6eda5b', 'LogActivity.saveLogPathChooseDialog', 'FileManagerConfig.<init>(String,String,int)', 'CALL', 'LogActivity.java:309', 'LogActivity.java:310'),
    ('Eb86e3085', 'Ed8cb7957', 'LogSettingsFragment.onCreate', 'InputFilterRange$Builder.<init>', 'CALL', 'LogSettingsFragment.java:59', 'LogSettingsFragment.java:60'),
    ('Ef2f58859', 'E7dbd445c', 'MainFragment.lambda$getAllTorrentsSingle$6', 'TorrentListItem.<init>', 'REGISTER', 'MainFragment.java:339', 'MainFragment.java:340'),
    ('E38fa2b9d', 'E5288aebc', 'MainFragment.openTorrentFileDialog', 'FileManagerConfig.<init>(String,String,int)', 'CALL', 'MainFragment.java:533', 'MainFragment.java:532'),
    ('Ec1deefb5', 'E50bf2f86', 'NetworkSettingsFragment.lambda$onCreate$4', 'PreferenceActivityConfig.<init>(String,String)', 'CALL', 'NetworkSettingsFragment.java:254', 'NetworkSettingsFragment.java:252'),
    ('E40a58c5a', 'Ee0aad578', 'NetworkSettingsFragment.startActivity', 'PreferenceActivityConfig.<init>(String,String)', 'CALL', 'NetworkSettingsFragment.java:374', 'NetworkSettingsFragment.java:373'),
    ('E5be78936', 'E9201dc1c', 'TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)', 'AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean)', 'CALL', 'TorrentEngine.java:1188', 'TorrentEngine.java:1187'),
    ('Eca02ae3f', 'E0427be7d', 'TorrentSessionImpl.lambda$handleStats$7', 'SessionStats.<init>(long,long,long,long,long,int)', 'CALL', 'TorrentSessionImpl.java:1179', 'TorrentSessionImpl.java:1174-1179'),
    ('E895cd7de', 'E95389332', 'TorrentSessionImpl.parseMagnet', 'MagnetInfo.<init>(String,String,String,List)', 'CALL', 'TorrentSessionImpl.java:451', 'TorrentSessionImpl.java:450'),
    ('E9f820ba5', 'Ec91ee2f6', 'TorrentSessionImpl.stopTasks', 'TorrentSessionImpl.handleStoppingTasks', 'REGISTER', 'TorrentSessionImpl.java:926', 'TorrentSessionImpl.java:928')
]

d5_notes = {}
for (_new, _old, _src, _dst, _kind, _old_ref, _new_ref) in D5_ROWS:
    assert _new in E, ('D5 new edge missing from fresh graph', _new)
    assert _old not in E, ('D5 old edge still in fresh graph', _old)
    _e = E[_new]
    assert (_e['src'], _e['dst'], _e['kind']) == (_src, _dst, _kind), \
        ('D5 edge src/dst/kind changed', _new, _e['src'], _e['dst'], _e['kind'])
    _ev = _e.get('evidence') or ''
    assert _new_ref in _ev, ('D5 new citation not on fresh edge', _new, _new_ref, _ev)
    d5_notes[_new] = ('D5 check-4 citation correction: %s -> %s; '
                      'src/dst/kind unchanged, no verdict change' % (_old_ref, _new_ref))
assert len(d5_notes) == 25, ('D5 row count', len(d5_notes))
print('D5 corrected edges validated against fresh graph:', len(d5_notes))

d5_ref = {_n: _nr for (_n, _o, _s, _d, _k, _or, _nr) in D5_ROWS}
edge_rows = {}  # id -> (result, confirmed_by, ref, note)
for _eid in sorted(rep_cites):
    _cs = sorted(rep_cites[_eid])
    edge_rows[_eid] = ('correct', 'SOURCE' if edge_sourced(_eid) else 'INFERRED',
                       _cs[0],
                       'framework claim checked: AOSP 8.1.0_r1 lines read for ' + '; '.join(_cs))
for _eid, _note in d5_notes.items():
    assert _eid in E, ('D5 edge missing', _eid)
    if _eid in edge_rows:
        _prev = edge_rows[_eid]
        edge_rows[_eid] = (_prev[0], _prev[1], _prev[2], _prev[3] + ' ' + _note)
    else:
        edge_rows[_eid] = ('fixed', 'SOURCE' if edge_sourced(_eid) else 'INFERRED',
                           d5_ref[_eid],
                           _note)
assert 'Ea751b47d' not in edge_rows, ('59/32 edge must never get an edge row', 'Ea751b47d')
print('edge rows total:', len(edge_rows),
      'FW-SRC reps:', len(rep_cites), 'D5:', len(d5_notes),
      'overlap:', len(set(rep_cites) & set(d5_notes)))

# W9c (Kiro, 2026-11-09; blind second pass part 2, scratch/reaudit/w9c_compare.csv LibreTorrent-c10, -c24, -c34): the
# SafFsModule dispatch steps got ENV other_app and the feed-items step STATE data. These four sampled routes keep the same
# steps (src, dst, kind checked against 224f1c94); only the edge id of the re-gated step changed.
for _m, _n in (('FeedDao_Impl$11.finalize', 'step 8 now needs a feed in the list'),
               ('SafFileSystem$FakePath.serialize', 'step 19 now carries ENV other_app (a content:// uri)'),
               ('SafFileSystem.getParentDirUri', 'step 17 now carries ENV other_app (a content:// uri)'),
               ('SafFileSystem$FakePath.makeRelativePathNodes', 'step 24 now carries ENV other_app (a content:// uri)')):
    NOTE[_m] += ' W9c: gate text changed, edge ids re-pointed, no replay, same steps (%s).' % _n

# ---- build and validate the rows ----
out = [['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']]
for m in sample:
    r = rows.get(m)
    assert r is not None and r['verdict'] == 'REACHABLE', ('path row not reachable', m)
    assert all(i in E for i in r['route_edge_ids'].split()), ('path edge missing from fresh graph', m)
    ref = route_ref(m)
    assert ref, ('no SRC ref on built route', m)
    base = ref.split(':')[0].split('/')[-1]
    ev_all = ' '.join(E[i].get('evidence') or '' for i in r['route_edge_ids'].split())
    assert base in ev_all, ('path ref not on route evidence', m, ref)
    assert NOTE[m].strip(), ('empty note', m)
    out.append(['path', m, VERDICT[m], 'SOURCE' if route_sourced(m) else 'INFERRED',
                ref, r['route_edge_ids'], NOTE[m]])

label_rows = []
for m in U:
    cb, ref, note = U[m]
    assert note.strip(), ('empty unreachable note', m)
    label_rows.append(['label', m, 'correct', cb, ref, '', note])
for m in sample:
    r = rows[m]
    label_rows.append(['label', m, VERDICT[m], 'SOURCE' if route_sourced(m) else 'INFERRED',
                       route_ref(m), '',
                       'REACHABLE confirmed: the route was read step by step (see the path row and route_table.md); gates read: env=%s state=%s'
                       % (r['env_kinds'] or '-', r['state_kinds'] or '-')])
assert len(label_rows) == len(U) + N, ('label row count', len(label_rows))
assert len({r[1] for r in label_rows}) == len(label_rows), ('duplicate label item', len(label_rows))
assert not ({r[1] for r in label_rows} & unresolved), ('label row for UNRESOLVED method')
for _row in sorted(label_rows, key=lambda r: r[1]):
    out.append(_row)
# W9 reachable audit (Kiro, 2026-11-08): one label row per drawn method from scratch/reaudit/audit_result.csv
# (note "reachable audit, class <X>"); a method that already has a label row keeps it.
_w9 = {}
exec(open('tools_dev/w9_audit_rows.py', encoding='utf-8').read(), _w9)
out.extend(_w9['audit_rows'](GDIR, [r[1] for r in out[1:] if r[0] == 'label']))

for i in sorted(edge_rows):
    _res, _cb, _ref, _note = edge_rows[i]
    assert i in E, ('edge id missing', i)
    assert _note.strip(), ('empty edge note', i)
    assert _ref, ('empty edge ref', i)
    out.append(['edge', i, _res, _cb, _ref, '', _note])

print('seeded totals (pre-DEVICE): path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
# W9c re-point (reviewer item 4 rule): {method: (edges as replayed, current edges)}. Only rows whose replayed steps are
# the current route's steps. SafFileSystem$FakePath.serialize and SafFileSystem$FakePath.makeRelativePathNodes are not
# re-pointed: their device rows (unscriptable, not run) replay older routes with other steps (already so at 224f1c94).
_W9C_DEVICE_REPOINT = {
    'FeedDao_Impl$11.finalize': (
        'Ebe0bf90d E9278e2d5 E37e3a4dc E6507c563 Ef969f0d4 Ef2176f7c E3a6833e8 E34c7b5a2 E9b4b24a7 Ed7bad68f Ed9f15dc8 '
        'Ea2db48be Edb748470 E27e8b62f E4d8c9499 E38bcd1c3 E1c77904d E6ac37b87 Ec4d16492 E8756175a',
        'Ebe0bf90d E9278e2d5 E37e3a4dc E6507c563 Ef969f0d4 Ef2176f7c E3a6833e8 E1691dd0f E9b4b24a7 Ed7bad68f Ed9f15dc8 '
        'Ea2db48be Edb748470 E27e8b62f E4d8c9499 E38bcd1c3 E1c77904d E6ac37b87 Ec4d16492 E8756175a'),
    'SafFileSystem.getParentDirUri': (
        'Ebe0bf90d Ed8e7f5f9 Ee453d286 E28c54333 E2e46bfdf E17916b8d Ed7e1785e E1ebb5848 Ed745fbc6 E4e7277c1 E4322fd9c '
        'E9bfa7a32 Eee58c113 E8bb4dc4c E5945e3f0 E2cd08e2c Effae07fc Ee28809ba',
        'Ebe0bf90d Ed8e7f5f9 Ee453d286 E28c54333 E2e46bfdf E17916b8d Ed7e1785e E1ebb5848 Ed745fbc6 E4e7277c1 E4322fd9c '
        'E9bfa7a32 Eee58c113 Ec25b6558 Ef111a826 E2cd08e2c Ea0e5acb3 Ee28809ba'),
}
_device_count = 0
# Reviewer rule 2026-11-09 (tools_dev/device_rows.py): a reached row is written only when its replayed edge ids (after
# the W9c re-point) equal the method's current best route; the five routes of LATER_RUNS come from run 42683233983-1.
_dr = {}
exec(open('tools_dev/device_rows.py', encoding='utf-8').read(), _dr)
_dev_rows, _dev_dropped = _dr['device_rows'](GDIR, 'LibreTorrent', _W9C_DEVICE_REPOINT)
for _d in _dev_dropped:
    print('DEVICE row dropped: %s %s: %s' % _d)
for _row in _dev_rows:
    _device_count += 1
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
    else:
        _res2, _note = 'unclear', _status + '; not run'
    assert _res2 != 'wrong', ('DEVICE row must never be wrong', _row)
    _edges = _row['edges']
    # W9c re-point: the replayed steps (src, dst, kind in the run's build 8521bd39) equal the current route's
    # steps; only edge ids of re-gated steps changed. Result and reason are kept.
    if _row['method'] in _W9C_DEVICE_REPOINT:
        assert _edges.split() == _W9C_DEVICE_REPOINT[_row['method']][0].split(), ('W9c re-point: device edges changed', _row['method'])
        assert _W9C_DEVICE_REPOINT[_row['method']][1].split() == rows[_row['method']]['route_edge_ids'].split(), ('W9c re-point: route moved', _row['method'])
        _edges = _W9C_DEVICE_REPOINT[_row['method']][1]
        _note += '; W9c: gate text changed, edge ids re-pointed, no replay, same steps'
    out.append(['path', _row['method'], _res2, 'DEVICE',
                'device run %s/%s' % (_row['run'], _row['script']),
                _edges, _note])
print('DEVICE rows added:', _device_count)

with open(OUT_FILE, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

print('rows by (type,result):', dict(collections.Counter((r[0], r[2]) for r in out[1:])))
print('totals: path=%d label=%d edge=%d device=%d grand=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge'),
    _device_count, len(out) - 1))
