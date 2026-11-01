#!/usr/bin/env python3
"""AmazeFileManager route_27: FileUtils.lambda$scanFile$1.

Method: FileUtils.lambda$scanFile$1
Edge ids in order:
    E69f5f041 E50bd16b1 Eddafb591 E15eca248 Eb41b8819 E0dcd9ee2
    E3ef101e1 E903029d8
Printed route: graphs/AmazeFileManager/scratch/route_print/
    FileUtils.lambda_scanFile_1.txt, verdict REACHABLE, 8 edges.
    This edge list matches methods.csv route_edge_ids for
    FileUtils.lambda$scanFile$1 exactly and matches the D1 draft
    route_27 row exactly; no mismatch.
Permissions: WRITE_EXTERNAL_STORAGE (manifest
    AndroidManifest.xml:31; READ_EXTERNAL_STORAGE is added by the
    merged manifest per the UI map). Both are ROUTES.csv decisions
    granted by run_app.sh under the standard config; the script
    itself grants nothing. No other runtime permission is needed:
    the rename is a local file-to-file rename.
Fixtures: route27_source.txt, shipped beside this script and
    pushed to /sdcard/Download/route27_source.txt (Download is one
    of the standard fixture locations for this app's work-emulator
    setup). The rename target is route27_renamed.txt in the same
    folder; it must not already exist, or Operations.rename takes
    its exists() branch (Operations.java:347-350) and never
    reaches onPostExecute's scanFile call.
Setup: standard config only (run_app.sh starts from `pm clear`
    and grants only the ROUTES.csv permissions above).
Standard configuration: run_app.sh starts from `pm clear` and
    grants only the ROUTES.csv permissions.

Mapping notes (printed source evidence):
  - ENTRY VARIANT, READ FIRST: the print's first two edges run
    through MainActivity.onActivityResult, which is only the
    storage-access-framework retry path: onActivityResult
    requestCode 3 dispatches DataUtils.RENAME to
    MainActivityHelper.rename (MainActivity.java:1373-1376), and
    that retry is only armed when an earlier rename hit
    checkFolder mode 2 (external SD card not writable without
    SAF; Operations.java:439-441, MainActivityHelper.java:277
    launchSAF arm). A fixture on internal storage is writable,
    so checkFolder returns 1 (Operations.java:491-519, "file not
    on external sd card" branch), the SAF retry never arms, and
    the script drives the direct rename path instead: the row
    popup menu's Rename item calls MainFragment.rename
    (ItemPopupMenu.java:99), which shows the rename dialog and
    on Save calls exactly the same MainActivityHelper.rename
    (MainFragment.java:1209-1226). Both variants converge at
    MainActivityHelper.rename -> Operations.rename, so every
    edge from Eddafb591 onward fires identically; only the two
    printed entry edges are logged as comments, not faked.
    Driving the SAF picker itself is out of scope: it is system
    UI outside the harness's package, and the UI map lists the
    SAF picker as a gate for exactly this reason.
  - Navigation to a folder uses the documented `path` intent
    extra (MainActivity.java:1571-1578; same extra at :308).
  - The row overflow button is ItemViewHolder.about, bound to
    R.id.properties (holders/ItemViewHolder.java:50; the button
    is the ic_more_vert ImageButton in res/layout/rowlayout.xml).
    The go-back row's overflow button is GONE
    (RecyclerAdapter.java:503-505), so with a single fixture
    file in Download the res_id tap hits the fixture row. The
    popup's Rename item carries title @string/rename = "Rename"
    (item_extras.xml, strings.xml:49).
  - The rename dialog is GeneralDialogCreation.showNameDialog
    (MainFragment.java:1210-1214): title "Rename", prefilled
    with the old name, positive button "Save"
    (strings.xml:50), negative "CANCEL" (strings.xml:43). Its
    EditText is R.id.singleedittext_input
    (res/layout/dialog_singleedittext.xml:15). A tap places the
    cursor at the tap point rather than at the end, so the script
    sends KEYCODE_MOVE_END first, then deletes the 18-character
    prefill with DEL, then types the new name; that sequence is
    deterministic regardless of where the tap landed.
  - The target lambda is the AsyncTask.execute body in
    FileUtils.scanFile(Context, HybridFile[])
    (FileUtils.java:242-243): onPostExecute calls scanFile with
    both files (Operations.java:480-485), and the renamed file
    exists and is local, so the lambda's first branch runs the
    media scan (FileUtils.java:244-251).
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E69f5f041", "E50bd16b1", "Eddafb591", "E15eca248", "Eb41b8819",
    "E0dcd9ee2", "E3ef101e1", "E903029d8",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/.activities.MainActivity"
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "route27_source.txt")
OLD_NAME = "route27_source.txt"
NEW_NAME = "route27_renamed.txt"
DEVICE_SRC = "/sdcard/Download/" + OLD_NAME
SOURCE_DIR = "/sdcard/Download"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_27")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_27", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E69f5f041 S_ENTRY -> MainActivity.onActivityResult: the
    # print's entry is the SAF-retry variant (see header). The
    # script does NOT drive the system SAF picker; it sets up the
    # direct rename below and logs this edge as a comment. Setup
    # for the route: push the fixture, launch MainActivity, and
    # navigate to Download with the `path` extra.
    r.comment("printed entry is the SAF-retry onActivityResult "
              "variant (MainActivity.java:1373-1376); scripted "
              "path is the direct rename, converging at "
              "MainActivityHelper.rename", "E69f5f041")
    r.push_fixture(FIXTURE, "E69f5f041", dest=DEVICE_SRC)
    r.launch(MAIN, "E69f5f041")
    r.start_intent("E69f5f041", extras={"path": SOURCE_DIR},
                   component=MAIN)
    r.wait_for("E69f5f041", text=OLD_NAME, timeout=30)
    # E50bd16b1 MainActivity.onActivityResult ->
    # MainActivityHelper.rename: the scripted step that reaches
    # MainActivityHelper.rename. Open the fixture row's popup
    # menu, tap Rename, and complete the rename dialog: focus
    # the EditText, move to the end, delete the 18-character
    # prefill, type the new name, and tap Save. On Save,
    # MainFragment.rename calls mainActivityHelper.rename
    # (MainFragment.java:1225-1226).
    r.tap("E50bd16b1", res_id="properties")
    r.tap("E50bd16b1", text="Rename")
    r.tap("E50bd16b1", res_id="singleedittext_input")
    r.key("KEYCODE_MOVE_END", "E50bd16b1")
    for _ in range(len(OLD_NAME)):
        r.key("DEL", "E50bd16b1")
    r.type_text(NEW_NAME, "E50bd16b1")
    r.tap("E50bd16b1", text="Save")
    # Eddafb591 MainActivityHelper.rename -> Operations.rename:
    # MainActivityHelper.rename calls Operations.rename
    # (MainActivityHelper.java:265). No user action beyond Save.
    r.comment("MainActivityHelper.rename calls Operations.rename "
              "(MainActivityHelper.java:265)", "Eddafb591")
    # E15eca248 Operations.rename -> Operations$3.<init>:
    # rename creates its anonymous AsyncTask
    # (Operations.java:335-488). No user action.
    r.comment("Operations.rename creates its AsyncTask "
              "(Operations.java:335-488)", "E15eca248")
    # Eb41b8819 Operations$3.<init> ->
    # Operations$3.doInBackground: AsyncTask.execute dispatches
    # the worker (framework). No user action.
    r.comment("AsyncTask.execute dispatches doInBackground",
              "Eb41b8819")
    # E0dcd9ee2 Operations$3.doInBackground ->
    # Operations$3.onPostExecute: the local rename runs
    # FileUtil.renameFolder and calls errorCallBack.done
    # (Operations.java:438-460); the framework then posts
    # onPostExecute, which calls FileUtils.scanFile
    # (Operations.java:480-485). No user action.
    r.comment("doInBackground renames; onPostExecute calls "
              "FileUtils.scanFile (Operations.java:480-485)",
              "E0dcd9ee2")
    # E3ef101e1 Operations$3.onPostExecute ->
    # FileUtils.scanFile(Context,HybridFile[]): the explicit call
    # at Operations.java:484. No user action.
    r.comment("onPostExecute calls FileUtils.scanFile "
              "(Operations.java:484)", "E3ef101e1")
    # E903029d8 FileUtils.scanFile(Context,HybridFile[]) ->
    # FileUtils.lambda$scanFile$1: scanFile runs
    # AsyncTask.execute with the scan lambda
    # (FileUtils.java:243). This is the target edge. No user
    # action; the renamed file appearing in the list evidences
    # that the rename (and hence onPostExecute) completed.
    r.comment("scanFile runs AsyncTask.execute with the scan "
              "lambda (FileUtils.java:243)", "E903029d8")
    r.wait_for("E903029d8", text=NEW_NAME, timeout=60)
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
