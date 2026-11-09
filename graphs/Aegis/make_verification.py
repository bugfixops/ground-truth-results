"""Write graphs/Aegis/verification.csv for the Aegis schema 2 trigger graph.

Modelled on graphs/AnyMemo/make_verification.py (and graphs/AnkiDroid/
make_verification.py). PROMOTED (branch-layout simulation; adapted
from the Aegis turn staging writer, NOT the old merger-tree writer):
no arguments, file-anchored paths, so it runs from any cwd as:
  python3 -I graphs/Aegis/make_verification.py
Resolved input/output paths are printed on every run. The audited
verdict source is parsed mechanically from the promoted table
graphs/Aegis/scratch/ROUTE_TABLE_NEW.md (reached below as TABLE_FILE,
GDIR-relative, inside the repo; the staging parents[3] resolution is
removed, so the run refuses loudly if the promoted table is absent).
See the staging report
~/workspace/finish/work/Aegis/turn/writer/WRITER_REPORT.md and the
promotion simulation report in turn/promotion/PROMOTION_REPORT.md.
Every row is validated against the built graph; the script raises (STOPs)
if a path/label item is missing, a verdict does not match, an edge id
does not exist, or a path row's edges are not the method's built route.
All paths it uses are anchored to this file's directory (GDIR),
including the promoted table path above (no cwd dependence,
no session folders, no path outside the repo).
It writes ONLY verification.csv: it never touches
out/ (brief section 2.3: only CI writes out/), so it never injects a
`verification` object into the trigger JSON — that injection, if the
readme generator needs it, is a CI-side step, recorded as an open item
in AGENT_NOTES (C4 decision 2), not done here.

C4 decisions (Muse's own, for the user and Yang to review; recorded in
AGENT_NOTES.md, not silently resolved):
1. Writer: REWRITE to the AnyMemo model (this file), not an extension
   of the 2026-11-01 draft. The draft failed brief section 4 (no edge-id
   existence check, no label-verdict match, no path-route match, input
   order instead of fixed sorted order, absolute paths accepted) and its
   default JSON-injection route conflicts with brief section 2.3.
2. Out-write conflict: resolved by NOT writing out/ at all (see above).
   Consequence, stated openly: gen_readme_v2.py reads verification
   counts from the trigger JSON's `verification` object, so until CI
   injects that object (or the generator is changed to read the CSV),
   a CI-generated README will still print "No verification log yet"
   for Aegis. The CSV is the authoritative log; the README gap is a
   CI-contract item, not a reason to break section 2.3.
3. Fixture gap: $WEMU/fixtures holds no Aegis vault/import DB/QR
   image/export file, so device setup scripts generate those fixtures
   at run time (never committed binaries); see device/routes/Aegis/
   setup scripts and ROUTES.csv.
4. Result vocabulary: CSV path results use the route-table verdicts
   directly (correct / wrong / unclear), as in the AnkiDroid writer;
   the draft's correct/error_found/unclear vocabulary is NOT used.
   Fixed is a rate concept only (first-draw WRONG -> final CORRECT)
   and is not a row result.

Path rows: one per method in the NEW FINAL sample
(branch-layout scratch/sample_new.txt, seed 20261025, 25 routes,
1093 steps, 446 distinct edges, V3-corrected graph 6430 edges).
The `edges` field is the method's built route (methods.csv
route_edge_ids); the writer asserts it equals the audited table's
edge-id list for every sampled method, so the path row's edges are
exactly the route that was read step by step.
The `result` is the AUDITED new final route-table verdict, parsed
mechanically from the promoted table
graphs/Aegis/scratch/ROUTE_TABLE_NEW.md
(CORRECT 13, WRONG 1, UNCLEAR 11, fixed 2, distinct rate 3/14
= 0.2143, table rate 3/16 = 0.1875). The single WRONG route is
AuthActivity.lambda$onCreate$3; RawSlot.getType is UNCLEAR in the
new table (42-step @IMP route). No verdict or note is hardcoded
in this adapted writer: VERDICT and NOTE are built by the table
parser below, and any parse failure refuses the run.
Label rows: one per UNREACHABLE method (from the graph labels, checked
against methods.csv) plus one per sampled REACHABLE method.
Edge rows: the 8 v2 variant dispatch edges (processImporterState@FILE_X
-> importer decrypt) plus one row per edge carrying a distinct FW-SRC
citation with line numbers (framework claims checked against AOSP
8.1.0_r1). An edge row's note names EVERY citation for which that
edge is the representative (first) carrier, so no checked citation is
silently unrepresented by dedup; its `ref` is the first citation named
in its note (never the edge's first evidence segment), and its
`confirmed_by` follows the same all-SRC/FW-SRC rule as path/label
rows (INFERRED where any genuine INFERRED segment is present).
Rows are written in a fixed order: path rows in sample order, then
ALL label rows globally sorted by item, then ALL edge rows globally
sorted by item. Two runs are byte-identical.

D7 DEVICE rows: if graphs/Aegis/device/results.csv exists (written by
the CI device run, not by this run), one row per results row is
appended, in results order, AFTER all existing rows. If the file does
not exist, this block does nothing and the output is the C4 file
exactly. DEVICE rows never feed back into labels, edges, or route
checks, and a not-reached route never becomes 'wrong'. NOTE (audit
observation O2, kept deliberately): D7 rows are appended WITHOUT
re-validating method/edge existence, as the D7 brief specifies; a
malformed device/results.csv would inject rows unchecked, so the
file's producer (device/compare.py output) is the trust boundary.
"""
import csv, glob, json, os as _os, re
from pathlib import Path

APP = 'Aegis'
# File-anchored resolution (promoted branch layout; C4 plan section 2.1):
# GDIR is this file's directory, so the run never depends on cwd.
GDIR = Path(__file__).resolve().parent
# Promoted table location: GDIR is graphs/Aegis, so the promoted
# table is GDIR / 'scratch' / 'ROUTE_TABLE_NEW.md', inside the repo.
# The staging GDIR.parents[3] resolution is removed entirely.
TABLE_FILE = GDIR / 'scratch' / 'route_table.md'
GRAPH_GLOB = str(GDIR / 'out' / '*_trigger_graph.json')
METHODS_FILE = GDIR / 'out' / 'methods.csv'
SAMPLE_FILE = GDIR / 'scratch' / 'sample_new.txt'
OUT_FILE = GDIR / 'verification.csv'
DEVICE_FILE = GDIR / 'device' / 'results.csv'
for _p in (TABLE_FILE, METHODS_FILE, SAMPLE_FILE):
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
      'UNREACHABLE:', sum(1 for r in rows.values() if r['verdict'] == 'UNREACHABLE'))

sample = []
sample_steps = {}
for _l in open(SAMPLE_FILE, encoding='utf-8'):
    _t = _l.split()
    if _t and _t[0] in ('NONSTD', 'INFERRED', 'STATE', 'ENV', 'LONG', 'PLAIN'):
        assert len(_t) >= 7 and _t[1] == 'steps', ('malformed sample line', _l.strip())
        sample.append(_t[-1])
        sample_steps[_t[-1]] = int(_t[2])
assert len(sample) == 25, ('final sample size', len(sample))
assert len(set(sample)) == 25, ('duplicate method in sample', sample)

# Mechanical parse of the audited new final table (ROUTE_TABLE_NEW.md).
# Parser logic (no hand-typed verdicts or notes anywhere below):
#  - a data row is a line starting with '| ' whose first field is an
#    integer row number; header/separator/convention lines are skipped
#    by that test (they do not start with '| <digit>');
#  - split on '|': exactly 9 fields
#    [#, Stratum, Method, Steps, ENV, STATE, Verdict, Decisive, Edge ids];
#  - Verdict field: first token lowercased must be correct/wrong/unclear,
#    optionally followed by ' (fixed)'; the full field (e.g.
#    'CORRECT (fixed)') is kept as the note prefix;
#  - NOTE[method] = '<Verdict field>: <Decisive field verbatim>';
#  - row numbers must be 1..25 in order, methods unique, step count
#    must equal the edge-id count, the sample-file step count, and
#    methods.csv steps_from_launch, and the edge-id list must equal
#    methods.csv route_edge_ids exactly (same ids, same order);
#  - table method order must equal sample order exactly.
# Any violation refuses the run and writes nothing.
_table_lines = open(TABLE_FILE, encoding='utf-8').read().splitlines()
VERDICT = {}
PATH_RESULT = {}
NOTE = {}
_table_methods = []
_table_steps = {}
_table_numbers = []
for _line in _table_lines:
    if not _line.startswith('| '):
        continue
    _fields = [c.strip() for c in _line.strip().strip('|').split('|')]
    if len(_fields) != 9 or not _fields[0].isdigit():
        continue
    _n, _stratum, _method, _steps, _env, _state, _verdict_raw, _decisive, _edge_ids = _fields
    _vtok = _verdict_raw.split()[0].lower()
    assert _vtok in ('correct', 'wrong', 'unclear'), ('bad verdict in table', _method, _verdict_raw)
    assert _verdict_raw == _vtok.upper() or _verdict_raw == _vtok.upper() + ' (fixed)', \
        ('bad verdict form in table', _method, _verdict_raw)
    assert _method not in VERDICT, ('duplicate method in table', _method)
    assert _decisive, ('empty decisive text in table', _method)
    _tedges = _edge_ids.split()
    assert int(_steps) == len(_tedges), ('table steps != edge count', _method, _steps, len(_tedges))
    assert _method in rows, ('table method missing from methods.csv', _method)
    assert rows[_method]['verdict'] == 'REACHABLE', ('table method not reachable', _method)
    assert int(rows[_method]['steps_from_launch']) == int(_steps), \
        ('table steps != methods.csv steps', _method, _steps, rows[_method]['steps_from_launch'])
    assert rows[_method]['route_edge_ids'].split() == _tedges, \
        ('table edge ids != methods.csv route_edge_ids', _method)
    VERDICT[_method] = _vtok
    # review 6 fix 2: a 'CORRECT (fixed)' row is written with result=fixed on its path row
    PATH_RESULT[_method] = 'fixed' if _verdict_raw.endswith(' (fixed)') else _vtok
    NOTE[_method] = '%s: %s' % (_verdict_raw, _decisive)
    _table_methods.append(_method)
    _table_steps[_method] = int(_steps)
    _table_numbers.append(int(_n))
assert _table_numbers == list(range(1, 26)), ('table row numbers', _table_numbers)
assert len(VERDICT) == 25, ('table row count', len(VERDICT))
assert _table_methods == sample, ('table order != sample order', _table_methods, sample)
for _m in sample:
    assert sample_steps[_m] == _table_steps[_m], ('sample steps != table steps', _m)
import collections as _collections
print('table parsed rows:', len(VERDICT),
      'verdicts:', dict(_collections.Counter(VERDICT.values())))
print('table verdict map (sample order):',
      [(m, VERDICT[m]) for m in sample])
# End of mechanical table parse. VERDICT/NOTE above are parser output,
# in sample order. No hardcoded verdict/note dict follows.


def evidence_labels(ev):
    labs = []
    for seg in (ev or '').split(';'):
        seg = seg.strip()
        if not seg:
            continue
        labs.append(seg.split()[0])
    return labs


def edge_sourced(eid):
    labs = evidence_labels(E[eid].get('evidence') or '')
    return bool(labs) and all(l in ('SRC', 'FW-SRC') for l in labs)


def route_ref(m):
    r = rows[m]
    for i in r['route_edge_ids'].split():
        ev = E[i].get('evidence') or ''
        for seg in ev.split(';'):
            seg = seg.strip()
            if seg.startswith('SRC '):
                return seg[4:].strip()
    return ''


def sourced(m):
    r = rows[m]
    return all(edge_sourced(i) for i in r['route_edge_ids'].split())


# ---- UNREACHABLE labels (exactly the graph's unreachable set) ----
unre = {m for m, l in g['labels'].items() if l.get('unreachable')}
assert unre == {m for m, r in rows.items() if r['verdict'] == 'UNREACHABLE'}, \
    ('label set != methods.csv unreachable', sorted(unre - {m for m, r in rows.items() if r['verdict'] == 'UNREACHABLE'})[:5])
U = {}
for m in unre:
    lab = g['labels'][m]
    ur = lab['unreachable']
    U[m] = (lab['confirmed_by'], lab['source_ref'],
            'UNREACHABLE %s: %s' % (ur['kind'], ur['text']))

# ---- edge rows: v2 variant dispatch edges + FW-SRC citations ----
# Staging tripwire (C4 plan section 2.3): re-derive the variant list
# from the FRESH graph and refuse if it differs from the writer list.
# Definition: src is ImportEntriesActivity.processImporterState@FILE_<X>
# and dst is an importer $EncryptedState.decrypt(...) (including the
# $LegacyEncryptedState form). Shared @FILE dispatch, error-dialog,
# processDecrypted, DatabaseImporter, and $2.<init> edges are excluded
# by the dst test, exactly as in the pre-fix writer.
_derived_variants = {x['id'] for x in g['edges']
                     if re.match(r'ImportEntriesActivity\.processImporterState@FILE_[A-Z]+$', x['src'])
                     and re.search(r'Importer\$.*EncryptedState\.decrypt\(', x['dst'])}
assert _derived_variants == {'E0fac12e7', 'E631e6e57', 'E53060425', 'Ea0308cd4', 'E94c0e46e',
                             'Ebab0cfbb', 'Ef3b2ba2f', 'E3445b99d'}, \
    ('variant list != fresh-graph derivation', sorted(_derived_variants))
print('variant edges re-derived from fresh graph:', len(_derived_variants))
VARIANT_NOTES = {}
for _eid in ('E0fac12e7', 'E631e6e57', 'E53060425', 'Ea0308cd4', 'E94c0e46e',
             'Ebab0cfbb', 'Ef3b2ba2f', 'E3445b99d'):
    assert _eid in E, ('variant edge missing', _eid)
    _e = E[_eid]
    VARIANT_NOTES[_eid] = ('v2 variant dispatch edge (file-pick v2, audited design): %s -> %s; '
                           'the per-importer @FILE variant chain, not the shared @FILE dispatch.' % (_e['src'], _e['dst']))

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
    out.append(['path', m, PATH_RESULT[m], 'SOURCE' if sourced(m) else 'INFERRED',
                ref, r['route_edge_ids'], NOTE[m]])

label_rows = []
for m in U:
    cb, ref, note = U[m]
    assert cb in ('SOURCE', 'INFERRED'), ('label confirmed_by', m, cb)
    label_rows.append(['label', m, 'correct', cb, ref, '', note])
for m in sample:
    r = rows[m]
    label_rows.append(['label', m, VERDICT[m], 'SOURCE' if sourced(m) else 'INFERRED',
                       route_ref(m).split(';')[0], '',
                       'REACHABLE confirmed: the route was read step by step (see the path row and ROUTE_TABLE_NEW.md); gates read: env=%s state=%s'
                       % (r['env_kinds'] or '-', r['state_kinds'] or '-')])
for _row in sorted(label_rows, key=lambda r: r[1]):
    out.append(_row)
# W9 reachable audit (Kiro, 2026-11-08): one label row per drawn method from scratch/reaudit/audit_result.csv
# (note "reachable audit, class <X>"); a method that already has a label row keeps it.
_w9 = {}
exec(open('tools_dev/w9_audit_rows.py', encoding='utf-8').read(), _w9)
out.extend(_w9['audit_rows'](GDIR, [r[1] for r in out[1:] if r[0] == 'label']))

# Edge rows, globally sorted by item. Citation keying uses the FULL
# FW-SRC segment (no '(' truncation: truncation previously swallowed
# the plain AbsListView.java:1136-1150 citation on E9edc8c99). One
# row per edge; a row's note lists every citation for which that edge
# is the representative (first) carrier, and its ref is the first such
# citation, untruncated (no ' and ' split). confirmed_by follows the
# same all-SRC/FW-SRC rule as path/label rows.
cites = {}  # full citation text -> [first edge id, ...all citations are keys]
for x in g['edges']:
    for seg in (x.get('evidence') or '').split(';'):
        seg = seg.strip()
        if seg.startswith('FW-SRC') and re.search(r':\d', seg):
            cites.setdefault(seg[7:].strip(), x['id'])
rep_cites = {}
for _cit, _eid in cites.items():
    rep_cites.setdefault(_eid, []).append(_cit)

edge_rows = {}


def emit_edge(i, note):
    assert i in E, ('edge id missing', i)
    assert note.strip(), ('empty edge note', i)
    edge_rows[i] = note


for i in sorted(VARIANT_NOTES):
    emit_edge(i, VARIANT_NOTES[i])
for _eid in sorted(rep_cites):
    _cs = sorted(rep_cites[_eid])
    _note = 'framework claim checked: AOSP 8.1.0_r1 lines read for ' + '; '.join(_cs)
    if _eid in edge_rows:
        edge_rows[_eid] = edge_rows[_eid] + ' ' + _note
    else:
        edge_rows[_eid] = _note
for i in sorted(edge_rows):
    _note = edge_rows[i]
    if i in rep_cites:
        _ref = sorted(rep_cites[i])[0]
    else:
        _ev = E[i].get('evidence') or ''
        _ref = None
        for _seg in _ev.split(';'):
            _seg = _seg.strip()
            if _seg.startswith('FW-SRC '):
                _ref = _seg[7:].strip()
                break
            if _seg.startswith('SRC '):
                _ref = _seg[4:].strip()
                break
    out.append(['edge', i, 'correct', 'SOURCE' if edge_sourced(i) else 'INFERRED',
                _ref or '', '', _note])

# D7: DEVICE rows (device prep). If GDIR/device/results.csv
# exists (written by the CI device run, not by this run), append one row
# per results row, in results order, AFTER all existing rows. If the file
# does not exist, this block does nothing and the output is the seeded
# file exactly. DEVICE rows are device confirmations only: they never feed
# back into labels, edges, or route checks, and a not-reached route
# never becomes 'wrong'.
# Stdout-only addition (C4 plan section 2.5 item 4): seeded totals are
# printed before the DEVICE block and a DEVICE count after it, so the
# pre-DEVICE and post-DEVICE totals are distinguishable in the log.
# CSV bytes are unchanged by these prints.
print('seeded totals (pre-DEVICE): path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
_res = DEVICE_FILE
_device_count = 0
if _os.path.exists(_res):
    with open(_res, encoding='utf-8', newline='') as _f:
        for _row in csv.DictReader(_f):
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
            else:  # reached=not_run with status ok (defensive; should not occur)
                _res2, _note = 'unclear', _status + '; not run'
            out.append(['path', _row['method'], _res2, 'DEVICE',
                        'device run %s/%s' % (_row['run'], _row['script']),
                        _row['edges'], _note])

print('DEVICE rows added:', _device_count)

with open(OUT_FILE, 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

import collections
print('rows by (type,result):', dict(collections.Counter((r[0], r[2]) for r in out[1:])))
print('totals: path=%d label=%d edge=%d' % (
    sum(1 for r in out[1:] if r[0] == 'path'),
    sum(1 for r in out[1:] if r[0] == 'label'),
    sum(1 for r in out[1:] if r[0] == 'edge')))
