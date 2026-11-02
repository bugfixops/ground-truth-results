#!/usr/bin/env python3
"""AnkiDroid route_20: libanki.Utils.base62.

Target: libanki.Utils.base62.
Table verdict: WRONG (final-draw verdict; this script drives the
    CORRECTED route, never the printed BFS route). The printed route
    reached guid64 from the CHECK_MEDIA prefix, where the Note id is
    an existing note id and the constructor takes the load() branch;
    this script reaches guid64 from NoteEditor new-note creation,
    per helper/judge-final/judge-11-20/JUDGEMENTS.md route 20.
Route followed: corrected route, 18 edges: deck picker -> drawer
    CardBrowser -> Add note -> NoteEditor lifecycle -> setNote ->
    Note constructors (id null) -> guid64 -> base91 -> base62.
Preconditions: collection open; collection.anki2 exists; a current
    model exists; the editor is opened for ADDING a note (note is
    null). No field text is needed: guid64 runs in the constructor
    before any editing.
Mapping notes:
  - Reuses the old first-draw route_22 script's drive (drawer Card
    browser -> Add note -> new-note construction) but FIXES its
    chain gap: the old script carried the page edge E37ba8c1f and
    then jumped to onCollectionLoaded with no connecting edge
    (flagged unresolved there). This script carries the INTENT edge
    E83452f16 plus the lifecycle edges, so the chain is contiguous
    end to end; see NOTES.md.
  - "Navigate up" and "More options" are the standard
    framework/AppCompat descriptions; verify them against a live
    uiautomator dump before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
Draft status: final-draw device draft for the merger; dry/static
    checks only. No live run has been performed with this script, and
    nothing in this file claims one.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ed1dad133",
    "E0e89f361", "Eb06cba16", "E352d419a", "E0281e707", "E83452f16",
    "E1fcbaff3", "Ef51ca70b", "E34bd403a", "Ef9f80682", "E80e8ad56",
    "E62a24da3", "Ed4aa2957", "E4a0aec25",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_20")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_20", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate: launch MAIN/LAUNCHER.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init> (else branch).
    r.comment("IntentHandler else branch starts DeckPicker",
              edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER (collection file
    # exists, WRITE_EXTERNAL_STORAGE granted).
    r.comment("deck-picker page shown", edge="Eb3058057")
    # Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser: open the
    # drawer, then tap the nav_browser item. String verified in
    # res: card_browser = "Card browser".
    r.tap(edge="Ed1dad133", desc="Navigate up")
    r.tap(edge="Ed1dad133", text="Card browser")
    # E0e89f361 openCardBrowser -> CardBrowser.<init>.
    r.comment("startActivityForResult CardBrowser", edge="E0e89f361")
    # Eb06cba16 CardBrowser.<init> -> onCreate.
    r.comment("CardBrowser onCreate", edge="Eb06cba16")
    # E352d419a -> S_CARDBROWSER.
    r.comment("card browser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> onOptionsItemSelected: open the
    # options menu (standard AppCompat overflow description).
    r.tap(edge="E0281e707", desc="More options")
    # E83452f16 onOptionsItemSelected -> NoteEditor.<init> (INTENT
    # edge for the action_add_card_from_card_browser item,
    # CardBrowser.java:628-633). The same tap was logged under the
    # page edge E37ba8c1f by the old route_22 script; this script
    # carries the INTENT edge instead, because it is the edge that
    # keeps the chain contiguous into NoteEditor lifecycle. String
    # verified in res: card_editor_add_card = "Add note".
    r.tap(edge="E83452f16", text="Add note")
    # E1fcbaff3 NoteEditor.<init> -> onCreate.
    r.comment("NoteEditor onCreate", edge="E1fcbaff3")
    # Ef51ca70b onCreate -> onCollectionLoaded.
    r.comment("NoteEditor collection loaded", edge="Ef51ca70b")
    # E34bd403a onCollectionLoaded -> setNote(Note): ADDING a note,
    # so setNote builds a new Note with the current model
    # (NoteEditor.java:1366-1370). The null argument is a runtime
    # value, not a graph node distinction: the live run must be
    # in add-note mode (CALLER_CARDBROWSER_ADD, no existing note
    # id), never in edit mode, or the id != null branch runs and
    # guid64 is never reached.
    r.comment("new note construction started (add-note mode)",
              edge="E34bd403a")
    # Ef9f80682 setNote(Note) -> Note.<init>(Collection,JSONObject).
    r.comment("two-arg Note constructor", edge="Ef9f80682")
    # E80e8ad56 Note.<init>(Collection,JSONObject) ->
    # Note.<init>(Collection,JSONObject,Long) with id null
    # (Note.java:58-60).
    r.comment("three-arg Note constructor, id null", edge="E80e8ad56")
    # E62a24da3 Note.<init>(Collection,JSONObject,Long) ->
    # libanki.Utils.guid64: the id == null else branch runs
    # (Note.java:66-72). This edge id is the same id the printed
    # BFS route used at step 19, but the drive puts it in the
    # correct new-note branch; the id alone does not distinguish
    # branches.
    r.comment("guid64 generated (new-note branch)", edge="E62a24da3")
    # Ed4aa2957 guid64 -> base91 (Utils.java:426-427).
    r.comment("base91 encoding", edge="Ed4aa2957")
    # E4a0aec25 base91 -> base62 (target; Utils.java:420-421).
    r.comment("base62 encoding reached (target)", edge="E4a0aec25")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
