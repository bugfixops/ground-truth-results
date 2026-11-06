#!/usr/bin/env python3
"""AnkiDroid step2-item3 route_31: Models.rem.

Method: Models.rem
Table verdict: CORRECT (combined-merge redraw, route_table.md
    row 15). Final-sample method, new to the device set (not in
    the Push-2 ROUTES.csv); route number 31 is new, so no existing
    route number is rebound.
Route followed: the final BFS route (16 steps), identical to the
    redraw print (newsample-routes-30.log): deck picker -> options
    menu -> Manage note types -> long-press note type -> context
    menu -> Delete -> confirmation OK -> deleteModel -> DELETE_MODEL
    task -> doInBackGroundDeleteModel -> Models.rem.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Efe74add3 Ec0803f80 Ec31ec494
    E68bf41c2 E5384a709 E82ba5876 Eedf5a98f E55c22d4f Ee84d976b
    Ea9dfcb07 E2e9e4956 E38b4440a E57ec7c14
Preconditions/fixtures:
  - Collection open; at least two note types (the delete
    confirmation dialog requires mModelIds.size() > 1,
    ModelBrowser.java:448). No file fixture is pushed.
Mapping notes:
  - Tap texts verified in res (values/17-model-manager.xml,
    values/03-dialogs.xml): menu item "Manage note types"
    (model_browser_label), context entry "Delete note type"
    (model_browser_delete), confirmation "OK" (dialog_ok).
  - The long-pressed note-type row text is fixture-dependent
    (a note-type name); the script long-presses by description
    and flags the row choice for the real-run driver.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Efe74add3", "Ec0803f80",
    "Ec31ec494", "E68bf41c2", "E5384a709", "E82ba5876", "Eedf5a98f",
    "E55c22d4f", "Ee84d976b", "Ea9dfcb07", "E2e9e4956", "E38b4440a",
    "E57ec7c14",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_31")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_31", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Efe74add3 DeckPicker.onCreate -> S_DECKPICKER: collection open.
    r.comment("deck-picker page shown", edge="Efe74add3")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected.
    r.tap(edge="Ec0803f80", desc="More options")
    # Ec31ec494 onOptionsItemSelected -> S_MODELBROWSER: the model
    # browser menu item is tapped.
    r.tap(edge="Ec31ec494", text="Manage note types")
    # E68bf41c2 S_MODELBROWSER -> ModelBrowser$5.onItemLongClick:
    # long-press a note type in the list.
    r.long_tap(edge="E68bf41c2", desc="note type row")
    # E5384a709 onItemLongClick -> S_DLG_MODELBROWSER_CONTEXT.
    r.comment("note type context menu shown", edge="E5384a709")
    # E82ba5876 S_DLG_MODELBROWSER_CONTEXT -> ModelBrowser$3.onSelection:
    # tap Delete in the note type long-press menu.
    r.tap(edge="E82ba5876", text="Delete note type")
    # Eedf5a98f onSelection -> ModelBrowser.deleteModelDialog.
    r.comment("deleteModelDialog called", edge="Eedf5a98f")
    # E55c22d4f deleteModelDialog -> S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL.
    r.comment("delete note type confirmation dialog shown",
              edge="E55c22d4f")
    # Ee84d976b S_DLG_CONFIRMATION -> ModelBrowser$7.confirm: press OK.
    r.tap(edge="Ee84d976b", text="OK")
    # Ea9dfcb07 confirm -> ModelBrowser.deleteModel.
    r.comment("deleteModel called", edge="Ea9dfcb07")
    # E2e9e4956 deleteModel -> DeckTask.doInBackground@DELETE_MODEL.
    r.comment("DELETE_MODEL task launched", edge="E2e9e4956")
    # E38b4440a doInBackground@DELETE_MODEL -> doInBackGroundDeleteModel.
    r.comment("deleteModel background work", edge="E38b4440a")
    # E57ec7c14 doInBackGroundDeleteModel -> Models.rem (target).
    r.comment("Models.rem reached (target)", edge="E57ec7c14")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
