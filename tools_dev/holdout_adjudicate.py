"""F3 of review/blind_check/PROTOCOL.md: join the blind adjudicators of the held-out disagreements with blind_key.csv.
Usage, from the repo root:  python3 -I tools_dev/holdout_adjudicate.py
Reads review/rounds/holdout/{blind.csv,blind_key.csv,disagreements.csv,agreement.txt} and
review/rounds/holdout/adjudicators/{A,B,C}.csv (C only for the rows where A and B differ in verdict or class_found).
Writes review/rounds/holdout/adjudication.csv (the columns of review/rounds/1/adjudication.csv) and prints the counts used
in result.txt."""
import collections
import csv
import os

H = 'review/rounds/holdout/'
rows = list(csv.DictReader(open(H + 'blind.csv', encoding='utf-8')))
key = {r['id']: r['A_is'] for r in csv.DictReader(open(H + 'blind_key.csv', encoding='utf-8'))}
rd = {}
for n in 'ABC':
    p = H + 'adjudicators/%s.csv' % n
    rd[n] = {r['id'].strip(): r for r in csv.DictReader(open(p, encoding='utf-8'))} if os.path.exists(p) else {}


def side(v, a_is):
    """map a reader verdict A/B to sample/full label."""
    v = v.strip().lower()
    if v == 'a':
        return a_is
    if v == 'b':
        return 'sample' if a_is == 'full' else 'full'
    return {'neither': 'neither', 'unclear': 'unclear'}.get(v, 'unclear')


def name(s):
    return {'full': 'full label'}.get(s, s)


out = []
cnt = collections.Counter()
per_app = collections.defaultdict(collections.Counter)
pairs = collections.Counter()
dialog = []
for r in rows:
    i = r['id']
    a_is = key[i]
    lab = {'sample': r['label_B'] if a_is == 'full' else r['label_A'], 'full': r['label_A'] if a_is == 'full' else r['label_B']}
    a, b = rd['A'][i], rd['B'][i]
    same = (a['verdict'].strip().lower(), a['class_found'].strip()) == (b['verdict'].strip().lower(), b['class_found'].strip())
    if same:
        win, how = a, '2 adjudicators agree'
    else:
        c = rd['C'].get(i)
        assert c is not None, ('third reader missing', i)
        win, how = c, '2 adjudicators differ; third decided (A: %s %s, B: %s %s)' % (
            side(a['verdict'], a_is), a['class_found'], side(b['verdict'], a_is), b['class_found'])
    s = side(win['verdict'], a_is)
    cnt[s] += 1
    per_app[r['app']][s] += 1
    if s == 'sample':
        pairs['%s | %s' % (win['class_found'].strip(), lab['full'])] += 1
    if 'yes' in (a.get('dialog_dependent', ''), b.get('dialog_dependent', ''), win.get('dialog_dependent', '')):
        dialog.append(i)
    out.append([i, r['app'], r['method'], lab['sample'], lab['full'], name(s), win['class_found'].strip(),
                win.get('dialog_dependent', '').strip(), win.get('confidence', '').strip(), how,
                win.get('route', ''), win.get('gates', ''), win.get('evidence', ''), win.get('reasoning', '')])
with open(H + 'adjudication.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['id', 'app', 'method', 'sample_class', 'full_label_class', 'source_supports', 'class_found', 'dialog_dependent',
                'confidence', 'adjudicators', 'route', 'gates', 'evidence', 'reasoning'])
    w.writerows(out)
print('rows', len(out), dict(cnt))
for a in sorted(per_app):
    print(' ', a, dict(per_app[a]))
print('wrong full labels (source class | full label):', ', '.join('%s %d' % kv for kv in pairs.most_common()))
print('third reader rows:', [o[0] for o in out if o[9].startswith('2 adjudicators differ')])
print('dialog-dependent rows:', dialog)
