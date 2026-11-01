#!/usr/bin/env python3
"""openlauncher route_02: AppItemView.setTargetedWidth.

Method: AppItemView.setTargetedWidth
Edge ids in order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E6c305cd5 E460ef627 E5f090eaa E9e80a447 E305d3071 E12016a69 Eeab16992
    E7a33c6e8 E0b59202a Eef712211 Eca084228 E56601e87
Printed route: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (AppItemView.setTargetedWidth,
    19 steps); path row of graphs/openlauncher/verification.csv;
    device/routes/openlauncher/ROUTES.csv route_02.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none. Setup: none (ROUTES.csv setup column empty).
Standard configuration: run_app.sh starts from pm clear and grants only
    the ROUTES.csv permissions (none here), so this is a first start and
    the onboarding intro is shown; the Skip tap below relies on that.

PRECONDITION GAP, flagged in REPORT.md: edge E12016a69 is guarded by
drawerMode == Vertical, but the default drawer mode is Paged
(LauncherSettings.java:299) and pm clear restores that default, so on a
fresh install the AppDrawerController.init branch taken is Paged, not
Vertical, and this route's target never fires. The device lead must set
the drawer style to Vertical through Settings and recreate Home before
invoking this script (or run a prior pass that leaves that setting in
place); the script itself contains no extra setup steps, because the
route contract allows exactly one block per route edge.

Repo-root derivation: the script lives at
device/routes/openlauncher/route_02.py, so the containing directory is
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
    "E9e80a447", "E305d3071", "E12016a69", "Eeab16992", "E7a33c6e8",
    "E0b59202a", "Eef712211", "Eca084228", "E56601e87",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_02")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_02", edge_ids=EDGE_IDS,
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
    # E9e80a447 Home.init -> Home.initViews: direct call.
    r.comment("Home.init calls initViews", "E9e80a447")
    # E305d3071 Home.initViews -> AppDrawerController.init: direct call
    # (Home.java:298-306, AppDrawerController.java:172-190).
    r.comment("initViews calls AppDrawerController.init", "E305d3071")
    # E12016a69 AppDrawerController.init ->
    # AppDrawer_Vertical.<init>(Context,AttributeSet): inflates
    # view_griddrawer.xml, the vertical style. PRECONDITION: this edge
    # fires only when drawerMode == Vertical
    # (AppDrawerController.java:172-190); the default is Paged, so see
    # the docstring gap note before running on a fresh install.
    r.comment("PRECONDITION: init inflates vertical drawer only if "
              "drawerMode is Vertical", "E12016a69")
    # Eeab16992 AppDrawer_Vertical.<init>(Context,AttributeSet) ->
    # AppDrawer_Vertical$1.onGlobalLayout: the first layout pass calls
    # the OnGlobalLayoutListener registered in preInit()
    # (AppDrawer_Vertical.java:63-227). No user action.
    r.comment("first layout calls OnGlobalLayoutListener", "Eeab16992")
    # E7a33c6e8 AppDrawer_Vertical$1.onGlobalLayout ->
    # AppDrawer_Vertical.init: direct call. No user action.
    r.comment("OnGlobalLayoutListener calls Vertical.init", "E7a33c6e8")
    # E0b59202a AppDrawer_Vertical.init ->
    # AppDrawer_Vertical$AppItem.getFactory: the RecyclerView shows the
    # rows and FastAdapter asks the item for getFactory. No action.
    r.comment("RecyclerView rows: FastAdapter asks getFactory",
              "E0b59202a")
    # Eef712211 AppDrawer_Vertical$AppItem.getFactory ->
    # AppDrawer_Vertical$AppItem$ItemFactory.create: FastAdapter calls
    # factory.create(view) for a new row. No user action.
    r.comment("FastAdapter calls factory.create for a new row",
              "Eef712211")
    # Eca084228 AppDrawer_Vertical$AppItem$ItemFactory.create ->
    # AppDrawer_Vertical$AppItem$ViewHolder.<init>: new ViewHolder(v).
    # No user action.
    r.comment("factory.create makes a new ViewHolder", "Eca084228")
    # E56601e87 AppDrawer_Vertical$AppItem$ViewHolder.<init> ->
    # AppItemView.setTargetedWidth: appItemView.setTargetedWidth(itemWidth)
    # (AppDrawer_Vertical.java:225). Framework/adapter construction, no
    # further user action. Target edge.
    r.comment("ViewHolder calls setTargetedWidth(itemWidth)", "E56601e87")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
