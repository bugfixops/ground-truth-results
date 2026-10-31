import re, sys, glob, os
G='/Users/darshan/Desktop/yang/work/graphs/MMEX/'
files = [G+'graph_def.py'] + sorted(glob.glob(G+'parts/label_*.py'))
texts = {f: open(f, encoding='utf-8', errors='replace').read() for f in files}
for name in sys.argv[1:]:
    hits = []
    for f, t in texts.items():
        for m in re.finditer(r"UNREACHABLE\['%s'\]" % re.escape(name), t):
            hits.append('UNREACH in %s' % os.path.basename(f))
        for m in re.finditer(r"e\('[^']*', '%s'" % re.escape(name), t):
            hits.append('edge-in in %s' % os.path.basename(f))
        for m in re.finditer(r"e\('%s', " % re.escape(name), t):
            hits.append('edge-out in %s' % os.path.basename(f))
    print(name, '|', '; '.join(sorted(set(hits))) or 'no label in graph_def/parts')
