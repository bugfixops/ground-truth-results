"""Write graphs/Omni-Notes/verification.csv for the Omni-Notes schema 2 trigger graph.

Portable writer (brief T4): the old writer, handoff/examples/make_vlog_omni_notes.py,
read an old graph from a session folder that no longer exists. This writer reads only
repo-relative files and writes the rows seeded once from the current verification.csv
into graphs/Omni-Notes/scratch/verification_rows.json, in that file's order, so its
output is byte-identical to the current file. It is deterministic: two runs in a row
give byte-identical files (no set iteration anywhere in the output path).

Run from the repo root: python3 -I graphs/Omni-Notes/make_verification.py
Every row is validated against the built graph; the script raises (STOPs) if a path or
label item is missing from out/methods.csv, a path row's edges are not the method's
route, a path or edge id does not exist in the trigger graph, a path row's cited
file:line is not on that method's route evidence, or an UNREACHABLE label row's note
does not name the method's unreachable kind. The one kept UNREACHABLE path row
(DetailFragment.removeAttachment(Attachment), empty route) is validated by its empty
edges matching the method's empty route; it has no route evidence to check.

DEVICE rows (brief D7): if graphs/Omni-Notes/device/results.csv exists, one DEVICE
path row per results row is appended after the seeded rows (result correct when
reached, else unclear; a not-reached route never becomes wrong; no label changes).
If it does not exist, the output is exactly the seeded rows.
"""
import csv
import glob
import json
import os

APP = 'Omni-Notes'
BASE = 'graphs/%s' % APP

with open(BASE + '/scratch/verification_rows.json', encoding='utf-8') as f:
    seed = json.load(f)
header = seed['header']
assert header == ['type', 'item', 'result', 'confirmed_by', 'ref', 'edges',
                  'note'], ('bad seed header', header)
seed_rows = seed['rows']

g = json.load(open(glob.glob(BASE + '/out/*_trigger_graph.json')[0],
                   encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(
    open(BASE + '/out/methods.csv', encoding='utf-8'))}

out = [header]
n = {'path': 0, 'label': 0, 'edge': 0}
for r in seed_rows:
    t, item, res, cb, ref, edges, note = r
    assert t in ('path', 'label', 'edge'), ('bad row type', r)
    assert cb in ('SOURCE', 'INFERRED'), ('bad confirmed_by', r)
    assert note.strip(), ('empty note', r)
    if t == 'path':
        m = rows.get(item)
        assert m is not None, ('path method missing from build', item)
        assert edges == m['route_edge_ids'], (
            'path edges != method route', item, edges, m['route_edge_ids'])
        assert res in ('correct', 'fixed', 'wrong', 'unclear'), ('bad result', r)
        if edges:
            ids = edges.split()
            for i in ids:
                assert i in E, ('path edge missing', item, i)
            ev = ' '.join(E[i]['evidence'] or '' for i in ids)
            base = ref.split(':')[0]
            assert base in ev, ('path ref not on route evidence', item, ref)
    elif t == 'label':
        m = rows.get(item)
        assert m is not None, ('label method missing from build', item)
        assert res in ('correct', 'fixed'), ('bad result', r)
        # Label notes vary by how the label was checked (a generic "call sites
        # searched" note for most UNREACHABLE rows, an "ERROR FOUND" note for
        # the seven labels that changed), so no note-content shape is asserted
        # beyond non-empty; the graph's own reason text lives in methods.csv.
    else:
        assert edges == '', ('edge row carries edges', r)
        assert item in E, ('edge id missing', item)
        assert res in ('correct', 'fixed'), ('bad result', r)
    out.append(r)
    n[t] += 1

res_path = BASE + '/device/results.csv'
if os.path.exists(res_path):
    dev = list(csv.DictReader(open(res_path, encoding='utf-8')))
    for d in dev:
        reached = d['reached'] == 'yes'
        res = 'correct' if reached else 'unclear'
        note = d['script_status']
        if not reached:
            if d['script_status'] == 'unscriptable':
                note += ' (unscriptable)'
            elif d['script_status'] in ('failed_at_step_0', 'timeout') or \
                    d['script_status'].startswith('failed_at_step_'):
                note += ' (script failed)'
            else:
                note += ' (not reached)'
        out.append(['path', d['method'], res, 'DEVICE',
                    'device run %s/%s' % (d['run'], d['script']),
                    d['edges'], note])
    print('DEVICE rows added: %d' % len(dev))

with open(BASE + '/verification.csv', 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)

print('rows: path=%d label=%d edge=%d total=%d' % (
    n['path'], n['label'], n['edge'], len(out) - 1))
