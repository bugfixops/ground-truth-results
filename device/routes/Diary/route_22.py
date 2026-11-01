#!/usr/bin/env python3
"""Diary route_22: Editor.lambda$onBackPressed$3 (Editor back-press path).

Method: Editor.lambda$onBackPressed$3
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E05ca1e11
    Ea338626d Eded1f47a Ea3b59f09 Ebd97851f E652d1540 E821ce1c6
    Ea16479ba E2c02c361 E159ad6f2
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt,
    section "Editor.lambda$onBackPressed$3" (verdict correct, SOURCE,
    Editor.java:256-271); path row 23 of graphs/Diary/verification.csv.
    Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (standard replay start: run_app.sh does
    pm clear, then this script launches Diary).
Route shape: launch Diary, open the overflow menu, tap "Edit styles…"
    (Diary.java:705-706, 1889-1895: startActivityForResult ACTION_EDIT
    on css/styles.css in Editor), type one character in the Editor so
    the TextWatcher sets changed (Editor.java:146-168, 150-154), press
    Back, which asks "Save changes?" (Editor.java:244-278, 250-253),
    and tap "Discard" to reach the lambda (Editor.java:256-271,
    BUTTON_NEGATIVE branch).
Mapping notes:
    - The overflow button has no app id/text; its content-desc is the
      Android framework default "More options".
    - "Edit styles…" is a showAsAction="never" menu item
      (res/menu/main.xml), so it appears in the overflow list with the
      text from res/values/strings.xml (editStyles = "Edit styles…",
      with the ellipsis character U+2026).
    - The Editor text field is res/layout/editor.xml @+id/text.
    - "Discard" is chosen for the final dialog tap (R.string.discard,
      Editor.java:256-271 via alertDialog 331-343) so the replay does
      not modify styles.css; "Save" would also reach the lambda.
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
    "E05ca1e11", "Ea338626d", "Eded1f47a", "Ea3b59f09", "Ebd97851f",
    "E652d1540", "E821ce1c6", "Ea16479ba", "E2c02c361", "E159ad6f2",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_22 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(args.package, "route_22", EDGE_IDS, args.log,
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

    # E05ca1e11 -- switch case R.id.editStyles: Tap More options ->
    # Edit styles… (Diary.java:705-706; res/menu/main.xml).
    r.tap("E05ca1e11", text="Edit styles…")

    # Ea338626d -- startActivityForResult(ACTION_EDIT
    # file://<folder>/css/styles.css, Editor.class), EDIT_STYLES
    # (Diary.java:1889-1895). Intent edge fired by the previous tap,
    # no further user action.
    r.comment("editStyles starts Editor on css/styles.css", "Ea338626d")

    # Eded1f47a -- The system instantiates Editor, then onCreate
    # (theme from pref_theme, Up arrow on) (Editor.java:72-110).
    # Lifecycle edge, no user action.
    r.comment("Editor instantiated, onCreate runs", "Eded1f47a")

    # Ea3b59f09 -- Editor shows the file with the Accept button and
    # the Up arrow (Editor.java:72-136; res/layout/editor.xml).
    # Wait for the Editor text field to confirm Editor is on screen.
    r.wait_for("Ea3b59f09", res_id="text")

    # Ebd97851f -- Typing notifies the TextWatcher (afterTextChanged)
    # (Editor.java:146-168). Tap the text field, then type one
    # character so the watcher fires.
    r.tap("Ebd97851f", res_id="text")
    r.type_text("x", "Ebd97851f")

    # E652d1540 -- changed = true (Back now asks Save / Discard)
    # (Editor.java:150-154). State edge set by the watcher, no action.
    r.comment("TextWatcher set changed to true", "E652d1540")

    # E821ce1c6 -- Back key (Editor.java:244-278).
    r.back("E821ce1c6")

    # Ea16479ba -- changed: alertDialog("Save changes?", Save, Discard,
    # listener) (Editor.java:250-253). Internal call, no user action.
    r.comment("onBackPressed calls alertDialog, changed branch",
              "Ea16479ba")

    # E2c02c361 -- builder.show(): "Save changes?" Save / Discard
    # (Editor.java:331-343). Dialog shown; wait for its message text.
    r.wait_for("E2c02c361", text="Save changes?")

    # E159ad6f2 -- Tap Save or Discard (Editor.java:256-271).
    # "Discard" (BUTTON_NEGATIVE) chosen so styles.css is not modified.
    r.tap("E159ad6f2", text="Discard")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
