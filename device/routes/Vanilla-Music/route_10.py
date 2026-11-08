#!/usr/bin/env python3
"""Vanilla-Music route_10: CoverBitmap.drawText.

Method: CoverBitmap.drawText
Edge ids (in order, from ROUTES.csv):
    E47380ade E29472d10 E80427a98 E370f1569 Eb03c94c3 E9218d7e4
    E3df8604f E91443f76 Eb8d87602 E65203762 E68fa90e1 Eaab0bde9
    E846a1da3 E81017758 E975ec859 Ef93cfd61 E35cb8470 Ed5ce5325
    E06466ed8
Printed route source:
    verification.csv path row (CoverBitmap.drawText, SOURCE):
      ref: LibraryActivity.java:587-589,451-456;
        FullPlaybackActivity.java:106-185; CoverView.java:280,
        166-169,249,201-206,256,219,236; CoverBitmap.java:132,295
      Steps read: tap the bottom bar -> openPlaybackActivity ->
        FullPlaybackActivity (onResume@FullPlaybackActivity) ->
        onCreate inflates CoverView -> onSizeChanged -> querySongs
        -> handleMessage(MSG_QUERY_SONGS) -> querySongsInternal ->
        handleMessage(MSG_SET_BITMAP) (STATE: a song is loaded,
        guard: the song of this slot changed) -> setSongBitmap ->
        generateBitmap -> CoverBitmap.createBitmap ->
        createSeparatedBitmap -> drawText.
    ROUTES.csv row: state_kinds=session, permissions=(none),
      fixtures=(none), setup="push fixtures/Music + media scan",
      status=scripted.
Permissions: none (ROUTES.csv lists none; storage is granted during
    setup, not by this route).
Fixtures: none (STATE file gates: none; the song is loaded through
    the app itself from the setup-scanned library).
Setup (run by run_app.sh before this script): pm clear, then push
    fixtures/Music + media scan.
State needed: a song loaded. This script builds it the same way
    as route_06: Tracks tab, tap the first list row (play-all
    header or song row; either loads a song), wait for the bottom
    bar, tap it. The MSG_SET_BITMAP guard (the song of this slot
    changed) holds because the full-playback CoverView is created
    fresh for the newly loaded song. drawText is the fallback-text
    path of createSeparatedBitmap (CoverBitmap.java:279,289,295):
    the setup fixtures carry no embedded cover art, so the
    generated bitmap draws title/album/artist text.
Harness notes: launch() takes (component, edge); every other call
    below passes edge= explicitly. The bottom-bar tap uses res_id
    content_controls, the inner row that BottomBarControls forwards
    clicks from (BottomBarControls.java:135-137;
    LibraryActivity.java:182-183). All edges after the full
    playback screen opens are framework/internal/async edges with
    no user action, so they are comment() blocks; the cover_view
    wait proves CoverView was inflated.
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
    "E9218d7e4", "E3df8604f", "E91443f76", "Eb8d87602", "E65203762",
    "E68fa90e1", "Eaab0bde9", "E846a1da3", "E81017758", "E975ec859",
    "Ef93cfd61", "E35cb8470", "Ed5ce5325", "E06466ed8",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    r = Runner(package=args.package, route="route_10", edge_ids=EDGE_IDS,
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
    # FullPlaybackActivity.class)). Fired by the bottom-bar tap.
    r.comment("FullPlaybackActivity started via intent", edge="E3df8604f")
    # E91443f76 -- Activity lifecycle callback; SRC
    # FullPlaybackActivity.java:106-185. setContentView inflates
    # CoverView (full_playback_alt.xml / full_playback.xml, res_id
    # cover_view); the wait proves inflation happened.
    r.wait_for(edge="E91443f76", res_id="cover_view", timeout=30)
    # Eb8d87602 -- setContentView / inflate builds the view
    # <CoverView> (framework; no user action).
    r.comment("CoverView inflated (framework)", edge="Eb8d87602")
    # E65203762 -- the cover view is measured, sized and drawn
    # (framework; no user action).
    r.comment("CoverView.onSizeChanged (framework)", edge="E65203762")
    # E68fa90e1 -- Direct call (querySongs from onSizeChanged).
    r.comment("CoverView.querySongs called", edge="E68fa90e1")
    # Eaab0bde9 -- the branch of CoverView that handles
    # MSG_QUERY_SONGS runs (async; guard: called by setSong /
    # replaceSong / onSizeChanged).
    r.comment("MSG_QUERY_SONGS handled (async)", edge="Eaab0bde9")
    # E846a1da3 -- call made in the message branch.
    r.comment("CoverView.querySongsInternal called", edge="E846a1da3")
    # E81017758 -- the branch of CoverView that handles
    # MSG_SET_BITMAP runs (async). Guard: the song of this slot
    # changed; needs_state: a song is loaded, satisfied by the
    # Tracks-tab tap above.
    r.comment("MSG_SET_BITMAP handled, song slot changed (async)",
              edge="E81017758")
    # E975ec859 -- call made in the message branch.
    r.comment("CoverView.setSongBitmap called", edge="E975ec859")
    # Ef93cfd61 -- Direct call.
    r.comment("CoverView.generateBitmap called", edge="Ef93cfd61")
    # E35cb8470 -- Direct call.
    r.comment("CoverBitmap.createBitmap called", edge="E35cb8470")
    # Ed5ce5325 -- Direct call.
    r.comment("CoverBitmap.createSeparatedBitmap called", edge="Ed5ce5325")
    # E06466ed8 -- Direct call to CoverBitmap.drawText (target).
    r.comment("CoverBitmap.drawText called (target)", edge="E06466ed8")
    r.screenshot("route_10_end", edge="E06466ed8")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
