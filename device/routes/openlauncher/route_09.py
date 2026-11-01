#!/usr/bin/env python3
"""openlauncher route_09: Tool.clampInt.

Method: Tool.clampInt
Edge ids, in route order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d
    Ecded7dff E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f
    Ea422d5c6 E4547b4f3 Ebd6b113a E438efe0b Ec18431c5 E01e4a9fe
    E35454574 E1773c56e Eae170a6f Ed7e82317 E4e73e729
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt, section "Tool.clampInt".
    Edge details: graphs/openlauncher/out/openlauncher_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none (ROUTES.csv setup column empty). run_app.sh clears the
    package before this script; no permissions are granted and no
    fixtures pushed by this script.

STATE PRECONDITION -- folder on the desktop (not a fixture):
    Edge Ed7e82317 requires "a folder exists on the desktop or in the
    dock (drop one app icon on another one)". No fixture file can
    substitute for a launcher folder (ROUTES_NOTES.md). The folder
    must therefore be created by GUI drag-drop BEFORE the route's own
    steps below, in this order:
      1. Open the app drawer and long-press an app icon (drag starts).
      2. Drop it on a free desktop cell (Desktop ACTION_DROP,
         Desktop.java:186-225 -> addItemToPosition).
      3. Open the drawer again, long-press a second app icon, and
         drop it ONTO the first icon: Desktop.handleOnDropOver
         (Desktop.java:543-560) turns the target into a GROUP item
         (default name "Unnamed", strings.xml unnamed) and the folder
         icon is drawn by GroupIconDrawable.
    This preamble is documented here, not driven, for the same reason
    as the route's own drag edges: the harness has no drag primitive
    and no long-press-by-coordinate (long_tap takes only text/res_id/
    desc), and drawer/desktop app icons are canvas-drawn AppItemViews
    with no text/res_id/desc node (AppItemView.java:205-243 onDraw).
    Until a D2 drag primitive exists, neither the preamble nor the
    route's drop edges can be driven in a real run; see REPORT.md.

Mapping notes (see REPORT.md for full citations):
- Launcher tap (E3a1527b1) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:28-36).
- Desktop touch (Ea422d5c6) is a further gap: Desktop.java:483-492
  opens the drawer only on a swipe-up of more than 150 px AND only
  when generalSettings.swipe is true, which defaults to false
  (LauncherSettings.java:283). The script cannot enable that setting
  (no route edge covers the Settings toggle), and the harness has no
  swipe primitive, so a real run needs swipe enabled before it starts.
- TARGET NUANCE: GroupIconDrawable.draw calls clampInt only while
  the folder icon is animating (GroupIconDrawable.java:105-110: the
  needAnimate branch, or the alpha != 255 branch). A static folder
  icon's draw (alpha 255, needAnimate false) calls neither branch.
  The only popUp() caller is a folder tap (ItemViewFactory.java:228);
  whether the preamble folder is still animating when the route's
  draw pass runs is not established by the printed route, so the
  target's real-mode reach must be settled by coverage, not assumed
  here; see REPORT.md.
"""

import argparse
import os
import sys

# Repo-root derivation (four dirname calls on __file__, i.e. three
# up from the script's containing directory device/routes/openlauncher):
#   __file__ -> .../device/routes/openlauncher/route_09.py
#   dirname  -> .../device/routes/openlauncher
#   dirname  -> .../device/routes
#   dirname  -> .../device
#   dirname  -> .../ (repo root, which holds device/harness).
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a", "E23660de0",
    "E1701006d", "Ecded7dff", "E06eb37f4", "E823bd16a", "E0117cced",
    "E9629945d", "E506c5f2f", "Ea422d5c6", "E4547b4f3", "Ebd6b113a",
    "E438efe0b", "Ec18431c5", "E01e4a9fe", "E35454574", "E1773c56e",
    "Eae170a6f", "Ed7e82317", "E4e73e729",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_09", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # STATE PRECONDITION (see docstring): a folder must already
        # exist on the desktop or in the dock before the blocks below
        # run. It is created by GUI drag-drop (drop one app icon on
        # another); no harness call here can do that, so the preamble
        # is documentation, not an action, until a D2 drag primitive
        # exists.

        # E3a1527b1 -- Tap the OpenLauncher icon in another launcher
        # (MAIN + LAUNCHER filter). Driven as am start.
        r.launch(args.package + "/.activity.Init", edge="E3a1527b1")

        # E996c92b8 -- The system instantiates Init, then calls
        # onCreate. Lifecycle edge: no user action.
        r.comment("system instantiates Init, then calls onCreate",
                  edge="E996c92b8")

        # E5aa97973 -- First start: the three onboarding pages are
        # set up (Init.java:20-51). Page arrival: wait for the Skip
        # button (strings.xml intro_skip = "Skip").
        r.wait_for(edge="E5aa97973", text="Skip")

        # E8b7dd43a -- Tap "Skip" (Init.onSkipButtonPressed,
        # Init.java:54-60).
        r.tap(edge="E8b7dd43a", text="Skip")

        # E23660de0 -- Direct call: onSkipButtonPressed -> RockIt
        # (Init.java:59). Follows the Skip tap; no user action.
        r.comment("onSkipButtonPressed calls RockIt", edge="E23660de0")

        # E1701006d -- startActivity(new Intent(Init.this, Home.class))
        # then finish() (Init.java:62-70). Effect of the Skip tap;
        # no extra action.
        r.comment("RockIt starts Home, then finishes Init",
                  edge="E1701006d")

        # Ecded7dff -- The system instantiates Home, then calls
        # onCreate. Lifecycle edge: no user action.
        r.comment("system instantiates Home, then calls onCreate",
                  edge="Ecded7dff")

        # E06eb37f4 -- onStart after onCreate (Home.java:723-728).
        # Lifecycle edge: no user action.
        r.comment("Home onStart after onCreate", edge="E06eb37f4")

        # E823bd16a -- onResume after onStart (Home.java:743-749).
        # Lifecycle edge: no user action.
        r.comment("Home onResume after onStart", edge="E823bd16a")

        # E0117cced -- handleLauncherPause() at the first resume
        # (Home.java:747, 751-760). Follows onResume; no action.
        r.comment("first resume calls handleLauncherPause",
                  edge="E0117cced")

        # E9629945d -- groupPopup.dismissPopup() (Home.java:762-764).
        # Follows handleLauncherPause; no user action.
        r.comment("handleLauncherPause dismisses the group popup",
                  edge="E9629945d")

        # E506c5f2f -- The popup is hidden: S_HOME_DESKTOP arrival
        # (GroupPopupView.java:87-94). Page arrival: wait for the
        # desktop pager (res/layout/view_home.xml:8-9, id desktop).
        r.wait_for(edge="E506c5f2f", res_id="desktop")

        # Ea422d5c6 -- HARNESS GAP, no action coded: touch the desktop
        # page (the page touch listener remembers where the touch
        # started) (Desktop.java:473-497). The drawer opens only on
        # ACTION_UP after a swipe-up of more than 150 px AND only when
        # generalSettings.swipe is true (Desktop.java:486-491;
        # default false, LauncherSettings.java:283). The harness has
        # no swipe primitive and no route edge enables the setting,
        # so a real run needs swipe enabled beforehand; see REPORT.md.
        r.comment("GAP: swipe up on the desktop page (needs swipe=true "
                  "setting + a harness swipe primitive) to open the "
                  "app drawer", edge="Ea422d5c6")

        # E4547b4f3 -- Direct call: Home.openAppDrawer(View, int, int)
        # (Desktop.java:491, Home.java:779-805). Follows the desktop
        # touch; no separate action (gap-dependent on Ea422d5c6).
        r.comment("desktop touch calls Home.openAppDrawer",
                  edge="E4547b4f3")

        # Ebd6b113a -- The circular reveal shows the paged drawer
        # (the default style) (Home.java:779-805;
        # AppDrawerController.java:63-113, 172-183; guard drawerMode
        # == Paged, the default, LauncherSettings.java:299). Follows
        # openAppDrawer; no distinguishing dump signal exists for
        # canvas-drawn drawer items, so this is a comment, not a wait.
        r.comment("paged app drawer shown (default drawerMode)",
                  edge="Ebd6b113a")

        # E438efe0b -- HARNESS GAP, no action coded: long-press an app
        # in the paged drawer (AppItemView.java:319-340). Drawer app
        # labels are drawn on canvas (AppItemView.java:205-243
        # onDraw), so no text/res_id/desc node identifies any drawer
        # app, and long_tap takes no coordinates; a plain tap would
        # launch the app instead of starting a drag. Needs a D2
        # drag/long-press primitive; see REPORT.md.
        r.comment("GAP: long-press an app in the paged drawer -- needs "
                  "a harness drag/long-press primitive",
                  edge="E438efe0b")

        # Ec18431c5 -- view.startDrag(...): the drag of this icon
        # starts (AppItemView.java:329-332; guard readyForDrag
        # returned true). Follows the long-press; no separate action
        # (gap-dependent on E438efe0b).
        r.comment("long-press starts the icon drag",
                  edge="Ec18431c5")

        # E01e4a9fe -- HARNESS GAP, no action coded: drop the item on
        # a free cell of the desktop page (Desktop.onDrag,
        # ACTION_DROP, addItemToPosition) (Desktop.java:186-225;
        # guard: a free cell exists at the drop point). The harness
        # has no drop/drag primitive; see REPORT.md.
        r.comment("GAP: drop the dragged item on a free desktop cell "
                  "-- needs a harness drag primitive",
                  edge="E01e4a9fe")

        # E35454574 -- The measure/layout/draw pass of every
        # AppItemView shown on the desktop, dock or drawer
        # (AppItemView.java:170-177). Framework edge: no action.
        r.comment("layout pass measures the placed AppItemView",
                  edge="E35454574")

        # E1773c56e -- The layout pass follows measure
        # (AppItemView.java:199-202). Framework edge: no action.
        r.comment("layout pass lays out the AppItemView",
                  edge="E1773c56e")

        # Eae170a6f -- The draw pass follows layout
        # (AppItemView.java:204-243). Framework edge: no action.
        r.comment("draw pass draws the AppItemView",
                  edge="Eae170a6f")

        # Ed7e82317 -- icon.draw(canvas): a group icon paints itself
        # (AppItemView.java:230-241; GroupIconDrawable.java:77-112).
        # Guard: the item is a folder (icon is a GroupIconDrawable)
        # -- the preamble folder. Follows the draw pass; no action.
        r.comment("preamble folder icon draws itself "
                  "(GroupIconDrawable.draw)", edge="Ed7e82317")

        # E4e73e729 -- TARGET: the pop animation eases the alpha
        # toward 0/255 each frame (GroupIconDrawable.java:105-110).
        # No user action; coverage decides whether the target was
        # reached (see the target nuance in the docstring).
        r.comment("TARGET: folder-icon animation calls Tool.clampInt",
                  edge="E4e73e729")
    finally:
        r.done()


if __name__ == "__main__":
    main()
