#!/usr/bin/env python3
"""AnkiDroid route_26b: ModelFieldEditor$1.<init> (route B, rename flow).

Method: ModelFieldEditor$1.<init>
Target verdict: WRONG (route_table.md route 26)
Route followed: CORRECTED route B (the rename-flow route), never the
    BFS dispatch route via the generic page through ModelBrowser
    deleteModelDialog. Route B shares route A steps 1-5, then runs
    the field-row tap, context menu, Rename, $5.onPositive,
    renameField (throws), the rename variant page, $5$1.confirm,
    renameField again, fullRefreshList, createfieldLabels, and the
    target. The primary script is route_26.py (route A); this file
    is the second script the format allows.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ec0803f80 Ec31ec494
    E737f97f5 Ebaef8dec E7ba5c3e5 E837cf393 E6424f703 E6a434eae
    E7f0718c5 E78a364ca Ecd7097ff E1b8c4afe Eb667146a Ec4550482
    Ee4640531 Ed28154fc E1412af99 E23ae6128 E31ebcb52 E7d28913e
Sources: route_table.md route 26 route B; helper/b6fix-r25-30/
    CORRECTED_ROUTES.md route 26 route B.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; a model named Basic with a field
    named Front; schema not yet marked changed, so renameField throws
    ConfirmModSchemaException on the first call.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Menu, list, and dialog selectors ("Manage note types", "Basic",
    "Front", "Rename", the rename dialog positive button, and the
    confirmation dialog confirm button) are UI strings not fixed by
    the graph edges; verify each against a live uiautomator dump
    before a real run.
  - E78a364ca is the shared context-menu selection edge: route 17
    uses it with selection FIELD_REPOSITION, this route uses it
    with selection RENAME (renameFieldDialog follows). The edge id
    is the same; the selection value differs.
  - Text input uses r.type_text, proven by the shared harness copy
    (device/stage/device/harness/harness.py: type_text(s, edge)).
    The new field name typed is "Front2": a valid name that does
    not collide with the Basic model's existing fields
    (Front, Back).
  - Eb667146a (S_MODELFIELDEDITOR -> $5.onPositive) is the graph's
    GUI abstraction for tapping the rename dialog's positive button
    after $5 is created; it is not a second, separate tap.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Ec31ec494", "E737f97f5", "Ebaef8dec", "E7ba5c3e5", "E837cf393",
    "E6424f703", "E6a434eae", "E7f0718c5", "E78a364ca", "Ecd7097ff",
    "E1b8c4afe", "Eb667146a", "Ec4550482", "Ee4640531", "Ed28154fc",
    "E1412af99", "E23ae6128", "E31ebcb52", "E7d28913e",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_26b")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_26b", edge_ids=EDGE_IDS,
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
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected.
    r.tap(edge="Ec0803f80", desc="Manage note types")
    # Ec31ec494 DeckPicker.onOptionsItemSelected -> S_MODELBROWSER.
    r.comment("model browser opened", edge="Ec31ec494")
    # E737f97f5 S_MODELBROWSER -> ModelBrowser$4.onItemClick.
    r.tap(edge="E737f97f5", text="Basic")
    # Ebaef8dec ModelBrowser$4.onItemClick -> ModelFieldEditor.<init>.
    r.comment("ModelFieldEditor started", edge="Ebaef8dec")
    # E7ba5c3e5 ModelFieldEditor.<init> -> ModelFieldEditor.onCreate.
    r.comment("system instantiates ModelFieldEditor, then onCreate",
              edge="E7ba5c3e5")
    # E837cf393 ModelFieldEditor.onCreate ->
    # ModelFieldEditor.onCollectionLoaded. Automatic.
    r.comment("model field editor collection loaded",
              edge="E837cf393")
    # E6424f703 ModelFieldEditor.onCollectionLoaded ->
    # ModelFieldEditor.createfieldLabels, so the field list exists.
    r.comment("field labels created", edge="E6424f703")
    # E6a434eae S_MODELFIELDEDITOR -> ModelFieldEditor$1.onItemClick:
    # tap a field row.
    r.tap(edge="E6a434eae", text="Front")
    # E7f0718c5 ModelFieldEditor$1.onItemClick ->
    # S_DLG_MODELEDITOR_CONTEXT: context menu shown. Automatic.
    r.comment("field context menu shown", edge="E7f0718c5")
    # E78a364ca S_DLG_MODELEDITOR_CONTEXT ->
    # ModelFieldEditor$9.onSelection: choose Rename (selection
    # value RENAME, not FIELD_REPOSITION as in route 17).
    r.tap(edge="E78a364ca", text="Rename")
    # Ecd7097ff ModelFieldEditor$9.onSelection ->
    # ModelFieldEditor.renameFieldDialog. Automatic.
    r.comment("rename dialog requested", edge="Ecd7097ff")
    # E1b8c4afe ModelFieldEditor.renameFieldDialog ->
    # ModelFieldEditor$5.<init>. Automatic.
    r.comment("rename dialog callback created", edge="E1b8c4afe")
    # Type the new field name first (see header), then confirm.
    r.type_text("Front2", edge="Eb667146a")
    # Eb667146a S_MODELFIELDEDITOR -> ModelFieldEditor$5.onPositive:
    # the rename dialog positive tap (graph GUI abstraction).
    r.tap(edge="Eb667146a", text="OK")
    # Ec4550482 ModelFieldEditor$5.onPositive ->
    # ModelFieldEditor.renameField: first call, valid-name branch
    # (ModelFieldEditor.java:312-315). Automatic after the tap.
    r.comment("rename attempted, first call", edge="Ec4550482")
    # Ee4640531 ModelFieldEditor$5.onPositive ->
    # S_DLG_CONFIRMATION_MODELFIELDEDITOR_RENAME: guard renameField
    # throws ConfirmModSchemaException (schema not yet changed).
    r.comment("rename confirmation dialog shown", edge="Ee4640531")
    # Ed28154fc S_DLG_CONFIRMATION_MODELFIELDEDITOR_RENAME ->
    # ModelFieldEditor$5$1.confirm: tap Confirm
    # (ModelFieldEditor.java:320-323).
    r.tap(edge="Ed28154fc", text="OK")
    # E1412af99 ModelFieldEditor$5$1.confirm ->
    # ModelFieldEditor.renameField: second call, after modSchema
    # (false) at :322. Automatic after the tap.
    r.comment("rename retried after confirmation", edge="E1412af99")
    # E23ae6128 ModelFieldEditor.renameField ->
    # ModelFieldEditor.fullRefreshList (save at :447, refresh at
    # :448). Automatic.
    r.comment("field list refreshed", edge="E23ae6128")
    # E31ebcb52 ModelFieldEditor.fullRefreshList ->
    # ModelFieldEditor.createfieldLabels. Automatic.
    r.comment("field labels recreated", edge="E31ebcb52")
    # E7d28913e ModelFieldEditor.createfieldLabels ->
    # ModelFieldEditor$1.<init>. Automatic; this is the target edge.
    r.comment("field item-click listener recreated",
              edge="E7d28913e")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
