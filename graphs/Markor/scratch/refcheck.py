import csv, os, re, sys, collections
ROOT = '/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app'
rows = list(csv.DictReader(open('out/methods.csv')))
un = [r for r in rows if r['verdict'] != 'REACHABLE']
outer = collections.OrderedDict()
for r in un:
    cls = r['method'].rsplit('.', 1)[0]
    top = cls.split('$')[0]
    outer.setdefault(top, set()).add(cls)
# index all java text once
files = {}
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.java'):
            p = os.path.join(d, f)
            try:
                files[p] = open(p, encoding='utf-8', errors='replace').read()
            except Exception:
                pass
out = []
for top in outer:
    pat = re.compile(r'\b%s\b' % re.escape(top))
    own = os.path.basename(top + '.java')
    refs = []
    for p, txt in files.items():
        if os.path.basename(p) == own:
            continue
        if pat.search(txt):
            refs.append(os.path.relpath(p, ROOT))
    out.append((top, len(refs), refs))
for top, n, refs in sorted(out, key=lambda x: x[1]):
    print(n, top, '|', ' '.join(x.split('/')[-1] for x in refs[:4]))
