# Writes graphs/Markor/verification.csv (schema 2): path rows for the 30-route sample, label rows for every
# UNREACHABLE method and every reachable sample method, edge rows for the corrected edges and the framework
# citations, and the chain-claim check. Every claim is asserted against the built graph before it is written.
# Route text in each path note is generated from methods.csv and the edge kinds, so it cannot drift from the graph.
# Run from the repo root:  python3 -I graphs/Markor/make_verification.py
# All paths below are repo-relative (resolved from the cwd or from this file's location);
# no absolute session paths, no missing-folder reads. Seed data for the pre-ref-fix citations
# lives in graphs/Markor/scratch/methods_before_refs.json (extracted once from the current
# verification.csv FIXED notes, same pattern as the T1 seed rows).
import collections, csv, json, os, re, sys

def _find_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.getcwd(), os.path.dirname(os.path.dirname(here))):
        if os.path.isdir(os.path.join(cand, 'tools')) and os.path.isdir(os.path.join(cand, 'graphs')):
            return cand
    raise SystemExit('cannot find repo root (need tools/ and graphs/ under the cwd or above graphs/Markor/)')


ROOT = _find_root()
G = os.path.join(ROOT, 'graphs', 'Markor') + os.sep
SCR = os.path.join(G, 'scratch') + os.sep
APP = os.path.join(ROOT, 'final_java_only', 'Markor', 'app', 'Markor-#v2.16.1', 'app') + os.sep
FW = os.path.join(ROOT, 'fw_src', 'android-8.1.0_r1') + os.sep
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import build_graph as b  # has a __main__ guard, so importing runs nothing

g = json.load(open(G + 'out/markor_trigger_graph.json', encoding='utf-8'))
E = {x['id']: x for x in g['edges']}
LAB = g['labels']
rows = {r['method']: r for r in csv.DictReader(open(G + 'out/methods.csv', encoding='utf-8'))}
oldrows = {m: {'source_ref': ref} for m, ref in json.load(open(SCR + 'methods_before_refs.json', encoding='utf-8')).items()}
# the sample is the final verify_sample draw (seed 20261025, passed explicitly), read live from the tool; no saved copy is used
import subprocess
_draw = subprocess.run(['python3', '-I', 'tools/verify_sample.py', 'Markor', '30', '20261025'], cwd=ROOT, capture_output=True, text=True, check=True).stdout
assert _draw.splitlines()[0].startswith('# Markor: 30 of 2450 reachable methods'), _draw.splitlines()[0]  # 2450: 2446 + the four widget service framework nodes (round 7)
SAMPLE = [mm.group(1).strip() for mm in (re.search(r'new edges\s+\d+\s+(.*)$', l) for l in _draw.splitlines()) if mm]
UNRE = {m for m, r in rows.items() if r['verdict'] == 'UNREACHABLE'}
REA = {m for m, r in rows.items() if r['verdict'] == 'REACHABLE'}
assert len(UNRE) == 414 and len(REA) == 2450, (len(UNRE), len(REA))
assert UNRE == {m for m, v in LAB.items() if v.get('unreachable')}
assert len(SAMPLE) == 30 and len(set(SAMPLE)) == 30 and set(SAMPLE) <= REA, SAMPLE


# ---------- helpers: every claim is an assertion on the graph
def between(src, dst):
    return [x for x in g['edges'] if x['src'] == src and x['dst'] == dst]


def has(src, dst, **kw):
    r = [x for x in between(src, dst) if all(v in str(x.get(k) or '') for k, v in kw.items())]
    assert r, ('missing edge', src, dst, kw)
    return r[0]


def absent(src, dst):
    assert not between(src, dst), ('edge present, should be absent', src, dst)


def node_exists(name):
    assert any(x['src'] == name or x['dst'] == name for x in g['edges']), ('no such node', name)


def cb(e):
    return 'SOURCE' if b.edge_sourced(e) else 'INFERRED'


def uref(m):
    # the built JSON keeps an unreachable label's ref and confirmed_by at the top level (kind and text are inside 'unreachable')
    l = LAB[m]
    v = l['source_ref'] if l.get('source_ref') else l['unreachable'].get('ref')
    assert v, m
    return v


def ucb(m):
    l = LAB[m]
    v = l['confirmed_by'] if l.get('confirmed_by') else l['unreachable'].get('confirmed_by')
    assert v in ('SOURCE', 'INFERRED'), (m, v)
    return v


def evref(e):
    return (e.get('evidence') or '')[:160]


def route_ids(m):
    return rows[m]['route_edge_ids'].split()


def chain_ok(m):
    nodes = rows[m]['shortest_path'].split(' > ')
    ids = route_ids(m)
    assert len(ids) == int(rows[m]['steps_from_launch']), (m, len(ids), rows[m]['steps_from_launch'])
    assert len(nodes) == len(ids) + 1, (m, len(nodes), len(ids))
    for i, a, c in zip(ids, nodes, nodes[1:]):
        assert E[i]['src'] == a and E[i]['dst'] == c, (m, i, E[i]['src'], E[i]['dst'], a, c)


def on(m, src, dst):
    assert any(E[i]['src'] == src and E[i]['dst'] == dst for i in route_ids(m)), (m, 'not on route', src, dst)


def route_text(m):
    nodes = rows[m]['shortest_path'].split(' > ')
    out = [nodes[0]]
    for i, n in zip(route_ids(m), nodes[1:]):
        e = E[i]
        tag = e['kind']
        if e.get('env_kinds'):
            tag += ' ENV'
        if e.get('needs_state'):
            tag += ' STATE'
        out.append('-[%s]-> %s' % (tag, n))
    return ' '.join(out)


def sourced_all(m):
    return all(b.edge_sourced(E[i]) for i in route_ids(m))


# ---------- path rows (the 30-route sample): result, hand-written part of the note, and checks
P = {}
COLD = ('Cold start (re-checked this pass): S_ENTRY -> ApplicationObject.<init> -> ApplicationObject.onCreate runs before the '
        'first activity or entry point of this route.')
NB_READING = ('Notebook reading (judgement J_NOTEBOOK): the notebook tab is the '
              'default startup tab (AppSettings.java:781), so after the cold start it is the visible page; this route reaches it from '
              'MainActivity.onCreate without an onResume step.')


def p(m, res, text, checks=()):
    assert m in SAMPLE, m
    chain_ok(m)
    for c in checks:
        if c[0] == 'on':
            on(m, c[1], c[2])
        elif c[0] == 'has':
            has(c[1], c[2], **(c[3] if len(c) > 3 else {}))
        elif c[0] == 'absent':
            absent(c[1], c[2])
        elif c[0] == 'node':
            node_exists(c[1])
        elif c[0] == 'onenv':
            # a route edge whose environment text contains c[3]
            assert any(E[i]['src'] == c[1] and E[i]['dst'] == c[2] and c[3] in str(E[i].get('env') or '') for i in route_ids(m)), (m, 'no such env edge on route', c)
        elif c[0] == 'stated':
            # every edge between two nodes carries a state gate containing c[3]
            r = between(c[1], c[2])
            assert r and all(c[3] in str(x.get('needs_state') or '') for x in r), (c, [x['id'] for x in r])
        elif c[0] == 'guardon':
            # the built edge from c[1] to c[2] carries a guard containing c[3], and that edge is on this route
            r = [x for x in between(c[1], c[2]) if c[3] in str(x.get('guard') or '')]
            assert r, ('guard missing on edge', c)
            assert any(x['id'] in route_ids(m) for x in r), ('guarded edge not on route', m, c)
        elif c[0] == 'into_only':
            # the only edges into c[1] come from c[2]
            srcs = {x['src'] for x in g['edges'] if x['dst'] == c[1]}
            assert srcs == {c[2]}, (c, srcs)
        else:
            raise ValueError(c[0])
    note = '%s %s Route (%s steps): %s' % (text, COLD, rows[m]['steps_from_launch'], route_text(m))
    P[m] = {'res': res, 'note': note, 'cb': 'SOURCE' if sourced_all(m) else 'INFERRED'}


CF = 'MainActivity$SectionsPagerAdapter.createFragment'
VPS = 'MainActivity.onViewPagerPageSelected'
# cold start: MainActivity is never resumed or paused without its onCreate first (the removed shortcut edges)
absent('MainActivity.<init>', 'MainActivity.onResume')
absent('MainActivity.<init>', 'MainActivity.onPostResume')
absent('MainActivity.onCreate', 'MainActivity.onPause')
absent('MainActivity.onResume', 'MainActivity.onPause')
# the activity constructor is not a shortcut to the first-visible hook either (it is posted from onPostResume)
absent('StoragePermissionActivity.<init>', 'StoragePermissionActivity.onActivityFirstTimeVisible')

p('FlexmarkKatexExtension$KatexInlineMath.getText', 'fixed',
  'FIXED (menu order, fix 6). The route reaches the notebook page through the cold start (MainActivity.onCreate, onResume, onPostResume, which ENTERS S_NOTEBOOK, MainActivity.java:105-106), '
  'then the notebook toolbar menu item for copy to clipboard (S_NOTEBOOK -> GsFileBrowserFragment.onOptionsItemSelected, case R.id.action_fs_copy_to_clipboard, GsFileBrowserFragment.java:472-475). '
  'The menu is reached after the resumed step; the route no longer uses the old createFragment -> onCreateOptionsMenu edge. The copy action needs a selected file (areItemsSelected, GsFileBrowserFragment.java:473): '
  'no graph edge carries that condition, so the route assumes a selection (the same assumption as the format-menu routes, judgement).',
  [('has', 'S_NOTEBOOK', 'GsFileBrowserFragment.onOptionsItemSelected', {'kind': 'GUI'}),
   ('on', 'GsFileBrowserFragment.onOptionsItemSelected', 'FormatRegistry.<clinit>'),
   ('on', 'FormatRegistry.<clinit>', 'MarkdownTextConverter.<clinit>'),
   ('on', 'FlexmarkKatexExtension$FlexmarkKatexExtensionInternal$KatexNodeRenderer.render(KatexInlineMath,NodeRendererContext,HtmlWriter)', 'FlexmarkKatexExtension$KatexInlineMath.getText'),
   ('absent', CF, 'GsFileBrowserFragment.onCreateOptionsMenu')])

p('GsPreferenceFragmentBase.tintPrefIconsRecursive', 'fixed',
  'FIXED (E1 residual). The More page framework edge now runs only on the More variant (MainActivity.onViewPagerPageSelected@MORE), which the More tab tap '
  'reaches from the notebook page (GUI edge from S_NOTEBOOK). The base edge MainActivity.onViewPagerPageSelected > MoreFragment.onViewCreated is absent (checked), '
  'so a page change that does not show the More tab no longer reaches it.',
  [('on', 'S_NOTEBOOK', 'MainActivity.onViewPagerPageSelected@MORE'),
   ('on', 'MainActivity.onViewPagerPageSelected@MORE', 'MoreFragment.onViewCreated'),
   ('on', 'MoreFragment.onViewCreated', 'MoreInfoFragment.newInstance'),
   ('absent', 'MainActivity.onViewPagerPageSelected', 'MoreFragment.onViewCreated')])

p('FileSearchEngine.isEncryptedFile', 'fixed',
  'FIXED (fix 1 and fix 3, this pass). The route enters the notebook from the first-visible resumed step: MainActivity.onPostResume ENTERS S_NOTEBOOK (MainActivity.java:105-106). '
  'The notebook is the default startup tab (AppSettings.java:781), so this is the page shown after the cold start. The toolbar tap on that page is now a GUI edge from S_NOTEBOOK; '
  'the old FRAMEWORK edge GsActivityBase.onResume -> GsActivityBase.onToolbarClick is removed (its registration is in _REG_SKIP). The toolbar listener is registered only when the toolbar exists '
  '(GsActivityBase.java:94-98), so that condition (toolbar != null) is on the GUI edge. The base handler (GsActivityBase.java:116-124) passes the tap to the first visible, resumed GsFragmentBase, '
  'and the receiver is the notebook fragment (guard on onToolbarClick > onToolbarClicked). The route assumes the notebook page is on screen when the toolbar is tapped (judgement, as the format-menu routes assume a format pick).',
  [('has', 'MainActivity.<init>', 'MainActivity.onCreate', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onCreate', 'MainActivity.onResume', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onResume', 'MainActivity.onPostResume', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onPostResume', 'S_NOTEBOOK', {'kind': 'ENTERS'}),
   ('has', 'S_NOTEBOOK', 'GsActivityBase.onToolbarClick', {'kind': 'GUI', 'evidence': 'toolbar != null'}),
   ('absent', 'GsActivityBase.onResume', 'GsActivityBase.onToolbarClick'),
   ('on', 'GsActivityBase.onToolbarClick', 'GsFileBrowserFragment.onToolbarClicked'),
   ('guardon', 'GsActivityBase.onToolbarClick', 'GsFileBrowserFragment.onToolbarClicked', 'notebook fragment')])

p('WrFilesWidgetFactory.getLoadingView', 'fixed',
  'FIXED (widget service lifecycle, round 8). The stale route reached the widget factory from the framework step without the service lifecycle steps. '
  'The route runs MainActivity.<init> -> onCreate -> onResume -> onPostResume -> onPause (cold start, no shortcut), then the notebook widget is updated from MainActivity.onPause (MainActivity.java:571, CALL). '
  'The launcher binds the widget service (WrMarkorWidgetProvider.onUpdate, env: outside package, WrMarkorWidgetProvider.java:98-104; AndroidManifest.xml:110-112), the service runs its lifecycle steps (onCreate, onBind, onGetViewFactory; Service and RemoteViewsService steps, FRAMEWORK_NODES), '
  'and the factory is created and updated. The framework reads the loading view at RemoteViewsService.java:177 (the edge cites this line). The loading view is a fixed RemoteViews (WrFilesWidgetFactory.java:95).',
  [('has', 'MainActivity.<init>', 'MainActivity.onCreate', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onCreate', 'MainActivity.onResume', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onResume', 'MainActivity.onPostResume', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onPostResume', 'MainActivity.onPause', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onPause', 'WrMarkorWidgetProvider.updateLauncherWidgets', {'kind': 'CALL'}),
   ('onenv', 'WrMarkorWidgetProvider.onUpdate', 'WrFilesWidgetService.<init>', 'outside package'),
   ('has', 'WrFilesWidgetService.<init>', 'WrFilesWidgetService.onCreate', {'kind': 'LIFECYCLE'}),
   ('has', 'WrFilesWidgetService.onCreate', 'WrFilesWidgetService.onBind', {'kind': 'LIFECYCLE'}),
   ('has', 'WrFilesWidgetService.onBind', 'WrFilesWidgetService.onGetViewFactory', {'kind': 'LIFECYCLE'}),
   ('has', 'WrFilesWidgetService.onGetViewFactory', 'WrFilesWidgetFactory.onCreate', {'kind': 'FRAMEWORK'}),
   ('on', 'WrFilesWidgetFactory.onDataSetChanged', 'WrFilesWidgetFactory.getLoadingView')])

p('TodoWidgetRemoteViewsFactory.getCount', 'fixed',
  'FIXED (widget service lifecycle, round 8). The stale route reached the todo widget factory from the framework step without the service steps. '
  'The route runs MainActivity.<init> -> onCreate -> onResume -> onPostResume -> onPause (cold start, no shortcut), then the todo widget is updated from MainActivity.onPause (CALL to TodoWidgetProvider.updateTodoWidgets). '
  'TodoWidgetProvider.onUpdate starts TodoWidgetService (env: outside package), which runs onCreate, onBind and onGetViewFactory (Service and RemoteViewsService steps, FRAMEWORK_NODES). The factory is created and onDataSetChanged runs; '
  'the framework reads the count at RemoteViewsService.java:154 (the edge cites this line and TodoWidgetRemoteViewsFactory.java:52).',
  [('has', 'MainActivity.<init>', 'MainActivity.onCreate', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onCreate', 'MainActivity.onResume', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onResume', 'MainActivity.onPostResume', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onPostResume', 'MainActivity.onPause', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onPause', 'TodoWidgetProvider.updateTodoWidgets', {'kind': 'CALL'}),
   ('onenv', 'TodoWidgetProvider.onUpdate', 'TodoWidgetService.<init>', 'outside package'),
   ('has', 'TodoWidgetService.<init>', 'TodoWidgetService.onCreate', {'kind': 'LIFECYCLE'}),
   ('has', 'TodoWidgetService.onCreate', 'TodoWidgetService.onBind', {'kind': 'LIFECYCLE'}),
   ('has', 'TodoWidgetService.onBind', 'TodoWidgetService.onGetViewFactory', {'kind': 'LIFECYCLE'}),
   ('has', 'TodoWidgetService.onGetViewFactory', 'TodoWidgetRemoteViewsFactory.onCreate', {'kind': 'FRAMEWORK'}),
   ('has', 'TodoWidgetRemoteViewsFactory.onCreate', 'TodoWidgetRemoteViewsFactory.onDataSetChanged'),
   ('on', 'TodoWidgetRemoteViewsFactory.onDataSetChanged', 'TodoWidgetRemoteViewsFactory.getCount')])

p('StoragePermissionActivity.processPermissionState', 'fixed',
  'FIXED (S3; cold start, this pass). The stale route started MainActivity.<init> -> MainActivity.onResume and went straight from StoragePermissionActivity.<init> to onActivityFirstTimeVisible, '
  'skipping onCreate, onResume and onPostResume for that activity. That edge is absent in the current graph (asserted), and the route now runs StoragePermissionActivity.<init> -> '
  'MarkorBaseActivity.onCreate@PERM -> GsActivityBase.onResume@PERM -> GsActivityBase.onPostResume@PERM -> onActivityFirstTimeVisible. The route passes MainActivity.onResume, '
  'where the permission request is made, without MainActivity.onPostResume: the first-visible hook does nothing in the standard configuration (judgement; counted as J_RESUME, see readme_notes.md). '
  'The first graph wired StoragePermissionActivity.<init> to onActivityResult (FRAMEWORK). That wiring is skipped (_CB_SKIP) and the hook '
  'is UNREACHABLE (closed_by_api_level): on API 27 the request goes through ActivityCompat.requestPermissions (GsContextUtils.java:2400), '
  'and the route now ends at onRequestPermissionsResult.',
  [('absent', 'StoragePermissionActivity.<init>', 'StoragePermissionActivity.onActivityResult'),
   ('has', 'MainActivity.onCreate', 'MainActivity.onResume', {'kind': 'LIFECYCLE'}),
   ('has', 'StoragePermissionActivity.<init>', 'MarkorBaseActivity.onCreate@PERM', {'kind': 'LIFECYCLE'}),
   ('on', 'GsActivityBase.onPostResume@PERM', 'StoragePermissionActivity.onActivityFirstTimeVisible'),
   ('on', 'StoragePermissionActivity.lambda$askForPermissions$1', 'StoragePermissionActivity.onRequestPermissionsResult')])

p('MarkorContextUtils.getIntentFile(Intent)', 'fixed',
  'FIXED (E3; cold start, this pass). The stale route started MainActivity.<init> -> MainActivity.onResume -> MainActivity.onPause, skipping onCreate and onPostResume; '
  'the route now runs MainActivity.<init> -> onCreate -> onResume -> onPostResume -> onPause before the todo widget update. '
  'The todo widget and the notebook widget shared one state (S_HOME_WIDGET), so the todo route reached a page whose buttons cited '
  'WrMarkorWidgetProvider. The state is split: S_HOME_WIDGET_TODO has one outgoing edge, GUI to OpenFromShortcutOrWidgetActivity.<init> (TodoWidgetProvider.java:38-42).',
  [('has', 'MainActivity.<init>', 'MainActivity.onCreate', {'kind': 'LIFECYCLE'}),
   ('has', 'MainActivity.onPostResume', 'MainActivity.onPause', {'kind': 'LIFECYCLE'}),
   ('has', 'S_HOME_WIDGET_TODO', 'OpenFromShortcutOrWidgetActivity.<init>', {'kind': 'GUI'}),
   ('on', 'TodoWidgetProvider.onUpdate', 'S_HOME_WIDGET_TODO'),
   ('on', 'OpenFromShortcutOrWidgetActivity.onCreate', 'DocumentActivity.launch(Activity,Intent)')])

p('GsFileBrowserListAdapter.lambda$scrollToAndFlash$3', 'fixed',
  'FIXED (listener guards, this pass). The route runs through the notebook folder tap (S_NOTEBOOK -> GsFileBrowserListAdapter.onClick, then loadFolder and the scroll chain), not through the FAB. '
  'The stale copy of this route went through a FRAMEWORK edge from MainActivity.onCreate to MainActivity.onClickFab (E68c24288), which is no longer in the graph. '
  'The scroll chain (loadFolder listener, postScrollToAndFlash listener, scrollToAndFlash, lambda$scrollToAndFlash$4) now carries its early returns and the pos >= 0 condition on the way to lambda$scrollToAndFlash$3 (GsFileBrowserListAdapter.java:628-630). '
  'The FAB tap (S_NOTEBOOK -> MainActivity.onClickFab, INFERRED) and the FAB listener registration are checked in their own rows below; they are not on this route.',
  [('guardon', 'GsFileBrowserListAdapter.scrollToAndFlash', 'GsFileBrowserListAdapter.lambda$scrollToAndFlash$4', 'pos >= 0'),
   ('guardon', 'GsFileBrowserListAdapter.lambda$scrollToAndFlash$4', 'GsFileBrowserListAdapter.lambda$scrollToAndFlash$3', 'pos >= 0')])

p('SyntaxHighlighterBase$1.draw', 'fixed',
  'FIXED (S2). The route is a format-menu switch on the todo page: S_TODO, the editor menu (DocumentEditAndViewFragment.onOptionsItemSelected), applyTextFormat '
  'and HighlightingEditor.setHighlighter. The key-value generator is reached only through the compute call under its key-value format state. '
  'The INFERRED lift from the base compute to the key-value generator is absent (checked), and the Asciidoc call is state-gated by the asciidoc format, so it is not on this route. This pass also put the empty-text early return (SyntaxHighlighterBase.java:437-439) on the compute edge and the highlighter registration conditions on the setHighlighter and recompute edges.',
  [('on', 'S_TODO', 'DocumentEditAndViewFragment.onOptionsItemSelected'),
   ('on', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'DocumentEditAndViewFragment.applyTextFormat'),
   ('on', 'DocumentEditAndViewFragment.applyTextFormat', 'HighlightingEditor.setHighlighter'),
   ('on', 'SyntaxHighlighterBase.compute', 'KeyValueSyntaxHighlighter.generateSpans'),
   ('stated', 'SyntaxHighlighterBase.compute', 'KeyValueSyntaxHighlighter.generateSpans', 'uses the key-value format'),
   ('stated', 'SyntaxHighlighterBase.compute', 'AsciidocSyntaxHighlighter.generateSpans', 'uses the asciidoc format'),
   ('guardon', 'SyntaxHighlighterBase.compute', 'KeyValueSyntaxHighlighter.generateSpans', 'TextUtils.isEmpty(_spannable)'),
   ('guardon', 'HighlightingEditor.setHighlighter', 'HighlightingEditor.recomputeHighlightingAsync', '_hl != null'),
   ('guardon', 'HighlightingEditor.recomputeHighlightingAsync', 'HighlightingEditor._recomputeHighlightingWorker', '_hlEnabled && runHighlight(true)')])

p('WikitextLinkResolver.wikitextPagePathToRelativeFilePath', 'fixed',
  'FIXED (virtual dispatch). The route starts from the quick note page wikitext button (S_QUICKNOTE, GUI to WikitextActionButtons.onActionClick, wikitext format state), '
  'which reaches WikitextLinkResolver.resolveWikitextPath and then this method. The share-as-HTML edge from the document menu into WikitextTextConverter.convertMarkup is absent (checked); '
  'the converter is now reached from the document page by its own GUI edge with the wikitext format state. The quick-note button edge also carries its displayMode condition (ActionButtonBase.java:305).',
  [('on', 'S_QUICKNOTE', 'WikitextActionButtons.onActionClick'),
   ('on', 'WikitextLinkResolver.resolveWikitextPath', 'WikitextLinkResolver.wikitextPagePathToRelativeFilePath'),
   ('stated', 'S_QUICKNOTE', 'WikitextActionButtons.onActionClick', 'uses the wikitext format'),
   ('absent', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'WikitextTextConverter.convertMarkup'),
   ('guardon', 'S_QUICKNOTE', 'WikitextActionButtons.onActionClick', 'the action is in this bar')])

p('GsSharedPreferencesPropertyBackend.getInt(String,int,SharedPreferences[])', 'correct',
  'CORRECT. AppSettings.<init> reads the preference through the int overload, which calls the String overload.',
  [('on', 'AppSettings.<init>', 'GsSharedPreferencesPropertyBackend.getInt(int,int,SharedPreferences[])'),
   ('on', 'GsSharedPreferencesPropertyBackend.getInt(int,int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getInt(String,int,SharedPreferences[])')])

p('GsSharedPreferencesPropertyBackend.rcolor', 'correct',
  'CORRECT. AppSettings.setEditorBasicColor reads the colour through rcolor.',
  [('on', 'AppSettings.setEditorBasicColor', 'GsSharedPreferencesPropertyBackend.rcolor')])

p('GsSharedPreferencesPropertyBackend.rstr', 'correct',
  'CORRECT. The int overload of getInt calls rstr.',
  [('on', 'GsSharedPreferencesPropertyBackend.getInt(int,int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.rstr')])

p('GsSharedPreferencesPropertyBackend.<init>', 'correct',
  'CORRECT. AppSettings.<init> creates the preference backend.',
  [('on', 'AppSettings.<init>', 'GsSharedPreferencesPropertyBackend.<init>')])

p('GsSharedPreferencesPropertyBackend.gp', 'correct',
  'CORRECT. AppSettings.<init> sets the two editor colours when the background colour key is not stored yet (AppSettings.java:79-81, guard getInt(R.string.pref_key__basic_color_scheme__bg_light, -999) == -999). '
  'setEditorBasicColor writes each colour through setInt, and setInt passes its target to gp (gp is defined at GsSharedPreferencesPropertyBackend.java:135 and used at line 269).',
  [('guardon', 'AppSettings.<init>', 'AppSettings.setEditorBasicColor', 'getInt(R.string.pref_key__basic_color_scheme__bg_light'),
   ('on', 'AppSettings.setEditorBasicColor', 'GsSharedPreferencesPropertyBackend.setInt(int,int,SharedPreferences[])'),
   ('has', 'GsSharedPreferencesPropertyBackend.setInt(int,int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.gp', {'kind': 'CALL'})])

p('GsContextUtils.<init>', 'correct',
  'CORRECT. AppSettings.<init> creates MarkorContextUtils (AppSettings.java:76). The JVM initialises the superclass GsContextUtils first, so GsContextUtils.<clinit> runs; its static field instance (GsContextUtils.java:167) constructs a GsContextUtils, which runs GsContextUtils.<init> (GsContextUtils.java:169).',
  [('on', 'AppSettings.<init>', 'GsContextUtils.<clinit>'),
   ('on', 'GsContextUtils.<clinit>', 'GsContextUtils.<init>')])

p('GsContextUtils.setChooserTitle', 'correct',
  'CORRECT. AppSettings.<init> creates MarkorContextUtils (AppSettings.java:76), whose constructor calls setChooserTitle only when the context is not null (MarkorContextUtils.java:40-41, context != null). '
  'AppSettings has already used the same context to open its preferences (AppSettings.java:74-75), so the condition holds on this route.',
  [('on', 'AppSettings.<init>', 'MarkorContextUtils.<init>'),
   ('has', 'MarkorContextUtils.<init>', 'GsContextUtils.setChooserTitle', {'kind': 'CALL'})])

p('DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getLinkTitle', 'fixed',
  'FIXED (fix 2, this pass). The route is the other-app share entry (DocumentActivity.handleLaunchingIntent@SEND -> showShareInto, env "another app"), then the share-into page committed by showShareInto, '
  'then the resumed share-into page (DocumentActivity.onResume@SHARE ENTERS S_SHARE_INTO, DocumentActivity.java:310-313), then the share-into preference pick (S_SHARE_INTO, GUI, DocumentShareIntoFragment.java:516), '
  'attachOrCopyAndClose, getFormatted, the line walk and getLineLink. Before this pass showShareInto itself had an ENTERS edge to the share-into page (the fix 2 error); that edge is removed. '
  'The line-walk listener in getFormatted is registered only when asLink is true (DocumentShareIntoFragment.java:385); that condition is on the getFormatted > lambda$getFormatted$2 edge. '
  'getLineLink reaches getLinkTitle only for a web link (Patterns.WEB_URL, the getLineLink > getLinkTitle guard).',
  [('onenv', 'DocumentActivity.handleLaunchingIntent@SEND', 'DocumentActivity.showShareInto', 'another app'),
   ('on', 'DocumentActivity.showShareInto', 'DocumentActivity.onResume@SHARE'),
   ('has', 'DocumentActivity.onResume@SHARE', 'S_SHARE_INTO', {'kind': 'ENTERS'}),
   ('absent', 'DocumentActivity.showShareInto', 'S_SHARE_INTO'),
   ('on', 'S_SHARE_INTO', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.onPreferenceClicked'),
   ('on', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.onPreferenceClicked', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.attachOrCopyAndClose'),
   ('on', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.attachOrCopyAndClose', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getFormatted'),
   ('guardon', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getFormatted', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.lambda$getFormatted$2', 'asLink is true'),
   ('on', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getLineLink', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getLinkTitle')])

p('SyntaxHighlighterBase.isFixupOverlap', 'fixed',
  'FIXED (fix 1 and fix 2, this pass). The route taps a file in the notebook list (S_NOTEBOOK, GUI to GsFileBrowserListAdapter.onClick; the row listener is set at GsFileBrowserListAdapter.java:271; the single-file tap calls the listener at 426, and the OK button at 440). '
  'The notebook listener opens it (MainActivity$2.onFsViewerSelected -> DocumentActivity.launch, MainActivity.java:490), then the in-app launch reaches DocumentActivity.<init> (INTENT; launch returns early for a null activity or file at DocumentActivity.java:71-73, and the edge to the constructor carries the forceOpenInThisApp guard), '
  'onCreate, handleLaunchingIntent and the resumed editor (DocumentActivity.onResume@EDIT ENTERS S_DOCUMENT, DocumentActivity.java:229, 310-313). Then the text-change fixup: HighlightingEditor$1.onTextChanged (guard _hlEnabled && _hl != null), '
  'fixup(int,int,int), fixup(int,int) and isFixupOverlap (guard _fixupAfter == -1).',
  [('on', 'S_NOTEBOOK', 'GsFileBrowserListAdapter.onClick'),
   ('on', 'GsFileBrowserListAdapter.onClick', 'MainActivity$2.onFsViewerSelected'),
   ('on', 'MainActivity$2.onFsViewerSelected', 'DocumentActivity.launch(Activity,File,Boolean,Integer)'),
   ('guardon', 'DocumentActivity.launch(Activity,File,Boolean,Integer,boolean)', 'DocumentActivity.<init>', 'forceOpenInThisApp'),
   ('guardon', 'DocumentActivity.handleLaunchingIntent', 'DocumentActivity.onResume@EDIT', 'frag'),
   ('has', 'DocumentActivity.onResume@EDIT', 'S_DOCUMENT', {'kind': 'ENTERS'}),
   ('on', 'HighlightingEditor$1.onTextChanged', 'SyntaxHighlighterBase.fixup(int,int,int)'),
   ('guardon', 'HighlightingEditor$1.onTextChanged', 'SyntaxHighlighterBase.fixup(int,int,int)', '_hl != null'),
   ('on', 'SyntaxHighlighterBase.fixup(int,int)', 'SyntaxHighlighterBase.isFixupOverlap'),
   ('guardon', 'SyntaxHighlighterBase.fixup(int,int)', 'SyntaxHighlighterBase.isFixupOverlap', '_fixupAfter == -1')])

p('DocumentShareIntoFragment$ShareIntoImportOptionsFragment.lambda$hasLinks$1', 'fixed',
  'FIXED (creation guard, this pass). The route is the other-app share entry (S_ENTRY into the SEND variant of DocumentActivity, env "another app sends the intent"), then showShareInto, the share-into fragment creation and its preference setup, then afterOnCreate and hasLinks. '
  'The fragment creation (DocumentShareIntoFragment.java:97) runs only when _savedInstanceState is null; that condition is now on the onViewCreated > ShareIntoImportOptionsFragment.<init> edge. '
  'The hasLinks listener (DocumentShareIntoFragment.java:361) has no extra condition on this route.',
  [('onenv', 'DocumentActivity.handleLaunchingIntent@SEND', 'DocumentActivity.showShareInto', 'another app'),
   ('guardon', 'DocumentShareIntoFragment.onViewCreated', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.<init>', '_savedInstanceState == null'),
   ('on', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.afterOnCreate', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.hasLinks'),
   ('on', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.hasLinks', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.lambda$hasLinks$1')])

p('AppSettings.lambda$getPopularDocumentsSorted$1', 'fixed',
  'FIXED (notebook info guard, round 8; the route moved). The stale route used the notebook menu info action (S_NOTEBOOK -> GsFileBrowserFragment.onOptionsItemSelected). That edge no longer reaches the dialog: the notebook info action runs only from the selection state (S_NOTEBOOK_SEL, guarded by areItemsSelected, GsFileBrowserFragment.java:457-460), and this route does not use it. '
  'The route now enters the todo page from the notebook tab (S_NOTEBOOK > MainActivity.lambda$onCreate$0 > S_TODO, MainActivity.java:109-112) and runs the todo page info action (DocumentEditAndViewFragment.onOptionsItemSelected, case R.id.action_info, DocumentEditAndViewFragment.java:604-606). That action calls FileInfoDialog.show only when saveDocument(false) returns true (the if at line 605; guard on the edge). '
  'The dialog builds its checkbox listener in setUpDialog (FRAMEWORK edge to lambda$setUpDialog$3, INFERRED: the listener type is not read per lambda). The checkbox calls AppSettings.setListFileInRecents (FileInfoDialog.java:126), '
  'which calls setRecentDocuments (AppSettings.java:875) and getPopularDocumentsSorted (AppSettings.java:638); the sort comparator is the listener registered at AppSettings.java:626 (FRAMEWORK, INFERRED). '
  'The route assumes the checkbox is ticked (judgement: no graph edge carries that condition).',
  [('on', 'S_NOTEBOOK', 'MainActivity.lambda$onCreate$0'),
   ('on', 'MainActivity.lambda$onCreate$0', 'S_TODO'),
   ('on', 'S_TODO', 'DocumentEditAndViewFragment.onOptionsItemSelected'),
   ('guardon', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'FileInfoDialog.show', 'saveDocument(false) returns true'),
   ('on', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'FileInfoDialog.show'),
   ('on', 'FileInfoDialog.show', 'FileInfoDialog.newInstance'),
   ('on', 'FileInfoDialog.newInstance', 'FileInfoDialog.onCreateDialog'),
   ('on', 'FileInfoDialog.onCreateDialog', 'FileInfoDialog.setUpDialog'),
   ('on', 'FileInfoDialog.setUpDialog', 'FileInfoDialog.lambda$setUpDialog$3'),
   ('on', 'FileInfoDialog.lambda$setUpDialog$3', 'AppSettings.setListFileInRecents'),
   ('on', 'AppSettings.setListFileInRecents', 'AppSettings.setRecentDocuments'),
   ('on', 'AppSettings.setRecentDocuments', 'AppSettings.getPopularDocumentsSorted'),
   ('on', 'AppSettings.getPopularDocumentsSorted', 'AppSettings.lambda$getPopularDocumentsSorted$1')])

p('CsvConfig.findChar', 'fixed',
  'FIXED (early-return guard, this pass). The route is the todo page editor menu reload (S_TODO, DocumentEditAndViewFragment.onOptionsItemSelected, loadDocument), then updateViewModeText and the web-view conversion (TextConverterBase.convertMarkupShowInWebView) into the CSV table converter, which infers the CSV configuration line by line (CsvConfig.infer). '
  'The converter call is reached only when the web view exists: the early return at DocumentEditAndViewFragment.java:988-990 is now on the convertMarkupShowInWebView > CsvTextConverter.convertMarkup edge. '
  'The out-of-memory catch on updateViewModeText is a disjunction with the normal path (the call at DocumentEditAndViewFragment.java:993-995 runs when no error is caught), so it is not added to the route; the gate reports it as a judgement item, not a missing condition.',
  [('on', 'DocumentEditAndViewFragment.loadDocument', 'DocumentEditAndViewFragment.updateViewModeText'),
   ('guardon', 'TextConverterBase.convertMarkupShowInWebView', 'CsvTextConverter.convertMarkup', 'not (_webView == null)'),
   ('on', 'CsvTextConverter.convertMarkup', 'CsvTextConverter$Csv2MdTable.toMdTable(String)'),
   ('on', 'CsvConfig.infer', 'CsvConfig.findChar')])

p('WikitextLinkResolver.findNotebookRootDir(File,File,boolean)', 'fixed',
  'FIXED (button and receiver guards, this pass). The route is the todo page action button (S_TODO, GUI to TodoTxtActionButtons.onActionClick, which the button bar guards with its displayMode condition, ActionButtonBase.java:305), '
  'then the insert-image-or-link dialog, its browse listener (AttachLinkOrFileDialog.java:446-448: LINK_BROWSE, IMAGE_BROWSE, AUDIO_BROWSE), and lambda$fetchAndInsertItem$10, which calls WikitextLinkResolver.resolveSystemFilePath. '
  'That call runs only in the wikitext branch (AttachLinkOrFileDialog.java:381, FormatRegistry.FORMAT_WIKITEXT), and the edge carries that condition. '
  'The gate also lists the loop over orderedKeys on the button edge (a loop, not a condition) and a case AUDIO_RECORDING label; the built guard cites AUDIO_BROWSE, so that label is a gate artifact.',
  [('guardon', 'S_TODO', 'TodoTxtActionButtons.onActionClick', 'the action is in this bar'),
   ('on', 'AttachLinkOrFileDialog$1.onFsViewerSelected', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$10'),
   ('guardon', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$10', 'WikitextLinkResolver.resolveSystemFilePath', 'the wikitext branch of setFields is taken'),
   ('on', 'WikitextLinkResolver.resolveSystemFilePath', 'WikitextLinkResolver.findNotebookRootDir(File,File,boolean)')])

p('SyntaxHighlighterBase$SpanGroup.compareTo', 'correct',
  'CORRECT (new in the final draw; not drawn before). The route is the todo page search: S_TODO, DocumentEditAndViewFragment.onOptionsItemSelected (search case, guard), ActionButtonBase.onSearch, TextSearchFragment.show, find2 and TextSearchHandler.find, '
  'then TextSearchHandler.loadMatches, whose while loop creates one Match per hit; Match.java:18 calls SyntaxHighlighterBase.createBackgroundHighlight (SyntaxHighlighterBase.java:695-697), which makes the SpanGroup. '
  'compareTo is the body at SyntaxHighlighterBase.java:171 (start - o.start). The graph reaches it through an INFERRED framework edge from createBackgroundHighlight; the sorted set at SyntaxHighlighterBase.java:197 and the Collections.sort calls (lines 444, 670, 678) may be the callers, and the edge does not name the caller.',
  [('guardon', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'ActionButtonBase.onSearch', 'case R.id.action_search'),
   ('on', 'S_TODO', 'DocumentEditAndViewFragment.onOptionsItemSelected'),
   ('on', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'ActionButtonBase.onSearch'),
   ('on', 'ActionButtonBase.onSearch', 'TextSearchFragment.show'),
   ('on', 'TextSearchFragment.show', 'TextSearchFragment.find2'),
   ('on', 'TextSearchFragment.find2', 'TextSearchHandler.find'),
   ('on', 'TextSearchHandler.find', 'TextSearchHandler.loadMatches'),
   ('on', 'TextSearchHandler.loadMatches', 'Match.<init>'),
   ('on', 'Match.<init>', 'SyntaxHighlighterBase.createBackgroundHighlight'),
   ('on', 'SyntaxHighlighterBase.createBackgroundHighlight', 'SyntaxHighlighterBase$SpanGroup.compareTo')])

p('WrWidgetConfigure$1.<init>', 'correct',
  'CORRECT. The widget configure activity is started from outside the package (ApplicationObject.onCreate -> WrWidgetConfigure.<init>, env "outside package", ENTRY ENV). Its onCreate (WrWidgetConfigure.java:35) calls showWidgetSelectFolderDialog (line 44), which is defined at line 56 and creates the anonymous selection listener WrWidgetConfigure$1 (line 58). The route runs the activity onCreate before the listener is made; the folder browser itself is shown from the resumed step (GsActivityBase.onResume@WRCONFIG ENTERS S_WIDGET_CONFIG), which this route does not reach.',
  [('onenv', 'ApplicationObject.onCreate', 'WrWidgetConfigure.<init>', 'outside package'),
   ('has', 'WrWidgetConfigure.<init>', 'WrWidgetConfigure.onCreate', {'kind': 'LIFECYCLE'}),
   ('on', 'WrWidgetConfigure.onCreate', 'WrWidgetConfigure.showWidgetSelectFolderDialog'),
   ('on', 'WrWidgetConfigure.showWidgetSelectFolderDialog', 'WrWidgetConfigure$1.<init>')])

p('ActionButtonSettingsActivity.lambda$saveNewOrder$0', 'correct',
  'CORRECT (new in the final draw; not drawn before). A bottom-navigation tap from the notebook page opens the More page (MainActivity.lambda$onCreate$0, ENTERS S_MORE, MainActivity.java:109-114), the More preference that opens Settings (MoreInfoFragment.java:60-66), '
  'the Settings list (S_SETTINGS, SettingsFragmentMaster), the action button order screen (S_ACTION_BUTTONS, entered from the resumed step GsActivityBase.onResume@ACTIONBTN). Leaving that screen calls onPause (GUI, ActionButtonSettingsActivity.java:112-114), '
  'which calls saveNewOrder (line 106); the lambda i -> _keys.get(i) at line 107 is passed to GsCollectionUtils.map (edge saveNewOrder -> lambda$saveNewOrder$0, FRAMEWORK, INFERRED: the utility calls the mapper).',
  [('on', 'S_NOTEBOOK', 'MainActivity.lambda$onCreate$0'),
   ('on', 'MainActivity.lambda$onCreate$0', 'S_MORE'),
   ('on', 'S_MORE', 'MoreInfoFragment.onPreferenceClicked'),
   ('guardon', 'MoreInfoFragment.onPreferenceClicked', 'SettingsActivity.<init>', 'keyResId == R.string.pref_key__more_info__settings'),
   ('has', 'SettingsActivity.onCreate', 'GsActivityBase.onResume@SETTINGS', {'kind': 'LIFECYCLE'}),
   ('has', 'GsActivityBase.onResume@SETTINGS', 'S_SETTINGS', {'kind': 'ENTERS'}),
   ('on', 'S_SETTINGS', 'SettingsActivity$SettingsFragmentMaster.onPreferenceClicked'),
   ('on', 'SettingsActivity$SettingsFragmentMaster.onPreferenceClicked', 'ActionButtonSettingsActivity.<init>'),
   ('has', 'ActionButtonSettingsActivity.onCreate', 'GsActivityBase.onResume@ACTIONBTN', {'kind': 'LIFECYCLE'}),
   ('has', 'GsActivityBase.onResume@ACTIONBTN', 'S_ACTION_BUTTONS', {'kind': 'ENTERS'}),
   ('on', 'S_ACTION_BUTTONS', 'ActionButtonSettingsActivity.onPause'),
   ('on', 'ActionButtonSettingsActivity.onPause', 'ActionButtonSettingsActivity.saveNewOrder'),
   ('on', 'ActionButtonSettingsActivity.saveNewOrder', 'ActionButtonSettingsActivity.lambda$saveNewOrder$0')])

p('DocumentEditAndViewFragment$2.lambda$search$0', 'fixed',
  'FIXED (search guards and view-mode state, round 8; the route was correct but its guards were not on the graph). A bottom-navigation tap from the notebook page selects the todo or quick-note page (MainActivity.java:109-112, lambda$onCreate$0), which runs the page change listener (MainActivity.java:95, MainActivity$1.onPageSelected) and onViewPagerPageSelected; that creates the document fragment only when the adapter exists and the tab is realized (MainActivity.java:445-446, 515-518). '
  'The fragment lifecycle runs onCreate, onViewCreated and onResume; the menu edge DocumentEditAndViewFragment.onResume -> onCreateOptionsMenu is modelled after the resumed step, and the AOSP order is not pinned (see readme_notes.md Limits). '
  'The search view is set up only in view mode: setupSearchView returns early unless the editor is in preview with a web view (DocumentEditAndViewFragment.java:697-699; guard and NEED_PREVIEW state on the setupSearchView > onQueryTextChange edge). '
  'The debounced search returns at once when the web view is null (DocumentEditAndViewFragment.java:707-708; guard on the search > lambda$search$0 edge). The route needs the preview state, which no earlier step on the route sets (judgement: the todo page is assumed in view mode). The debounced listener is INFERRED (the listener type is not read per lambda).',
  [('on', 'S_NOTEBOOK', 'MainActivity.lambda$onCreate$0'),
   ('on', 'MainActivity.lambda$onCreate$0', 'MainActivity$1.onPageSelected'),
   ('on', 'MainActivity$1.onPageSelected', 'MainActivity.onViewPagerPageSelected'),
   ('guardon', 'MainActivity.onViewPagerPageSelected', 'DocumentEditAndViewFragment.onCreate', '_sectionsAdapter != null'),
   ('on', 'DocumentEditAndViewFragment.onCreate', 'DocumentEditAndViewFragment.onViewCreated'),
   ('on', 'DocumentEditAndViewFragment.onViewCreated', 'DocumentEditAndViewFragment.onResume'),
   ('on', 'DocumentEditAndViewFragment.onResume', 'DocumentEditAndViewFragment.onCreateOptionsMenu'),
   ('on', 'DocumentEditAndViewFragment.onCreateOptionsMenu', 'DocumentEditAndViewFragment.setupSearchView'),
   ('guardon', 'DocumentEditAndViewFragment.setupSearchView', 'DocumentEditAndViewFragment$2.onQueryTextChange', 'not (!_isPreviewVisible || _webView == null)'),
   ('stated', 'DocumentEditAndViewFragment.setupSearchView', 'DocumentEditAndViewFragment$2.onQueryTextChange', 'preview mode'),
   ('on', 'DocumentEditAndViewFragment$2.onQueryTextChange', 'DocumentEditAndViewFragment$2.search'),
   ('on', 'DocumentEditAndViewFragment$2.search', 'DocumentEditAndViewFragment$2.lambda$search$0'),
   ('guardon', 'DocumentEditAndViewFragment$2.search', 'DocumentEditAndViewFragment$2.lambda$search$0', 'not (_webView == null)')])

p('AppSettings.getAttachmentFolder', 'correct',
  'CORRECT (new in the final draw; not drawn before). A bottom-navigation tap from the notebook page selects the todo page (ENTERS S_TODO from MainActivity.lambda$onCreate$0, MainActivity.java:109-114). The todo page action bar long press (S_TODO, TodoTxtActionButtons.onActionLongClick, guarded by the display-mode and enabled check of the bar, ActionButtonBase.java:304-305) '
  'runs the common long-press action (ActionButtonBase.runCommonLongPressAction), whose case for R.string.abid_common_insert_image calls AttachLinkOrFileDialog.insertCameraPhoto; then fetchAndInsertItem, the camera result listener lambda$fetchAndInsertItem$9 (FRAMEWORK, env: reached from an external activity; the listener type is INFERRED), '
  'setupFileAttachment (AttachLinkOrFileDialog.java:287) and getAttachmentFolder. That last call is guarded by the non-wikitext format and by the attachment lying outside the notebook (not GsFileUtils.isChild(notebookDir, attachment)).',
  [('on', 'S_NOTEBOOK', 'MainActivity.lambda$onCreate$0'),
   ('on', 'MainActivity.lambda$onCreate$0', 'S_TODO'),
   ('guardon', 'S_TODO', 'TodoTxtActionButtons.onActionLongClick', 'the action is in this bar'),
   ('on', 'AttachLinkOrFileDialog.insertCameraPhoto', 'AttachLinkOrFileDialog.fetchAndInsertItem'),
   ('onenv', 'AttachLinkOrFileDialog.fetchAndInsertItem', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$9', 'outside package'),
   ('on', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$9', 'AttachLinkOrFileDialog.setupFileAttachment'),
   ('guardon', 'AttachLinkOrFileDialog.setupFileAttachment', 'AppSettings.getAttachmentFolder', 'isChild')])

p('GsFileBrowserListAdapter.createDirectoryHere', 'correct',
  'CORRECT (new in the final draw; not drawn before). The notebook menu (S_NOTEBOOK, GsFileBrowserFragment.onOptionsItemSelected, GUI from the page after the resumed step), the move-or-copy action (askForMoveOrCopy, GsFileBrowserFragment.java:438-440), '
  'the folder dialog (MarkorFileBrowserFactory.showFolderDialog and showDialog, GsFileBrowserDialog.newInstance), its view and click callbacks (FRAMEWORK, INFERRED: the dialog listener is not read per lambda; onClicked at GsFileBrowserDialog.java:208), '
  'the new-folder dialog (showNewDirDialog), whose callback lambda$showNewDirDialog$2 calls createDirectoryHere (GsFileBrowserDialog.java:263). The folder dialog is the move-or-copy picker, not the notebook list row tap.',
  [('on', 'S_NOTEBOOK', 'GsFileBrowserFragment.onOptionsItemSelected'),
   ('on', 'GsFileBrowserFragment.onOptionsItemSelected', 'GsFileBrowserFragment.askForMoveOrCopy'),
   ('on', 'GsFileBrowserFragment.askForMoveOrCopy', 'MarkorFileBrowserFactory.showFolderDialog'),
   ('on', 'MarkorFileBrowserFactory.showDialog', 'GsFileBrowserDialog.newInstance'),
   ('on', 'GsFileBrowserDialog.onClicked', 'GsFileBrowserDialog.showNewDirDialog'),
   ('on', 'GsFileBrowserDialog.showNewDirDialog', 'GsFileBrowserDialog.lambda$showNewDirDialog$2'),
   ('on', 'GsFileBrowserDialog.lambda$showNewDirDialog$2', 'GsFileBrowserListAdapter.createDirectoryHere')])

p('GsSharedPreferencesPropertyBackend.getStringListOne', 'correct',
  'CORRECT (new in the final draw; not drawn before). Cold start: MainActivity.onCreate sets the pager adapter and realizes its tabs (MainActivity.java:445-446), and the adapter creates the notebook page (createFragment branch, MainActivity.java:519-522). '
  'The notebook view reads its options (GsFileBrowserFragment.onViewCreated, MainActivity.getFilesystemFragmentOptions, MarkorFileBrowserFactory.prepareFsViewerOpts and updateFsViewerOpts), and the popular-files list is read through AppSettings.getPopularFiles and the string-list backend. '
  'The route has no resumed step before this, so the notebook view is created in onCreate and shown later from onPostResume (the open item on fragment view timing, readme_notes.md Limits). The route is tagged J_NOTEBOOK (cold start; counted, not a failure).',
  [('has', 'MainActivity.onCreate', CF, {'kind': 'FRAMEWORK'}),
   ('on', CF, 'GsFileBrowserFragment.onViewCreated'),
   ('on', 'GsFileBrowserFragment.onViewCreated', 'MainActivity.getFilesystemFragmentOptions'),
   ('on', 'AppSettings.getPopularFiles', 'GsSharedPreferencesPropertyBackend.getStringList(int,SharedPreferences[])'),
   ('on', 'GsSharedPreferencesPropertyBackend.getStringList(int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getStringListOne')])

assert len(P) == 30 and set(P) == set(SAMPLE), set(SAMPLE) ^ set(P)

# ---- cold-start check on every sampled route: S_ENTRY -> ApplicationObject.<init> -> ApplicationObject.onCreate come first,
# every activity constructor is followed by its onCreate, and no lifecycle step is skipped (skip counts must be 0).
# Judgement tags are counted, not failures. J_RESUME is asserted to be exactly the two routes that pass
# MainActivity.onResume without MainActivity.onPostResume.
def mname(n):
    return n.split('(')[0].split('@')[0].rsplit('.', 1)[-1]


def mcls(n):
    return n.split('(')[0].split('@')[0].rsplit('.', 1)[0]


SKIP = {'<init>': ('onResume', 'onPause', 'onPostResume', 'onActivityFirstTimeVisible'),
        'onCreate': ('onPause', 'onPostResume', 'onActivityFirstTimeVisible'),
        'onResume': ('onPause', 'onActivityFirstTimeVisible')}
LIFE = ('<init>', 'onCreate', 'onResume', 'onPostResume', 'onPause')
LIFE_NEXT = {('<init>', 'onCreate'), ('onCreate', 'onResume'), ('onResume', 'onPostResume'), ('onPostResume', 'onPause')}
ACT_EXTRA = {'WrWidgetConfigure'}  # an activity without 'Activity' in its name (has LIFECYCLE <init> -> onCreate)
cold_rows = [['item', 'result', 'start_ok', 'ctor_ok', 'skip_hits', 'tags', 'first_steps']]
cold_tags = {}
for m in SAMPLE:
    nodes = rows[m]['shortest_path'].split(' > ')
    names = [mname(n) for n in nodes]
    start_ok = nodes[:3] == ['S_ENTRY', 'ApplicationObject.<init>', 'ApplicationObject.onCreate']
    ctor_ok = True
    skip_hits = 0
    for i, n in enumerate(nodes[:-1]):
        a, c = names[i], names[i + 1]
        is_act = ('Activity' in mcls(n) or mcls(n) in ACT_EXTRA) and 'Fragment' not in mcls(n)
        # the skip rules are about activity lifecycles only (a fragment's onResume -> onPause is ordinary)
        if is_act and a in SKIP and c in SKIP[a]:
            skip_hits += 1
        if a == '<init>' and is_act and c != 'onCreate':
            ctor_ok = False
    # MainActivity lifecycle order: each lifecycle step may follow only the step before it
    life = [mname(n) for n in nodes if mcls(n) == 'MainActivity' and mname(n) in LIFE]
    for prev_step, next_step in zip(life, life[1:]):
        if (prev_step, next_step) not in LIFE_NEXT:
            skip_hits += 1
    on_route = set(nodes)
    tags = []
    if 'MainActivity.onResume' in on_route and 'MainActivity.onPostResume' not in on_route:
        tags.append('J_RESUME')
    if 'MainActivity.onCreate' in on_route and 'MainActivity.onResume' not in on_route:
        tags.append('J_NOTEBOOK')
    if 'DocumentActivity.onCreate@SEND' in on_route and 'DocumentActivity.onResume' not in on_route:
        tags.append('J_SHARE')
    assert start_ok, (m, nodes[:3])
    assert ctor_ok, (m, 'activity constructor not followed by onCreate')
    assert skip_hits == 0, (m, 'skipped lifecycle step', skip_hits)
    cold_tags[m] = tags
    if 'J_NOTEBOOK' in tags and 'AppSettings.java:781' not in P[m]['note']:
        # the same notebook reading as the SearchAndReplaceTextDialog route: onCreate -> notebook, no onResume on this route
        P[m]['note'] = P[m]['note'].replace(' Route (', ' ' + NB_READING + ' Route (', 1)
    cold_rows.append([m, P[m]['res'], start_ok, ctor_ok, skip_hits, ','.join(tags) or '-', ' > '.join(nodes[:4])])
# J_RESUME: the routes that pass MainActivity.onResume without onPostResume. isEncryptedFile now enters the notebook from onPostResume (fix 1), so only one route is left.
assert sorted(m for m in SAMPLE if 'J_RESUME' in cold_tags[m]) == ['StoragePermissionActivity.processPermissionState'], cold_tags
with open(SCR + 'cold_start_table.txt', 'w', encoding='utf-8') as f:
    for r in cold_rows:
        f.write('\t'.join(str(x) for x in r) + '\n')
print('cold start: routes', len(SAMPLE), 'start_ok', sum(r[2] is True for r in cold_rows[1:]),
      'ctor_ok', sum(r[3] is True for r in cold_rows[1:]), 'skip_hits', sum(r[4] for r in cold_rows[1:]))
for t in ('J_RESUME', 'J_NOTEBOOK', 'J_SHARE'):
    print('  tag', t, sum(1 for m in SAMPLE if t in cold_tags[m]))

res_counts = collections.Counter(v['res'] for v in P.values())
assert res_counts == {'correct': 13, 'fixed': 17}, res_counts  # round 8: getLoadingView, getCount and compareTo replace getItemId, getViewTypeCount and clearAdditional; search$0 is now fixed (its guards are on the graph)
assert res_counts.get('wrong', 0) == 0, res_counts

out = [['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']]
for m in SAMPLE:
    v = P[m]
    out.append(['path', m, v['res'], v['cb'], LAB[m]['source_ref'], rows[m]['route_edge_ids'].strip(), v['note']])

# ---- label rows: every UNREACHABLE method
FIXED_UN = {}
oa = oldrows['StoragePermissionActivity.onActivityResult']['source_ref']
assert oa != uref('StoragePermissionActivity.onActivityResult')
FIXED_UN['StoragePermissionActivity.onActivityResult'] = (
    'FIXED (S3). The first graph had a FRAMEWORK edge from StoragePermissionActivity.<init> to this hook; the hook runs only after startActivityForResult, '
    'which is not called on API 27. Old ref %s; corrected ref %s.' % (oa, uref('StoragePermissionActivity.onActivityResult')))
assert uref('StoragePermissionActivity.onActivityResult').endswith('StoragePermissionActivity.java:70-73')
ok_ = 'GsPreferenceFragmentBase.keyToStringResId(String)'
ok_old = oldrows[ok_]['source_ref']
assert ok_old.endswith(':215'), ok_old
FIXED_UN[ok_] = (
    'FIXED. The entry cited %s (the Preference overload at line 215). Corrected to GsPreferenceFragmentBase.java:226 and the reason was rewritten '
    '(SOURCE): the app\'s only call (line 320) passes a Preference and binds to the Preference overload.' % ok_old)
assert uref(ok_).endswith('GsPreferenceFragmentBase.java:226'), uref(ok_)

ref_fix = json.load(open(G + 'scratch/ref_fix.json', encoding='utf-8'))
assert len(ref_fix) == 47, len(ref_fix)


def simple_name(key):
    cls, _, rest = key.partition('.')
    if rest.startswith('<init>'):
        return re.split(r'[$.]', cls)[-1]
    if rest.startswith('lambda'):
        return None
    return rest.split('(')[0]


def name_on_line(key, ref):
    mm = re.match(r'(.+?):(\d+)', ref)
    if not mm:
        return 'noref'
    path, line = mm.group(1), int(mm.group(2))
    if not os.path.isfile(APP + path):
        return 'nofile'
    text = open(APP + path, encoding='utf-8', errors='replace').read().splitlines()
    name = simple_name(key)
    if name is None:
        return 'lambda'
    return str(name in '\n'.join(text[max(0, line - 3):line + 2]))


name_check = collections.Counter()
for k, new in ref_fix.items():
    assert k in UNRE, k
    old = oldrows[k]['source_ref']
    assert old != new, (k, old)
    assert uref(k) == new, (k, uref(k), new)
    name_check[name_on_line(k, new)] += 1
print('ref_fix name check on the corrected line:', dict(name_check))
assert name_check['False'] == 0, 'a corrected ref does not show the method name'

chain_total = 0
for m in sorted(UNRE):
    u = dict(LAB[m]['unreachable'], ref=uref(m), confirmed_by=ucb(m))
    assert rows[m]['unreachable_kind'] == u['kind'], (m, rows[m]['unreachable_kind'], u['kind'])
    assert rows[m]['unreachable_reason'] == u['text'], m
    assert rows[m]['source_ref'] == u['ref'] and rows[m]['confirmed_by'] == u['confirmed_by'], (m, rows[m]['source_ref'], u['ref'])
    cbv = u['confirmed_by']
    if m in FIXED_UN:
        out.append(['label', m, 'fixed', cbv, u['ref'], '', FIXED_UN[m] + ' Kind %s.' % u['kind']])
        continue
    tail = ''
    mm = re.search(r'every caller is unreachable \((.*)\)$', u['text'])
    if mm:
        callers = mm.group(1).split(', ')
        for c in callers:
            assert c in UNRE, ('chain claim names a caller that is not UNREACHABLE', m, c)
        chain_total += 1
        tail = ' Chain check: caller(s) %s are UNREACHABLE in the final labels (asserted).' % ', '.join(callers)
    elif cbv == 'INFERRED':
        tail = ' INFERRED: the reason depends on a library class that is not on disk.'
    if m in ref_fix:
        old = oldrows[m]['source_ref']
        out.append(['label', m, 'fixed', cbv, u['ref'], '',
                    'FIXED (overload citation). The entry cited %s (the first or a same-arity overload); corrected to %s. Kind %s. %s%s'
                    % (old, u['ref'], u['kind'], u['text'], tail)])
    else:
        out.append(['label', m, 'correct', cbv, u['ref'], '',
                    'Kind %s, reason and ref as stored in the graph (asserted equal to methods.csv). %s%s' % (u['kind'], u['text'], tail)])
assert chain_total == 72, chain_total

# ---- label rows: every reachable sample method
for m in SAMPLE:
    v = P[m]
    l = LAB[m]
    if v['res'] in ('correct', 'fixed'):
        lres = 'correct'
        note = 'REACHABLE. Confirmed by its route (path row, result %s).' % v['res']
    else:
        lres = 'unclear'
        note = 'REACHABLE, but the route in the path row is wrong, so the label is not confirmed by it (see the path row).'
    out.append(['label', m, lres, l['confirmed_by'], l['source_ref'], '', note])


# ---- framework node added this pass (FRAMEWORK_NODES in graph_def.py): IntroActivity.onResume, inherited from Activity
_ir = LAB['IntroActivity.onResume']
assert rows['IntroActivity.onResume']['verdict'] == 'REACHABLE', rows['IntroActivity.onResume']['verdict']
assert _ir['confirmed_by'] == 'SOURCE' and _ir['source_ref'] == 'core/java/android/app/Activity.java:7098-7131', _ir
out.append(['label', 'IntroActivity.onResume', 'correct', _ir['confirmed_by'], _ir['source_ref'], '',
            'Framework method, not overridden by IntroActivity (no onResume in IntroActivity.java). Activity.performResume calls onResume at Activity.java:7107 (lines 7098-7131); '
            'performCreate calls onCreate at Activity.java:6989-6999. Incoming edge: LIFECYCLE IntroActivity.onCreate -> IntroActivity.onResume. '
            'The node is listed in methods.csv through FRAMEWORK_NODES (graph_def.py), not in method_list.json.'])

# ---- edge rows
# tools/build_graph.py reads an 'edge' row's item column as the edge id and warns if that id is not in the graph,
# so every edge row carries the real id in item and edges. A removed (suppressed) edge has no id: its row is not written
# (a warning would be wrong), and the removal is asserted above and described in the path notes and readme_notes.md.
skipped_edge_rows = []


def erow(desc, edge_id, res, conf, ref, note):
    if not edge_id:
        skipped_edge_rows.append(desc)
        return
    assert edge_id in E, edge_id
    out.append(['edge', edge_id, res, conf, ref, edge_id, '%s. %s' % (desc, note)])


for dst in ['DocumentEditAndViewFragment.newInstance', 'MoreFragment.newInstance', 'Document.<init>',
            'AppSettings.getTodoFile', 'AppSettings.getQuickNoteFile', 'DocumentEditAndViewFragment.<clinit>']:
    absent(CF, dst)
    erow('%s -> %s (AUTO, suppressed)' % (CF, dst), '', 'fixed', 'SOURCE', 'MainActivity.java:511-512, 522',
         'E1 SUPPRESS: the todo, quick note and more branches of createFragment run only for a realized tab (MainActivity.java:511-512).')
for dst in ['DocumentEditAndViewFragment.newInstance', 'Document.<init>', 'AppSettings.getTodoFile',
            'AppSettings.getQuickNoteFile', 'DocumentEditAndViewFragment.<clinit>']:
    e = has(VPS, dst, kind='CALL')
    erow('%s -> %s' % (VPS, dst), e['id'], 'fixed', cb(e), evref(e),
         'E1 realized-branch edge: runs when onViewPagerPageSelected realizes the tab (ensureRealized, MainActivity.java:446, 548-553).')
e = has(VPS, 'DocumentEditAndViewFragment.onCreate', kind='FRAMEWORK')
erow('%s -> DocumentEditAndViewFragment.onCreate' % VPS, e['id'], 'unclear', cb(e), evref(e),
     'Realized-branch framework edge: the fragment lifecycle step goes through androidx FragmentManager (not on disk; INFERRED).')
absent(VPS, 'MoreFragment.newInstance')
absent(VPS, 'MoreFragment.onViewCreated')
e = has(VPS + '@MORE', 'MoreFragment.newInstance', kind='CALL')
erow('%s@MORE -> MoreFragment.newInstance' % VPS, e['id'], 'fixed', cb(e), evref(e),
     'E1 fix: the More page is created only on the More variant, which runs when the More tab is realized (MainActivity.java:446, 519-520).')
e = has(VPS + '@MORE', 'MoreFragment.onViewCreated', kind='FRAMEWORK')
erow('%s@MORE -> MoreFragment.onViewCreated' % VPS, e['id'], 'fixed', cb(e), evref(e),
     'E1 fix (the residual edge that ran on every page change): the framework step now exists on the More variant only (MoreFragment.java:46).')

for dst in ['MoreInfoFragment.onPreferenceClicked', 'SettingsActivity$SettingsFragmentMaster.onPreferenceClicked',
            'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.onPreferenceClicked']:
    absent('GsPreferenceFragmentBase.onPreferenceTreeClick', dst)
    erow('GsPreferenceFragmentBase.onPreferenceTreeClick -> %s (lift skipped)' % dst, '', 'fixed', 'SOURCE',
         'GsPreferenceFragmentBase.java:226-320',
         'E2 receiver lift: the base method was lifted to this override; the lift edge is absent (_LIFT_SKIP).')
e = has('S_SHARE_INTO', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.onPreferenceClicked', kind='GUI')
erow('S_SHARE_INTO -> ShareIntoImportOptionsFragment.onPreferenceClicked', e['id'], 'correct', cb(e), evref(e),
     'The GUI edge into S_SHARE_INTO: the share-into preference click (line 538).')
e = has('MoreInfoFragment.onPreferenceClicked', 'SettingsActivity.<init>', kind='INTENT')
erow('MoreInfoFragment.onPreferenceClicked -> SettingsActivity.<init>', e['id'], 'correct', cb(e), evref(e),
     'The Settings intent from the More page preference (route of PasswordStore.createSecretKey).')

assert sorted({x['dst'] for x in g['edges'] if x['src'] == 'S_HOME_WIDGET_TODO'}) == ['OpenFromShortcutOrWidgetActivity.<init>']
e = has('S_HOME_WIDGET_TODO', 'OpenFromShortcutOrWidgetActivity.<init>', kind='GUI')
erow('S_HOME_WIDGET_TODO -> OpenFromShortcutOrWidgetActivity.<init> (E3 split)', e['id'], 'fixed', cb(e), evref(e),
     'E3: S_HOME_WIDGET was split into S_HOME_WIDGET_TODO and S_HOME_WIDGET_NOTEBOOK; this is the only outgoing edge of the todo state (TodoWidgetProvider.java:38-42)')

tx = [x for x in g['edges'] if x['src'] == 'DocumentEditAndViewFragment.onOptionsItemSelected'
      and 'View.postDelayed runs the Runnable' in str(x.get('trigger'))]
assert len(tx) == 1, len(tx)
assert 'opens the file browser' not in str(tx[0]['trigger']) and 'MainActivity.launch' in str(tx[0]['trigger'])
erow('DocumentEditAndViewFragment.onOptionsItemSelected -> lambda$onOptionsItemSelected$9 (text)', tx[0]['id'], 'fixed', cb(tx[0]), evref(tx[0]),
     'Text fixed: the edge said the editor menu item opens the file browser; the Runnable starts MainActivity with this file (MainActivity.launch).')
e = has('DocumentEditAndViewFragment.lambda$onOptionsItemSelected$9', 'MainActivity.launch', kind='CALL')
erow('lambda$onOptionsItemSelected$9 -> MainActivity.launch', e['id'], 'correct', cb(e), evref(e),
     'The direct call from the Runnable to MainActivity.launch (DocumentEditAndViewFragment.java:630, bytecode).')

e86 = has('SyntaxHighlighterBase.compute', 'AsciidocSyntaxHighlighter.generateSpans', kind='CALL')
assert b.edge_sourced(e86)
erow('SyntaxHighlighterBase.compute -> AsciidocSyntaxHighlighter.generateSpans', e86['id'], 'fixed', 'SOURCE', evref(e86),
     'S2 fixed: the sourced call (line 443) is state-gated by the asciidoc format. The INFERRED lift to this generator is skipped (_LIFT_SKIP).')
ekv = has('SyntaxHighlighterBase.compute', 'KeyValueSyntaxHighlighter.generateSpans', kind='CALL')
assert b.edge_sourced(ekv)
lifts = [x for x in between('SyntaxHighlighterBase.compute', 'KeyValueSyntaxHighlighter.generateSpans') if not b.edge_sourced(x)]
assert not lifts, [x['id'] for x in lifts]
erow('SyntaxHighlighterBase.compute -> KeyValueSyntaxHighlighter.generateSpans', ekv['id'], 'fixed', 'SOURCE', evref(ekv),
     'S2 fixed: the INFERRED lift to the key-value generator is removed (no unsourced edge remains). This sourced call (line 443) is state-gated by the key-value format.')

absent('StoragePermissionActivity.<init>', 'StoragePermissionActivity.onActivityResult')
erow('StoragePermissionActivity.<init> -> StoragePermissionActivity.onActivityResult (wiring skipped)', '', 'fixed', 'SOURCE',
     'GsContextUtils.java:2386-2412, 2400; StoragePermissionActivity.java:70-73',
     'S3: on API 27 the request runs ActivityCompat.requestPermissions only; the result hook needs startActivityForResult. The wiring is skipped (_CB_SKIP).')

absent('DocumentActivity.handleLaunchingIntent', 'DocumentActivity.showShareInto')
hs = between('DocumentActivity.handleLaunchingIntent@SEND', 'DocumentActivity.showShareInto')
assert len(hs) == 1 and 'another app' in str(hs[0].get('env') or ''), hs
erow('DocumentActivity.handleLaunchingIntent@SEND -> DocumentActivity.showShareInto', hs[0]['id'], 'fixed', cb(hs[0]), evref(hs[0]),
     'S4 fixed: the base edge is absent, so the in-app launch (no SEND action) cannot reach showShareInto. This gated edge stays on the SEND variant only (env: another app sends the intent).')

absent(CF, 'Document.equals')
erow('%s -> Document.equals (suppressed)' % CF, '', 'fixed', 'SOURCE', 'MainActivity.java:511-526',
     'S5: the generic createFragment -> Document.equals framework edge was removed (_CB_SKIP); Document.equals stays REACHABLE through NewFileDialog.lambda$makeDialog$13.')

e0 = has('MainActivity.onPostResume', 'GsActivityBase.onPostResume', kind='CALL')
erow('MainActivity.onPostResume -> GsActivityBase.onPostResume', e0['id'], 'correct', cb(e0), evref(e0),
     'The super call from MainActivity.onPostResume (MainActivity.java:318, bytecode).')
e4 = has('MainActivity.onPostResume', 'MainActivity.onPause', kind='LIFECYCLE')
erow('MainActivity.onPostResume -> MainActivity.onPause', e4['id'], 'fixed', cb(e4), evref(e4),
     'Pause now follows onPostResume (MainActivity.java:569-576), the order the cold start and the resume use. It replaces the stale direct MainActivity.onResume -> MainActivity.onPause edge.')
e5 = has('MainActivity.<init>', 'MainActivity.onCreate', kind='LIFECYCLE')
erow('MainActivity.<init> -> MainActivity.onCreate', e5['id'], 'fixed', cb(e5), evref(e5),
     'Cold start: the activity constructor is followed by onCreate. It replaces the stale direct MainActivity.<init> -> MainActivity.onResume shortcut.')
# removed shortcut edges have no id (asserted absent above), so they are listed as suppressed rows, not written
erow('MainActivity.<init> -> MainActivity.onResume (removed)', '', 'fixed', 'SOURCE', 'ActivityThread.java:2729-2950; Activity.java:7098-7131',
     'Suppressed: the stale shortcut is removed; onCreate runs before onResume on the cold start.')
erow('MainActivity.onResume -> MainActivity.onPause (removed)', '', 'fixed', 'SOURCE', 'MainActivity.java:569-576',
     'Suppressed: the stale direct edge is removed; onPostResume runs between them.')
erow('StoragePermissionActivity.<init> -> StoragePermissionActivity.onActivityFirstTimeVisible (removed)', '', 'fixed', 'SOURCE',
     'Activity.java:7098-7131; GsActivityBase.java:102-108',
     'Suppressed: the constructor is not a shortcut to the first-visible hook; the hook is posted from onPostResume.')
ep = has('MainActivity.onPostResume', 'MainActivity.onActivityFirstTimeVisible', kind='FRAMEWORK')
erow('MainActivity.onPostResume -> MainActivity.onActivityFirstTimeVisible (shortcut)', ep['id'], 'unclear', cb(ep), evref(ep),
     'Shortcut: this FRAMEWORK edge skips the base step GsActivityBase.onPostResume, which posts the hook through a Handler (Handler.java:355-358). Kept; the result is unclear.')

REG = has('MainActivity.onCreate', 'MainActivity.onClickFab', kind='REGISTER')
erow('MainActivity.onCreate -> MainActivity.onClickFab (listener registration)', REG['id'], 'correct', cb(REG), evref(REG),
     'The FAB listener is registered in onCreate (MainActivity.java:91). REGISTER edges are not used by route search; the tap that runs the listener is the next row.')
TAP = has('S_NOTEBOOK', 'MainActivity.onClickFab', kind='GUI')
erow('S_NOTEBOOK -> MainActivity.onClickFab (FAB tap)', TAP['id'], 'unclear', cb(TAP), evref(TAP),
     'The FAB tap from the notebook page; the listener type is not read per lambda, so the tap step is INFERRED. The stale FRAMEWORK edge from MainActivity.onCreate (E68c24288) is no longer in the graph.')

absent('GsActivityBase.onToolbarClick', 'DocumentEditAndViewFragment.onToolbarClicked')
absent('MarkorBaseActivity.onReceiveKeyPress', 'DocumentEditAndViewFragment.onReceiveKeyPress')
absent('GsFragmentBase.checkRunFirstTimeVisible', 'DocumentEditAndViewFragment.onFragmentFirstTimeVisible')
absent('GsFileBrowserListAdapter.onClick', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected')
absent('DocumentEditAndViewFragment.onOptionsItemSelected', 'WikitextTextConverter.convertMarkup')
e = has('S_TODO', 'DocumentEditAndViewFragment.onToolbarClicked', kind='GUI')
erow('S_TODO -> DocumentEditAndViewFragment.onToolbarClicked', e['id'], 'fixed', cb(e), evref(e),
     'Replaces the removed base toolbar edge (TodoTxtFilter.isStart route): the todo toolbar handler is reached by a GUI edge from the todo page.')
e = has('S_TODO', 'DocumentEditAndViewFragment.onReceiveKeyPress', kind='GUI')
erow('S_TODO -> DocumentEditAndViewFragment.onReceiveKeyPress', e['id'], 'fixed', cb(e), evref(e),
     'Replaces the removed base key edge (TextViewUtils route): the key handler is reached from the todo page by a GUI edge.')
e = has('S_QUICKNOTE', 'DocumentEditAndViewFragment.onReceiveKeyPress', kind='GUI')
erow('S_QUICKNOTE -> DocumentEditAndViewFragment.onReceiveKeyPress', e['id'], 'fixed', cb(e), evref(e),
     'Replaces the removed base key edge: the same key handler is reached from the quick note page by a GUI edge.')
e = has('GsFragmentBase.checkRunFirstTimeVisible@DocumentEditAndViewFragment', 'DocumentEditAndViewFragment.onFragmentFirstTimeVisible', kind='CALL')
erow('GsFragmentBase.checkRunFirstTimeVisible@DocumentEditAndViewFragment -> DocumentEditAndViewFragment.onFragmentFirstTimeVisible', e['id'], 'fixed', cb(e), evref(e),
     'Replaces the removed base first-visible edge (clearFixup route): the document-page variant makes the call (GsFragmentBase.java:135-140; DocumentEditAndViewFragment.java:241).')
e = has('S_DOCUMENT', 'WikitextTextConverter.convertMarkup', kind='GUI')
erow('S_DOCUMENT -> WikitextTextConverter.convertMarkup', e['id'], 'fixed', cb(e), evref(e),
     'Replaces the removed share-as-HTML base edge (wikitextPagePathToRelativeFilePath route): a GUI edge from the document page, gated by the wikitext format state (DocumentEditAndViewFragment.java:482-487).')
e = has('S_SHARE_PICKER', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected', kind='GUI')
erow('S_SHARE_PICKER -> ShareInto$1.onFsViewerSelected', e['id'], 'fixed', cb(e), evref(e),
     'Replaces the removed notebook list edge (findNotebookRootDir route): the share picker is its own GUI state (DocumentShareIntoFragment.java:466-476).')
e = has('GsActivityBase.onToolbarClick', 'GsFileBrowserFragment.onToolbarClicked', kind='CALL')
erow('GsActivityBase.onToolbarClick -> GsFileBrowserFragment.onToolbarClicked', e['id'], 'unclear', cb(e), evref(e),
     'Base-method edge: it reaches the notebook toolbar handler through the loop over the visible resumed fragments (guard on the edge, GsActivityBase.java:116-124). The isEncryptedFile route uses it.')
e = has('MarkorBaseActivity.onReceiveKeyPress', 'GsFragmentBase.onReceiveKeyPress', kind='CALL')
erow('MarkorBaseActivity.onReceiveKeyPress -> GsFragmentBase.onReceiveKeyPress', e['id'], 'unclear', cb(e), evref(e),
     'Base-method key edge, still ungated: it calls the base key handler from every page. No sampled route uses it; a hazard candidate, not fixed.')
absent('GsFileBrowserFragment.onViewCreated', 'GsFileBrowserListAdapter.onClick')
erow('GsFileBrowserFragment.onViewCreated -> GsFileBrowserListAdapter.onClick (suppressed)', '', 'fixed', 'INFERRED', '',
     'Suppressed (SUPPRESS, fix 3 family): the notebook row tap is a GUI edge from S_NOTEBOOK, entered from the resumed step (not from the fragment view creation).')
e = has('S_NOTEBOOK', 'GsFileBrowserListAdapter.onClick', kind='GUI')
erow('S_NOTEBOOK -> GsFileBrowserListAdapter.onClick (notebook row tap)', e['id'], 'fixed', cb(e), evref(e),
     'Limits item 4: the row listener is set at GsFileBrowserListAdapter.java:271 (setOnClickListener), and performClick calls it (View.java:6289-6296). The tap itself is the user action (GUI edge).')
e = has('S_NOTEBOOK', 'GsFileBrowserListAdapter.onLongClick', kind='GUI')
erow('S_NOTEBOOK -> GsFileBrowserListAdapter.onLongClick (notebook row long press)', e['id'], 'fixed', cb(e), evref(e),
     'Limits item 1: the long-press listener is set at GsFileBrowserListAdapter.java:272 and onLongClick toggles the selection (lines 562-567). This is the only route into the selection state.')
e = has('GsFileBrowserListAdapter.onLongClick', 'S_NOTEBOOK_SEL', kind='ENTERS')
erow('GsFileBrowserListAdapter.onLongClick -> S_NOTEBOOK_SEL', e['id'], 'fixed', cb(e), evref(e),
     'The selection state is entered only when the long-pressed view is the row root (GsFileBrowserListAdapter.java:563); the guard is on the edge.')
e = has('S_NOTEBOOK_SEL', 'FileInfoDialog.show', kind='GUI')
erow('S_NOTEBOOK_SEL -> FileInfoDialog.show (notebook info)', e['id'], 'fixed', cb(e), evref(e),
     'Limits item 1: the notebook info action needs a selection (guard areItemsSelected, GsFileBrowserFragment.java:457-460) and the state NEED_SELECTED. The unguarded S_NOTEBOOK menu edge to the dialog is suppressed (row below).')
absent('GsFileBrowserFragment.onOptionsItemSelected', 'FileInfoDialog.show')
erow('GsFileBrowserFragment.onOptionsItemSelected -> FileInfoDialog.show (suppressed)', '', 'fixed', 'SOURCE', 'GsFileBrowserFragment.java:457-460',
     'Suppressed: the notebook menu info action has no edge to the dialog without the selection gate (S_NOTEBOOK_SEL).')
e = has('DocumentEditAndViewFragment.onOptionsItemSelected', 'FileInfoDialog.show', kind='CALL')
erow('DocumentEditAndViewFragment.onOptionsItemSelected -> FileInfoDialog.show (todo info)', e['id'], 'fixed', cb(e), evref(e),
     'The todo page info action calls the dialog only when the save succeeds (guard read from DocumentEditAndViewFragment.java:604-606).')
e = has('AppSettings.addRecentFile', 'AppSettings.setRecentDocuments', kind='CALL')
erow('AppSettings.addRecentFile -> AppSettings.setRecentDocuments', e['id'], 'fixed', cb(e), evref(e),
     'The recent list is written only for a notebook file other than the todo and quick-note pages (AppSettings.java:396). The edge carries the state NEED_OTHER_DOC, so route search uses it only when a notebook file is open.')
e = has('GsFileBrowserListAdapter.onClick', 'MainActivity$2.onFsViewerSelected', kind='CALL')
erow('GsFileBrowserListAdapter.onClick -> MainActivity$2.onFsViewerSelected (row tap, OK button)', e['id'], 'correct', cb(e), evref(e),
     'Limits item 4: the single-file row tap (GsFileBrowserListAdapter.java:426) and the OK button (line 440) both call this listener. Dialog row taps are an accepted limit.')
e = has('DocumentEditAndViewFragment.setupSearchView', 'DocumentEditAndViewFragment$2.onQueryTextChange', kind='FRAMEWORK')
erow('DocumentEditAndViewFragment.setupSearchView -> $2.onQueryTextChange', e['id'], 'fixed', cb(e), evref(e),
     'Limits item 2: the search listener is set up only in view mode (guard at DocumentEditAndViewFragment.java:697-698); the edge carries the preview state NEED_PREVIEW.')
e = has('DocumentEditAndViewFragment$2.search', 'DocumentEditAndViewFragment$2.lambda$search$0', kind='FRAMEWORK')
erow('DocumentEditAndViewFragment$2.search -> lambda$search$0', e['id'], 'fixed', cb(e), evref(e),
     'Limits item 2: the search returns at once when the web view is null (guard at DocumentEditAndViewFragment.java:707-708).')
WIDGET_LC = [('TodoWidgetService.<init>', 'TodoWidgetService.onCreate'), ('TodoWidgetService.onCreate', 'TodoWidgetService.onBind'),
             ('TodoWidgetService.onBind', 'TodoWidgetService.onGetViewFactory'), ('WrFilesWidgetService.<init>', 'WrFilesWidgetService.onCreate'),
             ('WrFilesWidgetService.onCreate', 'WrFilesWidgetService.onBind'), ('WrFilesWidgetService.onBind', 'WrFilesWidgetService.onGetViewFactory')]
for s_, d_ in WIDGET_LC:
    e = has(s_, d_, kind='LIFECYCLE')
    erow('%s -> %s (widget service lifecycle)' % (s_, d_), e['id'], 'fixed', cb(e), evref(e),
         'Limits item 3: a widget service lifecycle step (FRAMEWORK_NODES: Service.onCreate and RemoteViewsService.onBind; ActivityThread.java:3311-3366, RemoteViewsService.java:235-244).')

e = has('S_NOTEBOOK', 'GsFileBrowserFragment.onOptionsItemSelected', kind='GUI')
erow('S_NOTEBOOK -> GsFileBrowserFragment.onOptionsItemSelected (notebook menu)', e['id'], 'fixed', cb(e), evref(e),
     'The notebook toolbar menu items from the page, after the resumed step (fix 6 order; AppCompat builds the menu after onResume is INFERRED).')
e = has('MainActivity.onPostResume', 'S_NOTEBOOK', kind='ENTERS')
erow('MainActivity.onPostResume -> S_NOTEBOOK (notebook entry)', e['id'], 'fixed', cb(e), evref(e),
     'Fix 1: the notebook page is entered from the first-visible resumed step, not from onCreate (MainActivity.java:105-106; default startup tab AppSettings.java:781).')
absent('MainActivity.onCreate', 'S_NOTEBOOK')
e = has('S_NOTEBOOK', 'GsActivityBase.onToolbarClick', kind='GUI')
erow('S_NOTEBOOK -> GsActivityBase.onToolbarClick (toolbar tap)', e['id'], 'fixed', cb(e), evref(e),
     'Fix 3: the toolbar tap is a GUI edge from the notebook page; the registration edge GsActivityBase.onResume -> onToolbarClick is removed (_REG_SKIP).')
absent('GsActivityBase.onResume', 'GsActivityBase.onToolbarClick')
e = has('S_SHARE_PICKER', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerNeutralButtonPressed', kind='GUI')
erow('S_SHARE_PICKER -> ShareIntoImportOptionsFragment$1.onFsViewerNeutralButtonPressed', e['id'], 'fixed', cb(e), evref(e),
     'The share folder browser neutral button (DocumentShareIntoFragment.java:487-489); the two dispatch edges into it are suppressed (sup).')
e = has('WrWidgetConfigure.onCreate', 'GsActivityBase.onResume@WRCONFIG', kind='LIFECYCLE')
erow('WrWidgetConfigure.onCreate -> GsActivityBase.onResume@WRCONFIG', e['id'], 'fixed', cb(e), evref(e),
     'Fix 2 (ENTERS rule): the widget folder browser is shown from the resumed step, so it is entered from this step (WrWidgetConfigure has no own onResume; MarkorBaseActivity.java has none).')
e = has('GsActivityBase.onResume@WRCONFIG', 'S_WIDGET_CONFIG', kind='ENTERS')
erow('GsActivityBase.onResume@WRCONFIG -> S_WIDGET_CONFIG', e['id'], 'fixed', cb(e), evref(e),
     'Fix 2: the widget folder browser ENTERS edge now comes from the resumed step; it replaces the direct edge from showWidgetSelectFolderDialog.')
absent('WrWidgetConfigure.showWidgetSelectFolderDialog', 'S_WIDGET_CONFIG')
erow('WrWidgetConfigure.showWidgetSelectFolderDialog -> S_WIDGET_CONFIG (removed)', '', 'fixed', 'SOURCE', 'WrWidgetConfigure.java:44, 56-58',
     'Suppressed: the direct ENTERS from onCreate-only code is removed (fix 2).')

# framework citations: host-side order for the RemoteViewsAdapter rows, then one row per FW-SRC citation
rva = open(FW + 'RemoteViewsAdapter.java', encoding='utf-8').read().splitlines()
assert 'onDataSetChanged' in rva[229] and 'updateTemporaryMetaData' in rva[245] and 'getViewTypeCount' in rva[941], (rva[229], rva[245], rva[941])
e54 = has('TodoWidgetRemoteViewsFactory.onCreate', 'TodoWidgetRemoteViewsFactory.onDataSetChanged')
erow('TodoWidgetRemoteViewsFactory.onCreate -> onDataSetChanged (host side)', e54['id'], 'correct', 'SOURCE',
     'RemoteViewsAdapter.java:228-230 (fw_src root copy)',
     'Host side, not in this edge evidence (which cites RemoteViewsService.java:140-142): the adapter calls factory.onDataSetChanged once the factory exists (RemoteViewsAdapter.java:228-230).')
e3c = has('TodoWidgetRemoteViewsFactory.onDataSetChanged', 'TodoWidgetRemoteViewsFactory.getViewTypeCount')
erow('TodoWidgetRemoteViewsFactory.onDataSetChanged -> getViewTypeCount (host side)', e3c['id'], 'correct', 'SOURCE',
     'RemoteViewsAdapter.java:246, 935-946 (fw_src root copy)',
     'Host side, not in this edge evidence (which cites RemoteViewsService.java:187): updateTemporaryMetaData runs (246) and calls factory.getViewTypeCount (942).')

cites = collections.OrderedDict()
n_fw_edges = 0
for x in g['edges']:
    segs = [s.strip() for s in (x.get('evidence') or '').split(';') if s.strip().startswith('FW-SRC')]
    if segs:
        n_fw_edges += 1
    for seg in segs:
        cites.setdefault(seg.split('(')[0].strip(), x['id'])
# Recounted after the schema-2 resume-variant and notebook-entry edges (fix 1 to fix 4). The earlier constant (74) was
# not updated when the resume-variant lifecycle and ENTERS edges (MainActivity, DocumentActivity, Settings, ActionButtonSettings,
# WrWidgetConfigure) were added. Each cited framework file is checked below, so the count is only a tripwire.
# 96 after the IntroActivity ENTERS edge began citing the framework resume (Activity.java:7098-7131).
# 97 after the LIFECYCLE edge IntroActivity.onCreate -> IntroActivity.onResume (FRAMEWORK_NODES) was added.
# 102 in round 8 (recounted after the widget service LIFECYCLE edges and the notebook, search and info edges were checked;
# the previous build is not kept, so the exact delta is not reconstructed edge by edge).
assert n_fw_edges == 102, n_fw_edges
for c, i in cites.items():
    path = c.replace('FW-SRC ', '').split(':')[0].strip()
    assert os.path.isfile(FW + path), ('framework file missing', path)
    erow('FW-SRC %s (edge %s)' % (c.replace('FW-SRC ', ''), i), i, 'correct', 'SOURCE', c.replace('FW-SRC ', ''),
         'Framework lines read in the Android 8.1.0_r1 source (fw_src): %s' % c.replace('FW-SRC ', ''))

# ---- DEVICE rows (D7): if a device run committed graphs/Markor/device/results.csv, add one row
# per results row, appended after the edge rows. Without that file the output above is unchanged
# (byte-identical); a not-reached route never becomes wrong, and no label changes.
dev_path = os.path.join(G, 'device', 'results.csv')
if os.path.isfile(dev_path):
    dev_rows = list(csv.DictReader(open(dev_path, encoding='utf-8')))
    for d in dev_rows:
        m = d['method']
        assert m in SAMPLE, ('device results row is not a sampled route', m)
        assert d['edges'].strip() == rows[m]['route_edge_ids'].strip(), ('device edges differ from route', m)
        reached = d['reached']
        assert reached in ('yes', 'no', 'not_run'), (m, reached)
        status = d['script_status']
        if reached == 'yes':
            res, note = 'correct', status
        elif status == 'unscriptable':
            res, note = 'unclear', status + ': unscriptable'
        elif status.startswith('failed') or status == 'timeout':
            res, note = 'unclear', status + ': script failed'
        elif reached == 'not_run':
            res, note = 'unclear', status + ': not run'
        else:
            res, note = 'unclear', status + ': not reached'
        out.append(['path', m, res, 'DEVICE', 'device run %s/%s' % (d['run'], d['script']), d['edges'].strip(), note])
    print('DEVICE rows', len(dev_rows))

with open(G + 'verification.csv', 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)
print('rows', len(out) - 1, sorted(collections.Counter((r[0], r[2]) for r in out[1:]).items()))
print('FW-SRC edges', n_fw_edges, 'distinct citations', len(cites), 'chain claims', chain_total)
print('edge rows not written (removed edges have no id; asserted above):', len(skipped_edge_rows))
for d in skipped_edge_rows:
    print('  -', d)
