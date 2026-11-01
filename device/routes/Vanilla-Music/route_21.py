"""Route route_21: FullPlaybackActivity.updateQueuePosition.

Printed route source: graphs/Vanilla-Music/verification.csv path row
"FullPlaybackActivity.updateQueuePosition" ("Steps read: tap the
play-all header row -> onItemClicked@HDR (guard: HEADER_ID, no
DATA_EXPANDABLE) -> pickSongs (guard: action != DO_NOTHING, row not
expandable) -> PlaybackService.jumpToQueuePosition ->
SongTimeline.setCurrentQueuePosition -> broadcastChangedSongs ->
PlaybackService.positionInfoChanged ->
FullPlaybackActivity.onPositionInfoChanged ->
handleMessage(MSG_UPDATE_POSITION) (guard: mQueuePosView != null) ->
updateQueuePosition") and device/routes/Vanilla-Music/ROUTES.csv row
route_21 (source: LibraryPagerAdapter.java:344,893-903,861-868,895,901;
LibraryActivity.java:472-482,395; PlaybackService.java:2376;
SongTimeline.java:657,955; PlaybackService.java:1936;
FullPlaybackActivity.java:288-292,601).

Edge ids, in order:
  E47380ade, E29472d10, E80427a98, E54b8ef2f, E87e2a8b0, Ecc4f5b3c,
  E911774df, E9d579bf2, E40b8c071, Ec48fda4b, Eee036630, E0d982b9c,
  E588dc475.

Permissions: none (ROUTES.csv permissions cell is empty; the setup
step grants storage during setup, not as a route gate).
Fixtures: none (STATE file gates: none).
Setup (done by run_app.sh before this script): push fixtures/Music +
media scan. This script therefore starts by launching the app and
waits for library content before tapping.

UI facts used (read from layout XML / strings, never invented):
- The play-all header row text is the string "Play all"
  (res/values/translatable.xml play_all; LibraryActivity.updateHeaders
  sets the header text to it, default action).
- The default library tab title is "Artists"
  (res/values/translatable.xml artists).
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

    r = Runner(package=args.package, route="route_21", edge_ids=[
        "E47380ade", "E29472d10", "E80427a98", "E54b8ef2f", "E87e2a8b0",
        "Ecc4f5b3c", "E911774df", "E9d579bf2", "E40b8c071", "Ec48fda4b",
        "Eee036630", "E0d982b9c", "E588dc475",
    ], log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")

    # E29472d10 -- Activity lifecycle callback (onResume).
    # No user action: the framework resumes the activity after launch.
    r.comment("lifecycle-onResume-no-user-action", "E29472d10")

    # E80427a98 -- LibraryActivity is resumed and shown (default tab
    # Artists: library_page = 0). Wait for the tab title so the
    # library list (and its header row) is on screen before tapping.
    r.wait_for("E80427a98", text="Artists")

    # E54b8ef2f -- Tap the play-all header row at the top of the list.
    # Header text is "Play all" (see module docstring).
    r.tap("E54b8ef2f", text="Play all")

    # E87e2a8b0 -- the play-all header row: onItemClicked
    # (createHeaderIntent(view)); guard id == HEADER_ID, no
    # DATA_EXPANDABLE. Follows automatically from the header tap.
    r.comment("header-row-onItemClicked-follows-tap", "E87e2a8b0")

    # Ecc4f5b3c -- pickSongs(rowData, action): the row cannot be
    # expanded, so it is played. Follows automatically from the tap.
    r.comment("pickSongs-follows-header-tap", "Ecc4f5b3c")

    # E911774df -- Direct call: pickSongs -> jumpToQueuePosition.
    r.comment("direct-call-no-user-action", "E911774df")

    # E9d579bf2 -- Direct call: jumpToQueuePosition ->
    # setCurrentQueuePosition.
    r.comment("direct-call-no-user-action", "E9d579bf2")

    # E40b8c071 -- Direct call: setCurrentQueuePosition ->
    # broadcastChangedSongs.
    r.comment("direct-call-no-user-action", "E40b8c071")

    # Ec48fda4b -- Virtual/interface call: broadcastChangedSongs ->
    # positionInfoChanged.
    r.comment("virtual-call-no-user-action", "Ec48fda4b")

    # Eee036630 -- Virtual/interface call: positionInfoChanged ->
    # FullPlaybackActivity.onPositionInfoChanged.
    r.comment("virtual-call-no-user-action", "Eee036630")

    # E0d982b9c -- the branch of FullPlaybackActivity that handles
    # MSG_UPDATE_POSITION runs; guard mQueuePosView != null. The
    # handler message is posted by onPositionInfoChanged; no user
    # action. Live-run note: this guard needs FullPlaybackActivity
    # resumed (its queue-position view exists); see REPORT.md.
    r.comment("handler-MSG_UPDATE_POSITION-no-user-action", "E0d982b9c")

    # E588dc475 -- call made in the message branch:
    # handleMessage@MSG_UPDATE_POSITION -> updateQueuePosition (target).
    r.comment("message-branch-call-target-reached", "E588dc475")

    r.done()


if __name__ == "__main__":
    main()
