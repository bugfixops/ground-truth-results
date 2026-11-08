"""Vanilla-Music route_11: PlaylistActivity.onFancyItemSelected.

Edge ids (ROUTES.csv, in order):
  E47380ade E29472d10 E80427a98 Ebe48c047 E47e1fc64 E4b9b8513
  Ec2a699b7 Ea3fb04b3 E1e5cc37a E5e427574 E82a5616a Ef41e17fa
  Efcc804f6 Eddae5477 Ea7e94b12

Printed route source:
  verification.csv path row (PlaylistActivity.onFancyItemSelected):
  "Steps read: tap the expand arrow of a Playlists-tab row (STATE:
  Playlists tab visible and a playlist exists) -> onItemExpanded@PL
  (guard: type == TYPE_PLAYLIST) -> editPlaylist ->
  PlaylistActivity.onCreate -> S_PLAYLIST -> long-press a song row
  (STATE: the playlist has a song) -> onItemLongClickWithCoords ->
  FancyMenu.show@P -> S_FANCY_PLAYLIST -> tap a row ->
  PlaylistActivity.onFancyItemSelected (the menu was built with
  callback=this, guard holds)."
  ROUTES.csv row: source "MediaAdapter.java:499,610-617;
  LibraryActivity.java:493-495,732-737; PlaylistActivity.java:102-158,
  211-225; FancyMenu.java:169-190,173-185,72-76,178", env empty,
  state data;session.
Permissions: none (ROUTES.csv). Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

UI labels used, all read from layout XML / strings.xml, never invented:
  - Songs tab label "Tracks" (translatable.xml: <string
    name="songs">Tracks</string>).
  - Song row "Morning Light": fixture 01 Morning Light.mp3, ID3 title
    "Morning Light" (verified with ffprobe on the setup fixtures).
  - Fancy-menu rows "Add to playlist…" (R.string.add_to_playlist),
    "New playlist…" (R.string.new_playlist), "Create"
    (R.string.create), "Play" (R.string.play).
  - Playlists tab label "Playlists" (R.string.playlists).
  - PlaylistActivity song list res_id "list"
    (res/layout/playlist_activity.xml).
  - Expand arrow res_id "dragger": MediaAdapter rows call
    row.setDraggerOnClickListener(this) (MediaAdapter.java:610-617),
    and the row layout's expander view is @+id/dragger
    (res/layout/draggable_row.xml). The route edge itself names the
    trigger "tap the arrow at the right end of an expandable row".
  - Playlist created here is named "Route11". run_app.sh runs pm clear
    before this script, so on a fresh install Route11 is the only
    playlist and the first dragger row is its row.

Setup steps (create the playlist and add a song first if fresh) live
in the S_LIBRARY block: they must run before the expand-arrow tap, and
every harness call names a route edge id.

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
    "E47380ade", "E29472d10", "E80427a98", "Ebe48c047", "E47e1fc64",
    "E4b9b8513", "Ec2a699b7", "Ea3fb04b3", "E1e5cc37a", "E5e427574",
    "E82a5616a", "Ef41e17fa", "Efcc804f6", "Eddae5477", "Ea7e94b12",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_11", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    # run_app.sh does pm clear and the setup step before this script.
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E29472d10 -- LIFECYCLE: Activity lifecycle callback (onResume).
    # No user action; the launch above drives it.
    r.comment("lifecycle onResume, no user action", "E29472d10")

    # E80427a98 -- ENTERS S_LIBRARY: LibraryActivity resumed and shown
    # (default tab Artists). Wait for library content, then the setup
    # the route needs: create playlist Route11 holding one song, so
    # the Playlists tab has a playlist and the open playlist has a
    # song. A fresh install has no playlist, so this always creates.
    r.wait_for("E80427a98", text="Tracks")
    r.tap("E80427a98", text="Tracks")
    r.wait_for("E80427a98", text="Morning Light")
    r.long_tap("E80427a98", text="Morning Light")
    r.tap("E80427a98", text="Add to playlist…")
    r.tap("E80427a98", text="New playlist…")
    r.type_text("Route11", "E80427a98")
    r.tap("E80427a98", text="Create")
    r.tap("E80427a98", text="Playlists")

    # Ebe48c047 -- GUI: tap the arrow at the right end of an
    # expandable row (the playlist row's dragger/expander).
    r.tap("Ebe48c047", res_id="dragger")

    # E47e1fc64 -- CALL: mActivity.onItemExpanded(createData(parent))
    # for the arrow of a playlist row. Guard (Playlists tab visible, a
    # playlist exists) is satisfied by the setup above; dispatch only.
    r.comment("onItemExpanded dispatch, guard satisfied by setup",
              "E47e1fc64")

    # E4b9b8513 -- CALL: type == TYPE_PLAYLIST: editPlaylist(rowData).
    # No user action; the type guard is satisfied by the playlist row.
    r.comment("TYPE_PLAYLIST dispatch to editPlaylist, no user action",
              "E4b9b8513")

    # Ec2a699b7 -- INTENT: startActivity(PlaylistActivity) with the
    # playlist id and title. Fired by editPlaylist; no user action.
    r.comment("startActivity fired by editPlaylist, no user action",
              "Ec2a699b7")

    # Ea3fb04b3 -- LIFECYCLE: Activity lifecycle callback (onCreate).
    # No user action; the intent above drives it.
    r.comment("lifecycle onCreate, no user action", "Ea3fb04b3")

    # E1e5cc37a -- ENTERS S_PLAYLIST: the playlist songs are shown.
    r.wait_for("E1e5cc37a", res_id="list")

    # E5e427574 -- GUI: long-press a song row (the playlist has a song:
    # Morning Light, added by the setup above).
    r.wait_for("E5e427574", text="Morning Light")
    r.long_tap("E5e427574", text="Morning Light")

    # E82a5616a -- CALL: mCallback.onItemLongClickWithCoords(...) with
    # the callback of this list (PlaylistActivity.onCreate:113).
    # Dispatch only; no user action.
    r.comment("onItemLongClickWithCoords dispatch, no user action",
              "E82a5616a")

    # Ef41e17fa -- CALL: fm.show(view, x, y): the bottom sheet of the
    # playlist activity opens. Consequence of the long-press above.
    r.comment("FancyMenu.show consequence of long-press, no user action",
              "Ef41e17fa")

    # Efcc804f6 -- ENTERS S_FANCY_PLAYLIST: the BottomSheetDialog with
    # the menu rows is shown.
    r.wait_for("Efcc804f6", text="Play")

    # Eddae5477 -- GUI: tap a row of the context menu (Play, the first
    # menu row PlaylistActivity builds for a playlist song).
    r.tap("Eddae5477", text="Play")

    # Ea7e94b12 -- CALL: mCallback.onFancyItemSelected(item) with the
    # callback of this menu (PlaylistActivity: new FancyMenu(this,
    # this)). Dispatch from the menu tap; this is the target method.
    r.comment("onFancyItemSelected dispatch from menu tap, target",
              "Ea7e94b12")
    r.screenshot("route_11_done", "Ea7e94b12")
    r.dump_ui("route_11_done", "Ea7e94b12")

    r.done()


if __name__ == "__main__":
    main()
