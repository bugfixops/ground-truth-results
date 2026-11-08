import collections
import json
import os
import sys

sys.path.insert(0, 'tools')
import build_graph as bg

GDIR = 'graphs/MMEX'
LIMIT = 40

rows = json.load(open(os.path.join(GDIR, 'method_list.json')))
names, by_name = bg.method_names(rows)

groups = collections.OrderedDict()
for n in names:
    outer = by_name[n]['class'].split('$')[0]
    groups.setdefault(outer, []).append(n)

batches = []
cur, cur_cls = [], []
for outer, ms in groups.items():
    if len(ms) > LIMIT:
        if cur:
            batches.append((cur_cls, cur))
            cur, cur_cls = [], []
        for i in range(0, len(ms), LIMIT):
            part = ms[i:i + LIMIT]
            batches.append(([outer + ' (methods %d-%d of %d)' % (i + 1, i + len(part), len(ms))], part))
        continue
    if len(cur) + len(ms) > LIMIT:
        batches.append((cur_cls, cur))
        cur, cur_cls = [], []
    cur = cur + ms
    cur_cls.append(outer)
if cur:
    batches.append((cur_cls, cur))

os.makedirs(os.path.join(GDIR, 'scratch', 'batches'), exist_ok=True)
table = ['| batch | classes | methods | helper | status |', '|---|---|---|---|---|']
for k, (cls, ms) in enumerate(batches, 1):
    path = os.path.join(GDIR, 'scratch', 'batches', 'batch_%03d.txt' % k)
    with open(path, 'w') as f:
        f.write('# batch %03d: %d methods, %d class groups\n' % (k, len(ms), len(cls)))
        for c in cls:
            f.write('# class: %s\n' % c)
        for m in ms:
            f.write(m + '\n')
    short = ', '.join(c.split('/')[-1] for c in cls)
    if len(short) > 90:
        short = short[:87] + '...'
    table.append('| %03d | %s | %d | - | not started |' % (k, short, len(ms)))

assert sum(len(ms) for _, ms in batches) == len(names) == len(set(names))
assert all(len(ms) <= LIMIT for _, ms in batches)
print('methods', len(names), 'batches', len(batches), 'max', max(len(ms) for _, ms in batches))
with open(os.path.join(GDIR, 'scratch', 'batch_table.md'), 'w') as f:
    f.write('\n'.join(table) + '\n')
