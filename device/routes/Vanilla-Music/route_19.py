"""Vanilla-Music route_19: BottomBarControls.setCover.

Edge ids (ROUTES.csv, in order):
  E47380ade E3aea4024 E8ee3f512 E8e6e45c2 Ea1ca8276 Ec1036aa5 E2cedf7b0
  Eaaa3c043 E3ad0bd94 Eb7f94138 E87375086 E5169a1ac Ebbe73e22 E769fe5a0
  E592d7d12 Ef3784465

Printed route source:
  verification.csv path row (BottomBarControls.setCover): "Steps read:
  PlaybackService.onCreate -> updateState -> handleMessage
  (MSG_BROADCAST_CHANGE) -> broadcastChange ->
  PlaybackActivity.setSong(long,Song) -> setSong(Song) -> runOnUiThread
  -> PlaybackActivity$2.run -> LibraryActivity.onSongChange (STATE:
  the code runs for the Library instance) -> handleMessage
  (MSG_UPDATE_COVER) (guard: song != null) -> updateCover ->
  runOnUiThread -> LibraryActivity$1.run -> BottomBarControls.setCover."
  ROUTES.csv row: source "PlaybackService.java:520,1000-1014,1584,1100;
  PlaybackActivity.java:339,302-312,309; LibraryActivity.java:991,997,
  964,579", state session.
Permissions: none. Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

How the route is driven: the early edges (service creation and the
  first broadcast) fire at launch, but the cover update needs a real
  song change while LibraryActivity is in front (STATE session:
  LibraryActivity open; guard song != null). So this script stays in
  the Library activity throughout -- it never opens full playback --
  plays "Morning Light", then changes song to "Silver Lake" while the
  Library activity is in front, which re-fires broadcastChange ->
  onSongChange -> MSG_UPDATE_COVER -> setCover for the Library
  instance. The bottom-bar cover view is res/layout/
  bottombar_controls.xml id "cover" (content-desc "Cover art").

UI labels used, all read from layout XML / strings.xml / fixture tags:
  - Songs tab label "Tracks" (translatable.xml songs -> "Tracks").
  - "Morning Light", "Silver Lake": fixtures 01/02, ID3 titles verified
    with ffprobe. Tapping a song row uses the default row action
    EXPAND_OR_PLAY_ALL, which for a non-expandable song row becomes
    PLAY_ALL, so each tap starts playback of that song (a song change).

Placement: this file is written for device/routes/Vanilla-Music/
  (four dirnames up from there is the repo root, which is what the
  sys.path derivation below assumes). It is delivered in the helper
  directory and must be copied to device/routes/Vanilla-Music/ by the
  merger before run_app.sh / drycheck.py execute it.
"""

import argparse
import os
import sys

_root = os.path.abspath(__file__)
for _ in range(4):
    _root = os.path.dirname(_root)
sys.path.insert(0, _root)

from device.harness.harness import Runner  # noqa: E402

PACKAGE_ACTIVITY = (
    "ch.blinkenlights.android.vanilla/"
    "ch.blinkenlights.android.vanilla.LibraryActivity"
)
EDGE_IDS = [
    "E47380ade", "E3aea4024", "E8ee3f512", "E8e6e45c2", "Ea1ca8276",
    "Ec1036aa5", "E2cedf7b0", "Eaaa3c043", "E3ad0bd94", "Eb7f94138",
    "E87375086", "E5169a1ac", "Ebbe73e22", "E769fe5a0", "E592d7d12",
    "Ef3784465",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_19", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    # LibraryActivity stays in front for the whole script (STATE:
    # LibraryActivity open), so the broadcast below reaches the
    # Library instance's onSongChange.
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E3aea4024 -- LIFECYCLE: Activity lifecycle callback (onStart).
    r.comment("lifecycle onStart, no user action", "E3aea4024")

    # E8ee3f512 -- CALL: LibraryActivity.onStart -> PlaybackActivity.
    # onStart (direct call, superclass dispatch).
    r.comment("superclass onStart dispatch, no user action", "E8ee3f512")

    # E8e6e45c2 -- INTENT: startService(new Intent(this,
    # PlaybackService.class)) (guard: the service does not run yet).
    r.comment("service start at launch, no user action", "E8e6e45c2")

    # Ea1ca8276 -- LIFECYCLE: the system creates the service and calls
    # onCreate.
    r.comment("service onCreate, no user action", "Ea1ca8276")

    # Ec1036aa5 -- CALL: PlaybackService.onCreate -> updateState
    # (direct call).
    r.comment("dispatch to updateState, no user action", "Ec1036aa5")

    # E2cedf7b0 -- ASYNC: the MSG_BROADCAST_CHANGE branch runs (guard:
    # state != oldState). Fires on the song changes below, not only at
    # launch; no separate user action for the branch itself.
    r.comment("MSG_BROADCAST_CHANGE branch, no user action", "E2cedf7b0")

    # Eaaa3c043 -- CALL: call made in the message branch (to
    # broadcastChange).
    r.comment("dispatch to broadcastChange, no user action", "Eaaa3c043")

    # E3ad0bd94 -- CALL: broadcastChange -> PlaybackActivity.setSong
    # (long,Song) (virtual/interface dispatch to this implementation).
    r.comment("dispatch to setSong(long,Song), no user action",
              "E3ad0bd94")

    # Eb7f94138 -- CALL: setSong(long,Song) -> setSong(Song) (direct
    # call).
    r.comment("dispatch to setSong(Song), no user action", "Eb7f94138")

    # E87375086 -- FRAMEWORK: runOnUiThread(new Runnable(){...}) runs
    # onSongChange(song) on the UI thread (PlaybackActivity$2.run).
    r.comment("runOnUiThread dispatch, no user action", "E87375086")

    # E5169a1ac -- CALL: onSongChange(...) of the LibraryActivity
    # instance (STATE: LibraryActivity is open). The user actions that
    # produce the song changes are the song-row taps here: play
    # "Morning Light", then change song to "Silver Lake" while the
    # Library activity is still in front, so the playback-state
    # broadcast reaches this instance and updates the bottom-bar cover.
    r.wait_for("E5169a1ac", text="Tracks")
    r.tap("E5169a1ac", text="Tracks")
    r.wait_for("E5169a1ac", text="Morning Light")
    r.tap("E5169a1ac", text="Morning Light")
    r.scroll_to("E5169a1ac", text="Silver Lake")
    r.tap("E5169a1ac", text="Silver Lake")

    # Ebbe73e22 -- ASYNC: the MSG_UPDATE_COVER branch runs (guard:
    # song != null; both tapped rows are real songs, so it holds).
    r.comment("MSG_UPDATE_COVER branch, no user action", "Ebbe73e22")

    # E769fe5a0 -- CALL: call made in the message branch (to
    # updateCover).
    r.comment("dispatch to updateCover, no user action", "E769fe5a0")

    # E592d7d12 -- ASYNC: runOnUiThread(new Runnable(){...}): the cover
    # bitmap is set on the UI thread (LibraryActivity$1.run).
    r.comment("runOnUiThread cover dispatch, no user action", "E592d7d12")

    # Ef3784465 -- CALL: mBottomBarControls.setCover(cover) (the
    # target; LibraryActivity.java:579). The bottom-bar cover view
    # (id "cover", content-desc "Cover art") is the visible evidence
    # that the cover update landed in the Library activity.
    r.wait_for("Ef3784465", res_id="cover")
    r.screenshot("route_19_bottom_bar_cover", "Ef3784465")

    r.done()


if __name__ == "__main__":
    main()
