"""Device replay script for Vanilla-Music route_30 (REWORK, unpushed).

Method: PlaybackService.getDuration
Edge ids: E47380ade E29472d10 E80427a98 Ed9ad8ad1 Ee8de0c7d E5c102dcf
    Eb90ef0a1 Ec3643f74 E2cb5514d E814a0c90 Eaa64b5e6
Printed route source: graphs/Vanilla-Music/verification.csv path row
    (result fixed; ref PlaybackActivity.java:317-331,221-223,222,207;
    PlaybackService.java:1774) and
    device/routes/Vanilla-Music/ROUTES.csv route_30.
Permissions (ROUTES.csv): none. Fixtures: none (no STATE file gate).
Setup: push fixtures/Music + media scan (run_app setup step).
Standard config: run_app does pm clear before this script; the script
    starts by launching the app.

REWORK NOTE (why the original failed, auditor-proven): the original
    script tapped Previous with no song playing. rewindCurrentSong
    (PlaybackService.java:1772-1777) calls getDuration() only if
    getPosition() > 2500 (REWIND_AFTER_PLAYED_MS = 2500, :105),
    short-circuit &&; idle getPosition() returns 0 (:1655-1659), so
    the target was certainly missed. This rework starts playback and
    then SEEKS to 10 s before the Previous tap, using only delivered
    harness actions -- no sleep/dwell primitive is needed, because the
    seek is a UI-driven position step, not a wait:

    - Start playback exactly as route_18 does (auditor-PASS): Songs
      tab "Tracks", tap "Morning Light" (fixture 01 Morning Light.mp3,
      ID3 title verified; default row action plays all, so playback
      starts and the queue is filled). This makes
      mMediaPlayerInitialized true, which seekToPosition requires
      (PlaybackService.java:1699-1704: returns early unless
      initialized, else mMediaPlayer.seekTo(msec)).
    - Open the options menu (MENU key, as route_01 does) and tap
      "Jump to Time": LibraryActivity extends SlidingPlaybackActivity
      (LibraryActivity.java:66-67), its onCreateOptionsMenu calls
      super (LibraryActivity.java:852-854), and the super menu adds
      MENU_JUMP_TO_TIME (SlidingPlaybackActivity.java:131, string
      "Jump to Time", translatable.xml:335); onOptionsItemSelected
      falls through to super (LibraryActivity.java:914) and the super
      case shows the dialog (SlidingPlaybackActivity.java:152-153).
    - In the dialog (layout duration_input.xml: hours/minutes/
      seconds EditTexts, ids hours/minutes/seconds), tap the seconds
      field, type "10", tap "OK" (android.R.string.ok, standard
      Android string -- live-confirm item, same class as route_29's
      standard strings). Hours/minutes left empty parse as 0
      (JumpToTimeDialog.java:130-137), so position =
      (0*3600 + 0*60 + 10) * 1000 = 10000 ms
      (JumpToTimeDialog.java:112-118), delivered via
      onPositionSubmit -> seekToPosition(10000)
      (SlidingPlaybackActivity.java:345-347).
    - Guard check at the Previous tap: getPosition() ~= 10000 > 2500
      AND getDuration() ~= 19938 > 5000 (fixture duration printed by
      ffprobe this session: 19.937813 s for 01 Morning Light.mp3;
      10000 < 19938, so the seek lands inside the song, and the
      swipe/tap steps after the seek only let the position grow --
      ~10 s of headroom remains, no end-of-song risk). The
      rewindCurrentSong condition therefore evaluates getDuration(),
      which IS the target method.
    - The after_seek dump is a live-verification aid only (the
      elapsed TextView should read ~0:10); no script step depends
      on parsing it.

    All pre-phase actions are logged under E80427a98 (the S_LIBRARY
    entry edge), the same convention route_18 uses for its
    playback-start taps. The route's own 11 edges then follow in
    ROUTES.csv order, unchanged. No pm clear call, no fixed
    coordinates, no private _shell use, no placeholder text.
Gesture note: the harness has no raw swipe action. The swipe-up on the
    bottom bar is performed with scroll_to, whose implementation swipes
    up (500,1500 -> 500,500) until the controls-stage target appears;
    the target here is the Previous button (content description
    "Previous track", controls.xml @+id/previous). That swipe IS the
    panel gesture of edge Ed9ad8ad1, not a generic scroll.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ["E47380ade", "E29472d10", "E80427a98", "Ed9ad8ad1", "Ee8de0c7d",
            "E5c102dcf", "Eb90ef0a1", "Ec3643f74", "E2cb5514d", "E814a0c90",
            "Eaa64b5e6"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_30", edge_ids=EDGE_IDS,
               log_path=a.log, dry_run=a.dry_run, outdir=a.outdir)
    # E47380ade: S_ENTRY -> LibraryActivity.<init>
    # MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("ch.blinkenlights.android.vanilla/.LibraryActivity",
             "E47380ade")
    # E29472d10: LibraryActivity.<init> -> onResume@LibraryActivity.
    # Activity lifecycle callback; no user action.
    r.comment("lifecycle: onResume runs on launch", "E29472d10")
    # E80427a98: onResume@LibraryActivity -> S_LIBRARY.
    # LibraryActivity is resumed and shown (default tab Artists).
    r.wait_for("E80427a98", text="Play all", timeout=30)
    # E80427a98 (pre-phase 1): start playback, as route_18 does.
    # Songs tab "Tracks", then "Morning Light": the default row action
    # plays all from that row, so playback starts, the queue is filled,
    # and mMediaPlayerInitialized becomes true (required by
    # seekToPosition, PlaybackService.java:1699-1704).
    r.wait_for("E80427a98", text="Tracks")
    r.tap("E80427a98", text="Tracks")
    r.wait_for("E80427a98", text="Morning Light")
    r.tap("E80427a98", text="Morning Light")
    # E80427a98 (pre-phase 2): seek to 10 s via Jump to Time.
    # MENU key opens LibraryActivity's options menu (super menu adds
    # "Jump to Time"); tapping it shows JumpToTimeDialog; tapping the
    # seconds field, typing "10", and tapping "OK" submits position
    # 10000 ms -> seekToPosition(10000) -> mMediaPlayer.seekTo(10000).
    # getPosition() is then ~= 10000 > 2500, so rewindCurrentSong's
    # condition evaluates getDuration() (the target) at the Previous
    # tap below. Hours/minutes left empty parse as 0.
    r.key("MENU", "E80427a98")
    r.wait_for("E80427a98", text="Jump to Time")
    r.tap("E80427a98", text="Jump to Time")
    r.wait_for("E80427a98", res_id="seconds")
    r.tap("E80427a98", res_id="seconds")
    r.type_text("10", "E80427a98")
    r.tap("E80427a98", text="OK")
    # E80427a98 (pre-phase 3): live-verification aid only. The dump
    # lets the device lead confirm the elapsed readout is ~0:10; no
    # step depends on parsing it.
    r.dump_ui("after_seek", "E80427a98")
    # Ed9ad8ad1: S_LIBRARY -> SlidingView.onTouch@LIBRARY.
    # Swipe up on the bottom bar; the sliding panel follows the finger.
    # scroll_to performs that swipe-up until the controls-stage
    # Previous button appears. scroll_to takes text or res_id only, so
    # the swipe target is the Previous button's resource id
    # (controls.xml @+id/previous); the tap below uses its content
    # description "Previous track".
    r.scroll_to("Ed9ad8ad1", res_id="previous")
    # Ee8de0c7d: onTouch@LIBRARY -> S_SLIDE_LIBRARY.
    # The panel snaps to the stage with the controls; no new action.
    r.comment("panel snap: controls stage reached", "Ee8de0c7d")
    # E5c102dcf: S_SLIDE_LIBRARY -> onClick(View)@BUTTON.
    # Tap one of the control buttons: Previous. Playback position is
    # now ~= 10 s (seek) plus the swipe time, so getPosition() > 2500
    # and getDuration() (~20 s) > 5000: rewindCurrentSong evaluates
    # getDuration(), the target.
    r.tap("E5c102dcf", desc="Previous track")
    # Eb90ef0a1: onClick(View)@BUTTON -> PlaybackActivity.onClick.
    # Call made in the click branch; no new action.
    r.comment("click branch: button click dispatches", "Eb90ef0a1")
    # Ec3643f74: onClick -> onClick@previous (previous button branch).
    r.comment("button branch: previous was tapped", "Ec3643f74")
    # E2cb5514d: onClick@previous -> rewindCurrentSong. Call for button.
    r.comment("call made for this button: rewind", "E2cb5514d")
    # E814a0c90: rewindCurrentSong -> PlaybackService.rewindCurrentSong.
    # Direct call.
    r.comment("direct call: activity rewinds via the service", "E814a0c90")
    # Eaa64b5e6: rewindCurrentSong -> getDuration. Direct call; target.
    # Reached because the seek established getPosition() > 2500, so
    # the && condition evaluates its second operand, getDuration().
    r.comment("direct call: rewind reads the duration (target)", "Eaa64b5e6")
    r.done()


if __name__ == "__main__":
    main()
