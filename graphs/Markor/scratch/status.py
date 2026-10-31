import csv, json, sys, collections
# Usage: python3 -I scratch/status.py [class-substring ...]
# One line per UNRESOLVED root (no incoming non-REGISTER edge): node, category, identifier count minus declarations (idtext),
# dotted-call count (dot). Writes scratch/status.tsv and prints a per-class summary.
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
ml = json.load(open(G + 'method_list.json'))
hier = json.load(open(G + 'scratch/hier.json'))
txt = json.load(open(G + 'scratch/textcount.json'))
dot = json.load(open(G + 'scratch/dotcount.json'))
g = json.load(open(G + 'out/markor_trigger_graph.json'))
inc = collections.defaultdict(list)
for x in g['edges']:
    if x['kind'] != 'REGISTER':
        inc[x['dst'].split('@')[0]].append(x['src'])
decl = collections.Counter(m['name'] for m in ml)
universe = {m['class'] for m in ml}
flags = {(m['class'], m['name'], m['desc']): m.get('flags', []) for m in ml}
byKey = {}
for m in ml:
    byKey.setdefault((m['short'].split('(')[0], m['desc']), m)
    byKey.setdefault((m['short'], m['desc']), m)


def ancestors(c, seen=None):
    seen = set() if seen is None else seen
    h = hier.get(c)
    if h:
        for p in ([h['super']] if h['super'] else []) + h['ifaces']:
            if p and p not in seen:
                seen.add(p)
                ancestors(p, seen)
    return seen


rows = list(csv.DictReader(open(G + 'out/methods.csv')))
out = []
for r in rows:
    if r['verdict'] != 'UNRESOLVED':
        continue
    node = r['method']
    if inc.get(node):
        continue                       # chain: has a live-or-dead caller, decided after its callers
    m = byKey.get((node.split('(')[0], r['jvm_descriptor'])) or byKey.get((node, r['jvm_descriptor']))
    if not m:
        continue
    name, c, fl = m['name'], m['class'], m.get('flags', [])
    if name == '<clinit>':
        cat = 'clinit'
    elif name == '<init>':
        cat = 'init'
    elif 'static' in fl:
        cat = 'static'
    elif 'private' in fl:
        cat = 'private'
    elif name.startswith('lambda$'):
        cat = 'lambda'
    else:
        anc = ancestors(c)
        ext = [a for a in anc if a not in hier and a != 'java/lang/Object']
        ovr = [a for a in anc if a in universe and (a, name, m['desc']) in flags]
        cat = 'app_override' if ovr else ('ext_ancestor' if ext else 'plain')
    idt = txt.get(name, 0) - decl.get(name, 0)
    out.append((node, cat, idt, dot.get(name, 0), c.split('/')[-1]))
with open(G + 'scratch/status.tsv', 'w') as f:
    for o in out:
        f.write('\t'.join(str(x) for x in o) + '\n')
flt = sys.argv[1:]
by = collections.defaultdict(list)
for o in out:
    by[o[4]].append(o)
print('roots', len(out), collections.Counter(o[1] for o in out))
print('zero identifier refs:', sum(1 for o in out if o[2] <= 0), ' zero dotted refs too:', sum(1 for o in out if o[2] <= 0 and o[3] <= 0))
for c in sorted(by, key=lambda k: -len(by[k])):
    if flt and not any(s in c for s in flt):
        continue
    if flt:
        for o in by[c]:
            print('  %-70s %-12s id=%d dot=%d' % (o[0][:70], o[1], o[2], o[3]))
    else:
        z = sum(1 for o in by[c] if o[2] <= 0)
        print('%s n=%d zero=%d cats=%s' % (c, len(by[c]), z, dict(collections.Counter(o[1] for o in by[c]))))
