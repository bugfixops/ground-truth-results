"""route_21: DialogUtils$2.onSelection.

Method: DialogUtils$2.onSelection
Edge ids (ROUTES.csv order): E3a1527b1, E996c92b8, E5aa97973, E8b7dd43a,
    E23660de0, E1701006d, Ecded7dff, E06eb37f4, E823bd16a, E0117cced,
    E9629945d, E506c5f2f, E2b9b86b1, Ecb7f915c, Ee8ace45b, Ebf800b8a,
    Ebd0c7205, Ee3b2c4ce, E7ef50d09, E4a1f474b, E2e80d75b, Ef5eeab0d,
    E0b40304d, E4df174f1, Ea728a24e
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (route_21 section), cross-checked
    against graphs/openlauncher/verification.csv (path row route_21) and
    out/openlauncher_trigger_graph.json.
Permissions: none. Fixtures: none. Setup: none (openlauncher has no
    setup; run_app.sh does pm clear before invoking this script).

DOUBTFUL MAPPINGS (see helper REPORT.md; dry-run passes, real-run
reachability of the flagged steps is NOT proven):
- The left-edge swipe that opens the minibar (E2b9b86b1) has NO
  harness primitive (tap / long_tap / scroll_to only; scroll_to is a
  vertical swipe to a target). It is a comment plus a UI dump, not a
  performed swipe; the device lead needs a swipe primitive.
- The LauncherSettings minibar row (Ee8ace45b) CANNOT be selected
  with any harness selector, so no tap is attempted for it (tapping
  the wrong row would be fake progress). Minibar rows carry no text
  (viewutil/IconListAdapter.java getView leaves the label TextView
  unset -- the setText line is commented out -- and only sets the
  icon ImageView, res/layout/item_minbar.xml id "iv"), no
  content-desc, and every row shares the same "iv" id. LauncherSettings
  is the sixth row (index 5) in LauncherAction.actionItems order
  (util/LauncherAction.java:29-38; activity/Home.java:551-584), so a
  first-match "iv" tap would hit EditMinBar, not LauncherSettings.
  The dump is saved so the device lead can add an index- or
  bounds-based tap for this row.
- The Drawer sub-screen "Style" row (Ef5eeab0d) is a ButtonPref whose
  text is title + summary joined with a line break
  (libs/materialpreffragment/.../MaterialPrefFragment.java:390-391
  warpText; title res/values/strings.xml settings_drawerStyle =
  "Style", summary settings_drawerStyle_summary = "Choose between
  paged and vertical view for the app drawer."). The tap below uses
  the two-line form; if a real dump shows the text without the line
  break, the selector must be adjusted to the dumped form.
"""

import argparse
import os
import sys
import time

# Repo-root derivation (corrected; see helper REPORT.md).
# __file__ here is device/routes/openlauncher/route_21.py, so
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

    r = Runner(package=args.package, route="route_21",
               edge_ids=["E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a",
                         "E23660de0", "E1701006d", "Ecded7dff", "E06eb37f4",
                         "E823bd16a", "E0117cced", "E9629945d", "E506c5f2f",
                         "E2b9b86b1", "Ecb7f915c", "Ee8ace45b", "Ebf800b8a",
                         "Ebd0c7205", "Ee3b2c4ce", "E7ef50d09", "E4a1f474b",
                         "E2e80d75b", "Ef5eeab0d", "E0b40304d", "E4df174f1",
                         "Ea728a24e"],
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
    # true, the default; activity/Home.java:544). NOT PERFORMED: no
    # harness swipe primitive (see docstring). The dump is saved so
    # the device lead can confirm the drawer state on a real run.
    r.comment("Home.onDrawerStateChanged: left-edge swipe NOT "
              "performed -- no harness swipe primitive; needs an input "
              "swipe from the left edge on a real run",
              edge="E2b9b86b1")
    r.dump_ui("route_21_minibar_closed", edge="E2b9b86b1")

    # Ecb7f915c: Home.onDrawerStateChanged -> S_HOME_MINIBAR --
    # "STATE_IDLE with the left drawer open: the overlay layout is
    # shown and the minibar is open" (guard: newState == STATE_IDLE
    # and drawerLayout.isDrawerOpen(Gravity.LEFT)). No action; follows
    # only if the swipe above happens.
    r.comment("S_HOME_MINIBAR: minibar open at STATE_IDLE with the "
              "left drawer open", edge="Ecb7f915c")

    # Ee8ace45b: S_HOME_MINIBAR -> Home$11.onItemClick@LauncherSettings
    # -- 'Tap the launcher gear icon in the minibar ("Launcher
    # settings")' (guard: the row is enabled; all eight are by
    # default). NOT TAPPED: no harness selector can address the sixth
    # minibar row (see docstring). Tapping first-match "iv" would hit
    # EditMinBar and would be fake progress, so it is not attempted.
    # The dump is saved for an index/bounds-based tap by the device
    # lead.
    r.comment("Home$11.onItemClick@LauncherSettings: row NOT tapped "
              "-- sixth minibar row has no text/desc and shares the "
              "iv id with every row; needs an index/bounds tap",
              edge="Ee8ace45b")
    r.dump_ui("route_21_minibar_rows", edge="Ee8ace45b")

    # Ebf800b8a: Home$11.onItemClick@LauncherSettings ->
    # LauncherAction.RunAction@LauncherSettings --
    # "LauncherAction.RunAction(action, Home.this)". No action.
    r.comment("LauncherAction.RunAction@LauncherSettings: direct "
              "call from the minibar item click", edge="Ebf800b8a")

    # Ebd0c7205: LauncherAction.RunAction@LauncherSettings ->
    # SettingsActivity.onCreate -- "the system creates
    # SettingsActivity, then calls onCreate". No action.
    r.comment("SettingsActivity.onCreate: system lifecycle after "
              "RunAction", edge="Ebd0c7205")

    # Ee3b2c4ce: SettingsActivity.onCreate -> S_SETTINGS_ROOT --
    # "MaterialPrefFragment.newInstance(...) with the 7 category
    # buttons is added to the layout (getSupportFragmentManager().add)"
    # (activity/SettingsActivity.java:41-49). No action.
    r.comment("S_SETTINGS_ROOT: 7 category buttons added by "
              "MaterialPrefFragment", edge="Ee3b2c4ce")

    # E7ef50d09: S_SETTINGS_ROOT ->
    # SettingsActivity.onPrefClicked@drawerSettings -- 'Tap "Drawer"
    # on the Settings root screen' (guard: id == 'drawerSettings').
    # The root ButtonPref has summary None, so its button text is
    # exactly the title (MaterialPrefFragment.java:390-391 warpText;
    # title res/values/strings.xml settings_group_drawer =
    # "App Drawer").
    r.tap(text="App Drawer", edge="E7ef50d09")

    # E4a1f474b: SettingsActivity.onPrefClicked@drawerSettings ->
    # SettingsActivity.onSettingsSelected@2 -- "onSettingsSelected(2)"
    # (guard: id == 'drawerSettings'). No action.
    r.comment("SettingsActivity.onSettingsSelected(2): direct call "
              "from onPrefClicked@drawerSettings", edge="E4a1f474b")

    # E2e80d75b: SettingsActivity.onSettingsSelected@2 ->
    # S_SETTINGS_DRAWER -- "the Drawer sub-screen fragment replaces
    # the root list (fragment transaction, added to the back stack)"
    # (guard: settingsCategory == 2). No action.
    r.comment("S_SETTINGS_DRAWER: Drawer sub-screen replaces the "
              "root list", edge="E2e80d75b")

    # Ef5eeab0d: S_SETTINGS_DRAWER ->
    # SettingsActivity.onPrefClicked@drawerStyle -- 'Tap "Drawer
    # style" on Settings > Drawer' (guard: id == 'drawerStyle').
    # DOUBTFUL two-line form: see docstring. The ButtonPref title is
    # "Style" (settings_drawerStyle) and its summary is the
    # "Choose between..." sentence; warpText joins them with a line
    # break. (The trigger text calls the row "Drawer style"; the
    # on-screen title string is "Style".)
    r.tap(text="Style\nChoose between paged and vertical view for "
              "the app drawer.", edge="Ef5eeab0d")

    # E0b40304d: SettingsActivity.onPrefClicked@drawerStyle ->
    # DialogUtils.appDrawerStylePicker -- "DialogUtils.appDrawerStylePicker(this)"
    # (guard: id == 'drawerStyle'; activity/SettingsActivity.java:
    # 337-340). No action.
    r.comment("DialogUtils.appDrawerStylePicker: direct call from "
              "onPrefClicked@drawerStyle", edge="E0b40304d")

    # E4df174f1: DialogUtils.appDrawerStylePicker -> S_DLG_DRAWER_STYLE
    # -- "b.show(): single-choice list Paged / Vertical"
    # (util/DialogUtils.java:32-50). No action: the dialog appears.
    r.comment("S_DLG_DRAWER_STYLE: single-choice dialog Paged / "
              "Vertical shown", edge="E4df174f1")

    # Ea728a24e: S_DLG_DRAWER_STYLE -> DialogUtils$2.onSelection --
    # 'Tap "Paged" or "Vertical"'. Tap "Vertical": the fresh-install
    # default is Paged (util/LauncherSettings.java:299), so Vertical
    # is the non-preselected choice and its tap certainly fires the
    # single-choice callback (util/DialogUtils.java:45-49; item text
    # res/values/strings.xml settings_drawer_style_vertical =
    # "Vertical"). The target.
    r.tap(text="Vertical", edge="Ea728a24e")
    r.screenshot("route_21_done", edge="Ea728a24e")

    r.done()


if __name__ == "__main__":
    main()
