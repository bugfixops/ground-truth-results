#!/usr/bin/env python3
"""AnkiDroid route_06: ModelEditorContextMenu.onCreateDialog.

Target: ModelEditorContextMenu.onCreateDialog (builds the
    MaterialDialog for a field row's context menu).
Table verdict: UNCLEAR (first-draw verdict, stands; this script
    drives the C06 sequence, which has no sequence change).
Route followed: C06 from helper/b6fix-r01-06/CORRECTED_ROUTES.md,
    with final-graph edge ids (14 edges). The route is unchanged
    from the BFS route except for guard/state fixes.
Edge-id note: the helper file cites Eaa8f1a6b for
    onOptionsItemSelected -> S_MODELBROWSER, but that id is absent
    from the final graph build_F5.json; the final graph carries the
    same transition as Ec31ec494 (guard: item
    action_model_browser_open and drawer toggle does not consume
    it), which this script uses instead. All other helper ids
    verified present.
Preconditions/fixtures:
  - Collection open; WRITE_EXTERNAL_STORAGE granted;
    collection.anki2 exists in the AnkiDroid folder.
  - At least one model with at least one field. The script taps the
    model "Basic" and the field "Front"; if setup creates different
    names, change FIXTURE_MODEL / FIXTURE_FIELD to match.
Mapping notes:
  - The final edge Ea860d9d5 (<init> -> onCreateDialog) is
    INFERRED: the support-v4 DialogFragment lifecycle source is not
    in the tree, and the route skips the showDialogFragment step
    (ModelFieldEditor.java:139) that leads into it. The script
    performs the real tap that shows the dialog (the field-row tap
    drives newInstance + showDialogFragment); onCreateDialog is
    their direct framework consequence. The INFERRED status is a
    graph-evidence caveat, not a device blocker, which is why this
    route is marked scripted with the caveat stated here and in
    REPORT.md. The library name is support-v4, not androidx.
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
    "Ec31ec494", "E737f97f5", "Ebaef8dec", "E7ba5c3e5", "E27518d88",
    "E6a434eae", "Ee0eb2278", "E2c1af362", "Ea860d9d5",
]

FIXTURE_MODEL = "Basic"
FIXTURE_FIELD = "Front"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_06")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_06", edge_ids=EDGE_IDS,
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
    # Ec31ec494 onOptionsItemSelected -> S_MODELBROWSER
    # (action_model_browser_open; drawer toggle does not consume it).
    r.tap(edge="Ec31ec494", text="Manage note types")
    # E737f97f5 S_MODELBROWSER -> ModelBrowser$4.onItemClick: tap a
    # model row (state: models loaded, position valid; the list and
    # listener exist only after onCollectionLoaded).
    r.tap(edge="E737f97f5", text=FIXTURE_MODEL)
    # Ebaef8dec $4.onItemClick -> ModelFieldEditor.<init> (Intent
    # with noteTypeID extra).
    r.comment("startActivityForResult ModelFieldEditor",
              edge="Ebaef8dec")
    # E7ba5c3e5 ModelFieldEditor.<init> -> ModelFieldEditor.onCreate.
    r.comment("ModelFieldEditor onCreate", edge="E7ba5c3e5")
    # E27518d88 ModelFieldEditor.onCreate -> S_MODELFIELDEDITOR.
    r.comment("model field editor page shown", edge="E27518d88")
    # E6a434eae S_MODELFIELDEDITOR -> ModelFieldEditor$1.onItemClick:
    # tap a field row (state: onCollectionLoaded has run and
    # createfieldLabels registered the listener).
    r.tap(edge="E6a434eae", text=FIXTURE_FIELD)
    # Ee0eb2278 $1.onItemClick -> ModelEditorContextMenu.newInstance
    # (label + listener).
    r.comment("field tap creates context menu instance",
              edge="Ee0eb2278")
    # E2c1af362 newInstance -> ModelEditorContextMenu.<init>.
    r.comment("context menu instance created", edge="E2c1af362")
    # Ea860d9d5 <init> -> onCreateDialog (target; INFERRED
    # support-v4 lifecycle step, reached via the showDialogFragment
    # call the field tap drives).
    r.comment("dialog shown, onCreateDialog runs (target; INFERRED "
              "support-v4 lifecycle step)", edge="Ea860d9d5")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
