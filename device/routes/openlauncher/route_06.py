#!/usr/bin/env python3
"""openlauncher route_06: MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.<init>.

Method: MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.<init>
Edge ids, in route order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d
    Ecded7dff E93498ba6 Ec297a09e E9cea3247 E9a03d612 E33c72cbe
    E5b7c3492 E13b0a69a Eb65c5e5a E494d6177
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt, section
    "MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.<init>".
    Edge details: graphs/openlauncher/out/openlauncher_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none (ROUTES.csv setup column empty). run_app.sh clears the
    package before this script; no permissions are granted and no
    fixtures pushed by this script.

Mapping notes (see REPORT.md for full citations):
- Launcher tap (E3a1527b1) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:28-36).
- The fling edges (E9cea3247, E9a03d612) are the route's known gap:
  the harness has no swipe or fling primitive, and the minibar can
  only be opened by a left-edge swipe (DrawerLayout, no button opens
  it). They are logged as comments stating the exact gesture, not as
  taps: tapping the ClearRam row would run the ClearRam action
  (LauncherAction.RunAction), not the swipe popup, so a tap would
  drive the wrong path. Real-mode reach of the target therefore needs
  a D2 swipe/fling primitive; the dry run below proves only the
  script contract, not the gesture.
"""

import argparse
import os
import sys

# Repo-root derivation (four dirname calls on __file__, i.e. three
# up from the script's containing directory device/routes/openlauncher):
#   __file__ -> .../device/routes/openlauncher/route_06.py
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
    "E1701006d", "Ecded7dff", "E93498ba6", "Ec297a09e", "E9cea3247",
    "E9a03d612", "E33c72cbe", "E5b7c3492", "E13b0a69a", "Eb65c5e5a",
    "E494d6177",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E3a1527b1 -- Tap the OpenLauncher icon in another launcher
        # (MAIN + LAUNCHER filter). Driven as am start.
        r.launch(args.package + "/.activity.Init", edge="E3a1527b1")

        # E996c92b8 -- The system instantiates Init, then calls
        # onCreate. Lifecycle edge: no user action.
        r.comment("system instantiates Init, then calls onCreate",
                  edge="E996c92b8")

        # E5aa97973 -- First start: the three onboarding pages are
        # set up (Init.java:20-51). Page arrival: wait for the Skip
        # button (setSkipButtonTitle(intro_skip); strings.xml
        # intro_skip = "Skip").
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

        # E93498ba6 -- setContentView inflates the layout, which names
        # <SwipeListView> (res/layout/activity_home.xml:21-30,
        # id minBar). Framework edge: no user action.
        r.comment("layout inflation creates SwipeListView (minBar)",
                  edge="E93498ba6")

        # Ec297a09e -- Direct call: SwipeListView init
        # (SwipeListView.java:33). Follows inflation; no action.
        r.comment("SwipeListView constructor calls init",
                  edge="Ec297a09e")

        # E9cea3247 -- HARNESS GAP, no action coded (see docstring):
        # the GestureDetector calls onFling when a touch ends with
        # enough velocity (SwipeListView.java:42-74; guard |dx| > 10 dp,
        # |dy| < 30 dp, velocityX > 0). Required gesture: open the
        # minibar with a left-edge swipe (DrawerLayout; minBarEnable
        # defaults true, LauncherSettings.java:316), then fling RIGHT
        # on the ClearRam row -- the 4th minibar row (index 3,
        # LauncherAction.java:33, donut icon). The row shows an icon
        # only (IconListAdapter.java:53-54: setText is commented out,
        # item_minbar.xml tv is gone), so it has no text/desc
        # selector either. A tap here would be the wrong path.
        r.comment("GAP: fling right on the ClearRam (donut) minibar row "
                  "-- needs a harness swipe/fling primitive",
                  edge="E9cea3247")

        # E9a03d612 -- onSwipeRight.onSwipe(pos, x, y) for the row:
        # the donut icon (Clear RAM) (SwipeListView.java:47-66,
        # Home.java:585-590). Follows the fling; no separate action
        # (gap-dependent on E9cea3247).
        r.comment("onSwipeRight fires for the ClearRam row (from fling)",
                  edge="E9a03d612")

        # E33c72cbe -- miniPopup.showActionWindow(Action.valueOf(label),
        # x, y) (Home.java:585-590). Follows onSwipe; no action.
        r.comment("onSwipe calls MiniPopupView.showActionWindow(ClearRam)",
                  edge="E33c72cbe")

        # E5b7c3492 -- new ClearRamViewHolder(window)
        # (MiniPopupView.java:57-60). Guard: action == ClearRam.
        # Follows showActionWindow; no user action.
        r.comment("showActionWindow builds ClearRamViewHolder",
                  edge="E5b7c3492")

        # E13b0a69a -- ButterKnife.bind(this, view) calls bind
        # (MiniPopupView.java:163-172). Framework edge: no action.
        r.comment("ClearRamViewHolder constructor calls ButterKnife.bind",
                  edge="E13b0a69a")

        # Eb65c5e5a -- bind creates the unbinder (generated ButterKnife
        # class; no source file in the dataset). No user action.
        r.comment("ViewBinder.bind creates the unbinder",
                  edge="Eb65c5e5a")

        # E494d6177 -- TARGET: createUnbinder builds the InnerUnbinder
        # (generated ButterKnife class). No user action; coverage
        # decides whether the target was reached.
        r.comment("TARGET: createUnbinder builds InnerUnbinder",
                  edge="E494d6177")
    finally:
        r.done()


if __name__ == "__main__":
    main()
