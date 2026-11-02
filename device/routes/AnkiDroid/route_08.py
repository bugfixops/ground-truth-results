#!/usr/bin/env python3
"""AnkiDroid route_08 (final draw): ModelEditorContextMenu.onCreateDialog.

Target: ModelEditorContextMenu.onCreateDialog (builds the
    MaterialDialog for a field row's context menu).
Table verdict: CORRECT (final draw, 14 steps; the BFS route IS the
    judged route, so this script drives the BFS route).
Route followed: final-draw BFS route from helper/judge-final/
    route_08.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). Reused from the
    first-draw script for the same method (old route_06): the edge
    list is unchanged and the drive is identical; only the route
    number, the table reference, and the verdict note changed.
    Condition for the model-browser step: the model list must load
    successfully (ModelBrowser onPostExecute requires
    result.getBoolean(), ModelBrowser.java:108-118).
Preconditions (see ROUTES_rows.csv setup cell):
  - Collection open; WRITE_EXTERNAL_STORAGE granted;
    collection.anki2 exists in the AnkiDroid folder.
  - At least one model with at least one field. The script taps the
    model "Basic" and the field "Front"; if setup creates different
    names, change FIXTURE_MODEL / FIXTURE_FIELD to match.
Mapping notes:
  - Selectors verified against the printed tree: "Manage note
    types" (model_browser_label string); model and field rows are
    tapped by their row text (Basic / Front), which setup must
    match.
  - The "More options" content description is the standard AppCompat
    overflow description; verify it against a live uiautomator dump
    before a real run.
  - The final edge Ea860d9d5 (<init> -> onCreateDialog) is
    INFERRED: the support-v4 DialogFragment lifecycle source is not
    in the tree, and the route skips the showDialogFragment step
    (ModelFieldEditor.java:139) that leads into it. The script
    performs the real tap that shows the dialog (the field-row tap
    drives newInstance + showDialogFragment); onCreateDialog is
    their direct framework consequence. The library name is
    support-v4, not androidx (ModelEditorContextMenu.java:5 imports
    android.support.v4.app.DialogFragment).
  - Route-08 flag carried from the table: the same method was
    UNCLEAR in the first draw (route 06) because this final
    <init> -> onCreateDialog step has no printed framework evidence
    and stays INFERRED. The final-draw judge marks that step
    genuine-INFERRED (the fragment's own onCreateDialog is printed
    at ModelEditorContextMenu.java:31, and support-v4 lifecycle
    calls it once the fragment is shown) and therefore CORRECT, the
    same genuine-INFERRED convention used for route 02's Apache
    dispatch and route 01's Gson step. If the table auditor rules
    UNCLEAR, this row flips to UNCLEAR with no other change; the
    script itself is unaffected.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh already does pm clear, permission
    grants, fixture pushes, and per-app setup before this script, so
    the script performs only the route actions starting from launch.
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
    parser = argparse.ArgumentParser(description="AnkiDroid route_08")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_08", edge_ids=EDGE_IDS,
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
