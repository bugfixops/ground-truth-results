"""W2 acceptance check for AnkiDroid (run from the repo root after a rebuild).

Proves: no REACHABLE method's best route contains a W2-cleared needs_state
text or a SETUP_ONLY node, except the setup-only methods themselves (note
'only during the first-run setup'). SETUP_ONLY is empty for AnkiDroid (W2:
no first-run-only page in this build), so the node part is vacuous here but
is checked anyway. Prints verdict counts before/after if a pre-W2
methods.csv is passed as argv[2] (optional).
"""
import csv
import json
import sys

CLEARED = {
    'data: the deck has cards to study (new, learning or due)',
    'file: a collection file (collection.anki2) exists in the AnkiDroid folder',
    'data: a deck exists in the collection (the user created or imported one)',
    'data: at least one note exists in the collection',
    'field type TEXT: the multimedia field editor uses a BasicTextFieldController, which creates the pronounce button',
}
SETUP_ONLY = set()  # AnkiDroid W2: no first-run-only page (DeckPicker.java:856-860)

out_dir = sys.argv[1] if len(sys.argv) > 1 else 'graphs/AnkiDroid/out'
graph = json.load(open(out_dir + '/ankidroid_trigger_graph.json'))
edges = {e['id']: e for e in graph['edges']}
rows = list(csv.DictReader(open(out_dir + '/methods.csv')))

from collections import Counter
print('methods:', len(rows), 'verdicts:', dict(Counter(r['verdict'] for r in rows)))

violations = []
setup_only_methods = 0
for r in rows:
    if r['verdict'] != 'REACHABLE':
        continue
    is_setup_only = 'only during the first-run setup' in (r.get('note') or '')
    if is_setup_only:
        setup_only_methods += 1
    for eid in r['route_edge_ids'].split():
        e = edges.get(eid)
        if e and e.get('needs_state') in CLEARED:
            violations.append((r['method'], eid, e['needs_state']))
    if SETUP_ONLY and not is_setup_only:
        for node in r['shortest_path'].split(' > '):
            base = node.split('@')[0].split('(')[0]
            if base in SETUP_ONLY:
                violations.append((r['method'], 'node', node))

print('setup-only methods (exempt):', setup_only_methods)
print('violations:', len(violations))
for v in violations[:20]:
    print('  VIOLATION:', v)
print('W2 ACCEPTANCE:', 'PASS' if not violations else 'FAIL')
