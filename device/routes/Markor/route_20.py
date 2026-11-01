"""Markor route_20: AppSettings.lambda$getPopularDocumentsSorted$1.

Edge ids in order: E211966cc, Ed6414d9f, E0254b914, Ed25af8f4, Eba46a594,
E659e191c, E0ecb8e4d, E54b4aedd, E80c409ce, Ea2691dfc, Ee0c056ee, Ee551d2e2,
Eb41d29b1, E269c7326, E9d83475c, E41ae1a1f, E3df3a9a7, Ec9766d60, E7c70b6a2.
Printed route file: graphs/Markor/scratch/route_print/route_20.txt.
ROUTES.csv permissions: none. Fixtures: Documents/todo.txt (pushed by
run_app.sh; the script itself never pushes fixtures -- the Todo tab
opens that pushed file as the app's todo document).
Setup: push fixtures/Documents; first-run tutorial can trap a tool.
Package: net.gsantner.markor_test.

Flow: launch MainActivity, tap the Todo bottom tab (the Todo page opens
the app's todo document), open the editor menu and tap Info, then tap
the "list in recent files" checkbox in the info dialog. Toggling that
checkbox calls setListFileInRecents (FileInfoDialog.java:126), which
flows through setRecentDocuments to getPopularDocumentsSorted and its
sort comparator (AppSettings.java:626, 638, 875).
Caveat: the checkbox tap toggles rather than forces a checked state;
the listener fires on either toggle, which is what this route needs.
The Info item is showAsAction="never"
(res/menu/document__edit__menu.xml:235-238), so the overflow menu is
opened first as a labelled preparatory tap (not a route edge).
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

    r = Runner(package=args.package, route="route_20",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E54b4aedd",
                         "E80c409ce", "Ea2691dfc", "Ee0c056ee", "Ee551d2e2",
                         "Eb41d29b1", "E269c7326", "E9d83475c", "E41ae1a1f",
                         "E3df3a9a7", "Ec9766d60", "E7c70b6a2"],
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
    # E54b4aedd: Tap a bottom navigation tab -- Todo.
    # Bottom-nav label is @string/todo = "To-Do"
    # (res/menu/main__bottom_nav.xml, res/values/string-not_translatable.xml:42).
    r.tap("E54b4aedd", text="To-Do")
    # E80c409ce: the Todo tab is shown -- no user action; the listener
    # selects its position and the Todo page opens the app's todo
    # document (MainActivity.java:109-114 and the nav_todo branch).
    r.comment("Todo page shown by the tab listener", "E80c409ce")
    # Preparatory (not an edge): open the overflow menu so the
    # showAsAction="never" Info item becomes tappable.
    r.tap("Ea2691dfc", desc="More options")
    # Ea2691dfc: Tap an item of the editor menu -- Info.
    # DocumentEditAndViewFragment.java:606 routes action_info to
    # FileInfoDialog.show. Menu title @string/info = "Info"
    # (res/menu/document__edit__menu.xml:235-238,
    # res/values/strings.xml:29).
    r.tap("Ea2691dfc", text="Info")
    # Ee0c056ee: direct call FileInfoDialog.show -- no user action
    # (DocumentEditAndViewFragment.java:606).
    r.comment("FileInfoDialog.show runs from onOptionsItemSelected",
              "Ee0c056ee")
    # Ee551d2e2: direct call FileInfoDialog.newInstance -- no user
    # action (FileInfoDialog.java:50).
    r.comment("FileInfoDialog.newInstance runs from show", "Ee551d2e2")
    # Eb41d29b1: framework calls onCreateDialog on the created dialog
    # -- no user action (FileInfoDialog.java:61).
    r.comment("onCreateDialog runs by the framework", "Eb41d29b1")
    # E269c7326: direct call setUpDialog -- no user action
    # (FileInfoDialog.java:61).
    r.comment("setUpDialog runs from onCreateDialog", "E269c7326")
    # E9d83475c: tap the "list in recent files" checkbox in the info
    # dialog; its OnCheckedChangeListener calls setListFileInRecents
    # (FileInfoDialog.java:124-126). Res id from
    # res/layout/file_info_dialog.xml:199.
    r.tap("E9d83475c", res_id="ui__fileinfodialog__recents")
    # E41ae1a1f: direct call setListFileInRecents -- no user action
    # (FileInfoDialog.java:126).
    r.comment("setListFileInRecents runs from the checkbox listener",
              "E41ae1a1f")
    # E3df3a9a7: direct call setRecentDocuments -- no user action
    # (AppSettings.java:875).
    r.comment("setRecentDocuments runs from setListFileInRecents",
              "E3df3a9a7")
    # Ec9766d60: direct call getPopularDocumentsSorted -- no user
    # action (AppSettings.java:638).
    r.comment("getPopularDocumentsSorted runs from setRecentDocuments",
              "Ec9766d60")
    # E7c70b6a2: the sort comparator lambda in
    # getPopularDocumentsSorted runs -- no user action
    # (AppSettings.java:626).
    r.comment("Sort comparator runs inside getPopularDocumentsSorted",
              "E7c70b6a2")
    r.done()


if __name__ == "__main__":
    main()
