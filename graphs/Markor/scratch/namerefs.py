import csv, json, os, re, sys, collections
# For each unresolved method with no bytecode caller (incoming_edges == 0), count word occurrences of its
# simple name in the app Java sources (src/main java + thirdparty java, build dirs excluded), minus the
# number of method declarations with that name in method_list.json. Zero means: no textual reference
# anywhere except declarations (candidate for no_trigger_in_app, after category check in scratch/roots.py).
ROOT = '/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app'
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
ml = json.load(open(G + 'method_list.json'))
decl = collections.Counter(m['name'] for m in ml)
byKey = {}
for m in ml:
    byKey.setdefault((m['short'], m['desc']), m)
    byKey.setdefault((m['short'].split('(')[0], m['desc']), m)
texts = []
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ('build', '.gradle')]
    for f in fs:
        if f.endswith('.java') or f.endswith('.kt') or f.endswith('.xml'):
            try:
                texts.append(open(os.path.join(d, f), encoding='utf-8', errors='replace').read())
            except Exception:
                pass
big = '\n'.join(texts)
rows = list(csv.DictReader(open(G + 'out/methods.csv')))
names = collections.Counter()
want = []
for r in rows:
    if r['verdict'] == 'REACHABLE' or r['incoming_edges'] != '0':
        continue
    m = byKey.get((r['method'], r['jvm_descriptor'])) or byKey.get((r['method'].split('(')[0], r['jvm_descriptor']))
    if not m or m['name'] in ('<init>', '<clinit>') or m['name'].startswith('lambda$'):
        continue
    want.append((r['method'], m['name'], m['class'], m.get('flags', [])))
    names[m['name']] += 1
occ = {n: len(re.findall(r'\b%s\b' % re.escape(n), big)) for n in names}
zero = [w for w in want if occ[w[1]] - decl[w[1]] <= 0]
print('roots with names', len(want), 'zero-reference names', len(zero))
by = collections.defaultdict(list)
for w in zero:
    by[w[0].rsplit('.', 1)[0]].append(w[0].rsplit('.', 1)[1])
for c in sorted(by):
    print(c, len(by[c]), ' '.join(sorted(set(by[c])))[:300])
