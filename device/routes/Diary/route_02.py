#!/usr/bin/env python3
"""Diary route_02: DiaryWidgetProvider.getHome.

Method: DiaryWidgetProvider.getHome
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
    Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691
    Ede74cf66 E6308923b Ef07452ff E90a3fefc E2adbb115 Eeb8ea610
    Efbe8cd80
Printed route: DiaryWidgetProvider.java:225; edge list identical
to the Diary ROUTES.csv route_02 row and to
diary_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none listed in ROUTES.csv. Setup: none.
Standard configuration: run_app.sh starts from `pm clear` and grants
only the ROUTES.csv permissions (none here).

Mapping notes (printed source): see route_01 for the placement
precondition (Ede74cf66 guard: at least one Diary widget placed),
the Launcher3 assumptions, the addTime overflow tap
(showAsAction="never", title "Add time"), and the HOME
backgrounding that drives save() -> updateWidgets -> broadcast ->
onReceive -> onUpdate. This route differs from route_01 in its
tail: the target fires DURING onUpdate itself (getText ->
getFile -> getDay -> getMonth -> getYear -> getHome, path
construction that runs regardless of whether an entry file
exists), so NO widget tap is needed after the broadcast.
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
            'Ede74cf66 E6308923b Ef07452ff E90a3fefc E2adbb115 Eeb8ea610 '
            'Efbe8cd80').split()

COMPONENT = 'org.billthefarmer.diary/org.billthefarmer.diary.Diary'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_02', EDGE_IDS, a.log,
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
    # E6308923b onUpdate -> getText: text = getText(context),
    # the entry of the widget date.
    r.comment('getText(context): entry of the widget date', 'E6308923b')
    # Ef07452ff getText -> getFile(Calendar): getFile(entry).
    r.comment('getFile(entry)', 'Ef07452ff')
    # E90a3fefc getFile(Calendar) -> getDay: getDay(y, m, d).
    r.comment('getDay(y, m, d)', 'E90a3fefc')
    # E2adbb115 getDay -> getMonth: getMonth(y, m); DD.txt or DD.md.
    r.comment('getMonth(y, m)', 'E2adbb115')
    # Eeb8ea610 getMonth -> getYear: new File(getYear(y), MM).
    r.comment('new File(getYear(y), MM)', 'Eeb8ea610')
    # Efbe8cd80 getYear -> getHome: new File(getHome(), YYYY).
    # Target.
    r.comment('new File(getHome(), YYYY)', 'Efbe8cd80')
    r.done()


if __name__ == '__main__':
    main()
