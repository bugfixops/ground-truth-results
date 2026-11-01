"""Device replay script for openlauncher route_22.

Method: GestureAnalyser.<init>(int,int,int)
Edge ids, in ROUTES.csv order:
    E3a1527b1 E996c92b8 E5aa97973 E8b7dd43a E23660de0 E1701006d Ecded7dff
    E6c305cd5 E460ef627 E5f090eaa E9e80a447 Ecc441e90 E70364911 E8aa7a78a
    Eb8482982 E00091e44 E0e46ed29
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (GestureAnalyser section), cross-checked
    against graphs/openlauncher/out/openlauncher_trigger_graph.json and the
    verification.csv path row for this method.
Permissions: none (ROUTES.csv permissions cell empty).
Fixtures: none (ROUTES.csv fixtures cell empty).
Setup: none (ROUTES.csv setup cell empty). run_app.sh clears the app
    (pm clear) before invoking this script, so the first-start onboarding
    is shown and the Skip tap below applies.

Package: com.benny.openlauncher (AndroidManifest.xml package attribute;
    launcher activity com.benny.openlauncher.activity.Init, manifest lines
    28-36, MAIN + LAUNCHER filter).
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# The script lives at device/routes/openlauncher/route_22.py, so the repo
# root is three directories up from the script's containing directory:
# openlauncher/ -> routes/ -> device/ -> repo root. (Four dirname calls
# in total counting _HERE: _HERE is already one level below routes/.)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner

EDGE_IDS = [
    "E3a1527b1", "E996c92b8", "E5aa97973", "E8b7dd43a", "E23660de0",
    "E1701006d", "Ecded7dff", "E6c305cd5", "E460ef627", "E5f090eaa",
    "E9e80a447", "Ecc441e90", "E70364911", "E8aa7a78a", "Eb8482982",
    "E00091e44", "E0e46ed29",
]

INIT_COMPONENT = "com.benny.openlauncher/com.benny.openlauncher.activity.Init"


def main(argv=None):
    parser = argparse.ArgumentParser(description="openlauncher route_22")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_22", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E3a1527b1 -- Tap the OpenLauncher icon in another launcher
    # (MAIN + LAUNCHER filter), or adb monkey / am start.
    # The trigger text itself allows am start, so launch the MAIN/LAUNCHER
    # activity directly. This starts the app process.
    r.launch(component=INIT_COMPONENT, edge="E3a1527b1")

    # E996c92b8 -- The system instantiates Init, then calls onCreate.
    # Lifecycle edge, no user action.
    r.comment("system instantiates Init then calls onCreate; no user action",
              "E996c92b8")

    # E5aa97973 -- First start: the three onboarding pages are set up.
    # Guard getBoolean("firstStart", true) holds on the fresh install
    # (run_app.sh cleared the app first). Page setup, no user action.
    r.comment("first start: onboarding pages set up; no user action",
              "E5aa97973")

    # E8b7dd43a -- Tap Skip.
    # Selector: text "Skip". Init.java sets the skip button title from
    # strings.xml intro_skip ("Skip") via setSkipButtonTitle
    # (activity/Init.java:53). The OnboarderActivity library layout is not
    # among the inputs, so no button resource-id is known; text is the
    # only grounded selector (see REPORT.md).
    r.tap(edge="E8b7dd43a", text="Skip")

    # E23660de0 -- Direct call: onSkipButtonPressed calls RockIt.
    # Framework/call edge, no user action.
    r.comment("onSkipButtonPressed calls RockIt directly; no user action",
              "E23660de0")

    # E1701006d -- startActivity(new Intent(Init.this, Home.class)) then
    # finish(). Intent edge driven by the app itself, no user action.
    r.comment("RockIt starts Home then finishes Init; no user action",
              "E1701006d")

    # Ecded7dff -- The system instantiates Home, then calls onCreate.
    # Lifecycle edge, no user action.
    r.comment("system instantiates Home then calls onCreate; no user action",
              "Ecded7dff")

    # E6c305cd5 -- new AsyncTask().execute(): LauncherSettings.readSettings
    # runs on a worker thread (Home.java:205-228). Async edge, no action.
    r.comment("Home.onCreate starts settings AsyncTask; no user action",
              "E6c305cd5")

    # E460ef627 -- The settings are read: onPostExecute runs on the main
    # thread. Async edge, no user action.
    r.comment("settings AsyncTask onPostExecute on main thread; no action",
              "E460ef627")

    # E5f090eaa -- Direct call (through Home.access$200): onPostExecute
    # calls Home.init. Call edge, no user action.
    r.comment("onPostExecute calls Home.init directly; no user action",
              "E5f090eaa")

    # E9e80a447 -- Direct call: Home.init calls Home.initViews.
    # Call edge, no user action.
    r.comment("Home.init calls initViews directly; no user action",
              "E9e80a447")

    # Ecc441e90 -- Direct call: Home.initViews calls Desktop.init
    # (Home.java:313). Call edge, no user action.
    r.comment("initViews calls Desktop.init directly; no user action",
              "Ecc441e90")

    # E70364911 -- Direct call: Desktop.init creates the DesktopAdapter
    # (widget/Desktop.java:82). Call edge, no user action.
    r.comment("Desktop.init creates DesktopAdapter; no user action",
              "E70364911")

    # E8aa7a78a -- Direct call: DesktopAdapter constructor calls
    # getItemLayout (widget/Desktop.java:346). Call edge, no user action.
    r.comment("DesktopAdapter constructor calls getItemLayout; no action",
              "E8aa7a78a")

    # Eb8482982 -- Direct call: getItemLayout creates SimpleFingerGestures
    # (widget/Desktop.java:460). Call edge, no user action.
    r.comment("getItemLayout creates SimpleFingerGestures; no user action",
              "Eb8482982")

    # E00091e44 -- Direct call: SimpleFingerGestures constructor creates
    # GestureAnalyser (SimpleFingerGestures.java:44). Call edge, no action.
    r.comment("SimpleFingerGestures constructor creates GestureAnalyser",
              "E00091e44")

    # E0e46ed29 -- Direct call: GestureAnalyser() delegates to
    # GestureAnalyser(int,int,int) (GestureAnalyser.java:74). This is the
    # route target; it is reached during Home init with no further UI.
    r.comment("GestureAnalyser() delegates to 3-arg constructor; target",
              "E0e46ed29")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
