"""Check 8 helper: for each method listed by check 8, does its UNREACHABLE reason name every bytecode caller?
Run from the repo root after bash handoff/ci/rebuild.sh LibreTorrent:
  python3 -I graphs/LibreTorrent/scratch/kiro/check8_names.py"""
import glob
import json
import re

g = json.load(open(glob.glob('graphs/LibreTorrent/out/*_trigger_graph.json')[0], encoding='utf-8'))
ok = bad = 0
for line in open('graphs/LibreTorrent/scratch/ci_latest/8b_scan_callers.txt', encoding='utf-8'):
    m = re.match(r'(\S+) \[(\w+)\] <- (.*)', line.strip())
    if not m:
        continue
    meth, callers = m.group(1), m.group(3)
    un = g['labels'].get(meth, {}).get('unreachable') or {}
    reason = un.get('text', '')
    names = [c.split(' (')[0].split('@')[0].split('(')[0] for c in callers.split('; ')]
    missing = [n for n in names if n not in reason]
    if missing:
        bad += 1
        print('MISSING  %s  caller(s) not named in its reason: %s' % (meth, ', '.join(missing)))
    else:
        ok += 1
        print('OK       %s' % meth)
print('named: %d, missing: %d' % (ok, bad))
