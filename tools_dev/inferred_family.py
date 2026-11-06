#!/usr/bin/env python3
"""Review 2 (Kiro): list the AmazeFileManager hand edges with the evidence "INFERRED framework calls ... after
construction of ..." that graph_def.py drops (Q-W8-1). Reads graph_def.py and graph_def_mod/*.py as text; read-only.
Usage: python3 -I tools_dev/inferred_family.py"""
import glob, re

pat = re.compile(r"e\('([^']+)', '([^']+)', '(\w+)'.*?evidence='([^']*INFERRED framework calls [^']* after construction of [^']*)'", re.S)
files = ['graphs/AmazeFileManager/graph_def.py'] + sorted(glob.glob('graphs/AmazeFileManager/graph_def_mod/*.py'))
n = 0
for f in files:
    text = open(f, encoding='utf-8').read()
    for m in pat.finditer(text):
        line = text.count('\n', 0, m.start()) + 1
        keep = m.group(1).startswith('SevenZMethodConfiguration.<init>') and m.group(2) == 'CoderBase.canAcceptOptions'
        print('%s %s:%d %s -> %s [%s]' % ('KEEP' if keep else 'DROP', f.split('/')[-1], line, m.group(1), m.group(2), m.group(3)))
        n += 1
print('%d edges in the family' % n)
