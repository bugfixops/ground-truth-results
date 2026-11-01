#!/usr/bin/env python3
"""openlauncher route_04: WidgetView.<init>(Context).

Method: WidgetView.<init>(Context)
Edge ids in order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E6c305cd5 E460ef627 E5f090eaa Ea61923a1 Eee7273ff E2edd3534 Ef215f199
    E9754a764 Ec80c126c Eddbe378e Eba47afc5 Ebae97443
Printed route: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (WidgetView.<init>(Context),
    19 steps); path row of graphs/openlauncher/verification.csv;
    device/routes/openlauncher/ROUTES.csv route_04.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none. Setup: none (ROUTES.csv setup column empty).
Standard configuration: run_app.sh starts from pm clear and grants only
    the ROUTES.csv permissions (none here), so this is a first start and
    the onboarding intro is shown; the Skip tap below relies on that.

PRECONDITION GAP, flagged in REPORT.md: edge Eddbe378e fires only when
a saved WIDGET desktop item exists in desktopData.json and is read at
process start (Desktop.java:88-102). A fresh install has no such item:
first launch only adds an app-drawer button to the dock. The device
lead must first place a widget through the system picker and restart
the app before invoking this script; the script itself contains no
extra setup steps, because the route contract allows exactly one block
per route edge.

Repo-root derivation: the script lives at
device/routes/openlauncher/route_04.py, so the containing directory is
device/routes/openlauncher; three dirname steps up from that directory
reach the repo root. Four dirname calls in total counting the one that
turns __file__ into its containing directory.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a", "E23660de0",
    "E1701006d", "Ecded7dff", "E6c305cd5", "E460ef627", "E5f090eaa",
    "Ea61923a1", "Eee7273ff", "E2edd3534", "Ef215f199", "E9754a764",
    "Ec80c126c", "Eddbe378e", "Eba47afc5", "Ebae97443",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_04")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_04", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E3a1527b1 S_ENTRY -> Init.<init>: tap the OpenLauncher icon.
    # Init is the MAIN/LAUNCHER activity (AndroidManifest.xml:28-36).
    r.launch(args.package + "/.activity.Init", "E3a1527b1")
    # E996c92b8 Init.<init> -> Init.onCreate: system instantiates Init,
    # then calls onCreate. No user action.
    r.comment("system instantiates Init, then onCreate", "E996c92b8")
    # E5aa97973 Init.onCreate -> S_INTRO: first start, the three
    # onboarding pages are set up (Init.java:20-51). No user action.
    r.comment("first start: three onboarding pages set up", "E5aa97973")
    # E8b7dd43a S_INTRO -> Init.onSkipButtonPressed: tap "Skip".
    # Init.java:54 sets the skip button title from intro_skip, whose
    # value is "Skip" (res/values/strings.xml:27).
    r.tap("E8b7dd43a", text="Skip")
    # E23660de0 Init.onSkipButtonPressed -> Init.RockIt: direct call.
    r.comment("onSkipButtonPressed calls RockIt", "E23660de0")
    # E1701006d Init.RockIt -> Home.<init>: startActivity(Home) then
    # finish() (Init.java:62-70). No user action.
    r.comment("RockIt starts Home, then finishes Init", "E1701006d")
    # Ecded7dff Home.<init> -> Home.onCreate: system instantiates Home,
    # then calls onCreate. No user action.
    r.comment("system instantiates Home, then onCreate", "Ecded7dff")
    # E6c305cd5 Home.onCreate -> Home$2.doInBackground: a new AsyncTask
    # executes and LauncherSettings.readSettings runs on a worker thread
    # (Home.java:205-306). No user action.
    r.comment("AsyncTask reads settings on worker thread", "E6c305cd5")
    # E460ef627 Home$2.doInBackground -> Home$2.onPostExecute: the
    # settings are read, onPostExecute runs on the main thread.
    r.comment("settings read: onPostExecute on main thread", "E460ef627")
    # E5f090eaa Home$2.onPostExecute -> Home.init: direct call.
    r.comment("onPostExecute calls Home.init", "E5f090eaa")
    # Ea61923a1 Home.init -> AppManager.init: direct call
    # (Home.java:282, AppManager.java:86). No user action.
    r.comment("Home.init calls AppManager.init", "Ea61923a1")
    # Eee7273ff AppManager.init -> AppManager.getAllApps: direct call.
    r.comment("AppManager.init calls getAllApps", "Eee7273ff")
    # E2edd3534 AppManager.getAllApps ->
    # AppManager$AsyncGetApps.doInBackground: the worker thread lists
    # the launcher activities and applies the hidden list and an icon
    # pack (AppManager.java:101-251). No user action.
    r.comment("worker lists launcher activities", "E2edd3534")
    # Ef215f199 AppManager$AsyncGetApps.doInBackground ->
    # AppManager$AsyncGetApps.onPostExecute: the list is ready,
    # onPostExecute runs on the main thread and tells the listeners.
    r.comment("list ready: onPostExecute tells listeners", "Ef215f199")
    # E9754a764 AppManager$AsyncGetApps.onPostExecute ->
    # Home$4.onAppDeleted: virtual/interface call that can dispatch to
    # this implementation. No user action.
    r.comment("listener dispatch reaches Home$4.onAppDeleted",
              "E9754a764")
    # Ec80c126c Home$4.onAppDeleted -> Desktop.initDesktopItem: direct
    # call (Home.java:287). No user action.
    r.comment("onAppDeleted calls Desktop.initDesktopItem", "Ec80c126c")
    # Eddbe378e Desktop.initDesktopItem ->
    # ItemViewFactory.getItemView@WIDGET: the desktop builds a saved
    # WIDGET item. PRECONDITION: this edge fires only if desktopData
    # already holds a WIDGET item at a valid position, read at process
    # start (Desktop.java:88-102); see the docstring gap note.
    r.comment("PRECONDITION: desktop builds a saved WIDGET item",
              "Eddbe378e")
    # Eba47afc5 ItemViewFactory.getItemView@WIDGET ->
    # WidgetHost.onCreateView: Home.appWidgetHost.createView calls the
    # overridden onCreateView (ItemViewFactory.java:82-85). No action.
    r.comment("createView calls WidgetHost.onCreateView", "Eba47afc5")
    # Ebae97443 WidgetHost.onCreateView -> WidgetView.<init>(Context):
    # new WidgetView(context) (WidgetHost.java:16-19). Target edge; no
    # further user action.
    r.comment("onCreateView makes a new WidgetView", "Ebae97443")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
