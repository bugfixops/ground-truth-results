"""Device route script for Markor route_06.

Method: FlexmarkKatexExtension$KatexInlineMath.getText
Edges (in order): E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594
    E659e191c E0ecb8e4d E3b54bcd8 Ed7e97140 E487ed32a Ec394a80e
    Ef85b957f E9d9ec918 E7010cfd5 E7f7c46e0 E709569fd E3b3724dd
Printed route file: graphs/Markor/scratch/route_print/route_06.txt
ROUTES.csv permissions: none
ROUTES.csv fixtures: Documents/notes.md (the selected notebook file)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Path in words: cold-start MainActivity, notebook tab, long-press
notes.md to select it, overflow menu, tap Clipboard. The Clipboard case
calls FormatRegistry.isFileSupported, which loads FormatRegistry and
MarkdownTextConverter and creates the Katex extension, whose renderer
renders an inline-math node and calls KatexInlineMath.getText.
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
    r = Runner(package=args.package, route="route_06",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E3b54bcd8",
                         "Ed7e97140", "E487ed32a", "Ec394a80e", "Ef85b957f",
                         "E9d9ec918", "E7010cfd5", "E7f7c46e0", "E709569fd",
                         "E3b3724dd"],
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
    # E3b54bcd8 -- Tap an item of the notebook toolbar menu.
    # Prerequisite: long-press the pushed fixture Documents/notes.md to
    # select it. Long click toggles selection (GsFileBrowserListAdapter.java:
    # 555-563) and only then is the copy item visible: updateMenuItems
    # shows action_fs_copy_to_clipboard for exactly one selected text file
    # (GsFileBrowserFragment.java:283). Then open the overflow menu and tap
    # Clipboard (menu title @string/clipboard, res/values/strings.xml:231),
    # which fires the action_fs_copy_to_clipboard case
    # (GsFileBrowserFragment.java:472-478).
    r.long_tap("E3b54bcd8", text="notes.md")
    r.tap("E3b54bcd8", desc="More options")
    r.tap("E3b54bcd8", text="Clipboard")
    # Ed7e97140 -- Direct call into FormatRegistry (class load).
    # No user action: follows from the Clipboard tap above.
    # E487ed32a -- Direct call into MarkdownTextConverter (class load).
    # No user action: follows from the Clipboard tap above.
    # Ec394a80e -- Direct call to KatexExtension.create.
    # No user action: follows from the Clipboard tap above.
    # Ef85b957f -- Framework/library calls extend on the created object.
    # No user action: library callback, not a UI step.
    # E9d9ec918 -- Framework/library calls Factory.create.
    # No user action: library callback, not a UI step.
    # E7010cfd5 -- Framework/library calls getNodeRenderingHandlers.
    # No user action: library callback, not a UI step.
    # E7f7c46e0 -- Framework/library calls the renderer render method.
    # No user action: library callback, not a UI step.
    # E709569fd -- Direct call to KatexNodeRenderer.render.
    # No user action: follows from the Clipboard tap above.
    # E3b3724dd -- Direct call to KatexInlineMath.getText (target method).
    # No user action: follows from the Clipboard tap above.
    r.done()


if __name__ == "__main__":
    main()
