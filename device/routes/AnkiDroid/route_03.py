#!/usr/bin/env python3
"""AnkiDroid route_03: StepsPreference.updateSettings.

Target: StepsPreference.updateSettings (called by the
    (Context, AttributeSet) constructor during DeckOptions inflation).
Table verdict: WRONG (first-draw verdict; this script drives the
    CORRECTED route C03, never the printed BFS route).
Route followed: CORRECTED route C03 from
    helper/b6fix-r01-06/CORRECTED_ROUTES.md, with final-graph edge
    ids (23 edges). The printed route took the LOAD_DECK_COUNTS task
    but the undo listener; this script uses the UNDO task and its own
    listener throughout, so task type, listener, and guard match.
Preconditions/fixtures:
  - Collection open; deck "Default" with at least one due card, and
    the deck already selected. Selecting a new deck clears undo
    history (DeckPicker.java:1719-1720), so the preamble reviews a
    card in the already-selected deck.
  - The preamble (review one card) establishes the undo state the
    route needs: after grading, the undo name is the review string,
    so DeckPicker$13.onPostExecute takes the isReview branch to
    openReviewer. Preamble taps are logged under the first UI edge
    Ec0803f80 with PREAMBLE comments; they are not that edge's own
    action, but no graph edge exists for the review taps.
Mapping notes:
  - The Undo menu item title is dynamic: "Undo %s" with the undo
    name (DeckPicker.java:516-517). After a review it reads
    "Undo last review" (undo_action_review = "last review").
  - The Reviewer options-menu item for deck options is titled
    "Deck options" (study_options string, reviewer.xml).
  - The "More options" content description is the standard AppCompat
    overflow description; verify it against a live uiautomator dump
    before a real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Eee750606", "Eb4c40f11", "E460971ee", "E3e610385", "Eee369b5f",
    "E69bc1fda", "E6d576f07", "E251b66e4", "E8fb9dd46", "E63fbdec5",
    "Ee2fb37d3", "Ea375fff8", "E875f2b99", "Ec1df4e42", "E1997e0e7",
    "E49c1f965", "E61f57fc4", "E5b96f052",
]

FIXTURE_DECK = "Default"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
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
    # PREAMBLE (logged under Ec0803f80): review one card so that an
    # undo of a review exists. Tapping a due deck on a
    # non-fragmented layout jumps straight to the Reviewer.
    r.tap(edge="Ec0803f80", text=FIXTURE_DECK)
    r.wait_for(edge="Ec0803f80", text="Show answer")
    r.tap(edge="Ec0803f80", text="Show answer")
    r.tap(edge="Ec0803f80", text="Good")
    # Back returns from the Reviewer to the deck picker.
    r.back(edge="Ec0803f80")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu (drawer toggle must not consume it).
    r.tap(edge="Ec0803f80", desc="More options")
    # Eee750606 onOptionsItemSelected -> DeckPicker.undo: tap Undo.
    r.tap(edge="Eee750606", text="Undo last review")
    # Eb4c40f11 undo -> launchDeckTask (TASK_TYPE_UNDO, $13 listener).
    r.comment("launchDeckTask TASK_TYPE_UNDO", edge="Eb4c40f11")
    # E460971ee launchDeckTask -> doInBackground (UNDO case).
    r.comment("doInBackground takes UNDO case", edge="E460971ee")
    # E3e610385 doInBackground -> onPostExecute (framework delivery).
    r.dwell(edge="E3e610385", seconds=5)
    # Eee369b5f onPostExecute -> TaskListener.onPostExecute.
    r.comment("listener onPostExecute", edge="Eee369b5f")
    # E69bc1fda TaskListener -> DeckPicker$13.onPostExecute: this is
    # the undo listener registered by undo() itself, not the
    # updateDeckList listener.
    r.comment("undo listener $13 onPostExecute", edge="E69bc1fda")
    # E6d576f07 $13.onPostExecute -> openReviewer (guard: isReview,
    # satisfied because the preamble graded a card).
    r.comment("isReview branch opens Reviewer", edge="E6d576f07")
    # E251b66e4 openReviewer -> Reviewer.<init>.
    r.comment("startActivityForResult Reviewer", edge="E251b66e4")
    # E8fb9dd46 Reviewer.<init> -> AbstractFlashcardViewer.<init>.
    r.comment("Reviewer extends AbstractFlashcardViewer",
              edge="E8fb9dd46")
    # E63fbdec5 AFV.<init> -> AFV.onCreate.
    r.comment("AbstractFlashcardViewer onCreate", edge="E63fbdec5")
    # Ee2fb37d3 AFV.onCreate -> Reviewer.onCollectionLoaded
    # (guard: col != null and colIsOpen()).
    r.comment("collection loaded, Reviewer onCollectionLoaded",
              edge="Ee2fb37d3")
    # Ea375fff8 Reviewer.onCollectionLoaded -> S_REVIEWER.
    r.comment("reviewer page shown", edge="Ea375fff8")
    # E875f2b99 S_REVIEWER -> Reviewer.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="E875f2b99", desc="More options")
    # Ec1df4e42 onOptionsItemSelected -> DeckOptions.<init>
    # (action_open_deck_options).
    r.tap(edge="Ec1df4e42", text="Deck options")
    # E1997e0e7 DeckOptions.<init> -> DeckOptions.onCreate.
    r.comment("DeckOptions onCreate", edge="E1997e0e7")
    # E49c1f965 DeckOptions.onCreate -> S_DECKOPTIONS (collection
    # loaded, so addPreferencesFromResource is reached).
    r.comment("deck options page shown", edge="E49c1f965")
    # E61f57fc4 S_DECKOPTIONS -> StepsPreference.<init>: inflation
    # of deck_options.xml constructs StepsPreference for the
    # newSteps/lapSteps entries.
    r.comment("inflation constructs StepsPreference", edge="E61f57fc4")
    # E5b96f052 StepsPreference.<init> -> updateSettings (target;
    # constructor calls updateSettings at StepsPreference.java:47).
    r.comment("constructor calls updateSettings (target)",
              edge="E5b96f052")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
