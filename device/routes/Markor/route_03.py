"""Device route script for Markor route_03.

Method: SyntaxHighlighterBase$1.draw
Printed route: graphs/Markor/scratch/route_print/route_03.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c E0ecb8e4d
  E54b4aedd E80c409ce Ea2691dfc E35d728d0 E6ffdfc03 E393236ff Ef889e907
  Ec2ab97a3 E519a7b85 Effd5ff23 Eb50f217f E9304813e E490aa39b
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: Documents/todo.txt
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
    "E659e191c", "E0ecb8e4d", "E54b4aedd", "E80c409ce", "Ea2691dfc",
    "E35d728d0", "E6ffdfc03", "E393236ff", "Ef889e907", "Ec2ab97a3",
    "E519a7b85", "Effd5ff23", "Eb50f217f", "E9304813e", "E490aa39b",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
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
    # E54b4aedd: Tap a bottom navigation tab (Todo).
    # MainActivity.java:109-114 wires the BottomNavigationView listener and
    # MainActivity.java:518 builds the Todo tab from the configured todo
    # file; res/menu/main__bottom_nav.xml titles it with @string/todo,
    # whose value is "To-Do" (res/values/string-not_translatable.xml:42).
    # Fixture: Documents/todo.txt (pushed by run_app.sh per ROUTES.csv) is
    # the open todo document; no file tap is needed, the tab opens it.
    r.tap("E54b4aedd", text="To-Do")
    # E80c409ce: Tab Todo is shown -- no user action.
    r.comment("Todo tab shown by bottom-nav listener", "E80c409ce")
    # Ea2691dfc: Tap an item of the editor menu (format menu, key-value).
    # DocumentEditAndViewFragment.java:535: a format menu item calls
    # applyTextFormat. The format submenu lives in the overflow menu
    # (res/menu/document__edit__menu.xml:108-119: "Format" submenu holding
    # the item titled "Key - Value", res/values/string-not_translatable
    # .xml:385), so this single route edge needs three physical taps:
    # open the overflow menu, open the Format submenu, pick Key - Value.
    r.tap("Ea2691dfc", desc="More options")
    r.tap("Ea2691dfc", text="Format")
    r.tap("Ea2691dfc", text="Key - Value")
    # E35d728d0: onOptionsItemSelected calls applyTextFormat -- no action.
    r.comment("menu item calls applyTextFormat", "E35d728d0")
    # E6ffdfc03: applyTextFormat calls setHighlighter -- no user action.
    r.comment("applyTextFormat calls setHighlighter", "E6ffdfc03")
    # E393236ff: setHighlighter triggers async recompute -- framework-driven.
    r.comment("setHighlighter triggers async recompute", "E393236ff")
    # Ef889e907: Async recompute runs the worker -- framework-driven.
    r.comment("async recompute runs worker", "Ef889e907")
    # Ec2ab97a3: Worker calls SyntaxHighlighterBase.compute -- no action.
    r.comment("worker calls compute", "Ec2ab97a3")
    # E519a7b85: compute calls generateSpans virtually; the key-value
    # format uses KeyValueSyntaxHighlighter (FormatRegistry.java:169).
    # State: the open document now uses the key-value format, chosen by
    # the format menu taps above -- no further user action.
    r.comment("compute dispatches to KeyValue generateSpans", "E519a7b85")
    # Effd5ff23: generateSpans calls createTabSpans -- no user action.
    r.comment("generateSpans calls createTabSpans", "Effd5ff23")
    # Eb50f217f: createTabSpans calls createReplacementSpanForMatches -- none.
    r.comment("createTabSpans calls createReplacementSpanForMatches",
              "Eb50f217f")
    # E9304813e: Framework lambda registered by createReplacementSpanForMatches
    # runs -- no user action.
    r.comment("replacement-span lambda runs", "E9304813e")
    # E490aa39b: The framework draws the replacement span ($1.draw) when
    # the editor redraws after the format switch -- no user action.
    r.comment("framework draws replacement span", "E490aa39b")

    r.done()


if __name__ == "__main__":
    main()
