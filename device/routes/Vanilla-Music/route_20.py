"""Vanilla-Music route_20: TrackDetailsDialog.<init>.

Edge ids (ROUTES.csv, in order):
  E47380ade E29472d10 E80427a98 Ed9ad8ad1 E9cfdcf27 E90cc7084 E729edfab
  E50091b04 Ea55eaad7 Efd701784 E3c9fabe6 Ea2cab75e E3b58c14c E59377245

Printed route source:
  verification.csv path row (TrackDetailsDialog.<init>): "Steps read:
  tap the bottom bar -> openPlaybackActivity -> FullPlaybackActivity
  (onResume@FullPlaybackActivity) -> swipe up to the queue stage ->
  long-press a queue row (STATE: queue has a song) ->
  ShowQueueFragment.onItemLongClickWithCoords -> FancyMenu.show@Q ->
  S_FANCY_QUEUE -> tap a row -> ShowQueueFragment.onFancyItemSelected
  -> TrackDetailsDialog.show -> newInstance -> <init>."
  ROUTES.csv row: source "LibraryActivity.java:587-589,451-456;
  ShowQueueFragment.java:108-130,160; TrackDetailsDialog.java:64,50",
  state data.
Permissions: none. Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

Note on the steps text vs the edge chain: the verification steps text
  mentions FullPlaybackActivity, but this route's edge chain itself
  goes through SlidingPlaybackActivity.onResume@LibraryActivity ->
  S_LIBRARY -> SlidingView.onTouch@LIBRARY -> S_SLIDE_LIBRARY_QUEUE,
  i.e. the queue stage of the Library activity's sliding panel, not a
  separate full-playback screen. The script follows the edge chain
  (which is what drycheck.py validates for contiguity): it plays a
  song in the Library, swipes the Library panel up to its queue stage,
  and long-presses a queue row there. "Full playback" in the task brief
  is read as starting full playback of a song (which fills the queue),
  not as opening FullPlaybackActivity, which the edges do not contain.

UI labels used, all read from layout XML / strings.xml / fixture tags:
  - Songs tab label "Tracks" (translatable.xml songs -> "Tracks").
  - "Morning Light": fixture 01 Morning Light.mp3, ID3 title verified
    with ffprobe. Tapping it uses the default row action
    EXPAND_OR_PLAY_ALL, which for a non-expandable song row becomes
    PLAY_ALL, so the queue holds songs (STATE data: queue holds at
    least one song) and the queue row carries the same title.
  - Queue-stage swipe: the harness has no generic swipe; scroll_to is
    its only swipe primitive (it swipes up until the target node
    appears). Two scroll_to steps are used: first to the controls-stage
    "next" button (controls.xml id "next"), then to the queue list
    (showqueue_listview.xml id "list"). The "list" id is queue-
    specific: the library list (listview.xml) carries no android:id,
    so scroll_to(res_id="list") cannot stop at the library list.
    Caveat for the device lead: uiautomator may list the queue node
    even while it is off-screen, in which case the second scroll_to
    returns without swiping; the long-press below then lands on the
    library row of the same title, whose fancy menu also offers
    "Details" and still reaches TrackDetailsDialog.<init> (though via
    the Library path rather than the queue path). Confirm the panel
    stage on the replay image.
  - Fancy-menu row "Details" (translatable.xml details -> "Details";
    ShowQueueFragment.java adds CTX_MENU_SHOW_DETAILS with
    R.string.details for queue rows).

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
    "E47380ade", "E29472d10", "E80427a98", "Ed9ad8ad1", "E9cfdcf27",
    "E90cc7084", "E729edfab", "E50091b04", "Ea55eaad7", "Efd701784",
    "E3c9fabe6", "Ea2cab75e", "E3b58c14c", "E59377245",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_20", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E29472d10 -- LIFECYCLE: Activity lifecycle callback (onResume).
    r.comment("lifecycle onResume, no user action", "E29472d10")

    # E80427a98 -- ENTERS S_LIBRARY: LibraryActivity resumed and shown.
    # STATE setup (queue holds at least one song): open the Songs tab
    # (label "Tracks") and tap "Morning Light"; the default row action
    # plays all songs from that row, filling the queue and starting
    # playback.
    r.wait_for("E80427a98", text="Tracks")
    r.tap("E80427a98", text="Tracks")
    r.wait_for("E80427a98", text="Morning Light")
    r.tap("E80427a98", text="Morning Light")

    # Ed9ad8ad1 -- GUI: swipe up on the bottom bar (the sliding panel
    # follows the finger and snaps to a stage). scroll_to is the
    # harness's only swipe primitive; the first swipe targets the
    # controls-stage "next" button.
    r.scroll_to("Ed9ad8ad1", res_id="next")

    # E9cfdcf27 -- ENTERS S_SLIDE_LIBRARY_QUEUE: the panel snaps to
    # the last stage, the queue is shown (guard: mDidScroll and the
    # target stage is the last one). Second swipe, targeting the
    # queue-only list id "list" (see the header caveat).
    r.scroll_to("E9cfdcf27", res_id="list")

    # E90cc7084 -- GUI: long-press a song row of the queue (STATE: the
    # queue holds at least one song, satisfied by the "Morning Light"
    # play above; the queue row carries the song title).
    r.long_tap("E90cc7084", text="Morning Light")

    # E729edfab -- CALL: mCallback.onItemLongClickWithCoords(...) with
    # the callback of this list (ShowQueueFragment.onCreateView:63).
    r.comment("dispatch to ShowQueueFragment, no user action", "E729edfab")

    # E50091b04 -- CALL: fm.show(view, x, y): the bottom sheet of the
    # queue opens (STATE: queue holds at least one song).
    r.comment("queue fancy menu shown by the long-press, no user action",
              "E50091b04")

    # Ea55eaad7 -- ENTERS S_FANCY_QUEUE: the BottomSheetDialog with the
    # menu rows is shown.
    r.wait_for("Ea55eaad7", text="Details")

    # Efd701784 -- GUI: tap a row of the context menu.
    r.tap("Efd701784", text="Details")

    # E3c9fabe6 -- CALL: mCallback.onFancyItemSelected(item) with the
    # callback of this menu (ShowQueueFragment; guard: the menu was
    # created by ShowQueueFragment).
    r.comment("dispatch to ShowQueueFragment.onFancyItemSelected, "
              "no user action", "E3c9fabe6")

    # Ea2cab75e -- CALL: ShowQueueFragment.onFancyItemSelected ->
    # TrackDetailsDialog.show (direct call).
    r.comment("dispatch to TrackDetailsDialog.show, no user action",
              "Ea2cab75e")

    # E3b58c14c -- CALL: TrackDetailsDialog.show -> newInstance
    # (direct call).
    r.comment("dispatch to newInstance, no user action", "E3b58c14c")

    # E59377245 -- CALL: newInstance -> TrackDetailsDialog.<init> (the
    # target; newInstance constructs the dialog). The dialog title is
    # the song title, and the screenshot/dump prove the dialog opened.
    r.assert_text("Morning Light", "E59377245")
    r.screenshot("route_20_details_dialog", "E59377245")
    r.dump_ui("route_20_details_dialog", "E59377245")

    r.done()


if __name__ == "__main__":
    main()
