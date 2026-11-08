import json, re
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
CL = json.load(open(G + '/scratch/class_lines.json'))
D = json.load(open(G + '/out/anymemo_trigger_graph.json'))
PKG = 'org.liberty.android.fantastischmemo.'
ANON = re.compile(r'\$\d')
def cls_of(node):
    return node.rsplit('.', 1)[0]
def lines_for_class(node):
    c = cls_of(node)
    # top-level package path: the class key is the full name, graph names are relative to the package dirs
    cands = [k for k in CL if k.endswith('.' + c) or k.endswith(c)]
    return cands
def cited(ev):
    out = []
    for m in re.finditer(r'SRC ([\w/]+\.java):(\d+)(?:-(\d+))?', ev or ''):
        a = int(m.group(2)); b = int(m.group(3) or a)
        out.append((m.group(1), a, b))
    return out
flags = []
seen = 0
for e in D['edges']:
    for side in ('src', 'dst'):
        node = e[side]
        if not ANON.search(node):
            continue
        seen += 1
        c = cls_of(node)
        cands = [k for k in CL if k.split('.')[-1] == c.split('.')[-1] and k.endswith('.' + c.split('.')[-1])]
        full = [k for k in cands if k.endswith(c)]
        if not full:
            flags.append((e['id'], side, node, 'class not in build', e.get('evidence', '')[:120])); continue
        cl = set(CL[full[0]])
        refs = cited(e.get('evidence', ''))
        if not refs:
            continue
        ok = False
        for f, a, b in refs:
            if any(l in cl for l in range(a - 1, b + 2)):
                ok = True
        if not ok:
            flags.append((e['id'], side, node, 'cited %s; class lines %s' % (refs[:3], sorted(cl)[:6]), e.get('evidence', '')[:100]))
print('anon endpoints', seen, 'flags', len(flags))
for f in flags[:80]:
    print(f)
