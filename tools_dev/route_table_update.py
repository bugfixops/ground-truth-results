#!/usr/bin/env python3
"""W8 point 2 (Kiro): record re-verified route verdicts in graphs/<App>/scratch/route_table.md.
Usage: python3 -I tools_dev/route_table_update.py <App> < lines
Each input line: method ; VERDICT ; note        (VERDICT: CORRECT, FIXED, WRONG or UNCLEAR)
For each method the "### N. <method> — <stratum>, <k> steps — <VERDICT>" heading gets the current step count
(from graphs/<App>/out/methods.csv), the new verdict and the qualifier "(re-verified 2026-11-07)"; a bullet
"- Re-verified 2026-11-07 (Kiro, self-checked only, second: pending reviewer): <note>" goes right under it.
The earlier bullets stay as the record of the first verification. make_verification.py then writes the path rows."""
import csv, re, sys

app = sys.argv[1]
T = 'graphs/%s/scratch/route_table.md' % app
methods = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8'))}
H = re.compile(r'^(###\s+\d+\.\s+)(.+?)(\s+—\s+.*?,\s*)(\d+)(\s+steps\s+—\s+)(\w+)(?:\s+\((.*)\))?\s*$')
todo = {}
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    m, v, note = [x.strip() for x in line.split(';', 2)]
    assert v in ('CORRECT', 'FIXED', 'WRONG', 'UNCLEAR'), line
    todo[m] = (v, note)
out, done = [], set()
for line in open(T, encoding='utf-8').read().split('\n'):
    h = H.match(line)
    if h and h.group(2) in todo:
        m = h.group(2)
        v, note = todo[m]
        steps = len(methods[m]['route_edge_ids'].split())
        first = h.group(6) + (' ' + h.group(7) if h.group(7) and 're-verified' not in h.group(7) else '')
        if h.group(7) and 're-verified' in h.group(7):
            first = h.group(7).split('first verification: ', 1)[-1] if 'first verification: ' in h.group(7) else h.group(6)
        out.append('%s%s%s%d%s%s (re-verified 2026-11-07; first verification: %s)' % (
            h.group(1), m, h.group(3), steps, h.group(5), v, first))
        out.append('- Re-verified 2026-11-07 (Kiro, self-checked only, second: pending reviewer): %s' % note)
        done.add(m)
        continue
    out.append(line)
missing = set(todo) - done
assert not missing, 'no heading for: %s' % ', '.join(sorted(missing))
open(T, 'w', encoding='utf-8').write('\n'.join(out))
print('%s: %d headings updated' % (app, len(done)))
