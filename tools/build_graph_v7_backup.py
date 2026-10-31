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
  PREFER_SETUP_OVER_ENV = False   # True: a method that is reachable with in-app setup but no environment gate is
                                  # REACHABLE_AFTER_SETUP even if another route reaches it without setup through an env gate
`env` marks an edge that needs an environment condition (network, certificates, ...).
NOTES maps a base method name to a free-text note for methods.csv.
USE_AUTO = True adds the call edges from <graph_dir>/auto_calls.json (tools/extract_calls.py) for every
caller/callee pair that no hand-written edge already covers; SUPPRESS = {(src, dst), ...} or {src, ...}
drops auto edges (e.g. calls inside branches that can never run). Lambda creations become REGISTER edges.

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


def class_prefixes(rows):
    """{outer class: 'pkgtail.'} for outer classes whose simple name is shared by another class (e.g. two TagsAdapter)."""
    simple = collections.defaultdict(set)
    for r in rows:
        outer = r['class'].split('$')[0]
        simple[outer.rsplit('/', 1)[-1]].add(outer)
    pre = {}
    for sn, fulls in simple.items():
        if len(fulls) < 2:
            continue
        for k in range(1, 8):
            tails = {f: '.'.join(f.split('/')[-1 - k:-1]) for f in fulls}
            if len(set(tails.values())) == len(fulls):
                break
        for f in fulls:
            pre[f] = tails[f] + '.'
    return pre


def method_names(rows):
    """Base node name per method; overloads get '(params)'; classes that share a simple name get a package prefix."""
    pre = class_prefixes(rows)
    shorts = [pre.get(r['class'].split('$')[0], '') + r['short'] for r in rows]
    count = collections.Counter(shorts)
    names, by_name = [], {}
    for r, sh in zip(rows, shorts):
        n = sh if count[sh] == 1 else '%s(%s)' % (sh, param_names(r['desc']))
        k = 2
        while n in by_name:   # same class, overloads whose parameter simple names coincide
            n = '%s#%d' % (n.split('#')[0], k)
            k += 1
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


def cheapest(out, allow_setup):
    """Like bfs, but each reachable node keeps the path with the fewest environment-gated edges, then the fewest
    earlier-setup (needs_state) edges, then the fewest steps.
    The returned dict is in settlement order (cheapest first), so the first variant found for a method is its best one."""
    import heapq
    best = {'S_ENTRY': (0, 0, 0)}
    via = {'S_ENTRY': None}
    done, prev = set(), {}
    heap, tick = [(0, 0, 0, 0, 'S_ENTRY')], 0
    while heap:
        env, setup, steps, _t, n = heapq.heappop(heap)
        if n in done:
            continue
        done.add(n)
        prev[n] = via[n]
        for x in out.get(n, []):
            if x['kind'] == 'REGISTER' or x['src'] == x['dst'] or x['dst'] in done:
                continue
            if x['needs_state'] and not allow_setup:
                continue
            cost = (env + (1 if x.get('env') else 0), setup + (1 if x['needs_state'] else 0), steps + 1)
            if x['dst'] not in best or cost < best[x['dst']]:
                best[x['dst']] = cost
                via[x['dst']] = x
                tick += 1
                heapq.heappush(heap, (cost[0], cost[1], cost[2], tick, x['dst']))
    return prev


def path_to(n, prev):
    p = []
    while prev.get(n):
        p.append(prev[n])
        n = prev[n]['src']
    return p[::-1]


def menu_label(trigger):
    m = re.search(r'(android\.R\.id\.home)|R\.id\.(\w+)', trigger or '')
    if not m:
        return None
    return 'Up arrow (top-left)' if m.group(1) else re.sub(r'^(action|menu|item)_', '', m.group(2)).replace('_', ' ')


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


def add_auto_edges(gdir, edges, e, suppress):
    auto = json.load(open(os.path.join(gdir, 'auto_calls.json')))
    manual = {(base(x['src']), base(x['dst'])) for x in edges if x['kind'] != 'REGISTER'}
    manual_reg = {(base(x['src']), base(x['dst'])) for x in edges if x['kind'] == 'REGISTER'}
    receiver = set(auto.get('receiver_variants', ()))
    variants = collections.defaultdict(set)  # hand-written context variants (not receiver variants)
    for x in edges:
        for n in (x['src'], x['dst']):
            if '@' in n and not is_screen(n) and n not in receiver:
                variants[base(n)].add(n)
    manual_nodes = {(x['src'], base(x['dst'])) for x in edges if x['kind'] != 'REGISTER'}
    for c in auto['calls']:
        p = (c['src'], c['dst'])
        if p in suppress or c['src'] in suppress or c['dst'] in suppress:
            continue
        if c['src'] in receiver:  # receiver variants: skip only if that exact node already has a hand edge
            if (c['src'], base(c['dst'])) in manual_nodes:
                continue
        elif (c['src'], base(c['dst'])) in manual or (base(c['src']), base(c['dst'])) in manual:
            continue
        trig = 'Direct call' if c['dispatch'] == 'exact' else 'Virtual/interface call that can dispatch to this implementation'
        if c['via']:
            trig += ' (through ' + ', '.join(c['via']) + ')'
        for s in [c['src']] + sorted(variants.get(c['src'], ())):
            e(s, c['dst'], 'CALL', trig, evidence='SRC %s:%s (bytecode)' % (c['file'], c['line']), auto=True)
    for l in auto['lambdas']:
        p = (l['src'], l['dst'])
        if p in manual or p in manual_reg or p in suppress or l['src'] in suppress:
            continue
        e(l['src'], l['dst'], 'REGISTER', 'Creates the lambda / method reference (its body runs when invoked)',
          evidence='SRC %s:%s (bytecode)' % (l['file'], l['line']), auto=True)


def main(argv):
    gdir, prefix = argv[1], argv[2]
    outdir = os.path.join(gdir, 'out')
    os.makedirs(outdir, exist_ok=True)
    rows = json.load(open(os.path.join(gdir, 'method_list.json')))
    methods, by_name = method_names(rows)

    edges = []

    def e(src, dst, kind, trigger, gui=(), guard=None, reads=(), writes=(), note=None,
          needs_state=None, evidence=None, env=None, auto=False):
        x = {'src': src, 'dst': dst, 'kind': kind, 'trigger': trigger, 'gui': list(gui),
             'guard': guard, 'reads': list(reads), 'writes': list(writes), 'note': note,
             'needs_state': needs_state, 'evidence': evidence, 'env': env}
        if auto:
            x['auto'] = True
        edges.append(x)

    auto_path = os.path.join(gdir, 'auto_calls.json')
    auto_data = json.load(open(auto_path)) if os.path.isfile(auto_path) else None

    def impl(cls, name, desc=None):
        """Node that runs when method `name` is invoked on an instance of class `cls` (short name)."""
        tbl = (auto_data or {}).get('impl', {}).get(cls, {}).get(name)
        if not tbl:
            raise KeyError('impl: %s has no method %s' % (cls, name))
        if desc:
            return tbl[desc]
        if len(set(tbl.values())) != 1:
            raise KeyError('impl: %s.%s is overloaded, pass desc: %s' % (cls, name, sorted(tbl)))
        return next(iter(tbl.values()))

    ns = {'e': e, 'SCREENS': {}, 'DEAD': {}, 'FRAMEWORK_ONLY': {}, 'TITLE': '', 'NOTES': {},
          'USE_AUTO': False, 'SUPPRESS': set(), 'AUTO': auto_data, 'impl': impl, 'METHODS': list(methods),
          'GDIR': os.path.abspath(gdir), 'TOOLS': os.path.dirname(os.path.abspath(__file__)),
          'AUTO_DEAD': None, 'COVERAGE': None}
    src_path = os.path.join(gdir, 'graph_def.py')
    exec(compile(open(src_path, encoding='utf-8').read(), src_path, 'exec'), ns)
    screens, dead, fwo, notes = ns['SCREENS'], ns['DEAD'], ns['FRAMEWORK_ONLY'], ns['NOTES']
    if ns['USE_AUTO']:
        add_auto_edges(gdir, edges, e, set(ns['SUPPRESS']))
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

    if ns.get('AUTO_DEAD'):   # drop pages (and their edges) that nothing reaches
        o0 = collections.defaultdict(list)
        for x in edges:
            o0[x['src']].append(x)
        reach = bfs(o0, allow_setup=True)
        gone = {s_ for s_ in screens if s_ != 'S_ENTRY' and not any(base(n) == s_ for n in reach)}
        if gone:
            edges[:] = [x for x in edges if base(x['src']) not in gone and base(x['dst']) not in gone]
            for s_ in gone:
                del screens[s_]
            for i, x in enumerate(edges, 1):
                x['id'] = 'E%03d' % i

    out, inn = collections.defaultdict(list), collections.defaultdict(list)
    for x in edges:
        out[x['src']].append(x)
        inn[base(x['dst'])].append(x)

    prev = bfs(out, allow_setup=False)
    prev_setup = bfs(out, allow_setup=True)
    prev_noenv = bfs(out, allow_setup=True, allow_env=False)
    prefer = bool(ns.get('PREFER_SETUP_OVER_ENV'))
    prev_clean = bfs(out, allow_setup=False, allow_env=False) if prefer else None
    best_first = cheapest(out, allow_setup=False)     # path choice: fewest environment gates, then fewest steps
    best_setup = cheapest(out, allow_setup=True)

    def first_variant(m, pv):
        for n in pv:  # dict keeps BFS discovery order, so the first hit is the shortest
            if base(n) == m:
                return n
        return None

    verdict, info = {}, {}
    auto_dead = set()
    for m in methods:
        if m in dead:
            verdict[m] = 'DEAD'
        elif m in fwo:
            verdict[m] = 'FRAMEWORK_ONLY'
        elif prefer and first_variant(m, prev_clean):
            verdict[m] = 'REACHABLE'
        elif prefer and first_variant(m, prev_noenv):
            verdict[m] = 'REACHABLE_AFTER_SETUP'   # reachable with in-app setup only: better than a route that needs the environment
        elif first_variant(m, prev):
            verdict[m] = 'REACHABLE'
        elif first_variant(m, prev_setup):
            verdict[m] = 'REACHABLE_AFTER_SETUP'
        elif ns.get('AUTO_DEAD'):
            verdict[m] = 'DEAD'
            auto_dead.add(m)
        else:
            verdict[m] = 'UNRESOLVED'
            errors.append('method has no path and no DEAD/FRAMEWORK_ONLY verdict: ' + m)
        if verdict[m] in ('DEAD', 'FRAMEWORK_ONLY') and m not in auto_dead:
            live = [x['id'] for x in inn.get(m, []) if x['kind'] != 'REGISTER']
            if live:
                warnings.append('%s is %s but has incoming edges %s' % (m, verdict[m], live))
        # prefer a path without environment gates; then the shortest
        order = [best_first] if verdict[m] == 'REACHABLE' else [best_setup]
        v, pv = None, None
        if verdict[m].startswith('REACHABLE'):
            for cand in order:
                v = first_variant(m, cand)
                if v:
                    pv = cand
                    break
        p = path_to(v, pv) if v else []
        info[m] = {'path': p, 'env_gated': any(x.get('env') for x in p)}

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
            cov[(r.get('class'), r['short'], r['desc'])] = r

    with open(os.path.join(outdir, 'methods.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['method', 'verdict', 'steps_from_launch', 'gui_steps_on_shortest_path',
                    'shortest_path', 'incoming_edges', 'note', 'jvm_descriptor',
                    'monkey_hit', 'ape_hit'])
        for m in methods:
            p = info[m]['path']
            note = [dead.get(m) or fwo.get(m) or (ns.get('AUTO_DEAD') if m in auto_dead else None) or notes.get(m) or '']
            envs = sorted({x['env'] for x in p if x.get('env')})
            if envs:
                note.append('needs environment: ' + '; '.join(envs))
            setup = sorted({x['needs_state'] for x in p if x.get('needs_state')})
            if setup:
                note.append('needs earlier setup: ' + '; '.join(setup))
            r = by_name[m]
            c = cov.get((r['class'], r['short'], r['desc']), {})
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
    rep.append('auto edges (from bytecode): %d of %d' % (sum(1 for x in edges if x.get('auto')), len(edges)))
    rep.append('evidence: ' + ', '.join('%s %d' % kv for kv in sorted(collections.Counter(x['evidence'].split()[0] for x in edges).items())))
    rep.append('needs_state edges: %d; env edges: %d; env-gated methods: %d' % (
        sum(1 for x in edges if x['needs_state']), sum(1 for x in edges if x.get('env')),
        sum(1 for m in methods if info[m]['env_gated'])))
    if cov:
        hit = lambda m: (lambda c: bool(c.get('monkey') or c.get('ape')))(cov.get((by_name[m]['class'], by_name[m]['short'], by_name[m]['desc']), {}))
        contra = [m for m in methods if verdict[m] in ('DEAD', 'FRAMEWORK_ONLY') and hit(m)]
        unreported = [m for m in methods if (by_name[m]['class'], by_name[m]['short'], by_name[m]['desc']) not in cov]
        reach_not_hit = [m for m in methods if verdict[m].startswith('REACHABLE') and not hit(m) and m not in unreported]
        rep.append('baseline cross-check: %d methods hit by APE or Monkey; %d DEAD/FRAMEWORK_ONLY but hit (contradictions)'
                   % (sum(1 for m in methods if hit(m)), len(contra)))
        for m in contra:
            rep.append('  CONTRADICTION: %s is %s but ran in the baseline' % (m, verdict[m]))
        rep.append('not in the JaCoCo report (filtered trivial methods): %s' % (', '.join(unreported) or 'none'))
        gated_hit = [m for m in methods if verdict[m].startswith('REACHABLE') and hit(m) and info[m]['env_gated']]
        rep.append('hit by APE/Monkey although the best path crosses an environment gate (gate probably refuted): %d' % len(gated_hit))
        for m in gated_hit:
            rep.append('  ENV-GATED BUT HIT: %s' % m)
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
