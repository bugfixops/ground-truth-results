"""Score blind readers against the key (review/blind_check/PROTOCOL.md). Usage, from the repo root:
    python3 -I tools_dev/blind_score.py <pass> <reader dir> [apps...]
Reads <reader dir>/<App>_reader1.csv (first readers) and, when present, <App>_reader2.csv (second readers, missed rows
only) and graphs/<App>/scratch/reaudit/blind_r3b/pass<k>/key.csv. A miss is class_found != our class, except
class_found state with dialog_dependent yes and our class gui (agree). A confirmed miss: the second reader's class_found
equals the first reader's (same exception). Prints per row and per draw; writes <reader dir>/<App>_misses.csv."""
import csv
import os
import sys

k, rdir = int(sys.argv[1]), sys.argv[2]
apps = sys.argv[3:] or ['Aegis', 'AmazeFileManager', 'AnkiDroid', 'LibreTorrent', 'MMEX']


def read(p):
    return {r['id'].strip(): r for r in csv.DictReader(open(p, encoding='utf-8'))} if os.path.exists(p) else None


def miss(r, ours):
    c = (r.get('class_found') or '').strip().lower()
    d = (r.get('dialog_dependent') or '').strip().lower()
    if c == ours:
        return False
    if c == 'state' and d == 'yes' and ours == 'gui':
        return False
    return True


tot = {}
for app in apps:
    key = read('graphs/%s/scratch/reaudit/blind_r3b/pass%d/key.csv' % (app, k))
    r1 = read('%s/%s_reader1.csv' % (rdir, app))
    r2 = read('%s/%s_reader2.csv' % (rdir, app))
    if r1 is None:
        print(app, 'no first reader output')
        continue
    ms = []
    for rid, kr in key.items():
        ours = kr['new_class']
        a = r1.get(rid)
        if a is None:
            print('  %s MISSING in reader 1' % rid)
            continue
        cat = kr['category']
        t = tot.setdefault(cat, [0, 0, 0, 0])  # rows, misses, confirmed, open
        t[0] += 1
        if not miss(a, ours):
            continue
        t[1] += 1
        ms.append(rid)
        st = 'pending'
        if r2 is not None and rid in r2:
            b = r2[rid]
            c1 = a['class_found'].strip().lower()
            c2 = b['class_found'].strip().lower()
            if c2 == c1 or not miss(b, c1):
                st = 'confirmed'
                t[2] += 1
            elif not miss(b, ours):
                st = 'second agrees with us'
            else:
                st = 'readers differ (worker decides)'
                t[3] += 1
        print('  %s %-9s ours=%-8s r1=%-8s(%s) %s | %s | %s' % (rid, cat, ours, a['class_found'], a.get('dialog_dependent'),
                                                         st, kr['method'], (a.get('gates') or '')[:90]))
    with open('%s/%s_misses.csv' % (rdir, app), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['id', 'app', 'jvm_class', 'method', 'desc'])
        ch = {r['id']: r for r in csv.DictReader(open('graphs/%s/scratch/reaudit/blind_r3b/pass%d/chunk.csv' % (app, k), encoding='utf-8'))}
        for rid in ms:
            c = ch[rid]
            w.writerow([rid, app, c['jvm_class'], c['method'], c['desc']])
    print(app, 'misses', len(ms))
for cat, (n, m, c, o) in sorted(tot.items()):
    print('%s rows %d misses %d confirmed %d open %d precision %.1f%%' % (cat, n, m, c, o, 100.0 * (1 - c / n) if n else 0))
