#!/usr/bin/env python3
"""Vanilla-Music route_05: ID3v2File.getDecodedString.

Method: ID3v2File.getDecodedString
Edge ids in order (ROUTES.csv row route_05, verbatim):
    E47380ade E0fd35a14 Eef7789d1 Ee566b4bb E0f67e824 E93c3a45f
    E01c68b9a E2fa2cdaf Ee410857a E1359ed61 E6a94f385 E344b7606
    E57cb1983 E8b69515b E17851189 E1cb597dd E03196706 E0a51609d
    E9e711fb3
Printed route source: the ID3v2File.getDecodedString path row of
    graphs/Vanilla-Music/verification.csv (ref MiniPlaybackActivity.
    java:37-51,54-58; FullPlaybackActivity.java:680,513-515,544;
    PlaybackService.java:766; BastpUtil.java:63,73; Bastp.java:38,74;
    ID3v2File.java:106,163,211) plus the route_05 row of
    device/routes/Vanilla-Music/ROUTES.csv. Steps read: library
    content inflates SlidingView -> onLayout -> setExpansionStage(0)
    -> ViewPropertyAnimator ends -> AnimationListener.onAnimationEnd
    -> FullPlaybackActivity.onSlideExpansionChanged ->
    setExtraInfoVisible -> handleMessage(MSG_LOAD_EXTRA_INFO) ->
    loadExtraInfo -> PlaybackService.getReplayGainValues -> BastpUtil
    -> Bastp.getTags -> ID3v2File.getTags -> parse_v3_frames ->
    normalizeTaginfo -> getDecodedString. The route needs the full
    playback screen with extra-info loading.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty; no STATE file gate).
Setup: push fixtures/Music + media scan (run_app.sh does pm clear and
    the setup step before this script, so the script starts by
    launching the app).

UI mapping (layout XML and strings.xml read, nothing invented):
  - Launcher activity is LibraryActivity (AndroidManifest.xml:73-90,
    MAIN/LAUNCHER); component is <package>/.LibraryActivity.
  - The song tab title is R.string.songs = "Tracks" (res/values/
    translatable.xml:133) and its header row text is R.string.
    play_all = "Play all" (translatable.xml:149), which enqueues all
    scanned songs and starts playback of the first one. The setup
    fixtures carry ID3v2.3 headers (verified by reading the fixture
    files: they start with the bytes "ID3" version 3), so the playing
    song's tags take the parse_v3_frames branch of the chain.
  - Tapping the bottom bar content opens the full playback screen:
    BottomBarControls content view id is "content_controls"
    (res/layout/bottombar_controls.xml) and LibraryActivity.onClick
    calls openPlaybackActivity() for it (LibraryActivity.java:
    587-589), which starts FullPlaybackActivity (lines 451-456).
    The default display mode is "2" (PrefDefaults.DISPLAY_MODE),
    i.e. DISPLAY_INFO_WIDGETS, so FullPlaybackActivity uses
    full_playback_alt.xml, which contains the info table
    (res_id "info_table"); the plain full_playback.xml has none.
  - Extra-info guard: the setExtraInfoVisible -> handleMessage edge
    is guarded "visible && no MSG_LOAD_EXTRA_INFO pending", but the
    visible-extra-info setting defaults to false
    (PrefDefaults.VISIBLE_EXTRA_INFO), so onSlideExpansionChanged
    on a fresh install calls setExtraInfoVisible(false) and sends no
    message. The toggle that makes the guard true is tapping the
    info table: FullPlaybackActivity.onClick for R.id.info_table
    calls setExtraInfoVisible(!mExtraInfoVisible)
    (FullPlaybackActivity.java:660-662), which with visible=true
    sends MSG_LOAD_EXTRA_INFO (lines 513-515). That tap is therefore
    attached to the setExtraInfoVisible -> handleMessage edge, and
    the preceding onSlideExpansionChanged edge is comment-only.
  - Full playback open is proven by res_id "cover_view" (CoverView
    in full_playback_alt.xml). The extra-info table rows (genre,
    track, year, composer, path, format, replaygain) are filled by
    loadExtraInfo, but their final texts depend on the playing
    song's tags, so the script asserts no tag text; it records a UI
    dump on the final edge instead.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E47380ade", "E0fd35a14", "Eef7789d1", "Ee566b4bb", "E0f67e824",
    "E93c3a45f", "E01c68b9a", "E2fa2cdaf", "Ee410857a", "E1359ed61",
    "E6a94f385", "E344b7606", "E57cb1983", "E8b69515b", "E17851189",
    "E1cb597dd", "E03196706", "E0a51609d", "E9e711fb3",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Vanilla-Music route_05")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade S_ENTRY -> LibraryActivity.<init>: MAIN / LAUNCHER
    # intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")
    # E0fd35a14 LibraryActivity.<init> -> LibraryActivity.onCreate:
    # Activity lifecycle callback. Wait for a scanned artist row so
    # the library is populated from the setup scan before playback.
    r.wait_for("E0fd35a14", text="Aria North", timeout=60)
    # Eef7789d1 LibraryActivity.onCreate -> SlidingView.<init>
    # (Context,AttributeSet): setContentView / inflate builds the
    # view or fragment <SlidingView> of library_content.xml,
    # bottombar_controls.xml, controls.xml. Preamble under this edge:
    # play a song so the full playback screen has a current song
    # (Tracks tab -> "Play all" header).
    r.tap("Eef7789d1", text="Tracks")
    r.wait_for("Eef7789d1", text="Play all", timeout=60)
    r.tap("Eef7789d1", text="Play all")
    # Ee566b4bb SlidingView.<init>(Context,AttributeSet) ->
    # SlidingView.onLayout: the sliding view is laid out. Open the
    # full playback screen by tapping the bottom bar content; the
    # new screen's SlidingView then lays out.
    r.tap("Ee566b4bb", res_id="content_controls")
    r.wait_for("Ee566b4bb", res_id="cover_view")
    # E0f67e824 SlidingView.onLayout -> SlidingView.setExpansionStage:
    # Direct call. Automatic on layout.
    r.comment("onLayout calls setExpansionStage", "E0f67e824")
    # E93c3a45f SlidingView.setExpansionStage ->
    # SlidingView$AnimationListener.onAnimationEnd: the
    # ViewPropertyAnimator ends: onAnimationEnd is called. Automatic.
    r.comment("expansion animation ends", "E93c3a45f")
    # E01c68b9a SlidingView$AnimationListener.onAnimationEnd ->
    # FullPlaybackActivity.onSlideExpansionChanged: Virtual/interface
    # call that can dispatch to this implementation. Automatic.
    r.comment("animation end calls onSlideExpansionChanged", "E01c68b9a")
    # E2fa2cdaf FullPlaybackActivity.onSlideExpansionChanged ->
    # FullPlaybackActivity.setExtraInfoVisible: Direct call. On a
    # fresh install this call passes visible=false (the setting
    # defaults to false), so it sends no message; the guard-satisfying
    # toggle is the info-table tap on the next edge. No user action
    # in this block itself.
    r.comment("expansion change calls setExtraInfoVisible", "E2fa2cdaf")
    # Ee410857a FullPlaybackActivity.setExtraInfoVisible ->
    # FullPlaybackActivity.handleMessage@MSG_LOAD_EXTRA_INFO: the
    # branch of FullPlaybackActivity that handles MSG_LOAD_EXTRA_INFO
    # runs (guard: visible && no MSG_LOAD_EXTRA_INFO pending). Tap
    # the info table to toggle extra info on, which calls
    # setExtraInfoVisible(true) and sends MSG_LOAD_EXTRA_INFO.
    r.tap("Ee410857a", res_id="info_table")
    # E1359ed61 FullPlaybackActivity.handleMessage@MSG_LOAD_EXTRA_INFO
    # -> FullPlaybackActivity.loadExtraInfo: call made in the message
    # branch. Automatic.
    r.comment("message branch calls loadExtraInfo", "E1359ed61")
    # E6a94f385 FullPlaybackActivity.loadExtraInfo ->
    # PlaybackService.getReplayGainValues: Direct call. Automatic.
    r.comment("loadExtraInfo calls getReplayGainValues", "E6a94f385")
    # E344b7606 PlaybackService.getReplayGainValues ->
    # BastpUtil.getReplayGainValues: Direct call. Automatic.
    r.comment("service calls BastpUtil", "E344b7606")
    # E57cb1983 BastpUtil.getReplayGainValues ->
    # BastpUtil.getReplayGainValuesFromFile: Direct call. Automatic.
    r.comment("BastpUtil calls getReplayGainValuesFromFile", "E57cb1983")
    # E8b69515b BastpUtil.getReplayGainValuesFromFile ->
    # Bastp.getTags(String): Direct call. Automatic.
    r.comment("file helper calls Bastp.getTags", "E8b69515b")
    # E17851189 Bastp.getTags(String) ->
    # Bastp.getTags(RandomAccessFile): Direct call. Automatic.
    r.comment("getTags(String) calls getTags(RAF)", "E17851189")
    # E1cb597dd Bastp.getTags(RandomAccessFile) -> ID3v2File.getTags:
    # Direct call. Automatic.
    r.comment("getTags(RAF) calls ID3v2File.getTags", "E1cb597dd")
    # E03196706 ID3v2File.getTags -> ID3v2File.parse_v3_frames:
    # Direct call. Automatic (fixtures are ID3v2.3).
    r.comment("getTags calls parse_v3_frames", "E03196706")
    # E0a51609d ID3v2File.parse_v3_frames ->
    # ID3v2File.normalizeTaginfo: Direct call. Automatic.
    r.comment("parse_v3_frames calls normalizeTaginfo", "E0a51609d")
    # E9e711fb3 ID3v2File.normalizeTaginfo ->
    # ID3v2File.getDecodedString: Direct call. Record a UI dump as
    # run evidence (extra-info table filled for the playing song).
    r.dump_ui("full_playback_extra_info", "E9e711fb3")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
