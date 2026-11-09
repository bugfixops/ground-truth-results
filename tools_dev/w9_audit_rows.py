"""W9 (Kiro): label rows of the reachable audit, for graphs/<App>/make_verification.py.

Reads graphs/<App>/scratch/reaudit/audit_result.csv (columns: app, class, order, method, result, source_read, ref, note)
and returns verification.csv rows ['label', method, result, confirmed_by, ref, '', note]:
  result       correct | fixed | wrong | unclear (W9 step 3)
  confirmed_by SOURCE when the checker printed and read the source for the row (source_read = yes); otherwise the
               method's own confirmed_by from the fresh methods.csv, so an audit row never lowers a label's basis
  note         "reachable audit, class <X>: " + the row's note (<X> is the drawn class)
Each drawn method gets at most one row. A method that already has a label row in the app's verification output is
skipped (the existing row stays), so the builder counts every method once.
Loaded with exec() because make_verification.py runs under python3 -I (no script directory on sys.path)."""
import csv
import os

RESULTS = ('correct', 'fixed', 'wrong', 'unclear')


def audit_rows(gdir, existing_label_items=()):
    gdir = str(gdir)
    path = os.path.join(gdir, 'scratch', 'reaudit', 'audit_result.csv')
    if not os.path.exists(path):
        return []
    methods = {}
    mpath = os.path.join(gdir, 'out', 'methods.csv')
    if os.path.exists(mpath):
        methods = {r['method']: r for r in csv.DictReader(open(mpath, encoding='utf-8'))}
    have = set(existing_label_items)
    out, seen = [], set()
    for r in csv.DictReader(open(path, encoding='utf-8')):
        m, res = r['method'], r['result'].strip()
        assert res in RESULTS, ('audit result', m, res)
        assert r['ref'].strip(), ('audit ref', m)
        if m in have or m in seen:
            continue
        seen.add(m)
        if r.get('source_read', '').strip() == 'yes':
            cb = 'SOURCE'
        else:
            cb = (methods.get(m, {}).get('confirmed_by') or 'INFERRED').strip() or 'INFERRED'
            if cb not in ('SOURCE', 'INFERRED'):
                cb = 'INFERRED'
        note = 'reachable audit, class %s: %s' % (r['class'], r['note'].strip())
        out.append(['label', m, res, cb, r['ref'].strip(), '', note])
    return out
