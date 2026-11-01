#!/usr/bin/env python3
"""openlauncher route_01: HideAppsFragment$2$1.onClick.

Method: HideAppsFragment$2$1.onClick
Edge ids in order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f E2b9b86b1 Ecb7f915c
    Ee8ace45b Ebf800b8a Ebd0c7205 Ee3b2c4ce Ea89dcc77 Efe1f8684 E18fdb83b
    Ee59edc19 Eded61e33 Ec92493a5 E62b23f08 Eb290a250 Efd58a4a1 E58a182d9
    Eb1b71e50 E33aba427 Ebb9bb2c5 Ea7611753 E26fc9fa1 Ea93709a8 Eb6632480
    E7400de03 E8596a759
Printed route: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (HideAppsFragment$2$1.onClick,
    37 steps); path row of graphs/openlauncher/verification.csv;
    device/routes/openlauncher/ROUTES.csv route_01.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none. Setup: none (ROUTES.csv setup column empty).
Standard configuration: run_app.sh starts from pm clear and grants only
    the ROUTES.csv permissions (none here), so this is a first start and
    the onboarding intro is shown; the Skip tap below relies on that.

Repo-root derivation (see the correction to the original brief): the
script lives at device/routes/openlauncher/route_01.py, so the
containing directory is device/routes/openlauncher; three dirname
steps up from that directory reach the repo root (device/routes ->
device -> repo root). Four dirname calls in total counting the one
that turns __file__ into its containing directory.
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
    "E9629945d", "E506c5f2f", "E2b9b86b1", "Ecb7f915c", "Ee8ace45b",
    "Ebf800b8a", "Ebd0c7205", "Ee3b2c4ce", "Ea89dcc77", "Efe1f8684",
    "E18fdb83b", "Ee59edc19", "Eded61e33", "Ec92493a5", "E62b23f08",
    "Eb290a250", "Efd58a4a1", "E58a182d9", "Eb1b71e50", "E33aba427",
    "Ebb9bb2c5", "Ea7611753", "E26fc9fa1", "Ea93709a8", "Eb6632480",
    "E7400de03", "E8596a759",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_01")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_01", edge_ids=EDGE_IDS,
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
    # E2b9b86b1 S_HOME_DESKTOP -> Home.onDrawerStateChanged: swipe in
    # from the left screen edge. GAP, flagged in REPORT.md: the harness
    # has no swipe primitive (scroll_to is a vertical centre swipe, not
    # a left-edge drag), so this edge is logged but not actuated here.
    # Guard: minBarEnable is true by default (LauncherSettings.java:316).
    r.comment("GAP: left-edge swipe not actuated; harness has no swipe",
              "E2b9b86b1")
    # Ecb7f915c Home.onDrawerStateChanged -> S_HOME_MINIBAR: STATE_IDLE
    # with the left drawer open, overlay shown, minibar open.
    r.comment("drawer idle and open: minibar shown", "Ecb7f915c")
    # Ee8ace45b S_HOME_MINIBAR -> Home$11.onItemClick@LauncherSettings:
    # tap the minibar row "Launcher settings". GAP, flagged in
    # REPORT.md: minibar rows are icons only (IconListAdapter.java sets
    # no text, res/layout/item_minbar.xml has no content description,
    # and every row shares res id iv), so no harness selector can pick
    # the LauncherSettings row (the 6th of 8) instead of the first row.
    # Logged, not actuated; do not tap res id iv (it would hit row 1).
    r.comment("GAP: minibar row has no unique selector; not actuated",
              "Ee8ace45b")
    # Ebf800b8a Home$11.onItemClick@LauncherSettings ->
    # LauncherAction.RunAction@LauncherSettings: RunAction(action,
    # Home.this) (Home.java:591-607). No user action.
    r.comment("minibar click runs LauncherSettings action", "Ebf800b8a")
    # Ebd0c7205 LauncherAction.RunAction@LauncherSettings ->
    # SettingsActivity.onCreate: system creates SettingsActivity, then
    # calls onCreate. No user action.
    r.comment("system creates SettingsActivity, then onCreate",
              "Ebd0c7205")
    # Ee3b2c4ce SettingsActivity.onCreate -> S_SETTINGS_ROOT:
    # MaterialPrefFragment with the 7 category buttons is added
    # (SettingsActivity.java:41-49). No user action.
    r.comment("Settings root fragment with 7 category buttons added",
              "Ee3b2c4ce")
    # Ea89dcc77 S_SETTINGS_ROOT -> SettingsActivity.onPrefClicked@iconsSettings:
    # tap "Icons". The root ButtonPref for iconsSettings carries title
    # "Icons" and a null summary (SettingsActivity.java:41-49,
    # res/values/strings.xml:87), and ButtonPref renders a null-summary
    # button as exactly its title (MaterialPrefFragment.java warpText),
    # so the text match is exact.
    r.tap("Ea89dcc77", text="Icons")
    # Efe1f8684 SettingsActivity.onPrefClicked@iconsSettings ->
    # SettingsActivity.onSettingsSelected@5: onSettingsSelected(5).
    r.comment("onPrefClicked iconsSettings selects category 5",
              "Efe1f8684")
    # E18fdb83b SettingsActivity.onSettingsSelected@5 -> S_SETTINGS_ICONS:
    # the Icons sub-screen fragment replaces the root list.
    r.comment("Icons sub-screen fragment replaces root list", "E18fdb83b")
    # Ee59edc19 S_SETTINGS_ICONS -> SettingsActivity.onPrefClicked@iconHide:
    # tap "Hide apps". DOUBTFUL, flagged in REPORT.md: ButtonPref
    # renders title plus summary as one button text (warpText), so the
    # full rendered text is used here (title "Hide apps",
    # res/values/strings.xml:155; summary "Hide selected apps from
    # launcher.", strings.xml:156). Whether a real dump joins them with
    # a newline is unverified against a live dump.
    r.tap("Ee59edc19",
          text="Hide apps\nHide selected apps from launcher.")
    # Eded61e33 SettingsActivity.onPrefClicked@iconHide ->
    # HideAppsActivity.<init>: startActivity(HideAppsActivity)
    # (SettingsActivity.java:364-366). No user action.
    r.comment("iconHide starts HideAppsActivity", "Eded61e33")
    # Ec92493a5 HideAppsActivity.<init> -> HideAppsActivity.onCreate:
    # system creates HideAppsActivity, then onCreate. No user action.
    r.comment("system creates HideAppsActivity, then onCreate",
              "Ec92493a5")
    # E62b23f08 HideAppsActivity.onCreate ->
    # HideAppsActivity.setupViewPager: setupViewPager(viewPager).
    r.comment("HideAppsActivity sets up its ViewPager", "E62b23f08")
    # Eb290a250 HideAppsActivity.setupViewPager ->
    # HideAppsActivity$ViewPagerAdapter.getItem: the first layout
    # populates page 0, getItem(0) returns HideAppsFragment.
    r.comment("ViewPager page 0 returns HideAppsFragment", "Eb290a250")
    # Efd58a4a1 HideAppsActivity$ViewPagerAdapter.getItem ->
    # HideAppsFragment.onCreateView: the FragmentManager attaches the
    # fragment and calls onCreateView. No user action.
    r.comment("FragmentManager attaches fragment, onCreateView runs",
              "Efd58a4a1")
    # E58a182d9 HideAppsFragment.onCreateView ->
    # HideAppsFragment$AsyncWorkerList.onPreExecute: taskList.execute(),
    # onPreExecute runs on the calling thread (HideAppsFragment.java).
    r.comment("AsyncWorkerList execute: onPreExecute on caller thread",
              "E58a182d9")
    # Eb1b71e50 HideAppsFragment$AsyncWorkerList.onPreExecute ->
    # HideAppsFragment$AsyncWorkerList.doInBackground: the worker
    # thread runs next. No user action.
    r.comment("worker thread runs doInBackground", "Eb1b71e50")
    # E33aba427 HideAppsFragment$AsyncWorkerList.doInBackground ->
    # HideAppsFragment$AsyncWorkerList.onPostExecute: the worker is done,
    # onPostExecute runs on the main thread. No user action.
    r.comment("worker done: onPostExecute on main thread", "E33aba427")
    # Ebb9bb2c5 HideAppsFragment$AsyncWorkerList.onPostExecute ->
    # S_HIDEAPPS_LIST: switcherLoad.showNext(), the checkable app list
    # is shown. No user action.
    r.comment("showNext shows the checkable app list", "Ebb9bb2c5")
    # Ea7611753 S_HIDEAPPS_LIST -> HideAppsFragment$1.onClick: tap the
    # floating confirm button, res id fab_rq
    # (res/layout/request.xml:68; HideAppsFragment.java binds fab_rq and
    # its click calls confirmSelection).
    r.tap("Ea7611753", res_id="fab_rq")
    # E26fc9fa1 HideAppsFragment$1.onClick ->
    # HideAppsFragment.confirmSelection: confirmSelection(). No action.
    r.comment("confirm button calls confirmSelection", "E26fc9fa1")
    # Ea93709a8 HideAppsFragment.confirmSelection ->
    # HideAppsFragment$2.<init>: new Thread() {...}.start(). No action.
    r.comment("confirmSelection starts a new thread", "Ea93709a8")
    # Eb6632480 HideAppsFragment$2.<init> -> HideAppsFragment$2.run:
    # Thread.start() calls run() on a new thread. No user action.
    r.comment("Thread.start calls run on a new thread", "Eb6632480")
    # E7400de03 HideAppsFragment$2.run -> S_HIDEAPPS_SNACKBAR: no app is
    # selected, so the snackbar with OK is shown (request_toast,
    # res/values/strings.xml:167). No user action.
    r.comment("no app selected: snackbar with OK shown", "E7400de03")
    # E8596a759 S_HIDEAPPS_SNACKBAR -> HideAppsFragment$2$1.onClick:
    # tap "OK" on the snackbar. The action text is getString(R.string.ok),
    # whose value is "OK" (res/values/strings.xml:173). Target edge.
    r.tap("E8596a759", text="OK")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
