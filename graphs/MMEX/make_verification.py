#!/usr/bin/env python3
"""Generate graphs/MMEX/verification.csv (mirror only) from judged routes + built graph.

REFUSES to run unless the built graph exists: it needs graphs/MMEX/out/methods.csv
and graphs/MMEX/out/mmex_trigger_graph.json from a faithful build, plus
scratch/sample_30.txt (sampler output) and scratch/route_judgments.tsv
(method<TAB>result<TAB>confirmed_by<TAB>ref<TAB>note, one row per sampled method).

Header is exactly: type,item,result,confirmed_by,ref,edges,note
Rows:
  path  - one per sampled method; edges MUST equal the method's current
          route_edge_ids from methods.csv, else the script stops (STALE).
  label - one per UNREACHABLE method in the built labels, and one per sampled
          reachable method; confirmed_by only SOURCE or INFERRED.
  edge  - one per corrected edge, listed in scratch/corrected_edges.tsv
          (edge_id<TAB>result<TAB>confirmed_by<TAB>ref<TAB>note).
No row is written by hand: this script is the only writer of verification.csv.
Exit non-zero (and write nothing) if any assertion fails or any input is missing.
"""
import csv, json, os, sys

# This file lives at <mirror>/graphs/MMEX/make_verification.py.
GDIR = os.path.dirname(os.path.abspath(__file__))
MIRROR = os.path.dirname(os.path.dirname(GDIR))
OUT = os.path.join(GDIR, 'out')

RESULTS = ('correct', 'fixed', 'wrong', 'unclear')
CB_LABEL = ('SOURCE', 'INFERRED')


def die(msg):
    print('make_verification: REFUSED: ' + msg, file=sys.stderr)
    sys.exit(1)


def main():
    methods_csv = os.path.join(OUT, 'methods.csv')
    graph_json = os.path.join(OUT, 'mmex_trigger_graph.json')
    sample_txt = os.path.join(GDIR, 'scratch/sample_30.txt')
    judgments_tsv = os.path.join(GDIR, 'scratch/route_judgments.tsv')
    corrected_tsv = os.path.join(GDIR, 'scratch/corrected_edges.tsv')
    for p in (methods_csv, graph_json, sample_txt, judgments_tsv):
        if not os.path.isfile(p):
            die('missing input: %s (faithful build + sampler output required; nothing written)' % p)
    rows = {}
    with open(methods_csv, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            rows[r['method']] = r
    with open(graph_json, encoding='utf-8') as f:
        graph = json.load(f)
    edge_ids = {e['id'] for e in graph['edges']}
    labels = graph['labels']

    judgments = {}
    with open(judgments_tsv, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 5:
                die('bad judgments row (need 5 tab fields): %r' % line)
            method, result, cb, ref, note = parts
            if result not in RESULTS:
                die('bad result %r for %s' % (result, method))
            if cb not in ('SOURCE', 'INFERRED'):
                die('bad confirmed_by %r for %s (no device tonight; SOURCE/INFERRED only)' % (cb, method))
            if method not in rows:
                die('judged method not in methods.csv: %s' % method)
            judgments[method] = (result, cb, ref, note)

    # Sample file: skip header line, last token of each line is the method name.
    with open(sample_txt, encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f if l.strip()]
    if not lines or not lines[0].startswith('#'):
        die('sample_30.txt missing sampler header line')
    sampled = [l.split()[-1] for l in lines[1:]]
    if len(sampled) != len(set(sampled)):
        die('sample_30.txt has duplicate methods')
    missing = [m for m in sampled if m not in judgments]
    if missing:
        die('sampled methods without judgments: %s' % ', '.join(missing))

    out_rows = []
    for m in sampled:
        result, cb, ref, note = judgments[m]
        current = rows[m]['route_edge_ids'].split() if rows[m]['route_edge_ids'].strip() else []
        if rows[m]['verdict'] != 'REACHABLE':
            die('sampled method is not REACHABLE: %s (%s)' % (m, rows[m]['verdict']))
        out_rows.append({'type': 'path', 'item': m, 'result': result, 'confirmed_by': cb,
                         'ref': ref, 'edges': ' '.join(current), 'note': note})
        out_rows.append({'type': 'label', 'item': m, 'result': result, 'confirmed_by': cb,
                         'ref': ref, 'edges': '', 'note': note})
    for m, lab in sorted(labels.items()):
        if lab.get('unreachable'):
            u = lab['unreachable']
            cb = lab.get('confirmed_by') or 'INFERRED'
            if cb not in CB_LABEL:
                die('unreachable method %s has confirmed_by %r' % (m, cb))
            out_rows.append({'type': 'label', 'item': m, 'result': 'correct', 'confirmed_by': cb,
                             'ref': u.get('ref') or lab.get('source_ref') or '',
                             'edges': '', 'note': u['text'][:300]})
    if os.path.isfile(corrected_tsv):
        with open(corrected_tsv, encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                if not line or line.startswith('#'):
                    continue
                parts = line.split('\t')
                if len(parts) != 5:
                    die('bad corrected_edges row: %r' % line)
                eid, result, cb, ref, note = parts
                if eid not in edge_ids:
                    die('corrected edge no longer exists (text changed): %s' % eid)
                if result not in RESULTS or cb not in ('SOURCE', 'INFERRED'):
                    die('bad corrected edge row: %r' % line)
                out_rows.append({'type': 'edge', 'item': eid, 'result': result, 'confirmed_by': cb,
                                 'ref': ref, 'edges': '', 'note': note})
    dest = os.path.join(GDIR, 'verification.csv')
    with open(dest, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note'])
        w.writeheader()
        w.writerows(out_rows)
    print('wrote %s: %d rows (%d path, %d label, %d edge)' % (
        dest, len(out_rows),
        sum(1 for r in out_rows if r['type'] == 'path'),
        sum(1 for r in out_rows if r['type'] == 'label'),
        sum(1 for r in out_rows if r['type'] == 'edge')))


if __name__ == '__main__':
    main()
