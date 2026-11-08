#!/usr/bin/env python3
"""Apply Phase 3 verdicts to phase3/work/ copies (one batch file at a time).

Sources: verdicts_applied_table.json (L1-L5) + coordinator_verdicts.json
(D34/D35/D36, R1, 58/32 ruling is already inside L3's entries).
Rules:
- Skip stays (new_label == old_label) and verified stands (not in table).
- Skip confirmed_by-only entries' label step; apply only confirmed_by.
- For each (batch,row): take the LAST table line whose first cell == row
  (main table follows conditional tables), assert its label == old_label,
  else log + skip (never corrupt).
- Replace label cell; replace confirmed_by cell if one exists and a new
  value is given; for OPEN->UNREACHABLE append Kind + trace note to the
  evidence cell (last cell); never add '|' characters to evidence.
- Backup lives in work-backup-pre-apply/ (made before this script ran).
"""
import json, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(BASE, 'work')

def label_of(cells):
    for c in cells:
        if c == 'REACHABLE' or c.startswith('REACHABLE '):
            return 'REACHABLE'
        if c == 'OPEN':
            return 'OPEN'
        if c.startswith('UNREACHABLE'):
            return 'UNREACHABLE'
    return None

def label_idx(cells):
    for i, c in enumerate(cells):
        if c == 'REACHABLE' or c.startswith('REACHABLE ') or c == 'OPEN' or c.startswith('UNREACHABLE'):
            return i
    return None

def parse_line(line):
    # returns cells or None if not a numbered table row
    if not line.startswith('|'):
        return None
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if not cells or not re.fullmatch(r'\d+', cells[0]):
        return None
    return cells

def main():
    with open(os.path.join(BASE, 'verdicts_applied_table.json')) as f:
        table = json.load(f)
    with open(os.path.join(BASE, 'coordinator_verdicts.json')) as f:
        coord = json.load(f)
    verdicts = []
    for e in table['entries']:
        verdicts.append({
            'batch': e['batch'], 'row': e['row'], 'leaf': e['leaf'],
            'old_label': e['old_label'], 'new_label': e['new_label'],
            'kind': e.get('unreachable_kind'),
            'confirmed_by': e.get('new_confirmed_by'),
        })
    for e in coord['verdicts']:
        verdicts.append({
            'batch': e['batch'], 'row': e['row'], 'leaf': 'COORD',
            'old_label': 'OPEN', 'new_label': e['new_label'],
            'kind': e.get('kind'), 'confirmed_by': e.get('confirmed_by'),
            'evidence': e.get('evidence', ''),
        })
    by_batch = {}
    for v in verdicts:
        by_batch.setdefault(v['batch'], []).append(v)
    applied, skipped, log = [], [], []
    for batch in sorted(by_batch):
        path = os.path.join(WORK, f'batch{batch}-merge-ready.md')
        if not os.path.exists(path):
            log.append(f'batch {batch}: FILE MISSING')
            continue
        with open(path, encoding='utf-8', errors='replace') as f:
            lines = f.read().split('\n')
        # index: row -> list of line indices
        idx = {}
        for i, ln in enumerate(lines):
            cells = parse_line(ln)
            if cells:
                idx.setdefault(int(cells[0]), []).append(i)
        changed = False
        for v in sorted(by_batch[batch], key=lambda x: x['row']):
            row = v['row']
            if row not in idx:
                skipped.append((batch, row, v['leaf'], 'row not found in work file'))
                continue
            li = idx[row][-1]  # last occurrence = main table
            cells = parse_line(lines[li])
            cur = label_of(cells)
            if v['new_label'] is None:
                # confirmed_by-only
                if cur != v['old_label']:
                    skipped.append((batch, row, v['leaf'], f'cb-only label mismatch cur={cur} old={v["old_label"]}'))
                    continue
                li2 = label_idx(cells)
                done = False
                for j in range(li2 + 1, len(cells)):
                    if cells[j] in ('SOURCE', 'INFERRED', '—', '-'):
                        cells[j] = v['confirmed_by']
                        done = True
                        break
                if not done:
                    cells[-1] = cells[-1] + f' confirmed_by {v["confirmed_by"]}.'
                lines[li] = '| ' + ' | '.join(cells) + ' |'
                applied.append((batch, row, v['leaf'], 'confirmed_by-only'))
                changed = True
                continue
            if v['new_label'] == v['old_label']:
                continue  # stay: no edit
            if cur != v['old_label']:
                skipped.append((batch, row, v['leaf'], f'label mismatch cur={cur} old={v["old_label"]}'))
                continue
            li2 = label_idx(cells)
            cells[li2] = v['new_label']
            if v.get('confirmed_by'):
                done = False
                for j in range(li2 + 1, len(cells)):
                    if cells[j] in ('SOURCE', 'INFERRED', '—', '-'):
                        cells[j] = v['confirmed_by']
                        done = True
                        break
                if not done:
                    cells[-1] = cells[-1] + f' confirmed_by {v["confirmed_by"]}.'
            if v['new_label'] == 'UNREACHABLE' and v.get('kind'):
                if 'Kind:' not in cells[-1]:
                    cells[-1] = cells[-1] + f' Kind: `{v["kind"]}`.'
            cells[-1] = cells[-1] + f' [Phase 3 completion 2026-11-01: {v["leaf"]} verdict applied.]'
            lines[li] = '| ' + ' | '.join(cells) + ' |'
            applied.append((batch, row, v['leaf'], f'{v["old_label"]}->{v["new_label"]}'))
            changed = True
        if changed:
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
    print(f'APPLIED: {len(applied)}')
    print(f'SKIPPED: {len(skipped)}')
    for s in skipped:
        print('SKIP:', s)
    with open(os.path.join(BASE, 'apply_log.txt'), 'w') as f:
        for a in applied:
            f.write(f'{a[0]}/{a[1]} {a[2]} {a[3]}\n')
        f.write(f'--- skipped {len(skipped)} ---\n')
        for s in skipped:
            f.write(f'{s}\n')

if __name__ == '__main__':
    main()
