# W5 listing (Kiro): edges on a default class (explicit or standard, authored or set by default; not
# non_standard, not page) whose trigger, evidence, via, note or guard mentions a library or reflection
# mechanism (brief W5 point 2). The build report's REVIEW list (class_basis default + NONSTD_HINT) is a
# subset of this list; it is empty in all five apps at this build.
# Usage, from the repo root: python3 -I graphs/<App>/scratch/reaudit/list_library_edges.py <App> [out.csv]
# Writes one row per edge: id, kind, edge_class, src, dst, matched mechanism, text excerpt.
# The same script is copied into each app's scratch/reaudit/.
import csv
import glob
import json
import re
import sys

PATTERNS = [
    ('EventBus', r'EventBus|@Subscribe\b'),
    ('Rx', r'\bFlowable\b|\bObservable\b|\bSingle\b|\bCompletable\b|\bsubscribe\b|\bRxJava\b|\bMaybe\b'),
    ('data binding', r'Binding\w*Impl|DataBinderMapper|@BindingAdapter|data ?binding'),
    ('XML inflation', r'\binflate\b|PreferenceInflater|android:onClick|XML-declared|declared in (the )?XML|layout XML|preferences?\.xml|res/xml/'),
    ('reflection', r'newInstance|Class\.forName|loadClass|reflection'),
]

app = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
g = json.load(open(glob.glob('graphs/%s/out/*_trigger_graph.json' % app)[0], encoding='utf-8'))
rows = []
for e in g['edges']:
    if e.get('edge_class') in ('non_standard', 'page'):
        continue
    text = ' '.join(str(e.get(k) or '') for k in ('trigger', 'evidence', 'via', 'note', 'guard'))
    hits = [name for name, pat in PATTERNS if re.search(pat, text)]
    if hits:
        rows.append([e['id'], e['kind'], e['edge_class'], e.get('class_basis'), e['src'], e['dst'], '+'.join(hits), text[:400]])
print('%s: default-class edges with a library/reflection hint: %d' % (app, len(rows)))
import collections
print('  by mechanism:', dict(collections.Counter(r[6] for r in rows)))
print('  by kind/class:', dict(collections.Counter((r[1], r[2]) for r in rows)))
if out:
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['id', 'kind', 'edge_class', 'class_basis', 'src', 'dst', 'mechanism', 'text'])
        w.writerows(rows)
