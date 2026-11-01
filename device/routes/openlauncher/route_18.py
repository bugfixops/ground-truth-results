"""route_18: Desktop$Item.toIntent.

Method: Desktop$Item.toIntent
Edge ids (ROUTES.csv order): E3a1527b1, E996c92b8, E5aa97973, E8b7dd43a,
    E23660de0, E1701006d, Ecded7dff, E6c305cd5, E460ef627, E5f090eaa,
    E7f91bef8, Ee4fe3bad, E738e28fe, E2aa80503, E02311481, Ee2225032,
    Eda1a05dc, Ecf3c9ee7
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (route_18 section), cross-checked
    against graphs/openlauncher/verification.csv (path row route_18) and
    out/openlauncher_trigger_graph.json.
Permissions: none. Fixtures: none. Setup: none (openlauncher has no
    setup; run_app.sh does pm clear before invoking this script).

Why this route needs no drawer tap: toIntent runs while the paged
drawer pages are built, not on a tap. AppDrawer_Paged$Adapter builds
every page eagerly in its constructor (widget/AppDrawer_Paged.java:
123-172), each cell calls withOnLongPressDrag(app, ...), and that
overload calls Desktop$Item.newAppItem(app) (widget/AppItemView.java:
314-315), which calls toIntent (widget/Desktop.java:706). The drawer
mode default is Paged (util/LauncherSettings.java:299), so the
reloadDrawerCardTheme -> resetAdapter chain below reaches it. The
script waits after Skip because the settings load (Home$2 AsyncTask)
and the app-list load (AppManager) are asynchronous.
"""

import argparse
import os
import sys
import time

# Repo-root derivation (corrected; see helper REPORT.md).
# __file__ here is device/routes/openlauncher/route_18.py, so
# dirname(abspath(__file__)) is device/routes/openlauncher/ and three
# further dirnames give routes -> device -> the repo root. Three
# dirnames from __file__ itself would land on device/ and the import
# below would fail (verified from a sibling helper's failure).
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_18",
               edge_ids=["E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a",
                         "E23660de0", "E1701006d", "Ecded7dff", "E6c305cd5",
                         "E460ef627", "E5f090eaa", "E7f91bef8", "Ee4fe3bad",
                         "E738e28fe", "E2aa80503", "E02311481", "Ee2225032",
                         "Eda1a05dc", "Ecf3c9ee7"],
               log_path=args.log, dry_run=args.dry_run,
               adb=args.adb, outdir=args.outdir)

    # E3a1527b1: S_ENTRY -> Init.<init> --
    # "Tap the OpenLauncher icon in another launcher (MAIN + LAUNCHER
    # filter), or adb monkey / am start". Launch the MAIN/LAUNCHER
    # activity directly (manifest AndroidManifest.xml:28-36).
    r.launch("%s/.activity.Init" % args.package, edge="E3a1527b1")

    # E996c92b8: Init.<init> -> Init.onCreate --
    # "The system instantiates Init, then calls onCreate". No action.
    r.comment("Init.onCreate: system lifecycle after launch",
              edge="E996c92b8")

    # E5aa97973: Init.onCreate -> S_INTRO --
    # "First start: the three onboarding pages are set up"
    # (guard: firstStart true, the default on a fresh install after
    # pm clear; activity/Init.java:20-51). No action: pages appear.
    r.comment("S_INTRO: three onboarding pages shown on first start",
              edge="E5aa97973")

    # E8b7dd43a: S_INTRO -> Init.onSkipButtonPressed -- Tap "Skip".
    # Skip button title is res/values/strings.xml intro_skip = "Skip"
    # (activity/Init.java: setSkipButtonTitle).
    r.tap(text="Skip", edge="E8b7dd43a")
    # Wall time for the asynchronous loads below (Home$2 settings
    # AsyncTask, AppManager app list). The harness has no sleep
    # primitive, so stdlib time is used; it logs no step line.
    time.sleep(5)

    # E23660de0: Init.onSkipButtonPressed -> Init.RockIt --
    # "Direct call". No action.
    r.comment("Init.RockIt: direct call from onSkipButtonPressed",
              edge="E23660de0")

    # E1701006d: Init.RockIt -> Home.<init> --
    # "startActivity(new Intent(Init.this, Home.class)) then finish()".
    # No action: system starts Home.
    r.comment("Home started by RockIt intent; Init finishes",
              edge="E1701006d")

    # Ecded7dff: Home.<init> -> Home.onCreate --
    # "The system instantiates Home, then calls onCreate". No action;
    # wait until the Home layout is present (res/layout/view_home.xml
    # id "desktop").
    r.comment("Home.onCreate: system lifecycle after RockIt",
              edge="Ecded7dff")
    r.wait_for(res_id="desktop", edge="Ecded7dff")

    # E6c305cd5: Home.onCreate -> Home$2.doInBackground --
    # "new AsyncTask().execute(): LauncherSettings.readSettings runs on
    # a worker thread" (guard: LauncherSettings.init is false). No
    # action: the AsyncTask runs on its own.
    r.comment("Home$2.doInBackground: settings read on worker thread",
              edge="E6c305cd5")

    # E460ef627: Home$2.doInBackground -> Home$2.onPostExecute --
    # "the settings are read: onPostExecute runs on the main thread".
    # No action.
    r.comment("Home$2.onPostExecute: settings read, main thread",
              edge="E460ef627")

    # E5f090eaa: Home$2.onPostExecute -> Home.init --
    # "Direct call (through Home.access$200)". No action.
    r.comment("Home.init: direct call from onPostExecute",
              edge="E5f090eaa")

    # E7f91bef8: Home.init -> Home.initSettings --
    # "Direct call". No action.
    r.comment("Home.initSettings: direct call from Home.init",
              edge="E7f91bef8")

    # Ee4fe3bad: Home.initSettings -> AppDrawerController.reloadDrawerCardTheme
    # -- "Direct call". No action.
    r.comment("reloadDrawerCardTheme: direct call from initSettings",
              edge="Ee4fe3bad")

    # E738e28fe: AppDrawerController.reloadDrawerCardTheme ->
    # AppDrawer_Paged.resetAdapter -- "Direct call" (Paged branch, the
    # default drawer mode). No action.
    r.comment("AppDrawer_Paged.resetAdapter: Paged branch of "
              "reloadDrawerCardTheme", edge="E738e28fe")

    # E2aa80503: AppDrawer_Paged.resetAdapter ->
    # AppDrawer_Paged$Adapter.<init> -- "Direct call". No action.
    r.comment("AppDrawer_Paged$Adapter init: direct call from "
              "resetAdapter", edge="E2aa80503")

    # E02311481: AppDrawer_Paged$Adapter.<init> ->
    # AppDrawer_Paged$Adapter.getItemView -- "Direct call". The
    # constructor builds every page cell eagerly. No action.
    r.comment("Adapter.getItemView: direct call while building pages",
              edge="E02311481")

    # Ee2225032: AppDrawer_Paged$Adapter.getItemView ->
    # AppItemView$Builder.withOnLongPressDrag(App,Action,LongPressCallBack)
    # -- "Direct call". This only registers the long-press listener;
    # the user long-press is NOT needed for toIntent. No action.
    r.comment("withOnLongPressDrag: direct call from getItemView; "
              "listener registered, no user press needed",
              edge="Ee2225032")

    # Eda1a05dc: AppItemView$Builder.withOnLongPressDrag(App,...) ->
    # Desktop$Item.newAppItem -- "Direct call" (the App overload calls
    # newAppItem; widget/AppItemView.java:314-315). No action.
    r.comment("Desktop$Item.newAppItem: direct call from the "
              "withOnLongPressDrag App overload", edge="Eda1a05dc")

    # Ecf3c9ee7: Desktop$Item.newAppItem -> Desktop$Item.toIntent --
    # "Direct call" (widget/Desktop.java:706). No action; the target
    # has run by the time the drawer pages are built.
    r.comment("Desktop$Item.toIntent: direct call from newAppItem",
              edge="Ecf3c9ee7")
    r.screenshot("route_18_done", edge="Ecf3c9ee7")

    r.done()


if __name__ == "__main__":
    main()
