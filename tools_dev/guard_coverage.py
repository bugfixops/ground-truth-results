#!/usr/bin/env python3
"""W7 (Kiro): share of flagged target-uses judged per app (a step counts with the number of never-run targets using it).
Usage, from the repo root: python3 -I tools_dev/guard_coverage.py [App ...]"""
import csv, sys
for A in sys.argv[1:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']:
    S = 'graphs/%s/scratch/reaudit/' % A
    st = {r['edge_id']: int(r['targets']) for r in csv.DictReader(open(S + 'guard_steps.csv', encoding='utf-8'))}
    d = list(csv.DictReader(open(S + 'guard_decisions.csv', encoding='utf-8')))
    tot = sum(st.get(r['step'], 0) for r in d)
    pen = [r for r in d if r['decision'] == 'PENDING']
    print('%-17s flagged rows %5d, PENDING %5d, flagged target-uses judged %.1f%%'
          % (A, len(d), len(pen), 100.0 * (tot - sum(st.get(r['step'], 0) for r in pen)) / max(1, tot)))
