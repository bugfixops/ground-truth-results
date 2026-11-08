import csv, json, collections, os
G = 'graphs/AnkiDroid/'
graph = json.load(open(G + 'out/ankidroid_trigger_graph.json'))
verdict = graph['verdict']
nodes = {r['node']: r for r in csv.DictReader(open(G + 'scratch/node_names.tsv'), delimiter='\t')}
unres = [m for m, v in verdict.items() if v == 'UNRESOLVED']
def top(m):
    cls = nodes[m]['class'] if m in nodes else m.split('.')[0]
    return cls.split('$')[0]
def pkg(c):
    return c.rsplit('/', 1)[0]
groups = collections.OrderedDict()
for m in unres:
    t = top(m)
    groups.setdefault(t, []).append(m)
UI = set()
for r in csv.DictReader(open(G + 'scratch/screen_scan.tsv'), delimiter='\t'):
    if r['base_kind'] and not r['base_kind'].startswith('UNRESOLVED'):
        UI.add(r['class'].replace('.', '/'))
PRI = ['IntentHandler', 'AnkiDroidApp', 'DeckPicker', 'StudyOptionsActivity', 'Reviewer', 'CardBrowser', 'NoteEditor',
       'Preferences', 'CardContentProvider', 'SdCardReceiver', 'AnkiDroidWidgetSmall']


def prio(t):
    if t.split('/')[-1] in PRI:
        return (-1, PRI.index(t.split('/')[-1]), t)
    if t in UI:
        return (0, t)
    if t.startswith('com/ichi2/anki/') and t.count('/') <= 3:
        return (1, t)
    if t.startswith('com/ichi2/anki/'):
        return (2, t)
    if t.startswith('com/ichi2/') and not t.startswith('com/ichi2/libanki'):
        return (3, t)
    if t.startswith('com/ichi2/libanki'):
        return (4, t)
    return (5, t)
order = sorted(groups, key=prio)
batches = []
cur, cur_classes = [], []
for t in order:
    ms = groups[t]
    if len(ms) > 40:
        if cur:
            batches.append((cur_classes, cur)); cur, cur_classes = [], []
        for i in range(0, len(ms), 40):
            batches.append(([t + ' (part %d)' % (i // 40 + 1)], ms[i:i + 40]))
        continue
    if len(cur) + len(ms) > 40:
        batches.append((cur_classes, cur)); cur, cur_classes = [], []
    cur = cur + ms
    cur_classes.append(t)
if cur:
    batches.append((cur_classes, cur))
os.makedirs(G + 'scratch/batches', exist_ok=True)
tab = open(G + 'scratch/batches/plan.tsv', 'w')
tab.write('batch\tclasses\tmethods\n')
for i, (cl, ms) in enumerate(batches, 1):
    with open(G + 'scratch/batches/batch_%03d.txt' % i, 'w') as f:
        f.write('\n'.join(ms) + '\n')
    tab.write('%03d\t%s\t%d\n' % (i, ' '.join(c.split('/')[-1] for c in cl), len(ms)))
tab.close()
print('unresolved', len(unres), 'batches', len(batches), 'max', max(len(b[1]) for b in batches))
print('first 12:')
for i, (cl, ms) in enumerate(batches[:12], 1):
    print(i, len(ms), ' '.join(c.split('/')[-1] for c in cl)[:110])
