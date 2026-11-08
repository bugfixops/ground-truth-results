import sys, json, io, contextlib, os, collections, importlib.util

WORK = '/Users/darshan/Desktop/yang/work'
GDIR = 'graphs/AmazeFileManager'
OUT = os.path.join(WORK, GDIR, 'scratch/finish22')
os.makedirs(OUT, exist_ok=True)

spec = importlib.util.spec_from_file_location('build_graph', os.path.join(WORK, 'tools/build_graph.py'))
bg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bg)

calls = []


def tracer(frame, event, arg):
    if event == 'call' and frame.f_code.co_name == 'e' and frame.f_code.co_filename.endswith('build_graph.py'):
        caller = frame.f_back
        if caller is not None and caller.f_code.co_filename.endswith('graph_def.py'):
            calls.append(caller.f_lineno)
    return None


sys.settrace(tracer)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    rc = bg.main(['build_graph.py', GDIR, 'amazefilemanager'])
sys.settrace(None)

d = json.load(open(os.path.join(WORK, GDIR, 'out/amazefilemanager_trigger_graph.json')))
edges = d['edges']
manual = [x for x in edges if not x.get('auto')]
verdict = d['verdict']
print('build rc', rc, 'edges', len(edges), 'manual', len(manual), 'trace calls', len(calls))
assert len(manual) == len(calls), 'trace/edge count mismatch'

lines_of = {}
for x, ln in zip(manual, calls):
    lines_of[x['id']] = ln
gd_lines = open(os.path.join(WORK, GDIR, 'graph_def.py'), encoding='utf-8').read().split('\n')
for i, x in enumerate(manual):
    ln = calls[i]
    ok = (x['src'] in gd_lines[ln - 1] or x['dst'] in gd_lines[ln - 1] or
          any(x['src'] in gd_lines[j] for j in range(ln - 1, min(ln + 3, len(gd_lines)))))
    if not ok:
        print('CHECK line', ln, x['id'], x['src'], '->', x['dst'])

with open(os.path.join(OUT, 'edge_lines.tsv'), 'w', encoding='utf-8') as f:
    f.write('id\tline\tauto\tsrc\tdst\tkind\tsrc_verdict\tdst_verdict\tevidence\n')
    for x in edges:
        ln = lines_of.get(x['id'], '')
        f.write('\t'.join(str(v) for v in (x['id'], ln, int(bool(x.get('auto'))), x['src'], x['dst'], x['kind'],
                                          verdict.get(x['src'].split('@')[0], 'NA'), verdict.get(x['dst'].split('@')[0], 'NA'),
                                          (x.get('evidence') or '').replace('\t', ' ').replace('\n', ' '))) + '\n')

inn = collections.defaultdict(list)
for x in edges:
    inn[x['dst'].split('@')[0]].append(x)
warn = []
for m, v in verdict.items():
    if v != 'UNREACHABLE':
        continue
    live = [x for x in inn.get(m, []) if x['kind'] != 'REGISTER']
    if live:
        warn.append(m)
print('warnings (computed):', len(warn))
with open(os.path.join(OUT, 'warn_table.tsv'), 'w', encoding='utf-8') as f:
    f.write('method\tkind\treason\tref\tedge_id\tedge_line\tauto\tedge_src\tsrc_verdict\tedge_kind\tedge_evidence\n')
    for m in sorted(warn):
        lab = d['labels'].get(m, {})
        u = lab.get('unreachable') or {}
        for x in inn[m]:
            if x['kind'] == 'REGISTER':
                continue
            f.write('\t'.join(str(v) for v in (m, u.get('kind'), (u.get('text') or '').replace('\t', ' '), u.get('ref'),
                                              x['id'], lines_of.get(x['id'], ''), int(bool(x.get('auto'))), x['src'],
                                              verdict.get(x['src'].split('@')[0], 'NA'), x['kind'],
                                              (x.get('evidence') or '').replace('\t', ' '))) + '\n')
print('written', OUT)
