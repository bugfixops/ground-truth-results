"""Blind check draw (review/blind_check/PROTOCOL.md, round 3b). Usage, from the repo root after a fresh build:
    python3 -I tools_dev/blind_draw.py <pass> <seed> <baseline commit> <reader dir>
Population per app: never-run methods (out/sanity_check.csv monkey_hit 0 and ape_hit 0). Class by the class rule of
review/TASK_NOTE.md (the cls function of tools_dev/reaudit_shares.py). GUI draw: 8 gui methods per app; changed draw:
5 methods whose class differs between <baseline commit> and this build. Methods drawn in an earlier pass are left out.
Writes the label-free chunk per app to <reader dir>/<App>_chunk.csv (for the readers) and the key file with our labels to
graphs/<App>/scratch/reaudit/blind_r3b/pass<k>/key.csv (the chunk is copied there too)."""
import csv
import glob
import io
import json
import os
import random
import subprocess
import sys

APPS = ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']
_src = open('tools_dev/reaudit_shares.py', encoding='utf-8').read()
_ns = {}
exec(_src[_src.index('def cls'):_src.index('def read')], _ns)
cls = _ns['cls']

k, seed, base, rdir = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
os.makedirs(rdir, exist_ok=True)
rng = random.Random(seed)
print('pass %d seed %d baseline %s' % (k, seed, base))
for app in APPS:
    never = {r['method'] for r in csv.DictReader(open('graphs/%s/out/sanity_check.csv' % app, encoding='utf-8'))
             if r['monkey_hit'] == '0' and r['ape_hit'] == '0'}
    rows = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8'))}
    old = subprocess.run(['git', 'show', '%s:graphs/%s/out/methods.csv' % (base, app)], capture_output=True, text=True,
                         check=True).stdout
    oldc = {r['method']: cls(r) for r in csv.DictReader(io.StringIO(old))}
    earlier = set()
    for p in glob.glob('graphs/%s/scratch/reaudit/blind_r3b/pass*/key.csv' % app):
        if not p.endswith('pass%d/key.csv' % k):
            earlier |= {r['method'] for r in csv.DictReader(open(p, encoding='utf-8'))}
    pop = sorted(m for m in never if m in rows and m not in earlier)
    gui = [m for m in pop if cls(rows[m]) == 'gui']
    chg = [m for m in pop if m in oldc and oldc[m] != cls(rows[m])]
    g = rng.sample(gui, min(8, len(gui)))
    c = rng.sample([m for m in chg if m not in g], min(5, len([m for m in chg if m not in g])))
    items = [(m, 'gui_draw') for m in g] + [(m, 'changed') for m in c]
    rng.shuffle(items)
    kdir = 'graphs/%s/scratch/reaudit/blind_r3b/pass%d' % (app, k)
    os.makedirs(kdir, exist_ok=True)
    chunk = [['id', 'app', 'jvm_class', 'method', 'desc']]
    key = [['id', 'method', 'category', 'old_class', 'new_class']]
    for i, (m, cat) in enumerate(items, 1):
        r = rows[m]
        rid = '%s-F%02d' % (app, i) if k == 1 else '%s-S%02d' % (app, i)
        chunk.append([rid, app, r['jvm_class'], m, r['jvm_descriptor']])
        key.append([rid, m, cat, oldc.get(m, ''), cls(r)])
    for path, data in (('%s/%s_chunk.csv' % (rdir, app), chunk), ('%s/chunk.csv' % kdir, chunk), ('%s/key.csv' % kdir, key)):
        with open(path, 'w', encoding='utf-8', newline='') as f:
            csv.writer(f).writerows(data)
    print('%s never-run %d gui %d changed %d drawn gui %d changed %d' % (app, len(never), len(gui), len(chg), len(g), len(c)))
