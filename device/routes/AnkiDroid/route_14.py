#!/usr/bin/env python3
"""AnkiDroid route_14: Preferences.replaceString.

Target: Preferences.replaceString (called from updateSummary for a
    SeekBarPreference at Preferences.java:636).
Table verdict: WRONG (first-draw verdict; this script drives the
    CORRECTED terminal path, never the printed BFS route).
Route followed: corrected terminal path from
    helper/b6fix-r13-18-rework/CORRECTED_ROUTES.md section 2:
    sampled steps 1-3 and 5-7 unchanged, steps 8-10 replaced by the
    backupMax path (10 edges). The sampled route used
    advanced_statistics_link, a plain <Preference>, for which
    updateSummary returns at Preferences.java:636 before
    replaceString; backupMax is a SeekBarPreference whose summary
    "XXX" (preference_summary_literal) is what replaceString
    substitutes into.
Preconditions/fixtures:
  - Launch state for the graph-fixed step 4 (Edd09dca3): collection
    NOT open, WRITE_EXTERNAL_STORAGE granted, SD card mounted, and
    the AnkiDroid directory NOT accessible. Under that guard,
    DeckPicker.onCreate goes to S_PREFERENCES instead of the deck
    picker. Run setup must arrange this state (fresh install with
    storage permission granted and no accessible collection dir);
    the script does not create it.
  - The Advanced preferences screen must be showing with the
    backupMax row ("Max number of backups", default 8, range 0-10,
    interval 1). If the launch screen is a different preferences
    screen, tap its Advanced entry first; verify the navigation
    against a live dump.
Mapping notes:
  - The SeekBar drag has no graph edge of its own: dragging the
    SeekBar changes the preference, which fires
    onSharedPreferenceChanged, logged as E249f9a1a. Because drag
    coordinates cannot be known without a live layout, the script
    resolves them at run time: it dumps the UI, finds the
    "Max number of backups" title node, takes the SeekBar node
    nearest in y, and drags within its track to 90 percent (a new
    value whenever the current value is not already the max). No
    coordinates are invented. In dry-run mode no dump file is
    produced, so the script logs a comment for the drag edge
    instead of parsing.
  - updatePreference -> updateSummary (E2f8145b9) holds because
    backupMax has no switch case (Preferences.java:455-567), so
    execution falls through to updateSummary at :567.
  - updateSummary -> replaceString (Ec779c0bd) holds because the
    pref is a SeekBarPreference, the value is non-empty, the
    original summary is non-empty ("XXX"), and the key is not
    minimumCardsDueForNotification (Preferences.java:614-636).
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner, parse_bounds  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Edd09dca3", "E60725a5c",
    "E48af4570", "E364fad28", "E249f9a1a", "E2f8145b9", "Ec779c0bd",
]


def _seekbar_drag_points(dump_path):
    """Return (x1, y, x2, y) for a drag inside the backupMax SeekBar.

    Finds the "Max number of backups" title node, then the SeekBar
    node nearest in y, and drags from 10 percent to 90 percent of
    its track. Raises RuntimeError when either node is missing.
    """
    root = ET.parse(dump_path).getroot()
    nodes = list(root.iter("node"))
    title = None
    for n in nodes:
        if n.get("text", "") == "Max number of backups":
            title = n
            break
    if title is None:
        raise RuntimeError("backupMax title node not found in dump")
    tx1, ty1, tx2, ty2 = parse_bounds(title.get("bounds", ""))
    tcy = (ty1 + ty2) // 2
    best = None
    for n in nodes:
        if n.get("class", "") != "android.widget.SeekBar":
            continue
        x1, y1, x2, y2 = parse_bounds(n.get("bounds", ""))
        cy = (y1 + y2) // 2
        dist = abs(cy - tcy)
        if best is None or dist < best[0]:
            best = (dist, x1, y1, x2, y2)
    if best is None:
        raise RuntimeError("no SeekBar node found in dump")
    _, x1, y1, x2, y2 = best
    cy = (y1 + y2) // 2
    return (x1 + (x2 - x1) // 10, cy, x1 + 9 * (x2 - x1) // 10, cy)


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_14")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
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
    # Edd09dca3 DeckPicker.onCreate -> S_PREFERENCES (graph-fixed
    # step 4: not colOpen, storage granted, SD mounted, AnkiDroid
    # directory NOT accessible).
    r.comment("no-collection guard opens Preferences", edge="Edd09dca3")
    # E60725a5c S_PREFERENCES -> SettingsFragment.<init>.
    r.comment("SettingsFragment created", edge="E60725a5c")
    # E48af4570 SettingsFragment.<init> -> onCreate.
    r.comment("SettingsFragment onCreate", edge="E48af4570")
    # E364fad28 onCreate -> onResume (listener registered here,
    # Preferences.java:795-796).
    r.comment("SettingsFragment onResume, listener registered",
              edge="E364fad28")
    # Wait for the backupMax row on the Advanced screen before
    # dragging its SeekBar (see header: navigate to Advanced first
    # if the launch screen is not it).
    r.wait_for(edge="E249f9a1a", text="Max number of backups")
    # E249f9a1a onSharedPreferenceChanged -> updatePreference: drag
    # the backupMax SeekBar to a new value. Coordinates come from a
    # live UI dump in real runs; dry-run logs a comment instead.
    if r.dry_run:
        r.comment("drag backupMax SeekBar to a new value "
                  "(coordinates resolved from live dump in real runs)",
                  edge="E249f9a1a")
    else:
        r.dump_ui("backupmax", edge="E249f9a1a")
        dump_path = os.path.join(args.outdir, "dumps", "route_14",
                                 "backupmax.xml")
        x1, y, x2, _ = _seekbar_drag_points(dump_path)
        r.drag(edge="E249f9a1a", x1=x1, y1=y, x2=x2, y2=y,
               why="move backupMax SeekBar to a new value")
    # E2f8145b9 updatePreference -> updateSummary (backupMax has no
    # switch case, so execution falls through).
    r.comment("updatePreference falls through to updateSummary",
              edge="E2f8145b9")
    # Ec779c0bd updateSummary -> replaceString (target; SeekBar
    # branch, summary XXX, key is not
    # minimumCardsDueForNotification).
    r.comment("SeekBar summary substituted via replaceString (target)",
              edge="Ec779c0bd")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
