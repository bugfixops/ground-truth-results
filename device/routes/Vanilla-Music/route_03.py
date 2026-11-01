#!/usr/bin/env python3
"""Vanilla-Music route_03: SongTimeline.removeSongPosition.

Method: SongTimeline.removeSongPosition
Edge ids in order (ROUTES.csv row route_03, verbatim):
    E47380ade E0fd35a14 Ecb02a323 Ec9e7b28f Ec2fb656d Ebe7c67e2
    Efb4fd81b Eb3377bc5 E3c43ea09 E5df70fe0 E5ca43de1 E82d06991
    Eab28d2eb Eacaaa856 Ec579ae8c Ed1c4bbde Eb511df54 E0fa3601c
Printed route source: the SongTimeline.removeSongPosition path row of
    graphs/Vanilla-Music/verification.csv (ref DragSortController.
    java:243-256,411-420; DragSortListView.java:1177-1178,1206-1209,
    1800-1850,2882-2920; ShowQueueFragment.java:202;
    PlaybackService.java:2395) plus the route_03 row of
    device/routes/Vanilla-Music/ROUTES.csv. Steps read (final route):
    onScroll -> startDrag (guarded: ON_DRAG mode, touch slop, sort
    enabled) -> SmoothAnimator.start/run -> RemoveAnimator.onStop
    (fraction >= 1f) -> doRemoveItem -> ShowQueueFragment.remove ->
    PlaybackService.removeSongPosition -> SongTimeline.
    removeSongPosition. The route needs a queue with at least two
    songs and a drag-to-sort animation run to completion (swipe, not
    tap).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty; no STATE file gate).
Setup: push fixtures/Music + media scan (run_app.sh does pm clear and
    the setup step before this script, so the script starts by
    launching the app).

UI mapping (layout XML and strings.xml read, nothing invented):
  - Launcher activity is LibraryActivity (AndroidManifest.xml:73-90,
    MAIN/LAUNCHER); component is <package>/.LibraryActivity.
  - Tab titles come from LibraryPagerAdapter.TITLES: the song tab
    title is R.string.songs = "Tracks" (res/values/translatable.xml:
    133). The header row text on a song list is R.string.play_all =
    "Play all" (translatable.xml:149; LibraryActivity.updateHeaders
    sets the header to "Play all" unless the default action is
    enqueue), and tapping it enqueues every scanned song and starts
    playback, which gives a queue of 12+ songs from the setup
    fixtures -- well over the two-song minimum. No song title is
    invented: the wait target is the header text itself.
  - The queue is the ShowQueueFragment in library_content.xml
    (fragment id "queue", DragSortListView from showqueue_listview.
    xml with drag_start_mode="onMove", remove_enabled=true,
    remove_mode="flingRemove", drag_handle_id and fling_handle_id
    "@+id/dragger"). Queue rows use draggable_row.xml; in the queue
    adapter (ShowQueueAdapter.getView) rows are set up with
    LAYOUT_DRAGGABLE, so the dragger handle is visible there, while
    it is GONE in plain library rows. Scrolling until a "dragger"
    node appears therefore proves the queue stage is revealed.
  - Drag gesture: the harness has no targeted drag primitive; its
    only swipe is scroll_to, which issues `input swipe 500 1500 500
    500` until the target node appears. That upward swipe is the
    drag gesture used here: it starts near the bottom bar (the
    SlidingView handle, library_content.xml slider_handle_id
    "@+id/bottombar_controls") and moves vertically past the touch
    slop, which is the onScroll -> startDrag gesture of the route.
    See REPORT.md for the geometry caveat: DragSortController only
    starts a drag when the touch down lands on the dragger handle
    (viewIdHitPosition), so the device lead must confirm on the
    replay image that the swipe starts a drag; if it only scrolls
    the list, the harness needs a drag primitive before this route
    can reach its target on a real device. The dry run below only
    proves edge ids and script shape, not gesture geometry.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E47380ade", "E0fd35a14", "Ecb02a323", "Ec9e7b28f", "Ec2fb656d",
    "Ebe7c67e2", "Efb4fd81b", "Eb3377bc5", "E3c43ea09", "E5df70fe0",
    "E5ca43de1", "E82d06991", "Eab28d2eb", "Eacaaa856", "Ec579ae8c",
    "Ed1c4bbde", "Eb511df54", "E0fa3601c",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Vanilla-Music route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade S_ENTRY -> LibraryActivity.<init>: MAIN / LAUNCHER
    # intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")
    # E0fd35a14 LibraryActivity.<init> -> LibraryActivity.onCreate:
    # Activity lifecycle callback. No user action.
    r.comment("system creates LibraryActivity", "E0fd35a14")
    # Ecb02a323 LibraryActivity.onCreate -> ShowQueueFragment.<init>:
    # setContentView inflates the <fragment class=ShowQueueFragment>
    # of library_content.xml. Wait for the library to be populated
    # from the setup scan before building the queue.
    r.wait_for("Ecb02a323", text="Aria North", timeout=60)
    # Ec9e7b28f ShowQueueFragment.<init> ->
    # ShowQueueFragment.onCreateView: Fragment lifecycle callback.
    # No user action.
    r.comment("queue fragment onCreateView runs", "Ec9e7b28f")
    # Ec2fb656d ShowQueueFragment.onCreateView ->
    # DragSortListView.<init>: setContentView / inflate builds the
    # view or fragment <DragSortListView> of showqueue_listview.xml.
    # Framework inflation; no user action.
    r.comment("queue DragSortListView inflated", "Ec2fb656d")
    # Ebe7c67e2 DragSortListView.<init> -> DragSortController.onTouch:
    # the touch dispatch calls the OnTouchListener registered in the
    # constructor (super.setOnTouchListener(controller), the default
    # DragSortController). Preamble under this edge: build a queue
    # with at least two songs (Tracks tab -> "Play all" header), then
    # swipe the sliding view up until a queue dragger is on screen,
    # which reveals the queue stage.
    r.tap("Ebe7c67e2", text="Tracks")
    r.wait_for("Ebe7c67e2", text="Play all", timeout=60)
    r.tap("Ebe7c67e2", text="Play all")
    r.scroll_to("Ebe7c67e2", res_id="dragger")
    # Efb4fd81b DragSortController.onTouch -> DragSortController.
    # onScroll: the GestureDetector dispatches the next touch event
    # of the same gesture (guard: isDragEnabled() is true). The drag
    # gesture itself: an upward swipe over the revealed queue (the
    # harness swipe primitive), run so the drag-to-sort animation
    # plays to completion instead of a tap.
    r.scroll_to("Efb4fd81b", res_id="dragger")
    # Eb3377bc5 DragSortController.onScroll -> DragSortController.
    # startDrag: the vertical drag exceeds the touch slop while the
    # drag handle is held and sorting is enabled (drag_start_mode=
    # onMove, sort_enabled default true). Automatic once the drag
    # gesture starts.
    r.comment("drag exceeds slop, startDrag fires", "Eb3377bc5")
    # E3c43ea09 DragSortController.startDrag ->
    # DragSortListView.startDrag(int,int,int,int): Direct call.
    # Automatic.
    r.comment("controller startDrag calls list startDrag", "E3c43ea09")
    # E5df70fe0 DragSortListView.startDrag(int,int,int,int) ->
    # DragSortListView.startDrag(int,View,int,int,int): Direct call.
    # Automatic.
    r.comment("startDrag overload chains", "E5df70fe0")
    # E5ca43de1 DragSortListView.startDrag(int,View,int,int,int) ->
    # DragSortListView$SmoothAnimator.start: Direct call. Automatic.
    r.comment("startDrag starts the animator", "E5ca43de1")
    # E82d06991 DragSortListView$SmoothAnimator.start ->
    # DragSortListView$SmoothAnimator.run: post(this): the animation
    # loop runs. Automatic.
    r.comment("animator loop runs", "E82d06991")
    # Eab28d2eb DragSortListView$SmoothAnimator.run ->
    # DragSortListView$RemoveAnimator.onStop: the animation reached
    # its end (guard: fraction >= 1f). Automatic once the animation
    # completes.
    r.comment("animation completes, onStop fires", "Eab28d2eb")
    # Eacaaa856 DragSortListView$RemoveAnimator.onStop ->
    # DragSortListView.doRemoveItem(): Direct call (through
    # DragSortListView.access$1900). Automatic.
    r.comment("onStop calls doRemoveItem", "Eacaaa856")
    # Ec579ae8c DragSortListView.doRemoveItem() ->
    # DragSortListView.doRemoveItem(int): Direct call. Automatic.
    r.comment("doRemoveItem overload chains", "Ec579ae8c")
    # Ed1c4bbde DragSortListView.doRemoveItem(int) ->
    # ShowQueueFragment.remove: Virtual/interface call that can
    # dispatch to this implementation. Automatic.
    r.comment("doRemoveItem calls fragment remove", "Ed1c4bbde")
    # Eb511df54 ShowQueueFragment.remove ->
    # PlaybackService.removeSongPosition: Direct call. Automatic.
    r.comment("fragment remove calls service", "Eb511df54")
    # E0fa3601c PlaybackService.removeSongPosition ->
    # SongTimeline.removeSongPosition: Direct call. Record a UI dump
    # as run evidence (the queue now holds one fewer song).
    r.dump_ui("queue_after_drag", "E0fa3601c")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
