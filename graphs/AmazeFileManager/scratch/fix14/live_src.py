import csv, json, re
BASE = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/'
d = json.load(open(BASE + 'out/amazefilemanager_trigger_graph.json', encoding='utf-8'))
verdict = d['verdict']
by_id = {e['id']: e for e in d['edges'] if 'id' in e}
rows = {r['method']: r for r in csv.DictReader(open(BASE + 'out/methods.csv', encoding='utf-8'))}
warned = {}
for line in open(BASE + 'scratch/build_finish_16.txt', encoding='utf-8'):
    m = re.search(r'WARN (.+?) is UNREACHABLE but has incoming edges \[(.*)\]', line)
    if m:
        warned[m.group(1)] = re.findall(r"'([^']+)'", m.group(2))
for meth, ids in warned.items():
    srcs = [(by_id[i]['src'], verdict.get(by_id[i]['src'], '?'), by_id[i]['kind'], by_id[i].get('evidence') or '') for i in ids if i in by_id]
    if not any(v == 'REACHABLE' for _, v, _, _ in srcs):
        continue
    r = rows.get(meth, {})
    print('##', meth, '|', r.get('unreachable_kind'), '|', (r.get('unreachable_reason') or '')[:150], '|', r.get('source_ref'))
    for s, v, k, ev in srcs[:2]:
        if v == 'REACHABLE':
            print('   <-', s, k, '|', ev[:170])
