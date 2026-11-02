#!/usr/bin/env python3
"""AnkiDroid route_16: Preferences.replaceString.

Target: Preferences.replaceString.
Table verdict: CORRECT as history (combined merge: NOT in the
    new sample; old CORRECT verdict stands as history, not
    re-printed; 10 edges, drive unchanged). Do NOT claim gate
    verification for this method. This is the
    initPreference route, not the old first-draw route_14 script's
    backupMax-drag terminal path: the call happens automatically
    while the Advanced screen inflates.
Route followed: printed route: launch under the no-collection guard
    -> S_PREFERENCES -> SettingsFragment -> initAllPreferences ->
    initPreference -> updateSummary -> replaceString.
Preconditions (launch state, arranged by run setup, not by this
    script): collection NOT open; WRITE_EXTERNAL_STORAGE granted;
    SD mounted; AnkiDroid directory NOT accessible. The Advanced
    screen must contain backupMax (default 8, range 0-10).
Mapping notes:
  - The script performs no tap: every step after launch is
    framework/inflation dispatch. If the launch screen is not the
    Advanced screen, the live run must navigate to it first; that
    fallback has no graph edge and is flagged here, not invented.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
Draft status: final-draw device draft for the merger; dry/static
    checks only. No live run has been performed with this script, and
    nothing in this file claims one.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Edd09dca3", "E60725a5c",
    "E48af4570", "E692d53dd", "Ee26a292c", "E0817366c", "Ec779c0bd",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_16")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_16", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init> (else branch).
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Edd09dca3 DeckPicker.onCreate -> S_PREFERENCES (graph-fixed
    # step 4: storage permission granted, SD mounted, but the
    # AnkiDroid directory is NOT accessible, DeckPicker.java:418-428.
    # No tap: the launch state itself opens Preferences.
    # The intent carries the Advanced subscreen
    # (CompatV11.java:41-48); if a different subscreen shows, tap
    # its Advanced entry first (fallback, no graph edge).
    r.comment("no-collection guard opens Advanced preferences",
              edge="Edd09dca3")
    # E60725a5c S_PREFERENCES -> SettingsFragment.<init>.
    r.comment("SettingsFragment created", edge="E60725a5c")
    # E48af4570 SettingsFragment.<init> -> onCreate.
    r.comment("SettingsFragment onCreate", edge="E48af4570")
    # E692d53dd onCreate -> initAllPreferences.
    r.comment("initAllPreferences", edge="E692d53dd")
    # Ee26a292c initAllPreferences -> initPreference (iterates the
    # screen, including nested groups, calling initPreference on
    # each leaf).
    r.comment("initPreference", edge="Ee26a292c")
    # E0817366c initPreference -> updateSummary (unconditional at
    # the end of initPreference).
    r.comment("updateSummary", edge="E0817366c")
    # Ec779c0bd updateSummary -> replaceString (target; reached for
    # a NumberRange/SeekBar/List/EditTextPreference with a non-empty
    # old summary and value, key not
    # minimumCardsDueForNotification, Preferences.java:613-636.
    # backupMax ("Max number of backups", summary "XXX") on the
    # Advanced screen is such a preference, so the call happens
    # automatically at screen inflation; no drag is needed for
    # this BFS terminal path).
    r.comment("replaceString reached (target)", edge="Ec779c0bd")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
