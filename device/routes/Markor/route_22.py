"""Device route script: route_22.

Method: GsFileBrowserListAdapter.lambda$scrollToAndFlash$3
Printed route file: graphs/Markor/scratch/route_print/route_22.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c
  E0ecb8e4d Eba14bdbd E289c960d E2ac0e2b0 Edc0d7fff Ef615fd2e
  Ebf8e92d2 Eaff01465 Eb3db1677 Ea6230386
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: Documents/notes.md
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Replay: cold-start MainActivity into the notebook list, then tap the
go-up ("..") row. Tapping that row calls loadFolder(parent, show =
current folder) (GsFileBrowserListAdapter.java:424), so after the
folder loads, _loadFolder posts scrollToAndFlash(current folder) and
the nested post/postDelayed runnables fire lambda$scrollToAndFlash$3.
The pushed Documents/notes.md stands for the notebook contents listed
and scrolled (the parent folder listing contains the pushed files).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "harness"))
from harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_22",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "Eba14bdbd",
                         "E289c960d", "E2ac0e2b0", "Edc0d7fff", "Ef615fd2e",
                         "Ebf8e92d2", "Eaff01465", "Eb3db1677", "Ea6230386"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # No permissions listed in ROUTES.csv for this route, so no grant().
    # Fixtures are pushed by run_app.sh, not here.
    # E211966cc: Tap the Markor launcher icon (process start).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: The system calls Application.onCreate -- no user action.
    r.comment("system lifecycle: Application.onCreate, no user action",
              "Ed6414d9f")
    # E0254b914: MAIN/LAUNCHER intent starts MainActivity -- already
    # started by the launch above, no further action.
    r.comment("MainActivity already started by the E211966cc launch",
              "E0254b914")
    # Ed25af8f4: The system calls Activity.onCreate -- no user action.
    r.comment("system lifecycle: Activity.onCreate, no user action",
              "Ed25af8f4")
    # Eba46a594: The system calls Activity.onStart/onResume -- no action.
    r.comment("system lifecycle: onStart/onResume, no user action",
              "Eba46a594")
    # E659e191c: Activity.performResume calls onPostResume -- no action.
    r.comment("system lifecycle: onPostResume, no user action",
              "E659e191c")
    # E0ecb8e4d: Notebook tab is the default startup tab (MainActivity
    # onCreate pager setup, MainActivity.java:105-106). Wait until the
    # notebook list is populated: the go-up row is titled ".."
    # (GsFileBrowserListAdapter.java:224, title set to ".." for the
    # go-up entry), so its presence means the list has loaded.
    r.wait_for("E0ecb8e4d", text="..")
    # Eba14bdbd: Tap a file or folder in the notebook list -- here the
    # go-up ("..") row. GsFileBrowserListAdapter.onClick, row-click
    # branch (GsFileBrowserListAdapter.java:404-424): a directory tap
    # calls loadFolder; for the go-up row it passes show = _currentFolder,
    # which is what makes _loadFolder later scroll to and flash that
    # folder. A plain subfolder tap would pass show = null and would
    # NOT reach scrollToAndFlash, so the ".." row is the correct tap.
    r.tap("Eba14bdbd", text="..")
    # E289c960d: GsFileBrowserListAdapter.loadFolder -- direct call.
    r.comment("direct call: loadFolder, no user action", "E289c960d")
    # E2ac0e2b0: lambda$loadFolder$5 -- executor callback registered
    # by loadFolder; the framework/executor runs it, no user action.
    r.comment("executor callback: lambda$loadFolder$5, no user action",
              "E2ac0e2b0")
    # Edc0d7fff: GsFileBrowserListAdapter._loadFolder -- direct call.
    r.comment("direct call: _loadFolder, no user action", "Edc0d7fff")
    # Ef615fd2e: postScrollToAndFlash -- direct call; it posts
    # scrollToAndFlash via RecyclerView.post (GsFileBrowserListAdapter
    # .java:614-618), with toShow = the folder passed as show above.
    r.comment("direct call: postScrollToAndFlash, no user action",
              "Ef615fd2e")
    # Ebf8e92d2: lambda$postScrollToAndFlash$2 -- RecyclerView.post
    # runnable; the framework runs it, no user action.
    r.comment("posted runnable: lambda$postScrollToAndFlash$2, no action",
              "Ebf8e92d2")
    # Eaff01465: scrollToAndFlash -- direct call (GsFileBrowserListAdapter
    # .java:622-640: scrolls to the position and posts the flash).
    r.comment("direct call: scrollToAndFlash, no user action", "Eaff01465")
    # Eb3db1677: lambda$scrollToAndFlash$4 -- RecyclerView.post runnable
    # (GsFileBrowserListAdapter.java:630), no user action.
    r.comment("posted runnable: lambda$scrollToAndFlash$4, no action",
              "Eb3db1677")
    # Ea6230386: lambda$scrollToAndFlash$3 -- postDelayed runnable
    # (GsFileBrowserListAdapter.java:631, 400 ms delay) that blinks the
    # holder view; the framework runs it, no user action.
    r.comment("delayed runnable: lambda$scrollToAndFlash$3, no action",
              "Ea6230386")
    r.done()


if __name__ == "__main__":
    main()
