#!/usr/bin/env python3
"""openlauncher route_03: AppDrawerController.scrollToStart.

Method: AppDrawerController.scrollToStart
Edge ids in order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f Ea422d5c6 E4547b4f3
    Ebd6b113a E0a3a55aa E7732f135 E53edad65 E6a4724e2 Ecfe22197 E1114aadb
    E34537d4a E9c94ad31
Printed route: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (AppDrawerController.scrollToStart,
    23 steps); path row of graphs/openlauncher/verification.csv;
    device/routes/openlauncher/ROUTES.csv route_03.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none. Setup: none (ROUTES.csv setup column empty).
Standard configuration: run_app.sh starts from pm clear and grants only
    the ROUTES.csv permissions (none here), so this is a first start and
    the onboarding intro is shown; the Skip tap below relies on that.

Repo-root derivation: the script lives at
device/routes/openlauncher/route_03.py, so the containing directory is
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
    "E1701006d", "Ecded7dff", "E06eb37f4", "E823bd16a", "E0117cced",
    "E9629945d", "E506c5f2f", "Ea422d5c6", "E4547b4f3", "Ebd6b113a",
    "E0a3a55aa", "E7732f135", "E53edad65", "E6a4724e2", "Ecfe22197",
    "E1114aadb", "E34537d4a", "E9c94ad31",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
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
    # E06eb37f4 Home.onCreate -> Home.onStart: onStart after onCreate.
    r.comment("onStart after onCreate", "E06eb37f4")
    # E823bd16a Home.onStart -> Home.onResume: onResume after onStart.
    r.comment("onResume after onStart", "E823bd16a")
    # E0117cced Home.onResume -> Home.handleLauncherPause@DESKTOP:
    # handleLauncherPause at the first resume (desktop not in edit mode,
    # drawer not visible). No user action.
    r.comment("first resume: handleLauncherPause, desktop state",
              "E0117cced")
    # E9629945d Home.handleLauncherPause@DESKTOP ->
    # GroupPopupView.dismissPopup: groupPopup.dismissPopup().
    r.comment("handleLauncherPause dismisses the group popup",
              "E9629945d")
    # E506c5f2f GroupPopupView.dismissPopup -> S_HOME_DESKTOP: the popup
    # is hidden. No user action.
    r.comment("popup hidden: desktop state reached", "E506c5f2f")
    # Ea422d5c6 S_HOME_DESKTOP -> Desktop$DesktopAdapter$3.onTouch:
    # touch the desktop page. APPROXIMATE, flagged in REPORT.md: the
    # page touch listener lives on the CellContainer page layout
    # (Desktop.java:473-497), which has no resource id, so the tap
    # targets the desktop pager itself, res id desktop
    # (res/layout/view_home.xml:9), whose centre is the current page.
    # The following edge additionally needs a swipe-up of over 150 px
    # with the swipe setting enabled (Desktop.java:486-491), while that
    # setting defaults to false (LauncherSettings.java:283); a plain
    # tap does not satisfy that branch, and the harness has no swipe
    # primitive. This tap is the closest harness step, not a guarantee.
    r.tap("Ea422d5c6", res_id="desktop")
    # E4547b4f3 Desktop$DesktopAdapter$3.onTouch ->
    # Home.openAppDrawer(View,int,int): direct call on the swipe-up
    # branch (Desktop.java:491). No further user action.
    r.comment("page touch branch calls openAppDrawer", "E4547b4f3")
    # Ebd6b113a Home.openAppDrawer(View,int,int) -> S_HOME_DRAWER_PAGED:
    # the circular reveal shows the paged drawer, the default style
    # (Home.java:779-805). No user action.
    r.comment("circular reveal shows the paged drawer", "Ebd6b113a")
    # E0a3a55aa S_HOME_DRAWER_PAGED -> Home.onBackPressed@DRAWER: press
    # Back (Home.java:738-741 closes drawers and handles pause).
    r.back("E0a3a55aa")
    # E7732f135 Home.onBackPressed@DRAWER ->
    # Home.handleLauncherPause@DRAWER: handleLauncherPause(). No action.
    r.comment("Back calls handleLauncherPause", "E7732f135")
    # E53edad65 Home.handleLauncherPause@DRAWER -> Home.closeAppDrawer:
    # the drawer view is visible, so closeAppDrawer(). No user action.
    r.comment("drawer visible: closeAppDrawer called", "E53edad65")
    # E6a4724e2 Home.closeAppDrawer -> AppDrawerController.close:
    # direct call. No user action.
    r.comment("closeAppDrawer calls AppDrawerController.close",
              "E6a4724e2")
    # Ecfe22197 AppDrawerController.close ->
    # AppDrawerController$3.run: paged style, the page fades out, then
    # the end action starts the reveal animator
    # (AppDrawerController.java:148-168). No user action.
    r.comment("paged fade-out end action starts reveal animator",
              "Ecfe22197")
    # E1114aadb AppDrawerController$3.run ->
    # AppDrawerController$2.onAnimationEnd: appDrawerAnimator.start(),
    # the hide animator calls its listener. No user action.
    r.comment("hide animator calls its listener onAnimationEnd",
              "E1114aadb")
    # E34537d4a AppDrawerController$2.onAnimationEnd -> Home$6.onEnd:
    # virtual/interface call that can dispatch to this implementation.
    r.comment("animator end dispatches to Home$6.onEnd", "E34537d4a")
    # E9c94ad31 Home$6.onEnd -> AppDrawerController.scrollToStart:
    # direct call (Home.java:383, AppDrawerController.java:136).
    # Target edge; no further user action.
    r.comment("onEnd calls scrollToStart", "E9c94ad31")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
