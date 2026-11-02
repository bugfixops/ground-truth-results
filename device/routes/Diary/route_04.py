#!/usr/bin/env python3
"""Diary route_04: DiaryWidgetUpdate.nextMonth.

Method: DiaryWidgetUpdate.nextMonth
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
    Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691
    Ede74cf66 Ed30f979f Ef930bfbc E1bda1894 E4f7e2de4 E6b9a06e0
Printed route: DiaryWidgetUpdate.java:253; edge list identical to
the Diary ROUTES.csv route_04 row and to diary_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none listed in ROUTES.csv. Setup: none.
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions (none here).

Mapping notes (printed source): see route_01 for the placement
precondition (Ede74cf66 guard: at least one Diary widget placed),
the Launcher3 assumptions, the addTime overflow tap
(showAsAction="never", title "Add time"), and the HOME
backgrounding that drives save() -> updateWidgets -> broadcast ->
onReceive -> onUpdate. This route's tail mirrors route_01's with
the NEXT direction: tap the next (chevron-right) icon on the
widget (res/layout/widget.xml id next) -> DiaryWidgetUpdate
NEXT branch -> getNextEntry (none -> today) -> nextMonth.
  - FRESH INSTALL: no diary entries exist, so getNextEntry finds
    none and nextMonth runs (guard "no matching day in this
    month") — the target.
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
            'Ede74cf66 Ed30f979f Ef930bfbc E1bda1894 E4f7e2de4 '
            'E6b9a06e0').split()

COMPONENT = 'org.billthefarmer.diary/org.billthefarmer.diary.Diary'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_04', EDGE_IDS, a.log,
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
    # Ef930bfbc S_HOME_WIDGET -> DiaryWidgetUpdate.<init>@NEXT:
    # tap the next (chevron-right) icon on the widget.
    r.tap('Ef930bfbc', res_id='org.billthefarmer.diary:id/next')
    # E1bda1894 DiaryWidgetUpdate.<init>@NEXT -> onCreate@NEXT:
    # lifecycle (Theme.NoDisplay activity).
    r.comment('System instantiates DiaryWidgetUpdate, then onCreate',
              'E1bda1894')
    # E4f7e2de4 onCreate@NEXT -> getNextEntry: NEXT branch.
    r.comment('NEXT: getNextEntry(stored widget date)', 'E4f7e2de4')
    # E6b9a06e0 getNextEntry -> nextMonth: no day found, so
    # nextMonth(year, month), then recursion. Target.
    r.comment('No day found: nextMonth(year, month)', 'E6b9a06e0')
    r.done()


if __name__ == '__main__':
    main()
