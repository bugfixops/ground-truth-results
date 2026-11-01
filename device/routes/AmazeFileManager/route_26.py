#!/usr/bin/env python3
"""AmazeFileManager route_26: GenericCopyUtil.doCopy.

Method: GenericCopyUtil.doCopy
Edge ids in order:
    E6b899d64 E2ed8719f Ea2e572e2 E4f746fc4 E230f7324 E95c06f94
    E6d73bd7e E91d5fb40 E09fea7ad E79c94d18
Printed route: graphs/AmazeFileManager/scratch/route_print/
    GenericCopyUtil.doCopy.txt, verdict REACHABLE, 10 edges.
    This edge list matches methods.csv route_edge_ids for
    GenericCopyUtil.doCopy exactly and matches the D1 draft
    route_26 row exactly; no mismatch.
Permissions: WRITE_EXTERNAL_STORAGE (manifest
    AndroidManifest.xml:31; READ_EXTERNAL_STORAGE is added by the
    merged manifest per the UI map). Both are ROUTES.csv decisions
    granted by run_app.sh under the standard config; the script
    itself grants nothing. No other runtime permission is needed:
    the copy is a local file-to-file copy.
Fixtures: route26_source.txt, shipped beside this script and
    pushed to /sdcard/Download/route26_source.txt (Download is one
    of the standard fixture locations for this app's work-emulator
    setup). The paste target is /sdcard (the storage root): it is
    a different folder from the source folder, so the paste does
    not hit the same-name conflict dialog (PrepareCopyTask
    showDialog, PrepareCopyTask.java:182-214, which disables
    overwrite when the target is the source's own parent).
Setup: standard config only (run_app.sh starts from `pm clear`
    and grants only the ROUTES.csv permissions above).
Standard configuration: run_app.sh starts from `pm clear` and
    grants only the ROUTES.csv permissions.

Mapping notes (printed source evidence):
  - MainActivity is the MAIN/LAUNCHER activity
    (AndroidManifest.xml:58, intent filter :61-65), so the script
    launches com.amaze.filemanager.debug/.activities.MainActivity.
  - Navigation to a folder uses the documented `path` intent
    extra: MainActivity.onNewIntent loads the directory when the
    extra names one (MainActivity.java:1571-1578; the same extra
    is read at :308 for pinned shortcuts). This avoids tapping
    the drawer hamburger and bookmark rows, whose on-screen
    positions depend on drawer scroll state.
  - The row overflow button is ItemViewHolder.about, bound to
    R.id.properties (holders/ItemViewHolder.java:50; the button
    is the ic_more_vert ImageButton in res/layout/rowlayout.xml).
    RecyclerAdapter.showPopup wires it to the ItemPopupMenu
    (RecyclerAdapter.java:948-952), which inflates
    res/menu/item_extras.xml; its Copy item carries title
    @string/copy = "Copy" (strings.xml:93). The go-back row's
    overflow button is GONE (RecyclerAdapter.java:503-505), so
    with a single fixture file in Download the res_id tap hits
    the fixture row.
  - Copy stores a PasteHelper (ItemPopupMenu.java:99-105) and the
    toolbar Paste item becomes visible (MainActivity.java:757-761,
    :856, :867). Tapping Paste runs PrepareCopyTask
    (MainActivity.java:1025-1033), whose finishCopying starts
    CopyService (PrepareCopyTask.java:279-301, :168-175).
  - Paste renders as text when there is room
    (activity_extra.xml: Paste showAsAction="ifRoom|withText")
    and as an icon-only action otherwise; the script therefore
    tries the "Paste" text first and falls back to its content
    description, which is the standard AppCompat action-item
    behaviour. Only one of the two can match on a given device.
  - The channel path is what the print shows: for a writable
    local target, GenericCopyUtil opens a RandomAccessFile
    channel for source and target, so startCopy (:99) takes the
    FileChannel overload (copyFile at :355, reached from copy
    at :325) and that overload calls doCopy (:392, print
    cite :359).
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
    "E6b899d64", "E2ed8719f", "Ea2e572e2", "E4f746fc4", "E230f7324",
    "E95c06f94", "E6d73bd7e", "E91d5fb40", "E09fea7ad", "E79c94d18",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/.activities.MainActivity"
FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "route26_source.txt")
FILENAME = "route26_source.txt"
DEVICE_SRC = "/sdcard/Download/" + FILENAME
SOURCE_DIR = "/sdcard/Download"
TARGET_DIR = "/sdcard"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_26")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_26", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E6b899d64 S_ENTRY -> CopyService.<init>: drive the in-app
    # copy flow that starts CopyService. Push the source fixture,
    # launch MainActivity, navigate to Download with the `path`
    # extra, open the fixture row's popup menu, and tap Copy.
    r.push_fixture(FIXTURE, "E6b899d64", dest=DEVICE_SRC)
    r.launch(MAIN, "E6b899d64")
    r.start_intent("E6b899d64", extras={"path": SOURCE_DIR},
                   component=MAIN)
    r.wait_for("E6b899d64", text=FILENAME, timeout=30)
    r.tap("E6b899d64", res_id="properties")
    r.tap("E6b899d64", text="Copy")
    # Still under E6b899d64: navigate to the paste target (a
    # different folder, so no conflict dialog) and tap Paste,
    # which runs PrepareCopyTask and starts CopyService.
    r.start_intent("E6b899d64", extras={"path": TARGET_DIR},
                   component=MAIN)
    try:
        r.tap("E6b899d64", text="Paste")
    except LookupError:
        # Toolbar rendered Paste as an icon-only action on this
        # device; its content description is the item title.
        r.tap("E6b899d64", desc="Paste")
    # E2ed8719f CopyService.<init> -> CopyService.onCreate:
    # service lifecycle. The started service registers its cancel
    # receiver here (CopyService.java:100). No user action.
    r.comment("service lifecycle: onCreate runs, cancel receiver "
              "registered (CopyService.java:100)", "E2ed8719f")
    # Ea2e572e2 CopyService.onCreate -> CopyService.onStartCommand:
    # service lifecycle. No user action.
    r.comment("service lifecycle: onStartCommand runs", "Ea2e572e2")
    # E4f746fc4 CopyService.onStartCommand ->
    # CopyService$DoInBackground.doInBackground: onStartCommand
    # executes the background task (CopyService.java:160).
    # Framework AsyncTask dispatch; no user action.
    r.comment("onStartCommand executes DoInBackground "
              "(CopyService.java:160)", "E4f746fc4")
    # E230f7324 CopyService$DoInBackground.doInBackground ->
    # CopyService$DoInBackground$Copy.execute: doInBackground
    # calls copy.execute(sourceFiles, targetPath, move, openMode)
    # (CopyService.java:254). No user action.
    r.comment("doInBackground calls Copy.execute "
              "(CopyService.java:254)", "E230f7324")
    # E95c06f94 CopyService$DoInBackground$Copy.execute ->
    # CopyService$DoInBackground$Copy.copyFiles: execute calls
    # copyFiles for the non-root source file
    # (CopyService.java:381). No user action.
    r.comment("execute calls copyFiles (CopyService.java:381)",
              "E95c06f94")
    # E6d73bd7e CopyService$DoInBackground$Copy.copyFiles ->
    # GenericCopyUtil.copy: copyFiles builds GenericCopyUtil and
    # calls copyUtil.copy(sourceFile, targetFile)
    # (CopyService.java:477). No user action.
    r.comment("copyFiles calls GenericCopyUtil.copy "
              "(CopyService.java:477)", "E6d73bd7e")
    # E91d5fb40 GenericCopyUtil.copy -> GenericCopyUtil.startCopy:
    # copy stores source/target and calls startCopy(false)
    # (GenericCopyUtil.java:330). No user action.
    r.comment("copy calls startCopy(false) "
              "(GenericCopyUtil.java:330)", "E91d5fb40")
    # E09fea7ad GenericCopyUtil.startCopy ->
    # GenericCopyUtil.copyFile(FileChannel,FileChannel): the
    # writable local target takes the channel branch, so
    # startCopy calls copyFile(inChannel, outChannel)
    # (GenericCopyUtil.java:285). No user action.
    r.comment("startCopy calls the FileChannel copyFile overload "
              "(GenericCopyUtil.java:285)", "E09fea7ad")
    # E79c94d18 GenericCopyUtil.copyFile(FileChannel,FileChannel)
    # -> GenericCopyUtil.doCopy: the overload calls
    # doCopy(inChannel, outChannel) (GenericCopyUtil.java:359).
    # This is the target edge. No user action; the copied file
    # appearing in the target folder evidences completion.
    r.comment("FileChannel copyFile calls doCopy "
              "(GenericCopyUtil.java:359)", "E79c94d18")
    r.wait_for("E79c94d18", text=FILENAME, timeout=60)
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
