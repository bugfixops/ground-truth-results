import csv, json, sys, collections
# Usage: python3 -I scratch/roots.py [class-substring]
# Joins out/methods.csv (unresolved rows) with method_list.json and scratch/hier.json.
# For each unresolved method with no bytecode caller (incoming_edges == 0) prints a category.
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
ml = json.load(open(G + 'method_list.json'))
hier = json.load(open(G + 'scratch/hier.json'))
universe = {m['class'] for m in ml}
byKey = {}
for m in ml:
    byKey.setdefault((m['short'], m['desc']), m)
    byKey.setdefault((m['short'].split('(')[0], m['desc']), m)


def ancestors(c, seen=None):
    seen = seen or set()
    h = hier.get(c)
    if not h:
        return seen
    for p in ([h['super']] if h['super'] else []) + h['ifaces']:
        if p and p not in seen:
            seen.add(p)
            ancestors(p, seen)
    return seen


def declared(c, name, desc):
    return any(m['class'] == c and m['name'] == name and m['desc'] == desc for m in ml)


rows = list(csv.DictReader(open(G + 'out/methods.csv')))
cat = collections.Counter()
detail = collections.defaultdict(list)
for r in rows:
    if r['verdict'] == 'REACHABLE' or r['incoming_edges'] != '0':
        continue
    key = (r['method'], r['jvm_descriptor'])
    m = byKey.get(key) or byKey.get((r['method'].split('(')[0], r['jvm_descriptor']))
    if not m:
        cat['NOMATCH'] += 1
        continue
    c = m['class']
    flags = m.get('flags', [])
    name = m['name']
    if sys.argv[1:] and not any(s in c for s in sys.argv[1:]):
        continue
    if name == '<clinit>':
        k = 'clinit'
    elif name == '<init>':
        k = 'init'
    elif 'static' in flags:
        k = 'static'
    elif 'private' in flags:
        k = 'private'
    elif name.startswith('lambda$'):
        k = 'lambda_body'
    else:
        anc = ancestors(c)
        ext = [a for a in anc if a not in hier and a != 'java/lang/Object']
        appov = [a for a in anc if a in universe and declared(a, name, m['desc'])]
        if appov:
            k = 'app_override'
        elif ext:
            k = 'ext_ancestor'
        else:
            k = 'plain'
    cat[k] += 1
    detail[k].append(r['method'])
print(dict(cat))
for k in sorted(detail):
    if k in ('plain', 'static', 'private', 'ext_ancestor', 'app_override', 'init', 'lambda_body', 'clinit'):
        cls = collections.Counter(x.rsplit('.', 1)[0] for x in detail[k])
        print('==', k, len(detail[k]), 'classes', len(cls))
        print('  ', '; '.join('%s %d' % (a, b) for a, b in sorted(cls.items(), key=lambda t: -t[1])[:80]))
