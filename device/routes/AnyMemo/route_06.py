#!/usr/bin/env python3
"""AnyMemo route_06: AudioRecorderFragment$2.<init>.

Method: AudioRecorderFragment$2.<init>
Edge ids in order:
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f Ea1b5c440 E22318784
    E2d07d42a E42afebab E539b41d9 E05e70ac4 Ede1d5ab9 E5cf2c281
    Ea4753c40 E5812ddc2 E30dd07f0 E7f487619 Ed271d628 E6812ae7d
    E1db89445 E4952317e E3709767c E1dfcf6c5 E1530f576 E7dcb0d1b
    Ed07c913c Edd0ac1e6 E95321333 E8cdc9c54 E3d39120b E4ebfb28f
    E158bd2be
Printed route: graphs/AnyMemo/scratch/route_print/AudioRecorderFragment_2.<init>.txt
Permissions (ROUTES.csv, granted by run_app.sh before this script runs):
    android.permission.WRITE_EXTERNAL_STORAGE
    android.permission.RECORD_AUDIO
Fixtures: none.
Setup: none pushed by run_app.sh. First launch auto-creates state:
    AnyMemo.prepareFirstTimeRun copies the bundled sample database
    (french-body-parts.db) to the app's external files anymemo folder
    and registers it as recent path 0 (ui/AnyMemo.java:315-321). A
    fresh install also shows the "New version installed" dialog; the
    script taps OK to dismiss it. The card edited later comes from
    that sample database via the merger/PreviewEdit/card-list chain;
    no card is created by hand.

Selector notes (all read from layout XML, strings.xml, or source):
  - Bottom navigation: menu/main_tab_items.xml id misc_tab_menu.
  - Misc tab Merge button: layout/misc_tab.xml id misc_merge.
  - Database Merger Merge button: layout/merge_layout.xml id
    merge_button.
  - Preview/Edit "Card list" menu item: menu/preview_edit_activity_menu.xml
    id editmenu_list_id (title "Card list", strings.xml
    list_mode_text). It is an ifRoom item, so the script first tries
    it directly and falls back to the overflow menu ("More options"
    content description on AOSP) if the direct tap finds nothing.
  - Card list long-press: layout/card_list_item.xml id item_question
    (CardListActivity.java:214 anchors the popup on the row's
    question view; the long-press listener is listItemLongClickListener
    at CardListActivity.java:437-445). The first matching row in
    document order is the first card of the list.
  - Long-press popup Edit item: menu/card_list_long_click_popup_menu.xml
    id edit with title "Edit" (strings.xml edit_text); it starts
    CardEditor for the card (CardListActivity.java:223-224,236-241).
  - Card editor question field: layout/card_editor_layout.xml id
    edit_dialog_question_entry; tapping it focuses the question edit,
    which is required for the audio menu item (CardEditor.java:192-194
    requires the focused view to be the question or answer edit, and
    the field must not already contain an audio reference).
  - Card editor audio menu item: menu/card_editor_menu.xml id
    add_new_audio, title "Add new audio" (strings.xml
    add_new_audio_text); it is an overflow item, reached through the
    "More options" overflow.
  - Audio recorder dialog: layout/recorder.xml ids record_button,
    play_button, save_button (AudioRecorderFragment.java:99-108).
    Play starts disabled and is enabled only after a recording is
    stopped, so the script taps Record, then Record again to stop,
    then Play; the Play tap is the action of the printed dialog edge,
    and startPlaying creates the target completion listener.
  - The target edge itself (startPlaying -> $2.<init>) is the
    MediaPlayer completion listener created in startPlaying; it fires
    when the short recording finishes playing, so it is logged as a
    comment after the Play tap, not as a further tap.

Caveat (see REPORT.md): as with route_01, the printed chain splices
    a Misc-tab DatabaseMerger entry onto a PreviewEditActivity result
    tail, but in this source a Misc-tab launch starts DatabaseMerger
    with no extras and does not return a result to PreviewEditActivity;
    the result-returning entry is PreviewEdit's own merge-db menu
    item. The script follows the printed edges as written; the tail
    (PreviewEdit -> card list -> editor -> recorder) may not be
    reachable in a real run from the Misc-tab entry point.
"""

import argparse
import importlib.util
import os
import sys


def _load_runner():
    """Find harness.py: walk up from this file, else the stage copy."""
    node = os.path.dirname(os.path.abspath(__file__))
    candidates = []
    while True:
        candidates.append(os.path.join(node, "harness", "harness.py"))
        parent = os.path.dirname(node)
        if parent == node:
            break
        node = parent
    for path in candidates:
        if os.path.isfile(path):
            spec = importlib.util.spec_from_file_location("device_harness", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.Runner
    raise ImportError("harness.py not found in any candidate location")


Runner = _load_runner()

EDGE_IDS = [
    "Eddc920eb", "Ee33f0797", "E0b0115b9", "Ed9aa2280", "Efe6c7871",
    "E006becde", "E48c9d4a5", "Ef4267162", "E25e1518b", "E690f7694",
    "E6da90567", "E41662266", "Eb655c6eb", "E705abaec", "Eee3d301b",
    "E3ae14c6f", "Ea1b5c440", "E22318784", "E2d07d42a", "E42afebab",
    "E539b41d9", "E05e70ac4", "Ede1d5ab9", "E5cf2c281", "Ea4753c40",
    "E5812ddc2", "E30dd07f0", "E7f487619", "Ed271d628", "E6812ae7d",
    "E1db89445", "E4952317e", "E3709767c", "E1dfcf6c5", "E1530f576",
    "E7dcb0d1b", "Ed07c913c", "Edd0ac1e6", "E95321333", "E8cdc9c54",
    "E3d39120b", "E4ebfb28f", "E158bd2be",
]

PKG_COMPONENT = ("org.liberty.android.fantastischmemopro/"
                 "org.liberty.android.fantastischmemo.ui.AnyMemo")


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_06 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_06", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Eddc920eb S_ENTRY -> AnyMemo.<init>: launch the MAIN/LAUNCHER
    # activity. A fresh install shows the "New version installed"
    # dialog on top of it; tap OK (strings.xml ok_text) to dismiss.
    r.launch(PKG_COMPONENT, "Eddc920eb")
    r.tap("Eddc920eb", text="OK")
    # Ee33f0797 AnyMemo.<init> -> AnyMemo.onCreate: framework.
    r.comment("system instantiates AnyMemo, then onCreate", "Ee33f0797")
    # E0b0115b9 AnyMemo.onCreate -> AnyMemo.loadUiComponents: granted
    # WRITE_EXTERNAL_STORAGE by run_app.sh; framework/call, no action.
    r.comment("loadUiComponents runs (permission pre-granted)", "E0b0115b9")
    # Ed9aa2280 AnyMemo.loadUiComponents -> AnyMemo.initDrawer: call.
    r.comment("initDrawer runs", "Ed9aa2280")
    # Efe6c7871 AnyMemo.initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT:
    # cold-start selection of the Recent tab (AnyMemo.java:263).
    r.comment("cold-start selects the Recent tab", "Efe6c7871")
    # E006becde AnyMemo$2.onNavigationItemSelected@INIT -> RecentListFragment.<init>.
    r.comment("RecentListFragment created for the Recent tab", "E006becde")
    # E48c9d4a5 RecentListFragment.<init> -> RecentListFragment.onAttach.
    r.comment("fragment onAttach", "E48c9d4a5")
    # Ef4267162 RecentListFragment.onAttach -> RecentListFragment.onCreate.
    r.comment("fragment onCreate", "Ef4267162")
    # E25e1518b RecentListFragment.onCreate -> RecentListFragment.onCreateView.
    r.comment("fragment onCreateView", "E25e1518b")
    # E690f7694 RecentListFragment.onCreateView -> S_MAIN_RECENT.
    r.comment("Recent tab page entered", "E690f7694")
    # E6da90567 S_MAIN_RECENT -> AnyMemo$2.onNavigationItemSelected:
    # tap the Misc bottom-navigation item.
    r.tap("E6da90567", res_id="misc_tab_menu")
    # E41662266 AnyMemo$2.onNavigationItemSelected -> MiscTabFragment.<init>:
    # itemId == misc_tab_menu branch (AnyMemo.java:249-250).
    r.comment("MiscTabFragment created for the Misc tab", "E41662266")
    # Eb655c6eb MiscTabFragment.<init> -> MiscTabFragment.onAttach.
    r.comment("fragment onAttach", "Eb655c6eb")
    # E705abaec MiscTabFragment.onAttach -> MiscTabFragment.onCreate.
    r.comment("fragment onCreate", "E705abaec")
    # Eee3d301b MiscTabFragment.onCreate -> MiscTabFragment.onCreateView.
    r.comment("fragment onCreateView (misc_tab layout)", "Eee3d301b")
    # E3ae14c6f MiscTabFragment.onCreateView -> MiscTabFragment.onClick:
    # tap the Merge DB button on the Misc tab.
    r.tap("E3ae14c6f", res_id="misc_merge")
    # Ea1b5c440 MiscTabFragment.onClick -> DatabaseMerger.<init>:
    # v == mergeButton branch starts DatabaseMerger.
    r.comment("mergeButton branch starts DatabaseMerger", "Ea1b5c440")
    # E22318784 DatabaseMerger.<init> -> DatabaseMerger.onCreate.
    r.comment("DatabaseMerger onCreate", "E22318784")
    # E2d07d42a DatabaseMerger.onCreate -> S_DB_MERGER.
    r.comment("Database Merger page entered", "E2d07d42a")
    # E42afebab S_DB_MERGER -> DatabaseMerger.onClick: tap Merge.
    r.tap("E42afebab", res_id="merge_button")
    # E539b41d9 DatabaseMerger.onClick -> DatabaseMerger$1.doHeavyTask:
    # v == mergeButton branch runs the merge progress task.
    r.comment("merge progress task runs (doHeavyTask)", "E539b41d9")
    # E05e70ac4 DatabaseMerger$1.doHeavyTask -> DatabaseMerger$1.doUITask.
    r.comment("merge task finishes, doUITask runs", "E05e70ac4")
    # Ede1d5ab9 DatabaseMerger$1.doUITask -> PreviewEditActivity.onActivityResult.
    r.comment("merge result returns to PreviewEditActivity", "Ede1d5ab9")
    # E5cf2c281 PreviewEditActivity.onActivityResult -> S_PREVIEW_EDIT.
    r.comment("Preview/Edit page entered (restartActivity)", "E5cf2c281")
    # Ea4753c40 S_PREVIEW_EDIT -> PreviewEditActivity.onOptionsItemSelected:
    # tap the Card list menu item. It is an ifRoom item, so try it
    # directly; if it is only in the overflow, open the overflow and
    # tap it there. (In dry mode the first tap is planned and the
    # fallback never runs.)
    try:
        r.tap("Ea4753c40", res_id="editmenu_list_id")
    except Exception:
        r.tap("Ea4753c40", desc="More options")
        r.tap("Ea4753c40", res_id="editmenu_list_id")
    # E5812ddc2 PreviewEditActivity.onOptionsItemSelected -> S_CARD_LIST:
    # the list-mode branch starts CardListActivity.
    r.comment("card list page entered", "E5812ddc2")
    # E30dd07f0 S_CARD_LIST -> CardListActivity$10.onItemLongClick:
    # long-press the first card row (question view of the first row).
    r.long_tap("E30dd07f0", res_id="item_question")
    # E7f487619 CardListActivity$10.onItemLongClick ->
    # CardListActivity.showListItemLongClickPopup: call.
    r.comment("long-press popup shown for the card", "E7f487619")
    # Ed271d628 CardListActivity.showListItemLongClickPopup ->
    # CardListActivity$2.onMenuItemClick: tap the Edit popup item.
    r.tap("Ed271d628", text="Edit")
    # E6812ae7d CardListActivity$2.onMenuItemClick -> CardEditor.<init>:
    # the edit branch starts CardEditor for the card.
    r.comment("CardEditor started for the card", "E6812ae7d")
    # E1db89445 CardEditor.<init> -> CardEditor.onCreate.
    r.comment("CardEditor onCreate", "E1db89445")
    # E4952317e CardEditor.onCreate -> CardEditor$InitTask.doInBackground:
    # async card load.
    r.comment("card loads in the background", "E4952317e")
    # E3709767c CardEditor$InitTask.doInBackground ->
    # CardEditor$InitTask.onPostExecute: async.
    r.comment("card loaded", "E3709767c")
    # E1dfcf6c5 CardEditor$InitTask.onPostExecute -> S_CARD_EDITOR.
    r.comment("card editor page entered", "E1dfcf6c5")
    # E1530f576 S_CARD_EDITOR -> CardEditor.onOptionsItemSelected:
    # focus the question edit (required for the audio menu item),
    # then open the overflow and tap Add new audio.
    r.tap("E1530f576", res_id="edit_dialog_question_entry")
    r.tap("E1530f576", desc="More options")
    r.tap("E1530f576", text="Add new audio")
    # E7dcb0d1b CardEditor.onOptionsItemSelected -> CardEditor.addNewAudio:
    # the add_new_audio branch runs.
    r.comment("addNewAudio runs for the focused field", "E7dcb0d1b")
    # Ed07c913c CardEditor.addNewAudio ->
    # CardEditor.startAudioRecorderWithPermissionCheck: the field has
    # no audio reference yet, so the permission check runs.
    r.comment("audio permission check runs", "Ed07c913c")
    # Edd0ac1e6 CardEditor.startAudioRecorderWithPermissionCheck ->
    # CardEditor.startAudioRecorder: RECORD_AUDIO pre-granted by
    # run_app.sh, so no request is made.
    r.comment("recorder started (permission pre-granted)", "Edd0ac1e6")
    # E95321333 CardEditor.startAudioRecorder -> S_DLG_AUDIO_RECORDER:
    # the recorder dialog is shown for the focused field.
    r.comment("audio recorder dialog entered", "E95321333")
    # E8cdc9c54 S_DLG_AUDIO_RECORDER -> AudioRecorderFragment$1.onClick:
    # Record, then Record again to stop (Play is disabled until a
    # recording exists), then Play. The Play tap is the action of
    # this edge; the two Record taps are its preconditions.
    r.tap("E8cdc9c54", res_id="record_button")
    r.tap("E8cdc9c54", res_id="record_button")
    r.tap("E8cdc9c54", res_id="play_button")
    # E3d39120b AudioRecorderFragment$1.onClick -> AudioRecorderFragment.onPlay:
    # the Play tap toggles playback on.
    r.comment("playback started", "E3d39120b")
    # E4ebfb28f AudioRecorderFragment.onPlay -> AudioRecorderFragment.startPlaying:
    # start is true, so startPlaying runs.
    r.comment("startPlaying runs", "E4ebfb28f")
    # E158bd2be AudioRecorderFragment.startPlaying ->
    # AudioRecorderFragment$2.<init>: target edge; the completion
    # listener is created in startPlaying and fires when the short
    # recording finishes playing (async, no further tap).
    r.comment("target: playback completion listener created", "E158bd2be")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
