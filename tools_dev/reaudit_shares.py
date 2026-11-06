#!/usr/bin/env python3
"""Class shares over never-run methods (monkey_hit 0 and ape_hit 0), before and after the re-audit (Kiro, W10).
Usage, from the repo root: python3 -I tools_dev/reaudit_shares.py <before-commit>
'before' reads graphs/<App>/out/ at the given commit (git show); 'after' reads the working tree's out/ (the CI output).
Classes follow review/TASK_NOTE.md; the weighted line uses review/measure.py's WEIGHTS."""
import collections, csv, io, subprocess, sys
sys.path.insert(0, 'review')
WEIGHTS = {'Aegis': 897, 'AmazeFileManager': 1012, 'AnkiDroid': 1633, 'LibreTorrent': 1510, 'MMEX': 1495}
CL = ['dead', 'config', 'env', 'state', 'library', 'gui']
def cls(r):
    if r['verdict'] != 'REACHABLE':
        return 'config' if r['unreachable_kind'] in ('closed_by_configuration', 'closed_by_api_level') else 'dead'
    if [k for k in (r['env_kinds'] or '').split(';') if k and k != 'permission']: return 'env'
    if r['state_kinds']: return 'state'
    if r['explicit_standard_route'] == 'no': return 'library'
    return 'gui'
def read(app, name, commit):
    p = 'graphs/%s/out/%s' % (app, name)
    txt = subprocess.run(['git', 'show', '%s:%s' % (commit, p)], capture_output=True, text=True).stdout if commit else open(p, encoding='utf-8').read()
    return list(csv.DictReader(io.StringIO(txt)))
def shares(app, commit):
    san = {r['method']: r for r in read(app, 'sanity_check.csv', commit)}
    rows = [r for r in read(app, 'methods.csv', commit) if r['method'] in san and san[r['method']]['monkey_hit'] in ('0', '') and san[r['method']]['ape_hit'] in ('0', '')]
    c = collections.Counter(cls(r) for r in rows)
    return len(rows), {k: 100.0 * c[k] / max(1, len(rows)) for k in CL}
before = sys.argv[1]
tot = {'before': collections.Counter(), 'after': collections.Counter()}
for app in WEIGHTS:
    nb, b = shares(app, before); na, a = shares(app, None)
    print('%s never-run %d -> %d' % (app, nb, na))
    print('  before: ' + ', '.join('%s %.1f' % (k, b[k]) for k in CL))
    print('  after:  ' + ', '.join('%s %.1f' % (k, a[k]) for k in CL))
    for k in CL:
        tot['before'][k] += WEIGHTS[app] * b[k]; tot['after'][k] += WEIGHTS[app] * a[k]
W = sum(WEIGHTS.values())
for side in ('before', 'after'):
    print('weighted %s: ' % side + ', '.join('%s %.1f' % (k, tot[side][k] / W) for k in CL))
