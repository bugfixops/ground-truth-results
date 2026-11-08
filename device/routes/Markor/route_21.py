"""Device route script: route_21.

Method: SyntaxHighlighterBase$SpanGroup.compareTo
Printed route file: graphs/Markor/scratch/route_print/route_21.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c
  E0ecb8e4d E54b4aedd E80c409ce Ea2691dfc E3ecdfe9d Ea408130e
  E37b1f97b Eb2ebd8bf E6c43423f E6e6ed335 E0fecccb6 Eae742bba
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: Documents/todo.txt
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Replay: cold-start MainActivity, switch to the To-Do tab, open the
editor search, and type a word from the pushed Documents/todo.txt
fixture ("Finish report") so the text search produces matches whose
highlight spans are sorted via SpanGroup.compareTo.
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
    r = Runner(package=args.package, route="route_21",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E54b4aedd",
                         "E80c409ce", "Ea2691dfc", "E3ecdfe9d", "Ea408130e",
                         "E37b1f97b", "Eb2ebd8bf", "E6c43423f", "E6e6ed335",
                         "E0fecccb6", "Eae742bba"],
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
    # bottom navigation is visible; the "To-Do" label is the nav item
    # title (res/menu/main__bottom_nav.xml nav_todo, title @string/todo
    # = "To-Do" in res/values/string-not_translatable.xml:42).
    r.wait_for("E0ecb8e4d", text="To-Do")
    # E54b4aedd: Tap a bottom navigation tab -- the To-Do tab.
    # MainActivity.java:109-114: the listener maps the item to a pager
    # position and selects it.
    r.tap("E54b4aedd", text="To-Do")
    # E80c409ce: Tab Todo is shown by the pager as a consequence of
    # the tap above -- no further action.
    r.comment("Todo page shown by the pager after the tab tap, no action",
              "E80c409ce")
    # Ea2691dfc: Tap an item of the editor menu (todo or quick note).
    # The edit-mode menu item action_search (res/menu/
    # document__edit__menu.xml:53-56, title @string/search = "Search")
    # reaches DocumentEditAndViewFragment.onOptionsItemSelected, whose
    # action_search case calls _format.getActions().onSearch()
    # (DocumentEditAndViewFragment.java:542).
    r.tap("Ea2691dfc", desc="Search")
    # E3ecdfe9d: ActionButtonBase.onSearch -- direct call, no action.
    r.comment("direct call: ActionButtonBase.onSearch, no user action",
              "E3ecdfe9d")
    # Ea408130e: TextSearchFragment.show -- direct call; the search UI
    # it shows contains the search box (res/layout/
    # text_search_fragment.xml:126, @+id/searchEditText). Focus it so
    # the following typed text lands in the search box.
    r.tap("Ea408130e", res_id="searchEditText")
    # E37b1f97b: TextSearchFragment.find2 -- the search runs over the
    # open todo document. Type a word from the pushed fixture
    # Documents/todo.txt ("Finish report") so the search produces
    # matches; typing in the search box drives the fragment's search
    # (TextSearchFragment.java:323 find path via the text watcher /
    # show-time find2). No fixture is pushed here; run_app.sh does it.
    r.type_text("report", "E37b1f97b")
    # Eb2ebd8bf: TextSearchHandler.find -- direct call, no action.
    r.comment("direct call: TextSearchHandler.find, no user action",
              "Eb2ebd8bf")
    # E6c43423f: TextSearchHandler.loadMatches -- direct call, no action.
    r.comment("direct call: TextSearchHandler.loadMatches, no user action",
              "E6c43423f")
    # E6e6ed335: Match.<init> -- direct call, no user action.
    r.comment("direct call: Match.<init>, no user action", "E6e6ed335")
    # E0fecccb6: SyntaxHighlighterBase.createBackgroundHighlight --
    # direct call, no user action.
    r.comment("direct call: createBackgroundHighlight, no user action",
              "E0fecccb6")
    # Eae742bba: SyntaxHighlighterBase$SpanGroup.compareTo -- framework
    # sorting callback on the highlight spans created above; the system
    # / library invokes it, no user action.
    r.comment("framework callback: SpanGroup.compareTo sorting, no action",
              "Eae742bba")
    r.done()


if __name__ == "__main__":
    main()
