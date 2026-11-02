#!/usr/bin/env python3
"""AnkiDroid route_05: Sched.totalRevForCurrentDeck.

Target: Sched.totalRevForCurrentDeck (called from
    CustomStudyDialog.getText1 for CUSTOM_STUDY_REV).
Table verdict: WRONG (first-draw verdict; this script drives the
    CORRECTED route C05, never the printed BFS route).
Route followed: CORRECTED route C05 from
    helper/b6fix-r01-06/CORRECTED_ROUTES.md, with final-graph edge
    ids (23 edges, including the second instance's show step). The
    printed route sent dialog id 0 to buildInputDialog; id 0 goes to
    buildContextMenu, so this script drives the two-dialog sequence:
    id 0 -> buildContextMenu -> pick 101 -> buildInputDialog.
Edge-id note: the helper file cites E5798aa47, E9d88d57c, E9e04d50a
    for the onCreate -> showStartupScreensAndDialogs ->
    onFinishedStartup -> loadStudyOptionsFragment chain, but those
    ids are absent from the final graph build_F5.json; the final
    graph carries the same chain as E5906a191, Ef3e13961, Eae89b47b
    (the same ids as the route_11 BFS chain), which this script uses
    instead. All other helper ids verified present.
Preconditions/fixtures:
  - Tablet/large-screen config, so mFragmented is true and
    loadStudyOptionsFragment runs (DeckPicker.java:827-830).
  - Deck non-empty, non-dynamic, with zero new/learning/due cards:
    that is CONTENT_CONGRATS, the only state in which the study
    options start button shows the custom-study context menu
    (StudyOptionsFragment.java:127-130, 566-570). Study every card
    first, then return to the deck picker while counts are zero.
Mapping notes:
  - The context-menu item for CUSTOM_STUDY_REV (101) is titled
    "Increase today’s review card limit"
    (custom_study_increase_review_limit; the apostrophe is the
    strings.xml character, copied exactly).
  - The two CustomStudyDialog.<init> -> onCreateDialog steps
    (E90f59cc0, both instances) are INFERRED: the support-v4
    DialogFragment lifecycle source is not in the tree. The script
    drives the real showDialogFragment calls; the lifecycle
    transition is their direct consequence.
  - The second instance's show step Ee5ab498a ($1.onSelection ->
    showDialogFragment) is a parallel branch edge, listed right
    after the newInstance edge it accompanies.
  - The study options start button is titled "Study"
    (studyoptions_start).
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E5906a191", "Ef3e13961",
    "Eae89b47b", "Ea73b74da", "E518f89ef", "E0cf28f6d", "Edb8f0d37",
    "Ecf5cf491", "E2c327703", "E90f59cc0", "Ec6b33a80", "Efd744093",
    "Efc4080d6", "Eda5cc9ae", "Ee5ab498a", "E2c327703", "E90f59cc0",
    "Eab9aa442", "Eb7b12863", "E0ca39dd5",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_05")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
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
    # E5906a191 onCreate -> showStartupScreensAndDialogs
    # (guard: colOpen).
    r.comment("colOpen branch shows startup screens", edge="E5906a191")
    # Ef3e13961 showStartupScreensAndDialogs -> onFinishedStartup
    # (final else branch: enough disc space, no noSpaceLeft, nothing
    # special required).
    r.comment("nothing-special-required branch", edge="Ef3e13961")
    # Eae89b47b onFinishedStartup -> loadStudyOptionsFragment
    # (guard: mFragmented, tablet layout).
    r.comment("fragmented layout loads study options fragment",
              edge="Eae89b47b")
    # Ea73b74da loadStudyOptionsFragment -> S_STUDYOPTIONS_FRAG.
    r.comment("study options fragment shown", edge="Ea73b74da")
    # E518f89ef S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick:
    # tap Study. In CONTENT_CONGRATS the listener takes the else
    # branch to showCustomStudyContextMenu.
    r.tap(edge="E518f89ef", text="Study")
    # E0cf28f6d $1.onClick -> showCustomStudyContextMenu.
    r.comment("CONTENT_CONGRATS branch shows context menu",
              edge="E0cf28f6d")
    # Edb8f0d37 showCustomStudyContextMenu -> newInstance(int,long)
    # (CONTEXT_MENU_STANDARD = 0).
    r.comment("newInstance id 0", edge="Edb8f0d37")
    # Ecf5cf491 newInstance(int,long) -> newInstance(int,long,boolean).
    r.comment("newInstance delegates to 3-arg form", edge="Ecf5cf491")
    # E2c327703 newInstance -> CustomStudyDialog.<init>.
    r.comment("first dialog instance created", edge="E2c327703")
    # E90f59cc0 <init> -> onCreateDialog (INFERRED support-v4
    # lifecycle; the dialog is shown via showDialogFragment).
    r.comment("first dialog onCreateDialog (INFERRED lifecycle)",
              edge="E90f59cc0")
    # Ec6b33a80 onCreateDialog -> buildContextMenu (id 0 < 100; this
    # is the correction of the printed buildInputDialog step).
    r.comment("id 0 takes buildContextMenu branch", edge="Ec6b33a80")
    # Efd744093 buildContextMenu -> CustomStudyDialog$1.<init>
    # (selection listener built).
    r.comment("context-menu selection listener built", edge="Efd744093")
    # Efc4080d6 S_DLG_CUSTOM_STUDY -> $1.onSelection: pick the REV
    # item (101) from the context menu.
    r.tap(edge="Efc4080d6", text="Increase today’s review card limit")
    # Eda5cc9ae $1.onSelection -> newInstance(int,long,boolean)
    # (second instance, id 101).
    r.comment("second instance newInstance id 101", edge="Eda5cc9ae")
    # Ee5ab498a $1.onSelection -> showDialogFragment (the second
    # instance is shown; parallel branch edge).
    r.comment("second dialog shown", edge="Ee5ab498a")
    # E2c327703 newInstance -> CustomStudyDialog.<init> (2nd instance).
    r.comment("second dialog instance created", edge="E2c327703")
    # E90f59cc0 <init> -> onCreateDialog (2nd instance, INFERRED).
    r.comment("second dialog onCreateDialog (INFERRED lifecycle)",
              edge="E90f59cc0")
    # Eab9aa442 onCreateDialog -> buildInputDialog (id 101 >= 100).
    r.comment("id 101 takes buildInputDialog branch", edge="Eab9aa442")
    # Eb7b12863 buildInputDialog -> getText1.
    r.comment("buildInputDialog sets text from getText1",
              edge="Eb7b12863")
    # E0ca39dd5 getText1 -> Sched.totalRevForCurrentDeck (target;
    # CUSTOM_STUDY_REV case at CustomStudyDialog.java:362-363).
    r.comment("REV case calls totalRevForCurrentDeck (target)",
              edge="E0ca39dd5")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
