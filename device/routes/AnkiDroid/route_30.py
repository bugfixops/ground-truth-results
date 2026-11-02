#!/usr/bin/env python3
"""AnkiDroid route_30: Models._availClozeOrds(JSONObject,String,boolean).

Method: Models._availClozeOrds(JSONObject,String,boolean)
Target verdict: WRONG (route_table.md route 30)
Route followed: the CORRECTED route via DeckTask SAVE_MODEL (10
    corrected steps, expanded here with the UI prefix to the
    template editor), never the BFS old-DeckPicker prefix: that
    prefix is guard-inconsistent, because save(m,false) at
    Models.java:174 cannot satisfy the templates==true guard on the
    save -> _syncTemplates edge (Models.java:191-192).
Edge ids in order (prefix 15 + SAVE_MODEL chain 10):
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ed1dad133 E0e89f361
    Eb06cba16 E352d419a E0281e707 E37ba8c1f E43fdf761 E1daab677
    Ee8a3d32e E9d2d3b7f E731864d1 Ef2bc6ed3 E982d45bb E460971ee
    E5de4e7fd Eace758ad E9003799e Eb5a7a949 E3185702b E459f83ca
    Eda12e377
Sources: route_table.md route 30; helper/b6fix-r25-30/
    CORRECTED_ROUTES.md route 30.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: collection file exists; template editor opened from a
    note; template text edited, so modelHasChanged is true; the
    model has an id (m non-null, has id, id != 0); the model type
    is MODEL_CLOZE; the notes query returns at least one row, so
    genCards runs availOrds.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Drawer and menu selectors ("Card browser", "Add", "Cards",
    "Save model") are UI strings not fixed by the graph edges;
    verify them against a live uiautomator dump before a real run.
  - Text input uses r.type_text, proven by the shared harness copy
    (device/stage/device/harness/harness.py: type_text(s, edge)).
    The template text is edited by appending " edited" to the
    focused template field, so modelHasChanged is true before Save
    model is tapped. This assumes the template field is focused on
    entry; verify the focus target on a live dump, and tap the
    field first if it is not focused. The typing is logged against
    the next edge in script order (Ef2bc6ed3, the Save press).
  - The provider route (CardContentProvider.java:609, also
    save(m,true)) was not chosen: the DeckTask route is the app's
    own model-save flow.
  - A guard-checking redraw must reject the old DeckPicker prefix
    in favour of this SAVE_MODEL prefix; the builder's best route
    still shows the old prefix because it ignores guard text.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ed1dad133",
    "E0e89f361", "Eb06cba16", "E352d419a", "E0281e707", "E37ba8c1f",
    "E43fdf761", "E1daab677", "Ee8a3d32e", "E9d2d3b7f", "E731864d1",
    "Ef2bc6ed3", "E982d45bb", "E460971ee", "E5de4e7fd", "Eace758ad",
    "E9003799e", "Eb5a7a949", "E3185702b", "E459f83ca", "Eda12e377",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_30")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_30", edge_ids=EDGE_IDS,
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
    # Ed1dad133 S_DECKPICKER -> DeckPicker.openCardBrowser: drawer
    # item nav_browser.
    r.tap(edge="Ed1dad133", text="Card browser")
    # E0e89f361 DeckPicker.openCardBrowser -> CardBrowser.<init>.
    r.comment("CardBrowser started", edge="E0e89f361")
    # Eb06cba16 CardBrowser.<init> -> CardBrowser.onCreate.
    r.comment("system instantiates CardBrowser, then onCreate",
              edge="Eb06cba16")
    # E352d419a CardBrowser.onCreate -> S_CARDBROWSER.
    r.comment("card browser page shown", edge="E352d419a")
    # E0281e707 S_CARDBROWSER -> CardBrowser.onOptionsItemSelected.
    r.tap(edge="E0281e707", text="Add")
    # E37ba8c1f CardBrowser.onOptionsItemSelected -> S_NOTEEDITOR:
    # guard action_add_card_from_card_browser, drawer toggle does
    # not consume the item. Automatic after the tap.
    r.comment("note editor page shown (add-card flow)",
              edge="E37ba8c1f")
    # E43fdf761 S_NOTEEDITOR -> NoteEditor$2.onClick: tap the Cards
    # button (NoteEditor.java:352-353, 357).
    r.tap(edge="E43fdf761", text="Cards")
    # E1daab677 NoteEditor$2.onClick ->
    # NoteEditor.showCardTemplateEditor. Automatic.
    r.comment("template editor requested", edge="E1daab677")
    # Ee8a3d32e NoteEditor.showCardTemplateEditor ->
    # CardTemplateEditor.<init> (valid model id required). Automatic.
    r.comment("template editor started", edge="Ee8a3d32e")
    # E9d2d3b7f CardTemplateEditor.<init> ->
    # CardTemplateEditor.onCreate.
    r.comment("system instantiates template editor, then onCreate",
              edge="E9d2d3b7f")
    # E731864d1 CardTemplateEditor.onCreate -> S_CARDTEMPLATEEDITOR.
    r.comment("template editor page shown", edge="E731864d1")
    # Edit the template text so modelHasChanged is true (see
    # header for the focus assumption).
    r.type_text(" edited", edge="Ef2bc6ed3")
    # Ef2bc6ed3 S_CARDTEMPLATEEDITOR ->
    # CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected:
    # tap Save model (action_confirm, modelHasChanged true,
    # CardTemplateEditor.java:507-512).
    r.tap(edge="Ef2bc6ed3", text="Save model")
    # E982d45bb fragment onOptionsItemSelected ->
    # DeckTask.launchDeckTask (TASK_TYPE_SAVE_MODEL,
    # mSaveModelAndExitHandler, :512). Automatic after the tap.
    r.comment("SAVE_MODEL task launched", edge="E982d45bb")
    # E460971ee DeckTask.launchDeckTask -> DeckTask.doInBackground.
    r.comment("task running", edge="E460971ee")
    # E5de4e7fd DeckTask.doInBackground ->
    # DeckTask.doInBackgroundSaveModel (TASK_TYPE_SAVE_MODEL case,
    # :330-331). Automatic.
    r.comment("save-model task running", edge="E5de4e7fd")
    # Eace758ad DeckTask.doInBackgroundSaveModel ->
    # Models.save(JSONObject,boolean): save(m,true) at :1075.
    r.comment("model saved with templates true", edge="Eace758ad")
    # E9003799e Models.save(JSONObject,boolean) ->
    # Models._syncTemplates: guard templates true and m non-null
    # with id and id != 0 (Models.java:191-192). Automatic.
    r.comment("templates synced", edge="E9003799e")
    # Eb5a7a949 Models._syncTemplates -> Collection.genCards(long[])
    # (Models.java:884-885). Automatic.
    r.comment("cards generated", edge="Eb5a7a949")
    # E3185702b Collection.genCards(long[]) -> Models.availOrds:
    # guard notes query returns at least one row (:653). Automatic.
    r.comment("available ords computed", edge="E3185702b")
    # E459f83ca Models.availOrds ->
    # Models._availClozeOrds(JSONObject,String): guard model type
    # MODEL_CLOZE (Models.java:1127-1129). Automatic.
    r.comment("cloze ords computed", edge="E459f83ca")
    # Eda12e377 Models._availClozeOrds(JSONObject,String) ->
    # Models._availClozeOrds(JSONObject,String,boolean): unconditional
    # delegation (Models.java:1185-1186). Automatic; target edge.
    r.comment("cloze ords with boolean flag reached",
              edge="Eda12e377")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
