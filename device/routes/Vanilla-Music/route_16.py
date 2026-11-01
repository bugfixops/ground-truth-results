"""Vanilla-Music route_16: TrackDetailsDialog$1$1.<init>.

Edge ids (ROUTES.csv, in order):
  E47380ade E29472d10 E80427a98 E4815c188 E6b53f69a E9d3f1968 E10f89d6b
  E84362eba Ee8712a3d E5ea28138 E3a5963e5 Edc7ee82f Edece7acc

Printed route source:
  verification.csv path row (TrackDetailsDialog$1$1.<init>): "Steps read:
  long-press a Songs-tab row (STATE: Songs tab visible, a song row
  shown; ENV permission for the scan to have populated it) ->
  onFancyItemSelected@SHOW_DETAILS (guard: type == TYPE_SONG) ->
  TrackDetailsDialog.onCreateView -> handler.post(new Runnable(){...})
  (TrackDetailsDialog$1.run) -> getActivity().runOnUiThread(new
  Runnable(){...}) -> TrackDetailsDialog$1$1.<init>."
  ROUTES.csv row: source "LibraryActivity.java:743-845;
  TrackDetailsDialog.java:75-117,89-114,99", env permission,
  state data;session.
Permissions (ROUTES.csv): android.permission.READ_EXTERNAL_STORAGE,
  android.permission.WRITE_EXTERNAL_STORAGE (granted here before launch;
  run_app.sh also grants the ROUTES.csv set during setup).
Fixtures: none (STATE file gates: none).
Setup (run_app.sh, before this script): push fixtures/Music + media scan.

UI labels used, all read from layout XML / strings.xml, never invented:
  - Songs tab label is "Tracks" (res/values/translatable.xml:
    <string name="songs">Tracks</string>; LibraryPagerAdapter TITLES
    maps TYPE_SONG to R.string.songs).
  - Song row "Morning Light": fixture 01 Morning Light.mp3, ID3 title
    "Morning Light" (verified with ffprobe on the setup fixtures).
  - Fancy-menu row "Details" (translatable.xml: <string
    name="details">Details</string>; LibraryActivity.java:715 adds
    CTX_MENU_SHOW_DETAILS with R.string.details for TYPE_SONG rows).
  - A header ("Play all") row is NOT long-pressed: its DATA_ID is
    HEADER_ID (-1), so TrackDetailsDialog would get songId -1, the
    song lookup would return null, and the runOnUiThread runnable
    (the target's enclosing runnable) would never be created. Only a
    real song row reaches the target.

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
    "E47380ade", "E29472d10", "E80427a98", "E4815c188", "E6b53f69a",
    "E9d3f1968", "E10f89d6b", "E84362eba", "Ee8712a3d", "E5ea28138",
    "E3a5963e5", "Edc7ee82f", "Edece7acc",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    r = Runner(package=args.package, route="route_16", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- ENTRY: MAIN / LAUNCHER intent starts LibraryActivity.
    # Storage is granted first so the setup scan has populated the
    # library (ENV permission gate on E5ea28138); run_app.sh runs
    # pm clear + setup before this script, so granting here is
    # idempotent with the setup grants.
    r.grant("android.permission.READ_EXTERNAL_STORAGE", "E47380ade")
    r.grant("android.permission.WRITE_EXTERNAL_STORAGE", "E47380ade")
    r.launch(PACKAGE_ACTIVITY, "E47380ade")

    # E29472d10 -- LIFECYCLE: Activity lifecycle callback (onResume).
    # No user action; the launch above drives it.
    r.comment("lifecycle onResume, no user action", "E29472d10")

    # E80427a98 -- ENTERS S_LIBRARY: LibraryActivity resumed and shown.
    # Select the Songs tab (label "Tracks") so a song row is shown.
    r.wait_for("E80427a98", text="Tracks")
    r.tap("E80427a98", text="Tracks")

    # E4815c188 -- GUI: long-press a row of the list (a real song row,
    # not the play-all header row; see the header note above).
    r.wait_for("E4815c188", text="Morning Light")
    r.long_tap("E4815c188", text="Morning Light")

    # E6b53f69a -- CALL: mCallback.onItemLongClickWithCoords(...).
    # Framework dispatch from the long-press; no separate user action.
    r.comment("dispatch to LibraryPagerAdapter, no user action", "E6b53f69a")

    # E9d3f1968 -- CALL: mActivity.onCreateFancyMenu(intent, view, x, y)
    # for a media-tab row (guard: type != TYPE_FILE; a song row passes).
    r.comment("dispatch to onCreateFancyMenu, no user action", "E9d3f1968")

    # E10f89d6b -- CALL: fm.show(view, x, y), the library bottom sheet.
    r.comment("fancy menu shown by the long-press, no user action",
              "E10f89d6b")

    # E84362eba -- ENTERS S_FANCY_LIBRARY: the BottomSheetDialog with
    # the menu rows is shown.
    r.wait_for("E84362eba", text="Details")

    # Ee8712a3d -- GUI: tap a row of the context menu.
    r.tap("Ee8712a3d", text="Details")

    # E5ea28138 -- CALL: item SHOW_DETAILS tapped (guard: type ==
    # TYPE_SONG; storage granted, so the library is populated).
    r.comment("SHOW_DETAILS dispatch from the Details tap, no user action",
              "E5ea28138")

    # E3a5963e5 -- FRAMEWORK: the fragment builds its view (the dialog
    # window shows it). The dialog title is the song title, proving
    # the dialog opened for the long-pressed song.
    r.assert_text("Morning Light", "E3a5963e5")

    # Edc7ee82f -- ASYNC: handler.post(new Runnable(){...}) on the
    # dialog's HandlerThread (TrackDetailsDialog$1.run).
    r.comment("handler.post runnable, no user action", "Edc7ee82f")

    # Edece7acc -- CALL: getActivity().runOnUiThread(new Runnable()
    # {...}) -> TrackDetailsDialog$1$1.<init> (the target). The dialog
    # rendering below is the evidence that the runnable chain ran.
    r.screenshot("route_16_details_dialog", "Edece7acc")
    r.dump_ui("route_16_details_dialog", "Edece7acc")

    r.done()


if __name__ == "__main__":
    main()
