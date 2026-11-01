"""Diary route_07: Diary.alertDialog(int,String,int).

Method: Diary.alertDialog(int,String,int)
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E3ca949a2
    E40f66627 E45b1bb57 Eca36c4c7 Eb4634804 E95cb08f1 E5f87aaf2
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.alertDialog(int,String,int)", ref
    Diary.java:3186-3188).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none from ROUTES.csv (setup column empty). The route's
    failure is produced by ordinary GUI input: a backup path in a
    folder that does not exist (edge Eca36c4c7), so no fixture or
    device precondition is needed.
Standard configuration: run_app.sh clears the package before this
    script; no permissions are granted and no fixtures pushed.

Mapping notes:
- Launcher tap (Ee6b8aa80) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:52-59).
- The backup dialog's EditText is res/layout/save_path.xml
  (@+id/pathText), prefilled with the default backup path
  (Diary.java:1952-1973, 1914). The harness has no clear-text
  action, so the script clears it with repeated DEL keys (60, more
  than any prefilled home-relative path) before typing the bad path.
- The dialog's positive button is R.string.save ("Save",
  Diary.java:1956, res/values/strings.xml:43).
- alertDialog(int,String,int) (Diary.java:2340-2349) shows a dialog
  with a single neutral button, android.R.string.ok ("OK"); waiting
  for "OK" proves the target ran, and tapping it dismisses the
  dialog (cleanup, not a route step).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

COMPONENT = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E3ca949a2", "E40f66627", "E45b1bb57", "Eca36c4c7", "Eb4634804",
    "E95cb08f1", "E5f87aaf2",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_07", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter). Driven as am start.
        r.launch(COMPONENT, "Ee6b8aa80")

        # Edd0b9192 -- The system instantiates Diary, then onCreate.
        # Lifecycle edge: no user action.
        r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

        # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
        r.comment("onStart -> onResume", "Ee63879c9")

        # Ea885d6f1 -- Diary visible with the MarkdownView.
        # Page arrival: wait for the MarkdownView (res/layout/main.xml
        # @+id/markdown).
        r.wait_for("Ea885d6f1", res_id="markdown")

        # E002e1746 -- Tap an action bar icon or an item under More
        # options. Backup lives in the overflow menu
        # (showAsAction="never", res/menu/main.xml), so open it.
        r.tap("E002e1746", desc="More options")

        # E3ca949a2 -- switch case R.id.backup (Diary.java:711-712).
        r.tap("E3ca949a2", text="Backup\u2026")

        # E40f66627 -- saveAsDialog(name, Backup, "Choose a file
        # name", listener) (Diary.java:1914). Internal call; no action.
        r.comment("saveAsDialog(name, Backup, choose, listener)",
                  "E40f66627")

        # E45b1bb57 -- builder.show() with the path EditText prefilled
        # (Diary.java:1952-1973; res/layout/save_path.xml). Wait for
        # the dialog's EditText.
        r.wait_for("E45b1bb57", res_id="pathText")

        # Eca36c4c7 -- Save to a path in a folder that does not exist
        # (Diary.java:1916-1936). Clear the prefilled path (no
        # clear-text harness action exists, so DEL repeatedly), type
        # a path in a missing folder, and tap Save.
        r.tap("Eca36c4c7", res_id="pathText")
        for _ in range(60):
            r.key("DEL", "Eca36c4c7")
        r.type_text("nofolder/backup.zip", "Eca36c4c7")
        r.tap("Eca36c4c7", text="Save")

        # Eb4634804 -- execute -> doInBackground(uri) on a worker
        # thread (Diary.java:1936). Async edge: no user action.
        r.comment("ZipTask execute -> doInBackground(uri)",
                  "Eb4634804")

        # E95cb08f1 -- openOutputStream(file URI in a missing folder)
        # throws FileNotFoundException: runOnUiThread(alert)
        # (Diary.java:3131-3133). Background failure; no user action.
        r.comment("openOutputStream throws, runOnUiThread(alert)",
                  "E95cb08f1")

        # E5f87aaf2 -- alertDialog(appName, e.getMessage(), OK)
        # (Diary.java:3186-3188). The dialog's only button is "OK"
        # (Diary.java:2340-2349); waiting for it proves the target
        # ran, then dismiss it.
        r.wait_for("E5f87aaf2", text="OK")
        r.tap("E5f87aaf2", text="OK")
    finally:
        r.done()


if __name__ == "__main__":
    main()
