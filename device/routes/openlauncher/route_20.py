"""route_20: MinibarEditActivity$Item$ViewHolder.<init>.

Method: MinibarEditActivity$Item$ViewHolder.<init>
Edge ids (ROUTES.csv order): E3a1527b1, E996c92b8, E5aa97973, E8b7dd43a,
    E23660de0, E1701006d, Ecded7dff, E06eb37f4, E823bd16a, E0117cced,
    E9629945d, E506c5f2f, E2b9b86b1, Ecb7f915c, E738b5300, E2cb91242,
    E965027f2, Ea04b419a, E8b4ede1f, Ed0d4c000, E5ba6f68e
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (route_20 section), cross-checked
    against graphs/openlauncher/verification.csv (path row route_20) and
    out/openlauncher_trigger_graph.json.
Permissions: none. Fixtures: none. Setup: none (openlauncher has no
    setup; run_app.sh does pm clear before invoking this script).

DOUBTFUL MAPPINGS (see helper REPORT.md; dry-run passes, real-run
reachability of the minibar steps is NOT proven):
- The left-edge swipe that opens the minibar (E2b9b86b1) has NO
  harness primitive: the harness offers tap / long_tap / scroll_to
  only, and scroll_to is a vertical swipe to a target, not a swipe in
  from the left screen edge. That edge is therefore a comment plus a
  UI dump, not a performed swipe. The device lead needs a swipe
  primitive (input swipe from the left edge) before the minibar rows
  can be reached on device.
- The minibar row tap (E738b5300) uses res_id "iv" as a first-match
  tap: minibar rows carry no text at all (viewutil/IconListAdapter.java
  getView leaves the label TextView unset -- the setText line is
  commented out -- and only sets the icon ImageView, res/layout/
  item_minbar.xml id "iv"), and rows have no content-desc. Rows are
  built in LauncherAction.actionItems order (activity/Home.java:
  551-584), whose first item is EditMinBar (util/LauncherAction.java:
  30, label res/values/strings.xml minibar_0 = "Change the layout of
  the minibar."), so the first "iv" node in dump order should be the
  EditMinBar row. That first-match assumption is unverified against a
  real dump.
"""

import argparse
import os
import sys
import time

# Repo-root derivation (corrected; see helper REPORT.md).
# __file__ here is device/routes/openlauncher/route_20.py, so
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

    r = Runner(package=args.package, route="route_20",
               edge_ids=["E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a",
                         "E23660de0", "E1701006d", "Ecded7dff", "E06eb37f4",
                         "E823bd16a", "E0117cced", "E9629945d", "E506c5f2f",
                         "E2b9b86b1", "Ecb7f915c", "E738b5300", "E2cb91242",
                         "E965027f2", "Ea04b419a", "E8b4ede1f", "Ed0d4c000",
                         "E5ba6f68e"],
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
    # Wall time for the asynchronous loads (Home$2 settings AsyncTask,
    # AppManager app list). The harness has no sleep primitive, so
    # stdlib time is used; it logs no step line.
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

    # E2b9b86b1: S_HOME_DESKTOP -> Home.onDrawerStateChanged --
    # "Swipe in from the left screen edge: the DrawerLayout starts to
    # move and settles open" (guard: generalSettings.minBarEnable is
    # true, the default; otherwise the drawer is locked closed --
    # activity/Home.java:544). NOT PERFORMED: no harness swipe
    # primitive (see docstring). The dump is saved so the device lead
    # can confirm the drawer state on a real run.
    r.comment("Home.onDrawerStateChanged: left-edge swipe NOT "
              "performed -- no harness swipe primitive; needs an input "
              "swipe from the left edge on a real run",
              edge="E2b9b86b1")
    r.dump_ui("route_20_minibar_closed", edge="E2b9b86b1")

    # Ecb7f915c: Home.onDrawerStateChanged -> S_HOME_MINIBAR --
    # "STATE_IDLE with the left drawer open: the overlay layout is
    # shown and the minibar is open" (guard: newState == STATE_IDLE
    # and drawerLayout.isDrawerOpen(Gravity.LEFT)). No action; follows
    # only if the swipe above happens.
    r.comment("S_HOME_MINIBAR: minibar open at STATE_IDLE with the "
              "left drawer open", edge="Ecb7f915c")

    # E738b5300: S_HOME_MINIBAR -> Home$11.onItemClick@EditMinBar --
    # 'Tap the pencil icon in the minibar ("Change the layout of the
    # minibar")' (guard: the row is enabled; all eight are by
    # default). DOUBTFUL first-match tap: see docstring. Rows have no
    # text, so the row icon id "iv" is the only selector, and the
    # first "iv" node should be the first row, EditMinBar.
    r.tap(res_id="iv", edge="E738b5300")

    # E2cb91242: Home$11.onItemClick@EditMinBar ->
    # LauncherAction.RunAction@EditMinBar --
    # "LauncherAction.RunAction(action, Home.this)". No action.
    r.comment("LauncherAction.RunAction@EditMinBar: direct call from "
              "the minibar item click", edge="E2cb91242")

    # E965027f2: LauncherAction.RunAction@EditMinBar ->
    # MinibarEditActivity.onCreate -- "the system creates
    # MinibarEditActivity, then calls onCreate". No action.
    r.comment("MinibarEditActivity.onCreate: system lifecycle after "
              "RunAction", edge="E965027f2")

    # Ea04b419a: MinibarEditActivity.onCreate ->
    # MinibarEditActivity$Item.getType -- "rv.setAdapter(adapter):
    # FastAdapter shows the 8 rows". No action.
    r.comment("MinibarEditActivity$Item.getType: FastAdapter shows "
              "the 8 rows", edge="Ea04b419a")

    # E8b4ede1f: MinibarEditActivity$Item.getType ->
    # MinibarEditActivity$Item.getFactory -- "FastAdapter asks the item
    # for getFactory". No action.
    r.comment("MinibarEditActivity$Item.getFactory: FastAdapter asks "
              "for the factory", edge="E8b4ede1f")

    # Ed0d4c000: MinibarEditActivity$Item.getFactory ->
    # MinibarEditActivity$Item$ItemFactory.create -- "FastAdapter calls
    # factory.create(view) for a new row". No action.
    r.comment("MinibarEditActivity$Item$ItemFactory.create: "
              "FastAdapter creates a row", edge="Ed0d4c000")

    # E5ba6f68e: MinibarEditActivity$Item$ItemFactory.create ->
    # MinibarEditActivity$Item$ViewHolder.<init> -- "new ViewHolder(v)"
    # (activity/MinibarEditActivity.java:144-146,176-182). No action;
    # the target.
    r.comment("MinibarEditActivity$Item$ViewHolder init: new "
              "ViewHolder(v) from the factory", edge="E5ba6f68e")
    r.screenshot("route_20_done", edge="E5ba6f68e")

    r.done()


if __name__ == "__main__":
    main()
