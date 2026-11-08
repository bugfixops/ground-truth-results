import json, os, re, sys, collections
sys.path.insert(0, 'tools')
import build_graph as bg
G = 'graphs/AnkiDroid/'
ROOT = 'final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/'
rows = json.load(open(G + 'method_list.json'))
names, by_name = bg.method_names(rows)
out = open(G + 'scratch/node_names.tsv', 'w')
out.write('node\tclass\tmethod\tdesc\tsource_file\tdecl_line\n')
cnt = collections.Counter()
srccache = {}
for r, n in zip(rows, names):
    cls = r['class']
    outer = cls.split('$')[0]
    src = ROOT + outer + '.java'
    srcrel = ''
    decl = ''
    if os.path.isfile(src):
        srcrel = outer.split('/', 0)[0] and (outer + '.java')
        if src not in srccache:
            srccache[src] = open(src, encoding='utf-8', errors='replace').read().splitlines()
        lines = srccache[src]
        mname = r['name']
        if mname not in ('<init>', '<clinit>'):
            pat = re.compile(r'\b' + re.escape(mname) + r'\s*\(')
            for i, ln in enumerate(lines, 1):
                s = ln.strip()
                if pat.search(ln) and not s.startswith(('*', '//', 'return', 'if ', 'else', 'for ', 'while ')) and not re.search(r'[=;]\s*$', s.split('(')[0] or '') and '.' + mname + '(' not in ln:
                    decl = str(i)
                    break
    out.write('\t'.join([n, cls, r['name'], r['desc'], srcrel, decl]) + '\n')
    cnt[(outer.rsplit('/', 1)[0], 'has_source' if os.path.isfile(src) else 'no_source')] += 1
out.close()
print('nodes', len(names), 'unique', len(set(names)))
for k, v in sorted(cnt.items()):
    print(k, v)
