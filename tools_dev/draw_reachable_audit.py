#!/usr/bin/env python3
"""W9 draw of the reachable audit (re-audit brief W9 point 1; Kiro, tool lead).

Usage, from the repo root, after the last round's CI:
    python3 -I tools_dev/draw_reachable_audit.py [--seed 20261106] [App ...]
For each app (default: the five re-audit apps) and each class of REACHABLE methods (env, state, library, gui;
review/TASK_NOTE.md mapping on out/methods.csv), draws 15 methods at random (all when fewer). Excluded: the
methods of review/sample_tune/ (when that folder exists) and the checked cases (Appendix B of
handoff/MUSE_REAUDIT_5APPS.md until review/checked_cases.csv exists). Writes
graphs/<App>/scratch/reaudit/audit_draw.csv: app, class, draw order, method, steps_from_launch, best route edge ids.
The draw is deterministic: methods are sorted by name before random.Random(seed + app).sample.
"""
import csv
import glob
import os
import random
import re
import sys

APPS = ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']
CLASSES = ['env', 'state', 'library', 'gui']
PER_CLASS = 15


def class_of(r):
    if [k for k in (r['env_kinds'] or '').split(';') if k and k != 'permission']:
        return 'env'
    if r['state_kinds']:
        return 'state'
    if r['explicit_standard_route'] == 'no':
        return 'library'
    return 'gui'


def excluded():
    out = set()
    if os.path.exists('review/checked_cases.csv'):
        for r in csv.DictReader(open('review/checked_cases.csv', encoding='utf-8')):
            out.add((r.get('app') or r.get('case', '').rsplit('-', 1)[0], r.get('target') or r.get('method')))
    else:
        txt = open('handoff/MUSE_REAUDIT_5APPS.md', encoding='utf-8').read().split('## Appendix B')[1].split('## Appendix C')[0]
        for line in txt.split('\n'):
            m = re.match(r'\|\s*([\w-]+)-(\d+)\s*\|\s*`([^`]+)`', line)
            if m:
                out.add((m.group(1), m.group(3)))
    for p in glob.glob('review/sample_tune/**/*.csv', recursive=True):
        for r in csv.DictReader(open(p, encoding='utf-8')):
            app = r.get('app')
            m = r.get('method') or r.get('target')
            if app and m:
                out.add((app, m))
    return out


def main():
    args = sys.argv[1:]
    seed = 20261106
    if args[:1] == ['--seed']:
        seed = int(args[1])
        args = args[2:]
    apps = args or APPS
    ex = excluded()
    for app in apps:
        rows = [r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8')) if r['verdict'] == 'REACHABLE']
        out = []
        for c in CLASSES:
            pool = sorted((r for r in rows if class_of(r) == c and (app, r['method']) not in ex
                           and not any(r['method'].startswith(t + '(') or r['method'] == t for a, t in ex if a == app)),
                          key=lambda r: r['method'])
            rng = random.Random('%d:%s:%s' % (seed, app, c))
            pick = pool if len(pool) <= PER_CLASS else rng.sample(pool, PER_CLASS)
            for k, r in enumerate(pick, 1):
                out.append([app, c, k, r['method'], r['steps_from_launch'], r['route_edge_ids']])
        path = 'graphs/%s/scratch/reaudit/audit_draw.csv' % app
        with open(path, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(['app', 'class', 'order', 'method', 'steps_from_launch', 'route_edge_ids'])
            w.writerows(out)
        print('%s: drew %d (%s)' % (app, len(out), ', '.join('%s %d' % (c, sum(1 for o in out if o[1] == c)) for c in CLASSES)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
