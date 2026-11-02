#!/usr/bin/env python3
"""AnkiDroid route_07 (final draw): MediaCheckDialog$3.<init>.

Target: MediaCheckDialog$3.<init> (the RESULTS-dialog OK callback
    for the unused-empty branch; MediaCheckDialog.java:132-139).
    $3.<init> runs at dialog creation when onCreateDialog takes
    the RESULTS branch with unused empty, before any button tap,
    so the script performs no tap after the media check finishes.
Table verdict: CORRECT (combined-merge redraw, row 07,
    16 steps on the sync-error print; device drive KEPT as the
    14-edge menu chain below). The new-sample row 07 print is
    the 16-edge sync-error drive (launch with sync-on-resume ->
    sync-null -> $17.onPostExecute -> showSyncErrorDialog ->
    S_DLG_SYNC_ERROR_MEDIA -> mediaCheck -> ... -> $3.<init>);
    its condition is media-sync-server-error + check success +
    logged-in hkey + online. THIS device row keeps the MENU
    drive (options menu -> Check media -> OK on the confirm
    dialog -> wait for the media check -> RESULTS dialog),
    whose whole 14-edge chain still exists contiguously in the
    new JSON. The live run must confirm the MENU drive, not the
    sync drive (see NOTES_NEW.md, OPEN). No account, no sync,
    and no server result are needed for the menu drive.
Route followed: the 14-edge menu chain verified contiguous
    against graphs/AnkiDroid/out/ankidroid_trigger_graph.json
    (first src S_ENTRY, each dst equals the next src, last dst
    MediaCheckDialog$3.<init>). Steps 1-5 are the shared
    collection-open head (identical ids to the BFS head through
    S_DECKPICKER); steps 6-14 are the menu entry plus the tail
    identical to the printed route's steps 11-16:
    DeckPicker options menu case R.id.action_check_media
    (DeckPicker.java:600-602) -> showMediaCheckDialog(
    DIALOG_CONFIRM_MEDIA_CHECK) -> confirm-dialog OK ->
    MediaCheckDialog$1.onPositive -> DeckPicker.mediaCheck
    (MediaCheckDialog.java:70) -> $16.onPostExecute ->
    showMediaCheckDialog(int, List) (DeckPicker.java:1207,
    success branch result.getBoolean()) -> newInstance(int, List)
    -> <init> -> onCreateDialog -> $3.<init>.
    This chain is a REWRITE, not a reuse: the old first-draw
    route_07.py targeted a different method (libanki.Utils$1)
    with an 18-edge HINT/SELECT chain, and the delivered dev-01-10
    route 07 row was unscriptable (no script). No old script's
    chain or drive is carried over.
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open; WRITE_EXTERNAL_STORAGE granted;
    collection.anki2 exists in the AnkiDroid folder.
  - SD card mounted, so the Check media menu item is enabled
    (DeckPicker.java:529).
  - Media check succeeds (DeckPicker.java:1207 success branch).
  - Check result has ZERO unused files, so the RESULTS dialog
    takes the else branch (MediaCheckDialog.java:132). This is a
    collection-state precondition (clean media directory / all
    media referenced), not a server result.
Mapping notes:
  - Selectors verified against the printed tree: "Check media"
    (menu item action_check_media in res/menu/deck_picker.xml,
    title @string/check_media, res/values/02-strings.xml:131
    "Check media"); "OK" for the confirm dialog's positive
    button (MediaCheckDialog.java:67-73 uses
    R.string.dialog_ok, res/values/03-dialogs.xml:81 "OK").
    The RESULTS dialog's own OK button is never tapped: $3 is
    its callback's constructor, which runs at dialog creation.
  - The "More options" content description is the standard
    AppCompat overflow description; verify it against a live
    uiautomator dump before a real run (see NOTES.md).
  - The final lifecycle step E72b1fcb3 (<init> ->
    onCreateDialog) is INFERRED: the graph evidence cites an
    inferred DialogFragment lifecycle and no framework source is
    in the tree. The script drives the real show call (the
    RESULTS dialog is shown by DeckPicker.showMediaCheckDialog);
    onCreateDialog is its direct framework consequence, and
    $3.<init> is constructed inside onCreateDialog at
    MediaCheckDialog.java:133 (graph evidence for Ed68ff3d0).
  - No live run is claimed by this script. The live run must
    confirm the items listed in NOTES.md (menu item visibility,
    confirm-dialog OK label rendering, zero-unused-files
    collection state, RESULTS dialog appearance, and the wait
    duration for the media check).
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "E1f73edbe", "E4c24ccb4", "Ef671cae6", "Ecf295e7b", "E4fb91c49",
    "E73517f6d", "Ef167e308", "E72b1fcb3", "Ed68ff3d0",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_07")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_07", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (collection file
    # exists, WRITE_EXTERNAL_STORAGE granted).
    r.comment("deck-picker page shown", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="More options")
    # E1f73edbe onOptionsItemSelected -> S_DLG_MEDIA_CHECK
    # (action_check_media, DeckPicker.java:600-603; menu item
    # enabled only when the SD card is mounted, :529).
    r.tap(edge="E1f73edbe", text="Check media")
    # E4c24ccb4 S_DLG_MEDIA_CHECK -> MediaCheckDialog$1.onPositive:
    # tap OK on the confirm dialog (MediaCheckDialog.java:67-73;
    # positive text is R.string.dialog_ok, "OK").
    r.tap(edge="E4c24ccb4", text="OK")
    # Ef671cae6 $1.onPositive -> DeckPicker.mediaCheck
    # (MediaCheckDialog.java:70).
    r.comment("confirm OK starts mediaCheck", edge="Ef671cae6")
    # Ecf295e7b DeckPicker.mediaCheck -> DeckPicker$16.onPostExecute:
    # wait for the background media check to finish.
    r.dwell(edge="Ecf295e7b", seconds=5)
    # E4fb91c49 $16.onPostExecute -> showMediaCheckDialog(int,List)
    # (DeckPicker.java:1207, success branch result.getBoolean()).
    r.comment("media check succeeded, RESULTS dialog shown",
              edge="E4fb91c49")
    # E73517f6d showMediaCheckDialog(int,List) ->
    # MediaCheckDialog.newInstance(int,List).
    r.comment("RESULTS dialog newInstance", edge="E73517f6d")
    # Ef167e308 newInstance(int,List) -> MediaCheckDialog.<init>.
    r.comment("RESULTS dialog instance created", edge="Ef167e308")
    # E72b1fcb3 <init> -> onCreateDialog (INFERRED DialogFragment
    # lifecycle step; the shown fragment's onCreateDialog at
    # MediaCheckDialog.java:56 is called by the framework once
    # shown, and takes the RESULTS branch).
    r.comment("RESULTS dialog onCreateDialog (INFERRED lifecycle)",
              edge="E72b1fcb3")
    # Ed68ff3d0 onCreateDialog -> MediaCheckDialog$3.<init>
    # (target; MediaCheckDialog.java:133, the else branch at :132
    # with unused empty: the OK-only RESULTS dialog's callback
    # constructor runs at dialog creation, before any button tap,
    # so no further tap is performed).
    r.comment("unused-empty branch constructs $3 (target; no tap "
              "needed, runs at dialog creation)", edge="Ed68ff3d0")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
