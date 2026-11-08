# W3 check (Kiro): methods whose best route uses an env gate from an exported
# or external entry. Usage, from the repo root:
#   python3 -I graphs/<App>/scratch/reaudit/check_w3.py <App> [<outdir>]
# An "env entry" is an ENTRY edge that carries an env gate (exported component,
# system broadcast, PendingIntent, other app). For every REACHABLE method the
# script looks at its best route (methods.csv route_edge_ids) and counts the
# methods whose route contains such an edge, grouped by the edge.
# The same script is copied into each app's scratch/reaudit/.
import collections
import csv
import glob
import json
import sys

app = sys.argv[1]
outdir = sys.argv[2] if len(sys.argv) > 2 else 'graphs/%s/out' % app
g = json.load(open(glob.glob(outdir + '/*_trigger_graph.json')[0], encoding='utf-8'))
rows = list(csv.DictReader(open(outdir + '/methods.csv', encoding='utf-8')))
E = {e['id']: e for e in g['edges']}
env_entry = {i for i, e in E.items() if e['kind'] == 'ENTRY' and e.get('env')}
per = collections.Counter()
n = 0
reach = [r for r in rows if r['verdict'] == 'REACHABLE']
for r in reach:
    hit = [i for i in (r['route_edge_ids'] or '').split() if i in env_entry]
    if hit:
        n += 1
        per[hit[0]] += 1
print('%s: env-gated ENTRY edges: %d' % (app, len(env_entry)))
print('%s: REACHABLE methods whose best route uses an env gate from an exported or external entry: %d of %d'
      % (app, n, len(reach)))
for i, c in per.most_common():
    e = E[i]
    print('  %5d  %s  %s -> %s  | %s | %s' % (c, i, e['src'], e['dst'], ','.join(e.get('env_kinds') or []),
                                         (e.get('env') or '')[:100]))
print('verdicts:', dict(collections.Counter(r['verdict'] for r in rows)))
