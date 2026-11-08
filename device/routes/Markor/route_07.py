"""Device route script for Markor route_07.

Method: DocumentEditAndViewFragment$2.lambda$search$0
Edges (in order): E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594
    E659e191c E0ecb8e4d E54b4aedd Eb6c73931 Ed0815705 E4cbf1ab4
    E40cadc21 E8122e9a5 Ee25007ce E89a53091 Ea25aa01b E2f2d66bd
    Ee582196d
Printed route file: graphs/Markor/scratch/route_print/route_07.txt
ROUTES.csv permissions: none
ROUTES.csv fixtures: Documents/todo.txt (the open todo document)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Path in words: cold-start MainActivity, notebook tab, tap the To-Do
bottom tab, switch the todo page to View Mode (preview), expand the
SearchView and type a query. The search listener is set only in view
mode (DocumentEditAndViewFragment.java:697-702); typing fires
onQueryTextChange, whose debounced task (500 ms, lines 707-711) runs
findAllAsync and reaches lambda$search$0. The query "milk" matches
"Buy milk" in the pushed Documents/todo.txt fixture.
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
    r = Runner(package=args.package, route="route_07",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E54b4aedd",
                         "Eb6c73931", "Ed0815705", "E4cbf1ab4", "E40cadc21",
                         "E8122e9a5", "Ee25007ce", "E89a53091", "Ea25aa01b",
                         "E2f2d66bd", "Ee582196d"],
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
    # Eb6c73931 -- The pager calls the page-change callback after setCurrentItem.
    # No user action: framework callback following the tab tap.
    # Ed0815705 -- Direct call to onViewPagerPageSelected.
    # No user action: follows from the tab tap above.
    # E4cbf1ab4 -- The pager creates the todo page; FragmentManager runs onCreate.
    # No user action: framework lifecycle step.
    # E40cadc21 -- The FragmentManager creates the page view.
    # No user action: framework lifecycle step.
    # E8122e9a5 -- The FragmentManager resumes the visible page.
    # No user action: framework lifecycle step.
    # Ee25007ce -- The page adds its editor menu to the toolbar once resumed.
    # No user action: framework step; the menu is built by the system.
    # E89a53091 -- Direct call to setupSearchView from onCreateOptionsMenu.
    # No user action: direct call, not a UI step. Note the search listener
    # is only registered when the page is in preview mode, so the block
    # below switches to View Mode first.
    # Ea25aa01b -- The search view calls its query listener when text changes
    # (listener set only in view mode, DocumentEditAndViewFragment.java:
    # 697-702).
    # Prerequisite 1: tap View Mode (action_preview case, lines 454-456;
    # menu title @string/view_mode is "View Mode", res/values/strings.xml:
    # 326). This makes action_search_view visible (line 321) and registers
    # the listener via setupSearchView (line 332).
    # Prerequisite 2: expand the SearchView (action_search_view,
    # res/menu/document__edit__menu.xml action_search_view item).
    # Implementing step: type the query; each change fires onQueryTextChange.
    r.tap("Ea25aa01b", desc="View Mode")
    r.tap("Ea25aa01b", desc="Search")
    r.type_text("milk", "Ea25aa01b")
    # E2f2d66bd -- Direct call from onQueryTextChange to search.
    # No user action: follows from typing the query above.
    # Ee582196d -- The debounced task (500 ms) runs the web-view search.
    # No user action: timer callback following the typed query
    # (DocumentEditAndViewFragment.java:707-711).
    r.done()


if __name__ == "__main__":
    main()
