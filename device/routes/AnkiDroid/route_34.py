#!/usr/bin/env python3
"""AnkiDroid step2-item3 route_34: UIUtils$1.onPostExecute.

Method: UIUtils$1.onPostExecute
Table verdict: CORRECT (combined-merge redraw, route_table.md
    row 24). Final-sample method, new to the device set (not in
    the Push-2 ROUTES.csv); route number 34 is new, so no existing
    route number is rebound.
Route followed: the final BFS route (11 steps), identical to the
    redraw print (newsample-routes-30.log): deck picker -> HOME
    key backgrounds the app (onPause/onStop) -> saveCollectionInBackground
    -> SAVE_COLLECTION task -> onPostExecute chain -> UIUtils$1.onPostExecute.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b E553ad2d8 Eb8a794fb Ef82c95ca
    Ec788bd08 E1d7dbff0 Ea01eda48 Ea2b5de1a Ebff1608e
Preconditions/fixtures:
  - Collection open. No file fixture is pushed.
Mapping notes:
  - The HOME key for the onResume -> onPause edge follows the
    shipped route_22.py precedent (same edge Eb8a794fb, same
    key). Backgrounding (not back) is used so the activity
    stops without finishing.
  - No live run is claimed by this script.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "Eb8a794fb",
    "Ef82c95ca", "Ec788bd08", "E1d7dbff0", "Ea01eda48", "Ea2b5de1a",
    "Ebff1608e",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_34")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_34", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("DeckPicker resumed", edge="E553ad2d8")
    # Eb8a794fb onResume -> onPause: HOME key backgrounds the app.
    r.key("HOME", edge="Eb8a794fb")
    # Ef82c95ca onPause -> onStop: lifecycle callback.
    r.comment("DeckPicker stopped", edge="Ef82c95ca")
    # Ec788bd08 onStop -> UIUtils.saveCollectionInBackground.
    r.comment("background collection save starts", edge="Ec788bd08")
    # E1d7dbff0 saveCollectionInBackground -> DeckTask.doInBackground@SAVE_COLLECTION.
    r.comment("SAVE_COLLECTION task launched", edge="E1d7dbff0")
    # Ea01eda48 doInBackground@SAVE_COLLECTION -> onPostExecute@SAVE_COLLECTION.
    r.comment("worker result delivered to onPostExecute",
              edge="Ea01eda48")
    # Ea2b5de1a onPostExecute@SAVE_COLLECTION -> TaskListener.onPostExecute@SAVE_COLLECTION.
    r.comment("onPostExecute forwards to TaskListener", edge="Ea2b5de1a")
    # Ebff1608e TaskListener.onPostExecute -> UIUtils$1.onPostExecute (target).
    r.comment("UIUtils listener reached (target)", edge="Ebff1608e")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
