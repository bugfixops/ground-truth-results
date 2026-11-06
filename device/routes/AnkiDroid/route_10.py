#!/usr/bin/env python3
"""AnkiDroid route_10 (final draw): Template$1.compare.

Target: Template$1.compare (anonymous Comparator in
    Template.render_unescaped, Template.java:229-238).
Table verdict: CORRECT (combined-merge redraw, row 11, 17 steps;
    the judged route, so this script drives the BFS route, NOT
    the old first-draw Template script's CardBrowser render
    route). Edges unchanged.
Route followed: final-draw BFS route from helper/judge-final/
    route_10.txt, edge ids verified against
    graphs/AnkiDroid/out/ankidroid_trigger_graph.json and
    methods.csv (route_edge_ids identical). No first-draw script
    drives this route: the old route_10 script drove a
    CardBrowser-scroll render path, which is a different prefix.
Route shape: launch-only. On a cold start where the collection is
    not yet open, DeckPicker.onCreate takes the colOpen==false
    branch (permission granted, directory accessible) and calls
    CollectionHelper.exceededCursorSizeLimit, which calls getCol;
    getCol opens the collection via Storage.Collection when it is
    not already open (CollectionHelper.java:99). With a stored
    schema below SCHEMA_VERSION, Storage._upgrade runs and saves
    each model; a saved model with non-zero id takes _updateRequired,
    which renders each template via _reqForTemplate -> _renderQA ->
    Template.render -> render_tags -> render_unescaped, where the
    multi-modifier tag sort calls Template$1.compare.
Preconditions (see ROUTES_rows.csv setup cell):
  - Cold start with the collection not yet open;
    WRITE_EXTERNAL_STORAGE granted; AnkiDroid directory accessible.
  - Stored collection schema below SCHEMA_VERSION so
    Storage._upgrade runs (Storage.java:65-67).
  - A saved model with non-zero id (Models.java:189 guard).
  - A non-cloze model with a template whose qfmt contains a tag
    with at least 2 modifiers whose field is absent from the
    _reqForTemplate context (Template.java:199-240; JDK sort calls
    compare only for >= 2 modifiers). The _reqForTemplate values are
    synthetic (Models.java:1079, 1082), not a real note.
  - Judge caveat carried, not hidden: the judge's steps 4-6 note
    describes this as a transient first-open failure followed by a
    successful retry inside exceededCursorSizeLimit -> getCol ->
    Storage.Collection, and states no printed line contradicts it.
    The script drives the launch that enters this probe; whether
    the probe's getCol open is the first or a retry open is a
    live-run observation, flagged in NOTES.md for the live run to
    confirm (a run whose collection opens by the ordinary
    firstCollectionOpen path without entering the upgrade chain
    would not reach the target).
Mapping notes:
  - No UI tap exists on this route after launch: every step after
    onCreate is an automatic collection-open/upgrade consequence,
    logged with r.comment (and one dwell for the open/upgrade).
  - The final edge Ef98eff28 (render_unescaped -> Template$1
    .compare) is a JDK sort dispatch, INFERRED (java.util not in
    the tree); the comparator's existence at Template.java:229-238
    is printed.
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
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E45d63a96", "E37e55142",
    "E4c7e034e", "Eda786c6a", "E9ce50a2f", "E8c772cd2", "E2fe95109",
    "Ed609aaee", "E61c27691", "E1eb126ee", "Ef0029247", "Ef3d963e0",
    "E82c9f13e", "Ef98eff28",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_10")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_10", edge_ids=EDGE_IDS,
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
    # E45d63a96 DeckPicker.onCreate -> CollectionHelper
    # .exceededCursorSizeLimit (colOpen==false else-branch,
    # DeckPicker.java:430; permission granted, directory accessible).
    r.comment("collection-open probe (colOpen false branch)",
              edge="E45d63a96")
    # E37e55142 exceededCursorSizeLimit -> CollectionHelper.getCol
    # (CollectionHelper.java:126, inside the probe).
    r.comment("probe calls getCol", edge="E37e55142")
    # E4c7e034e getCol -> Storage.Collection (CollectionHelper
    # .java:99, when not already open).
    r.dwell(edge="E4c7e034e", seconds=5)
    # Eda786c6a Storage.Collection -> Storage._upgrade (old-schema
    # condition, Storage.java:65-67).
    r.comment("old schema -> _upgrade", edge="Eda786c6a")
    # E9ce50a2f _upgrade -> Models.save(JSONObject) (Storage
    # .java:227 upgrade block, per model).
    r.comment("upgrade saves each model", edge="E9ce50a2f")
    # E8c772cd2 save(JSONObject) -> save(JSONObject,boolean)
    # (Models.java:174).
    r.comment("save delegates", edge="E8c772cd2")
    # E2fe95109 save(JSONObject,boolean) -> _updateRequired
    # (Models.java:189, non-zero-id condition).
    r.comment("_updateRequired (non-zero model id)", edge="E2fe95109")
    # Ed609aaee _updateRequired -> _reqForTemplate (Models.java:1056,
    # per template).
    r.comment("_reqForTemplate", edge="Ed609aaee")
    # E61c27691 _reqForTemplate -> Collection._renderQA(Object[])
    # (Models.java:1082, :1085, :1095, :1105; synthetic field values
    # at :1079, :1082).
    r.comment("_renderQA with synthetic values", edge="E61c27691")
    # E1eb126ee _renderQA(Object[]) -> _renderQA(Object[],String,
    # String) (Collection.java:962).
    r.comment("_renderQA overload", edge="E1eb126ee")
    # Ef0029247 _renderQA -> Template.render (Collection.java:1009,
    # new Template(format, fields).render()).
    r.comment("Template.render", edge="Ef0029247")
    # Ef3d963e0 render -> render_tags (Template.java:89).
    r.comment("render_tags", edge="Ef3d963e0")
    # E82c9f13e render_tags -> render_unescaped (Template.java:
    # 169-170, untyped tag).
    r.comment("render_unescaped", edge="E82c9f13e")
    # Ef98eff28 render_unescaped -> Template$1.compare (target;
    # Template.java:199-200 first lookup null, :209-218 multi-part
    # tag with >= 2 modifiers and absent field, :229 sort; JDK sort
    # dispatch INFERRED; non-cloze condition matches Collection
    # .java:986-990 STD branch).
    r.comment("tag sort calls Template$1.compare (target; JDK "
              "dispatch INFERRED)", edge="Ef98eff28")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
