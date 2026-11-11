"""Step 2b (Kiro, 2026-11-10): the label row of a sampled method whose route row is WRONG used to copy the route's
verdict, so it read 'wrong' while its note said 'REACHABLE confirmed'. Each such method was re-read from the source
(graphs/<App>/scratch/reaudit/reconciled_routes.txt, graphs/reconciled_routes_2b.csv): the label row now says whether
the method's verdict and class hold. A class that was wrong was fixed in the graph (round 3b step 2b judgments in
r3_judged.csv), so its label row is 'correct' after the fix and says what it was.
Exec'd from a make_verification.py; label_2b(app, method, result, note) returns the reconciled (result, note)."""
import csv as _c2b

_R2B = {}
for _r in _c2b.DictReader(open('graphs/reconciled_routes_2b.csv', encoding='utf-8')):
    _R2B[(_r['app'], _r['method'])] = _r


def label_2b(app, method, result, note):
    r = _R2B.get((app, method))
    if r is None:
        return result, note
    if r['label_result'] == 'correct':
        return 'correct', note + ' Step 2b: re-read from the source; the drawn route is not one execution (path row WRONG), ' \
                                 'but the method is reachable on a real route and its class (%s) holds: %s' % (r['class_source'], r['note'])
    return 'correct', note + ' Step 2b: re-read from the source; the class was %s and the source supports %s; fixed in the graph ' \
                             '(round 3b step 2b judgment): %s' % (r['class_graph'], r['class_source'], r['note'])
