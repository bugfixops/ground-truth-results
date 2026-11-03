#!/usr/bin/env python3
"""AnyMemo route_11: Option.getCopyClipboard.

Method: Option.getCopyClipboard
Edge ids (in route order):
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 E6ae5fc6b Ee46c98e0 Ed2ab48e4 E9ba271ea E02065d3d
    Eafe0cb7b E1cb33bb0 E95db7dc7 E47abfdf7 E0b8a412e E43c9d046
    E82b481db E4309d5ec E32f3db39
Printed route file: graphs/AnyMemo/scratch/route_print/
    Option.getCopyClipboard.txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (granted by
    run_app.sh from ROUTES.csv; this script never grants it).
Fixtures: none.
Setup: fresh install (pm clear). The printed chain reaches
    Preview/Edit through DatabaseMerger: the Misc tab starts the
    merger, tapping Merge runs the merge task and finishes back to
    the Preview/Edit session, whose menu then opens the card player
    on the current card. The card player shows the front side and,
    under the default single-sided card style, displayCard(true)
    copies the card to the clipboard, which reads the copy option.
Caveat (see REPORT.md): a merger started from the Misc tab has
    empty target/source fields, and merging "" into "" raises
    IllegalArgumentException instead of finishing; the graph's
    Preview/Edit return assumes the merger was started from
    Preview/Edit with a db and card in session. A real run needs
    that session (or two distinct db paths set in the merger)
    before the card-player steps can run.
"""

import argparse
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
try:
    from device.harness import Runner
except ModuleNotFoundError:
    # Fallback for layouts where the repo root is not four levels up:
    # load harness.py from the nearest ancestor device/harness dir.
    _dir = os.path.dirname(os.path.abspath(__file__))
    _spec = None
    while True:
        for _cand in (os.path.join(_dir, "device", "harness", "harness.py"),
                      os.path.join(_dir, "harness", "harness.py")):
            if os.path.isfile(_cand):
                _spec = importlib.util.spec_from_file_location(
                    "device_harness", _cand)
                break
        if _spec is not None:
            break
        _parent = os.path.dirname(_dir)
        if _parent == _dir:
            raise
        _dir = _parent
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    Runner = _mod.Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_11",
               edge_ids=["Eddc920eb", "Ee33f0797", "E0b0115b9",
                         "Ed9aa2280", "Efe6c7871", "E006becde",
                         "E48c9d4a5", "Ef4267162", "E25e1518b",
                         "E690f7694", "E6da90567", "E41662266",
                         "Eb655c6eb", "E705abaec", "Eee3d301b",
                         "E3ae14c6f", "Ea1b5c440", "E22318784",
                         "E2d07d42a", "E42afebab", "E539b41d9",
                         "E05e70ac4", "Ede1d5ab9", "E5cf2c281",
                         "Ea4753c40", "E6ae5fc6b", "Ee46c98e0",
                         "Ed2ab48e4", "E9ba271ea", "E02065d3d",
                         "Eafe0cb7b", "E1cb33bb0", "E95db7dc7",
                         "E47abfdf7", "E0b8a412e", "E43c9d046",
                         "E82b481db", "E4309d5ec", "E32f3db39"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # Eddc920eb: MAIN / LAUNCHER intent starts AnyMemo.
        r.launch(args.package + "/org.liberty.android.fantastischmemo.ui.AnyMemo", edge="Eddc920eb")
        # Ee33f0797: system instantiates AnyMemo, then onCreate.
        r.comment("system instantiates AnyMemo, then calls onCreate",
                  edge="Ee33f0797")
        # E0b0115b9: onCreate, permission already granted, loadUiComponents.
        r.comment("WRITE_EXTERNAL_STORAGE granted by run_app.sh; "
                  "onCreate calls loadUiComponents", edge="E0b0115b9")
        # Ed9aa2280: loadUiComponents calls initDrawer.
        r.comment("loadUiComponents calls initDrawer", edge="Ed9aa2280")
        # Efe6c7871: bottomNavigation.setSelectedItemId(recent_tab_menu)
        # dispatches the listener, so the Recent tab is selected cold.
        r.comment("setSelectedItemId(recent_tab_menu) dispatches the "
                  "bottom-nav listener", edge="Efe6c7871")
        # E006becde: itemId == recent_tab_menu: new RecentListFragment.
        r.comment("itemId == recent_tab_menu: new RecentListFragment",
                  edge="E006becde")
        # E48c9d4a5: fragment lifecycle: onAttach.
        r.comment("RecentListFragment lifecycle: onAttach",
                  edge="E48c9d4a5")
        # Ef4267162: fragment lifecycle: onCreate.
        r.comment("RecentListFragment lifecycle: onCreate",
                  edge="Ef4267162")
        # E25e1518b: fragment lifecycle: onCreateView.
        r.comment("RecentListFragment lifecycle: onCreateView",
                  edge="E25e1518b")
        # E690f7694: the Recent tab is shown once its view exists.
        r.comment("Recent tab shown (S_MAIN_RECENT)", edge="E690f7694")
        # E6da90567: tap a bottom-navigation item; Misc tab title is
        # "Misc" (strings.xml misc_tab_text, menu main_tab_items.xml).
        r.tap(edge="E6da90567", desc="Misc")
        # E41662266: itemId == misc_tab_menu: new MiscTabFragment.
        r.comment("itemId == misc_tab_menu: new MiscTabFragment",
                  edge="E41662266")
        # Eb655c6eb: fragment lifecycle: onAttach.
        r.comment("MiscTabFragment lifecycle: onAttach", edge="Eb655c6eb")
        # E705abaec: fragment lifecycle: onCreate.
        r.comment("MiscTabFragment lifecycle: onCreate", edge="E705abaec")
        # Eee3d301b: fragment lifecycle: onCreateView (misc_tab.xml).
        r.comment("MiscTabFragment lifecycle: onCreateView",
                  edge="Eee3d301b")
        # E3ae14c6f: tap any Misc-tab button; v == mergeButton
        # (misc_tab.xml misc_merge) starts DatabaseMerger.
        r.tap(edge="E3ae14c6f", res_id="misc_merge")
        # Ea1b5c440: onClick starts DatabaseMerger.
        r.comment("v == mergeButton: startActivity(DatabaseMerger)",
                  edge="Ea1b5c440")
        # E22318784: activity lifecycle: onCreate.
        r.comment("DatabaseMerger lifecycle: onCreate", edge="E22318784")
        # E2d07d42a: setContentView(merge_layout) shows the merger.
        r.comment("setContentView(merge_layout) shows the merger",
                  edge="E2d07d42a")
        # E42afebab: tap a field or button in Database Merger;
        # v == mergeButton (merge_layout.xml merge_button) runs the
        # merge progress task.
        r.tap(edge="E42afebab", res_id="merge_button")
        # E539b41d9: v == mergeButton: doProgressTask, whose task
        # doHeavyTask merges target into source.
        r.comment("mergeButton: doProgressTask runs doHeavyTask",
                  edge="E539b41d9")
        # E05e70ac4: doProgressTask runs doHeavyTask on a background
        # thread, then posts doUITask to the main thread.
        r.comment("doHeavyTask finishes; doUITask posted to main",
                  edge="E05e70ac4")
        # Ede1d5ab9: doUITask sets RESULT_OK and finishes, so the
        # Preview/Edit starter gets its result (menu_context_merge_db).
        r.comment("doUITask sets RESULT_OK and finishes",
                  edge="Ede1d5ab9")
        # E5cf2c281: PreviewEdit onActivityResult restarts the
        # activity, showing Preview/Edit (S_PREVIEW_EDIT).
        r.comment("PreviewEdit onActivityResult restarts Preview/Edit",
                  edge="E5cf2c281")
        # Ea4753c40: tap a Preview/Edit toolbar/overflow menu item.
        # menu_card_player has no showAsAction, so it lives in the
        # overflow menu ("More options" is the framework overflow
        # affordance); its title is "Card player" (strings.xml
        # card_player_text, menu preview_edit_activity_menu.xml).
        r.tap(edge="Ea4753c40", desc="More options")
        r.tap(edge="Ea4753c40", text="Card player")
        # E6ae5fc6b: menu_card_player starts CardPlayerActivity for
        # the current card (S_CARD_PLAYER).
        r.comment("menu_card_player starts CardPlayerActivity",
                  edge="E6ae5fc6b")
        # Ee46c98e0: fragment lifecycle: CardPlayerFragment onCreate.
        r.comment("CardPlayerFragment lifecycle: onCreate",
                  edge="Ee46c98e0")
        # Ed2ab48e4: fragment lifecycle: onCreateView.
        r.comment("CardPlayerFragment lifecycle: onCreateView",
                  edge="Ed2ab48e4")
        # E9ba271ea: tap a Card Player control; v == playButton
        # (card_player_layout.xml card_player_play_button), not
        # already playing, starts playing.
        r.tap(edge="E9ba271ea", res_id="card_player_play_button")
        # E02065d3d: v == playButton, not already playing: startPlaying.
        r.comment("playButton not selected: startPlaying",
                  edge="E02065d3d")
        # Eafe0cb7b: startPlaying transitions the STOPPED state.
        r.comment("startPlaying transitions the STOPPED state",
                  edge="Eafe0cb7b")
        # E1cb33bb0: the state transition calls onPlayCard.
        r.comment("state transition calls onPlayCard", edge="E1cb33bb0")
        # E95db7dc7: onPlayCard broadcasts ACTION_GO_TO_CARD.
        r.comment("onPlayCard broadcasts ACTION_GO_TO_CARD",
                  edge="E95db7dc7")
        # E47abfdf7: the receiver calls gotoCardId (card id changed).
        r.comment("receiver calls gotoCardId", edge="E47abfdf7")
        # E0b8a412e: gotoCardId calls gotoCard.
        r.comment("gotoCardId calls gotoCard", edge="E0b8a412e")
        # E43c9d046: gotoCard calls updateCardFrontSide.
        r.comment("gotoCard calls updateCardFrontSide", edge="E43c9d046")
        # E82b481db: updateCardFrontSide calls displayCard; under
        # the default single-sided style it shows both sides
        # (displayCard(true)), which copies to the clipboard.
        r.comment("updateCardFrontSide calls displayCard",
                  edge="E82b481db")
        # E4309d5ec: displayCard(true) calls copyToClipboard.
        r.comment("displayCard(true) calls copyToClipboard",
                  edge="E4309d5ec")
        # E32f3db39: copyToClipboard reads the option: target
        # Option.getCopyClipboard.
        r.comment("copyToClipboard reads the option (target)",
                  edge="E32f3db39")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
