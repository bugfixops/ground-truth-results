#!/usr/bin/env python3
"""AmazeFileManager route_24: ThemedImageView.getActivity.

Method: ThemedImageView.getActivity
Edge ids in order:
    Ebe9ec603 E4d630b84 E5028d221 Eecbda88f Ef8df1bc2 E678e912e
    E5c3e8784 E999ff49e E8048d85b E0bcc7226
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ThemedImageView.getActivity.txt, verdict REACHABLE, 10 edges.
    Edge list identical to methods.csv route_edge_ids for
    ThemedImageView.getActivity. The D1 draft's third edge was the
    pre-B6-fix id Ed6562688; the B6 citation/trigger corrections
    renumbered it to E5028d221 (edge ids hash their content, see
    build_graph.py assign_ids), so the draft id is stale here.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE only (the
    app's declared set), pre-granted by run_app.sh (the bookmark
    database that this route depends on lives under app storage).
Fixtures: none. Setup: MainActivity must run first in this script
    (see the state note below); no fixture file is needed.
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions.

Mapping notes (printed source):
  - PRINT-CITATION CORRECTION, edge E5028d221: the print cites
    PrefFrag.java:221 for PrefFrag.onPreferenceClick ->
    PreferencesActivity.selectItem, but line 221 is the
    FRAGMENT_ADVANCED_SEARCH case, which loads AdvancedSearchPref,
    not the FoldersPref of the next printed edge. The only click
    consistent with the next edge (PreferencesActivity.java:261,
    loadPrefFragment(new FoldersPref())) is the FRAGMENT_FOLDERS
    case at PrefFrag.java:211-213, key "sidebar_folders"
    (PreferencesConstants.java:12), preference title "Shortcuts"
    (res/xml/preferences.xml:57-60, res/values/strings.xml:525).
    This script therefore taps "Shortcuts", NOT "Advanced Search".
    The edge list itself is unchanged; only the step-3 line
    citation in the print points at the wrong switch case.
  - STATE REQUIREMENT: FoldersPref.onCreate creates a
    PathSwitchPreference only for each entry of
    dataUtils.getBooks() (FoldersPref.java:58-59). Books are
    populated by MainActivity: on first run MainActivity adds the
    common bookmarks (MainActivity.java:358-361 ->
    UtilsHandler.addCommonBookmarks, DCIM/Downloads/Movies/Music/
    Pictures) and the async load sets them into DataUtils
    (MainActivity.java:373, setBooks(getBookmarksList())).
    Launching PreferencesActivity directly in a fresh process
    would leave getBooks() empty and the chain would never reach
    PathSwitchPreference. So this script launches MainActivity
    first (logged under the entry edge, with the drawer Settings
    navigation in the same block), then taps "Shortcuts".
  - Drawer "Settings" row: Drawer.java:435-442 starts
    PreferencesActivity (and finishes MainActivity);
    PreferencesActivity.onCreate with no extras calls
    selectItem(START_PREFERENCE = 0), which loads PrefFrag
    (PreferencesActivity.java:92-96, 255). The "Settings" row
    text is R.string.setting = "Settings"
    (res/values/strings.xml:31); the drawer is opened via the
    toggle content-desc "Open navigation drawer"
    (Drawer.java:217-224, res/values/strings.xml:25).
  - "Shortcuts" preference dependency: preferences.xml:58 makes
    sidebar_folders depend on sidebar_folders_enable, whose
    default value is true (preferences.xml:53-56), so the row is
    enabled on a fresh install; the script scrolls to it before
    tapping because the settings list is longer than one screen.
  - Target construction chain (all framework, no further taps):
    PathSwitchPreference.onCreateView sets the widget layout
    (PathSwitchPreference.java:28-29); the framework inflates
    ThemedImageButton from res/layout/namepathswitch_preference.xml
    :10,19; ThemedImageButton(Context, AttributeSet) calls
    super (ThemedImageButton.java:18-20); ThemedImageView
    (Context, AttributeSet) delegates to the 3-arg constructor
    (ThemedImageView.java:25-27); the 3-arg constructor calls
    getActivity() (ThemedImageView.java:29-32). No fixed
    coordinates are used anywhere in this script.
"""

import argparse
import os
import sys

# Locate the app root (the directory containing device/harness/)
# from wherever this script is checked out: the helper output dir
# or the merged device/routes/AmazeFileManager/ location. The
# template's fixed four-dirname climb assumes only the merged
# location, so this ancestor search replaces it.
_here = os.path.dirname(os.path.abspath(__file__))
_root = _here
while not os.path.exists(os.path.join(_root, "device", "harness",
                                      "harness.py")):
    _parent = os.path.dirname(_root)
    if _parent == _root:
        raise RuntimeError("device/harness/harness.py not found above %s"
                           % _here)
    _root = _parent
sys.path.insert(0, _root)
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ebe9ec603", "E4d630b84", "E5028d221", "Eecbda88f", "Ef8df1bc2",
    "E678e912e", "E5c3e8784", "E999ff49e", "E8048d85b", "E0bcc7226",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_24")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_24", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ebe9ec603 S_ENTRY -> PrefFrag.onCreate: MainActivity must run
    # first so the bookmark list is seeded (MainActivity.java:358
    # -361, 373), then the drawer "Settings" row starts
    # PreferencesActivity (Drawer.java:435-442), whose onCreate
    # loads PrefFrag via selectItem(0) (PreferencesActivity.java:
    # 92-96, 255). The MainActivity launch and drawer navigation
    # are logged under this entry edge; PrefFrag.onCreate itself
    # is framework-driven after PreferencesActivity starts.
    r.launch(args.package + "/com.amaze.filemanager.activities.MainActivity", "Ebe9ec603")
    r.tap("Ebe9ec603", desc="Open navigation drawer")
    r.scroll_to("Ebe9ec603", text="Settings")
    r.tap("Ebe9ec603", text="Settings")
    r.comment("PreferencesActivity selectItem(0) loads PrefFrag",
              "Ebe9ec603")
    # E4d630b84 PrefFrag.onCreate -> PrefFrag.onPreferenceClick:
    # PrefFrag registers this listener on every PREFERENCE_KEYS
    # entry (PrefFrag.java:89). Tap the "Shortcuts" preference
    # (key sidebar_folders, preferences.xml:57-60). See the
    # header note: the print's line-221 citation is the wrong
    # switch case; the FOLDERS case at PrefFrag.java:211-213 is
    # the one consistent with the next edge.
    r.scroll_to("E4d630b84", text="Shortcuts")
    r.tap("E4d630b84", text="Shortcuts")
    # E5028d221 PrefFrag.onPreferenceClick ->
    # PreferencesActivity.selectItem: the FRAGMENT_FOLDERS case
    # calls selectItem(FOLDERS_PREFERENCE) (PrefFrag.java:211-213).
    # Automatic after the tap; no further action.
    r.comment("FRAGMENT_FOLDERS case calls selectItem(FOLDERS)",
              "E5028d221")
    # Eecbda88f PreferencesActivity.selectItem -> FoldersPref.onCreate:
    # selectItem loads FoldersPref (PreferencesActivity.java:261)
    # and the framework runs its onCreate. No user action.
    r.comment("loadPrefFragment(FoldersPref); onCreate runs",
              "Eecbda88f")
    # Ef8df1bc2 FoldersPref.onCreate -> PathSwitchPreference.<init>:
    # the onCreate loop constructs one PathSwitchPreference per
    # bookmark (FoldersPref.java:58-59). Automatic; no user action.
    # (Requires the MainActivity-first seeding in the first block:
    # with an empty book list this loop constructs nothing.)
    r.comment("onCreate loop constructs PathSwitchPreference",
              "Ef8df1bc2")
    # E678e912e PathSwitchPreference.<init> ->
    # PathSwitchPreference.onCreateView: onCreateView sets the
    # widget layout resource (PathSwitchPreference.java:28-29).
    # Framework; no user action.
    r.comment("onCreateView sets widget layout", "E678e912e")
    # E5c3e8784 PathSwitchPreference.onCreateView ->
    # ThemedImageButton.<init>(Context,AttributeSet): the framework
    # inflates ThemedImageButton from
    # res/layout/namepathswitch_preference.xml:10,19. No action.
    r.comment("framework inflates ThemedImageButton from widget layout",
              "E5c3e8784")
    # E999ff49e ThemedImageButton.<init>(Context,AttributeSet) ->
    # ThemedImageView.<init>(Context,AttributeSet): the button
    # constructor calls super (ThemedImageButton.java:18-20).
    # No user action.
    r.comment("ThemedImageButton constructor calls super", "E999ff49e")
    # E8048d85b ThemedImageView.<init>(Context,AttributeSet) ->
    # ThemedImageView.<init>(Context,AttributeSet,int): the 2-arg
    # constructor delegates with defStyleAttr 0
    # (ThemedImageView.java:25-27). No user action.
    r.comment("2-arg constructor delegates to 3-arg constructor",
              "E8048d85b")
    # E0bcc7226 ThemedImageView.<init>(Context,AttributeSet,int) ->
    # ThemedImageView.getActivity: the 3-arg constructor calls
    # getActivity() (ThemedImageView.java:29-32). This is the
    # target edge; framework construction, no user action.
    r.comment("3-arg constructor calls getActivity()", "E0bcc7226")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
