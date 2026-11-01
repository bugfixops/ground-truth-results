"""Vanilla-Music route_18: MediaLibrary.updateSongPlayCounts.

Edge ids (ROUTES.csv, in order):
  E47380ade E29472d10 E80427a98 Ed9ad8ad1 Ee8de0c7d E5c102dcf Eb90ef0a1
  Ed8f23832 Ec958d00b E6515cc1d Edc966b36 Ec66727e1 E681d9bad E8c6979ac

Printed route source:
  verification.csv path row (MediaLibrary.updateSongPlayCounts):
  "Steps read: tap the bottom bar, swipe up to the controls stage ->
  tap ""next"" -> shiftCurrentSong -> PlaybackService.shiftCurrentSong
  -> preparePlayCountsUpdate -> handleMessage(MSG_UPDATE_PLAYCOUNTS)
  (STATE: a song is loaded; guard: isPlaying() and the played-
  percentage condition) -> PlayCountsHelper.countSong ->
  MediaLibrary.updateSongPlayCounts."
  ROUTES.csv row: source "LibraryActivity.java:609-611,610;
  PlaybackActivity.java:215-217,193; PlaybackService.java:1760,678-693,
  1609; PlayCountsHelper.java:36", state session.
Permissions: none. Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

Playback-position control (stated, with what was used): harness.py
  offers NO seek or drag primitive -- its actions are launch/tap/
  long_tap/type_text/key/back/scroll_to/wait_for/start_intent/
  broadcast/grant/deny/push_fixture/screenshot/dump_ui/assert_text,
  and scroll_to's swipe is a fixed full swipe, not a seekbar drag, so
  the seek bar (res/layout/seek_bar.xml, id seek_bar) cannot be
  dragged through this harness. Position is therefore controlled with
  the SHIFT_NEXT_SONG branch of the guard in
  PlaybackService.preparePlayCountsUpdate: SHIFT_NEXT_SONG with at most
  50% played (the other branch, SHIFT_KEEP_SONG, needs 80% played).
  Every fixture song is ~20 s long (ffprobe on the setup fixtures), and
  this script taps "next" within seconds of starting playback -- only
  a tab tap, a song tap, and one swipe-up intervene -- so the played
  percentage at the "next" tap is far below 50% and the
  MSG_UPDATE_PLAYCOUNTS message fires (delayed 800 ms in the service;
  the final screenshot/dump steps give it time to fire before the
  coverage dump that run_app.sh takes after the script).
  The 80% branch is NOT attempted: reaching it would need ~16 s of
  playback and the harness has no sleep/wait-for-duration action.

UI labels used, all read from layout XML / strings.xml / fixture tags:
  - Songs tab label "Tracks" (translatable.xml songs -> "Tracks").
  - "Morning Light": fixture 01 Morning Light.mp3, ID3 title verified
    with ffprobe. Tapping it uses the default row action
    EXPAND_OR_PLAY_ALL (PrefDefaults DEFAULT_ACTION_INT "9"), which
    for a non-expandable song row becomes PLAY_ALL, so playback starts
    and the queue is filled (STATE session: a song is loaded).
  - Controls-stage "next" button: res/layout/controls.xml id "next"
    (content-desc "Next song", PlaybackActivity.onClick case R.id.next
    -> shiftCurrentSong(SHIFT_NEXT_SONG)).

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
    "E47380ade", "E29472d10", "E80427a98", "Ed9ad8ad1", "Ee8de0c7d",
    "E5c102dcf", "Eb90ef0a1", "Ed8f23832", "Ec958d00b", "E6515cc1d",
    "Edc966b36", "Ec66727e1", "E681d9bad", "E8c6979ac",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_18", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E29472d10 -- LIFECYCLE: Activity lifecycle callback (onResume).
    r.comment("lifecycle onResume, no user action", "E29472d10")

    # E80427a98 -- ENTERS S_LIBRARY: LibraryActivity resumed and shown.
    # STATE setup for the route (a song loaded): open the Songs tab
    # (label "Tracks") and tap "Morning Light". The default row action
    # plays all songs from that row, so playback starts immediately --
    # this is what makes isPlaying() true and the position small when
    # "next" is tapped below (see the header note on position control).
    r.wait_for("E80427a98", text="Tracks")
    r.tap("E80427a98", text="Tracks")
    r.wait_for("E80427a98", text="Morning Light")
    r.tap("E80427a98", text="Morning Light")

    # Ed9ad8ad1 -- GUI: swipe up on the bottom bar (the sliding panel
    # follows the finger and snaps to a stage). The harness has no
    # generic swipe; scroll_to is its only swipe primitive (it swipes
    # up until the target node appears), so it is used here as the
    # panel swipe, targeting the controls-stage "next" button.
    r.scroll_to("Ed9ad8ad1", res_id="next")

    # Ee8de0c7d -- ENTERS S_SLIDE_LIBRARY: the panel snaps to the stage
    # with the controls (guard: mDidScroll and the target stage shows
    # the control buttons).
    r.wait_for("Ee8de0c7d", res_id="next")

    # E5c102dcf -- GUI: tap one of the control buttons (next). Tapped
    # within seconds of playback starting on a ~20 s song, so the
    # played percentage is at most 50% (SHIFT_NEXT_SONG branch).
    r.tap("E5c102dcf", res_id="next")

    # Eb90ef0a1 -- CALL: call made in the click branch (to
    # PlaybackActivity.onClick).
    r.comment("click-branch dispatch, no user action", "Eb90ef0a1")

    # Ed8f23832 -- CALL: the button next was tapped (guard:
    # view.getId() == R.id.next).
    r.comment("next-button branch, no user action", "Ed8f23832")

    # Ec958d00b -- CALL: call made for this button (to shiftCurrentSong).
    r.comment("dispatch to shiftCurrentSong, no user action", "Ec958d00b")

    # E6515cc1d -- CALL: PlaybackActivity.shiftCurrentSong ->
    # PlaybackService.shiftCurrentSong (direct call).
    r.comment("dispatch to the service, no user action", "E6515cc1d")

    # Edc966b36 -- CALL: shiftCurrentSong -> preparePlayCountsUpdate
    # (direct call).
    r.comment("dispatch to preparePlayCountsUpdate, no user action",
              "Edc966b36")

    # Ec66727e1 -- ASYNC: the MSG_UPDATE_PLAYCOUNTS branch runs (guard:
    # isPlaying() and SHIFT_NEXT_SONG with at most 50% played -- met by
    # the prompt "next" tap above, seconds into a ~20 s song).
    r.comment("MSG_UPDATE_PLAYCOUNTS branch (guard met: next tapped at "
              "<=50% played), no user action", "Ec66727e1")

    # E681d9bad -- CALL: call made in the message branch (to
    # PlayCountsHelper.countSong).
    r.comment("dispatch to countSong, no user action", "E681d9bad")

    # E8c6979ac -- CALL: countSong -> MediaLibrary.updateSongPlayCounts
    # (the target). The message is sent delayed by 800 ms, so the
    # evidence steps below also serve as dwell time before run_app.sh
    # takes the coverage dump.
    r.screenshot("route_18_after_next", "E8c6979ac")
    r.dump_ui("route_18_after_next", "E8c6979ac")

    r.done()


if __name__ == "__main__":
    main()
