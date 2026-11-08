import csv, os, collections
G = 'graphs/LibreTorrent'
PLAN = 'handoff/LIBRETORRENT_BATCH_PLAN.tsv'
labels = {}
with open(f'{G}/out/methods.csv', newline='') as f:
    for r in csv.DictReader(f):
        labels[(r['method'], r['jvm_descriptor'])] = (r['verdict'], r['unreachable_kind'])
with open(PLAN, newline='') as f:
    rd = csv.reader(f, delimiter='\t')
    header = next(rd)
    rows = list(rd)
changed = collections.Counter()
for row in rows:
    if row[1] != 'TODO_UNCLASSIFIED':
        continue
    key = (row[2], row[3])
    if key not in labels:
        changed['missing_in_build'] += 1
        continue
    verdict, kind = labels[key]
    if verdict == 'UNREACHABLE' and kind and kind != 'unclassified':
        row[1] = 'DONE_LABEL'
        row[4] = f'UNREACHABLE {kind}'
        changed['DONE_LABEL'] += 1
    else:
        changed['still_todo'] += 1
print(dict(changed))
tmp = PLAN + '.tmp'
with open(tmp, 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(header)
    w.writerows(rows)
os.replace(tmp, PLAN)
