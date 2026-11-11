"""F1 of review/blind_check/PROTOCOL.md: build the held-out half of the hand-labelled sample by script, without
looking at its rows. Keeps the rows whose id number is even and whose id is not in review/checked_cases.csv, writes them
to review/sample_holdout/<App>.csv with the same columns, and prints only the counts per app (they must total 114).
Usage, from the repo root:  python3 -I tools_dev/build_holdout.py <full sample dir>"""
import csv
import os
import re
import sys

APPS = ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']
src = sys.argv[1]
checked = {r['id'].strip() for r in csv.DictReader(open('review/checked_cases.csv', encoding='utf-8'))}
os.makedirs('review/sample_holdout', exist_ok=True)
total = 0
for app in APPS:
    with open(os.path.join(src, '%s.csv' % app), encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f)
        head = rd.fieldnames
        keep = []
        for r in rd:
            m = re.search(r'-(\d+)$', r['id'].strip())
            if m and int(m.group(1)) % 2 == 0 and r['id'].strip() not in checked:
                keep.append(r)
    with open('review/sample_holdout/%s.csv' % app, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=head)
        w.writeheader()
        w.writerows(keep)
    total += len(keep)
    print('%s %d' % (app, len(keep)))
print('total %d' % total)
