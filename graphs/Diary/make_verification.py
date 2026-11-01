"""Write graphs/Diary/verification.csv for the Diary schema 2 trigger graph.

Modelled on graphs/AnyMemo/make_verification.py, adapted to the T2 rule:
the row data is seeded once from the branch verification.csv into
graphs/Diary/scratch/verification_rows.json (repo data, pushed), and this
writer validates every row against the built graph and writes the file in
the seed's order, so the output is byte-identical to the branch file.

Run from the repo root: python3 -I graphs/Diary/make_verification.py
All paths it uses are repo-relative. It stops with an error on any
mismatch. Two runs in a row give byte-identical files.

Validation (brief section 4):
- every path row's method exists in out/methods.csv, is REACHABLE, and
  its edges are exactly that method's route_edge_ids; every edge id
  exists in out/*_trigger_graph.json;
- every label row's method exists in out/methods.csv; UNREACHABLE label
  rows carry result 'correct'; REACHABLE label rows are exactly the 30
  sampled path methods with result 'correct' or 'fixed';
- every edge row's id exists in the trigger graph;
- every row has result in {correct, fixed, unclear}, confirmed_by in
  {SOURCE, INFERRED}, and a non-empty note.

D7 (DEVICE rows): if graphs/Diary/device/results.csv exists (written by
device/compare.py from a committed device/results/<run>/), one DEVICE
path row is appended per results row: result 'correct' when reached is
'yes', else 'unclear'; ref 'device run <run>/<script>'; note the script
status, plus the reason for 'unclear' (not reached / script failed /
unscriptable). A not-reached route never becomes 'wrong', and no label
changes. If the file does not exist, the output is exactly the seed rows.
"""

import csv
import glob
import json
import sys

APP = 'Diary'
HEADER = ['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']
RESULTS = {'correct', 'fixed', 'unclear'}
CONFIRMED = {'SOURCE', 'INFERRED'}


def fail(msg):
    raise SystemExit('make_verification.py: ERROR: ' + msg)


def main():
    seed_path = 'graphs/%s/scratch/verification_rows.json' % APP
    with open(seed_path, encoding='utf-8') as f:
        seed = json.load(f)
    if not isinstance(seed, list) or not seed:
        fail('seed file %s holds no rows' % seed_path)

    methods_path = 'graphs/%s/out/methods.csv' % APP
    with open(methods_path, encoding='utf-8', newline='') as f:
        methods = {r['method']: r for r in csv.DictReader(f)}

    trigger_paths = glob.glob('graphs/%s/out/*_trigger_graph.json' % APP)
    if len(trigger_paths) != 1:
        fail('expected exactly one trigger graph, found %r' % trigger_paths)
    with open(trigger_paths[0], encoding='utf-8') as f:
        graph = json.load(f)
    edges = {x['id']: x for x in graph['edges']}

    paths = {}
    labels = {}
    edge_rows = 0
    for i, r in enumerate(seed):
        if sorted(r.keys()) != sorted(HEADER):
            fail('row %d has keys %r, expected %r' % (i, sorted(r.keys()), HEADER))
        t, item, res, cb, ref, ed, note = (r[k] for k in HEADER)
        if t not in ('path', 'label', 'edge'):
            fail('row %d: bad type %r' % (i, t))
        if res not in RESULTS:
            fail('row %d: bad result %r' % (i, res))
        if cb not in CONFIRMED:
            fail('row %d: bad confirmed_by %r' % (i, cb))
        if not ref.strip() or not note.strip():
            fail('row %d: empty ref or note' % i)
        if t == 'path':
            m = methods.get(item)
            if m is None:
                fail('path row %d: method %r not in methods.csv' % (i, item))
            if m['verdict'] != 'REACHABLE':
                fail('path row %d: method %r verdict %r, not REACHABLE'
                     % (i, item, m['verdict']))
            if ed.split() != m['route_edge_ids'].split():
                fail('path row %d: edges of %r differ from route_edge_ids'
                     % (i, item))
            for e in ed.split():
                if e not in edges:
                    fail('path row %d: edge %r of %r not in trigger graph'
                         % (i, e, item))
            if item in paths:
                fail('duplicate path row for %r' % item)
            paths[item] = r
        elif t == 'label':
            m = methods.get(item)
            if m is None:
                fail('label row %d: method %r not in methods.csv' % (i, item))
            if ed.strip():
                fail('label row %d: edges field must be empty' % i)
            if m['verdict'] == 'UNREACHABLE':
                if res != 'correct':
                    fail('label row %d: UNREACHABLE %r has result %r, not correct'
                         % (i, item, res))
            elif m['verdict'] == 'REACHABLE':
                if res not in ('correct', 'fixed'):
                    fail('label row %d: REACHABLE %r has result %r'
                         % (i, item, res))
            else:
                fail('label row %d: method %r verdict %r' % (i, item, m['verdict']))
            if item in labels:
                fail('duplicate label row for %r' % item)
            labels[item] = r
        else:
            if item not in edges:
                fail('edge row %d: edge %r not in trigger graph' % (i, item))
            if ed.strip():
                fail('edge row %d: edges field must be empty' % i)
            edge_rows += 1

    if len(paths) != 30:
        fail('path rows: %d, expected 30 (the final sample)' % len(paths))
    unreachable = {m for m, r in methods.items() if r['verdict'] == 'UNREACHABLE'}
    if set(labels) != unreachable | set(paths):
        fail('label set != UNREACHABLE methods + sampled path methods: '
             'extra %r, missing %r'
             % (sorted(set(labels) - unreachable - set(paths)),
                sorted((unreachable | set(paths)) - set(labels))))
    for m in paths:
        if m not in labels:
            fail('sampled method %r has no label row' % m)

    out = [[r[k] for k in HEADER] for r in seed]

    # D7: DEVICE rows from a committed device run, if one exists.
    device_path = 'graphs/%s/device/results.csv' % APP
    device_rows = 0
    try:
        with open(device_path, encoding='utf-8', newline='') as f:
            results = list(csv.DictReader(f))
    except FileNotFoundError:
        results = None
    if results is not None:
        for i, r in enumerate(results):
            method = r['method']
            if method not in paths:
                fail('device results row %d: method %r is not a path row'
                     % (i, method))
            if r['edges'].split() != paths[method]['edges'].split():
                fail('device results row %d: edges of %r differ from the path row'
                     % (i, method))
            reached = r['reached']
            status = r['script_status']
            if reached == 'yes':
                res, note = 'correct', status
            elif reached == 'no':
                res = 'unclear'
                if status == 'unscriptable':
                    note = status + '; unscriptable'
                elif status in ('timeout',) or status.startswith('failed_at_step'):
                    note = status + '; script failed'
                else:
                    note = status + '; not reached'
            else:
                fail('device results row %d: bad reached %r' % (i, reached))
            out.append(['path', method, res, 'DEVICE',
                        'device run %s/%s' % (r['run'], r['script']),
                        r['edges'], note])
            device_rows += 1

    out_path = 'graphs/%s/verification.csv' % APP
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerows([HEADER] + out)

    import collections
    c = collections.Counter((r[0], r[2]) for r in out)
    print('rows by (type,result):', dict(sorted(c.items())))
    print('totals: path=%d label=%d edge=%d device=%d'
          % (sum(1 for r in out if r[0] == 'path' and r[3] != 'DEVICE'),
             sum(1 for r in out if r[0] == 'label'),
             sum(1 for r in out if r[0] == 'edge'),
             device_rows))


if __name__ == '__main__':
    main()
