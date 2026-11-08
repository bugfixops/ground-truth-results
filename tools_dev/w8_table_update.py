#!/usr/bin/env python3
"""W8 (Kiro, review 4): update a 9-column route table (Aegis / LibreTorrent layout:
| # | Stratum | Method | Steps | ENV | STATE | Verdict | Decisive | Edge ids |) and its sample file for the routes whose
best route changed. Usage, from the repo root, after a fresh build:
    python3 -I tools_dev/w8_table_update.py <App> <table.md> <sample.txt> < notes
notes: one line per changed method: 'METHOD ; RECHECK ; note' with RECHECK CORRECT, WRONG or UNCLEAR (the re-check result).
The verdict kept follows review 3 fix 4: a first verdict WRONG or '... (fixed)' is kept; otherwise the re-check result is
written. The decisive text becomes 'W8 re-verified 2026-11-07 (first verification: X; re-check: Y). note Earlier: <old text>'.
Steps, ENV, STATE and edge ids are copied from out/methods.csv. Every changed method must have a note line."""
import csv, sys
app, table, sample = sys.argv[1:4]
rows = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8'))}
notes = {}
for l in sys.stdin:
    if not l.strip(): continue
    m, rc, note = [x.strip() for x in l.split(' ; ', 2)]
    assert rc in ('CORRECT', 'WRONG', 'UNCLEAR'), l
    notes[m] = (rc, note)
out, changed = [], []
for l in open(table, encoding='utf-8').read().split('\n'):
    f = [c.strip() for c in l.strip().strip('|').split('|')] if l.startswith('| ') else []
    if l.startswith('| ') and len(f) > 6 and f[0].isdigit() and len(f) != 9:
        f = [c.strip() for c in l.strip()[1:-1].split('|', 5)]  # 6-column layout: the reason may hold '|'
    six = len(f) == 6 and f[0].isdigit()
    if six:  # | # | Method | Stratum | Steps | Verdict | Reason |  (LibreTorrent); changed = has a note
        m = f[1]; r = rows[m]
        if m in notes:
            rc, note = notes.pop(m)
            first = f[4]
            keep = first == 'WRONG' or first.endswith('(fixed)')
            verdict = first if keep else rc
            old = f[5].split(' Earlier: ', 1)[-1] if f[5].startswith('W8 re-verified') else f[5]
            f[3] = r['steps_from_launch']; f[4] = verdict
            f[5] = 'W8 re-verified 2026-11-07 (first verification: %s; re-check: %s). %s Earlier: %s' % (first, rc, note, old)
            changed.append((m, first, rc, verdict))
            l = '| ' + ' | '.join(f) + ' |'
    elif len(f) == 9 and f[0].isdigit():
        m = f[2]; r = rows[m]
        if r['route_edge_ids'].split() != f[8].split():
            assert m in notes, ('no note for changed route', m)
            rc, note = notes.pop(m)
            first = f[6]
            keep = first == 'WRONG' or first.endswith('(fixed)')
            verdict = first if keep else rc
            old = f[7]
            if old.startswith('W8 re-verified'):
                old = old.split(' Earlier: ', 1)[-1]
            f[3] = r['steps_from_launch']; f[4] = r['env_kinds'] or '-'; f[5] = r['state_kinds'] or '-'
            f[6] = verdict
            f[7] = 'W8 re-verified 2026-11-07 (first verification: %s; re-check: %s). %s Earlier: %s' % (first, rc, note, old)
            f[8] = r['route_edge_ids']
            changed.append((m, first, rc, verdict))
            l = '| ' + ' | '.join(f) + ' |'
    out.append(l)
assert not notes, ('notes for unchanged routes', sorted(notes))
open(table, 'w', encoding='utf-8').write('\n'.join(out))
# sample file: the third token is the step count, the last the method
so = []
for l in open(sample, encoding='utf-8').read().split('\n'):
    t = l.split()
    if len(t) >= 3 and t[-1] in rows and t[2].isdigit() and any(c[0] == t[-1] for c in changed):
        parts = l.split(t[2], 1)
        l = parts[0] + rows[t[-1]]['steps_from_launch'] + parts[1]
    so.append(l)
open(sample, 'w', encoding='utf-8').write('\n'.join(so))
for c in changed: print('%-70s first %-16s re-check %-8s written %s' % c)
print('%d rows updated' % len(changed))
