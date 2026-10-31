import json, os, re, collections
ROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo'
files = []
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if f.endswith('.java'):
            files.append(os.path.join(dp, f))
texts = {p: open(p, encoding='utf-8', errors='replace').read() for p in files}
sp = json.load(open('scratch/unres_split.json'))
roots = sp['roots']
def simple(m):
    # 'Cls.name(args)' or 'Cls.<init>(args)' -> (cls, name)
    base = m.split('(')[0]
    cls, _, name = base.rpartition('.')
    return cls, name
out = collections.OrderedDict()
for m in roots:
    cls, name = simple(m)
    short = cls.split('.')[-1].split('$')[0]
    if name == '<clinit>':
        key = 'clinit'
    elif name == '<init>':
        key = 'init'
    else:
        key = 'method'
    if key == 'method':
        rx = re.compile(r'\b' + re.escape(name) + r'\s*\(')
    elif key == 'init':
        rx = re.compile(r'\bnew\s+' + re.escape(short) + r'\s*[<(]')
    else:
        rx = re.compile(r'\b' + re.escape(short) + r'\b')
    hits = []
    for p, t in texts.items():
        for i, line in enumerate(t.split('\n'), 1):
            if rx.search(line):
                hits.append((os.path.relpath(p, ROOT), i, line.strip()))
    out[m] = {'key': key, 'hits': hits}
json.dump({k: {'key': v['key'], 'hits': v['hits'][:12], 'n': len(v['hits'])} for k, v in out.items()}, open('scratch/rootcheck.json', 'w'), indent=1)
cnt = collections.Counter()
for m, v in out.items():
    cnt[(v['key'], 'nohit' if len(v['hits']) == 0 else ('few' if len(v['hits']) <= 2 else 'many'))] += 1
print(cnt)
