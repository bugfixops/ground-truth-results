"""Route route_25: PlaybackActivity.onStateChange.

Printed route source: graphs/Vanilla-Music/verification.csv path row
"PlaybackActivity.onStateChange" ("Steps read: swipe up to the
controls stage -> long-press the shuffle/repeat button ->
onCreateContextMenu@LIBRARY -> S_CTX_BUTTON@LIBRARY ->
onContextItemSelected -> setState(int) (guard: state changed) ->
runOnUiThread -> PlaybackActivity$1.run -> onStateChange (guard: the
activity is Mini/AudioPicker/AudioSearch, the plain-PlaybackActivity
override)") and device/routes/Vanilla-Music/ROUTES.csv row route_25
(source: PlaybackActivity.java:325-330,676-690,692-702,700;
PlaybackActivity.java:256-266,263).

Edge ids, in order:
  E47380ade, E29472d10, E80427a98, Ed9ad8ad1, Ee8de0c7d, Ec8635c32,
  E49924471, E63ca4fce, Ea32e63ba, E8291b22a, Ece8f9411.

Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (STATE file gates: none).
Setup (done by run_app.sh before this script): push fixtures/Music +
media scan. This script therefore starts by launching the app and
waits for library content before proceeding.

State-change choice: run_app.sh runs pm clear before this script, so
the shuffle mode starts at its default, SHUFFLE_NONE (SongTimeline
SHUFFLE_NONE = 0). The script therefore long-presses the shuffle
button and taps "Shuffle tracks", which is different from the
current state, satisfying the setState guard (mState != state).

UI facts used (read from layout XML / strings / handler source,
never invented):
- The shuffle button is res id "shuffle" in controls.xml with
  content-description "Cycle shuffle mode"
  (@string/cycle_shuffle_mode); the repeat/end button is res id
  "end_action" with content-description "Cycle repeat mode".
- The shuffle context menu entries (PlaybackActivity.java:680-683)
  are "No shuffle", "Shuffle tracks", "Shuffle albums"
  (res/values/translatable.xml no_shuffle, shuffle_songs,
  shuffle_albums).
- The default library tab title is "Artists"
  (res/values/translatable.xml artists).

Swipe-up note: the harness has no raw swipe primitive. The swipe-up
step below uses scroll_to, whose real-mode implementation issues
upward swipes (500,1500 -> 500,500) until its target is found; the
target is the shuffle button (res id "shuffle"), which lives in the
controls stage. See REPORT.md for the live-run verification this
needs (dump_ui after the swipe) and for the fallback if the panel
does not move.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_25", edge_ids=[
        "E47380ade", "E29472d10", "E80427a98", "Ed9ad8ad1", "Ee8de0c7d",
        "Ec8635c32", "E49924471", "E63ca4fce", "Ea32e63ba", "E8291b22a",
        "Ece8f9411",
    ], log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")

    # E29472d10 -- Activity lifecycle callback (onResume).
    # No user action: the framework resumes the activity after launch.
    r.comment("lifecycle-onResume-no-user-action", "E29472d10")

    # E80427a98 -- LibraryActivity is resumed and shown (default tab
    # Artists: library_page = 0). Wait for the tab title so the
    # library screen (with its bottom bar / sliding panel) is on
    # screen before swiping.
    r.wait_for("E80427a98", text="Artists")

    # Ed9ad8ad1 -- Swipe up on the bottom bar (the sliding panel
    # follows the finger and snaps to a stage). The harness has no
    # raw swipe: scroll_to issues upward swipes (500,1500 ->
    # 500,500) until its target is found, so the target is the
    # shuffle button of the controls stage (res id "shuffle").
    # The dump after the swipe is evidence for the live run: it
    # lets the device lead confirm the panel actually reached the
    # controls stage (see REPORT.md).
    r.scroll_to("Ed9ad8ad1", res_id="shuffle")
    r.dump_ui("after_swipe_up", "Ed9ad8ad1")

    # Ee8de0c7d -- the panel snaps to the stage with the controls
    # (ACTION_UP after a scroll); guard mDidScroll and the target
    # stage shows the control buttons. Follows from the swipe-up.
    r.comment("panel-snaps-to-controls-stage", "Ee8de0c7d")

    # Ec8635c32 -- Long-press the shuffle or the repeat button.
    # Shuffle button by content-description "Cycle shuffle mode"
    # (controls.xml); the shuffle menu is the one whose entry
    # ("Shuffle tracks") is known to differ from the default state.
    r.long_tap("Ec8635c32", desc="Cycle shuffle mode")

    # E49924471 -- the context menu of the button is shown. Wait for
    # the "No shuffle" menu entry so the menu is on screen.
    r.wait_for("E49924471", text="No shuffle")

    # E63ca4fce -- Tap an entry of the shuffle / repeat context
    # menu. "Shuffle tracks" differs from the default SHUFFLE_NONE
    # state, so setState's state-changed guard passes.
    r.tap("E63ca4fce", text="Shuffle tracks")

    # Ea32e63ba -- Direct call: onContextItemSelected -> setState.
    r.comment("direct-call-no-user-action", "Ea32e63ba")

    # E8291b22a -- runOnUiThread(new Runnable(){...}) runs
    # onStateChange(state, toggled) on the UI thread; guard the
    # state changed (mState != state). Follows from the menu tap.
    r.comment("runOnUiThread-guard-state-changed", "E8291b22a")

    # Ece8f9411 -- onStateChange(...) of the instance that runs the
    # code (the plain PlaybackActivity version). Reached through
    # the runnable; on LibraryActivity the call passes through
    # SlidingPlaybackActivity.onStateChange's super call to this
    # plain override (see REPORT.md).
    r.comment("runnable-call-target-reached", "Ece8f9411")

    r.done()


if __name__ == "__main__":
    main()
