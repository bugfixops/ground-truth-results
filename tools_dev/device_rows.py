"""DEVICE row input for graphs/<App>/make_verification.py (reviewer rule, 2026-11-09).

The rule, applied the same way in all five apps:
  1. The base rows are graphs/<App>/device/results.csv (written by device/compare.py from the run of record).
  2. LATER_RUNS lists, per app, the routes the reviewer accepted from a later real run. For each listed route the row of
     that run (device/results/<run>/<App>/results.csv, as committed by the bot) replaces the base row of the same
     route. The replacement must have reached=yes and edge ids equal to the method's current best route (asserted).
  3. A reached row (reached=yes) is written only when its replayed edge ids, after the app's documented re-point (if
     any), equal the method's current best route (route_edge_ids in graphs/<App>/out/methods.csv). A reached row that
     replays an older route makes a claim about a route the graph no longer uses, so it is dropped, and the method
     keeps its static label.
  4. Rows that did not reach the method (reached=no or not_run) make no reach claim; they are written as replayed,
     unchanged, whatever their edge ids.
Returns (rows, dropped): rows as dicts with the results.csv columns, in base order; dropped as (route, method, reason).
Loaded with exec() because make_verification.py runs under python3 -I (no script directory on sys.path)."""
import csv
import os

# Third real run, 42683233983-1 (the retry after run 42674277844-1 was lost to a GitHub incident and reached no
# device): the reviewer accepted only the five LibreTorrent routes, whose scripts were made on the current routes.
# Aegis route_21 and MMEX route_21, 24 and 29 failed on the device (unlock step, per-route setup) and give no row.
LATER_RUNS = {
    'LibreTorrent': ('42683233983-1', ('route_01', 'route_09', 'route_10', 'route_17', 'route_19')),
}


def device_rows(gdir, app, repoint=None):
    gdir = str(gdir)
    repoint = repoint or {}
    base = os.path.join(gdir, 'device', 'results.csv')
    if not os.path.exists(base):
        return [], []
    root = os.path.dirname(os.path.dirname(os.path.abspath(gdir)))
    current = {r['method']: r['route_edge_ids'].split()
               for r in csv.DictReader(open(os.path.join(gdir, 'out', 'methods.csv'), encoding='utf-8'))}
    rows = list(csv.DictReader(open(base, encoding='utf-8', newline='')))
    if app in LATER_RUNS:
        run, routes = LATER_RUNS[app]
        later = {r['route']: r for r in csv.DictReader(open(
            os.path.join(root, 'device', 'results', run, app, 'results.csv'), encoding='utf-8', newline=''))}
        for i, r in enumerate(rows):
            if r['route'] in routes:
                n = later[r['route']]
                assert n['method'] == r['method'], ('later run: method differs', app, r['route'])
                assert n['reached'] == 'yes', ('later run: accepted route not reached', app, r['route'])
                assert n['edges'].split() == current.get(n['method']), ('later run: not the current route', app, r['route'])
                rows[i] = {'route': n['route'], 'method': n['method'], 'edges': n['edges'], 'reached': n['reached'],
                           'script_status': n['script_status'], 'run': run, 'script': n['route'] + '.py'}
        assert sum(1 for r in rows if r['run'] == run) == len(routes), ('later run: route missing in base', app)
    out, dropped = [], []
    for r in rows:
        edges = r['edges'].split()
        if r['method'] in repoint:
            edges = repoint[r['method']][1].split()
        if r['reached'] == 'yes' and edges != current.get(r['method']):
            dropped.append((r['route'], r['method'], 'reached row replays an older route (run %s)' % r['run']))
            continue
        out.append(r)
    return out, dropped
