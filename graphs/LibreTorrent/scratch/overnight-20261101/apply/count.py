#!/usr/bin/env python3
"""Mechanical counter for LibreTorrent merge-ready batch files.

Rule (validated in Phase 2): for each batch file, scan lines starting with
'|', split into cells, keep rows whose FIRST cell is exactly digits, take
the label from the cell that is exactly 'REACHABLE' or 'OPEN' or starts
with 'UNREACHABLE' (main-table label column; conditional-table prose
cells never match exactly). Last occurrence per row number wins (main
table follows conditional tables in the files).
Usage: count.py [dir] [--open-only] [--per-batch]
"""
import os, re, sys, glob

def parse_file(path):
    rows = {}
    for line in open(path, encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not cells or not re.fullmatch(r'\d+', cells[0]):
            continue
        label = None
        for c in cells:
            if c == 'REACHABLE' or c.startswith('REACHABLE '):
                label = 'REACHABLE'; break
            if c == 'OPEN':
                label = 'OPEN'; break
            if c.startswith('UNREACHABLE'):
                label = 'UNREACHABLE'; break
        if label is None:
            continue
        rows[int(cells[0])] = label
    return rows

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else '.'
    open_only = '--open-only' in sys.argv
    per_batch = '--per-batch' in sys.argv
    tot = {'REACHABLE': 0, 'UNREACHABLE': 0, 'OPEN': 0}
    files = sorted(glob.glob(os.path.join(d, 'batch*-merge-ready.md')),
                   key=lambda p: int(re.search(r'batch(\d+)', p).group(1)))
    for f in files:
        b = int(re.search(r'batch(\d+)', f).group(1))
        rows = parse_file(f)
        c = {'REACHABLE': 0, 'UNREACHABLE': 0, 'OPEN': 0}
        for v in rows.values():
            c[v] += 1
        for k in tot:
            tot[k] += c[k]
        if per_batch:
            print(f"batch {b}: {c['REACHABLE']}/{c['UNREACHABLE']}/{c['OPEN']} "
                  f"({len(rows)} rows, seq {min(rows) if rows else '-'}-{max(rows) if rows else '-'})")
        if open_only:
            for n in sorted(rows):
                if rows[n] == 'OPEN':
                    print(f"{b}/{n}")
    print(f"TOTAL: {tot['REACHABLE']} REACHABLE / {tot['UNREACHABLE']} UNREACHABLE / "
          f"{tot['OPEN']} OPEN of {sum(tot.values())}")

if __name__ == '__main__':
    main()
