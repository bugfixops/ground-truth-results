#!/usr/bin/env python3
"""AnkiDroid route_10: Template$1.compare.

Target: Template$1.compare (anonymous Comparator in
    Template.render_unescaped tag sorting).
Table verdict: FIXED (first-draw verdict; this script drives the
    final BFS route from methods.csv, 15 edges).
Route followed: final BFS route, with one documented trigger
    substitution. The BFS head (updateDeckList -> launchDeckTask ->
    doInBackground -> doInBackgroundRenderBrowserQA) is the graph's
    cheapest head, but on a device the RENDER_BROWSER_QA task is
    genuinely launched by scrolling the CardBrowser list
    (CardBrowser.java:1156 scroll, :1170 scroll-state idle). The
    script therefore drives drawer -> CardBrowser -> scroll, and the
    tail edges from doInBackgroundRenderBrowserQA onward are exactly
    the BFS tail. The merger should confirm this substitution; if
    the BFS head is itself ruled a dispatch artifact, the script's
    trigger is the genuine one and only the head edges change.
Preconditions/fixtures (the F2 guard set):
  - Collection open (colOpen).
  - Fixture model: non-cloze, with at least one template; the card
    being rendered has a plain tag plus a multi-modifier tag whose
    field is absent from the context (txt == null,
    Template.java:201-206), with >= 2 modifiers so Collections.sort
    calls compare (Template.java:229-238). The rendered data are
    synthetic _reqForTemplate values, not a real note.
  - The scroll target text must be a card row visible in the
    CardBrowser list; set FIXTURE_CARD_TEXT from setup.
Mapping notes:
  - The drawer taps and the scroll are logged under the render edge
    E07ddaa6d, which is the edge they trigger; no graph edge exists
    for opening the drawer or for the scroll itself.
  - The "Navigate up" content description is the standard framework
    description; verify it against a live uiautomator dump before a
    real run.
Launcher: com.ichi2.anki/.IntentHandler (AndroidManifest.xml:81-89).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "E0b111c68",
    "E8b5d2971", "E460971ee", "Eba94fbde", "E07ddaa6d", "E6ae91770",
    "Ebcdf07cd", "Ef0029247", "Ef3d963e0", "E82c9f13e", "Ef98eff28",
]

# Card row text in the CardBrowser list, from the fixture model card.
# Set this to the fixture card's rendered text before a real run.
FIXTURE_CARD_TEXT = "FIXTURE_CARD_TEXT"


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
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("onStart -> onResume", edge="E553ad2d8")
    # E0b111c68 onResume -> updateDeckList.
    r.comment("deck list loads", edge="E0b111c68")
    # E8b5d2971 updateDeckList -> launchDeckTask (BFS head edge).
    r.comment("BFS head: launchDeckTask (see header: genuine trigger "
              "is the CardBrowser scroll below)", edge="E8b5d2971")
    # E460971ee launchDeckTask -> doInBackground.
    r.comment("DeckTask execute -> doInBackground", edge="E460971ee")
    # Eba94fbde doInBackground -> doInBackgroundRenderBrowserQA.
    r.comment("render task (genuinely launched by CardBrowser scroll)",
              edge="Eba94fbde")
    # E07ddaa6d doInBackgroundRenderBrowserQA ->
    # CardBrowser.updateSearchItemQA: open the drawer, open the
    # CardBrowser, and scroll its list to fire the render task.
    r.tap(edge="E07ddaa6d", desc="Navigate up")
    r.tap(edge="E07ddaa6d", text="Card browser")
    r.scroll_to(edge="E07ddaa6d", text=FIXTURE_CARD_TEXT)
    # E6ae91770 updateSearchItemQA -> Card._getQA(boolean,boolean).
    r.comment("render QA for the browser item", edge="E6ae91770")
    # Ebcdf07cd Card._getQA -> Collection._renderQA.
    r.comment("collection renders QA", edge="Ebcdf07cd")
    # Ef0029247 _renderQA -> Template.render.
    r.comment("Template.render", edge="Ef0029247")
    # Ef3d963e0 Template.render -> render_tags.
    r.comment("render_tags", edge="Ef3d963e0")
    # E82c9f13e render_tags -> render_unescaped.
    r.comment("render_unescaped", edge="E82c9f13e")
    # Ef98eff28 render_unescaped -> Template$1.compare (target;
    # fixture model conditions from the header must hold).
    r.comment("tag sort calls Template$1.compare (target)",
              edge="Ef98eff28")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
