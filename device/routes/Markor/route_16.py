"""Markor route_16: MarkorContextUtils.getIntentFile(Intent).

Edge ids in order: E211966cc, Ed6414d9f, E0254b914, Ed25af8f4, Eba46a594,
E659e191c, E4850ba7b, Eb100fd9b, E5a67a199, E03c42d58, E7a697b93, E8fe5671c,
Ee0d255cd, E9904b004.
Printed route file: graphs/Markor/scratch/route_print/route_16.txt.
ROUTES.csv permissions: none. Fixtures: none (no fixture pinned for this
route; the todo widget reads the app's todo file).
Setup: push fixtures/Documents; first-run tutorial can trap a tool.
Package: net.gsantner.markor_test.

Flow: launch MainActivity, leave it to the home screen (which pauses it
and refreshes the todo widget), then tap the todo widget. Tapping the
widget container fires the pending intent to OpenFromShortcutOrWidget-
Activity (TodoWidgetProvider.java:41), which launches DocumentActivity
and reaches getIntentFile.
Caveat: a todo widget must already be placed on the home screen before
this script runs (launcher widget placement has no harness call; see
ROUTES_NOTES.md, route_16). The tap below assumes that placed widget.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "harness"))
from harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_16",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E4850ba7b", "Eb100fd9b",
                         "E5a67a199", "E03c42d58", "E7a697b93", "E8fe5671c",
                         "Ee0d255cd", "E9904b004"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E211966cc: Tap the Markor launcher icon (process start).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch("net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: system calls Application.onCreate -- no user action.
    r.comment("Application.onCreate runs by the system", "Ed6414d9f")
    # E0254b914: MAIN/LAUNCHER intent starts MainActivity -- same launch as
    # E211966cc above; no separate user action.
    r.comment("MainActivity started by the E211966cc launch", "E0254b914")
    # Ed25af8f4: system calls Activity.onCreate -- no user action.
    r.comment("Activity.onCreate runs by the system", "Ed25af8f4")
    # Eba46a594: system calls onStart then onResume -- no user action.
    r.comment("onStart/onResume run by the system", "Eba46a594")
    # E659e191c: performResume calls onPostResume -- no user action.
    r.comment("onPostResume runs by the system", "E659e191c")
    # E4850ba7b: the activity leaves the foreground (home screen).
    # MainActivity.onPause calls TodoWidgetProvider.updateTodoWidgets()
    # (MainActivity.java:569-576, call at :572).
    r.key("HOME", "E4850ba7b")
    # Eb100fd9b: direct call updateTodoWidgets -- no user action.
    r.comment("updateTodoWidgets runs from onPause", "Eb100fd9b")
    # E5a67a199: app sends ACTION_APPWIDGET_UPDATE to its own provider --
    # no user action (inside updateTodoWidgets, TodoWidgetProvider.java:52-68).
    r.comment("ACTION_APPWIDGET_UPDATE broadcast sent by the app", "E5a67a199")
    # E03c42d58: the launcher shows the todo widget -- no user action.
    r.comment("Todo widget shown by the launcher", "E03c42d58")
    # E7a697b93: Tap a todo in the todo widget list or its header.
    # The widget container carries the pending intent to
    # OpenFromShortcutOrWidgetActivity (TodoWidgetProvider.java:38-42).
    r.tap("E7a697b93", res_id="todo_widget_container")
    # E8fe5671c: system calls Activity.onCreate -- no user action.
    r.comment("Activity.onCreate runs by the system", "E8fe5671c")
    # Ee0d255cd: direct call DocumentActivity.launch -- no user action
    # (OpenFromShortcutOrWidgetActivity.java:19).
    r.comment("DocumentActivity.launch runs from onCreate", "Ee0d255cd")
    # E9904b004: direct call MarkorContextUtils.getIntentFile -- no user
    # action (DocumentActivity.java:49).
    r.comment("getIntentFile runs from DocumentActivity.launch", "E9904b004")
    r.done()


if __name__ == "__main__":
    main()
