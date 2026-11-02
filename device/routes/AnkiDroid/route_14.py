#!/usr/bin/env python3
"""AnkiDroid route_14: Models$TransformFieldDelete.<init>.

Target: Models$TransformFieldDelete.<init>.
Table verdict: CORRECT (combined-merge redraw, row 16, 21 steps;
    the printed route IS the judged route). This is the 21-step
    DELETEFIELD variant: step 15 E59b6ceef (deleteFieldDialog ->
    DELETEFIELD confirmation page, guard mFieldLabels.size() >= 2)
    and step 16 E4daf57a4 ($3.confirm) replace old steps 15-16
    E5cba0e2c/Ef84c6616; steps 17-21 (deleteField -> DELETE_FIELD
    task -> remField -> TransformFieldDelete) are unchanged.
    Drive: Delete field -> OK in the confirmation dialog.
Route followed: corrected route, 21 edges: steps 1-6 as printed to
    S_MODELBROWSER, then model item CLICK -> ModelFieldEditor ->
    field list -> field tap -> context menu -> deleteFieldDialog ->
    $3.confirm -> deleteField -> DELETE_FIELD task -> remField ->
    TransformFieldDelete.
Preconditions: collection open; collection.anki2 exists;
    WRITE_EXTERNAL_STORAGE granted; model "Basic" with at least two
    fields ("Front" plus one more).
Mapping notes:
  - Reuses the old first-draw route_06 script's prefix (deck picker
    -> Manage note types -> model tap -> field tap) with the
    fixture names Basic / Front, but replaces its context-menu tail
    (onCreateDialog target) with the delete-field tail, and uses
    item CLICK where the printed route wrongly used long-click.
  - "More options" is the standard AppCompat overflow description;
    verify it against a live uiautomator dump before a real run.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Ec31ec494", "E737f97f5", "Ebaef8dec", "E7ba5c3e5", "E27518d88",
    "E6a434eae", "E7f0718c5", "E78a364ca", "Ee94b33d8", "E59b6ceef",
    "E4daf57a4", "Ea45d1c59", "Eb39e20a8", "E174b8f61", "Ef3f2eae2",
    "E11ebf3f9",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_14")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_14", edge_ids=EDGE_IDS,
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
    # Ec0803f80 S_DECKPICKER -> onOptionsItemSelected: open the
    # options menu (standard AppCompat overflow description).
    r.tap(edge="Ec0803f80", desc="More options")
    # Ec31ec494 onOptionsItemSelected -> S_MODELBROWSER
    # (action_model_browser_open). String verified in res:
    # model_browser_label = "Manage note types".
    r.tap(edge="Ec31ec494", text="Manage note types")
    # E737f97f5 S_MODELBROWSER -> ModelBrowser$4.onItemClick: tap a
    # model row (item CLICK, not long-click; the corrected route
    # opens ModelFieldEditor from the click listener,
    # ModelBrowser.java:271-280).
    r.tap(edge="E737f97f5", text="Basic")
    # Ebaef8dec $4.onItemClick -> ModelFieldEditor.<init> (Intent
    # with noteTypeID extra).
    r.comment("startActivityForResult ModelFieldEditor",
              edge="Ebaef8dec")
    # E7ba5c3e5 ModelFieldEditor.<init> -> onCreate.
    r.comment("ModelFieldEditor onCreate", edge="E7ba5c3e5")
    # E27518d88 onCreate -> S_MODELFIELDEDITOR.
    r.comment("model field editor page shown", edge="E27518d88")
    # E6a434eae S_MODELFIELDEDITOR -> ModelFieldEditor$1.onItemClick:
    # tap a field row (listener registered by onCollectionLoaded /
    # createfieldLabels).
    r.tap(edge="E6a434eae", text="Front")
    # E7f0718c5 $1.onItemClick -> S_DLG_MODELEDITOR_CONTEXT (the
    # field tap drives newInstance + showDialogFragment).
    r.comment("field context-menu dialog shown", edge="E7f0718c5")
    # E78a364ca S_DLG_MODELEDITOR_CONTEXT -> $9.onSelection: the
    # context-menu listener switch (ModelFieldEditor.java:590-601).
    # String verified in res: model_field_editor_delete =
    # "Delete field".
    r.tap(edge="E78a364ca", text="Delete field")
    # Ee94b33d8 $9.onSelection -> deleteFieldDialog.
    r.comment("deleteFieldDialog", edge="Ee94b33d8")
    # E59b6ceef deleteFieldDialog -> DELETEFIELD confirmation page
    # (guard: mFieldLabels.size() >= 2, ModelFieldEditor.java:236-237).
    # at least 2 fields, else only a toast (ModelFieldEditor
    # .java:236-237); the fixture model must satisfy it.
    r.comment("confirmation dialog shown", edge="E59b6ceef")
    # E4daf57a4 DELETEFIELD confirmation -> ModelFieldEditor$3.confirm
    # (this activity's own confirm, ModelFieldEditor.java:241-256,
    # not ModelBrowser's delete-model confirm; positive text
    # dialog_ok = "OK").
    # this activity's own confirm (ModelFieldEditor.java:241-256),
    # not ModelBrowser's delete-model confirm. Positive text is
    # dialog_ok = "OK" (ConfirmationDialog.java:38).
    r.tap(edge="E4daf57a4", text="OK")
    # Ea45d1c59 $3.confirm -> deleteField.
    r.comment("deleteField", edge="Ea45d1c59")
    # Eb39e20a8 deleteField -> DeckTask.doInBackground@DELETE_FIELD.
    r.comment("DELETE_FIELD task launched", edge="Eb39e20a8")
    # E174b8f61 -> doInBackGroundDeleteField.
    r.comment("doInBackGroundDeleteField", edge="E174b8f61")
    # Ef3f2eae2 -> Models.remField.
    r.comment("remField", edge="Ef3f2eae2")
    # E11ebf3f9 remField -> Models$TransformFieldDelete.<init>
    # (target; Models.java:575).
    r.comment("TransformFieldDelete constructed (target)",
              edge="E11ebf3f9")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
