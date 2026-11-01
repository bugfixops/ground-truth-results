#!/usr/bin/env python3
"""Markor route_13: TodoWidgetRemoteViewsFactory.getCount.

Method: TodoWidgetRemoteViewsFactory.getCount
Edge ids (in route order):
    E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c
    E4850ba7b Eb100fd9b E5a67a199 E27dc1291 E57cc7a2e E6c54174c
    E60f00f7c Ef1543024 E54993a4b E164691c4
Printed route file: graphs/Markor/scratch/route_print/route_13.txt
ROUTES.csv permissions: none.
ROUTES.csv fixtures: none (the count method runs regardless of item
    count; the todo document is read by onDataSetChanged, not by a
    pinned fixture file).
Setup (verbatim): push fixtures/Documents; first-run tutorial can trap
    a tool.
No pm clear here (run_app.sh does it) and no fixture push here
    (run_app.sh does it per ROUTES.csv).
Widget-placement caveat: the launcher-bind edge (E27dc1291) is the one
    step this harness cannot drive on its own -- placing a widget
    instance needs a launcher drag, and the harness has no drag
    primitive. The script drives everything up to that edge (launch,
    Home -> onPause -> the app's own update broadcast) and records
    the bind edge as a comment naming the precondition (a Markor todo
    widget already placed on the home screen). See REPORT.md.
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
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_13",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914",
                         "Ed25af8f4", "Eba46a594", "E659e191c",
                         "E4850ba7b", "Eb100fd9b", "E5a67a199",
                         "E27dc1291", "E57cc7a2e", "E6c54174c",
                         "E60f00f7c", "Ef1543024", "E54993a4b",
                         "E164691c4"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E211966cc: Tap the Markor launcher icon (MAIN / LAUNCHER
        # intent filter, AndroidManifest.xml:61-71).
        r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
                 edge="E211966cc")
        # Ed6414d9f: The system calls Application.onCreate.
        r.comment("system calls Application.onCreate", edge="Ed6414d9f")
        # E0254b914: MAIN / LAUNCHER intent starts MainActivity after
        # Application.onCreate on a cold start. No separate action:
        # the launch above starts it.
        r.comment("system starts MainActivity after Application.onCreate",
                  edge="E0254b914")
        # Ed25af8f4: The system calls Activity.onCreate.
        r.comment("system calls Activity.onCreate", edge="Ed25af8f4")
        # Eba46a594: The system calls Activity.onStart then onResume.
        r.comment("system calls onStart then onResume", edge="Eba46a594")
        # E659e191c: Activity.performResume calls onPostResume.
        r.comment("performResume calls onPostResume", edge="E659e191c")
        # E4850ba7b: The activity leaves the foreground. Pressing
        # Home drives onPause (MainActivity.java:569-576).
        r.key("HOME", edge="E4850ba7b")
        # Eb100fd9b: Direct call from onPause (MainActivity.java:572,
        # bytecode).
        r.comment("onPause calls updateTodoWidgets", edge="Eb100fd9b")
        # E5a67a199: The app sends ACTION_APPWIDGET_UPDATE to its own
        # provider to refresh the views (TodoWidgetProvider.java:
        # 52-68). Sent by the app itself, not by the script.
        r.comment("app sends ACTION_APPWIDGET_UPDATE to its provider",
                  edge="E5a67a199")
        # E27dc1291: SYSTEM, outside package: the launcher binds the
        # todo list service named by setRemoteAdapter
        # (TodoWidgetProvider.java:33-34; AndroidManifest.xml:125-127
        # declares TodoWidgetService with BIND_REMOTEVIEWS). This bind
        # only happens for a widget instance already placed on the
        # home screen (widget info res/xml/todo_widget.xml); placing
        # that instance needs a launcher drag, which this harness
        # cannot express (no drag primitive), so no tap is faked
        # here. With a placed widget, the Home key above plus the
        # app's own broadcast refresh it and the launcher binds the
        # service.
        r.comment("launcher binds TodoWidgetService for a placed todo "
                  "widget; placement itself is a launcher drag "
                  "outside this harness (see REPORT.md)",
                  edge="E27dc1291")
        # E57cc7a2e: The framework creates the service and calls
        # Service.onCreate (not overridden in the app).
        r.comment("framework creates service, calls onCreate",
                  edge="E57cc7a2e")
        # E6c54174c: handleBindService calls the service onBind
        # (RemoteViewsService.onBind, not overridden in the app).
        r.comment("framework calls service onBind", edge="E6c54174c")
        # E60f00f7c: RemoteViewsService.onBind calls onGetViewFactory,
        # which the app overrides (TodoWidgetService.java:8-10).
        r.comment("onBind calls onGetViewFactory", edge="E60f00f7c")
        # Ef1543024: onBind calls factory.onCreate on the new factory
        # (TodoWidgetRemoteViewsFactory.onCreate calls
        # onDataSetChanged, TodoWidgetRemoteViewsFactory.java:31-36).
        r.comment("onBind calls factory.onCreate", edge="Ef1543024")
        # E54993a4b: The launcher asks for the list data; the adapter
        # calls factory.onDataSetChanged.
        r.comment("adapter calls factory.onDataSetChanged",
                  edge="E54993a4b")
        # E164691c4: The launcher asks the adapter for the list
        # (getCount); the adapter calls factory.getCount
        # (TodoWidgetRemoteViewsFactory.java:52). Target method
        # reached.
        r.comment("adapter calls factory.getCount", edge="E164691c4")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
