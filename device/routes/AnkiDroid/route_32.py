#!/usr/bin/env python3
"""AnkiDroid step2-item3 route_32: Models$TransformFieldMove.<init>.

Method: Models$TransformFieldMove.<init>
Table verdict: CORRECT (combined-merge redraw, route_table.md
    row 17). Final-sample method, new to the device set (not in
    the Push-2 ROUTES.csv); route number 32 is new, so no existing
    route number is rebound.
Route followed: the final BFS route (20 steps), identical to the
    redraw print (newsample-routes-30.log): deck picker -> options
    menu -> Manage note types -> tap note type -> field editor ->
    tap field row -> context menu -> Reposition field -> type 1,
    OK -> REPOSITION_FIELD task -> doInBackGroundRepositionField
    -> Models.moveField -> Models$TransformFieldMove.<init>.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ec0803f80 Ec31ec494
    E737f97f5 Ebaef8dec E7ba5c3e5 E27518d88 E6a434eae E7f0718c5
    E78a364ca Ee41f94d4 Eaac1b7fd E442921a6 Ee1989f34 E37331a72
    E61c549d6 Ec14b3e6c
Preconditions/fixtures:
  - Collection open; a note type with at least one field; the
    field editor opens for the tapped note type. No file fixture
    is pushed.
Mapping notes:
  - Tap texts verified in res: menu item "Manage note types"
    (model_browser_label), field context entry "Reposition field"
    (model_field_editor_reposition_menu), dialog "OK" (dialog_ok).
  - The tapped note-type row and field row texts are
    fixture-dependent; the script taps by description and flags
    the row choices for the real-run driver.
  - The reposition dialog carries a number input
    (ModelFieldEditor.java:352-356, EditText TYPE_CLASS_NUMBER);
    pressing OK with an empty input throws NumberFormatException
    and launches no task, so the script types "1" (valid for any
    field list with at least one field) before OK. The drawn
    print's "press OK" step assumes a valid input; the typed "1"
    is a drive completion, not a route change.
  - PRE-REAL-RUN CHECK: mCol.modSchema() may throw
    ConfirmModSchemaException, showing a ConfirmationDialog whose
    confirm() launches the task (ModelFieldEditor.java:380-395).
    The drawn route takes the direct path (no confirmation). If a
    schema-change confirmation appears on a real run, an extra OK
    tap on that dialog is needed before the task launches.
  - No live run is claimed by this script.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script.
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
    "E6a434eae", "E7f0718c5", "E78a364ca", "Ee41f94d4", "Eaac1b7fd",
    "E442921a6", "Ee1989f34", "E37331a72", "E61c549d6", "Ec14b3e6c",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_32")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_32", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER: collection open.
    r.comment("deck-picker page shown", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected.
    r.tap(edge="Ec0803f80", desc="More options")
    # Ec31ec494 onOptionsItemSelected -> S_MODELBROWSER: the model
    # browser menu item is tapped.
    r.tap(edge="Ec31ec494", text="Manage note types")
    # E737f97f5 S_MODELBROWSER -> ModelBrowser$4.onItemClick: tap a
    # note type in the list (opens its field editor).
    r.tap(edge="E737f97f5", desc="note type row")
    # Ebaef8dec onItemClick -> ModelFieldEditor.<init>.
    r.comment("field editor opened for the tapped note type",
              edge="Ebaef8dec")
    # E7ba5c3e5 ModelFieldEditor.<init> -> ModelFieldEditor.onCreate.
    r.comment("system instantiates ModelFieldEditor, then onCreate",
              edge="E7ba5c3e5")
    # E27518d88 onCreate -> S_MODELFIELDEDITOR: field list shown.
    r.comment("field editor screen shown", edge="E27518d88")
    # E6a434eae S_MODELFIELDEDITOR -> ModelFieldEditor$1.onItemClick:
    # tap a field name row on the field editor screen.
    r.tap(edge="E6a434eae", desc="field row")
    # E7f0718c5 onItemClick -> S_DLG_MODELEDITOR_CONTEXT: the field
    # context menu is shown for the tapped row.
    r.comment("field context menu shown", edge="E7f0718c5")
    # E78a364ca S_DLG_MODELEDITOR_CONTEXT -> ModelFieldEditor$9.onSelection:
    # tap Reposition field in the field context menu.
    r.tap(edge="E78a364ca", text="Reposition field")
    # Ee41f94d4 onSelection -> ModelFieldEditor.repositionFieldDialog.
    r.comment("reposition dialog called", edge="Ee41f94d4")
    # Eaac1b7fd repositionFieldDialog -> ModelFieldEditor$6.<init>.
    r.comment("reposition dialog shown", edge="Eaac1b7fd")
    # E442921a6 $6.<init> -> $6.onPositive: type a valid position
    # (1) in the number input, then press OK.
    r.type_text("1", edge="E442921a6")
    r.tap(edge="E442921a6", text="OK")
    # Ee1989f34 onPositive -> DeckTask.doInBackground@REPOSITION_FIELD.
    r.comment("REPOSITION_FIELD task launched", edge="Ee1989f34")
    # E37331a72 doInBackground@REPOSITION_FIELD -> doInBackGroundRepositionField.
    r.comment("reposition background work", edge="E37331a72")
    # E61c549d6 doInBackGroundRepositionField -> Models.moveField.
    r.comment("moveField called", edge="E61c549d6")
    # Ec14b3e6c moveField -> Models$TransformFieldMove.<init> (target).
    r.comment("TransformFieldMove reached (target)", edge="Ec14b3e6c")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
