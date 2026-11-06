#!/usr/bin/env python3
"""W7 (Kiro): write judgments for flagged steps to graphs/<App>/scratch/reaudit/w7_judged.csv.
Usage: python3 -I tools_dev/guard_judge.py <App> [--replace] < lines
Each input line: step_id ; DECISION ; kinds ; file:line ; text [ ; match=SUBSTRING ]
  text may contain ';'. Only a last part written as match=SUBSTRING is a match: a substring of the edge trigger, so
  the gate goes only on same-key edges whose trigger has it. (Before 2026-11-06 a sixth part was always taken as the
  match, which cut 43 gate texts at their first ';' and kept those gates off; the rows were rejoined.)
  DECISION is NONE (the step's own guard holds in the baseline, or is a GUI action on this step), STATE or ENV
  (text = the gate text written on the edge; kinds from the schema vocabulary), or DEAD.
  One step per line (round-2 review: every row gets its own reason and file:line).
  --replace: a line for a step that is already judged replaces that row (re-judging); without it such lines are
  skipped.
The src/dst/kind of each step come from guard_steps.csv (or, for a step the pre-screen did not list, from
pre_w7_edges.json). The app's graph_def.py W7 block applies STATE and ENV rows to every edge with the same src, dst
and kind that has no gate of that type yet."""
import csv, json, os, sys

app = sys.argv[1]
replace = '--replace' in sys.argv
S = 'graphs/%s/scratch/reaudit/' % app
steps = {r['edge_id']: r for r in csv.DictReader(open(S + 'guard_steps.csv', encoding='utf-8'))}
pre = {e['id']: e for e in json.load(open(S + 'pre_w7_edges.json', encoding='utf-8'))}
path = S + 'w7_judged.csv'
HEAD = ['step', 'kind', 'src', 'dst', 'decision', 'kinds', 'ref', 'text', 'helper', 'auditor', 'match']
rows = list(csv.DictReader(open(path, encoding='utf-8'))) if os.path.exists(path) else []
index = {r['step']: k for k, r in enumerate(rows)}
added = replaced = skipped = 0
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    parts = [x.strip() for x in line.split(';')]
    ids, dec, kinds, ref = parts[:4]
    rest = parts[4:]
    match = ''
    if len(rest) > 1 and rest[-1].startswith('match='):
        match = rest.pop()[len('match='):].strip()
    text = '; '.join(rest)
    assert dec in ('NONE', 'STATE', 'ENV', 'DEAD'), line
    assert ',' not in ids, 'one step per line: ' + line
    i = ids
    s = steps.get(i) or pre.get(i)
    assert s, 'unknown step ' + i
    row = {'step': i, 'kind': s['kind'], 'src': s['src'], 'dst': s['dst'], 'decision': dec, 'kinds': kinds,
           'ref': ref, 'text': text, 'helper': 'Kiro', 'auditor': 'second: pending reviewer', 'match': match}
    if i in index:
        if replace:
            rows[index[i]] = row
            replaced += 1
        else:
            skipped += 1
        continue
    index[i] = len(rows)
    rows.append(row)
    added += 1
with open(path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=HEAD)
    w.writeheader()
    w.writerows(rows)
print('%s: %d added, %d replaced, %d skipped (already judged) (%d in total)' % (app, added, replaced, skipped, len(rows)))
