#!/usr/bin/env python3
"""Vanilla-Music route_04: CoverCache$BitmapDiskCache.getUsedSpace.

Method: CoverCache$BitmapDiskCache.getUsedSpace
Edge ids in order (ROUTES.csv row route_04, verbatim):
    E47380ade E0fd35a14 Eb282789e E860e3aca Eb10496ae E0f17da19
    E0b074369 E2ef1bab0 E277de41c Eee1c8b4a E244d89c0 E829b83f9
    Ec354a6e8
Printed route source: the CoverCache$BitmapDiskCache.getUsedSpace path
    row of graphs/Vanilla-Music/verification.csv (ref
    LibraryPagerAdapter.java:353; MediaAdapter.java:554; Song.java:
    256,273; CoverCache.java:122,148,348,274) plus the route_04 row of
    device/routes/Vanilla-Music/ROUTES.csv. Steps read: instantiateItem
    -> MediaAdapter.getView -> row.getCoverView().setCover ->
    LazyCoverView.handleMessage(MSG_CREATE_COVER) -> Song.getSmallCover
    -> getCoverInternal -> CoverCache.getCoverFromSong -> storeCover
    -> BitmapDiskCache.put -> trim -> getUsedSpace. The route needs
    at least one scanned song with cover handling; any setup Music
    fixture song qualifies.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty; no STATE file gate).
Setup: push fixtures/Music + media scan (run_app.sh does pm clear and
    the setup step before this script, so the script starts by
    launching the app).

UI mapping (layout XML and strings.xml read, nothing invented):
  - Launcher activity is LibraryActivity (AndroidManifest.xml:73-90,
    MAIN/LAUNCHER); component is <package>/.LibraryActivity.
  - Scanned-content wait targets come from the setup fixtures' ID3v2
    tags, verified by reading the fixture files: "01 Morning Light.
    mp3" has TPE1 "Aria North" and TALB "Daybreak". The default first
    tab is Artists, so an "Aria North" row proves the library is
    populated; the Albums tab (title R.string.albums = "Albums",
    res/values/translatable.xml:130) shows album rows, and a
    "Daybreak" row proves album-row rendering, which is the
    cover-loading path: MediaAdapter.getView binds the row cover view
    (draggable_row.xml cover id) and setCover drives the disk-cache
    chain.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E47380ade", "E0fd35a14", "Eb282789e", "E860e3aca", "Eb10496ae",
    "E0f17da19", "E0b074369", "E2ef1bab0", "E277de41c", "Eee1c8b4a",
    "E244d89c0", "E829b83f9", "Ec354a6e8",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Vanilla-Music route_04")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_04", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade S_ENTRY -> LibraryActivity.<init>: MAIN / LAUNCHER
    # intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")
    # E0fd35a14 LibraryActivity.<init> -> LibraryActivity.onCreate:
    # Activity lifecycle callback. Wait for a scanned artist row so
    # the library list is rendered from the setup scan before the
    # cover chain is expected to run.
    r.wait_for("E0fd35a14", text="Aria North", timeout=60)
    # Eb282789e LibraryActivity.onCreate ->
    # LibraryPagerAdapter.instantiateItem: pager.setAdapter(...): the
    # ViewPager asks the adapter for the first pages (INFERRED,
    # androidx source not read; guard: the pager starts on page 0 and
    # keeps one page on each side). Framework-driven; no user action.
    r.comment("ViewPager setAdapter asks for first pages", "Eb282789e")
    # E860e3aca LibraryPagerAdapter.instantiateItem ->
    # MediaAdapter.getView: the tab's ListView reads the rows
    # (list.setAdapter(adapter), LibraryPagerAdapter.java:353). Show
    # the Albums tab so album rows (with covers) render: tap the
    # tab, then wait for an album row.
    r.tap("E860e3aca", text="Albums")
    r.wait_for("E860e3aca", text="Daybreak", timeout=60)
    # Eb10496ae MediaAdapter.getView -> LazyCoverView.setCover:
    # Direct call (MediaAdapter.java:554). Automatic once rows render.
    r.comment("getView calls row cover setCover", "Eb10496ae")
    # E0f17da19 LazyCoverView.setCover -> LazyCoverView.handleMessage:
    # cache miss: sHandler.sendMessage(sHandler.obtainMessage
    # (MSG_CREATE_COVER, payload)): the worker handler thread builds
    # the cover. Automatic.
    r.comment("cover miss posts MSG_CREATE_COVER", "E0f17da19")
    # E0b074369 LazyCoverView.handleMessage -> Song.getSmallCover:
    # Direct call. Automatic.
    r.comment("handleMessage calls getSmallCover", "E0b074369")
    # E2ef1bab0 Song.getSmallCover -> Song.getCoverInternal: Direct
    # call. Automatic.
    r.comment("getSmallCover calls getCoverInternal", "E2ef1bab0")
    # E277de41c Song.getCoverInternal -> CoverCache.getCoverFromSong:
    # Direct call. Automatic.
    r.comment("getCoverInternal calls getCoverFromSong", "E277de41c")
    # Eee1c8b4a CoverCache.getCoverFromSong -> CoverCache.storeCover:
    # Direct call. Automatic.
    r.comment("getCoverFromSong calls storeCover", "Eee1c8b4a")
    # E244d89c0 CoverCache.storeCover ->
    # CoverCache$BitmapDiskCache.put: Direct call. Automatic.
    r.comment("storeCover calls disk cache put", "E244d89c0")
    # E829b83f9 CoverCache$BitmapDiskCache.put ->
    # CoverCache$BitmapDiskCache.trim: Direct call. Automatic.
    r.comment("put calls trim", "E829b83f9")
    # Ec354a6e8 CoverCache$BitmapDiskCache.trim ->
    # CoverCache$BitmapDiskCache.getUsedSpace: Direct call. Record a
    # UI dump as run evidence (covers rendered in the album list).
    r.dump_ui("album_list", "Ec354a6e8")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
