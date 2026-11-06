"""Compare the full labels (graphs/<App>/out/methods.csv) with the independent hand-labelled sample.

Class of a full label (review/TASK_NOTE.md, "Map labels to classes"), first that applies:
  dead or config  verdict UNREACHABLE; config when unreachable_kind is closed_by_configuration or closed_by_api_level,
                  dead otherwise (no_trigger_in_app, framework_never_calls, branch_never_taken)
  env             env_kinds other than permission
  state           state_kinds not empty
  library         explicit_standard_route = no
  gui             everything else

Matching: a sample row (jvm_class, method, desc) matches the methods.csv row with the same jvm_class, the same
simple method name and jvm_descriptor = desc. A sample row with no match is reported, never guessed.

Usage (from the repo root):
  python3 -I review/measure.py --sample review/sample_tune --out review/rounds/<round>
      prints agreement per app and in total, the confusion table (rows: sample, columns: full labels) and the class
      shares weighted by the app weights below; writes into --out:
        agreement.txt        the printed report
        disagreements.csv    every disagreement with both classes and the evidence of both sides
        blind.csv            the same rows with the two classes shown only as A and B (random order, seed below),
                             for adjudication from the source by agents who must not know which side is which
        blind_key.csv        which of A and B is the sample (keep it away from the adjudicators)
Never run it on a held-out file: the held-out half is measured once, at the end, by the reviewer.
"""
import argparse
import collections
import csv
import glob
import os
import random
import re
import sys

APPS = ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']
WEIGHTS = {'Aegis': 897, 'AmazeFileManager': 1012, 'AnkiDroid': 1633, 'LibreTorrent': 1510, 'MMEX': 1495}
CLASSES = ['dead', 'config', 'env', 'state', 'library', 'gui']
CONFIG_KINDS = {'closed_by_configuration', 'closed_by_api_level'}
SEED = 20261105


def full_class(r):
    if r['verdict'] == 'UNREACHABLE':
        return 'config' if r['unreachable_kind'] in CONFIG_KINDS else 'dead'
    if [k for k in re.split(r'[;, ]+', r['env_kinds']) if k and k != 'permission']:
        return 'env'
    if r['state_kinds'].strip():
        return 'state'
    if r['explicit_standard_route'].strip().lower() == 'no':
        return 'library'
    return 'gui'


def simple_name(key):
    """methods.csv key -> simple method name: drop '(params)', '#n', then take the part after the last dot."""
    k = re.sub(r'#\d+$', '', key.split('(')[0])
    return k.rsplit('.', 1)[-1]


def norm_class(c):
    return (c or '').strip().replace('/', '.')


def load_full(app):
    path = 'graphs/%s/out/methods.csv' % app
    rows = list(csv.DictReader(open(path, encoding='utf-8')))
    if not rows or 'jvm_class' not in rows[0]:
        sys.exit('%s has no jvm_class column: rebuild with the current tools/build_graph.py' % path)
    idx = collections.defaultdict(list)
    for r in rows:
        idx[(norm_class(r['jvm_class']), simple_name(r['method']), r['jvm_descriptor'])].append(r)
        idx[(norm_class(r['jvm_class']), simple_name(r['method']), None)].append(r)
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sample', required=True, help='folder with <App>.csv sample files')
    ap.add_argument('--out', required=True, help='folder for the round report')
    ap.add_argument('--apps', nargs='*', default=APPS)
    a = ap.parse_args()
    if 'holdout' in os.path.abspath(a.sample).lower():
        print('note: this looks like the held-out half; only the reviewer measures it, once, at the end')
    os.makedirs(a.out, exist_ok=True)
    rep, dis = [], []
    conf = collections.Counter()
    per_app = {}
    shares = {'full': collections.Counter(), 'sample': collections.Counter()}
    for app in a.apps:
        f = os.path.join(a.sample, '%s.csv' % app)
        if not os.path.exists(f):
            rep.append('%s: no sample file %s' % (app, f))
            continue
        srows = list(csv.DictReader(open(f, encoding='utf-8')))
        need = {'class', 'jvm_class', 'method', 'desc'}
        if not srows or not need <= set(srows[0]):
            sys.exit('%s: needs the columns %s; has %s' % (f, sorted(need), list(srows[0]) if srows else 'no rows'))
        idcol = 'id' if 'id' in srows[0] else list(srows[0])[0]
        idx = load_full(app)
        n = agree = 0
        unmatched = []
        app_counts = {'full': collections.Counter(), 'sample': collections.Counter()}
        for s in srows:
            sc = s['class'].strip().lower()
            if sc not in CLASSES:
                sys.exit('%s %s: unknown sample class %r' % (f, s[idcol], s['class']))
            key = (norm_class(s['jvm_class']), s['method'].strip().rsplit('.', 1)[-1], s['desc'].strip())
            hits = idx.get(key) or idx.get(key[:2] + (None,))
            if not hits or len({full_class(h) for h in hits}) > 1 and not idx.get(key):
                unmatched.append(s[idcol])
                continue
            r = hits[0]
            fc = full_class(r)
            n += 1
            agree += fc == sc
            conf[(sc, fc)] += 1
            app_counts['full'][fc] += 1
            app_counts['sample'][sc] += 1
            if fc != sc:
                dis.append({'id': s[idcol], 'app': app, 'jvm_class': s['jvm_class'], 'method': s['method'], 'desc': s['desc'],
                            'sample_class': sc, 'full_class': fc, 'full_method_key': r['method'],
                            'sample_reason': s.get('reason', ''), 'sample_evidence': s.get('evidence', ''), 'sample_route': s.get('route', ''),
                            'full_env': r['env'], 'full_state': r['state'], 'full_route': r['shortest_path'],
                            'full_route_edge_ids': r['route_edge_ids'], 'full_route_edge_classes': r['route_edge_classes']})
        per_app[app] = (n, agree)
        for side in ('full', 'sample'):
            for c, k in app_counts[side].items():
                shares[side][c] += WEIGHTS[app] * k / max(1, n)
        rep.append('%-16s matched %3d of %3d, agree %3d (%.1f%%)%s' % (
            app, n, len(srows), agree, 100.0 * agree / max(1, n), ('; unmatched ids: %s' % ' '.join(unmatched)) if unmatched else ''))
    tn = sum(v[0] for v in per_app.values())
    ta = sum(v[1] for v in per_app.values())
    rep.append('TOTAL            matched %d, agree %d (%.1f%%)' % (tn, ta, 100.0 * ta / max(1, tn)))
    rep.append('')
    rep.append('confusion (rows: sample, columns: full labels)')
    rep.append('%-9s' % '' + ''.join('%9s' % c for c in CLASSES))
    for sc in CLASSES:
        rep.append('%-9s' % sc + ''.join('%9d' % conf[(sc, fc)] for fc in CLASSES))
    rep.append('')
    wsum = sum(WEIGHTS[x] for x in per_app if per_app[x][0])
    rep.append('class shares weighted by the app weights (%):')
    for c in CLASSES:
        rep.append('  %-8s full %5.1f   sample %5.1f' % (c, 100.0 * shares['full'][c] / max(1, wsum), 100.0 * shares['sample'][c] / max(1, wsum)))
    text = '\n'.join(rep)
    print(text)
    open(os.path.join(a.out, 'agreement.txt'), 'w', encoding='utf-8').write(text + '\n')
    cols = list(dis[0]) if dis else ['id']
    with open(os.path.join(a.out, 'disagreements.csv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator='\n')
        w.writeheader()
        w.writerows(dis)
    rnd = random.Random(SEED)
    with open(os.path.join(a.out, 'blind.csv'), 'w', encoding='utf-8', newline='') as fb, \
            open(os.path.join(a.out, 'blind_key.csv'), 'w', encoding='utf-8', newline='') as fk:
        wb = csv.writer(fb, lineterminator='\n')
        wk = csv.writer(fk, lineterminator='\n')
        wb.writerow(['id', 'app', 'jvm_class', 'method', 'desc', 'label_A', 'label_B'])
        wk.writerow(['id', 'A_is'])
        for d in dis:
            flip = rnd.random() < 0.5
            A, B = (d['full_class'], d['sample_class']) if flip else (d['sample_class'], d['full_class'])
            wb.writerow([d['id'], d['app'], d['jvm_class'], d['method'], d['desc'], A, B])
            wk.writerow([d['id'], 'full' if flip else 'sample'])
    print('\nwrote %s/agreement.txt, disagreements.csv (%d rows), blind.csv, blind_key.csv' % (a.out, len(dis)))


if __name__ == '__main__':
    main()
