"""Device route script for Markor route_08.

Method: FileSearchEngine.isEncryptedFile
Edges (in order): E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594
    E659e191c E0ecb8e4d E14b03637 E004e31e3 E99c21962 E3a03f744
    E227c6b68 E85d08c32 Ebcf2d1c2 E4a1130e5 Ec457d96e E99669d9a
Printed route file: graphs/Markor/scratch/route_print/route_08.txt
ROUTES.csv permissions: none
ROUTES.csv fixtures: Documents/notes.md (stands for the searched
    notebook contents; the setup pushes the whole Documents folder)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Path in words: cold-start MainActivity, notebook tab, tap the toolbar
title. The toolbar click listener (GsActivityBase.java:94-98) hands the
tap to the visible page, whose onToolbarClicked runs the notebook
filter action: showNotebookFilterDialog queues a search over the whole
notebook directory (MarkorDialogFactory.java:1084), and the background
task walks each file, reads it, and calls isEncryptedFile on the stream.
No pm clear and no fixture push here: run_app.sh does both.
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
    r = Runner(package=args.package, route="route_08",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E14b03637",
                         "E004e31e3", "E99c21962", "E3a03f744", "E227c6b68",
                         "E85d08c32", "Ebcf2d1c2", "E4a1130e5", "Ec457d96e",
                         "E99669d9a"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E211966cc -- Tap the Markor launcher icon (process starts).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch(args.package + "/net.gsantner.markor.activity.MainActivity", "E211966cc")
    # Ed6414d9f -- The system calls Application.onCreate.
    # No user action: framework lifecycle step.
    # E0254b914 -- The MAIN / LAUNCHER intent starts MainActivity.
    # No separate action: the launch above already started it.
    # Ed25af8f4 -- The system calls Activity.onCreate.
    # No user action: framework lifecycle step.
    # Eba46a594 -- The system calls Activity.onStart then onResume.
    # No user action: framework lifecycle step.
    # E659e191c -- Activity.performResume calls onPostResume.
    # No user action: framework lifecycle step.
    # E0ecb8e4d -- The notebook tab is the default startup tab (position 0).
    # No user action: the notebook page is already visible after cold start
    # (MainActivity.java:105-106).
    # E14b03637 -- Tap the toolbar title of the notebook.
    # The toolbar click listener is set in GsActivityBase.onResume when the
    # toolbar exists (GsActivityBase.java:94-98); the toolbar view id is
    # "toolbar" (res/layout/main__activity.xml:29). The tap hands control
    # to the visible page (GsActivityBase.java:116-124). The wait confirms
    # the filter dialog opened (title @string/notebook is "Notebook",
    # res/values/strings.xml:108); queueFileSearch already ran when the
    # dialog was shown (MarkorDialogFactory.java:1084).
    r.tap("E14b03637", res_id="toolbar")
    r.wait_for("E14b03637", text="Notebook")
    # E004e31e3 -- Virtual/interface call to onToolbarClicked.
    # No user action: dispatch following the toolbar tap above.
    # E99c21962 -- Direct call to executeFilterNotebookAction.
    # No user action: follows from the toolbar tap above
    # (GsFileBrowserFragment.java:176).
    # E3a03f744 -- Direct call to showNotebookFilterDialog.
    # No user action: follows from the toolbar tap above
    # (GsFileBrowserFragment.java:506).
    # E227c6b68 -- Direct call to FileSearchEngine.queueFileSearch.
    # No user action: follows from the toolbar tap above
    # (MarkorDialogFactory.java:1084).
    # E85d08c32 -- Framework/library runs the background search task.
    # No user action: AsyncTask-style callback, not a UI step.
    # Ebcf2d1c2 -- Direct call to handleDirectory.
    # No user action: follows from the toolbar tap above.
    # E4a1130e5 -- Direct call to getContentMatches.
    # No user action: follows from the toolbar tap above.
    # Ec457d96e -- Direct call to getInputStream.
    # No user action: follows from the toolbar tap above.
    # E99669d9a -- Direct call to isEncryptedFile (target method).
    # No user action: follows from the toolbar tap above.
    r.done()


if __name__ == "__main__":
    main()
