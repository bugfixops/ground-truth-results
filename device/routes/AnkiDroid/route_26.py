#!/usr/bin/env python3
"""AnkiDroid route_26: ModelFieldEditor$1.<init> (route A, open route).

Method: ModelFieldEditor$1.<init>
Target verdict: WRONG (route_table.md route 26)
Route followed: CORRECTED route A (the open route), never the BFS
    dispatch route via the generic page through ModelBrowser
    deleteModelDialog. Route A reaches the target on every
    ModelFieldEditor open, independent of the rename flow, because
    onCollectionLoaded calls createfieldLabels.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ec0803f80 Ec31ec494
    E737f97f5 Ebaef8dec E7ba5c3e5 E837cf393 E6424f703 E7d28913e
Sources: route_table.md route 26 route A; helper/b6fix-r25-30/
    CORRECTED_ROUTES.md route 26 route A.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; a model named Basic exists.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Menu and list selectors ("Manage note types", "Basic") are UI
    strings not fixed by the graph edges; verify them against a
    live uiautomator dump before a real run.
  - The parallel page edge E27518d88 (ModelFieldEditor.onCreate ->
    S_MODELFIELDEDITOR) is the same lifecycle step as the loader
    edge E837cf393 (onCreate -> onCollectionLoaded) carried here;
    the edge list carries the loader edge because createfieldLabels
    is reached through onCollectionLoaded.
  - The rename-flow variant is a second script, route_26b.py, with
    its own edge list; it is not merged into this file.
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
    "E6424f703", "E7d28913e",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_26")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_26", edge_ids=EDGE_IDS,
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
    # E837cf393 ModelFieldEditor.onCreate ->
    # ModelFieldEditor.onCollectionLoaded: loader delivery
    # (ModelFieldEditor.java:116-119). Automatic.
    r.comment("model field editor collection loaded",
              edge="E837cf393")
    # E6424f703 ModelFieldEditor.onCollectionLoaded ->
    # ModelFieldEditor.createfieldLabels (ModelFieldEditor.java:119).
    # Automatic.
    r.comment("field labels created", edge="E6424f703")
    # E7d28913e ModelFieldEditor.createfieldLabels ->
    # ModelFieldEditor$1.<init> (ModelFieldEditor.java:132-135,
    # setOnItemClickListener at :135). Automatic; target edge.
    r.comment("field item-click listener created", edge="E7d28913e")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
