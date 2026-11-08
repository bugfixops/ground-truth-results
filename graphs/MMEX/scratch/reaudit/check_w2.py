# W2 acceptance check for MMEX. Usage: python3 check_w2.py <outdir>
# Verifies, on a fresh build's outputs:
#  1. no edge still carries a cleared (baseline) needs_state text;
#  2. no REACHABLE method's best route contains a cleared text;
#  3. no REACHABLE method's best route passes through the SETUP_ONLY page
#     (S_TUTORIAL) or the tutorial intent edge, unless the method is itself a
#     setup-only method (note 'only during the first-run setup');
#  4. the tutorial gate edge kept its needs_state (SETUP_ONLY reroutes, it
#     does not clear the gate);
#  5. prints verdict / gate totals for the before-after comparison.
import csv
import json
import sys

outdir = sys.argv[1]
g = json.load(open(outdir + '/mmex_trigger_graph.json'))
rows = list(csv.DictReader(open(outdir + '/methods.csv', encoding='utf-8')))
edges = {e['id']: e for e in g['edges']}

CLEARED = [
    'at least one account exists, so the account list shows rows (HomeFragment.java:793), and the row group is expanded (group expansion is saved in settings, HomeFragment.java:719 and 731)',
    'at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is expanded (its saved setting is true, HomeFragment.java:754)',
    'at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is collapsed (its saved setting is false, HomeFragment.java:719)',
    'a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)',
    'the quote provider setting is YahooYql (the default when the setting is unset)',
    'the repeating transaction notifications setting is on (default on, BehaviourSettings.java:42)',
    'sync is enabled and the sync interval is above 0 (SyncSchedulerBroadcastReceiver.java:76, 82)',
]
SETUP_NOTE = 'only during the first-run setup'

fail = 0

still = [e['id'] for e in g['edges'] if e.get('needs_state') in CLEARED]
print('1. edges still carrying a cleared text:', len(still), still[:5])
fail += bool(still)

reach = [r for r in rows if r['verdict'] == 'REACHABLE']
bad_route = []
for r in reach:
    for i in (r['route_edge_ids'] or '').split():
        e = edges.get(i)
        if e and e.get('needs_state') in CLEARED:
            bad_route.append((r['method'], i))
            break
print('2. REACHABLE methods whose best route contains a cleared text:', len(bad_route), bad_route[:5])
fail += bool(bad_route)

viol = []
setup_only_methods = []
for r in reach:
    ids = (r['route_edge_ids'] or '').split()
    nodes = (r['shortest_path'] or '').split(' > ')
    through_setup = ('S_TUTORIAL' in nodes) or any(
        (edges.get(i) or {}).get('src') == 'S_TUTORIAL' or (edges.get(i) or {}).get('dst') == 'S_TUTORIAL'
        for i in ids)
    is_setup_only = SETUP_NOTE in (r['note'] or '')
    if is_setup_only:
        setup_only_methods.append(r['method'])
    if through_setup and not is_setup_only:
        viol.append(r['method'])
print('3. REACHABLE non-setup-only methods routed through S_TUTORIAL:', len(viol), viol[:5])
fail += bool(viol)
print('   setup-only methods (note %r): %d' % (SETUP_NOTE, len(setup_only_methods)))
for m in setup_only_methods[:40]:
    print('     setup-only:', m)

tut = next((e for e in g['edges'] if e['src'] == 'MainActivity.showTutorial' and e['dst'] == 'TutorialActivity.<init>'), None)
print('4. tutorial gate edge (MainActivity.showTutorial -> TutorialActivity.<init>) needs_state kept:', bool(tut and tut.get('needs_state')))
fail += not (tut and tut.get('needs_state'))

from collections import Counter
print('5. verdicts:', dict(Counter(r['verdict'] for r in rows)))
print('   edges total:', len(g['edges']), '| edges with needs_state:', sum(1 for e in g['edges'] if e.get('needs_state')))
print('   REACHABLE methods with a state text on the best route:', sum(1 for r in reach if r['state']))
child = next((e for e in g['edges'] if e['src'] == 'S_HOME' and e['dst'] == 'HomeFragment$6.onChildClick'), None)
print('   T1 edge (S_HOME -> HomeFragment$6.onChildClick) needs_state:', child.get('needs_state'), '| note:', child.get('note'))
print('RESULT:', 'FAIL' if fail else 'PASS')
