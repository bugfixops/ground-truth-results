#!/usr/bin/env python3
"""Diary route_01: DiaryWidgetUpdate.getYear.

Method: DiaryWidgetUpdate.getYear
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
    Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691
    Ede74cf66 Ed30f979f E6bfccc45 E50c0a087 E4c763149 E9433c4e1
    E18600188
Printed route: DiaryWidgetUpdate.java:169; edge list identical to
the Diary ROUTES.csv route_01 row and to diary_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none listed in ROUTES.csv. Setup: none.
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions (none here).

Mapping notes (printed source):
  - PLACEMENT PRECONDITION (logged under Ee6b8aa80, before the
    chain's launch): the Ede74cf66 guard requires at least one
    Diary widget placed — Diary.updateWidgets broadcasts
    APPWIDGET_UPDATE with the placed ids, and
    AppWidgetProvider.onReceive dispatches onUpdate only for
    those ids. Without a placed widget the tail (widget taps)
    cannot fire. The Diary widget has NO configure activity
    (res/xml/widget.xml has no android:configure), so placement
    is immediate on drop. Placement is driven through the
    launcher (system UI, which the harness dumps like any other
    foreground UI): HOME -> long-press an empty home area ->
    tap "Widgets" -> long-press-drag the "Diary" picker entry
    onto an empty home-screen cell. The long-press on empty
    space uses drag() with identical start/end points (the
    harness implements long_tap the same way, as a same-point
    swipe, but long_tap only takes node selectors, not empty
    space). The picker drag uses drag_from() from the "Diary"
    entry to the home-screen center (540, 960 on a 1080x1920
    screen; any empty cell works).
  - LAUNCHER ASSUMPTIONS (live-run uncertainties, fail loudly):
    the CI emulator's launcher is Launcher3 (long-press empty
    space opens an overview with a "Widgets" button; the widget
    picker lists entries by app label "Diary"). If the launcher
    differs, the placement steps fail loudly (node not found),
    never silently — the route is unclear, never wrong.
  - ADDTIME: menu/main.xml gives addTime showAsAction="never"
    with title @string/addTime = "Add time", so the script opens
    the overflow (desc "More options") and taps text "Add time".
  - BACKGROUND: onPause@CHANGED fires when Diary loses the
    foreground with unsaved changes; key HOME backgrounds it,
    save() runs, updateWidgets broadcasts, onReceive dispatches
    onUpdate (guard satisfied by the placed widget).
  - WIDGET TAP: the widget's prev button is res/layout/
    widget.xml id prev (ic_chevron_left). RemoteViews nodes on
    the launcher home screen carry the app's res_ids, so the tap
    uses res_id org.billthefarmer.diary:id/prev.
  - FRESH INSTALL: no diary entries exist, so getPrevEntry finds
    none and prevMonth runs (guard "no matching day in this
    month"), then getYear — the target.
  - This route was unscriptable ("widget placement via launcher
    not drivable with the delivered harness") until the harness
    gained drag/drag_from plus system-UI driving; it converts on
    those primitives.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950 '
            'Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691 '
            'Ede74cf66 Ed30f979f E6bfccc45 E50c0a087 E4c763149 E9433c4e1 '
            'E18600188').split()

COMPONENT = 'org.billthefarmer.diary/org.billthefarmer.diary.Diary'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_01', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # Ee6b8aa80 (precondition): place the Diary widget through
    # the launcher, then launch Diary (MAIN/LAUNCHER).
    r.key('HOME', 'Ee6b8aa80')
    r.drag('Ee6b8aa80', 540, 960, 540, 960, duration_ms=1500,
           why='long-press empty home area to open the Launcher3 overview')
    r.tap('Ee6b8aa80', text='Widgets')
    r.wait_for('Ee6b8aa80', text='Diary', timeout=10)
    r.drag_from('Ee6b8aa80', 540, 960, text='Diary',
                why='drop the Diary widget on an empty home-screen cell')
    r.launch(COMPONENT, 'Ee6b8aa80')
    # Edd0b9192 Diary.<init> -> Diary.onCreate: lifecycle.
    r.comment('System instantiates Diary, then onCreate', 'Edd0b9192')
    # Ee63879c9 onCreate -> onResume: lifecycle.
    r.comment('onStart -> onResume', 'Ee63879c9')
    # Ea885d6f1 onResume -> S_DIARY_VIEW: Diary visible with the
    # MarkdownView (markdown on, the default).
    r.comment('Diary visible with the MarkdownView', 'Ea885d6f1')
    # E002e1746 S_DIARY_VIEW -> onOptionsItemSelected@VIEW: open
    # the overflow (addTime is showAsAction="never") and tap
    # "Add time".
    r.tap('E002e1746', desc='More options')
    r.tap('E002e1746', text='Add time')
    # E13d2a950 onOptionsItemSelected@VIEW -> addTime: the
    # R.id.addTime switch case, no action.
    r.comment('Switch case R.id.addTime', 'E13d2a950')
    # Ec7e88adf addTime -> S_DIARY_VIEW_CHANGED: current time
    # inserted at the cursor, Cancel visible, no action.
    r.comment('Current time inserted at the cursor', 'Ec7e88adf')
    # E9b269181 S_DIARY_VIEW_CHANGED -> onPause@CHANGED: Diary
    # loses the foreground with unsaved changes (HOME key).
    r.key('HOME', 'E9b269181')
    # E519112ea onPause@CHANGED -> save(): unsaved changes are
    # saved when Diary leaves the foreground.
    r.comment('Unsaved changes saved on leaving the foreground', 'E519112ea')
    # Ec8b3376c save() -> updateWidgets: updateWidgets(text).
    r.comment('updateWidgets(text)', 'Ec8b3376c')
    # E9ddac6cd updateWidgets -> DiaryWidgetProvider.<init>@APP:
    # sendBroadcast(APPWIDGET_UPDATE, placed ids).
    r.comment('Broadcast APPWIDGET_UPDATE with the placed ids', 'E9ddac6cd')
    # Ef7699691 provider.<init>@APP -> onReceive@APP: the system
    # instantiates the manifest receiver and calls onReceive.
    r.comment('System calls onReceive on the manifest receiver', 'Ef7699691')
    # Ede74cf66 onReceive@APP -> onUpdate: super.onReceive
    # dispatches onUpdate for the placed ids (guard satisfied by
    # the placement precondition above).
    r.comment('Placed widget: onUpdate dispatched for its id', 'Ede74cf66')
    # Ed30f979f onUpdate -> S_HOME_WIDGET: updateAppWidget shows
    # the date header and entry text on the home screen.
    r.comment('Widget shown on the home screen', 'Ed30f979f')
    # E6bfccc45 S_HOME_WIDGET -> DiaryWidgetUpdate.<init>@PREV:
    # tap the prev (chevron-left) icon on the widget.
    r.tap('E6bfccc45', res_id='org.billthefarmer.diary:id/prev')
    # E50c0a087 DiaryWidgetUpdate.<init>@PREV -> onCreate@PREV:
    # lifecycle (Theme.NoDisplay activity).
    r.comment('System instantiates DiaryWidgetUpdate, then onCreate',
              'E50c0a087')
    # E4c763149 onCreate@PREV -> getPrevEntry: PREV branch.
    r.comment('PREV: getPrevEntry(stored widget date)', 'E4c763149')
    # E9433c4e1 getPrevEntry -> prevMonth: no day found, so
    # prevMonth(year, month), then recursion.
    r.comment('No day found: prevMonth(year, month)', 'E9433c4e1')
    # E18600188 prevMonth -> getYear: getYear(year). Target.
    r.comment('getYear(year)', 'E18600188')
    r.done()


if __name__ == '__main__':
    main()
