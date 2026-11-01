#!/usr/bin/env python3
"""Markor route_12: WrFilesWidgetFactory.getLoadingView.

Method: WrFilesWidgetFactory.getLoadingView
Edge ids (in route order):
    E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c
    E4850ba7b E6982af1d E2681f8bd E48e0024a E3993c95d E43f11a02
    E5401b8fc Ea5c8c699 Ef25c6b36 E5c43a497
Printed route file: graphs/Markor/scratch/route_print/route_12.txt
ROUTES.csv permissions: none.
ROUTES.csv fixtures: none (the loading view is fixed; see
    WrFilesWidgetFactory.getLoadingView, which returns null).
Setup (verbatim): push fixtures/Documents; first-run tutorial can trap
    a tool.
No pm clear here (run_app.sh does it) and no fixture push here
    (run_app.sh does it per ROUTES.csv).
Widget-placement caveat: the launcher-bind edge (E48e0024a) is the one
    step this harness cannot drive on its own -- placing a widget
    instance needs a launcher drag, and the harness has no drag
    primitive. The script drives everything up to that edge (launch,
    Home -> onPause -> the app's own update broadcast) and records
    the bind edge as a comment naming the precondition (a Markor
    files widget already placed on the home screen). See REPORT.md.
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

    r = Runner(package=args.package, route="route_12",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914",
                         "Ed25af8f4", "Eba46a594", "E659e191c",
                         "E4850ba7b", "E6982af1d", "E2681f8bd",
                         "E48e0024a", "E3993c95d", "E43f11a02",
                         "E5401b8fc", "Ea5c8c699", "Ef25c6b36",
                         "E5c43a497"],
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
        # E6982af1d: Direct call from onPause (MainActivity.java:571,
        # bytecode).
        r.comment("onPause calls updateLauncherWidgets",
                  edge="E6982af1d")
        # E2681f8bd: The app sends ACTION_APPWIDGET_UPDATE to its own
        # provider to refresh the views (WrMarkorWidgetProvider
        # .java:118-134). Sent by the app itself, not by the script.
        r.comment("app sends ACTION_APPWIDGET_UPDATE to its provider",
                  edge="E2681f8bd")
        # E48e0024a: SYSTEM, outside package: the launcher binds the
        # notebook list service named by setRemoteAdapter
        # (WrMarkorWidgetProvider.java:98-104; AndroidManifest
        # .xml:110-112 declares WrFilesWidgetService with
        # BIND_REMOTEVIEWS). This bind only happens for a widget
        # instance already placed on the home screen (widget info
        # res/xml/markor_widget.xml, configure activity
        # WrWidgetConfigure); placing that instance needs a launcher
        # drag, which this harness cannot express (no drag
        # primitive), so no tap is faked here. With a placed widget,
        # the Home key above plus the app's own broadcast refresh it
        # and the launcher binds the service.
        r.comment("launcher binds WrFilesWidgetService for a placed "
                  "files widget; placement itself is a launcher drag "
                  "outside this harness (see REPORT.md)",
                  edge="E48e0024a")
        # E3993c95d: The framework creates the service and calls
        # Service.onCreate (not overridden in the app).
        r.comment("framework creates service, calls onCreate",
                  edge="E3993c95d")
        # E43f11a02: handleBindService calls the service onBind
        # (RemoteViewsService.onBind, not overridden in the app).
        r.comment("framework calls service onBind", edge="E43f11a02")
        # E5401b8fc: RemoteViewsService.onBind calls onGetViewFactory,
        # which the app overrides (WrFilesWidgetService.java:17-19).
        r.comment("onBind calls onGetViewFactory", edge="E5401b8fc")
        # Ea5c8c699: onBind calls factory.onCreate on the new factory.
        r.comment("onBind calls factory.onCreate", edge="Ea5c8c699")
        # Ef25c6b36: The launcher asks for the list data; the adapter
        # calls factory.onDataSetChanged (WrFilesWidgetFactory
        # .java:43-48).
        r.comment("adapter calls factory.onDataSetChanged",
                  edge="Ef25c6b36")
        # E5c43a497: The launcher asks the adapter for the list
        # (getLoadingView); the adapter calls factory.getLoadingView
        # (WrFilesWidgetFactory.java:95). Target method reached.
        r.comment("adapter calls factory.getLoadingView",
                  edge="E5c43a497")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
