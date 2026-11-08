# W6 sweep (Kiro): edges on REACHABLE best routes that may consume outside data but carry no env gate
# on the route. Usage, from the repo root: python3 -I graphs/<App>/scratch/reaudit/w6_sweep.py <App> [out.csv]
# Groups (brief W6): (a) results from other apps, (b) network and servers, (c) data only older versions
# write, (d) limits of the API 27 image. A method is counted for an edge only when its best route has no
# env gate at all (a route that already carries env is env whatever this edge does).
# The same script is copied into each app's scratch/reaudit/.
import collections
import csv
import glob
import json
import re
import sys

GROUPS = [
    ('a other_app', re.compile(r'ACTION_(OPEN_DOCUMENT|CREATE_DOCUMENT|GET_CONTENT|PICK|SEND|VIEW)|registerForActivityResult|'
                               r'StartActivityForResult|onActivityResult|getData\(\)|document picker|file picker|chooser', re.I)),
    ('b network', re.compile(r'Retrofit|OkHttp|HttpURLConnection|onResponse\b|HttpSyncer|AnkiWeb|\bYql|socket|\bSFTP|\bSSH\b|'
                             r'SshClient|jcifs|\bSmb|\bFTP\b|FTPClient|https?://|\burl\.openConnection|server', re.I)),
    ('c older version', re.compile(r'migrat|legacy|onUpgrade|oldVersion|old format|older (app )?version|upgrade', re.I)),
    ('d API 27 limits', re.compile(r'SDK_INT\s*>=?\s*(2[89]|3\d)|VERSION_CODES\.(P|Q|R|S|TIRAMISU)\b|API (2[89]|3\d)', re.I)),
]

app = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
E = {e['id']: e for e in g['edges']}
hits = collections.defaultdict(lambda: [None, 0])
for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8')):
    if r['verdict'] != 'REACHABLE':
        continue
    ids = (r['route_edge_ids'] or '').split()
    if any(E[i].get('env') for i in ids):
        continue
    for i in ids:
        e = E[i]
        text = ' '.join(str(e.get(k) or '') for k in ('src', 'dst', 'trigger', 'guard', 'evidence', 'note'))
        for name, pat in GROUPS:
            if pat.search(text):
                hits[(name, i)][0] = e
                hits[(name, i)][1] += 1
rows = sorted(((name, i, e['kind'], e['src'], e['dst'], n,
                ' '.join(str(e.get(k) or '') for k in ('trigger', 'guard', 'evidence'))[:300])
               for (name, i), (e, n) in hits.items()), key=lambda x: (x[0], -x[5]))
print('%s: candidate edges %d' % (app, len(rows)), dict(collections.Counter(r[0] for r in rows)))
for r in rows:
    print('  %-16s %s %-9s %s -> %s  (%d methods)' % (r[0], r[1], r[2], r[3], r[4], r[5]))
if out:
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['group', 'id', 'kind', 'src', 'dst', 'methods', 'text'])
        w.writerows(rows)
