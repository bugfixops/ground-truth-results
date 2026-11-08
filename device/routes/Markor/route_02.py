"""Device route script for Markor route_02.

Method: SyntaxHighlighterBase.isFixupOverlap
Printed route: graphs/Markor/scratch/route_print/route_02.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c E0ecb8e4d
  Eba14bdbd E08a94a9d E1e3370f7 E2052a409 E69c12a89 E61ca7c61 Eba99443f
  E4e39442d Ec8eaff3b E091c9edb E08c63a40 E3f2685be Ea060a0d6
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: Documents/notes.md
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
from harness import Runner

EDGE_IDS = [
    "E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4", "Eba46a594",
    "E659e191c", "E0ecb8e4d", "Eba14bdbd", "E08a94a9d", "E1e3370f7",
    "E2052a409", "E69c12a89", "E61ca7c61", "Eba99443f", "E4e39442d",
    "Ec8eaff3b", "E091c9edb", "E08c63a40", "E3f2685be", "Ea060a0d6",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_02", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E211966cc: Tap the Markor launcher icon (process start).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch("net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: The system calls Application.onCreate -- no user action.
    r.comment("system calls Application.onCreate", "Ed6414d9f")
    # E0254b914: The MAIN/LAUNCHER intent starts MainActivity -- no separate
    # action; the same launcher tap as E211966cc starts it.
    r.comment("same launcher tap as E211966cc starts MainActivity", "E0254b914")
    # Ed25af8f4: The system calls Activity.onCreate -- no user action.
    r.comment("system calls Activity.onCreate", "Ed25af8f4")
    # Eba46a594: The system calls Activity.onStart then onResume -- no action.
    r.comment("system calls onStart then onResume", "Eba46a594")
    # E659e191c: Activity.performResume calls onPostResume -- no user action.
    r.comment("system calls onPostResume", "E659e191c")
    # E0ecb8e4d: The notebook tab is the default startup tab -- no user action.
    r.comment("notebook tab shown by default after cold start", "E0ecb8e4d")
    # Eba14bdbd: Tap a file in the notebook list.
    # GsFileBrowserListAdapter.java:404-416: a file row tap goes to the
    # notebook listener (a folder would open instead). Fixture file tapped:
    # Documents/notes.md (pushed by run_app.sh per ROUTES.csv).
    r.tap("Eba14bdbd", text="notes.md")
    # E08a94a9d: Interface call to the notebook listener -- no user action.
    r.comment("file tap dispatches to notebook listener", "E08a94a9d")
    # E1e3370f7: Direct call to DocumentActivity.launch -- no user action.
    r.comment("direct call to DocumentActivity.launch", "E1e3370f7")
    # E2052a409: Direct call to the 5-arg launch overload -- no user action.
    r.comment("direct call to 5-arg launch overload", "E2052a409")
    # E69c12a89: The app starts DocumentActivity with an explicit intent
    # (DocumentActivity.java:116) -- no user action; the file tap caused it.
    r.comment("explicit intent starts DocumentActivity", "E69c12a89")
    # E61ca7c61: The system calls Activity.onCreate -- no user action.
    r.comment("system calls Activity.onCreate", "E61ca7c61")
    # Eba99443f: onCreate hands the intent to handleLaunchingIntent -- none.
    r.comment("onCreate calls handleLaunchingIntent", "Eba99443f")
    # E4e39442d: The editor fragment is committed, activity resumes -- none.
    r.comment("editor committed then activity resumes", "E4e39442d")
    # Ec8eaff3b: The editor of the file is shown -- no user action.
    r.comment("document editor shown", "Ec8eaff3b")
    # E091c9edb: Type or delete text in the document.
    # HighlightingEditor.java:94-103: the TextWatcher onTextChanged calls
    # _hl.fixup, which chains to isFixupOverlap. The editor holds focus
    # after the document opens, so typing goes to it.
    r.type_text("test text", "E091c9edb")
    # E08c63a40: onTextChanged calls fixup directly -- no user action.
    r.comment("onTextChanged calls fixup directly", "E08c63a40")
    # E3f2685be: fixup(int,int,int) calls fixup(int,int) -- no user action.
    r.comment("fixup 3-arg calls fixup 2-arg", "E3f2685be")
    # Ea060a0d6: fixup(int,int) calls isFixupOverlap -- no user action.
    r.comment("fixup calls isFixupOverlap", "Ea060a0d6")

    r.done()


if __name__ == "__main__":
    main()
