# W6 (Kiro): writes graphs/<App>/scratch/reaudit/outside_data.csv from the pre-W6 sweep (w6_sweep.py output
# given as argv[2]) and the current build: each candidate edge gets ENV when the build now gives that edge an env
# gate (the W6 block in graph_def.py), otherwise KEEP with the group's reason. Usage from the repo root:
#   python3 -I graphs/<App>/scratch/reaudit/w6_write.py <App> <pre-W6 sweep csv> [extra edge ids ...]
import csv, glob, json, sys
app, sweep = sys.argv[1], sys.argv[2]
extra = sys.argv[3:]
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
E = {}
for e in g['edges']:
    E.setdefault((e['src'], e['dst'], e['kind']), e)
KEEP = {
    'a': 'the result comes from one of the app\'s own activities or dialogs (setResult in app code), not from another app',
    'b': 'an in-app step before any server answer (the edge that consumes the answer carries the env gate), a local dialog, or a text match only',
    'c': 'runs on a normal start or the text only names an upgrade; no older-version data is needed',
    'd': 'no API-level limit applies on API 27',
}
rows = list(csv.DictReader(open(sweep, encoding='utf-8')))
seen = set()
out = []
for r in rows:
    key = (r['src'], r['dst'], r['kind'])
    if (r['group'], key) in seen:
        continue
    seen.add((r['group'], key))
    e = E.get(key)
    env = (e or {}).get('env') or ''
    dec = 'ENV' if env else 'KEEP'
    out.append([r['group'], (e or {}).get('id', r['id']), r['kind'], r['src'], r['dst'], r['methods'], dec,
                env if env else KEEP[r['group'][0]], 'self'])
for t in extra:
    s, d, k = t.split('|')
    e = E[(s, d, k)]
    if not any(o[3] == s and o[4] == d and o[2] == k for o in out):
        out.append(['target', e['id'], k, s, d, '', 'ENV', e.get('env'), 'self'])
with open('graphs/%s/scratch/reaudit/outside_data.csv' % app, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['group', 'id', 'kind', 'src', 'dst', 'methods_on_envfree_routes_before', 'decision', 'env text or reason', 'checked_by'])
    w.writerows(out)
print('%s: %d candidate edges, ENV %d, KEEP %d' % (app, len(out), sum(o[6] == 'ENV' for o in out), sum(o[6] == 'KEEP' for o in out)))
