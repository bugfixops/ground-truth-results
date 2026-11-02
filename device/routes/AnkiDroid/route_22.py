#!/usr/bin/env python3
"""AnkiDroid final-draw route_22: MetaDB.getNotificationStatus.

Target: MetaDB.getNotificationStatus (via WidgetStatus.fetchDue).
Table verdict: CORRECT (final draw, route_table.md row 22).
Route followed: the final BFS route (14 edges), identical to the
    first-draw route_09 route. This script is reused from first-draw
    route_09.py with only the route name/docstring updated; the edge
    list, drive, and guards are unchanged.
Preconditions/fixtures:
  - Collection open (colIsOpen() guard on the onStop step).
  - Notifications enabled: minimumCardsDueForNotification below
    1000000 (its default, 1000001, disables the task), or the small
    widget enabled. Run setup must set one of these; the script
    itself does not open Preferences (that would leave the route).
    No file fixture is pushed.
Mapping notes:
  - Backgrounding the app with the HOME key is what drives
    onPause -> onStop; there is no tap that produces onStop.
  - The onPostExecute step starts NotificationService; the service
    then runs onStartCommand -> fetchDue -> getNotificationStatus
    on its own, so the script waits (dwell) rather than tapping.
  - No live run is claimed by this script.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "Eb8a794fb",
    "Ef82c95ca", "Ea4264ce0", "E7f645320", "Ebecac143", "E10b85314",
    "E6d79dde5", "E3c7d7dc4", "E11340011", "E184845c0",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_22")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_22", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("onStart -> onResume; deck list loads", edge="E553ad2d8")
    # Eb8a794fb onResume -> onPause: press HOME to background the app.
    r.key("HOME", edge="Eb8a794fb")
    # Ef82c95ca onPause -> onStop.
    r.comment("activity stops", edge="Ef82c95ca")
    # Ea4264ce0 onStop -> WidgetStatus.update (guard: colIsOpen()).
    r.comment("onStop updates widget status (collection open)",
              edge="Ea4264ce0")
    # E7f645320 WidgetStatus.update -> UpdateDeckStatusAsyncTask
    # .doInBackground (gate: widget or notifications enabled).
    r.comment("update starts status task", edge="E7f645320")
    # Ebecac143 doInBackground -> onPostExecute: wait for the task.
    r.dwell(edge="Ebecac143", seconds=5)
    # E10b85314 onPostExecute -> NotificationService.<init>.
    r.comment("onPostExecute starts NotificationService",
              edge="E10b85314")
    # E6d79dde5 NotificationService.<init> -> onCreate.
    r.comment("NotificationService onCreate", edge="E6d79dde5")
    # E3c7d7dc4 onCreate -> onStartCommand.
    r.comment("NotificationService onStartCommand", edge="E3c7d7dc4")
    # E11340011 onStartCommand -> WidgetStatus.fetchDue.
    r.comment("service fetches due count", edge="E11340011")
    # E184845c0 fetchDue -> MetaDB.getNotificationStatus (target).
    r.comment("fetchDue reads notification status (target)",
              edge="E184845c0")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
