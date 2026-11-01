#!/usr/bin/env python3
"""openlauncher route_07: Tool.checkForUnusedIconAndDelete.

Method: Tool.checkForUnusedIconAndDelete
Edge ids, in route order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d
    Ecded7dff E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f
    E2b9b86b1 Ecb7f915c Ee8ace45b Ebf800b8a Ebd0c7205 Ee3b2c4ce
    Edb554be5 Ee140035c E7bba8962 Ee7603858 Ea8d50c1a Ec36a57c1
    Ecb1e09d0 Ef5aaed4b E5e2263e9
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt, section
    "Tool.checkForUnusedIconAndDelete".
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
- Minibar drawer swipe (E2b9b86b1) is the route's first gap: the
  harness has no swipe primitive and no button opens the DrawerLayout
  drawer. It is logged as a comment, not faked with a tap.
- Minibar row tap (Ee8ace45b) is the route's second gap: the row
  shows an icon only (IconListAdapter.java:53-54: setText is commented
  out; item_minbar.xml tv is gone), so no dump node carries the
  "Launcher settings" label. The script taps the label text anyway so
  a real run fails loudly at this step instead of silently taking a
  wrong path (tapping res_id iv would hit the first row, EditMinBar).
  A D2 row-position tap is the fix; see REPORT.md.
- Desktop-style dialog tap (Ecb1e09d0) picks "Show All Apps
  (Experimental)", not "Normal": the default desktopHomePage is 0
  (Normal), so tapping the already-selected item may not re-fire the
  MaterialDialogs single-choice callback, while tapping the other
  item definitely changes the selection and fires onSelection ->
  switchDesktopMode -> checkForUnusedIconAndDelete (unconditional
  tail call, LauncherSettings.java:202). Either choice reaches the
  target; this one guarantees the callback.
- Settings sub-screen button tap (Ee7603858): MaterialPrefFragment
  ButtonPref renders title + summary as one button text
  (MaterialPrefFragment.java:390-391 warpText), so the tap string is
  the space-joined "Style Choose between different styles for your
  desktop." -- see REPORT.md for the newline-vs-space caveat.
"""

import argparse
import os
import sys

# Repo-root derivation (four dirname calls on __file__, i.e. three
# up from the script's containing directory device/routes/openlauncher):
#   __file__ -> .../device/routes/openlauncher/route_07.py
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
    "E9629945d", "E506c5f2f", "E2b9b86b1", "Ecb7f915c", "Ee8ace45b",
    "Ebf800b8a", "Ebd0c7205", "Ee3b2c4ce", "Edb554be5", "Ee140035c",
    "E7bba8962", "Ee7603858", "Ea8d50c1a", "Ec36a57c1", "Ecb1e09d0",
    "Ef5aaed4b", "E5e2263e9",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_07", edge_ids=EDGE_IDS,
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

        # E2b9b86b1 -- HARNESS GAP, no action coded: swipe in from the
        # left screen edge so the DrawerLayout starts to move and
        # settles open (Home.java:235, 544, 857-878;
        # res/layout/activity_home.xml:5-32). Guard:
        # generalSettings.minBarEnable is true (the default,
        # LauncherSettings.java:316). The harness has no swipe
        # primitive and no button opens this drawer, so this edge
        # cannot be driven as written; see REPORT.md.
        r.comment("GAP: swipe in from the left screen edge to open the "
                  "minibar drawer -- needs a harness swipe primitive",
                  edge="E2b9b86b1")

        # Ecb7f915c -- STATE_IDLE with the left drawer open: the
        # overlay layout is shown and the minibar is open
        # (Home.java:870-875). Follows the drawer swipe; no separate
        # action (gap-dependent on E2b9b86b1).
        r.comment("drawer settles open: minibar page shown",
                  edge="Ecb7f915c")

        # Ee8ace45b -- Tap the minibar row "Launcher settings"
        # (launcher gear icon) (Home.java:591-607;
        # LauncherAction.java:35, minibar_5). SELECTOR GAP (see
        # docstring): the row shows an icon only, so no dump node
        # carries this label text; the tap below is the intended
        # target and will fail loudly in a real run until a D2
        # row-position tap exists. Do NOT substitute res_id iv: it
        # would hit the first row (EditMinBar).
        r.tap(edge="Ee8ace45b",
              text="Shortcut for the OpenLauncher settings.")

        # Ebf800b8a -- LauncherAction.RunAction(action, Home.this)
        # (Home.java:594-595). Follows the minibar tap; no action.
        r.comment("minibar tap calls LauncherAction.RunAction",
                  edge="Ebf800b8a")

        # Ebd0c7205 -- The system creates SettingsActivity, then calls
        # onCreate (SettingsActivity.java:28-29). Lifecycle edge:
        # no user action.
        r.comment("system creates SettingsActivity, then onCreate",
                  edge="Ebd0c7205")

        # Ee3b2c4ce -- MaterialPrefFragment with the 7 category
        # buttons is added (SettingsActivity.java:33-51).
        # Page arrival: wait for the Settings toolbar title
        # (SettingsActivity.java:37 setTitle(settings); strings.xml
        # settings = "Settings").
        r.wait_for(edge="Ee3b2c4ce", text="Settings")

        # Edb554be5 -- Tap "Desktop" on the Settings root screen
        # (SettingsActivity.java:41-49, 302-324; guard id ==
        # 'desktopSettings'). Root ButtonPref has a null summary, so
        # its button text is exactly the title
        # (MaterialPrefFragment.java:390-391 warpText; strings.xml
        # settings_group_desktop = "Desktop").
        r.tap(edge="Edb554be5", text="Desktop")

        # Ee140035c -- onSettingsSelected(0)
        # (SettingsActivity.java:304-324). Follows the tap; no action.
        r.comment("onPrefClicked(desktopSettings) calls "
                  "onSettingsSelected(0)", edge="Ee140035c")

        # E7bba8962 -- The Desktop sub-screen fragment replaces the
        # root list (SettingsActivity.java:54-138; guard
        # settingsCategory == 0). Page arrival: wait for the
        # sub-screen toolbar title (SettingsActivity.java:72
        # setTitle(settings_group_desktop) = "Desktop").
        r.wait_for(edge="E7bba8962", text="Desktop")

        # Ee7603858 -- Tap "Desktop style" on Settings > Desktop
        # (SettingsActivity.java:61, 341-344; guard id ==
        # 'desktopMode'). The button is a ButtonPref whose text is
        # title + summary (MaterialPrefFragment.java:390-391):
        # settings_desktopStyle = "Style",
        # settings_desktopStyle_summary = "Choose between different
        # styles for your desktop." -- space-joined here; see
        # REPORT.md for the newline-vs-space caveat.
        r.tap(edge="Ee7603858",
              text="Style Choose between different styles for your "
                   "desktop.")

        # Ea8d50c1a -- DialogUtils.desktopStylePicker(this)
        # (SettingsActivity.java:341-344). Follows the tap; no action.
        r.comment("onPrefClicked(desktopMode) calls desktopStylePicker",
                  edge="Ea8d50c1a")

        # Ec36a57c1 -- b.show(): single-choice list Normal / Show all
        # apps (DialogUtils.java:19-30). Dialog arrival: wait for the
        # dialog title (settings_desktopStyle = "Style").
        r.wait_for(edge="Ec36a57c1", text="Style")

        # Ecb1e09d0 -- Tap "Normal" or "Show all apps"
        # (DialogUtils.java:23-28; res/values/arrays.xml
        # desktopStyleEntries). Picks "Show All Apps (Experimental)"
        # so the selection actually changes from the default (Normal)
        # and the single-choice callback fires; see docstring.
        r.tap(edge="Ecb1e09d0", text="Show All Apps (Experimental)")

        # Ef5aaed4b -- LauncherSettings.getInstance(context)
        # .switchDesktopMode(position) (DialogUtils.java:26). Follows
        # the dialog tap; no user action.
        r.comment("dialog selection calls switchDesktopMode",
                  edge="Ef5aaed4b")

        # E5e2263e9 -- TARGET: icon files not referenced by any item
        # are deleted from the cache (LauncherSettings.java:202,
        # unconditional tail call inside switchDesktopMode). No user
        # action; coverage decides whether the target was reached.
        r.comment("TARGET: switchDesktopMode calls "
                  "checkForUnusedIconAndDelete", edge="E5e2263e9")
    finally:
        r.done()


if __name__ == "__main__":
    main()
