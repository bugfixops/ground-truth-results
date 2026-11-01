#!/usr/bin/env python3
"""AmazeFileManager route_28:
ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0.

Method: ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0
Edge ids in order:
    E7836345a E65d0ad48 Ed845d59b Ef0ba5cf2 Ed8c5adf0 E02c0db97
    Efb401063 E5d4de743
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ProcessViewerFragment_CustomServiceConnection_1.lambda_onUpdate_0.txt,
    verdict REACHABLE, 8 edges. This edge list matches methods.csv
    route_edge_ids for the method exactly; the D1 draft's last edge
    was the pre-B6-fix id E815f241d, which the B6 citation/trigger
    corrections renumbered to E5d4de743 (edge ids hash their
    content, see build_graph.py assign_ids), so the draft id is
    stale here.
Permissions: WRITE_EXTERNAL_STORAGE only (the app's declared set),
    granted by run_app.sh under the standard config; the script
    itself grants nothing. No other runtime permission is needed:
    extraction is a local archive-to-local-folder operation.
Fixtures: route28_archive.zip, generated at run time by
    setup_route_28.py into the run's gen dir ($GEN_DIR/
    route28_archive.zip; the script falls back to its beside-script
    path for manual runs) and pushed to
    /sdcard/Download/route28_archive.zip (Download is one
    of the standard fixture locations for this app's work-emulator
    setup). It is deliberately large (three 20 MiB entries of highly
    compressible text, about 3 MB compressed): see the timing note
    below and setup_route_28.py's caveat.
Setup: standard config only (run_app.sh starts from `pm clear`
    and grants only the ROUTES.csv permissions above).
Standard configuration: run_app.sh starts from `pm clear` and
    grants only the ROUTES.csv permissions.

Mapping notes (printed source evidence):
  - TIMING, READ FIRST: the target lambda only fires for
    datapoints published AFTER the process viewer binds
    ExtractService. ProcessViewerFragment.onResume binds all
    five progressive services (ProcessViewerFragment.java:155-172),
    and onServiceConnected installs the ProgressListener whose
    onUpdate runs the lambda on the UI thread
    (ProcessViewerFragment.java:416-423; the print cites :422
    for the same lambda). AbstractProgressiveService.addDatapoint
    only calls the listener if one is set
    (AbstractProgressiveService.java:182-191, onUpdate at :189),
    and datapoints published before the bind are replayed through
    processResults directly, not through onUpdate
    (ProcessViewerFragment.java:408-411). The script therefore
    starts extraction and then, with no intervening wait, opens
    the viewer, so the bind lands while extraction is still
    publishing. The tens-of-MB archive is what makes that window
    wide enough: the UI map recommends exactly this ("a file of
    tens of MB, so copy/extract services run long enough").
    CAVEAT: the run-time archive holds highly compressible text,
    so it decompresses faster than the original fixture and the
    window may be narrower (see setup_route_28.py's caveat).
    If a device run shows extraction finishing before the bind,
    enlarge the fixture; do not claim the lambda fired.
  - MainActivity is the MAIN/LAUNCHER activity
    (AndroidManifest.xml:58, intent filter :61-65), so the script
    launches com.amaze.filemanager.debug/.activities.MainActivity.
  - Navigation to a folder uses the documented `path` intent
    extra (MainActivity.java:1571-1578; same extra at :308).
  - Tapping the archive row opens the archive dialog:
    FileUtils.openFile shows it for an extractable archive
    (FileUtils.java:753-755), with title "Archive"
    (strings.xml:175) and positive button "Extract"
    (strings.xml:72); the positive lambda calls
    mainActivityHelper.extractFile (GeneralDialogCreation.java:924-936).
    extractFile takes the writable-local branch and decompresses
    (MainActivityHelper.java:522-531), and Decompressor starts
    ExtractService (Decompressor.java:44-48).
  - Opening the viewer uses the documented intent path, not the
    notification shade (which is system UI outside the harness
    package): MainActivity.onNewIntent replaces content_frame
    with ProcessViewerFragment when the `openprocesses` boolean
    extra is true (MainActivity.java:1588-1596; the key is
    KEY_INTENT_PROCESS_VIEWER = "openprocesses" at :231, and the
    same path runs at cold start at :388-397). The harness
    passes a boolean extra with extras_args, since its extras
    dict only carries string extras. The UI map confirms this
    route ("process viewer via --ez openprocesses true").
  - The viewer title is R.string.process_viewer = "Process
    Viewer" (strings.xml:122), set by ProcessViewerFragment
    (ProcessViewerFragment.java:141), so waiting for that
    text evidences the viewer is visible while extraction
    publishes.
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
    "E7836345a", "E65d0ad48", "Ed845d59b", "Ef0ba5cf2", "Ed8c5adf0",
    "E02c0db97", "Efb401063", "E5d4de743",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/.activities.MainActivity"
ARCHIVE_NAME = "route28_archive.zip"
# Archive generated at run time by setup_route_28.py; run_app.sh
# sets GEN_DIR to the run's gen dir. Prefer the generated file
# there; fall back to the beside-script path for manual runs.
_GEN_DIR = os.environ.get("GEN_DIR", "")
FIXTURE = os.path.join(_GEN_DIR, ARCHIVE_NAME) \
    if _GEN_DIR and os.path.isfile(os.path.join(_GEN_DIR, ARCHIVE_NAME)) \
    else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "route28_archive.zip")
DEVICE_ARCHIVE = "/sdcard/Download/" + ARCHIVE_NAME
SOURCE_DIR = "/sdcard/Download"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_28")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_28", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E7836345a S_ENTRY -> ExtractService.<init>: drive the
    # extraction that starts ExtractService. Push the archive
    # fixture, launch MainActivity, navigate to Download with
    # the `path` extra, tap the archive row to open the archive
    # dialog, and tap Extract. ExtractService is declared in
    # AndroidManifest.xml:165-169.
    r.push_fixture(FIXTURE, "E7836345a", dest=DEVICE_ARCHIVE)
    r.launch(MAIN, "E7836345a")
    r.start_intent("E7836345a", extras={"path": SOURCE_DIR},
                   component=MAIN)
    r.wait_for("E7836345a", text=ARCHIVE_NAME, timeout=30)
    r.tap("E7836345a", text=ARCHIVE_NAME)
    r.tap("E7836345a", text="Extract")
    # E65d0ad48 ExtractService.<init> -> ExtractService.onCreate:
    # service lifecycle. No user action.
    r.comment("service lifecycle: onCreate runs", "E65d0ad48")
    # Ed845d59b ExtractService.onCreate ->
    # ExtractService.onStartCommand: service lifecycle; the
    # service goes foreground and starts its DoWork task here.
    # No user action.
    r.comment("service lifecycle: onStartCommand runs", "Ed845d59b")
    # Ef0ba5cf2 ExtractService.onStartCommand ->
    # ExtractService.lambda$onStartCommand$0: onStartCommand sets
    # the progress listener (ExtractService.java:142-143), which
    # publishes results on each progress update. No user action.
    r.comment("onStartCommand sets the progress listener "
              "(ExtractService.java:142-143)", "Ef0ba5cf2")
    # Ed8c5adf0 ExtractService.lambda$onStartCommand$0 ->
    # AbstractProgressiveService.publishResults@ExtractService:
    # the listener calls publishResults(speed, false, false)
    # (ExtractService.java:143). No user action.
    r.comment("progress listener calls publishResults "
              "(ExtractService.java:143)", "Ed8c5adf0")
    # E02c0db97 AbstractProgressiveService.publishResults@ExtractService
    # -> AbstractProgressiveService.addDatapoint@ExtractService:
    # publishResults builds the datapoint and calls addDatapoint
    # (AbstractProgressiveService.java:161). No user action.
    r.comment("publishResults calls addDatapoint "
              "(AbstractProgressiveService.java:161)", "E02c0db97")
    # Efb401063 AbstractProgressiveService.addDatapoint@ExtractService
    # -> ProcessViewerFragment$CustomServiceConnection$1.onUpdate:
    # addDatapoint calls getProgressListener().onUpdate(datapoint)
    # (AbstractProgressiveService.java:189), but only a listener
    # installed by a bound viewer receives it. Open the viewer
    # NOW, with no wait before this step, so the bind (and its
    # listener install in onServiceConnected) lands while the
    # tens-of-MB extraction is still publishing.
    r.start_intent("Efb401063", component=MAIN,
                   extras_args=["--ez", "openprocesses", "true"])
    # E5d4de743 ProcessViewerFragment$CustomServiceConnection$1.onUpdate
    # -> ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0:
    # onUpdate posts fragment.processResults to the UI thread
    # via runOnUiThread (ProcessViewerFragment.java:416-423);
    # the lambda is that runnable. This is the target edge. No user
    # action; the viewer title evidences the viewer is visible
    # while extraction publishes.
    r.comment("onUpdate posts processResults via runOnUiThread "
              "(ProcessViewerFragment.java:422)", "E5d4de743")
    r.wait_for("E5d4de743", text="Process Viewer", timeout=30)
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
