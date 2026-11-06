#!/usr/bin/env python3
"""W7 (Kiro): append judgments for flagged steps to graphs/<App>/scratch/reaudit/w7_judged.csv.
Usage: python3 -I tools_dev/guard_judge.py <App> < lines
Each input line: step_id ; DECISION ; kinds ; file:line ; text [ ; match ]
  match (optional): a substring of the edge trigger; the gate then goes only on same-key edges whose trigger has it
  DECISION is NONE (null check, always-true, baseline, a GUI action on the route, a framework call that always
  happens), STATE or ENV (text = the gate text written on the edge; kinds from the schema vocabulary), or DEAD.
  A step may name several ids separated by commas when one decision covers them.
The src/dst/kind of each step come from guard_steps.csv. The app's graph_def.py W7 block applies STATE and ENV rows
to every edge with the same src, dst and kind that has no gate of that type yet."""
import csv, os, sys
app = sys.argv[1]
S = 'graphs/%s/scratch/reaudit/' % app
steps = {r['edge_id']: r for r in csv.DictReader(open(S + 'guard_steps.csv', encoding='utf-8'))}
path = S + 'w7_judged.csv'
new = not os.path.exists(path)
have = set() if new else {r['step'] for r in csv.DictReader(open(path, encoding='utf-8'))}
n = 0
with open(path, 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    if new:
        w.writerow(['step', 'kind', 'src', 'dst', 'decision', 'kinds', 'ref', 'text', 'helper', 'auditor', 'match'])
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = [x.strip() for x in line.split(';')]
        ids, dec, kinds, ref = parts[:4]
        text = parts[4]
        match = parts[5] if len(parts) > 5 else ''
        assert dec in ('NONE', 'STATE', 'ENV', 'DEAD'), line
        for i in ids.split(','):
            i = i.strip()
            s = steps[i]
            if i in have:
                continue
            w.writerow([i, s['kind'], s['src'], s['dst'], dec, kinds, ref, text, 'Kiro', 'second: pending reviewer', match])
            have.add(i); n += 1
print('%s: %d judgments added (%d in total)' % (app, n, len(have)))
