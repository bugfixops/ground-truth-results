#!/usr/bin/env python3
"""Vanilla-Music route_01: FolderPickerAdapter$Item.<init>.

Method: FolderPickerAdapter$Item.<init>
Edge ids in order (ROUTES.csv row route_01, verbatim):
    E47380ade E29472d10 E80427a98 E65584de0 E95b25aef E38459d6f
    Ef8b94848 Eb3a597bc E46a6b4b8 E700804fd Ef4c93f9d Ed9dcf10e
    E47209207 E41c31ae6 Eedb6da33 Ebe51d2ec E1fd3fd5d E51844326
    E8dd51645 E3058ae6d
Printed route source: the FolderPickerAdapter$Item.<init> path row of
    graphs/Vanilla-Music/verification.csv (ref LibraryActivity.java:
    587-589; PreferencesActivity.java:69-74,185-192;
    FolderPickerActivity.java:68-93,168; FolderPickerAdapter.java:120,
    204) plus the route_01 row of device/routes/Vanilla-Music/
    ROUTES.csv. Steps read: launcher -> onResume@LibraryActivity ->
    S_LIBRARY -> tap the bottom bar overflow -> Settings -> tap
    "Library" header -> tap "Customize file browser start" ->
    FilebrowserStartActivity.onCreate -> setCurrentDir ->
    FolderPickerAdapter.setCurrentDir -> refresh -> new Item(...).
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none (ROUTES.csv fixtures column empty; no STATE file gate).
Setup: push fixtures/Music + media scan (run_app.sh does pm clear and
    the setup step before this script, so the script starts by
    launching the app).

UI mapping (layout XML and strings.xml read, nothing invented):
  - Launcher activity is LibraryActivity (AndroidManifest.xml:73-90,
    MAIN/LAUNCHER); component is <package>/.LibraryActivity.
  - The bottom-bar overflow button is created programmatically in
    BottomBarControls.enableOptionsMenu (BottomBarControls.java:
    156-181): getImageButton sets only a drawable and a background
    (lines 260-266), so the button has no id, text, or content-desc
    for the harness to find. The script therefore opens the menu
    with the MENU key instead: the framework options menu is
    populated by the same onCreateOptionsMenu that fills the popup
    (PlaybackActivity.java:401-405 adds MENU_PREFS with title
    R.string.settings), and tapping its "Settings" entry reaches the
    same onOptionsItemSelected@PREFS branch. See REPORT.md for the
    live-run risk and the fixed-coordinate fallback.
  - Overflow menu entry text "Settings" is R.string.settings
    (res/values/translatable.xml:31).
  - Settings header text is "Library screen": the header in
    res/xml/preference_headers.xml uses @string/library_screen
    (translatable.xml:232). The edge gui text says "Library"; the
    rendered text is "Library screen", so that is what is tapped.
  - The file-browser-start row title is "Filebrowser home":
    res/xml/preference_library.xml uses @string/filebrowser_start
    (translatable.xml:342) with summary @string/
    customize_filebrowser_start ("Filebrowser starts at this
    directory", translatable.xml:343) and an <intent> to
    FilebrowserStartActivity. The edge gui text says "Customize file
    browser start folder"; the rendered row title is "Filebrowser
    home", so that is what is tapped.
  - Folder picker open is proven by res_id "path_display", the
    EditText in res/layout/folderpicker_content.xml. FolderPicker
    refresh (which constructs the Item) runs inside setCurrentDir
    during FilebrowserStartActivity.onCreate, before the picker is
    shown, so reaching the picker proves the target edge ran.
"""

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E47380ade", "E29472d10", "E80427a98", "E65584de0", "E95b25aef",
    "E38459d6f", "Ef8b94848", "Eb3a597bc", "E46a6b4b8", "E700804fd",
    "Ef4c93f9d", "Ed9dcf10e", "E47209207", "E41c31ae6", "Eedb6da33",
    "Ebe51d2ec", "E1fd3fd5d", "E51844326", "E8dd51645", "E3058ae6d",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Vanilla-Music route_01")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_01", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E47380ade S_ENTRY -> LibraryActivity.<init>: MAIN / LAUNCHER
    # intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")
    # E29472d10 LibraryActivity.<init> ->
    # SlidingPlaybackActivity.onResume@LibraryActivity: Activity
    # lifecycle callback. No user action.
    r.comment("system resumes LibraryActivity", "E29472d10")
    # E80427a98 SlidingPlaybackActivity.onResume@LibraryActivity ->
    # S_LIBRARY: LibraryActivity is resumed and shown (default tab
    # Artists). Wait for the tab strip so the library is on screen
    # before opening the menu.
    r.wait_for("E80427a98", text="Artists")
    # E65584de0 S_LIBRARY -> BottomBarControls.onClick@POPUP: Tap the
    # overflow (three dots) button at the right end of the bottom
    # bar. That button has no id, text, or content-desc (see header),
    # so the MENU key opens the framework options menu populated by
    # the same onCreateOptionsMenu instead.
    r.key("MENU", "E65584de0")
    # E95b25aef BottomBarControls.onClick@POPUP ->
    # BottomBarControls.openMenu: call made in the click branch. The
    # menu opens automatically once the overflow/menu key is handled.
    r.comment("menu opens (openMenu / options menu panel)", "E95b25aef")
    # E38459d6f BottomBarControls.openMenu -> S_LIBRARY_MENU:
    # mPopupMenu.show(): the overflow menu is open. No user action.
    r.comment("overflow menu is open", "E38459d6f")
    # Ef8b94848 S_LIBRARY_MENU -> BottomBarControls.onMenuItemClick:
    # Tap an entry of the overflow menu.
    r.tap("Ef8b94848", text="Settings")
    # Eb3a597bc BottomBarControls.onMenuItemClick ->
    # PlaybackActivity.onOptionsItemSelected@PREFS: the item MENU_PREFS
    # of the overflow menu was tapped. Automatic after the tap.
    r.comment("MENU_PREFS branch selected", "Eb3a597bc")
    # E46a6b4b8 PlaybackActivity.onOptionsItemSelected@PREFS ->
    # PreferencesActivity.<init>: startActivity(new Intent(this,
    # PreferencesActivity.class)). Automatic after the tap.
    r.comment("startActivity PreferencesActivity intent", "E46a6b4b8")
    # E700804fd PreferencesActivity.<init> ->
    # PreferencesActivity.onCreate: Activity lifecycle callback.
    # No user action.
    r.comment("system creates PreferencesActivity", "E700804fd")
    # Ef4c93f9d PreferencesActivity.onCreate -> S_PREFS: the list of
    # settings headers is shown. No user action.
    r.comment("settings headers shown", "Ef4c93f9d")
    # Ed9dcf10e S_PREFS -> PreferencesActivity$LibraryFragment.<init>:
    # Tap the "Library" header. Rendered text is "Library screen"
    # (see header note).
    r.tap("Ed9dcf10e", text="Library screen")
    # E47209207 PreferencesActivity$LibraryFragment.<init> ->
    # PreferencesActivity$LibraryFragment.onCreate: Fragment lifecycle
    # callback. No user action.
    r.comment("LibraryFragment onCreate runs", "E47209207")
    # E41c31ae6 PreferencesActivity$LibraryFragment.onCreate ->
    # S_PREFS_LIBRARY: addPreferencesFromResource: the settings rows
    # of this section are shown. No user action.
    r.comment("Library section rows shown", "E41c31ae6")
    # Eedb6da33 S_PREFS_LIBRARY -> FilebrowserStartActivity.<init>:
    # tap "Customize file browser start": performClick starts the
    # Intent of the PreferenceScreen. Rendered row title is
    # "Filebrowser home" (see header note).
    r.tap("Eedb6da33", text="Filebrowser home")
    # Ebe51d2ec FilebrowserStartActivity.<init> ->
    # FilebrowserStartActivity.onCreate: Activity lifecycle callback.
    # No user action.
    r.comment("system creates FilebrowserStartActivity", "Ebe51d2ec")
    # E1fd3fd5d FilebrowserStartActivity.onCreate ->
    # FolderPickerActivity.setCurrentDir: Direct call. Automatic in
    # onCreate.
    r.comment("onCreate calls setCurrentDir", "E1fd3fd5d")
    # E51844326 FolderPickerActivity.setCurrentDir ->
    # FolderPickerAdapter.setCurrentDir: Direct call. Automatic.
    r.comment("adapter setCurrentDir called", "E51844326")
    # E8dd51645 FolderPickerAdapter.setCurrentDir ->
    # FolderPickerAdapter.refresh: Direct call. Automatic.
    r.comment("adapter refresh runs", "E8dd51645")
    # E3058ae6d FolderPickerAdapter.refresh ->
    # FolderPickerAdapter$Item.<init>: Direct call. Refresh builds one
    # Item per directory entry; reaching the folder picker (path
    # display visible) proves refresh ran.
    r.wait_for("E3058ae6d", res_id="path_display")
    r.screenshot("folder_picker", "E3058ae6d")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
