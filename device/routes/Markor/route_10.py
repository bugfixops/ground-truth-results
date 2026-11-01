"""Device route script for Markor route_10.

Method: WikitextLinkResolver.findNotebookRootDir(File,File,boolean)
Edges (in order): E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594
    E659e191c E0ecb8e4d E54b4aedd E80c409ce E3a1cb83b E603cd10f
    Ead3f6294 Eba7d5d98 Ee3753c08 Ec277c5fd E47a807f1 E64965f49
Printed route file: graphs/Markor/scratch/route_print/route_10.txt
ROUTES.csv permissions: none
ROUTES.csv fixtures: Documents/todo.txt (the open todo document; the
    file picked in the browse dialog can be any pushed Documents file)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Path in words: cold-start MainActivity, notebook tab, tap the To-Do
bottom tab, switch the todo document's format to Wikitext, tap the
Insert link action button, tap Browse filesystem in the attach dialog,
pick notes.md in the file browser. Picking the file fills the dialog's
path field; in a wikitext document that goes through
WikitextLinkResolver.resolveSystemFilePath, which calls
findNotebookRootDir. The format switch is a prerequisite for the
wikitext branch (AttachLinkOrFileDialog.java:380-398, wikitext branch
at line 397).
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
    r = Runner(package=args.package, route="route_10",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E54b4aedd",
                         "E80c409ce", "E3a1cb83b", "E603cd10f", "Ead3f6294",
                         "Eba7d5d98", "Ee3753c08", "Ec277c5fd", "E47a807f1",
                         "E64965f49"],
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
    # E54b4aedd -- Tap a bottom navigation tab.
    # Bottom-nav title @string/todo is "To-Do"
    # (res/values/string-not_translatable.xml:42); the listener selects the
    # tab position (MainActivity.java:109-114).
    r.tap("E54b4aedd", text="To-Do")
    # E80c409ce -- Tab Todo is shown (the listener selects its position).
    # No user action: pager state following the tab tap.
    # E3a1cb83b -- Tap an action button in the toolbar of the todo page.
    # Prerequisite: switch the document format to Wikitext while still in
    # edit mode (the format menu is only visible in edit mode,
    # DocumentEditAndViewFragment.java:322): overflow menu -> File Settings
    # (title "File Settings", res/values/strings.xml:436) -> Format (title
    # "Format", res/values/strings.xml:159) -> Wikitext / Zim (title
    # @string/wikitext, res/values/string-not_translatable.xml:367). The
    # format case sets the document format (lines 533-538).
    # Implementing tap: the Insert link action button. Action buttons carry
    # the action's display string as content-desc (ActionButtonBase.java:
    # 343-354); the todo list includes insert_link (TodoTxtActionButtons.
    # java:53) whose display string @string/insert_link is "Insert link"
    # (res/values/strings.xml:79). The click dispatches to onActionClick,
    # whose default branch runs runCommonAction (TodoTxtActionButtons.java:
    # 134), reaching the insert-link case (ActionButtonBase.java:672).
    r.tap("E3a1cb83b", desc="More options")
    r.tap("E3a1cb83b", text="File Settings")
    r.tap("E3a1cb83b", text="Format")
    r.tap("E3a1cb83b", text="Wikitext / Zim")
    r.tap("E3a1cb83b", desc="Insert link")
    # E603cd10f -- Direct call to runCommonAction.
    # No user action: follows from the Insert link tap above.
    # Ead3f6294 -- Direct call to showInsertImageOrLinkDialog.
    # No user action: follows from the Insert link tap above.
    # Eba7d5d98 -- Listener registered by showInsertImageOrLinkDialog runs.
    # Tap Browse filesystem in the attach dialog (button text
    # @string/browse_filesystem, res/values/strings.xml:22; listener set at
    # AttachLinkOrFileDialog.java:155). This opens the file browser.
    r.tap("Eba7d5d98", text="Browse filesystem")
    # Ee3753c08 -- Tap Browse in the attach dialog: the file tapped in the
    # browser is passed to the attach dialog.
    # The browser starts at the todo file's parent folder
    # (AttachLinkOrFileDialog.java:446-456); tap the pushed fixture
    # Documents/notes.md there. ROUTES_NOTES.md leaves this pick unpinned.
    r.tap("Ee3753c08", text="notes.md")
    # Ec277c5fd -- The picked file is put into the dialog fields (setFields).
    # No user action: callback following the file tap above.
    # E47a807f1 -- In a wikitext document, the browsed file becomes a
    # notebook-relative link path (wikitext branch, AttachLinkOrFileDialog.
    # java:380-398, resolveSystemFilePath call at line 397).
    # No user action: follows from the file tap above.
    # E64965f49 -- Direct call to findNotebookRootDir (target method).
    # No user action: follows from the file tap above.
    r.done()


if __name__ == "__main__":
    main()
