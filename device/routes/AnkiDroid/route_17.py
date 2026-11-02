#!/usr/bin/env python3
"""AnkiDroid route_17: ModelFieldEditor$6$1.<init>.

Method: ModelFieldEditor$6$1.<init>
Target verdict: FIXED (route_table.md route 17)
Route followed: the final BFS route (17 steps). The fix guards are in
    the graph; the script must satisfy them, notably the step-6 menu
    guard (887 block only, evidence line 890) and the step-17
    modSchema-exception guard.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ec0803f80 Ec31ec494
    E737f97f5 Ebaef8dec E7ba5c3e5 E27518d88 E6a434eae E7f0718c5
    E78a364ca Ee41f94d4 Eaac1b7fd E442921a6 Ef28943f1
Printed route: graphs/AnkiDroid/scratch/route_print/
    ModelFieldEditor_6_1.<init>.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; a model named Basic with a field
    named Front; schema not yet marked changed, so modSchema throws.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Menu and list selectors ("Manage note types", "Basic", "Front",
    "Reposition") are UI strings not fixed by the graph edges; verify
    each against a live uiautomator dump before a real run.
  - Text input uses r.type_text, proven by the shared harness copy
    (device/stage/device/harness/harness.py: type_text(s, edge))
    and by Amaze route scripts using type_text(s, edge) with the
    edge of the step the typing serves. The reposition dialog needs
    a valid in-range integer typed before confirming; "1" is used
    (valid when the model has at least two fields, as Basic does).
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
    "E442921a6", "Ef28943f1",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_17")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_17", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="Manage note types")
    # Ec31ec494 DeckPicker.onOptionsItemSelected -> S_MODELBROWSER:
    # guard item is R.id.action_model_browser_open and the drawer
    # toggle does not consume the item. Automatic after the tap.
    r.comment("model browser opened", edge="Ec31ec494")
    # E737f97f5 S_MODELBROWSER -> ModelBrowser$4.onItemClick: tap a
    # model row (ModelBrowser.java:271-279).
    r.tap(edge="E737f97f5", text="Basic")
    # Ebaef8dec ModelBrowser$4.onItemClick -> ModelFieldEditor.<init>.
    # Automatic after the tap.
    r.comment("ModelFieldEditor started", edge="Ebaef8dec")
    # E7ba5c3e5 ModelFieldEditor.<init> -> ModelFieldEditor.onCreate.
    r.comment("system instantiates ModelFieldEditor, then onCreate",
              edge="E7ba5c3e5")
    # E27518d88 ModelFieldEditor.onCreate -> S_MODELFIELDEDITOR.
    r.comment("model field editor page shown", edge="E27518d88")
    # E6a434eae S_MODELFIELDEDITOR -> ModelFieldEditor$1.onItemClick:
    # tap a field row.
    r.tap(edge="E6a434eae", text="Front")
    # E7f0718c5 ModelFieldEditor$1.onItemClick ->
    # S_DLG_MODELEDITOR_CONTEXT: context menu shown. Automatic.
    r.comment("field context menu shown", edge="E7f0718c5")
    # E78a364ca S_DLG_MODELEDITOR_CONTEXT ->
    # ModelFieldEditor$9.onSelection: choose Reposition.
    r.tap(edge="E78a364ca", text="Reposition")
    # Ee41f94d4 ModelFieldEditor$9.onSelection ->
    # ModelFieldEditor.repositionFieldDialog: guard selection is
    # FIELD_REPOSITION. Automatic after the tap.
    r.comment("reposition dialog built", edge="Ee41f94d4")
    # Eaac1b7fd ModelFieldEditor.repositionFieldDialog ->
    # ModelFieldEditor$6.<init>. Automatic.
    r.comment("reposition dialog callback created", edge="Eaac1b7fd")
    # E442921a6 ModelFieldEditor$6.<init> ->
    # ModelFieldEditor$6.onPositive: type a valid in-range integer,
    # then tap the dialog positive button.
    r.type_text("1", edge="E442921a6")
    r.tap(edge="E442921a6", text="OK")
    # Ef28943f1 ModelFieldEditor$6.onPositive ->
    # ModelFieldEditor$6$1.<init>: guard mCol.modSchema() throws
    # ConfirmModSchemaException. Automatic; this is the target edge.
    r.comment("modSchema throws, target listener created",
              edge="Ef28943f1")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
