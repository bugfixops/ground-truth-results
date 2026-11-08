# W2 acceptance check for Aegis (Kiro). Usage, from the repo root:
#   python3 -I graphs/Aegis/scratch/reaudit/check_w2.py graphs/Aegis/out
# Verifies, on a fresh build's outputs:
#  1. no edge still carries a cleared (baseline) needs_state text;
#  2. no REACHABLE method's best route contains a cleared text;
#  3. no REACHABLE method's best route passes through a SETUP_ONLY page, unless
#     the method is itself setup-only (note 'only during the first-run setup');
#  4. the SETUP_ONLY gate text on the intro page S_INTRO_SETUP is kept;
#  5. KeyDerivationTask.onPostExecute's best route avoids the intro pages;
#  6. prints verdict and gate totals for the before-after comparison.
import collections
import csv
import json
import sys

outdir = sys.argv[1]
g = json.load(open(outdir + '/aegis_trigger_graph.json', encoding='utf-8'))
rows = list(csv.DictReader(open(outdir + '/methods.csv', encoding='utf-8')))
edges = {e['id']: e for e in g['edges']}
CLEARED = [r['needs_state'] for r in csv.DictReader(open(
    'graphs/Aegis/scratch/reaudit/state_gates.csv', encoding='utf-8')) if r['decision'] == 'CLEAR']
SETUP = {'S_INTRO_WELCOME', 'S_INTRO_PICKER', 'S_INTRO_SETUP', 'S_INTRO_DONE'}
SETUP_NOTE = 'only during the first-run setup'
fail = 0

print('cleared texts:', len(CLEARED))
still = [e['id'] for e in g['edges'] if e.get('needs_state') in CLEARED]
print('1. edges still carrying a cleared text:', len(still), still[:5])
fail += bool(still)

reach = [r for r in rows if r['verdict'] == 'REACHABLE']
bad = []
for r in reach:
    for i in (r['route_edge_ids'] or '').split():
        if (edges.get(i) or {}).get('needs_state') in CLEARED:
            bad.append((r['method'], i))
            break
print('2. REACHABLE methods whose best route contains a cleared text:', len(bad), bad[:5])
fail += bool(bad)


def through_setup(r):
    nodes = set((r['shortest_path'] or '').split(' > '))
    if nodes & SETUP:
        return True
    return any((edges.get(i) or {}).get('src') in SETUP or (edges.get(i) or {}).get('dst') in SETUP
               for i in (r['route_edge_ids'] or '').split())


viol, so = [], []
for r in reach:
    s = SETUP_NOTE in (r['note'] or '')
    if s:
        so.append(r['method'])
    elif through_setup(r):
        viol.append(r['method'])
print('3. REACHABLE non-setup-only methods routed through a SETUP_ONLY page:', len(viol), viol[:5])
fail += bool(viol)
print('   setup-only methods (note %r): %d' % (SETUP_NOTE, len(so)))
for m in so:
    print('     setup-only:', m)

kept = [e['id'] for e in g['edges'] if e['src'] == 'S_INTRO_SETUP' and e.get('needs_state')]
print('4. gated edges leaving S_INTRO_SETUP (text kept):', len(kept), kept[:3])
fail += not kept

kd = [r for r in reach if r['method'] == 'KeyDerivationTask.onPostExecute']
kd_ok = bool(kd) and not through_setup(kd[0])
print('5. KeyDerivationTask.onPostExecute avoids the intro:', kd_ok,
      '| path:', kd[0]['shortest_path'] if kd else None)
fail += not kd_ok

print('6. verdicts:', dict(collections.Counter(r['verdict'] for r in rows)))
print('   edges total:', len(g['edges']), '| edges with needs_state:', sum(1 for e in g['edges'] if e.get('needs_state')))
print('   REACHABLE methods with a state text on the best route:', sum(1 for r in reach if r['state']))
print('RESULT:', 'FAIL' if fail else 'PASS')
