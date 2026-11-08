"""Write graphs/Currency/verification.csv for the Currency schema 2 graph.

Modelled on graphs/AnyMemo/make_verification.py, adapted to the T1 rule
for Currency: the file is written in the CURRENT row order (seeded once
from the branch verification.csv into scratch/verification_rows.json),
not re-sorted, and the run must be byte-identical to the current file.

Run from the repo root: python3 -I graphs/Currency/make_verification.py
Every row is validated against the built graph (brief section 4):
every edge id exists, every label verdict matches the graph, and every
path row's edges are the method's route. The script raises (STOPs) on
any mismatch. A row that fails validation is out of date: re-check that
route from printed source, correct the row, and record it in
scratch/fix_log.md; the file then changes for that reason only.

D7 (DEVICE rows): if graphs/Currency/device/results.csv exists (one
row per device route, written by device/compare.py from a committed
device/results/<run>/), one DEVICE path row is appended per route:
result correct when reached, else unclear; confirmed_by DEVICE;
ref "device run <run>/<script>"; note the script status plus, for
unclear, the reason (not reached / script failed / unscriptable). A
route that is not reached never becomes wrong, and no label changes.
If the file does not exist, the output is exactly the seeded rows.

All paths are repo-relative (resolved from this file's location).
"""
import csv
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
APP_DIR = os.path.join(ROOT, 'graphs', 'Currency')
OUT_DIR = os.path.join(APP_DIR, 'out')
SEED = os.path.join(APP_DIR, 'scratch', 'verification_rows.json')
TARGET = os.path.join(APP_DIR, 'verification.csv')
DEVICE_RESULTS = os.path.join(APP_DIR, 'device', 'results.csv')
HEADER = ['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']


def fail(msg):
    raise SystemExit('make_verification.py: STOP: %s' % msg)


def load_graph():
    paths = glob.glob(os.path.join(OUT_DIR, '*_trigger_graph.json'))
    if len(paths) != 1:
        fail('expected exactly one trigger graph in out/, found %r' % paths)
    with open(paths[0], encoding='utf-8') as f:
        g = json.load(f)
    edges = {e['id']: e for e in g['edges']}
    methods = {}
    with open(os.path.join(OUT_DIR, 'methods.csv'), newline='',
              encoding='utf-8') as f:
        for r in csv.DictReader(f):
            methods[r['method']] = r
    return edges, methods


def source_basenames():
    """Basenames of app + framework source files, for ref sanity checks."""
    names = set()
    for base in (os.path.join(ROOT, 'final_java_only', 'Currency'),
                 os.path.join(ROOT, 'fw_src')):
        for dp, dn, fn in os.walk(base):
            dn[:] = [d for d in dn
                     if d not in ('build', 'test', 'androidTest', '.git')]
            for f in fn:
                if f.endswith(('.java', '.xml', '.kt')):
                    names.add(f)
    return names


def ref_ok(ref, names):
    """A ref names a real source file (app or framework) or a manifest /
    resource form. The file part is everything before the first ':'."""
    base = ref.split(':')[0].strip()
    if not base:
        return False
    if base.startswith(('res/', 'AndroidManifest.xml',
                        'android-8.1.0_r1:')):
        return True
    if '/' in base:
        leaf = base.rsplit('/', 1)[-1]
        return leaf in names or base in names
    return base in names


def main():
    edges, methods = load_graph()
    names = source_basenames()
    with open(SEED, encoding='utf-8') as f:
        seed = json.load(f)
    if not isinstance(seed, list) or not seed:
        fail('seed %s is empty or not a list' % SEED)

    out = [HEADER]
    seen = set()
    unreachable_labelled = set()
    for row in seed:
        r = [row[k] for k in HEADER]
        key = (row['type'], row['item'])
        if key in seen:
            fail('duplicate row %r' % (key,))
        seen.add(key)
        if not row['note'].strip():
            fail('empty note on %r' % (key,))
        if not row['ref'].strip():
            fail('empty ref on %r' % (key,))
        if row['type'] == 'path':
            m = methods.get(row['item'])
            if m is None:
                fail('path method not in methods.csv: %s' % row['item'])
            if m['verdict'] != 'REACHABLE':
                fail('path row for unreachable method: %s' % row['item'])
            if m['route_edge_ids'] != row['edges']:
                fail('path edges != method route: %s' % row['item'])
            if not ref_ok(row['ref'], names):
                fail('path ref names no source file: %s %s'
                     % (row['item'], row['ref']))
            for eid in row['edges'].split():
                if eid not in edges:
                    fail('path edge id missing: %s' % eid)
        elif row['type'] == 'label':
            m = methods.get(row['item'])
            if m is None:
                fail('label method not in methods.csv: %s' % row['item'])
            if m['verdict'] == 'UNREACHABLE':
                unreachable_labelled.add(row['item'])
                if row['ref'] != m['source_ref']:
                    fail('unreachable label ref != graph source_ref: %s'
                         % row['item'])
                if row['confirmed_by'] != m['confirmed_by']:
                    fail('unreachable label confirmed_by != graph: %s'
                         % row['item'])
            else:
                if row['confirmed_by'] not in ('SOURCE', 'INFERRED'):
                    fail('bad confirmed_by on label row: %s' % row['item'])
        elif row['type'] == 'edge':
            if row['item'] not in edges:
                fail('edge id missing: %s' % row['item'])
        else:
            fail('unknown row type %r' % row['type'])
        out.append(r)

    unreachable = {m for m, r in methods.items()
                   if r['verdict'] == 'UNREACHABLE'}
    if unreachable_labelled != unreachable:
        fail('unreachable label set != graph unreachable set: missing %s, '
             'extra %s' % (sorted(unreachable - unreachable_labelled),
                           sorted(unreachable_labelled - unreachable)))

    # D7: DEVICE rows, only when a device results file exists.
    device_rows = 0
    if os.path.isfile(DEVICE_RESULTS):
        with open(DEVICE_RESULTS, newline='', encoding='utf-8') as f:
            for d in csv.DictReader(f):
                m = methods.get(d['method'])
                if m is None:
                    fail('device method not in methods.csv: %s'
                         % d['method'])
                if m['route_edge_ids'] != d['edges']:
                    fail('device edges != method route: %s' % d['method'])
                reached = (d['reached'] == 'yes')
                result = 'correct' if reached else 'unclear'
                if reached:
                    note = d['script_status']
                elif d['script_status'] == 'unscriptable':
                    note = 'unscriptable'
                elif d['script_status'] == 'ok':
                    note = 'ok, not reached'
                else:
                    note = '%s, script failed' % d['script_status']
                out.append(['path', d['method'], result, 'DEVICE',
                            'device run %s/%s' % (d['run'], d['script']),
                            d['edges'], note])
                device_rows += 1

    with open(TARGET, 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerows(out)

    from collections import Counter
    c = Counter((r[0], r[2]) for r in out[1:])
    print('rows by (type,result):', dict(c))
    print('totals: path=%d label=%d edge=%d device=%d' % (
        sum(1 for r in out[1:] if r[0] == 'path'
            and r[3] != 'DEVICE'),
        sum(1 for r in out[1:] if r[0] == 'label'),
        sum(1 for r in out[1:] if r[0] == 'edge'),
        device_rows))


if __name__ == '__main__':
    sys.exit(main())
