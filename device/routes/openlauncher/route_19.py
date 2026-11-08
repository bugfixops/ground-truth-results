"""route_19: Desktop$DesktopAdapter.getItemFromCoordinate.

Method: Desktop$DesktopAdapter.getItemFromCoordinate
Edge ids (ROUTES.csv order): E3a1527b1, E996c92b8, E5aa97973, E8b7dd43a,
    E23660de0, E1701006d, Ecded7dff, E06eb37f4, E823bd16a, E0117cced,
    E9629945d, E506c5f2f, E0f6246f9, E16774099, E21693917, E59b3b06d,
    E7daec898, E40a52c15, Eb8539a54
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (route_19 section), cross-checked
    against graphs/openlauncher/verification.csv (path row route_19) and
    out/openlauncher_trigger_graph.json.
Permissions: none. Fixtures: none. Setup: none (openlauncher has no
    setup; run_app.sh does pm clear before invoking this script).

DOUBTFUL MAPPINGS (see helper REPORT.md; dry-run passes, real-run
reachability of the last steps is NOT proven):
- The "All Apps" button is a canvas-drawn custom View, not a TextView:
  AppItemView extends View (widget/AppItemView.java:33) and draws its
  label on canvas (setLabel only stores the string, :60-67); the label
  text comes from res/values/strings.xml allApps = "All Apps"
  (widget/AppItemView.java:283). uiautomator may therefore show no
  "All Apps" text node, in which case the long_tap below fails on a
  real device and the device lead must replace it with a bounds-based
  long-press from a real UI dump. The button is the dock item at x=2
  placed on first launch (activity/Home.java:264-272; type ACTION via
  widget/Desktop.java:733-740; ACTION case in
  viewutil/ItemViewFactory.java:44-54, whose readyForDrag is true).
- The drag move (E21693917) has NO harness primitive: the harness
  offers tap / long_tap / scroll_to only, and scroll_to is a vertical
  swipe to a target, not a drag of the held item over the desktop.
  That edge is therefore a comment, not a performed drag, and the
  DRAG_LOCATION events it needs may not fire on a real run. The device
  lead needs a drag primitive (input swipe from the held item across
  the desktop) before this route can be claimed reached on device.
"""

import argparse
import os
import sys
import time

# Repo-root derivation (corrected; see helper REPORT.md).
# __file__ here is device/routes/openlauncher/route_19.py, so
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

    r = Runner(package=args.package, route="route_19",
               edge_ids=["E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a",
                         "E23660de0", "E1701006d", "Ecded7dff", "E06eb37f4",
                         "E823bd16a", "E0117cced", "E9629945d", "E506c5f2f",
                         "E0f6246f9", "E16774099", "E21693917", "E59b3b06d",
                         "E7daec898", "E40a52c15", "Eb8539a54"],
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
    # Skip button title is res/values/strings.xml intro_skip = "Skip".
    r.tap(text="Skip", edge="E8b7dd43a")
    # Wall time for the asynchronous app-list load (AppManager) that
    # places the All Apps button in the dock. The harness has no sleep
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

    # E06eb37f4: Home.onCreate -> Home.onStart --
    # "onStart after onCreate". No action.
    r.comment("Home.onStart: system lifecycle after onCreate",
              edge="E06eb37f4")

    # E823bd16a: Home.onStart -> Home.onResume --
    # "onResume after onStart (first resume of this instance: the
    # splash or the desktop is built only later)". No action.
    r.comment("Home.onResume: system lifecycle after onStart",
              edge="E823bd16a")

    # E0117cced: Home.onResume -> Home.handleLauncherPause@DESKTOP --
    # "handleLauncherPause() at the first resume: desktop is not in
    # edit mode and the drawer is not visible". No action.
    r.comment("handleLauncherPause@DESKTOP: first-resume call from "
              "onResume", edge="E0117cced")

    # E9629945d: Home.handleLauncherPause@DESKTOP ->
    # GroupPopupView.dismissPopup -- "groupPopup.dismissPopup()"
    # (guard: groupPopup != null). No action.
    r.comment("GroupPopupView.dismissPopup: call from "
              "handleLauncherPause", edge="E9629945d")

    # E506c5f2f: GroupPopupView.dismissPopup -> S_HOME_DESKTOP --
    # "the popup is hidden". No action: the desktop is now shown.
    r.comment("S_HOME_DESKTOP: popup hidden, desktop shown",
              edge="E506c5f2f")

    # E0f6246f9: S_HOME_DESKTOP -> AppItemView$Builder$3.onLongClick@LAUNCHER
    # -- 'Long-press the round "All Apps" button'. DOUBTFUL: see the
    # docstring. The label string is "All Apps" (strings.xml allApps,
    # set in widget/AppItemView.java:283), but the view draws it on
    # canvas, so a real dump may carry no such text node.
    r.long_tap(text="All Apps", edge="E0f6246f9")

    # E16774099: AppItemView$Builder$3.onLongClick@LAUNCHER ->
    # S_HOME_DRAG@LAUNCHER -- "view.startDrag(...): the drag of this
    # icon starts" (guard: readyForDrag returned true; true for the
    # ACTION case, viewutil/ItemViewFactory.java:44-54). No action:
    # the long-press starts the drag.
    r.comment("S_HOME_DRAG@LAUNCHER: startDrag from the long-press; "
              "readyForDrag true for the ACTION case",
              edge="E16774099")

    # E21693917: S_HOME_DRAG@LAUNCHER -> Desktop.onDrag --
    # "Drag the item over the desktop or drop it there (DRAG_LOCATION
    # / DROP)". NOT PERFORMED: the harness has no drag primitive (see
    # docstring). A real run needs an input swipe from the held item
    # across the desktop before the following edges can fire.
    r.comment("Desktop.onDrag: drag move NOT performed -- no harness "
              "drag primitive; needs an input swipe across the desktop "
              "on a real run", edge="E21693917")

    # E59b3b06d: Desktop.onDrag -> CellContainer.peekItemAndSwap --
    # "Direct call" (widget/Desktop.java:183, DRAG_LOCATION branch).
    # No action; follows only if the drag move happens.
    r.comment("CellContainer.peekItemAndSwap: direct call from onDrag "
              "on DRAG_LOCATION", edge="E59b3b06d")

    # E7daec898: CellContainer.peekItemAndSwap ->
    # CellContainer.onItemRearrange -- "Direct call"
    # (widget/CellContainer.java:131). No action.
    r.comment("CellContainer.onItemRearrange: direct call from "
              "peekItemAndSwap", edge="E7daec898")

    # E40a52c15: CellContainer.onItemRearrange ->
    # Desktop$DesktopAdapter$2.onItemRearrange -- "Virtual/interface
    # call that can dispatch to this implementation"
    # (widget/CellContainer.java:140). No action.
    r.comment("Desktop$DesktopAdapter$2.onItemRearrange: virtual "
              "dispatch from onItemRearrange", edge="E40a52c15")

    # Eb8539a54: Desktop$DesktopAdapter$2.onItemRearrange ->
    # Desktop$DesktopAdapter.getItemFromCoordinate -- "Direct call
    # (through Desktop$DesktopAdapter.access$100)"
    # (widget/Desktop.java:466). No action; the target.
    r.comment("Desktop$DesktopAdapter.getItemFromCoordinate: direct "
              "call from onItemRearrange", edge="Eb8539a54")
    r.screenshot("route_19_done", edge="Eb8539a54")

    r.done()


if __name__ == "__main__":
    main()
