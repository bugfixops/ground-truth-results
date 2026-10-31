import json, re, sys, os
sys.path.insert(0, '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch')
from anon_blocks import blocks, SRC, CL
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo'
D = json.load(open(G + '/out/anymemo_trigger_graph.json'))
PFX = 'org.liberty.android.fantastischmemo.'
ANON = re.compile(r'\$\d')
def top_file(name):
    top = name.split('$')[0]
    for root, _, fs in os.walk(SRC):
        if top + '.java' in fs:
            return os.path.join(root, top + '.java')
    return None
BLK = {}
def block_of(cls):
    """cls like 'PreviewEditActivity$3$1' -> (start,end) of the innermost block containing all its lines"""
    if cls in BLK: return BLK[cls]
    full = PFX + cls.replace('$', '$')
    # class file full name uses the package path; CL keys are fully qualified with package path
    key = [k for k in CL if k.endswith('.' + cls) and k.count('.') >= 4]
    key = [k for k in key if k.split('.')[-1] == cls.split('$')[-1] or True]
    ls = None
    for k in CL:
        if k.endswith('.' + cls) and CL[k]:
            ls = CL[k]; break
    tf = top_file(cls)
    if ls is None or tf is None:
        BLK[cls] = None; return None
    bl = blocks(tf)
    mn, mx = ls[0], ls[-1]
    cands = [(s, e) for s, e in bl if e and s <= mn and e >= mx]
    res = max(cands, key=lambda t: t[0]) if cands else None
    BLK[cls] = res
    return res
def cited(ev):
    out = []
    for m in re.finditer(r'(?:SRC |; )([\w/]+\.java)(?: \(bytecode\))?:(\d+)(?:-(\d+))?', ev or ''):
        out.append((m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))))
    return out
if __name__ == '__main__':
    flags = []
    for e in D['edges']:
        for side in ('src', 'dst'):
            node = e[side]
            if not ANON.search(node): continue
            names = node.split('.')[0]          # class part, e.g. PreviewEditActivity$3$1
            refs = cited(e.get('evidence', ''))
            if not refs: continue
            b = block_of(names)
            if b is None:
                flags.append(('NOBLOCK', e['id'], side, node)); continue
            s, en = b
            hit = [r for r in refs if r[0].split('/')[-1] == (names.split('$')[0] + '.java') and any(s - 2 <= c <= en + 2 for c in range(r[1], r[2] + 1))]
            if not hit:
                flags.append((e['id'], side, node, 'block %d-%d' % (s, en), 'cited ' + ', '.join('%s:%d-%d' % r for r in refs[:2])))
    print('flags', len(flags))
    for f in flags: print(f)
