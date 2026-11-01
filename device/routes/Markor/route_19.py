"""Markor route_19: GsFileBrowserListAdapter.createDirectoryHere.

Edge ids in order: E211966cc, Ed6414d9f, E0254b914, Ed25af8f4, Eba46a594,
E659e191c, E0ecb8e4d, E3b54bcd8, E3d9f32c1, Ec0e689c4, E3ee6f9fc, Edb73b446,
E76d2150f, E926780be, Edbac9d51, E95d059a0, E8cac44f6.
Printed route file: graphs/Markor/scratch/route_print/route_19.txt.
ROUTES.csv permissions: none. Fixtures: Documents/notes.md (pushed by
run_app.sh; the script itself never pushes fixtures).
Setup: push fixtures/Documents; first-run tutorial can trap a tool.
Package: net.gsantner.markor_test.

Flow: launch MainActivity (notebook tab by default), select the pushed
fixture file Documents/notes.md, open the notebook toolbar menu and tap
Move (move-or-copy -> folder dialog), tap the new-folder button in the
folder dialog, type a new folder name and confirm with ENTER. The
dialog callback then calls createDirectoryHere
(GsFileBrowserDialog.java:263).
Preparatory taps (selection + overflow menu) are labelled as such:
they are not route edges, they only make the route's own GUI edge
reachable -- the Move item is showAsAction="never"
(res/menu/filesystem__menu.xml:52-57), so it only appears after the
overflow menu is opened, and it is only visible while an item is
selected (GsFileBrowserFragment.java:274).
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

    r = Runner(package=args.package, route="route_19",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E3b54bcd8",
                         "E3d9f32c1", "Ec0e689c4", "E3ee6f9fc", "Edb73b446",
                         "E76d2150f", "E926780be", "Edbac9d51", "E95d059a0",
                         "E8cac44f6"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E211966cc: Tap the Markor launcher icon (process start).
    r.launch("net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: system calls Application.onCreate -- no user action.
    r.comment("Application.onCreate runs by the system", "Ed6414d9f")
    # E0254b914: MAIN/LAUNCHER intent starts MainActivity -- same launch
    # as E211966cc above; no separate user action.
    r.comment("MainActivity started by the E211966cc launch", "E0254b914")
    # Ed25af8f4: system calls Activity.onCreate -- no user action.
    r.comment("Activity.onCreate runs by the system", "Ed25af8f4")
    # Eba46a594: system calls onStart then onResume -- no user action.
    r.comment("onStart/onResume run by the system", "Eba46a594")
    # E659e191c: performResume calls onPostResume -- no user action.
    r.comment("onPostResume runs by the system", "E659e191c")
    # E0ecb8e4d: the notebook tab is the default startup tab, shown
    # after a cold start -- no user action (MainActivity.java:105-106).
    r.comment("Notebook tab shown by default after cold start", "E0ecb8e4d")
    # Preparatory (not an edge): long-press the pushed fixture
    # Documents/notes.md to select it; long click toggles selection
    # (GsFileBrowserListAdapter.java:558-562). Without a selection the
    # Move item stays invisible (GsFileBrowserFragment.java:274).
    r.long_tap("E3b54bcd8", text="notes.md")
    # Preparatory (not an edge): open the overflow menu so the
    # showAsAction="never" Move item becomes tappable.
    r.tap("E3b54bcd8", desc="More options")
    # E3b54bcd8: Tap an item of the notebook toolbar menu -- Move.
    # GsFileBrowserFragment.java:438-441 routes action_move_selected_
    # items to askForMoveOrCopy. Menu title @string/move = "Move"
    # (res/menu/filesystem__menu.xml:52-55, res/values/strings.xml:28).
    r.tap("E3b54bcd8", text="Move")
    # E3d9f32c1: direct call askForMoveOrCopy -- no user action
    # (GsFileBrowserFragment.java:440).
    r.comment("askForMoveOrCopy runs from onOptionsItemSelected",
              "E3d9f32c1")
    # Ec0e689c4: direct call showFolderDialog -- no user action
    # (GsFileBrowserFragment.java:527).
    r.comment("showFolderDialog runs from askForMoveOrCopy", "Ec0e689c4")
    # E3ee6f9fc: direct call showDialog -- no user action
    # (MarkorFileBrowserFactory.java:131).
    r.comment("showDialog runs from showFolderDialog", "E3ee6f9fc")
    # Edb73b446: direct call GsFileBrowserDialog.newInstance -- no user
    # action (MarkorFileBrowserFactory.java:106).
    r.comment("GsFileBrowserDialog.newInstance runs from showDialog",
              "Edb73b446")
    # E76d2150f: framework creates the dialog view -- no user action.
    r.comment("Dialog view created by the framework", "E76d2150f")
    # E926780be: tap the new-folder button in the folder dialog.
    # The button is registered for onClicked in onViewCreated
    # (GsFileBrowserDialog.java:126) and its case calls
    # showNewDirDialog (GsFileBrowserDialog.java:231-233).
    # Res id from res/layout/opoc_filesystem_dialog.xml:69.
    r.tap("E926780be", res_id="ui__filesystem_dialog__new_dir")
    # Edbac9d51: direct call showNewDirDialog -- no user action
    # (GsFileBrowserDialog.java:232).
    r.comment("showNewDirDialog runs from onClicked", "Edbac9d51")
    # E95d059a0: the new-folder dialog's callback fires. The dialog has
    # no positive-button text set (GsFileBrowserDialog.java:232-263
    # sets no okButtonText), so the callback fires on ENTER in the
    # search field (GsSearchOrCustomTextDialog OnKeyListener: ENTER
    # with non-empty text calls dopt.callback, which is
    # _filesystemViewerAdapter.createDirectoryHere).
    r.type_text("new-folder", "E95d059a0")
    r.key("ENTER", "E95d059a0")
    # E8cac44f6: direct call createDirectoryHere -- no user action
    # (GsFileBrowserDialog.java:263, the dialog callback).
    r.comment("createDirectoryHere runs from the dialog callback",
              "E8cac44f6")
    r.done()


if __name__ == "__main__":
    main()
