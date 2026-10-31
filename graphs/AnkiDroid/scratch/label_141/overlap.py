import re, glob, sys
ms = [m.strip() for m in open('graphs/AnkiDroid/scratch/label_141/methods.txt') if m.strip()]
files = ['graphs/AnkiDroid/graph_def.py'] + sorted(glob.glob('graphs/AnkiDroid/parts/*.py'))
pat = re.compile(r"""e\(\s*(?P<s>'[^']*'|"[^"]*"|[A-Za-z_][A-Za-z_0-9.]*)\s*,\s*(?P<d>'[^']*'|"[^"]*"|[A-Za-z_][A-Za-z_0-9.]*)""", re.S)
upat = re.compile(r"""UNREACHABLE\[\s*['"]([^'"]+)['"]\s*\]""")
hits = {m: [] for m in ms}
unr = {m: [] for m in ms}
for f in files:
    txt = open(f, encoding='utf-8').read()
    for mm in pat.finditer(txt):
        s = mm.group('s').strip('\'"'); d = mm.group('d').strip('\'"')
        ln = txt.count('\n', 0, mm.start()) + 1
        for m in ms:
            if s == m or d == m:
                hits[m].append((f.split('/')[-1], ln, s, d))
    for mm in upat.finditer(txt):
        k = mm.group(1); ln = txt.count('\n', 0, mm.start()) + 1
        if k in ms: unr[k].append((f.split('/')[-1], ln))
for m in ms:
    print(m, '| edges:', len(hits[m]), '| UNREACHABLE:', unr[m])
    for h in hits[m][:6]:
        print('     ', h)
