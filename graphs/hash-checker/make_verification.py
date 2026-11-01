"""Write graphs/hash-checker/verification.csv for the hash-checker schema 2 trigger graph.

Portable writer for T3 (the old handoff/examples/make_vlog_hash_checker.py
read sample_final.txt from a session folder that no longer exists).

Run from the repo root:  python3 -I graphs/hash-checker/make_verification.py

Row data is seeded once from the verified branch file, in file order
(path block, label block, edge block), in
graphs/hash-checker/scratch/verification_rows.json. The order is fixed by
the seed file, so two runs are byte-identical; the order is NOT
alphabetical, because T3 acceptance is byte-identical output against the
current file, and the current file is in verification order (final sample
30 path rows first, then the 7 earlier-read path rows).

Every row is validated against the built graph before anything is
written; the script stops with an error on any mismatch:
- path rows: the method exists in out/methods.csv and is REACHABLE, the
  edges field is exactly the method's route_edge_ids, every edge id
  exists in out/hash-checker_trigger_graph.json, and every file cited
  in ref appears in the route's edge evidence, is the method's own
  source file, or is listed in REF_EXCEPTIONS with its reason.
- label rows: the method exists in out/methods.csv, confirmed_by
  matches methods.csv, the UNREACHABLE label set is exactly the graph's
  unreachable set, and every REACHABLE label row has a path row.
- edge rows: the id exists in the trigger graph and every file cited in
  ref appears in that edge's evidence.
- no duplicate (type, item) among the seeded rows; every note non-empty.

DEVICE rows (D7): if graphs/hash-checker/device/results.csv exists, one
row per results row is appended after the seeded rows: type=path,
item=method, result=correct when reached is yes else unclear,
confirmed_by=DEVICE, ref='device run <run>/<script>', edges=<edges>,
note=<script_status> plus the unclear reason (not reached / script
failed / unscriptable). A not-reached route never becomes wrong and no
label changes. The results row's method must have a seeded path row and
its edges must equal that path row's edges. If the file does not exist,
the output is exactly the seeded rows.

All paths are repo-relative. Only the standard library is used. Output
is written with csv.writer defaults, matching the current file's
line endings.
"""
import csv
import glob
import json
import os
import re
import sys

APP = 'hash-checker'
GDIR = 'graphs/%s' % APP
SEED = '%s/scratch/verification_rows.json' % GDIR
METHODS_CSV = '%s/out/methods.csv' % GDIR
RESULTS_CSV = '%s/device/results.csv' % GDIR
OUT = '%s/verification.csv' % GDIR

COLS = ['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']

# One documented exception to the path-ref rule, verified by printing
# the lines: the LogUtils.e path row's ref cites
# SharedPreferencesSettings.java:44-49, the getLastHashType() catch that
# calls LogUtils.e (the second printed LogUtils.e call site, retained as
# supporting evidence for this 'fixed' row). It is not on the route's
# edge evidence (the route ends at the openSystemFileManager catch,
# HashCalculatorFragment.java:196-199) and it is not the method's own
# file, so it is listed here rather than weakening the rule for all rows.
REF_EXCEPTIONS = {
    ('LogUtils.e', 'SharedPreferencesSettings.java'): (
        'second printed LogUtils.e call site: getLastHashType() catch, '
        'SharedPreferencesSettings.java:44-49'),
}


def fail(msg):
    sys.stderr.write('make_verification: ERROR: %s\n' % msg)
    sys.exit(1)


def own_file(method_row):
    ref = method_row.get('source_ref') or ''
    return ref.split(':')[0].split('/')[-1].strip()


FILE_RE = re.compile(r'[\w./$#-]+(?:\.java|\.xml)')


def evidence_files(evidence):
    # File basenames cited anywhere in the evidence text, including
    # tokens like 'ThemeConfigImpl.java:30' that do not end in .java.
    return {m.split('/')[-1] for m in FILE_RE.findall(evidence or '')}


def check_ref_files(item, ref, allowed_files, where):
    for seg in ref.split(';'):
        seg = seg.strip()
        if not seg:
            continue
        f = seg.split(':')[0].strip().split('/')[-1]
        if f in allowed_files:
            continue
        if (item, f) in REF_EXCEPTIONS:
            continue
        fail('%s %s: ref file %s not on route evidence, not the '
             'method file, and not an allowed exception (ref %s)'
             % (where, item, f, ref))


def main():
    if not os.path.isdir(GDIR):
        fail('run from the repo root (graphs/%s not found)' % APP)
    with open(SEED, encoding='utf-8') as fh:
        seed = json.load(fh)
    methods = {}
    with open(METHODS_CSV, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            methods[row['method']] = row
    gj_path = glob.glob('%s/out/*_trigger_graph.json' % GDIR)
    if not gj_path:
        fail('no trigger graph json under %s/out/' % GDIR)
    with open(gj_path[0], encoding='utf-8') as fh:
        graph = json.load(fh)
    edges = {e['id']: e for e in graph['edges']}

    out_rows = []
    seen = set()
    path_methods = []
    label_unreachable = set()
    label_reachable = set()
    for row in seed:
        if list(row.keys()) != COLS:
            fail('seed row has wrong columns: %r' % (row,))
        typ, item = row['type'], row['item']
        if typ not in ('path', 'label', 'edge'):
            fail('unknown row type %r' % typ)
        if row['result'] not in ('correct', 'fixed', 'unclear'):
            fail('unknown result %r for %s %s'
                 % (row['result'], typ, item))
        if row['confirmed_by'] not in ('SOURCE', 'INFERRED'):
            fail('seed confirmed_by must be SOURCE or INFERRED: %s %s'
                 % (typ, item))
        if not row['note'].strip():
            fail('empty note for %s %s' % (typ, item))
        key = (typ, item)
        if key in seen:
            fail('duplicate seed row %s %s' % key)
        seen.add(key)
        if typ == 'path':
            m = methods.get(item)
            if m is None:
                fail('path method not in methods.csv: %s' % item)
            if m['verdict'] != 'REACHABLE':
                fail('path method not REACHABLE: %s (%s)'
                     % (item, m['verdict']))
            if row['edges'] != m['route_edge_ids']:
                fail('path edges != route_edge_ids for %s' % item)
            ev_files = set()
            for eid in row['edges'].split():
                e = edges.get(eid)
                if e is None:
                    fail('path edge id not in trigger graph: %s' % eid)
                ev_files |= evidence_files(e.get('evidence'))
            check_ref_files(item, row['ref'],
                            ev_files | {own_file(m)}, 'path')
            path_methods.append(item)
        elif typ == 'label':
            m = methods.get(item)
            if m is None:
                fail('label method not in methods.csv: %s' % item)
            if row['confirmed_by'] != m['confirmed_by']:
                fail('label confirmed_by != methods.csv for %s' % item)
            if m['verdict'] == 'UNREACHABLE':
                label_unreachable.add(item)
            else:
                label_reachable.add(item)
        else:  # edge
            e = edges.get(item)
            if e is None:
                fail('edge id not in trigger graph: %s' % item)
            ev_files = evidence_files(e.get('evidence'))
            check_ref_files(item, row['ref'], ev_files, 'edge')
        out_rows.append([row[c] for c in COLS])

    unreachable = {m for m, r in methods.items()
                   if r['verdict'] == 'UNREACHABLE'}
    if label_unreachable != unreachable:
        fail('UNREACHABLE label set != graph unreachable set '
             '(missing %s, extra %s)'
             % (sorted(unreachable - label_unreachable)[:5],
                sorted(label_unreachable - unreachable)[:5]))
    path_set = set(path_methods)
    if not label_reachable <= path_set:
        fail('REACHABLE label rows without a path row: %s'
             % sorted(label_reachable - path_set)[:5])

    n_device = 0
    if os.path.isfile(RESULTS_CSV):
        seed_paths = {}
        for row in seed:
            if row['type'] == 'path':
                seed_paths[row['item']] = row
        with open(RESULTS_CSV, newline='', encoding='utf-8') as fh:
            for r in csv.DictReader(fh):
                method = r['method']
                base = seed_paths.get(method)
                if base is None:
                    fail('device results method has no path row: %s'
                         % method)
                if r['edges'] != base['edges']:
                    fail('device results edges != path row edges for %s'
                         % method)
                reached = r['reached'].strip()
                status = r['script_status'].strip()
                if reached == 'yes':
                    result, note = 'correct', status
                else:
                    if status == 'ok':
                        reason = 'not reached'
                    elif status == 'unscriptable':
                        reason = 'unscriptable'
                    else:
                        reason = 'script failed'
                    result, note = 'unclear', '%s (%s)' % (status, reason)
                out_rows.append(['path', method, result, 'DEVICE',
                                 'device run %s/%s' % (r['run'], r['script']),
                                 r['edges'], note])
                n_device += 1

    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        w.writerows(out_rows)

    import collections
    c = collections.Counter((r[0], r[2]) for r in out_rows)
    print('rows by (type,result):', dict(c))
    print('totals: path=%d label=%d edge=%d device=%d'
          % (sum(1 for r in out_rows if r[0] == 'path'
                 and r[3] != 'DEVICE'),
             sum(1 for r in out_rows if r[0] == 'label'),
             sum(1 for r in out_rows if r[0] == 'edge'),
             n_device))


if __name__ == '__main__':
    main()
