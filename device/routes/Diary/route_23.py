#!/usr/bin/env python3
"""Diary route_23: Diary.showToast(String) (toast path).

Method: Diary.showToast(String)
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E3ca949a2
    E40f66627 E45b1bb57 Ef1071153 Efbd9bfb6 Ee05ecba5 Eed0ae7aa
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt,
    section "Diary.showToast(String)" (verdict correct, SOURCE,
    Diary.java:2953-2957); path row 24 of graphs/Diary/verification.csv.
    Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (standard replay start: run_app.sh does
    pm clear, then this script launches Diary).
Route shape: launch Diary, open the overflow menu, tap "Backup…"
    (Diary.java:711-712), keep the prefilled path in the save dialog
    (Diary.java:1914, 1952-1973; res/layout/save_path.xml) and tap
    "Save", which runs ZipTask.execute(uri) (Diary.java:1916-1947);
    AsyncTask.execute runs onPreExecute on the main thread
    (FW-SRC AsyncTask.java:648), and onPreExecute calls
    showToast(R.string.start) (Diary.java:3117-3122), which calls
    showToast(getString(id)) (Diary.java:2953-2957) -- the target.
Toast observability: the final edge is logged as no-action-observable
    (see the Eed0ae7aa block). A Toast is transient and is rendered in
    a system window that uiautomator dump does not reliably capture,
    so the harness (which finds views only by parsing uiautomator dump)
    cannot wait for or assert on the toast text "Start backup"
    (R.string.start, res/values/strings.xml) without racing the toast's
    lifetime. Asserting on it would fail a run even when the method was
    reached. The drivable action is the "Save" tap; showToast(String) is
    then reached by a direct internal call chain with no further user
    action, and the JaCoCo dump taken after this script is the evidence
    that it ran.
Mapping notes:
    - The overflow button has no app id/text; its content-desc is the
      Android framework default "More options".
    - "Backup…" is a showAsAction="never" menu item (res/menu/main.xml),
      so it appears in the overflow list with the text from
      res/values/strings.xml (backup = "Backup…", ellipsis U+2026).
    - The save dialog's path field is res/layout/save_path.xml
      @+id/pathText, prefilled by Diary.java:1972-1973; the positive
      button guard (BUTTON_POSITIVE and a non-empty path,
      Diary.java:1916-1947) is satisfied by keeping that prefilled path
      unchanged, so no typing is done here.
    - "Save" is the dialog positive button (R.string.save,
      Diary.java:1957 via saveAsDialog 1952-1973).
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
    "E3ca949a2", "E40f66627", "E45b1bb57", "Ef1071153", "Efbd9bfb6",
    "Ee05ecba5", "Eed0ae7aa",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_23 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(args.package, "route_23", EDGE_IDS, args.log,
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

    # E3ca949a2 -- switch case R.id.backup: Tap More options -> Backup…
    # (Diary.java:711-712; res/menu/main.xml).
    r.tap("E3ca949a2", text="Backup…")

    # E40f66627 -- saveAsDialog(name, Backup, "Choose a file name",
    # listener) (Diary.java:1914). Internal call, no user action.
    r.comment("backup calls saveAsDialog with prefilled name",
              "E40f66627")

    # E45b1bb57 -- builder.show() with the path EditText prefilled
    # (Diary.java:1952-1973; res/layout/save_path.xml). Wait for the
    # path field to confirm the dialog is on screen.
    r.wait_for("E45b1bb57", res_id="pathText")

    # Ef1071153 -- Tap Save (keep or edit the path), Storage, or Cancel
    # (Diary.java:1916-1947). "Save" (BUTTON_POSITIVE) chosen, with the
    # prefilled path left unchanged so the non-empty-path guard holds.
    r.tap("Ef1071153", text="Save")

    # Efbd9bfb6 -- zipTask.execute(uri) -> onPreExecute on the main
    # thread (Diary.java:1936; FW-SRC AsyncTask.java:648). Framework
    # edge fired by the Save tap, no user action.
    r.comment("ZipTask execute runs onPreExecute on main thread",
              "Efbd9bfb6")

    # Ee05ecba5 -- showToast(R.string.start) "Start backup"
    # (Diary.java:3117-3122). Internal call from onPreExecute, guarded
    # only on the Diary still being referenced; no user action.
    r.comment("onPreExecute calls showToast(R.string.start)",
              "Ee05ecba5")

    # Eed0ae7aa -- showToast(getString(id)) (Diary.java:2953-2957).
    # NO-ACTION-OBSERVABLE: the toast ("Start backup") is transient
    # and lives in a system window that uiautomator dump does not
    # reliably capture, so the harness cannot wait for or assert on
    # it; no tap or assertion is attempted here. The target is reached
    # by the direct internal call from the previous edge, and the
    # post-run JaCoCo dump is the evidence it ran.
    r.comment("no-action-observable: toast showToast(String) reached "
              "by internal call; toast text not asserted (transient, "
              "not in uiautomator dump)", "Eed0ae7aa")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
