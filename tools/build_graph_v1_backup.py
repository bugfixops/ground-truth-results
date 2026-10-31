"""Build, validate and export a trigger graph from an app's graph_def.py.

Usage: python3 -I build_graph.py <graph_dir> <file_prefix>

<graph_dir> must contain:
  graph_def.py          edge definitions (see below)
  method_list.json      output of list_methods.py --json (the method universe)
  coverage_baseline.json  output of coverage_methods.py --json (optional cross-check)

graph_def.py is executed with these names predefined:
  e(src, dst, kind, trigger, gui=(), guard=None, reads=(), writes=(), note=None,
    needs_state=None, evidence=None, env=None)      -> appends one edge
  SCREENS = {}  DEAD = {}  FRAMEWORK_ONLY = {}  TITLE = ''  NOTES = {}
`env` marks an edge that needs an environment condition (network, certificates, ...).
NOTES maps a base method name to a free-text note for methods.csv.

Writes into <graph_dir>/out/:
  <prefix>_trigger_graph.json, methods.csv, <prefix>_trigger_graph.html (if the template exists),
  build_report.txt (validation, evidence counts, baseline cross-check).
"""
import collections
import csv
import json
import os
import re
import sys

KINDS = {'ENTRY', 'LIFECYCLE', 'GUI', 'REGISTER', 'CALL', 'INTENT', 'RESULT', 'ASYNC',
         'FRAMEWORK', 'SYSTEM', 'ENTERS'}
EVIDENCE = ('SRC', 'FW-SRC', 'DYN', 'FW-MEMORY', 'INFERRED', 'UNVERIFIED')
JVM = {'I': 'int', 'J': 'long', 'Z': 'boolean', 'F': 'float', 'D': 'double', 'B': 'byte',
       'C': 'char', 'S': 'short', 'V': 'void'}
TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'viewer_template.html')


def base(n):
    return n.split('@')[0]


def is_screen(n):
    return n.startswith('S_')


def param_names(desc):
    """'(Landroid/content/Context;I)Z' -> 'Context,int'"""
    args, i, out = desc[1:desc.index(')')], 0, []
    while i < len(args):
        dims = 0
        while args[i] == '[':
            dims += 1
            i += 1
        if args[i] == 'L':
            j = args.index(';', i)
            name = args[i + 1:j].rsplit('/', 1)[-1].split('$')[-1]
            i = j + 1
        else:
            name = JVM[args[i]]
            i += 1
        out.append(name + '[]' * dims)
    return ','.join(out)


def method_names(rows):
    """Base node name per method; overloads get '(params)'."""
    count = collections.Counter(r['short'] for r in rows)
    names, by_name = [], {}
    for r in rows:
        n = r['short'] if count[r['short']] == 1 else '%s(%s)' % (r['short'], param_names(r['desc']))
        names.append(n)
        by_name[n] = r
    return names, by_name


def bfs(out, allow_setup, allow_env=True):
    prev, q = {'S_ENTRY': None}, ['S_ENTRY']
    for n in q:
        for x in out.get(n, []):
            if x['kind'] == 'REGISTER' or x['src'] == x['dst'] or x['dst'] in prev:
                continue
            if x['needs_state'] and not allow_setup:
                continue
            if x.get('env') and not allow_env:
                continue
            prev[x['dst']] = x
            q.append(x['dst'])
    return prev


def path_to(n, prev):
    p = []
    while prev.get(n):
        p.append(prev[n])
        n = prev[n]['src']
    return p[::-1]


def menu_label(trigger):
    m = re.search(r'(android\.R\.id\.home|action_\w+)', trigger or '')
    if not m:
        return None
    return 'Up arrow (top-left)' if m.group(1) == 'android.R.id.home' else m.group(1).replace('action_', '').replace('_', ' ')


def gui_steps(path):
    steps = []
    for i, x in enumerate(path):
        if not x['gui']:
            continue
        if i + 1 < len(path) and re.search(r'case (android\.)?R\.id\.', path[i + 1]['trigger'] or ''):
            lab = menu_label(path[i + 1]['trigger'])
            if lab:
                steps.append('Tap menu item: ' + lab)
                continue
        steps.append(x['gui'][0])
    return steps


def main(argv):
    gdir, prefix = argv[1], argv[2]
    outdir = os.path.join(gdir, 'out')
    os.makedirs(outdir, exist_ok=True)
    rows = json.load(open(os.path.join(gdir, 'method_list.json')))
    methods, by_name = method_names(rows)

    edges = []

    def e(src, dst, kind, trigger, gui=(), guard=None, reads=(), writes=(), note=None,
          needs_state=None, evidence=None, env=None):
        edges.append({'src': src, 'dst': dst, 'kind': kind, 'trigger': trigger, 'gui': list(gui),
                      'guard': guard, 'reads': list(reads), 'writes': list(writes), 'note': note,
                      'needs_state': needs_state, 'evidence': evidence, 'env': env})

    ns = {'e': e, 'SCREENS': {}, 'DEAD': {}, 'FRAMEWORK_ONLY': {}, 'TITLE': '', 'NOTES': {}}
    src_path = os.path.join(gdir, 'graph_def.py')
    exec(compile(open(src_path, encoding='utf-8').read(), src_path, 'exec'), ns)
    screens, dead, fwo, notes = ns['SCREENS'], ns['DEAD'], ns['FRAMEWORK_ONLY'], ns['NOTES']
    for i, x in enumerate(edges, 1):
        x['id'] = 'E%03d' % i

    errors, warnings = [], []
    known = set(methods) | set(screens)
    for x in edges:
        for end in ('src', 'dst'):
            if base(x[end]) not in known:
                errors.append('%s: unknown %s node %s' % (x['id'], end, x[end]))
        if x['kind'] not in KINDS:
            errors.append('%s: bad kind %s' % (x['id'], x['kind']))
        if x['kind'] == 'GUI' and (not is_screen(x['src']) or is_screen(x['dst'])):
            errors.append('%s: GUI edge must go page -> method' % x['id'])
        if x['kind'] == 'ENTERS' and not is_screen(x['dst']):
            errors.append('%s: ENTERS edge must end on a page' % x['id'])
        if not x['evidence'] or x['evidence'].split()[0] not in EVIDENCE:
            errors.append('%s: missing/invalid evidence label' % x['id'])
    for m in list(dead) + list(fwo):
        if m not in methods:
            errors.append('verdict for unknown method ' + m)

    out, inn = collections.defaultdict(list), collections.defaultdict(list)
    for x in edges:
        out[x['src']].append(x)
        inn[base(x['dst'])].append(x)

    prev = bfs(out, allow_setup=False)
    prev_setup = bfs(out, allow_setup=True)
    prev_noenv = bfs(out, allow_setup=True, allow_env=False)

    def first_variant(m, pv):
        for n in pv:  # dict keeps BFS discovery order, so the first hit is the shortest
            if base(n) == m:
                return n
        return None

    verdict, info = {}, {}
    for m in methods:
        if m in dead:
            verdict[m] = 'DEAD'
        elif m in fwo:
            verdict[m] = 'FRAMEWORK_ONLY'
        elif first_variant(m, prev):
            verdict[m] = 'REACHABLE'
        elif first_variant(m, prev_setup):
            verdict[m] = 'REACHABLE_AFTER_SETUP'
        else:
            verdict[m] = 'UNRESOLVED'
            errors.append('method has no path and no DEAD/FRAMEWORK_ONLY verdict: ' + m)
        if verdict[m] in ('DEAD', 'FRAMEWORK_ONLY'):
            live = [x['id'] for x in inn.get(m, []) if x['kind'] != 'REGISTER']
            if live:
                warnings.append('%s is %s but has incoming edges %s' % (m, verdict[m], live))
        pv = prev if verdict[m] == 'REACHABLE' else prev_setup
        v = first_variant(m, pv) if verdict[m].startswith('REACHABLE') else None
        p = path_to(v, pv) if v else []
        info[m] = {'path': p, 'env_gated': bool(v) and not first_variant(m, prev_noenv)}

    pages = set(screens)
    for s in pages:
        if s not in ('S_ENTRY',) and not any(base(n) == s for n in prev_setup):
            errors.append('page not reachable from S_ENTRY: ' + s)

    graph = {'title': ns['TITLE'], 'screens': screens, 'methods': methods, 'verdict': verdict,
             'dead': dead, 'framework_only': fwo, 'edges': edges}
    jpath = os.path.join(outdir, prefix + '_trigger_graph.json')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=1, ensure_ascii=False)

    cov = {}
    cpath = os.path.join(gdir, 'coverage_baseline.json')
    if os.path.isfile(cpath):
        for r in json.load(open(cpath)):
            cov[(r['short'], r['desc'])] = r

    with open(os.path.join(outdir, 'methods.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['method', 'verdict', 'steps_from_launch', 'gui_steps_on_shortest_path',
                    'shortest_path', 'incoming_edges', 'note', 'jvm_descriptor',
                    'monkey_hit', 'ape_hit'])
        for m in methods:
            p = info[m]['path']
            note = [dead.get(m) or fwo.get(m) or notes.get(m) or '']
            if info[m]['env_gated']:
                envs = sorted({x['env'] for x in p if x.get('env')})
                note.append('needs environment: ' + '; '.join(envs))
            r = by_name[m]
            c = cov.get((r['short'], r['desc']), {})
            w.writerow([m, verdict[m], len(p) if p else '', ' ; '.join(gui_steps(p)),
                        ' > '.join([p[0]['src']] + [x['dst'] for x in p]) if p else '',
                        sum(1 for x in inn.get(m, []) if x['kind'] != 'REGISTER'),
                        ' | '.join(s for s in note if s), r['desc'],
                        int(bool(c.get('monkey'))) if c else '', int(bool(c.get('ape'))) if c else ''])

    if os.path.isfile(TEMPLATE):
        data = json.dumps(graph, ensure_ascii=False).replace('</', '<\\/')
        html = open(TEMPLATE, encoding='utf-8').read().replace('/*DATA*/', data)
        with open(os.path.join(outdir, prefix + '_trigger_graph.html'), 'w', encoding='utf-8') as f:
            f.write(html)

    # report
    rep = []
    vc = collections.Counter(verdict.values())
    rep.append('methods %d, pages %d, edges %d' % (len(methods), len(screens), len(edges)))
    rep.append('verdicts: ' + ', '.join('%s %d' % kv for kv in sorted(vc.items())))
    rep.append('edge kinds: ' + ', '.join('%s %d' % kv for kv in sorted(collections.Counter(x['kind'] for x in edges).items())))
    rep.append('evidence: ' + ', '.join('%s %d' % kv for kv in sorted(collections.Counter(x['evidence'].split()[0] for x in edges).items())))
    rep.append('needs_state edges: %d; env edges: %d; env-gated methods: %d' % (
        sum(1 for x in edges if x['needs_state']), sum(1 for x in edges if x.get('env')),
        sum(1 for m in methods if info[m]['env_gated'])))
    if cov:
        hit = lambda m: (lambda c: bool(c.get('monkey') or c.get('ape')))(cov.get((by_name[m]['short'], by_name[m]['desc']), {}))
        contra = [m for m in methods if verdict[m] in ('DEAD', 'FRAMEWORK_ONLY') and hit(m)]
        unreported = [m for m in methods if (by_name[m]['short'], by_name[m]['desc']) not in cov]
        reach_not_hit = [m for m in methods if verdict[m].startswith('REACHABLE') and not hit(m) and m not in unreported]
        rep.append('baseline cross-check: %d methods hit by APE or Monkey; %d DEAD/FRAMEWORK_ONLY but hit (contradictions)'
                   % (sum(1 for m in methods if hit(m)), len(contra)))
        for m in contra:
            rep.append('  CONTRADICTION: %s is %s but ran in the baseline' % (m, verdict[m]))
        rep.append('not in the JaCoCo report (filtered trivial methods): %s' % (', '.join(unreported) or 'none'))
        rep.append('reachable per graph but never hit by APE/Monkey: %d' % len(reach_not_hit))
        for m in reach_not_hit:
            rep.append('  %s%s' % (m, '  [env-gated]' if info[m]['env_gated'] else ''))
    rep.append('errors: %d' % len(errors))
    rep += ['  ERROR ' + s for s in errors]
    rep.append('warnings: %d' % len(warnings))
    rep += ['  WARN ' + s for s in warnings]
    text = '\n'.join(rep)
    with open(os.path.join(outdir, 'build_report.txt'), 'w', encoding='utf-8') as f:
        f.write(text + '\n')
    print(text)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
