#!/usr/bin/env python3
"""W9 review aid (Kiro): the class of each drawn method on the current build, next to the drawn class. Read-only.

Usage, from the repo root, on a FRESH build:
    python3 -I tools_dev/audit_class_now.py [<App> ...]
Prints one line per drawn method whose class or route changed since the draw (class rule as in
draw_reachable_audit.py: env, state, library, gui), then per app the count of changed classes and changed routes.
"""
import csv
import sys

APPS = sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']


def class_of(r):
    if r['verdict'] != 'REACHABLE':
        return 'UNREACHABLE'
    if [k for k in (r['env_kinds'] or '').split(';') if k and k != 'permission']:
        return 'env'
    if r['state_kinds']:
        return 'state'
    if r['explicit_standard_route'] == 'no':
        return 'library'
    return 'gui'


for app in APPS:
    G = 'graphs/%s/' % app
    M = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
    nc = nr = 0
    for d in csv.DictReader(open(G + 'scratch/reaudit/audit_draw.csv', encoding='utf-8')):
        r = M.get(d['method'])
        now = class_of(r) if r else 'MISSING'
        route = r and r['route_edge_ids'].split() != d['route_edge_ids'].split()
        nc += now != d['class']
        nr += bool(route)
        if now != d['class'] or route:
            print('%s %s %s %s: drawn %s, now %s%s' % (app, d['class'], d['order'], d['method'], d['class'], now,
                                                     ' (route changed)' if route else ''))
    print('%s: class changed %d, route changed %d' % (app, nc, nr))
