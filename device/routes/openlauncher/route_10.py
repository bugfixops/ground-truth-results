#!/usr/bin/env python3
"""openlauncher route_10: GroupPopupView$6$1.hereIsTheText.

Method: GroupPopupView$6$1.hereIsTheText
Edge ids, in route order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d
    Ecded7dff E06eb37f4 E823bd16a E0117cced E9629945d E506c5f2f
    E43dc7c02 E31210536 Ea594e538 E162f036c E49bf5c2b E0cc2720b
    Ef5b731f2
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt, section
    "GroupPopupView$6$1.hereIsTheText".
    Edge details: graphs/openlauncher/out/openlauncher_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none (ROUTES.csv setup column empty). run_app.sh clears the
    package before this script; no permissions are granted and no
    fixtures pushed by this script.

STATE PRECONDITION -- folder on the desktop (not a fixture):
    Edge E43dc7c02 requires "a folder exists on the desktop or in the
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
         with the default name "Unnamed" (strings.xml unnamed).
    This preamble is documented here, not driven: the harness has no
    drag primitive and no long-press-by-coordinate (long_tap takes
    only text/res_id/desc), and desktop app icons are canvas-drawn
    AppItemViews with no text/res_id/desc node (AppItemView.java:
    205-243 onDraw). Until a D2 drag primitive exists, the preamble
    cannot be driven in a real run; see REPORT.md.

Mapping notes (see REPORT.md for full citations):
- Launcher tap (E3a1527b1) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:28-36).
- Folder-icon tap (E43dc7c02) is a selector gap: the folder icon is
  a canvas-drawn AppItemView whose label (item.name, default
  "Unnamed") is painted by onDraw, not a TextView, so no dump node
  carries "Unnamed" for the desktop icon. The script taps that text
  anyway so a real run fails loudly at this step instead of tapping
  an unrelated view; a D2 position tap is the fix (see REPORT.md).
- Folder-title tap (E162f036c) is NOT a gap: the popup title IS a
  real TextView (res/layout/view_grouppopup.xml:17-26, id tv;
  GroupPopupView.java:186 title.setText(item.name)), so tapping the
  folder name text works -- provided the preamble folder kept the
  default name "Unnamed". If the device lead names the folder
  otherwise, change both "Unnamed" strings in this script.
- Rename dialog (E0cc2720b): the input field is focused by the
  MaterialDialogs input dialog on show (assumption, flagged in
  REPORT.md); type_text types into the focused field, then the
  positive button is tapped (Tool.java:472 positiveText OK,
  strings.xml ok = "OK"). The name must be non-empty: an empty input
  returns early (GroupPopupView.java:193).
"""

import argparse
import os
import sys

# Repo-root derivation (four dirname calls on __file__, i.e. three
# up from the script's containing directory device/routes/openlauncher):
#   __file__ -> .../device/routes/openlauncher/route_10.py
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
    "E9629945d", "E506c5f2f", "E43dc7c02", "E31210536", "Ea594e538",
    "E162f036c", "E49bf5c2b", "E0cc2720b", "Ef5b731f2",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_10", edge_ids=EDGE_IDS,
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

        # E43dc7c02 -- Tap a folder icon
        # (ItemViewFactory.java:224-231; guard: the preamble folder
        # exists). SELECTOR GAP (see docstring): the folder icon's
        # label is painted on canvas by AppItemView.onDraw, so no
        # dump node carries it; the tap below names the default
        # folder name ("Unnamed") and will fail loudly in a real run
        # until a D2 position tap exists. Do NOT substitute a
        # res_id: AppItemViews carry no id.
        r.tap(edge="E43dc7c02", text="Unnamed")

        # E31210536 -- Direct call: GroupPopupView.showWindowV
        # (ItemViewFactory.java:227). Follows the folder tap; no
        # separate action.
        r.comment("folder tap calls GroupPopupView.showWindowV",
                  edge="E31210536")

        # Ea594e538 -- The folder card is added with the apps of the
        # folder and its title (GroupPopupView.java:96-258; guard:
        # getVisibility() != VISIBLE). Popup arrival: wait for the
        # title text (GroupPopupView.java:186 title.setText(item.name);
        # default name "Unnamed").
        r.wait_for(edge="Ea594e538", text="Unnamed")

        # E162f036c -- Tap the folder title (GroupPopupView.java:
        # 187-202). The title is a real TextView
        # (res/layout/view_grouppopup.xml:17-26, id tv) holding the
        # folder name; tap it by that text (default "Unnamed").
        r.tap(edge="E162f036c", text="Unnamed")

        # E49bf5c2b -- Tool.DialogHelper.promptInputText(...).show():
        # the rename dialog (GroupPopupView.java:187-202;
        # Tool.java:463-475). Dialog arrival: wait for the dialog
        # title (Tool.java:465 title param; GroupPopupView.java:190
        # passes strings.xml toast_rename = "Rename").
        r.wait_for(edge="E49bf5c2b", text="Rename")

        # E0cc2720b -- Type a new name and tap "OK"
        # (Tool.java:466-471). The MaterialDialogs input dialog
        # focuses its input on show (assumption; see REPORT.md), so
        # type_text goes to that field; then tap the positive button
        # (Tool.java:472 positiveText OK). The name is non-empty, as
        # an empty input returns early (GroupPopupView.java:193).
        # NOTE: this edge has two harness calls in sequence (type,
        # then tap) because the trigger text names two actions; the
        # edge is still counted once in REPORT.md.
        r.type_text("Renamed", edge="E0cc2720b")
        r.tap(edge="E0cc2720b", text="OK")

        # Ef5b731f2 -- TARGET: virtual/interface call that can
        # dispatch to this implementation (Tool.java:469:
        # listener.hereIsTheText(input.toString())). Follows the OK
        # tap; no user action; coverage decides whether the target
        # was reached.
        r.comment("TARGET: dialog input dispatches to hereIsTheText",
                  edge="Ef5b731f2")
    finally:
        r.done()


if __name__ == "__main__":
    main()
