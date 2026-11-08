"""Device replay script for openlauncher route_23.

Method: IconLabelItem$ViewHolder.<init>
Edge ids, in ROUTES.csv order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f E2b9b86b1 Ecb7f915c
    Ee8ace45b Ebf800b8a Ebd0c7205 Ee3b2c4ce Ea89dcc77 Efe1f8684 E18fdb83b
    E63702a49 E44f52e32 E70090d31 E48270fbd E8d0dd10f E07333387
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (IconLabelItem section), cross-checked
    against graphs/openlauncher/out/openlauncher_trigger_graph.json and the
    verification.csv path row for this method.
Permissions: none (ROUTES.csv permissions cell empty).
Fixtures: none (ROUTES.csv fixtures cell empty).
Setup: none (ROUTES.csv setup cell empty). run_app.sh clears the app
    (pm clear) before invoking this script, so the first-start onboarding
    is shown and the Skip tap below applies.

Package: com.benny.openlauncher (AndroidManifest.xml package attribute;
    launcher activity com.benny.openlauncher.activity.Init, manifest lines
    28-36, MAIN + LAUNCHER filter).

DOUBTFUL MAPPINGS (see REPORT.md for full evidence):
- E2b9b86b1 (left-edge swipe): the harness has no horizontal-swipe call,
  so scroll_to on the minibar list is used as the closest swipe-issuing
  call. It may not open the drawer on a real run; replace with a real
  left-edge swipe before any real run.
- Ee8ace45b (minibar "Launcher settings" row): minibar rows are icon-only
  (IconListAdapter sets only the row ImageView; the row TextView text is
  never set and is gone; no content-desc; every row shares @+id/iv), so no
  text/desc/unique-id selector exists and no guessed coordinate is written.
  This edge is a comment only; the device lead must tap the 6th minibar
  row (launcher gear icon, index 5) from a real device dump.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# The script lives at device/routes/openlauncher/route_23.py, so the repo
# root is three directories up from the script's containing directory:
# openlauncher/ -> routes/ -> device/ -> repo root. (Four dirname calls
# in total counting _HERE: _HERE is already one level below routes/.)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a", "E23660de0",
    "E1701006d", "Ecded7dff", "E06eb37f4", "E823bd16a", "E0117cced",
    "E9629945d", "E506c5f2f", "E2b9b86b1", "Ecb7f915c", "Ee8ace45b",
    "Ebf800b8a", "Ebd0c7205", "Ee3b2c4ce", "Ea89dcc77", "Efe1f8684",
    "E18fdb83b", "E63702a49", "E44f52e32", "E70090d31", "E48270fbd",
    "E8d0dd10f", "E07333387",
]

INIT_COMPONENT = "com.benny.openlauncher/com.benny.openlauncher.activity.Init"


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_23")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_23", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E3a1527b1 -- Tap the OpenLauncher icon in another launcher
    # (MAIN + LAUNCHER filter), or adb monkey / am start.
    # The trigger text itself allows am start, so launch the MAIN/LAUNCHER
    # activity directly. This starts the app process.
    r.launch(component=INIT_COMPONENT, edge="E3a1527b1")

    # E996c92b8 -- The system instantiates Init, then calls onCreate.
    # Lifecycle edge, no user action.
    r.comment("system instantiates Init then calls onCreate; no user action",
              "E996c92b8")

    # E5aa97973 -- First start: the three onboarding pages are set up.
    # Guard getBoolean("firstStart", true) holds on the fresh install
    # (run_app.sh cleared the app first). Page setup, no user action.
    r.comment("first start: onboarding pages set up; no user action",
              "E5aa97973")

    # E8b7dd43a -- Tap Skip.
    # Selector: text "Skip". Init.java sets the skip button title from
    # strings.xml intro_skip ("Skip") via setSkipButtonTitle
    # (activity/Init.java:53). The OnboarderActivity library layout is not
    # among the inputs, so no button resource-id is known; text is the
    # only grounded selector (see REPORT.md).
    r.tap(edge="E8b7dd43a", text="Skip")

    # E23660de0 -- Direct call: onSkipButtonPressed calls RockIt.
    # Call edge, no user action.
    r.comment("onSkipButtonPressed calls RockIt directly; no user action",
              "E23660de0")

    # E1701006d -- startActivity(new Intent(Init.this, Home.class)) then
    # finish(). Intent edge driven by the app itself, no user action.
    r.comment("RockIt starts Home then finishes Init; no user action",
              "E1701006d")

    # Ecded7dff -- The system instantiates Home, then calls onCreate.
    # Lifecycle edge, no user action.
    r.comment("system instantiates Home then calls onCreate; no user action",
              "Ecded7dff")

    # E06eb37f4 -- onStart after onCreate. Lifecycle edge, no action.
    r.comment("Home onStart after onCreate; no user action", "E06eb37f4")

    # E823bd16a -- onResume after onStart (first resume of this instance).
    # Lifecycle edge, no user action.
    r.comment("Home onResume after onStart; no user action", "E823bd16a")

    # E0117cced -- handleLauncherPause() at the first resume: desktop is
    # not in edit mode and the drawer is not visible. Call edge, no action.
    r.comment("first resume calls handleLauncherPause; no user action",
              "E0117cced")

    # E9629945d -- groupPopup.dismissPopup(). Guard groupPopup != null.
    # Call edge, no user action.
    r.comment("handleLauncherPause dismisses group popup; no user action",
              "E9629945d")

    # E506c5f2f -- The popup is hidden; the home desktop state is entered.
    # Page-enter edge, no user action.
    r.comment("popup hidden, home desktop entered; no user action",
              "E506c5f2f")

    # E2b9b86b1 -- Swipe in from the left screen edge: the DrawerLayout
    # starts to move and settles open. Guard: minBarEnable is true (the
    # default; Home.java:544 unlocks the drawer in that case).
    # DOUBTFUL: the harness has no horizontal-swipe call. scroll_to is the
    # harness's only swipe-issuing call, so it is used here targeted at
    # the drawer list (res/layout/activity_home.xml: minBar SwipeListView
    # inside the start drawer). On a real run this vertical-swipe call may
    # not open the drawer; replace it with a real left-edge swipe before
    # any real run (see REPORT.md). In dry mode it logs a planned swipe.
    r.scroll_to(edge="E2b9b86b1", res_id="minBar")

    # Ecb7f915c -- STATE_IDLE with the left drawer open: the overlay layout
    # is shown and the minibar is open. Page-enter edge, no user action.
    r.comment("drawer idle and open, minibar shown; no user action",
              "Ecb7f915c")

    # Ee8ace45b -- Tap the minibar row "Launcher settings" (launcher gear
    # icon). Guard: the row is enabled in the minibar arrangement (all
    # eight are, by default).
    # NO HARNESS ACTION WRITTEN, DELIBERATELY: minibar rows are icon-only.
    # IconListAdapter.getView inflates res/layout/item_minbar.xml and sets
    # only the ImageView (@+id/iv); the row TextView (@+id/tv) text is
    # never set (the setText line is commented out) and the view is gone
    # in the layout, no content-desc is set anywhere, and every row shares
    # the same @+id/iv -- so tap by text, desc, or res_id cannot select
    # the LauncherSettings row (res_id "iv" would hit the first row,
    # EditMinBar, and derail the route), and no device metrics are among
    # the inputs to ground a fixed coordinate. The device lead must tap
    # the 6th minibar row (index 5 in the default arrangement, gear icon
    # ic_settings_launcher_24dp) from a real device dump (see REPORT.md).
    r.comment("minibar Launcher settings row: icon-only row, no selector "
              "exists; tap 6th row from a real dump; see REPORT",
              "Ee8ace45b")

    # Ebf800b8a -- LauncherAction.RunAction(action, Home.this).
    # Call edge, no user action.
    r.comment("minibar tap runs LauncherAction.RunAction; no user action",
              "Ebf800b8a")

    # Ebd0c7205 -- The system creates SettingsActivity, then calls
    # onCreate. Lifecycle edge, no user action.
    r.comment("system creates SettingsActivity onCreate; no user action",
              "Ebd0c7205")

    # Ee3b2c4ce -- MaterialPrefFragment.newInstance(...) with the 7
    # category buttons is added to the layout. Page-enter edge, no action.
    r.comment("Settings root fragment added with 7 buttons; no action",
              "Ee3b2c4ce")

    # Ea89dcc77 -- Tap "Icons" on the Settings root screen.
    # Guard id == 'iconsSettings'. Selector: text "Icons". The root
    # ButtonPref is built with title getString(settings_group_icons) =
    # "Icons" (strings.xml:87; SettingsActivity.java:47) and a null
    # summary, so the vendored MaterialPrefFragment ButtonPref renders
    # exactly that text (warpText returns the title alone when the summary
    # is null; MaterialPrefFragment.java:390-392, 371).
    r.tap(edge="Ea89dcc77", text="Icons")

    # Efe1f8684 -- onSettingsSelected(5). Guard id == 'iconsSettings'.
    # Call edge, no user action.
    r.comment("Icons tap calls onSettingsSelected(5); no user action",
              "Efe1f8684")

    # E18fdb83b -- The Icons sub-screen fragment replaces the root list
    # (fragment transaction, added to the back stack). Page-enter edge.
    r.comment("Icons sub-screen fragment replaces root; no user action",
              "E18fdb83b")

    # E63702a49 -- Tap "Icon pack" on Settings > Icons.
    # Guard id == 'iconPack'. Selector: the full rendered button text.
    # The Icons ButtonPref is built with title getString(settings_iconPack)
    # = "Icon pack" (strings.xml:153) and summary
    # getString(settings_iconPack_summary) = "Select an installed icon
    # pack." (strings.xml:154; SettingsActivity.java case 5), and
    # warpText renders title + line break + summary when the summary is
    # non-null (MaterialPrefFragment.java:390-392). The harness matches
    # node text after XML parsing, and XML attribute normalisation turns
    # that line break into a space, so the matchable text is the
    # space-joined form below. No resource-id exists (the Button is
    # created programmatically with no id set) and no content-desc is
    # set, so this text is the only selector. Verify against a real dump
    # before a real run (see REPORT.md).
    r.tap(edge="E63702a49",
          text="Icon pack Select an installed icon pack.")

    # E44f52e32 -- AppManager.getInstance(this).startPickIconPackIntent
    # (this). Guard id == 'iconPack'. Call edge, no user action.
    r.comment("Icon pack tap calls startPickIconPackIntent; no action",
              "E44f52e32")

    # E70090d31 -- fastItemAdapter.add(...) then d.show(): FastAdapter
    # shows the rows (AppManager.java:114-152). Framework edge, no action.
    # The dialog always contains at least the "Default" row, so rows are
    # bound even with no icon pack installed.
    r.comment("icon-pack dialog shown, FastAdapter shows rows; no action",
              "E70090d31")

    # E48270fbd -- FastAdapter asks the item for getFactory.
    # Framework edge, no user action.
    r.comment("FastAdapter asks item for getFactory; no user action",
              "E48270fbd")

    # E8d0dd10f -- FastAdapter calls factory.create(view) for a new row.
    # Framework edge, no user action.
    r.comment("FastAdapter calls factory.create for a new row; no action",
              "E8d0dd10f")

    # E07333387 -- new ViewHolder(v) (IconLabelItem.java:43, 60-66).
    # This is the route target; it is reached when the dialog binds its
    # first row, with no further UI step.
    r.comment("factory creates ViewHolder; target reached on row bind",
              "E07333387")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
