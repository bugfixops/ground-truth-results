#!/usr/bin/env python3
"""Diary route_21: Diary.lambda$cancel$17 (cancel menu item path).

Method: Diary.lambda$cancel$17
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
    Ec7e88adf Ec5df0a10 Ef3256716 Ef19e7dc8 Ec8877910 E4b4f59bc
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt,
    section "Diary.lambda$cancel$17" (verdict fixed, SOURCE,
    Diary.java:1214-1225); path row 22 of graphs/Diary/verification.csv.
    Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (standard replay start: run_app.sh does
    pm clear, then this script launches Diary).
Route shape: launch Diary, open the overflow menu, tap "Add time"
    (which inserts the time and sets changed, so the Cancel icon
    becomes visible -- Diary.java:632, 1084-1085, 1847-1855), then tap
    the Cancel icon, which opens the "Save changes?" dialog
    (Diary.java:1208-1225, 2325-2337); tap "Save" to reach the lambda
    (Diary.java:1214-1225, BUTTON_POSITIVE branch).
Mapping notes:
    - The overflow button has no app id/text; its content-desc is the
      Android framework default "More options".
    - "Add time" is a showAsAction="never" menu item (res/menu/main.xml),
      so it appears in the overflow list with the text from
      res/values/strings.xml (addTime = "Add time").
    - Cancel is a showAsAction="ifRoom" action-bar icon (res/menu/main.xml,
      title @android:string/cancel); its content-desc is its title,
      "Cancel". The GUI dispatch edge before it is logged as a comment
      because the icon tap itself is the action, logged under the
      following CALL edge.
    - "Save" is the dialog positive button (R.string.save, Diary.java
      1214-1225 via alertDialog 2325-2337); "Discard" would also reach
      the lambda, but "Save" is the deterministic choice.
"""

import argparse
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E13d2a950", "Ec7e88adf", "Ec5df0a10", "Ef3256716", "Ef19e7dc8",
    "Ec8877910", "E4b4f59bc",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_21 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(args.package, "route_21", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # Ee6b8aa80 -- Tap the Diary icon in the launcher
    # (MAIN/LAUNCHER intent filter, AndroidManifest.xml:52-59).
    # Realised as launching the Diary activity, the adb equivalent
    # of tapping the launcher icon.
    r.launch("org.billthefarmer.diary/.Diary", "Ee6b8aa80")

    # Edd0b9192 -- The system instantiates Diary, then onCreate
    # (Diary.java:441-443). Lifecycle edge, no user action.
    r.comment("Diary instantiated, onCreate runs", "Edd0b9192")

    # Ee63879c9 -- onStart -> onResume (Diary.java:539-541).
    # Lifecycle edge, no user action.
    r.comment("onStart to onResume", "Ee63879c9")

    # Ea885d6f1 -- Diary visible with the MarkdownView
    # (Diary.java:570, 1696-1709; markdown on and shown, the default).
    r.wait_for("Ea885d6f1", res_id="markdown")

    # E002e1746 -- Tap an action bar icon or an item under
    # More options (Diary.java:659-726; res/menu/main.xml:22-118).
    r.tap("E002e1746", desc="More options")

    # E13d2a950 -- switch case R.id.addTime: Tap More options -> Add time
    # (Diary.java:696-697; res/menu/main.xml).
    r.tap("E13d2a950", text="Add time")

    # Ec7e88adf -- Current time (SHORT format) inserted at the cursor;
    # MarkdownView shown, Cancel visible (Diary.java:1847-1855,
    # 1084-1085: the watcher sets changed, so onPrepareOptionsMenu
    # makes Cancel visible, Diary.java:632). No user action.
    r.comment("Add time inserted, changed set, Cancel now visible",
              "Ec7e88adf")

    # Ec5df0a10 -- Tap an action bar icon or an item under
    # More options (Diary.java:659-726). Cancel is an ifRoom action-bar
    # icon already visible in the bar, so there is no overflow menu to
    # open here; the icon tap itself is logged under the next edge.
    r.comment("Cancel icon already visible in action bar; tap follows",
              "Ec5df0a10")

    # Ef3256716 -- switch case R.id.cancel: Tap the Cancel icon
    # (Diary.java:666-667; res/menu/main.xml). Guard: visible only
    # while changed (Diary.java:632), satisfied by the Add time step.
    r.tap("Ef3256716", desc="Cancel")

    # Ef19e7dc8 -- changed: alertDialog("Save changes?", Save, Discard,
    # listener) (Diary.java:1208-1225). Internal call, no user action.
    r.comment("cancel calls alertDialog with Save/Discard listener",
              "Ef19e7dc8")

    # Ec8877910 -- builder.show(): title, message, Save / Discard
    # (Diary.java:2325-2337). Dialog shown; wait for its message text.
    r.wait_for("Ec8877910", text="Save changes?")

    # E4b4f59bc -- Tap Save or Discard (Diary.java:1214-1225).
    # "Save" (BUTTON_POSITIVE) chosen deterministically.
    r.tap("E4b4f59bc", text="Save")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
