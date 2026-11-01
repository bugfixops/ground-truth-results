#!/usr/bin/env python3
"""AnyMemo route_16: AlgorithmCustomizationScreen$1$1.<init>.

Method: AlgorithmCustomizationScreen$1$1.<init>
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E61565a0d Ea1315438
    Eaca59498 Ebfe5218f Ea2fed85c E5bca89c8 E10650dad E98d4b43a
    E209e1e2e E93241413 E42d7661c E14933b48
Printed route source:
    graphs/AnyMemo/scratch/route_print/AlgorithmCustomizationScreen_1_1.<init>.txt
    plus graphs/AnyMemo/out/anymemo_trigger_graph.json edges above.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: none listed for this route in ROUTES.csv.
Setup: none beyond a fresh install (pm clear by run_app.sh). No deck
    or card state is needed: the route only walks preferences screens.

REAL-RUN CAVEAT (drawer): the printed edge E61565a0d is the
NavigationView drawer listener (AnyMemo$1, AnyMemo.java:209-232),
reached by tapping a drawer entry. The drawer starts closed, and the
harness offers no drawer-open gesture (no swipe primitive; a
fixed-coordinate tap is a tap, not an edge swipe), so this script
taps the "Options" drawer entry directly (title option_button_text
from menu/main_screen_drawer_menu.xml). On a real run the drawer
must be opened first (e.g. via the toolbar hamburger) or this tap
will not resolve. Fallback if it does not resolve: the Misc tab's
Options button (layout id misc_options) starts the same
OptionScreen (MiscTabFragment optionButton branch); the rest of
the script is unchanged. That fallback is NOT scripted here because
the printed edge names the drawer entry.
"""

import argparse
import os
import sys

_HERE = os.path.abspath(__file__)
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(_HERE))))
if not os.path.isfile(os.path.join(_ROOT, "device", "harness",
                                   "harness.py")):
    # Fallback for staging/helper layouts: walk up looking for a
    # device/harness dir, including the stage/device staging root.
    _d = os.path.dirname(_HERE)
    while True:
        if os.path.isfile(os.path.join(_d, "device", "harness",
                                       "harness.py")):
            _ROOT = _d
            break
        if os.path.isfile(os.path.join(_d, "device", "stage", "device",
                                       "harness", "harness.py")):
            _ROOT = os.path.join(_d, "device", "stage")
            break
        _parent = os.path.dirname(_d)
        if _parent == _d:
            break
        _d = _parent
sys.path.insert(0, _ROOT)

from device.harness import Runner

COMPONENT = ("org.liberty.android.fantastischmemopro/"
             "org.liberty.android.fantastischmemopro.ui.AnyMemo")

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E61565a0d", "Ea1315438", "Eaca59498", "Ebfe5218f", "Ea2fed85c",
    "E5bca89c8", "E10650dad", "E98d4b43a", "E209e1e2e", "E93241413",
    "E42d7661c", "E14933b48",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_16", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(COMPONENT, edge="Eddc920eb")
        # Ee33f0797: Activity lifecycle / framework callback.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E0b0115b9: onCreate: API <= 29 and WRITE_EXTERNAL_STORAGE
        # already granted, so loadUiComponents() runs.
        r.comment("permission pre-granted by run_app.sh; "
                  "loadUiComponents() runs", edge="E0b0115b9")
        # Ed9aa2280: initDrawer().
        r.comment("loadUiComponents calls initDrawer()", edge="Ed9aa2280")
        # Efe6c7871: bottomNavigation.setSelectedItemId(recent_tab_menu)
        # selects the Recent tab by default on a cold start.
        r.comment("bottom nav selects the Recent tab by default",
                  edge="Efe6c7871")
        # E006becde: Direct call to RecentListFragment.
        r.comment("bottom-nav listener creates RecentListFragment",
                  edge="E006becde")
        # E48c9d4a5: Fragment lifecycle callback.
        r.comment("FragmentManager calls onAttach", edge="E48c9d4a5")
        # Ef4267162: Fragment lifecycle callback.
        r.comment("FragmentManager calls onCreate", edge="Ef4267162")
        # E25e1518b: Fragment lifecycle callback.
        r.comment("FragmentManager calls onCreateView", edge="E25e1518b")
        # E690f7694: The Recent tab is shown once its view exists.
        r.comment("Recent tab shown", edge="E690f7694")
        # E61565a0d: Swipe in the drawer, tap a drawer entry (Recent
        # / Open / Download / Misc / Options / About). The Options
        # entry title is option_button_text ("Options") in
        # menu/main_screen_drawer_menu.xml. See the header caveat:
        # the drawer must be open for this tap to resolve.
        r.tap(edge="E61565a0d", text="Options")
        # Ea1315438: startActivity(OptionScreen) for the Options
        # drawer item.
        r.comment("drawer Options entry starts OptionScreen",
                  edge="Ea1315438")
        # Eaca59498: the system creates the activity and calls
        # onCreate (PreferenceActivity).
        r.comment("system instantiates OptionScreen, then onCreate",
                  edge="Eaca59498")
        # Ebfe5218f: addPreferencesFromResource(option_screen).
        r.comment("OptionScreen loads res/xml/option_screen.xml",
                  edge="Ebfe5218f")
        # Ea2fed85c: Tap "Customize scheduling algorithm"
        # (customize_scheduling_algorithm_text in option_screen.xml,
        # key customize_scheduling_algorithm_key).
        r.tap(edge="Ea2fed85c", text="Customize scheduling algorithm")
        # E5bca89c8: the warning dialog is shown (title warning_text,
        # message customize_scheduling_algorithm_warning).
        r.comment("OptionScreen shows the algorithm warning dialog",
                  edge="E5bca89c8")
        # E10650dad: Tap OK (open the algorithm screen). The dialog
        # positive button text is ok_text ("OK").
        r.tap(edge="E10650dad", text="OK")
        # E98d4b43a: startActivity(AlgorithmCustomizationScreen).
        r.comment("OK click starts AlgorithmCustomizationScreen",
                  edge="E98d4b43a")
        # E209e1e2e: the system creates the activity and calls
        # onCreate (PreferenceActivity).
        r.comment("system instantiates AlgorithmCustomizationScreen, "
                  "then onCreate", edge="E209e1e2e")
        # E93241413: addPreferencesFromResource
        # (algorithm_customization_screen).
        r.comment("AlgorithmCustomizationScreen loads "
                  "res/xml/algorithm_customization_screen.xml",
                  edge="E93241413")
        # E42d7661c: Tap "Reset customized algorithm"
        # (reset_customized_scheduling_algorithm_text in
        # algorithm_customization_screen.xml, key
        # reset_customized_scheduling_algorithm).
        r.tap(edge="E42d7661c",
              text="Reset customized scheduling algorithm")
        # E14933b48: Direct call to AlgorithmCustomizationScreen$1$1
        # .<init>. The $1$1 object is the dialog's positive-button
        # OnClickListener, instantiated when onPreferenceClick builds
        # the warning dialog (AlgorithmCustomizationScreen.java
        # :62-78) -- i.e. by the preference tap above, before any OK
        # tap. The target method is therefore already reached; the
        # OK tap below only dismisses the dialog (its onClick calls
        # finish() and resets the parameters).
        r.comment("$1$1 listener instantiated by the preference tap "
                  "building the dialog", edge="E14933b48")
        r.tap(edge="E14933b48", text="OK")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
