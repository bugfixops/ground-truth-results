import csv, json, collections, re, os, subprocess
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
SRC = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main'
files = []
for root, _, fs in os.walk(SRC):
    for f in fs:
        if f.endswith('.java') or f.endswith('.kt') or f.endswith('.xml'):
            files.append(os.path.join(root, f))
texts = {p: open(p, encoding='utf-8', errors='replace').read() for p in files}
U = [l.strip() for l in open(G + '/scratch/unresolved.txt') if l.strip()]
auto = json.load(open(G + '/auto_calls.json'))
callers = collections.defaultdict(list)
for c in auto['calls']:
    callers[c['dst']].append(c['src'])
lamb = collections.defaultdict(list)
for l in auto['lambdas']:
    lamb[l['dst']].append(l['src'])
res = []
for m in U:
    base_ = re.sub(r'\(.*', '', m)
    cls, _, name = base_.rpartition('.')
    if '@' in m:
        continue
    if name in ('<init>', '<clinit>'):
        continue
    pat = re.compile(r'\b' + re.escape(name) + r'\s*\(')
    hits = []
    for p, t in texts.items():
        if p.endswith('.java') or p.endswith('.kt'):
            for i, line in enumerate(t.split('\n'), 1):
                if pat.search(line) and not re.search(r'(public|private|protected|static|void|boolean|int|String|Override)\s.*\b' + re.escape(name) + r'\s*\(', line):
                    hits.append('%s:%d' % (os.path.relpath(p, SRC), i))
    res.append((m, len(callers.get(m, [])), len(lamb.get(m, [])), len(hits), hits[:2]))
json.dump(res, open(G + '/scratch/textual.json', 'w'))
nohit = [r for r in res if r[3] == 0 and r[1] == 0 and r[2] == 0]
print('methods checked', len(res), 'no caller no lambda no textual hit:', len(nohit))
print('with textual hits but no bytecode caller:', len([r for r in res if r[3] > 0 and r[1] == 0 and r[2] == 0]))
print('bytecode callers present:', len([r for r in res if r[1] > 0]))
