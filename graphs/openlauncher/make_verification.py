import csv, collections, glob, json, re, sys
sys.path.insert(0, 'tools')
import build_graph as b

g = json.load(open(glob.glob('graphs/openlauncher/out/*_trigger_graph.json')[0]))
E = {x['id']: x for x in g['edges']}
rows = {r['method']: r for r in csv.DictReader(open('graphs/openlauncher/out/methods.csv', encoding='utf-8'))}

LIBS = (' Steps that run through MaterialDialogs / ButterKnife / the support FragmentManager / DrawerLayout / PopupMenu / FastAdapter / RecyclerView / the support '
        'FragmentPagerAdapter / DragScrollBar rest on INFERRED claims (none of those library sources are in this dataset).')

DLG_COPY_NOTE = (
    'ERROR FOUND: the edge onSelection -> DialogUtils.copy carried env=ENV_STORAGE_FAIL, whose text is "a backup or restore step throws (the OpenLauncher folder or a '
    'data file is not readable or writable)" - the opposite of what the edge needs. copy() is called from inside the try block (DialogUtils.java:153-158 for Backup, '
    '169-173 for Restore) only when the earlier package-info lookup (and, for the 2nd/3rd call, the earlier copy calls) do NOT throw; throwing skips straight to the '
    'catch (just a Toast). The ENV-gated "throws" condition belongs, if anywhere, on the two onSelection -> page edges that follow the whole if/else (S_SETTINGS_OTHER, '
    'S_EXIT), and reading DialogUtils.java:146-182 in full shows those two guards were ALSO wrong: System.exit(1) at line 179 is outside the Restore try/catch, so it '
    'always runs for Restore whether or not the copy threw (the old guard said "and the copy did not throw"); Backup never calls exit() at all, so it always returns to '
    'S_SETTINGS_OTHER regardless of throw (the old guard said "or Restore and the copy threw"). None of the three edges actually depends on whether copy() throws - that '
    'outcome only changes which Toast is shown, which is not modelled. Fixed: dropped env=ENV_STORAGE_FAIL (and its now-unused definition) from the onSelection -> copy '
    'edge; simplified both page-edge guards to plain "item is \\"Backup\\"" / "item is \\"Restore\\"". Steps read: minibar "Launcher settings" -> SettingsActivity -> '
    'Other -> Backup/Restore dialog (ENV permission: READ_EXTERNAL_STORAGE) -> onSelection -> copy.' + LIBS)

# ---- path rows: the final sample of 27 (seed 20261025, verify_sample.py openlauncher 30), read with show_route.py --dedupe
# (a locally-patched copy, graphs/openlauncher/show_route_fixed.py, was used to work around a tools/show_route.py bug - see AGENT_NOTES.md / LESSONS.md)
P = {}
def p(m, res, ref, note):
    P[m] = (res, ref, note)

p('HideAppsFragment$2$1.onClick', 'correct', 'activity/Home.java:591-607; activity/SettingsActivity.java:41-49,302-324,364-366; fragment/HideAppsFragment.java:58-154',
  '37 steps read in full: launcher entry -> Init onboarding skip (firstStart) -> Home create/start/resume (handleLauncherPause@DESKTOP) -> minibar row "Launcher settings" -> '
  'SettingsActivity -> root -> Icons -> Hide apps -> HideAppsActivity -> ViewPager/HideAppsFragment -> AsyncWorkerList (onPreExecute/doInBackground/onPostExecute) -> list shown -> '
  'confirm FAB -> confirmSelection -> new Thread -> selected == 0 -> Snackbar "select at least one app" -> tap OK. Every guard (the AsyncTask.Status.PENDING check, the switch on the '
  'ButtonPref id, the settingsCategory switch, selected == 0) matches the source exactly.' + LIBS)
p('AppItemView.setTargetedWidth', 'correct', 'activity/Home.java:205-306; widget/AppDrawerController.java:172-190; widget/AppDrawer_Vertical.java:63-227',
  '19 steps: Home.onCreate -> AsyncTask reads LauncherSettings -> init -> initViews -> AppDrawerController.init (guard drawerMode == Vertical, STATE settings) -> inflates '
  'AppDrawer_Vertical -> first-layout OnGlobalLayoutListener -> init -> FastAdapter asks AppItem for getFactory/create -> new ViewHolder -> setTargetedWidth(itemWidth) '
  '(AppDrawer_Vertical.java:225). The STATE text matches the comment in NEED_VERTICAL exactly (style read by AppDrawerController.init at Home start).' + LIBS)
p('AppDrawerController.scrollToStart', 'correct', 'activity/Home.java:383,779-829; widget/AppDrawerController.java:115-168',
  '23 steps: desktop touch -> openAppDrawer (paged, the default style) -> Back closes the drawer (Activity.java:2886-2894,2975-2985,3001-3010) -> handleLauncherPause@DRAWER -> '
  'closeAppDrawer -> AppDrawerController.close (guard: appDrawerAnimator not null/not running, Paged) -> circular-reveal animator end -> Home$6.onEnd -> scrollToStart '
  '(Home.java:383, AppDrawerController.java:136).' + LIBS)
p('WidgetView.<init>(Context)', 'correct', 'activity/Home.java:282,287; util/AppManager.java:86,101-251; widget/Desktop.java:88-102; viewutil/ItemViewFactory.java:82-85; viewutil/WidgetHost.java:16-19',
  '19 steps, STATE data: Home.onCreate -> AsyncTask reads settings -> init -> AppManager.init/getAllApps -> AsyncGetApps (worker + onPostExecute) -> onAppDeleted -> '
  'Desktop.initDesktopItem (STATE: desktopData.json already holds a WIDGET item at a valid x/y, read at process start) -> ItemViewFactory.getItemView@WIDGET -> '
  'Home.appWidgetHost.createView -> WidgetHost.onCreateView -> new WidgetView(context) (WidgetHost.java:18).' + LIBS)
p('CellContainer.findFreeSpace()', 'correct', 'widget/Desktop.java:472-537; activity/Home.java:470-507',
  '21 steps: desktop touch -> long-press empty area -> edit mode (inEditMode=true, pages scale down) -> ButterKnife doClick for the "Action" edit-panel button -> '
  'onViewClicked@ACTION -> addLauncherAction -> support PopupMenu "AppDrawer" item -> onMenuItemClick -> onOptionsItemSelected -> '
  'desktop.getCurrentPage().findFreeSpace() (Home.java:507).' + LIBS)
p('MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.<init>', 'correct', 'activity/Home.java:194-195,585-590; widget/SwipeListView.java:42-74; widget/MiniPopupView.java:57-172',
  '16 steps: setContentView inflates <SwipeListView> (XML-instantiated view, non_standard) -> init registers a GestureDetector -> onFling (dx/dy/velocity thresholds match the '
  'source exactly) -> Home$10.onSwipe@CLEARRAM -> MiniPopupView.showActionWindow@CLEARRAM (guard action==ClearRam) -> new ClearRamViewHolder(window) -> ButterKnife.bind -> '
  'createUnbinder -> new InnerUnbinder.' + LIBS)
p('Tool.checkForUnusedIconAndDelete', 'correct', 'activity/Home.java:591-607; activity/SettingsActivity.java:41-49,302-324,341-344; util/DialogUtils.java:19-30; util/LauncherSettings.java:202',
  '27 steps: minibar "Launcher settings" -> Settings root -> Desktop -> "Desktop style" -> desktopStylePicker dialog -> onSelection -> LauncherSettings.switchDesktopMode -> '
  'Tool.checkForUnusedIconAndDelete (LauncherSettings.java:202, unconditional tail call inside switchDesktopMode).' + LIBS)
p('LauncherSettings.setPinchGesture', 'correct', 'activity/SettingsActivity.java:103,304-324,351-352; util/DialogUtils.java:79-90',
  '26 steps: minibar "Launcher settings" -> Settings root -> Gestures -> "Pinch" -> startPinchPicker single-choice dialog -> onSelection -> '
  'LauncherSettings.getInstance(context).setPinchGesture(position) (DialogUtils.java:86).' + LIBS)
p('Tool.clampInt', 'correct', 'widget/Desktop.java:160-340; widget/AppItemView.java:170-243,319-340; viewutil/GroupIconDrawable.java:77-112',
  '23 steps, STATE data (a folder on the desktop): desktop touch -> open the paged drawer -> long-press an app -> startDrag -> drop on a free desktop cell -> '
  'getItemView@APP -> onMeasure/onLayout/onDraw -> (guard: the item is a folder, icon is a GroupIconDrawable) icon.draw(canvas) -> GroupIconDrawable.draw -> the pop-animation '
  'alpha easing calls Tool.clampInt (GroupIconDrawable.java:105-110).' + LIBS)
p('GroupPopupView$6$1.hereIsTheText', 'correct', 'viewutil/ItemViewFactory.java:224-231; widget/GroupPopupView.java:87-202; util/Tool.java:463-475',
  '19 steps, STATE data (a folder exists): desktop -> tap a folder icon -> GroupPopupView.showWindowV (guard: not already showing) -> tap the folder title -> '
  'Tool.DialogHelper.promptInputText rename dialog -> type a name, OK -> Tool$DialogHelper$1.onInput -> listener.hereIsTheText (guard: str not empty, Tool.java:468-470).' + LIBS)
p('GroupIconDrawable.init', 'correct', 'widget/AppItemView.java:319-340; widget/Desktop.java:186-225,292-314; viewutil/ItemViewFactory.java:200-233,289; viewutil/GroupIconDrawable.java:36',
  '18 steps, STATE data (a folder exists): desktop -> long-press a folder icon -> startDrag -> drop on a free cell -> getItemView@GROUP (guard item.type==GROUP) -> '
  'getGroupIconDrawable -> new GroupIconDrawable(icons, iconSize) -> init(icons, size) (GroupIconDrawable.java:36).' + LIBS)
p('DialogUtils.copy', 'fixed', 'util/DialogUtils.java:140-186', DLG_COPY_NOTE)
p('Desktop$Item.newWidgetItem', 'correct', 'widget/Desktop.java:470-488; activity/Home.java:479-481,647-652,706-713,711-712,671',
  '21 steps, ENV other_app (the widget picker / its configure activity): desktop edit panel "Widget" -> pickWidget -> ACTION_APPWIDGET_PICK -> onActivityResult@CONFIGURED '
  '(RESULT_OK, REQUEST_CREATE_APPWIDGET - the cheaper of the two onActivityResult branches once a configure activity exists) -> createWidget -> Desktop.Item.newWidgetItem '
  '(Home.java:671).' + LIBS)
p('AutoFinishActivity.onCreate', 'correct', 'util/FiveSecsDelayContentProvider.java:48-87; activity/AutoFinishActivity.java:9-17; AndroidManifest.xml:56-61',
  '4 steps, ENV other_app: another app (or adb) calls delete() on the exported provider -> checkCallingPackage() (confirmed against the source: throws unless the caller is '
  'org.kustom.wallpaper or org.kustom.widget, matching ENV_KUSTOM word for word) -> last path segment "reset5secs" -> AutoFinishActivity.start -> startActivity -> onCreate '
  'calls finish() immediately.' + LIBS)
p('Tool.saveIconAndReturnID', 'correct', 'activity/Home.java:176-177,639-643; util/ShortcutReceiver.java:23-65; widget/Desktop.java:725',
  '15 steps, ENV other_app (legacy INSTALL_SHORTCUT broadcast): desktop -> ShortcutReceiver.onReceive (dynamically registered) -> Desktop.Item.newShortcutItem -> '
  'Tool.saveIconAndReturnID (Desktop.java:725).' + LIBS)
p('Home.configureWidget', 'correct', 'activity/Home.java:470-488,647-652,706-713,709-710',
  '20 steps, ENV other_app (the system widget picker): desktop edit panel "Widget" -> pickWidget -> ACTION_APPWIDGET_PICK -> onActivityResult@PICKED (RESULT_OK, '
  'REQUEST_PICK_APPWIDGET) -> configureWidget(data) (Home.java:709-710).' + LIBS)
p('DeviceAdminReceiver.onReceive', 'correct', 'AndroidManifest.xml:84-94; util/DeviceAdminReceiver.java:7-12',
  '2 steps, ENV other_app: the user activates OpenLauncher as device administrator in the system settings -> the manifest receiver DeviceAdminReceiver gets DEVICE_ADMIN_ENABLED '
  '-> onReceive (empty body, confirmed against the source).')
p('Desktop$Item.toIntent', 'correct', 'activity/Home.java:222,241,289,306-313,532; widget/AppDrawerController.java:210; widget/AppDrawer_Paged.java:123,142,172; widget/AppItemView.java:315; widget/Desktop.java:706',
  '18 steps: Home.onCreate -> settings AsyncTask -> init -> initSettings -> AppDrawerController.reloadDrawerCardTheme -> AppDrawer_Paged.resetAdapter -> new Adapter -> '
  'getItemView -> withOnLongPressDrag -> Desktop.Item.newAppItem -> toIntent (Desktop.java:706).' + LIBS)
p('Desktop$DesktopAdapter.getItemFromCoordinate', 'correct', 'widget/Desktop.java:160-231,466-497; widget/CellContainer.java:131,140; widget/AppItemView.java:319-340',
  '19 steps: desktop touch -> long-press the round "All Apps" button -> startDrag -> drag over / drop on the desktop (Desktop.onDrag) -> CellContainer.peekItemAndSwap -> '
  'onItemRearrange -> Desktop$DesktopAdapter$2.onItemRearrange (virtual dispatch) -> getItemFromCoordinate (Desktop.java:466, through access$100).' + LIBS)
p('MinibarEditActivity$Item$ViewHolder.<init>', 'correct', 'activity/Home.java:591-607; activity/MinibarEditActivity.java:36-37,57-65,131-182',
  '21 steps: minibar "Change the layout of the minibar" (pencil) -> LauncherAction.RunAction@EditMinBar -> MinibarEditActivity.onCreate -> FastAdapter rows -> '
  'Item.getType/getFactory -> ItemFactory.create -> new ViewHolder(v) (MinibarEditActivity.java:144-146,176-182).' + LIBS)
p('DialogUtils$2.onSelection', 'correct', 'activity/SettingsActivity.java:41-49,85,302-324,337-340; util/DialogUtils.java:32-50',
  '25 steps: minibar "Launcher settings" -> Settings root -> Drawer -> "Drawer style" -> appDrawerStylePicker single-choice dialog (Paged / Vertical) -> onSelection '
  '(DialogUtils.java:45-49).' + LIBS)
p('GestureAnalyser.<init>(int,int,int)', 'correct', 'activity/Home.java:205-313; widget/Desktop.java:82,346,460; in/championswimmer/sfg/lib/SimpleFingerGestures.java:44; in/championswimmer/sfg/lib/GestureAnalyser.java:74',
  '17 steps: Home.onCreate -> settings AsyncTask -> init -> initViews -> Desktop.init -> new DesktopAdapter -> getItemLayout -> new SimpleFingerGestures() -> '
  'new GestureAnalyser() -> this(3, 500, 100) (GestureAnalyser.java:74). The vendored SFG library is compiled source in this dataset (SRC, not INFERRED).' + LIBS)
p('IconLabelItem$ViewHolder.<init>', 'correct', 'activity/Home.java:591-607; activity/SettingsActivity.java:41-49,123,302-324,334-336; util/AppManager.java:114-152; viewutil/IconLabelItem.java:34-66',
  '27 steps: minibar "Launcher settings" -> Settings root -> Icons -> "Icon pack" -> AppManager.startPickIconPackIntent -> FastAdapter rows -> '
  'IconLabelItem.getType/getFactory -> ItemFactory.create -> new ViewHolder(v) (IconLabelItem.java:43,60-66).' + LIBS)
p('FiveSecsDelayContentProvider.onCreate', 'correct', 'AndroidManifest.xml:56-61; util/FiveSecsDelayContentProvider.java:19-22', '2 steps: the process installs its manifest providers before any component -> attachInfo calls onCreate (returns true).')
p('FiveSecsDelayContentProvider.<init>', 'correct', 'AndroidManifest.xml:56-61', '1 step: the process installs the provider named in the manifest.')
p('Init.onCreate', 'correct', 'AndroidManifest.xml:28-36; activity/Init.java:16-18', '2 steps: the launcher entry (MAIN+LAUNCHER) -> Init is instantiated and onCreate called.')
p('Init.<init>', 'correct', 'AndroidManifest.xml:28-36', '1 step: the launcher entry instantiates Init.')

out = [['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note']]
for m, (res, ref, note) in P.items():
    out.append(['path', m, res, 'SOURCE', ref, rows[m]['route_edge_ids'], note])

# ---- label rows: every UNREACHABLE method (172), plus the reachable methods of the sample
unre = {m for m, l in g['labels'].items() if l.get('unreachable')}
CALLERS_NOTE = ('bytecode callers outside the unreachable set checked with tools/scan_unreachable.py openlauncher --all --callers: 2 of 172 have one '
                '(Home$CallLogObserver.<init> and .onChange(boolean), called from Home.initQuickCenter and Home.onRequestPermissionsResult), both already named and explained in the reason text below.')
HAS_CALLER = {'Home$CallLogObserver.<init>', 'Home$CallLogObserver.onChange(boolean)'}
for m in sorted(unre):
    l = g['labels'][m]
    u = l['unreachable']
    note = u['text']
    if m in HAS_CALLER:
        note = note + ' ' + CALLERS_NOTE
    out.append(['label', m, 'correct', l['confirmed_by'], l['source_ref'], '', note])
assert len(unre) == 172 and HAS_CALLER <= unre

for m in P:
    if rows[m]['verdict'] != 'REACHABLE':
        continue
    sourced = all(b.edge_sourced(E[i]) for i in rows[m]['route_edge_ids'].split())
    cb = 'SOURCE' if sourced else 'INFERRED'
    out.append(['label', m, 'correct', cb, P[m][1].split(';')[0], '',
                'REACHABLE confirmed: the route to it was read step by step (path row above); ENV / STATE gates on it: env=%s state=%s' % (rows[m]['env_kinds'] or '-', rows[m]['state_kinds'] or '-')])

# ---- edge rows: the 3 edges fixed in the DialogUtils backup/restore cluster, plus one row per distinct FW-SRC citation read
seen = set()
def edge(i, res, ref, note):
    if i in seen:
        return
    seen.add(i)
    out.append(['edge', i, res, 'SOURCE', ref, '', note])

def eid(src, dst, contains=None):
    c = [x for x in g['edges'] if x['src'] == src and x['dst'] == dst and (contains is None or contains in (x.get('guard') or ''))]
    assert c, (src, dst, contains)
    return c[0]['id']

edge(eid('DialogUtils$9.onSelection', 'DialogUtils.copy'), 'fixed', 'util/DialogUtils.java:146-182', DLG_COPY_NOTE)
edge(eid('DialogUtils$9.onSelection', 'S_SETTINGS_OTHER'), 'fixed', 'util/DialogUtils.java:146-163,177-180', DLG_COPY_NOTE)
edge(eid('DialogUtils$9.onSelection', 'S_EXIT'), 'fixed', 'util/DialogUtils.java:164-180', DLG_COPY_NOTE)

# framework claims that were read (FW-SRC), one row per distinct citation (see AGENT_NOTES.md: all 28 files, ~60 citation groups, all checked, all correct)
cites = collections.OrderedDict()
for x in g['edges']:
    for seg in (x['evidence'] or '').split(';'):
        seg = seg.strip()
        if seg.startswith('FW-SRC'):
            cites.setdefault(seg.split('(')[0].strip(), x['id'])
for c, i in cites.items():
    edge(i, 'correct', c.replace('FW-SRC ', '').split(' and ')[0],
         'Lines printed from work/fw_src/android-8.1.0_r1/ and read against this claim: ' + c.replace('FW-SRC ', '') + '. Matched what the text claims (see AGENT_NOTES.md).')

with open('graphs/openlauncher/verification.csv', 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(out)
print(collections.Counter((r[0], r[2]) for r in out[1:]))
print('total rows:', len(out) - 1)
