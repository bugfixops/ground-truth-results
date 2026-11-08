#!/usr/bin/env python3
"""Vanilla-Music route_09: MediaLibrary.renamePlaylist.

Method: MediaLibrary.renamePlaylist
Edge ids (in order, from ROUTES.csv):
    E47380ade E29472d10 E80427a98 E4815c188 E6b53f69a E9d3f1968
    E10f89d6b E84362eba Ee8712a3d Efd230069 E4a79d1ad E4fb95163
    Ec64b1a2b E39dbfa6f E7d715c39 E3b256a9a Eb2fb11a8 E50cb1f9a
Printed route source:
    verification.csv path row (MediaLibrary.renamePlaylist, SOURCE):
      ref: LibraryPagerAdapter.java:341-343;
        CoordClickListener.java:60-62,79;
        LibraryPagerAdapter.java:890; LibraryActivity.java:725,
        743-845,827-837; FancyMenu.java:169-190,173-185,178,72-76;
        PlaylistDialog.java:146-172; PlaylistInputDialog.java:93-98,
        143-156,150; LibraryActivity.java:771-777,773-776;
        PlaybackActivity.java:495; Playlist.java:194
      Steps read: long-press the play-all header ->
        onCreateFancyMenu -> FancyMenu.show -> S_FANCY_LIBRARY ->
        tap "Add to playlist" (always present) -> S_DLG_PLAYLIST ->
        tap an entry -> "New playlist..." branch (guard: which ==
        BUTTON_CREATE_PLAYLIST) -> PlaylistInputDialog -> onClick ->
        LibraryActivity$2.onSuccess (STATE: the rename dialog of a
        playlist row is open - the same dialog class is reused for
        rename, with the matching callback guard) ->
        handleMessage(MSG_RENAME_PLAYLIST) -> Playlist.renamePlaylist
        -> MediaLibrary.renamePlaylist.
    ROUTES.csv row: state_kinds=session, permissions=(none),
      fixtures=(none), setup="push fixtures/Music + media scan",
      status=scripted.
Permissions: none (ROUTES.csv lists none).
Fixtures: none (STATE file gates: none; the playlist is created
    through the app itself from the setup-scanned library).
Setup (run by run_app.sh before this script): pm clear, then push
    fixtures/Music + media scan.
Two-phase structure (read this before replaying): the route's
    middle edges (Efd230069, E4a79d1ad, E4fb95163, Ec64b1a2b)
    describe the playlist-chooser / create dialog, while the
    callback edge E7d715c39 names the RENAME dialog's callback
    (LibraryActivity$2, the callback given by LibraryActivity for
    the rename branch, LibraryActivity.java:768-777) with the guard
    "the rename dialog of a playlist is open". The create flow
    alone cannot fire that callback: PlaylistDialog's create branch
    uses its own callback, not LibraryActivity$2. Only the rename
    flow (long-press a playlist row -> Rename -> confirm) reaches
    MSG_RENAME_PLAYLIST -> Playlist.renamePlaylist ->
    MediaLibrary.renamePlaylist. So this script runs both phases,
    each in route order:
      Phase A (precondition + the route's middle edges): long-press
        a Tracks-tab row -> Add to playlist -> New playlist... ->
        type "Route09Playlist" -> Create. This creates the playlist
        the rename phase needs, and traverses Efd230069, E4a79d1ad,
        E4fb95163, Ec64b1a2b for real.
      Phase B (the rename traversal): Playlists tab -> long-press
        the "Route09Playlist" row -> Rename -> confirm with a new
        name. It re-traverses the shared early edges (long-press,
        fancy menu) and then E39dbfa6f, E7d715c39, E3b256a9a,
        Eb2fb11a8, E50cb1f9a. The middle edges get comment-only
        blocks in Phase B stating they were traversed in Phase A
        and have no separate rename-phase action.
    The harness checks edge membership, not monotonic order, so the
    log contains only this route's edge ids; the phase comments
    make the repetition explicit rather than silent.
Rename typing note: PlaylistInputDialog pre-fills its EditText
    with the current playlist name and enables the positive button
    only when the text differs (PlaylistInputDialog.java: onStart,
    onTextChanged). The EditText is created programmatically with
    no res_id, and the dialog requests focus for it, so type_text
    types into it with no tap needed. Cursor placement after
    setText is not guaranteed, so Phase B first sends 16 DEL
    keyevents (one more than the 15 characters of
    "Route09Playlist") and then types "Route09Renamed": whether
    the cursor started at the end (field cleared, then the new
    name) or at the start (DELs are no-ops, new name prepended),
    the result differs from the initial text, does not collide
    with an existing playlist, and the positive button still
    reads "Rename". Fresh-install assumption (run_app.sh does pm
    clear per route): no pre-existing "Route09Playlist", so the
    create button reads "Create", not "Overwrite".
Harness notes: launch() takes (component, edge); every other call
    below passes edge= explicitly. Fancy-menu row texts come from
    strings.xml: "Add to playlist…" is R.string.add_to_playlist,
    "New playlist…" is R.string.new_playlist, "Rename" is
    R.string.rename, "Create" is R.string.create, and the input
    dialog title is R.string.choose_playlist_name ("Choose
    playlist name"). The ellipsis in the first two is the single
    character U+2026 as stored in strings.xml.
"""

import argparse
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT = _SCRIPT_DIR
for _ in range(3):
    _ROOT = os.path.dirname(_ROOT)
# Insert only a root that really contains device/harness: inserting a
# wrong root first would cache a namespace "device" package and break
# the fallback import below.
_CANDIDATES = []
if os.path.isfile(os.path.join(_ROOT, "device", "harness", "harness.py")):
    _CANDIDATES.append(_ROOT)
else:
    # Helper-dir copies (e.g. work/Vanilla-Music/helper/...) are not
    # under device/routes/, so the four-dirname root above is not a
    # repo root there. Fall back to a stage checkout found under an
    # ancestor (device/stage/device/harness). In the merged layout
    # (device/routes/Vanilla-Music/route_NN.py) the primary root
    # contains device/harness and this branch never runs.
    _dir = _SCRIPT_DIR
    while True:
        _cand = os.path.join(_dir, "device", "stage")
        if os.path.isfile(os.path.join(_cand, "device", "harness",
                                       "harness.py")):
            _CANDIDATES.append(_cand)
            break
        _parent = os.path.dirname(_dir)
        if _parent == _dir:
            break
        _dir = _parent
for _c in _CANDIDATES:
    sys.path.insert(0, _c)
from device.harness.harness import Runner

EDGE_IDS = [
    "E47380ade", "E29472d10", "E80427a98", "E4815c188", "E6b53f69a",
    "E9d3f1968", "E10f89d6b", "E84362eba", "Ee8712a3d", "Efd230069",
    "E4a79d1ad", "E4fb95163", "Ec64b1a2b", "E39dbfa6f", "E7d715c39",
    "E3b256a9a", "Eb2fb11a8", "E50cb1f9a",
]

CREATE_NAME = "Route09Playlist"
RENAME_NAME = "Route09Renamed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    r = Runner(package=args.package, route="route_09", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch("%s/.LibraryActivity" % args.package, edge="E47380ade")
    # E29472d10 -- Activity lifecycle callback (no user action).
    r.comment("LibraryActivity onResume (lifecycle)", edge="E29472d10")
    # E80427a98 -- LibraryActivity is resumed and shown (default tab
    # Artists: library_page = 0). Wait for the library pager.
    r.wait_for(edge="E80427a98", res_id="pager", timeout=30)
    # ---- Phase A: create the playlist (precondition + middle edges)
    # E4815c188 -- Long-press the play-all header row or a row of
    # the list. Precondition navigation first: open the Tracks tab
    # (R.string.songs = "Tracks") so the long-pressed row is a song
    # row, then long-press the first list row title (draggable_row
    # TextView res_id "text").
    r.tap(edge="E4815c188", text="Tracks")
    r.wait_for(edge="E4815c188", res_id="text", timeout=30)
    r.long_tap(edge="E4815c188", res_id="text")
    # E6b53f69a -- mCallback.onItemLongClickWithCoords(...) with the
    # callback of this list (internal; no user action).
    r.comment("onItemLongClickWithCoords (internal)", edge="E6b53f69a")
    # E9d3f1968 -- mActivity.onCreateFancyMenu(intent, view, x, y)
    # for a row of a media tab or the play-all header. Guard
    # type != TYPE_FILE holds for a song row (internal).
    r.comment("onCreateFancyMenu (internal)", edge="E9d3f1968")
    # E10f89d6b -- fm.show(view, x, y): the bottom sheet of the
    # library opens (internal show call; the visible result is the
    # next edge).
    r.comment("FancyMenu.show (internal)", edge="E10f89d6b")
    # E84362eba -- the BottomSheetDialog with the menu rows is
    # shown. The "Add to playlist..." row proves the menu is open.
    r.wait_for(edge="E84362eba", text="Add to playlist\u2026",
               timeout=30)
    # Ee8712a3d -- Tap a row of the context menu.
    r.tap(edge="Ee8712a3d", text="Add to playlist\u2026")
    # Efd230069 -- item ADD_TO_PLAYLIST of the context menu was
    # tapped. Guard: item "Add to playlist": always present (also
    # on the header row). Taken by the tap above.
    r.comment("ADD_TO_PLAYLIST branch taken", edge="Efd230069")
    # E4a79d1ad -- the playlist chooser dialog is shown. Its title
    # is R.string.add_to_playlist ("Add to playlist...").
    r.wait_for(edge="E4a79d1ad", text="Add to playlist\u2026",
               timeout=30)
    # E4fb95163 -- Tap an entry of the list ("New playlist..." or
    # an existing playlist). Fresh install: only "New playlist..."
    # exists.
    r.tap(edge="E4fb95163", text="New playlist\u2026")
    # Ec64b1a2b -- the new-playlist name dialog is shown. Guard
    # which == BUTTON_CREATE_PLAYLIST holds (first list entry).
    # Title is R.string.choose_playlist_name.
    r.wait_for(edge="Ec64b1a2b", text="Choose playlist name",
               timeout=30)
    # E39dbfa6f -- Tap "Create" (or "Overwrite") in the dialog, or
    # Cancel. The dialog's EditText is focused on open (no tap
    # needed to type); type the new playlist name, then tap the
    # positive button "Create".
    r.type_text(CREATE_NAME, edge="E39dbfa6f")
    r.tap(edge="E39dbfa6f", text="Create")
    # ---- Phase B: rename the playlist just created
    # E4815c188 -- Long-press a row of the list (here: the playlist
    # row). Precondition navigation first: open the Playlists tab
    # and wait for the row created in Phase A.
    r.tap(edge="E4815c188", text="Playlists")
    r.wait_for(edge="E4815c188", text=CREATE_NAME, timeout=30)
    r.long_tap(edge="E4815c188", text=CREATE_NAME)
    # E6b53f69a -- mCallback.onItemLongClickWithCoords(...) (internal).
    r.comment("onItemLongClickWithCoords (internal)", edge="E6b53f69a")
    # E9d3f1968 -- mActivity.onCreateFancyMenu for a playlist row.
    # Guard type != TYPE_FILE holds for a playlist row (internal).
    r.comment("onCreateFancyMenu for playlist row (internal)",
              edge="E9d3f1968")
    # E10f89d6b -- fm.show(view, x, y) (internal show call).
    r.comment("FancyMenu.show (internal)", edge="E10f89d6b")
    # E84362eba -- the BottomSheetDialog with the menu rows is
    # shown. The "Rename" row (added only for TYPE_PLAYLIST rows,
    # LibraryActivity.java:703-705) proves the menu is open.
    r.wait_for(edge="E84362eba", text="Rename", timeout=30)
    # Ee8712a3d -- Tap a row of the context menu: "Rename".
    r.tap(edge="Ee8712a3d", text="Rename")
    # Efd230069 -- Phase B has no ADD_TO_PLAYLIST tap: this edge
    # was traversed for real in Phase A (see docstring). Comment
    # only, so the block order stays complete.
    r.comment("ADD_TO_PLAYLIST traversed in Phase A, not in rename "
              "phase", edge="Efd230069")
    # E4a79d1ad -- Phase B shows no playlist-chooser dialog: this
    # edge was traversed for real in Phase A. Comment only.
    r.comment("playlist chooser traversed in Phase A, not in rename "
              "phase", edge="E4a79d1ad")
    # E4fb95163 -- Phase B taps no chooser entry: this edge was
    # traversed for real in Phase A. Comment only.
    r.comment("chooser entry tapped in Phase A, not in rename phase",
              edge="E4fb95163")
    # Ec64b1a2b -- the rename input dialog is shown: the same
    # PlaylistInputDialog class as Phase A, this time the rename
    # instance (initial text = playlist name, positive button
    # "Rename"). Title is R.string.choose_playlist_name.
    r.wait_for(edge="Ec64b1a2b", text="Choose playlist name",
               timeout=30)
    # E39dbfa6f -- Tap the positive button in the dialog. Clear
    # any pre-filled text first (cursor placement after setText is
    # not guaranteed: 16 DELs cover the 15-character name either
    # way), type the new name, then tap "Rename".
    for _ in range(len(CREATE_NAME) + 1):
        r.key("DEL", edge="E39dbfa6f")
    r.type_text(RENAME_NAME, edge="E39dbfa6f")
    r.tap(edge="E39dbfa6f", text="Rename")
    # E7d715c39 -- mCallback.onSuccess(text) for the rename dialog
    # of the library. Guard: positive button and the callback is
    # the one given by LibraryActivity (rename). Fired by the
    # confirm tap above (internal; no further user action).
    r.comment("LibraryActivity rename callback onSuccess (internal)",
              edge="E7d715c39")
    # E3b256a9a -- the branch of LibraryActivity that handles
    # MSG_RENAME_PLAYLIST runs (async; no user action).
    r.comment("MSG_RENAME_PLAYLIST handled (async)", edge="E3b256a9a")
    # Eb2fb11a8 -- call made in the message branch.
    r.comment("Playlist.renamePlaylist called", edge="Eb2fb11a8")
    # E50cb1f9a -- Direct call to MediaLibrary.renamePlaylist
    # (target).
    r.comment("MediaLibrary.renamePlaylist called (target)",
              edge="E50cb1f9a")
    r.screenshot("route_09_end", edge="E50cb1f9a")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
