"""Device route script for Markor route_01.

Method: ActionButtonSettingsActivity.lambda$saveNewOrder$0
Printed route: graphs/Markor/scratch/route_print/route_01.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c E0ecb8e4d
  E54b4aedd Ec433d118 E42444724 E8f245ff4 Eaa1bbd98 Ef379c2e7 E37269db8
  E241ef74f E6664a9b1 E44424d57 Ef3f50818 Ee9f1c197 Ef8d10451 Ed575ae65
  E09fd3f83
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: (none)
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
    "E659e191c", "E0ecb8e4d", "E54b4aedd", "Ec433d118", "E42444724",
    "E8f245ff4", "Eaa1bbd98", "Ef379c2e7", "E37269db8", "E241ef74f",
    "E6664a9b1", "E44424d57", "Ef3f50818", "Ee9f1c197", "Ef8d10451",
    "Ed575ae65", "E09fd3f83",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_01", edge_ids=EDGE_IDS,
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
    # E54b4aedd: Tap a bottom navigation tab.
    # MainActivity.java:109-114 wires the BottomNavigationView listener;
    # res/menu/main__bottom_nav.xml titles the More item "More"
    # (res/values/strings.xml:107).
    r.tap("E54b4aedd", text="More")
    # Ec433d118: Tab More is shown -- no user action.
    r.comment("More tab shown by bottom-nav listener", "Ec433d118")
    # E42444724: Tap a row of the More list (Settings row).
    # MoreInfoFragment.java:65-67: the Settings key starts SettingsActivity;
    # res/xml/prefactions__more_information.xml:34 titles that row "Settings"
    # (res/values/strings.xml:12).
    r.tap("E42444724", text="Settings")
    # E8f245ff4: The Settings row starts SettingsActivity -- no user action;
    # the tap above fires the intent.
    r.comment("Settings row intent starts SettingsActivity", "E8f245ff4")
    # Eaa1bbd98: The system calls Activity.onCreate -- no user action.
    r.comment("system calls Activity.onCreate", "Eaa1bbd98")
    # Ef379c2e7: The system calls onResume (inherited GsActivityBase) -- none.
    r.comment("system calls inherited onResume", "Ef379c2e7")
    # E37269db8: The settings list is shown -- no user action.
    r.comment("settings list shown", "E37269db8")
    # E241ef74f: Tap a row of the settings list (action-button order row).
    # SettingsActivity.java:371: a reorder_actions key starts
    # ActionButtonSettingsActivity. The reorder rows live inside the nested
    # format screens of res/xml/preferences_master.xml (the Markdown screen
    # row there is titled "Action order", res/values/strings.xml:406), so
    # this edge needs two physical taps: enter the Markdown screen, then
    # tap its Action order row. Both taps implement this single route edge.
    r.tap("E241ef74f", text="Markdown")
    r.tap("E241ef74f", text="Action order")
    # E6664a9b1: The action button row starts ActionButtonSettingsActivity
    # -- no user action; the tap above fires the intent.
    r.comment("action order row intent starts ActionButtonSettingsActivity",
              "E6664a9b1")
    # E44424d57: The system calls Activity.onCreate -- no user action.
    r.comment("system calls Activity.onCreate", "E44424d57")
    # Ef3f50818: The system calls onResume (inherited GsActivityBase) -- none.
    r.comment("system calls inherited onResume", "Ef3f50818")
    # Ee9f1c197: The action order list is shown -- no user action.
    r.comment("action order list shown", "Ee9f1c197")
    # Ef8d10451: Press Back (the screen closes and the new order is saved).
    # ActionButtonSettingsActivity.java:112-114: onPause calls saveNewOrder.
    r.back("Ef8d10451")
    # Ed575ae65: onPause calls saveNewOrder directly -- no user action.
    r.comment("onPause calls saveNewOrder directly", "Ed575ae65")
    # E09fd3f83: saveNewOrder's mapping lambda runs while the order is
    # saved -- no user action; it fires as part of the Back press above.
    r.comment("saveNewOrder mapping lambda runs during save", "E09fd3f83")

    r.done()


if __name__ == "__main__":
    main()
