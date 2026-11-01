#!/usr/bin/env python3
"""Vanilla-Music route_07: SongTimeline$FlagComparator.compare.

Method: SongTimeline$FlagComparator.compare
Edge ids (in order, from ROUTES.csv):
    E47380ade E3aea4024 E8ee3f512 E8e6e45c2 Ea1ca8276 E1a900462
    E8b3ceffa E0591813a
Printed route source:
    verification.csv path row (SongTimeline$FlagComparator.compare,
      SOURCE):
      ref: PlaybackActivity.java:124-127; PlaybackService.java:449,
        2014; SongTimeline.java:309-322,385
      Steps read: onStart starts PlaybackService (guard:
        hasInstance() false) -> onCreate -> loadState ->
        SongTimeline.readState -> Collections.sort(songs, new
        FlagComparator()) (SongTimeline.java:385). The
        Collections.sort -> Comparator.compare call is INFERRED
        standard JDK behavior.
    ROUTES.csv row: env_kinds=(none), state_kinds=(none),
      permissions=(none), fixtures=(none),
      setup="push fixtures/Music + media scan", status=scripted.
Permissions: none (ROUTES.csv lists none).
Fixtures: none (STATE file gates: none).
Setup (run by run_app.sh before this script): pm clear, then push
    fixtures/Music + media scan.
State dependency (read this before replaying): compare runs only
    when a previous session saved timeline state. SongTimeline
    .readState sorts with FlagComparator only inside "if (n > 0)"
    and only when the songs query returns rows (SongTimeline
    .java:385), and PlaybackService.loadState reads that state from
    the app-private STATE_FILE. A plain launch after pm clear has no
    saved state, so the sort (and compare) does not run; the
    startService guard (hasInstance() false) is satisfied by a fresh
    launch, but the saved-state guard is not. The device lead must
    run this route after a session that played a song and saved
    state, WITHOUT an intervening pm clear, or seed the state file
    by other means. This script itself performs no state-building
    step: it launches and lets the saved-state sort run, as the
    route specifies. No special UI state is built here.
Harness notes: launch() takes (component, edge); every other call
    below passes edge= explicitly. All edges after launch are
    lifecycle/service/framework edges with no user action, so they
    are comment() blocks.
"""

import argparse
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT = _SCRIPT_DIR
for _ in range(3):
    _ROOT = os.path.dirname(_ROOT)
# Insert only a root that really contains device/harness: inserting a
# wrong root first would cache a namespace "device" package and break
# the fallback import below.
_CANDIDATES = []
if os.path.isfile(os.path.join(_ROOT, "device", "harness", "harness.py")):
    _CANDIDATES.append(_ROOT)
else:
    # Helper-dir copies (e.g. work/Vanilla-Music/helper/...) are not
    # under device/routes/, so the four-dirname root above is not a
    # repo root there. Fall back to a stage checkout found under an
    # ancestor (device/stage/device/harness). In the merged layout
    # (device/routes/Vanilla-Music/route_NN.py) the primary root
    # contains device/harness and this branch never runs.
    _dir = _SCRIPT_DIR
    while True:
        _cand = os.path.join(_dir, "device", "stage")
        if os.path.isfile(os.path.join(_cand, "device", "harness",
                                       "harness.py")):
            _CANDIDATES.append(_cand)
            break
        _parent = os.path.dirname(_dir)
        if _parent == _dir:
            break
        _dir = _parent
for _c in _CANDIDATES:
    sys.path.insert(0, _c)
from device.harness.harness import Runner

EDGE_IDS = [
    "E47380ade", "E3aea4024", "E8ee3f512", "E8e6e45c2", "Ea1ca8276",
    "E1a900462", "E8b3ceffa", "E0591813a",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    r = Runner(package=args.package, route="route_07", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    # Ordinary launch; the saved-state sort runs during service
    # start below (see module docstring for the saved-state
    # dependency).
    r.launch("%s/.LibraryActivity" % args.package, edge="E47380ade")
    # E3aea4024 -- Activity lifecycle callback; SRC
    # LibraryActivity.java:158-216. The pager wait proves the
    # activity started.
    r.wait_for(edge="E3aea4024", res_id="pager", timeout=30)
    # E8ee3f512 -- Direct call (PlaybackActivity.onStart from
    # LibraryActivity.onStart; no user action).
    r.comment("PlaybackActivity.onStart called", edge="E8ee3f512")
    # E8e6e45c2 -- startService(new Intent(this,
    # PlaybackService.class)): the service is created and started.
    # Guard hasInstance() false holds on a fresh launch; the service
    # start itself is framework-driven, no user action.
    r.comment("PlaybackService started (hasInstance false)", edge="E8e6e45c2")
    # Ea1ca8276 -- the system creates the service and calls onCreate
    # (lifecycle; no user action).
    r.comment("PlaybackService.onCreate (lifecycle)", edge="Ea1ca8276")
    # E1a900462 -- Direct call (loadState from onCreate).
    r.comment("PlaybackService.loadState called", edge="E1a900462")
    # E8b3ceffa -- Direct call (SongTimeline.readState from
    # loadState). Reads the saved STATE_FILE; with no saved state
    # the sort below does not run (see docstring).
    r.comment("SongTimeline.readState called", edge="E8b3ceffa")
    # E0591813a -- Collections.sort(songs, new FlagComparator()):
    # the songs are restored to the order they were saved in
    # (framework sort; no user action). Target edge.
    r.comment("FlagComparator.compare via Collections.sort (target)",
              edge="E0591813a")
    r.screenshot("route_07_end", edge="E0591813a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
