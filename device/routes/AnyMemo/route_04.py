#!/usr/bin/env python3
"""AnyMemo route_04: Mnemosyne2CardsImporter$ValueType.<clinit>.

Method: Mnemosyne2CardsImporter$ValueType.<clinit>
Edge ids in order:
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 E41662266
    Eb655c6eb E705abaec Eee3d301b E3ae14c6f E4d455e8e E06cb551e
    Ee7fb6e62 E293210fe E09df7003 E6d22692a Ea6b99e70 E1b342eec
    E4bc3be81 E3edbc981 Eece3b07c E9c19e28c E12bd28f7 Ef94688d7
    E92ea72a0 E81e8b1b7 E835f2200 E94b69705 E50df8fb0 E49950861
    Eed16c0fe
Printed route: graphs/AnyMemo/scratch/route_print/Mnemosyne2CardsImporter_ValueType.<clinit>.txt
Permissions (ROUTES.csv, granted by run_app.sh before this script runs):
    android.permission.WRITE_EXTERNAL_STORAGE
Fixtures (ROUTES.csv, pushed by run_app.sh to /sdcard/<fixture>):
    Download/sample_deck.apkg
Setup: none. First launch auto-creates state: AnyMemo.prepareFirstTimeRun
    copies the bundled sample database to the app's external files
    anymemo folder (ui/AnyMemo.java:315-321). A fresh install also
    shows the "New version installed" dialog; the script taps OK.

Selector notes (all read from layout XML, strings.xml, or source):
  - Bottom navigation: menu/main_tab_items.xml id misc_tab_menu.
  - Misc tab: layout/misc_tab.xml ids misc_export (expands the
    export section, initially gone) and export_mnemosyne (the button
    whose branch creates ConverterFragment with the MnemosyneXML
    exporter, MiscTabFragment.java:291-296). The trigger graph's
    branch text for the ConverterFragment edge names this button.
  - File-browser rows: layout/filebrowser_item.xml rows show the
    relative file name (FileBrowserFragment.java onBindViewHolder
    strips a trailing "/" from folder names and a leading "/").
    The browser starts in the app's external files anymemo folder
    (FileBrowserFragment.java:164-170), so the script walks up with
    ".." rows to the shared-storage root, then into "Download", then
    taps the fixture row "sample_deck.apkg".
  - Merge dialog confirmation: strings.xml yes_text "Yes".

Caveats (see REPORT.md for the full analysis, with evidence):
  - The in-app converter browser filters its listing to ".db" files
    (the export button passes EXTRA_FILE_EXTENSIONS ".db", and
    FileBrowserFragment.fill only lists files matching the extension
    in RELATIVE mode), so the ".apkg" fixture row may not be listed
    at all in a real run and the fixture tap may fail.
  - The fixture itself is an Anki archive (it contains
    collection.anki2 and no cards.xml), while
    Mnemosyne2CardsImporter.convert unzips its input and throws
    unless cards.xml is present, before ever calling xmlToCards,
    which is the only place ValueType is first used
    (Mnemosyne2CardsImporter.java:184). The converter therefore
    rejects this fixture before the target class initializer can
    fire. A genuine Mnemosyne2 cards archive (a zip containing
    cards.xml) would be needed for the target to be reached.
  - The printed chain splices an export-converter browser head
    (MnemosyneXMLExporter, destination extension "xml", so its
    startConversion takes the create-document branch, not a merge
    dialog) onto an import-service tail (Mnemosyne2CardsImporter,
    destination extension "db"). The script follows the printed
    edges as written and taps "Yes" for the dialog edge; in a real
    run that dialog may not appear from the export head.
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
    "E3ae14c6f", "E4d455e8e", "E06cb551e", "Ee7fb6e62", "E293210fe",
    "E09df7003", "E6d22692a", "Ea6b99e70", "E1b342eec", "E4bc3be81",
    "E3edbc981", "Eece3b07c", "E9c19e28c", "E12bd28f7", "Ef94688d7",
    "E92ea72a0", "E81e8b1b7", "E835f2200", "E94b69705", "E50df8fb0",
    "E49950861", "Eed16c0fe",
]

PKG_COMPONENT = ("org.liberty.android.fantastischmemopro/"
                 "org.liberty.android.fantastischmemo.ui.AnyMemo")


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_04 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_04", EDGE_IDS, args.log,
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
    # tap Export to expand the export section (initially gone).
    r.tap("E3ae14c6f", res_id="misc_export")
    # E4d455e8e MiscTabFragment.onClick -> ConverterFragment.<init>:
    # v == exportMnemosyneButton branch shows ConverterFragment.
    r.tap("E4d455e8e", res_id="export_mnemosyne")
    # E06cb551e ConverterFragment.<init> -> ConverterFragment.onCreate.
    r.comment("ConverterFragment onCreate", "E06cb551e")
    # Ee7fb6e62 ConverterFragment.onCreate ->
    # FileBrowserFragment.onCreate@CONVERTER: ConverterFragment extends
    # FileBrowserFragment, so super.onCreate runs the browser setup.
    r.comment("file browser created inside the converter", "Ee7fb6e62")
    # E293210fe FileBrowserFragment.onCreate@CONVERTER ->
    # FileBrowserFragment.onCreateView@CONVERTER: lifecycle.
    r.comment("file browser view created", "E293210fe")
    # E09df7003 FileBrowserFragment.onCreateView@CONVERTER ->
    # FileBrowserFragment.onResume@CONVERTER: lifecycle.
    r.comment("file browser resumed", "E09df7003")
    # E6d22692a FileBrowserFragment.onResume@CONVERTER ->
    # FileBrowserFragment.browseTo@CONVERTER: call.
    r.comment("browser lists the starting folder", "E6d22692a")
    # Ea6b99e70 FileBrowserFragment.browseTo@CONVERTER ->
    # FileBrowserFragment.fill@CONVERTER: call.
    r.comment("folder entries filled", "Ea6b99e70")
    # E1b342eec FileBrowserFragment.fill@CONVERTER ->
    # FileBrowserFragment$FileBrowserAdapter.setItems@CONVERTER: call.
    r.comment("adapter receives the entries", "E1b342eec")
    # E4bc3be81 FileBrowserFragment$FileBrowserAdapter.setItems@CONVERTER ->
    # FileBrowserFragment$FileBrowserAdapter.onBindViewHolder@CONVERTER:
    # RecyclerView binds the rows.
    r.comment("browser rows bound", "E4bc3be81")
    # E3edbc981 FileBrowserFragment$FileBrowserAdapter.onBindViewHolder@CONVERTER ->
    # FileBrowserFragment$FileBrowserAdapter$1.onClick@CONVERTER: walk
    # up from the starting anymemo folder to the shared-storage root
    # (files, package dir, data, Android, storage root), enter
    # Download, then tap the fixture row. NOTE: the converter browser
    # filters to ".db" files, so the ".apkg" row may not be listed;
    # see the header caveats and REPORT.md.
    r.tap("E3edbc981", text="..")
    r.tap("E3edbc981", text="..")
    r.tap("E3edbc981", text="..")
    r.tap("E3edbc981", text="..")
    r.tap("E3edbc981", text="..")
    r.tap("E3edbc981", text="Download")
    r.tap("E3edbc981", text="sample_deck.apkg")
    # Eece3b07c FileBrowserFragment$FileBrowserAdapter$1.onClick@CONVERTER ->
    # FileBrowserFragment.openFile@CONVERTER: the tapped file row opens.
    r.comment("fixture file row opened", "Eece3b07c")
    # E9c19e28c FileBrowserFragment.openFile@CONVERTER ->
    # ConverterFragment$1.onFileBrowserFileClick: the clicked file is a
    # file and the click listener is set, so the listener runs.
    r.comment("converter file-click listener runs", "E9c19e28c")
    # E12bd28f7 ConverterFragment$1.onFileBrowserFileClick ->
    # ConverterFragment.startConversion: call.
    r.comment("conversion prepared for the tapped file", "E12bd28f7")
    # Ef94688d7 ConverterFragment.startConversion -> S_DLG_CONVERT_MERGE:
    # destination extension is db and the output file already exists,
    # so the merge dialog is shown.
    r.comment("merge dialog entered", "Ef94688d7")
    # E92ea72a0 S_DLG_CONVERT_MERGE -> MiscTabFragment$4.onClick:
    # tap Yes to overwrite/merge into the existing converted file.
    r.tap("E92ea72a0", text="Yes")
    # E81e8b1b7 MiscTabFragment$4.onClick ->
    # MiscTabFragment.invokeImportConversion: call.
    r.comment("import conversion invoked", "E81e8b1b7")
    # E835f2200 MiscTabFragment.invokeImportConversion ->
    # ConvertIntentService.onCreate@IMPORT: service started.
    r.comment("conversion service started", "E835f2200")
    # E94b69705 ConvertIntentService.onCreate@IMPORT ->
    # ConvertIntentService.onHandleIntent@IMPORT: lifecycle.
    r.comment("conversion service handles the intent", "E94b69705")
    # E50df8fb0 ConvertIntentService.onHandleIntent@IMPORT ->
    # Mnemosyne2CardsImporter.convert: call.
    r.comment("importer converts the tapped file", "E50df8fb0")
    # E49950861 Mnemosyne2CardsImporter.convert ->
    # Mnemosyne2CardsImporter.xmlToCards: call.
    r.comment("imported cards parsed from XML", "E49950861")
    # Eed16c0fe Mnemosyne2CardsImporter.xmlToCards ->
    # Mnemosyne2CardsImporter$ValueType.<clinit>: target edge, first
    # use of the ValueType enum during parsing.
    r.comment("target: ValueType first used while parsing", "Eed16c0fe")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
