import csv, json, os, re, collections
# callback names: the same list as graph_def.py _CB_NAMES (read from that file so the two cannot drift apart)
CB_NAMES = set(open('/Users/darshan/Desktop/yang/work/graphs/Markor/graph_def.py').read().split("_CB_NAMES = set('''", 1)[1].split("'''", 1)[0].split())
# Usage: python3 -I scratch/plan.py
# Sorts the UNRESOLVED methods of out/markor_trigger_graph.json (last build) into two lists:
#   scratch/dead_plan.json   node -> [kind, reason, source_ref, confirmed_by]  (candidates for UNREACHABLE)
#   scratch/manual_list.txt  node <TAB> why it is not decided by rule (needs a route in graph_def.py or a hand decision)
# Rules, in order:
#   D1 constructor (<init>) with no incoming edge, class and all its subclasses never created on a reachable path,
#      not named in XML or the manifest                          -> no_trigger_in_app, SOURCE
#   D2 static or private method, no incoming edge, no method reference, no textual use of its name -> no_trigger_in_app, SOURCE
#   D3 instance method, no incoming edge, class tree never created on a reachable path (and no XML name)
#                                                                   -> no_trigger_in_app, SOURCE
#   D4 instance method, no incoming edge, class tree live, plain (no supertype outside the app), name not in text
#                                                                   -> no_trigger_in_app, SOURCE
#   D5 closure: a node with incoming edges where every source is dead -> no_trigger_in_app, INFERRED
#   everything else -> manual (callback overrides of library types with a live class, method references, XML names,
#                      static initializers, nodes with a live but unwired caller)
G = '/Users/darshan/Desktop/yang/work/graphs/Markor/'
ROOT = '/Users/darshan/Desktop/yang/final_java_only/Markor/app/Markor-#v2.16.1/app'
ml = json.load(open(G + 'method_list.json'))
hier = json.load(open(G + 'scratch/hier.json'))
auto = json.load(open(G + 'auto_calls.json'))
g = json.load(open(G + 'out/markor_trigger_graph.json'))
rows = list(csv.DictReader(open(G + 'out/methods.csv')))
textc = json.load(open(G + 'scratch/textcount.json'))


def base(n):
    return n.split('@')[0]


def simple(cls):
    return cls.split('/')[-1]


decl = collections.Counter(m['name'] for m in ml)
mlkey = {}
for m in ml:
    mlkey[(simple(m['class']) + '.' + m['name'], m['desc'])] = m
unres = {}
nomatch = 0
for r in rows:
    if r['verdict'] != 'UNRESOLVED':
        continue
    node = r['method'].split('(')[0]
    m = mlkey.get((node, r['jvm_descriptor']))
    if m is None:
        nomatch += 1
        continue
    unres[r['method']] = m
print('unresolved', len(unres), 'nomatch', nomatch)

# incoming edges (all kinds, full receiver-variant names kept) and reachability (non-REGISTER, from S_ENTRY)
inc = collections.defaultdict(set)
adj = collections.defaultdict(set)
for x in g['edges']:
    s, d = x['src'], x['dst']
    inc[base(d)].add(s)
    if x['kind'] != 'REGISTER':
        adj[s].add(d)
R_full = {'S_ENTRY'}
st = ['S_ENTRY']
while st:
    x = st.pop()
    for y in adj.get(x, ()):
        if y not in R_full:
            R_full.add(y)
            st.append(y)
# the build labels a base method REACHABLE when its own node or any receiver variant is reached (checked: this set
# equals the REACHABLE verdicts, see scratch/check_plan.py); S is that set
S = {n for n in R_full if '@' not in n} | {base(n) for n in R_full if '@' in n}
reach = S
rv_set = {r['method'] for r in rows if r['verdict'] == 'REACHABLE'}
print('reachable (full names)', len(R_full), 'label set', len(S), 'mismatch with REACHABLE verdicts', len((S - {p for p in S if p.startswith('S_')}) ^ rv_set))

# creators: simple class name -> creator nodes (bytecode X.<init> calls)
creators = collections.defaultdict(set)
for c in auto['calls']:
    d = c['dst'].split('(')[0]
    if d.endswith('.<init>'):
        creators[simple(d[:-len('.<init>')])].add(base(c['src']))

# XML and manifest names (tags, handlers, class attributes): identifiers in every app xml file
ROOTX = ROOT
xml_names = set()        # class-like names: element tags and name=/class= attribute values
xml_handlers = set()     # android:onClick-style handler names (on...="method")
files = collections.defaultdict(list)
mref_names = set()
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ('build', '.gradle')]
    for f in fs:
        p = os.path.join(d, f)
        if f.endswith('.xml'):
            xt = open(p, encoding='utf-8', errors='replace').read()
            xml_names |= set(re.findall(r'<([A-Za-z_][\w.$]*)', xt)) | set(re.findall(r'(?:name|class)="([\w.$]+)"', xt))
            xml_handlers |= set(re.findall(r'\bon\w+="([A-Za-z_]\w*)"', xt))
        elif f.endswith(('.java', '.kt')):
            files[f.rsplit('.', 1)[0]].append(p)
            for mm in re.finditer(r'::\s*([A-Za-z_]\w*)', open(p, encoding='utf-8', errors='replace').read()):
                mref_names.add(mm.group(1))
xml_simple = {n.split('.')[-1] for n in xml_names}

SUBS = collections.defaultdict(set)
for k in hier:
    st2 = [k]
    seen = set()
    while st2:
        x = st2.pop()
        h = hier.get(x)
        if not h:
            continue
        for p in ([h['super']] if h['super'] else []) + h['ifaces']:
            if p and p not in seen:
                seen.add(p)
                SUBS[p].add(k)
                st2.append(p)


def ancestors(c):
    out, st3 = set(), [c]
    while st3:
        x = st3.pop()
        h = hier.get(x)
        if not h:
            continue
        for p in ([h['super']] if h['super'] else []) + h['ifaces']:
            if p and p not in out:
                out.add(p)
                st3.append(p)
    return out


def tree_state(cls):
    # 'live' if an object of cls or of an app subclass is created at a reached node; 'xml' if named in XML/manifest;
    # 'dead' otherwise
    members = {cls} | SUBS.get(cls, set())
    state = 'dead'
    for k in members:
        s = simple(k)
        if creators.get(s, set()) & reach:
            return 'live'
        if s.split('$')[-1] in xml_simple or s in xml_simple:
            state = 'xml'
    return state


def text_refs(name):
    return textc.get(name, 0) - decl.get(name, 0)


def decl_ref(cls, name):
    outer = simple(cls).split('$')[0]
    paths = files.get(outer, [])
    if not paths:
        return None
    p = paths[0]
    rel = os.path.relpath(p, ROOT)
    lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
    if name == '<clinit>':
        key = 'static {'
    elif name == '<init>':
        key = simple(cls).split('$')[-1]
    elif name.startswith('lambda$'):
        key = name.split('$')[1]
    else:
        key = name
    pat = re.compile(r'(?<![\w.$])' + re.escape(key) + r'\s*[({]')
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith(('//', '*', '/*', 'return ', 'new ', 'if ', 'for ', 'while ')):
            continue
        mm = pat.search(line)
        if not mm:
            continue
        before = line[:mm.start()].rstrip()
        if before.endswith('.') or before.endswith('=') or before.endswith('->'):
            continue
        if name not in ('<clinit>', '<init>') and not re.search(r'(void|int|boolean|String|Object|[\w>\]])\s*$|^\s*(public|private|protected|static|final|abstract|synchronized)\b|^\s*@', before) and not before.strip().startswith(('public', 'private', 'protected', 'static')):
            continue
        return '%s:%d' % (rel, i)
    return rel


ALL_JAVA = [q for lst in files.values() for q in lst]
dead = {}
manual = {}
for node, m in unres.items():
    cls, name, desc, fl = m['class'], m['name'], m['desc'], m.get('flags', [])
    if inc.get(base(node)):
        continue  # decided by closure below
    ts = tree_state(cls)
    if name == '<clinit>':
        # a static initializer runs only when the class is first used: dead when no other app file names the class
        outer = simple(cls).split('$')[0]
        others = [q for q in ALL_JAVA if q not in files.get(outer, [])]
        used = [q for q in others if re.search(r'\b%s\b' % re.escape(outer), open(q, encoding='utf-8', errors='replace').read())]
        if used:
            manual[node] = 'static initializer; class named in other app files: %s' % ', '.join(os.path.relpath(q, ROOT) for q in used[:2])
        else:
            dead[node] = ['no_trigger_in_app', 'the class %s is named only in its own file (no other app .java/.kt/.xml file uses it), so no code runs its static initializer' % outer, decl_ref(cls, name), 'SOURCE']
    elif name == '<init>':
        xml_ctor = desc == '(Landroid/content/Context;Landroid/util/AttributeSet;)V'
        if ts == 'dead':
            dead[node] = ['no_trigger_in_app', 'class %s is never created on a reachable path (no reached constructor call, no XML or manifest name)' % simple(cls), decl_ref(cls, name), 'SOURCE']
        elif not xml_ctor:
            # no bytecode call builds an object with this signature (call table has no caller). XML and preference inflation
            # use only the (Context, AttributeSet) constructor, which graph_def.py wires in section G.
            dead[node] = ['no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', decl_ref(cls, name), 'SOURCE']
        else:
            manual[node] = 'constructor, class %s state %s, no incoming edge' % (simple(cls), ts)
    elif 'static' in fl or 'private' in fl:
        if name in mref_names or name in xml_handlers:
            manual[node] = 'static/private, method reference or XML handler name'
        else:
            dead[node] = ['no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name %s' % name, decl_ref(cls, name), 'SOURCE']
    else:
        anc = ancestors(cls)
        ext = [a for a in anc if a not in hier and a != 'java/lang/Object']
        if ts == 'dead':
            dead[node] = ['no_trigger_in_app', 'no bytecode caller; no reached code creates an object of %s or of a subclass' % simple(cls), decl_ref(cls, name), 'SOURCE']
        elif ext:
            # a library superclass may call a method of this name. A callback name (graph_def.py _CB_NAMES) would be wired from its
            # creator in section E, so reaching this branch means no creator is reached; any other name is not a known callback.
            libs = ', '.join(sorted(simple(a) for a in ext)[:3])
            if cls.startswith('net/gsantner/opoc/wrapper/GsMenuItemDummy'):
                dead[node] = ['no_trigger_in_app', 'placeholder for library %s; the app text never uses the name %s, so no app code calls it through the placeholder (library source not read)' % (libs, name), decl_ref(cls, name), 'INFERRED']
            elif name in CB_NAMES:
                dead[node] = ['no_trigger_in_app', 'framework callback name %s on a subclass of library %s; no reached creator wires it (library source not read)' % (name, libs), decl_ref(cls, name), 'INFERRED']
            else:
                dead[node] = ['no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name %s; the class extends library %s, which could call a method of this name (library source not read)' % (name, libs), decl_ref(cls, name), 'INFERRED']
        elif name in mref_names or name in xml_handlers:
            manual[node] = 'instance method, method reference or XML handler name'
        else:
            dead[node] = ['no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name %s' % name, decl_ref(cls, name), 'SOURCE']

# D5 greatest fixpoint: the undecided nodes D that cannot be reached from a live node. A node leaves D when one of its
# callers is live (in S), manual, or undecided but already removed from D; what is left in D has only dead or
# undecided-dead callers, so it is unreachable (this also covers call cycles with no entry).
D = {n for n in unres if n not in dead and n not in manual and inc.get(n)}
changed = True
while changed:
    changed = False
    for n in sorted(D):
        for s in inc[n]:
            b_ = base(s)
            if s in R_full or b_ in manual or (b_ in unres and b_ not in dead and b_ not in D):
                D.discard(n)
                changed = True
                break
for n in sorted(D):
    m = unres[n]
    dead[n] = ['no_trigger_in_app', 'no route from the entry points: every caller is unreachable (%s)' % ', '.join(sorted(inc[n])[:3]), decl_ref(m['class'], m['name']), 'INFERRED']
for node in unres:
    if node not in dead and node not in manual:
        manual[node] = 'has incoming edges from live or undecided nodes'
for node in list(dead) + list(manual):
    m_ = unres[node]
    if '/openeditor/' in m_['class']:
        # launchers disabled by configuration: manifest android:enabled=false (AndroidManifest.xml 140-180); enabled only by
        # MarkorContextUtils.setLauncherActivityEnabled when isSpecialFileLaunchersEnabled() (false in the test build)
        dead[node] = ['closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', decl_ref(m_['class'], m_['name']), 'SOURCE']
        manual.pop(node, None)
json.dump(dead, open(G + 'scratch/dead_plan.json', 'w'), indent=0, sort_keys=True)
with open(G + 'scratch/manual_list.txt', 'w') as f:
    for k in sorted(manual):
        f.write('%s\t%s\n' % (k, manual[k]))
print('dead', len(dead), 'manual', len(manual))
print('dead by kind', collections.Counter(v[0] for v in dead.values()))
print('dead by confirmed_by', collections.Counter(v[3] for v in dead.values()))
print('manual by reason', collections.Counter(re.sub(r'\(\d+\)|, class state \w+|, no incoming edge', '', v) for v in manual.values()).most_common(12))

# ---- diagnostics for the manual group
cat = collections.Counter()
for n, v in manual.items():
    if v.startswith('has incoming'):
        for s in inc[n]:
            b_ = base(s)
            cat[('inS' if b_ in S else 'notS', 'manual' if b_ in manual else ('dead' if b_ in dead else ('unres' if b_ in unres else 'other')))] += 1
print('sources of manual-incoming nodes', cat.most_common())
lib = sorted(n for n, v in manual.items() if v.startswith('instance method overriding'))
print('library-override manual, classes', collections.Counter(n.rsplit('.', 1)[0] for n in lib).most_common(12))
print('example library-override', lib[:6])
