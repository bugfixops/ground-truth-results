#!/usr/bin/env python3
"""Prose/cb fix pass for Phase 3b spot-check FAILs (batches 1-60 only).

- FAIL-prose rows: append an explicit in-cell supersession note to the
  evidence cell (last cell) of the last-occurrence table line. Labels,
  kinds, confirmed_by untouched. No '|' characters added.
- FAIL-cb rows: normalise the confirmed_by cell '— / X' -> 'X' exactly.
Reads FAIL rows from phase3/spotcheck/batch<N>.md files (lines starting
with '- row N ... FAIL-prose|FAIL-cb'). Only batches 1-60 are fixed;
batches 1-60 are left for their own leaf's summary + fix pass.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SC = os.path.join(BASE, 'spotcheck')
WORK = os.path.join(BASE, 'work')
NOTE = (' [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences '
        'in this cell are superseded by the applied verdict; the label, kind, '
        'and confirmed_by cells govern.]')

def parse_line(line):
    if not line.startswith('|'):
        return None
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if not cells or not re.fullmatch(r'\d+', cells[0]):
        return None
    return cells

prose, cb = [], []
for n in range(1, 61):
    p = os.path.join(SC, f'batch{n}.md')
    if not os.path.exists(p):
        continue
    for ln in open(p, encoding='utf-8', errors='replace'):
        m = re.match(r'\s*-\s*row\s+(\d+)\s*\|.*?\|\s*FAIL-(prose|cb)\b', ln)
        if not m:
            continue
        row, kind = int(m.group(1)), m.group(2)
        if kind == 'prose':
            prose.append((n, row))
        else:
            m2 = re.search(r'cb\s+—\s*/\s*(SOURCE|INFERRED)', ln)
            cb.append((n, row, m2.group(1) if m2 else None))

print(f'prose rows: {len(prose)}, cb rows: {len(cb)}')
fixed_p, fixed_c, problems = [], [], []
for batch, row in prose:
    path = os.path.join(WORK, f'batch{batch}-merge-ready.md')
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    idx = [i for i, ln in enumerate(lines) if (lambda c: c and int(c[0]) == row)(parse_line(ln))]
    if not idx:
        problems.append((batch, row, 'row not found')); continue
    li = idx[-1]
    cells = parse_line(lines[li])
    if NOTE.strip() in cells[-1]:
        continue
    cells[-1] = cells[-1] + NOTE
    lines[li] = '| ' + ' | '.join(cells) + ' |'
    open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    fixed_p.append((batch, row))
for batch, row, want in cb:
    if not want:
        problems.append((batch, row, 'no intended cb parsed')); continue
    path = os.path.join(WORK, f'batch{batch}-merge-ready.md')
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    idx = [i for i, ln in enumerate(lines) if (lambda c: c and int(c[0]) == row)(parse_line(ln))]
    if not idx:
        problems.append((batch, row, 'row not found')); continue
    li = idx[-1]
    cells = parse_line(lines[li])
    done = False
    for j, c in enumerate(cells):
        if c == f'— / {want}':
            cells[j] = want
            done = True
            break
    if not done:
        problems.append((batch, row, f'cell — / {want} not found')); continue
    lines[li] = '| ' + ' | '.join(cells) + ' |'
    open(path, 'w', encoding='utf-8').write('\n'.join(lines))
    fixed_c.append((batch, row, want))
print(f'fixed prose: {len(fixed_p)}, fixed cb: {len(fixed_c)}, problems: {problems}')
with open(os.path.join(BASE, 'fixpass_1_60_log.txt'), 'w') as f:
    for b, r in fixed_p:
        f.write(f'prose {b}/{r}\n')
    for b, r, w in fixed_c:
        f.write(f'cb {b}/{r} -> {w}\n')
    for p in problems:
        f.write(f'PROBLEM {p}\n')
