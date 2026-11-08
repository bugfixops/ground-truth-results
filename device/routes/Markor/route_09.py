"""Device route script for Markor route_09.

Method: CsvConfig.findChar
Edges (in order): E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594
    E659e191c E0ecb8e4d E54b4aedd E80c409ce Ea2691dfc E7500999c
    E79e44db6 E4d1b7116 Ef62c7355 E20914758 Ecd6e481c Eabc206d6
    E254ddb97 Ef8f3e6a3
Printed route file: graphs/Markor/scratch/route_print/route_09.txt
ROUTES.csv permissions: none
ROUTES.csv fixtures: Documents/table.csv (the CSV-format document;
    its comma-separated rows drive CsvConfig.infer/findChar)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Path in words: cold-start MainActivity, notebook tab, tap the To-Do
bottom tab, switch the open document's format to CSV, switch to View
Mode (preview), then tap Reload. Reload calls loadDocument, which in
preview mode calls updateViewModeText, which converts with the CSV
converter: CsvTextConverter -> Csv2MdTable -> inferCsvConfiguration ->
CsvConfig.infer -> findChar. The format switch and the View Mode switch
are prerequisites for the Reload edge: the format menu is only visible
in edit mode (DocumentEditAndViewFragment.java:322) and
updateViewModeText only runs when preview is visible (lines 410-412).
No pm clear and no fixture push here: run_app.sh does both.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "harness"))
from harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_09",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E54b4aedd",
                         "E80c409ce", "Ea2691dfc", "E7500999c", "E79e44db6",
                         "E4d1b7116", "Ef62c7355", "E20914758", "Ecd6e481c",
                         "Eabc206d6", "E254ddb97", "Ef8f3e6a3"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E211966cc -- Tap the Markor launcher icon (process starts).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch(args.package + "/net.gsantner.markor.activity.MainActivity", "E211966cc")
    # Ed6414d9f -- The system calls Application.onCreate.
    # No user action: framework lifecycle step.
    # E0254b914 -- The MAIN / LAUNCHER intent starts MainActivity.
    # No separate action: the launch above already started it.
    # Ed25af8f4 -- The system calls Activity.onCreate.
    # No user action: framework lifecycle step.
    # Eba46a594 -- The system calls Activity.onStart then onResume.
    # No user action: framework lifecycle step.
    # E659e191c -- Activity.performResume calls onPostResume.
    # No user action: framework lifecycle step.
    # E0ecb8e4d -- The notebook tab is the default startup tab (position 0).
    # No user action: the notebook page is already visible after cold start
    # (MainActivity.java:105-106).
    # E54b4aedd -- Tap a bottom navigation tab.
    # Bottom-nav title @string/todo is "To-Do"
    # (res/values/string-not_translatable.xml:42); the listener selects the
    # tab position (MainActivity.java:109-114).
    r.tap("E54b4aedd", text="To-Do")
    # E80c409ce -- Tab Todo is shown (the listener selects its position).
    # No user action: pager state following the tab tap.
    # Ea2691dfc -- Tap an item of the editor menu (todo or quick note).
    # The implementing tap is Reload (action_reload case, which calls
    # loadDocument: DocumentEditAndViewFragment.java:447-451; menu title
    # @string/reload is "Reload", res/values/strings.xml:339).
    # Prerequisites, in order (all still in edit mode at this point):
    # 1. Switch the document format to CSV: overflow menu -> File Settings
    #    (submenu_per_file_settings title @string/file_settings is
    #    "File Settings", res/values/strings.xml:436) -> Format
    #    (submenu_format_selection title @string/format is "Format",
    #    res/values/strings.xml:159) -> CSV (title @string/csv is "CSV",
    #    res/values/string-not_translatable.xml:442). The format case sets
    #    the document format (DocumentEditAndViewFragment.java:533-538).
    # 2. Switch to View Mode (action_preview case, lines 454-456; menu
    #    title @string/view_mode is "View Mode", res/values/strings.xml:
    #    326), so loadDocument reaches updateViewModeText (lines 410-412).
    r.tap("Ea2691dfc", desc="More options")
    r.tap("Ea2691dfc", text="File Settings")
    r.tap("Ea2691dfc", text="Format")
    r.tap("Ea2691dfc", text="CSV")
    r.tap("Ea2691dfc", desc="View Mode")
    r.tap("Ea2691dfc", desc="More options")
    r.tap("Ea2691dfc", text="Reload")
    # E7500999c -- Direct call to loadDocument.
    # No user action: follows from the Reload tap above.
    # E79e44db6 -- Direct call to updateViewModeText.
    # No user action: follows from the Reload tap above (preview visible).
    # E4d1b7116 -- Direct call to convertMarkupShowInWebView.
    # No user action: follows from the Reload tap above.
    # Ef62c7355 -- The view mode converts with the format's converter (CSV).
    # No user action: converter dispatch following the Reload tap above.
    # E20914758 -- Direct call to Csv2MdTable.toMdTable(String).
    # No user action: follows from the Reload tap above.
    # Ecd6e481c -- Direct call to Csv2MdTable.toMdTable(Reader).
    # No user action: follows from the Reload tap above.
    # Eabc206d6 -- Direct call to inferCsvConfiguration.
    # No user action: follows from the Reload tap above.
    # E254ddb97 -- Direct call to CsvConfig.infer.
    # No user action: follows from the Reload tap above.
    # Ef8f3e6a3 -- Direct call to CsvConfig.findChar (target method).
    # No user action: follows from the Reload tap above.
    r.done()


if __name__ == "__main__":
    main()
