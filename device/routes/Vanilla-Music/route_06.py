#!/usr/bin/env python3
"""Vanilla-Music route_06: SongTimeline.removeSong.

Method: SongTimeline.removeSong
Edge ids (in order, from ROUTES.csv):
    E47380ade E29472d10 E80427a98 E370f1569 Eb03c94c3 E9218d7e4
    E3df8604f Ec2adbce7 Efeca3e48 Ef8de8435 E46586603 E800017ed
    Edc1d9b46 E33e96932 Eb6814891 E7119237b Eb4222deb
Printed route source:
    verification.csv path row (SongTimeline.removeSong, SOURCE):
      ref: LibraryActivity.java:587-589,451-456;
        FullPlaybackActivity.java:383-408,393-400;
        PlaybackActivity.java:499,579; PlaybackService.java:1743
      Steps read: tap the bottom bar -> openPlaybackActivity ->
        FullPlaybackActivity (onResume@FullPlaybackActivity, the fixed
        variant) -> overflow menu -> Delete (needs_state: a song is
        loaded, correct per FullPlaybackActivity.java:384) -> confirm
        dialog -> handleMessage(MSG_DELETE) -> PlaybackActivity.delete
        -> PlaybackService.deleteMedia -> SongTimeline.removeSong.
    ROUTES.csv row: state_kinds=session, permissions=(none),
      fixtures=(none), setup="push fixtures/Music + media scan",
      status=scripted.
Permissions: none (ROUTES.csv lists none; storage is granted during
    setup, not by this route).
Fixtures: none (STATE file gates: none; the song is loaded through
    the app itself from the setup-scanned library).
Setup (run by run_app.sh before this script): pm clear, then push
    fixtures/Music + media scan.
State needed: a song loaded. This script builds it: it opens the
    Tracks tab and taps the first list row (the play-all header or a
    song row; either loads a song, since the default row action is
    EXPAND_OR_PLAY_ALL and song rows are not expandable, so the tap
    resolves to play-all). It then waits for the bottom bar before
    tapping it, so the Delete menu item's song-loaded guard holds.
Side effect to know: confirming Delete deletes the playing file
    from storage (PlaybackService.deleteMedia). run_app.sh clears and
    re-runs setup per route, so a later route needs its fixtures
    re-pushed; do not run this script twice in one install without
    re-pushing fixtures/Music.
Harness notes: launch() takes (component, edge); every other call
    below passes edge= explicitly. The overflow button has no app
    res_id or app string: it is tapped by the standard AOSP overflow
    content description "More options" (framework-provided, not an
    app label). The bottom-bar tap uses res_id content_controls, the
    inner row that BottomBarControls forwards clicks from
    (BottomBarControls.java:135-137; LibraryActivity.java:182-183).
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
    "E47380ade", "E29472d10", "E80427a98", "E370f1569", "Eb03c94c3",
    "E9218d7e4", "E3df8604f", "Ec2adbce7", "Efeca3e48", "Ef8de8435",
    "E46586603", "E800017ed", "Edc1d9b46", "E33e96932", "Eb6814891",
    "E7119237b", "Eb4222deb",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("%s/.LibraryActivity" % args.package, edge="E47380ade")
    # E29472d10 -- Activity lifecycle callback (no user action).
    r.comment("LibraryActivity onResume (lifecycle)", edge="E29472d10")
    # E80427a98 -- LibraryActivity is resumed and shown (default tab
    # Artists: library_page = 0). Wait for the library pager, then
    # build the STATE session precondition: load a song.
    r.wait_for(edge="E80427a98", res_id="pager", timeout=30)
    # Precondition (same edge block): open the Tracks tab (the songs
    # tab title is R.string.songs = "Tracks") and tap the first list
    # row to load/play a song.
    r.tap(edge="E80427a98", text="Tracks")
    r.wait_for(edge="E80427a98", res_id="text", timeout=30)
    r.tap(edge="E80427a98", res_id="text")
    # E370f1569 -- Tap the bottom bar (current song). Wait for the
    # bottom bar to appear once the song is loaded, then tap its
    # clickable inner row.
    r.wait_for(edge="E370f1569", res_id="bottombar_controls", timeout=30)
    r.tap(edge="E370f1569", res_id="content_controls")
    # Eb03c94c3 -- the click comes from the bottom bar itself.
    r.comment("click routed from BottomBarControls", edge="Eb03c94c3")
    # E9218d7e4 -- call made in the click branch.
    r.comment("openPlaybackActivity called from onClick", edge="E9218d7e4")
    # E3df8604f -- startActivity(new Intent(this,
    # FullPlaybackActivity.class)). The intent itself is fired by the
    # bottom-bar tap; wait for the full-playback cover view as the
    # arrival check.
    r.wait_for(edge="E3df8604f", res_id="cover_view", timeout=30)
    # Ec2adbce7 -- Activity lifecycle callback (no user action).
    r.comment("FullPlaybackActivity onResume (lifecycle)", edge="Ec2adbce7")
    # Efeca3e48 -- FullPlaybackActivity is resumed and shown
    # (controls visible by default). Reached by the cover_view wait
    # above; no further user action.
    r.comment("full playback screen shown", edge="Efeca3e48")
    # Ef8de8435 -- the overflow menu of the action bar opens.
    r.tap(edge="Ef8de8435", desc="More options")
    # E46586603 -- Tap "Delete" (menu item R.string.delete; guard: a
    # song is loaded, satisfied by the Tracks-tab tap above).
    r.tap(edge="E46586603", text="Delete")
    # E800017ed -- the item DELETE finished; the confirm dialog
    # (S_DLG_DELETE_FULL) is shown. Its title and positive button
    # both read "Delete".
    r.wait_for(edge="E800017ed", text="Delete", timeout=30)
    # Edc1d9b46 -- Tap "Delete" in the confirm dialog. The tap
    # resolver prefers clickable nodes, so this hits the positive
    # button rather than the dialog title.
    r.tap(edge="Edc1d9b46", text="Delete")
    # E33e96932 -- the branch of FullPlaybackActivity that handles
    # MSG_DELETE runs (async; no user action).
    r.comment("MSG_DELETE handled (async)", edge="E33e96932")
    # Eb6814891 -- call made in the message branch.
    r.comment("PlaybackActivity.delete called", edge="Eb6814891")
    # E7119237b -- Direct call.
    r.comment("PlaybackService.deleteMedia called", edge="E7119237b")
    # Eb4222deb -- Direct call to SongTimeline.removeSong (target).
    r.comment("SongTimeline.removeSong called (target)", edge="Eb4222deb")
    r.screenshot("route_06_end", edge="Eb4222deb")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
