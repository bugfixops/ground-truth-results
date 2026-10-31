import csv, os, re, collections
WORK = '/Users/darshan/Desktop/yang/work'
G = os.path.join(WORK, 'graphs/AmazeFileManager')
OUT = os.path.join(G, 'scratch/finish23')
JROOT = os.path.join(WORK, 'final_java_only/AmazeFileManager')
idx = collections.defaultdict(list)
for dp, dn, fn in os.walk(JROOT):
    for f in fn:
        if f.endswith('.java'):
            idx[f].append(os.path.join(dp, f))
def pick(name):
    c = idx.get(name, [])
    for key in ('/src/main/', '/src/fdroid/', '/src/play/'):
        for p in c:
            if key in p:
                return p
    return c[0] if c else None
gd = open(os.path.join(G, 'graph_def.py'), encoding='utf-8').read().split('\n')
rows = list(csv.DictReader(open(os.path.join(G, 'scratch/finish22/warn_table.tsv'), encoding='utf-8'), delimiter='\t'))
def jlines(path, pat, n=3):
    out = []
    if not path:
        return ['(no source file on disk)']
    L = open(path, encoding='utf-8', errors='replace').read().split('\n')
    for i, l in enumerate(L):
        if re.search(pat, l):
            out.append('   %s:%d: %s' % (os.path.relpath(path, JROOT).split('/src/')[-1] if '/src/' in path else path, i + 1, l.strip()[:160]))
            if len(out) >= n:
                break
    return out or ['(no match for %s)' % pat]
by = collections.OrderedDict()
for r in rows:
    by.setdefault(r['method'], []).append(r)
with open(os.path.join(OUT, 'dossier.txt'), 'w', encoding='utf-8') as f:
    for m, rs in by.items():
        r0 = rs[0]
        f.write('=== %s\n' % m)
        f.write('  UNREACHABLE: %s | %s | ref: %s\n' % (r0['kind'], r0['reason'], r0['ref']))
        cls, _, name = m.split('(')[0].rpartition('.')
        top = cls.split('$')[0].split('.')[-1]
        simple = cls.split('$')[-1]
        if name == '<init>':
            pat = r'\b%s\s*\(' % re.escape(simple)
        else:
            base = name.split('$')[1] if name.startswith('lambda$') else name
            pat = r'\b%s\s*\(' % re.escape(base)
        dpath = pick(top + '.java')
        f.write('  dst source: %s\n' % (dpath or 'NONE'))
        for l in jlines(dpath, pat, 2):
            f.write(l + '\n')
        for r in rs:
            ln = int(r['edge_line']) if r['edge_line'] else 0
            f.write('  IN %s %s %s from %s [%s] %s\n' % (r['edge_id'], r['edge_kind'], 'auto' if r['auto'] == '1' else 'manual', r['edge_src'], r['src_verdict'], ('gd line %d' % ln) if ln else 'no line'))
            if r['auto'] == '1':
                mm = re.search(r'SRC (\S+):(\d+)', r['edge_evidence'] or '')
                if mm:
                    cp = pick(mm.group(1))
                    if cp:
                        L = open(cp, encoding='utf-8', errors='replace').read().split('\n')
                        ci = int(mm.group(2))
                        f.write('      call site %s:%d: %s\n' % (mm.group(1), ci, L[ci - 1].strip()[:170]))
                    else:
                        f.write('      call site %s:%s (no file on disk)\n' % (mm.group(1), mm.group(2)))
            elif ln:
                for k in range(ln - 1, min(ln + 2, len(gd))):
                    f.write('      gd%d: %s\n' % (k + 1, gd[k].strip()[:170]))
        f.write('\n')
print('methods', len(by), 'rows', len(rows))
