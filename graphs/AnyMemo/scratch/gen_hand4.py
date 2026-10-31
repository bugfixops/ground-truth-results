"""Scratch generator for pass-2 chunk 3, hand-written part: ORMLite DAO links, Dagger roots and providers,
the data-binding path, no-caller roots, the Oauth1 island. Writes graphs/AnyMemo/scratch/chunk3_hand.txt.
Line numbers are read from the app source. Run: python3 -I graphs/AnyMemo/scratch/gen_hand4.py
"""
import collections, json, os, re

os.chdir('/Users/darshan/Desktop/yang/work')
APP = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main'
SRC = APP + '/java/org/liberty/android/fantastischmemo'
RES = APP + '/res'

G = json.load(open('graphs/AnyMemo/out/anymemo_trigger_graph.json'))
V = G['verdict']
ORIG = set((e['src'], e['dst']) for e in G['edges'])
EX = set(ORIG)
INC = collections.defaultdict(list)
for e in G['edges']:
    INC[e['dst']].append(e['src'])
out, rep = [], []

ALLJAVA = ''
for dp, dn, fn in os.walk(SRC):
    for f in fn:
        if f.endswith('.java'):
            ALLJAVA += open(os.path.join(dp, f), encoding='utf-8', errors='replace').read() + '\n'


def S(rel):
    return os.path.join(SRC, rel)


def find_java(name):
    hits = []
    for dp, dn, fn in os.walk(SRC):
        if name in fn:
            hits.append(os.path.relpath(os.path.join(dp, name), SRC))
    if len(hits) != 1:
        raise SystemExit('java file %s: %s' % (name, hits))
    return hits[0]


def ln(path, pat):
    for i, l in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        if re.search(pat, l):
            return i
    raise SystemExit('no line %s /%s/' % (path, pat))


def need(k):
    if k not in V:
        raise SystemExit('missing key ' + k)
    return k


def edge(s, d, kind, trig, ev_const, ev_text, cls=None, via=None):
    need(s)
    need(d)
    if (s, d) in EX:
        rep.append('skip (edge exists) %s -> %s' % (s, d))
        return
    EX.add((s, d))
    ev = (ev_const + ' + ' if ev_const else '') + repr(ev_text)
    extra = (', cls=%r' % cls if cls else '') + (', via=%r' % via if via else '')
    out.append('e(%r, %r, %r, %r,\n  evidence=%s%s)' % (s, d, kind, trig, ev, extra))


def sup_pair(a, b):
    need(a)
    need(b)
    if (a, b) in ORIG:
        out.append('sup((%r, %r))' % (a, b))
    else:
        rep.append('no sup needed (no auto edge) %s -> %s' % (a, b))


def unr(key, kind, reason, ref_text, conf):
    need(key)
    if V[key] != 'UNRESOLVED':
        rep.append('kept as %s: %s' % (V[key], key))
        return
    reach = [s for s in INC.get(key, []) if V.get(s) == 'REACHABLE']
    if reach:
        rep.append('CONTRADICTION %s <- %s' % (key, reach))
        return
    callers = sorted(set(INC.get(key, [])))
    if callers:
        rep.append('unreachable callers of %s: %s' % (key, callers[:5]))
    out.append('UNREACHABLE[%r] = (%r, %r,\n    %r, %r)' % (key, kind, reason, ref_text, conf))
    V[key] = 'UNREACHABLE'


def count_calls(name):
    return len(re.findall(r'\b%s\s*\(' % re.escape(name), ALLJAVA))


# ---------------------------------------------------------------- header with the evidence constants
out.append('''# ---- section L part 2, pass 2, chunk 3 (2026-10-26) ----
# ORMLite DAO links, Dagger providers and injected-field edges, the data-binding path, no-caller roots,
# the Oauth1 island. Hand part from scratch/gen_hand4.py; Dagger field edges from scratch/gen_dagger.py.
C3_ORM = ('INFERRED ORMLite (DaoManager, called by OrmLiteSqliteOpenHelper.getDao) creates the DAO class named by '
          '@DatabaseTable(daoClass=...) through one of its constructors; the overload is not known, so both are kept, '
          'and the ORMLite source is not read')
C3_CLINIT = ('INFERRED the JVM initialises a class before its first constructor call (class-initialiser rule; '
             'the JVM specification is not read in this build)')
C3_DATABIND = ('INFERRED the androidx DataBindingUtil and its DataBinderMapper (library source not read) bind the '
               'layout through the generated mapper, which selects the Binding class by layout id')
C3_PROVIDER = ('INFERRED javax.inject.Provider.get() is an interface call made by Dagger-generated code, which is not '
               'in the build output; the bytecode extractor does not follow it, so the target is the object the provider builds')
C3_LIB_PENDING = ('INFERRED the androidx ViewDataBinding pending-bindings pass (library source not read) runs '
                  'executeBindings and hasPendingBindings after the generated invalidateAll marks the binding dirty')
''')

# ---------------------------------------------------------------- ORMLite: DAOs that are reached
DBH_REL = 'common/AnyMemoDBOpenHelper.java'
DBH = S(DBH_REL)
SIGS = ['(ConnectionSource,DatabaseTableConfig)', '(ConnectionSource,Class)']
GETTERS = [('getCardDao', 'Card', 'CardDaoImpl'), ('getCategoryDao', 'Category', 'CategoryDaoImpl'),
           ('getSettingDao', 'Setting', 'SettingDaoImpl'), ('getLearningDataDao', 'LearningData', 'LearningDataDaoImpl')]
for getter, ent, dao in GETTERS:
    gl = ln(DBH, r'getDao\(%s\.class\)' % ent)
    for sig in SIGS:
        c = '%s.<init>%s' % (dao, sig)
        edge('AnyMemoDBOpenHelper.' + getter, c, 'FRAMEWORK',
             'the first %s() call asks ORMLite for the %s DAO, which creates it' % (getter, ent),
             'C3_ORM', '; SRC %s:%d (getDao(%s.class))' % (DBH_REL, gl, ent),
             cls='non_standard', via='ORMLite DaoManager (reflection)')
    if dao + '.<clinit>' in V:
        for sig in SIGS:
            c = '%s.<init>%s' % (dao, sig)
            edge(c, dao + '.<clinit>', 'LIFECYCLE', 'the JVM initialises %s before its constructor runs' % dao,
                 'C3_CLINIT', '; SRC dao/%s.java' % dao)
ABS = 'AbstractHelperDaoImpl'
if ABS + '.<clinit>' in V:
    for sig in SIGS:
        c = '%s.<init>%s' % (ABS, sig)
        if c in V:
            edge(c, ABS + '.<clinit>', 'LIFECYCLE',
                 'the JVM initialises the superclass before a DAO constructor runs the superclass constructor',
                 'C3_CLINIT', '; SRC dao/%s.java' % ABS)

# ---------------------------------------------------------------- ORMLite: DAOs that nothing asks for
for getter, pat, ent, dao in [('getDeckDao', r'\bDeckDao getDeckDao\(', 'Deck', 'DeckDaoImpl'),
                              ('getFilterDao', r'\bFilterDao getFilterDao\(', 'Filter', 'FilterDaoImpl')]:
    assert count_calls(getter) == 1, (getter, count_calls(getter))
    gl = ln(DBH, pat)
    unr('AnyMemoDBOpenHelper.' + getter, 'no_trigger_in_app',
        'no code calls %s() (the declaration at %s:%d is the only mention), so no code asks ORMLite for the %s DAO'
        % (getter, DBH_REL, gl, ent), 'SRC %s:%d' % (DBH_REL, gl), 'SOURCE')
for k in sorted(V):
    m = re.match(r'(Deck|Filter|Stat)DaoImpl\.<init>\(', k)
    if not m:
        continue
    cls = m.group(1) + 'DaoImpl'
    cl = ln(S('dao/%s.java' % cls), r'public %s\(' % cls)
    if m.group(1) == 'Stat':
        assert not re.search(r'\bStat\.class', ALLJAVA), 'Stat.class is used'
        reason = ('no getStatDao() exists and no code calls getDao(Stat.class) or TableUtils for Stat (grep); '
                  'ORMLite would create the DAO only when asked for it')
    else:
        reason = ('the DAO is created only when ORMLite is asked for it by get%sDao(), which no code calls (see '
                  'AnyMemoDBOpenHelper.java)' % m.group(1))
    unr(k, 'no_trigger_in_app', reason, 'SRC dao/%s.java:%d' % (cls, cl), 'SOURCE')
ftk = 'FilterDaoImpl.getActiveFilter'
if ftk in V:
    fl = ln(S('dao/FilterDaoImpl.java'), r'getActiveFilter\(')
    unr(ftk, 'no_trigger_in_app',
        'the only way to reach this DAO method is through getFilterDao(), which no code calls (AnyMemoDBOpenHelper.java)',
        'SRC dao/FilterDaoImpl.java:%d' % fl, 'SOURCE')

# ---------------------------------------------------------------- Dagger: roots, modules, provider holders, providers
AMOD = 'modules/AppModules.java'
AMOD_P = S(AMOD)
ACOMP = S('modules/AppComponents.java')
ACTMOD = S('modules/ActivityModules.java')
unr('DaggerAppComponents.<init>', 'no_trigger_in_app',
    'the generated Dagger root class is used only through its static builder; its constructor is never invoked '
    '(bytecode: no invoke site; the generated source is not in the build output)',
    'SRC modules/AppComponents.java:%d' % ln(ACOMP, r'@Component\('), 'INFERRED')
unr('ActivityModules.<init>', 'no_trigger_in_app',
    'every @Provides method of ActivityModules is static (first one at ActivityModules.java:%d), so Dagger creates no module '
    'instance (bytecode: no invoke site)' % ln(ACTMOD, r'providesMultipleLoaderManager\('),
    'SRC modules/ActivityModules.java:%d' % ln(ACTMOD, r'providesMultipleLoaderManager\('), 'INFERRED')
ap_exec = ln(AMOD_P, r'provideExecutorService\(')
unr('AppModules.<init>', 'no_trigger_in_app',
    'every @Provides method of AppModules is static (from AppModules.java:%d) and the @Binds methods are abstract, so Dagger '
    'creates no module instance (bytecode: no invoke site)' % ap_exec,
    'SRC modules/AppModules.java:%d' % ap_exec, 'INFERRED')
assert not re.search(r'new\s+AppModules\(|new\s+ActivityModules\(', ALLJAVA)
unr('AppModules.provideExecutorService', 'no_trigger_in_app',
    'no @Inject field or call asks for an ExecutorService in the app (grep); AnyMemoExecutor creates its own executor '
    '(utils/AnyMemoExecutor.java:34)', 'SRC modules/AppModules.java:%d' % ap_exec, 'SOURCE')
for k in sorted(V):
    m = re.match(r'(AppModules_\w+Factory)\$InstanceHolder\.(<init>|<clinit>)$', k)
    if not m:
        continue
    factory, which = m.group(1), m.group(2)
    stem = factory[len('AppModules_'):-len('Factory')]
    meth = stem[0].lower() + stem[1:]
    hl = ln(AMOD_P, r'\b%s\(' % meth)
    if which == '<init>':
        unr(k, 'no_trigger_in_app',
            'javac default constructor of the Dagger holder of %s (a class with one static INSTANCE field); nothing creates '
            'the holder (bytecode: no invoke site)' % meth, 'SRC %s:%d' % (AMOD, hl), 'INFERRED')
    else:
        unr(k, 'no_trigger_in_app',
            'the holder of %s is initialised only when %s is called, and no code path calls it (see AppModules.provideExecutorService)'
            % (meth, meth), 'SRC %s:%d' % (AMOD, hl), 'INFERRED')

am_line = ln(S('common/AMApplication.java'), r'activityComponentsBuilder\.get\(\)')
edge('AMApplication.activityComponents', 'DaggerAppComponents$AppComponentsImpl$1.get', 'FRAMEWORK',
     'the ActivityComponents builder is obtained from the Dagger provider when a builder is needed',
     'C3_PROVIDER', '; SRC common/AMApplication.java:%d (activityComponentsBuilder.get())' % am_line,
     cls='non_standard', via='Dagger provider (javax.inject.Provider.get)')
edge('DaggerAppComponents$ActivityComponentsImpl.fragmentsComponentsBuilder',
     'DaggerAppComponents$ActivityComponentsImpl$1.get', 'FRAMEWORK',
     'the component returns its fragment builder through the Dagger provider',
     'C3_PROVIDER', '; generated class, no source line in the build output',
     cls='non_standard', via='Dagger provider (javax.inject.Provider.get)')

# ---------------------------------------------------------------- CardEditor, loaders, no-caller injectors
CE_REL = 'ui/CardEditor.java'
ce_on = ln(S(CE_REL), r'public void onCreate')
unr('DaggerAppComponents$ActivityComponentsImpl.inject(CardEditor)', 'no_trigger_in_app',
    'CardEditor.onCreate never calls the component injector (no inject call in ui/CardEditor.java), so the member injector '
    'for CardEditor has no caller', 'SRC %s:%d' % (CE_REL, ce_on), 'SOURCE')
if 'CardEditor.<clinit>' in V:
    edge('CardEditor.<init>', 'CardEditor.<clinit>', 'LIFECYCLE',
         'the JVM initialises CardEditor before its first constructor runs', 'C3_CLINIT',
         '; SRC %s:%d (class declaration)' % (CE_REL, ln(S(CE_REL), r'class CardEditor')))
for key, rel, cls_pat, comp_pat in [
        ('DaggerAppComponents$AppComponentsImpl.inject(LearnQueueManagerLoader)', 'ui/StudyActivity.java',
         r'class LearnQueueManagerLoader\b', r'inject\(StudyActivity\.LearnQueueManagerLoader'),
        ('DaggerAppComponents$AppComponentsImpl.inject(QuizQueueManagerLoader)', 'ui/QuizActivity.java',
         r'class QuizQueueManagerLoader\b', r'inject\(QuizActivity\.QuizQueueManagerLoader')]:
    cl = ln(S(rel), cls_pat)
    cmp_line = ln(ACOMP, comp_pat)
    unr(key, 'no_trigger_in_app',
        'no code calls this component injector (no call site of inject with this loader; grep). The loader is created by '
        'the LoaderManager; the component declares the injector at modules/AppComponents.java:%d' % cmp_line,
        'SRC %s:%d' % (rel, cl), 'SOURCE')

# ---------------------------------------------------------------- Oauth1 island (never started)
ISLAND = {'OauthAccountActivity': find_java('OauthAccountActivity.java'),
          'OauthAccessCodeRetrievalFragment': find_java('OauthAccessCodeRetrievalFragment.java')}
for k in sorted(V):
    if V[k] != 'UNRESOLVED':
        continue
    base = k.split('.')[0]
    outer = [c for c in ISLAND if base == c or base.startswith(c + '$')]
    if not outer:
        continue
    c = outer[0]
    cl = ln(S(ISLAND[c]), r'class %s\b' % c)
    unr(k, 'no_trigger_in_app',
        'Oauth1 island: %s has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment '
        'is referenced only from OauthAccountActivity, which nothing starts)' % c,
        'SRC %s:%d' % (ISLAND[c], cl), 'SOURCE')

# ---------------------------------------------------------------- AnyMemoDBOpenHelperManager (static use only)
MGR = find_java('AnyMemoDBOpenHelperManager.java')
if not re.search(r'new\s+AnyMemoDBOpenHelperManager\b', ALLJAVA):
    unr('AnyMemoDBOpenHelperManager.<init>', 'no_trigger_in_app',
        'every use of AnyMemoDBOpenHelperManager is a static call; the app never creates an instance (grep: no '
        '"new AnyMemoDBOpenHelperManager")', 'SRC %s:%d' % (MGR, ln(S(MGR), r'class AnyMemoDBOpenHelperManager')), 'SOURCE')

# ---------------------------------------------------------------- data binding: the three layouts
GETDB = 'fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)'
GETDB_ARR = 'fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)'
LIB_MAP = 'databinding.DataBinderMapperImpl.<init>'
BINDINGS = [
    ('AnyMemo.onCreate', 'ui/AnyMemo.java', 'main_tabs', 'MainTabsBindingImpl'),
    ('DropboxListActivity.onCreate', 'downloader/dropbox/DropboxListActivity.java', 'dropbox_list_activity',
     'DropboxListActivityBindingImpl'),
    ('UploadDropboxActivity.onCreate', 'downloader/dropbox/UploadDropboxActivity.java', 'upload_dropbox_screen',
     'UploadDropboxScreenBindingImpl'),
]
for k in (GETDB, GETDB_ARR, LIB_MAP):
    need(k)
layout_line = {}
for onc, rel, layout, impl in BINDINGS:
    need(onc)
    sc = ln(S(rel), r'R\.layout\.%s\b' % layout)
    lay_path = os.path.join(RES, 'layout', layout + '.xml')
    lay = ln(lay_path, r'<layout')
    layout_line[layout] = lay
    txt = open(lay_path, encoding='utf-8', errors='replace').read()
    assert '<merge' not in txt and '<include' not in txt and '<variable' not in txt, layout
    ev_text = '; SRC %s:%d (R.layout.%s); SRC res/layout/%s.xml:%d (layout root)' % (rel, sc, layout, layout, lay)
    edge(onc, LIB_MAP, 'FRAMEWORK', 'setContentView with the data-binding layout %s asks the library for the generated mapper'
         % layout, 'C3_DATABIND', ev_text, cls='non_standard', via='androidx DataBindingUtil loads the generated mapper by name')
    edge(onc, GETDB, 'FRAMEWORK', 'the library asks the generated mapper for the Binding class of R.layout.%s' % layout,
         'C3_DATABIND', ev_text, cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
    ctor = impl + '.<init>(DataBindingComponent,View)'
    edge(onc, ctor, 'FRAMEWORK', 'the layout %s is bound to its generated Binding class (the switch in getDataBinder selects '
         'this class for this layout id)' % layout, 'C3_DATABIND', ev_text, cls='non_standard',
         via='androidx DataBindingUtil -> generated getDataBinder')
    # the automatic edges from getDataBinder reach every Binding class; each one is cut and the layout keeps its own edge
    sup_pair(GETDB, ctor)
    sup_pair(GETDB, impl + '.<clinit>')
    if impl + '.<clinit>' in V:
        edge(ctor, impl + '.<clinit>', 'LIFECYCLE', 'the JVM initialises %s when its first instance is created' % impl,
             'C3_CLINIT', '; SRC res/layout/%s.xml:%d (generated Binding class of the layout)' % (layout, lay))
    inv = impl + '.invalidateAll'
    if inv in V and impl + '.executeBindings' in V:
        edge(inv, impl + '.executeBindings', 'FRAMEWORK',
             'invalidateAll marks the binding dirty; the library runs executeBindings in its pending pass',
             'C3_LIB_PENDING', '; the generated constructor calls invalidateAll (bytecode edge of %s.<init>)' % impl,
             cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
    if inv in V and impl + '.hasPendingBindings' in V:
        edge(inv, impl + '.hasPendingBindings', 'FRAMEWORK',
             'the library checks hasPendingBindings in the same pending pass', 'C3_LIB_PENDING',
             '; the generated constructor calls invalidateAll (bytecode edge of %s.<init>)' % impl,
             cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
    if impl + '.setVariable' in V:
        assert not re.search(r'\bsetVariable\s*\(', ALLJAVA), 'setVariable is called in the app'
        unr(impl + '.setVariable', 'no_trigger_in_app',
            'the app never calls setVariable on this binding (grep: no call); res/layout/%s.xml declares no <variable>'
            % layout, 'SRC res/layout/%s.xml:%d' % (layout, lay), 'SOURCE')
    if impl + '.onFieldChange' in V:
        unr(impl + '.onFieldChange', 'framework_never_calls',
            'the library calls onFieldChange only when an observable field or a <variable> changes; res/layout/%s.xml declares '
            'no <variable> (library source not read)' % layout, 'SRC res/layout/%s.xml:%d' % (layout, lay), 'INFERRED')

unr(GETDB_ARR, 'framework_never_calls',
    'the library calls the View[] variant only to bind the children of a <merge> root; the three layouts have a single '
    '<layout> root and no <merge> or <include> (res/layout/*.xml, grep)',
    'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')
unr('fantastischmemo.DataBinderMapperImpl.collectDependencies', 'framework_never_calls',
    'the library calls collectDependencies only to load the mappers of other modules; AnyMemo has no feature modules '
    '(library source not read)', 'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')
unr('fantastischmemo.DataBinderMapperImpl.convertBrIdToString', 'framework_never_calls',
    'the library calls convertBrIdToString only to name a <variable> in an error message; the layouts declare no <variable> '
    '(library source not read)', 'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')
for k in sorted(V):
    if k.startswith('fantastischmemo.DataBinderMapperImpl.getLayoutId') and V[k] == 'UNRESOLVED':
        unr(k, 'framework_never_calls',
            'the library calls getLayoutId only while it binds the children of an <include> or <merge> layout (library source '
            'not read); the three layouts have neither (res/layout/*.xml)',
            'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')
for k in sorted(V):
    m = re.match(r'fantastischmemo\.DataBinderMapperImpl\$Inner(\w+)\.(<clinit>|<init>)$', k)
    if not m:
        continue
    if m.group(2) == '<clinit>':
        unr(k, 'framework_never_calls',
            'the static lookup table of %s is initialised only by convertBrIdToString or getLayoutId, which no caller reaches '
            '(library source not read)' % m.group(1), 'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')
    else:
        unr(k, 'no_trigger_in_app',
            'javac default constructor of a static lookup holder; nothing creates it (bytecode: no invoke site)',
            'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')
for k in sorted(V):
    if re.match(r'(\w+\.)?BR\.<init>$', k):
        unr(k, 'no_trigger_in_app',
            'the BR constants class is generated from the layout variables; nothing creates it (bytecode: no invoke site) and the '
            'three layouts declare no <variable>', 'SRC res/layout/main_tabs.xml:%d' % layout_line['main_tabs'], 'INFERRED')

# ---------------------------------------------------------------- write
with open('graphs/AnyMemo/scratch/chunk3_hand.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')
print('statements written:', len(out))
print('verdict counts before writing:', collections.Counter(G['verdict'].values()))
for r in rep:
    print(r)
