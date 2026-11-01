#!/usr/bin/env python3
"""openlauncher route_05: CellContainer.findFreeSpace().

Method: CellContainer.findFreeSpace()
Edge ids in order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f E539087ed E93cf49d5
    Ebff6f424 E3a13d9d6 E07d7afc7 E5e9eb634 E4f315aed Ee23d816a Ee333d331
Printed route: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (CellContainer.findFreeSpace(),
    21 steps); path row of graphs/openlauncher/verification.csv;
    device/routes/openlauncher/ROUTES.csv route_05.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none. Setup: none (ROUTES.csv setup column empty).
Standard configuration: run_app.sh starts from pm clear and grants only
    the ROUTES.csv permissions (none here), so this is a first start and
    the onboarding intro is shown; the Skip tap below relies on that.

Repo-root derivation: the script lives at
device/routes/openlauncher/route_05.py, so the containing directory is
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
    "E9629945d", "E506c5f2f", "E539087ed", "E93cf49d5", "Ebff6f424",
    "E3a13d9d6", "E07d7afc7", "E5e9eb634", "E4f315aed", "Ee23d816a",
    "Ee333d331",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_05")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
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
    # E539087ed S_HOME_DESKTOP -> Desktop$DesktopAdapter$5.onLongClick:
    # long-press an empty area of the desktop page. APPROXIMATE, flagged
    # in REPORT.md: the long-click listener lives on the CellContainer
    # page layout (Desktop.java:520-535), which has no resource id, so
    # the long-press targets the desktop pager itself, res id desktop
    # (res/layout/view_home.xml:9), whose centre is the current page.
    # The trigger text says "empty area"; on a fresh install the page
    # holds only the default items, so the centre press is the closest
    # available step, not a verified empty cell.
    r.long_tap("E539087ed", res_id="desktop")
    # E93cf49d5 Desktop$DesktopAdapter$5.onLongClick -> S_HOME_EDIT: the
    # pages scale down, the edit panel appears, page touches are
    # blocked (Desktop.java:522-535). No user action.
    r.comment("long-press enters desktop edit mode", "E93cf49d5")
    # Ebff6f424 S_HOME_EDIT -> Home$$ViewBinder$4.doClick: tap "Action"
    # in the edit panel. The edit-panel TextView addLauncherAction has
    # the literal text "Action"
    # (res/layout/view_desktop_edit_option.xml; Home.java:470 binds it
    # to onViewClicked). ButterKnife dispatch is inferred.
    r.tap("Ebff6f424", text="Action")
    # E3a13d9d6 Home$$ViewBinder$4.doClick ->
    # Home.onViewClicked@ACTION: doClick calls target.onViewClicked.
    r.comment("edit-panel click calls onViewClicked", "E3a13d9d6")
    # E07d7afc7 Home.onViewClicked@ACTION -> Home.addLauncherAction:
    # addLauncherAction(view) (Home.java:482-484). No user action.
    r.comment("onViewClicked ACTION calls addLauncherAction", "E07d7afc7")
    # E5e9eb634 Home.addLauncherAction -> S_ACTION_MENU: PopupMenu.show(),
    # the menu with the single item "AppDrawer" (Home.java:491-501,
    # res/menu/launcher_action.xml:3-5). No user action.
    r.comment("PopupMenu shows the single AppDrawer item", "E5e9eb634")
    # E4f315aed S_ACTION_MENU -> Home$9.onMenuItemClick: tap "AppDrawer"
    # in the popup menu (menu item title, res/menu/launcher_action.xml).
    r.tap("E4f315aed", text="AppDrawer")
    # Ee23d816a Home$9.onMenuItemClick -> Home.onOptionsItemSelected:
    # direct call (Home.java:497). No user action.
    r.comment("menu click calls onOptionsItemSelected", "Ee23d816a")
    # Ee333d331 Home.onOptionsItemSelected ->
    # CellContainer.findFreeSpace(): direct call; onOptionsItemSelected
    # calls desktop.getCurrentPage().findFreeSpace() (Home.java:507).
    # Target edge; no further user action.
    r.comment("onOptionsItemSelected calls findFreeSpace", "Ee333d331")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
