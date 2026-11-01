#!/usr/bin/env python3
"""AnyMemo route_05: DownloaderUtils.downloadFile.

Method: DownloaderUtils.downloadFile
Edge ids in order:
    Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
    E48c9d4a5 Ef4267162 E25e1518b E690f7694 E6da90567 Ebf74c9c7
    E953ab259 E2455ca30 E1e204ebe E6e6eed14 Eb58ca0ea Eabeaf426
    E7fb331ae E450c56c0 E553e8d3a E9827b63c Ec5d30f7f E24b4ee5c
    E76c5baf3 E32fc9ed1 E30961aed Edbdccc47 E279c40e6 Edf112fb9
    E86dd5c3a Eb150dbd7 E93f22026 E4dfe850b
Printed route: graphs/AnyMemo/scratch/route_print/DownloaderUtils.downloadFile.txt
Permissions (ROUTES.csv, granted by run_app.sh before this script runs):
    android.permission.WRITE_EXTERNAL_STORAGE
Fixtures: none.
Setup: none. No deck/card state is needed: the download list comes
    from the live anymemo.org service (AMEnv.ANYMEMO_SERVICE_ENDPOINT
    "https://anymemo.org", AnyMemoDownloaderFragment
    LIST_DATABASES_PATH "/api/legacy_database/list").

Selector notes (all read from layout XML, strings.xml, or source):
  - Bottom navigation: menu/main_tab_items.xml id download_tab_menu.
  - Download tab: layout/download_tab.xml id source_anymemo
    (DownloadTabFragment.java:56,64 starts AnyMemoDownloaderActivity
    on it).
  - Download list rows: layout/filebrowser_item.xml rows show the
    item title (AbstractDownloaderFragment.java:395,407). The initial
    list is categories (AnyMemoDownloaderFragment.initialRetrieve
    returns getCategories()), so the script first opens a category
    and then taps a database row; the database-row tap is the action
    of the printed row-click edge. Row titles come from the live
    service at run time, so neither row has a stable id, text, or
    content description; the script therefore uses fixed-coordinate
    taps for the first list row, with a why string, as the harness
    allows when no selector exists. The coordinates assume a
    1080-wide display with the first list row near the top of the
    list; they are the weakest part of this script (see REPORT.md).
  - Download confirmation dialog: strings.xml yes_text "Yes"
    (AbstractDownloaderFragment.java:284).

Caveat: this route needs live anymemo.org reachability from the
    emulator. If the service is unreachable, RetrieveTask reports a
    connection error instead of a list and no row tap can proceed;
    the fetch then never calls DownloaderUtils.downloadFile.
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
    "E6da90567", "Ebf74c9c7", "E953ab259", "E2455ca30", "E1e204ebe",
    "E6e6eed14", "Eb58ca0ea", "Eabeaf426", "E7fb331ae", "E450c56c0",
    "E553e8d3a", "E9827b63c", "Ec5d30f7f", "E24b4ee5c", "E76c5baf3",
    "E32fc9ed1", "E30961aed", "Edbdccc47", "E279c40e6", "Edf112fb9",
    "E86dd5c3a", "Eb150dbd7", "E93f22026", "E4dfe850b",
]

PKG_COMPONENT = ("org.liberty.android.fantastischmemopro/"
                 "org.liberty.android.fantastischmemopro.ui.AnyMemo")


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnyMemo route_05 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_05", EDGE_IDS, args.log,
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
    # tap the Download bottom-navigation item.
    r.tap("E6da90567", res_id="download_tab_menu")
    # Ebf74c9c7 AnyMemo$2.onNavigationItemSelected -> DownloadTabFragment.<init>:
    # itemId == download_tab_menu branch (AnyMemo.java:247-248).
    r.comment("DownloadTabFragment created for the Download tab", "Ebf74c9c7")
    # E953ab259 DownloadTabFragment.<init> -> DownloadTabFragment.onAttach.
    r.comment("fragment onAttach", "E953ab259")
    # E2455ca30 DownloadTabFragment.onAttach -> DownloadTabFragment.onCreateView.
    r.comment("fragment onCreateView (download_tab layout)", "E2455ca30")
    # E1e204ebe DownloadTabFragment.onCreateView -> DownloadTabFragment.onClick:
    # tap the AnyMemo download source button.
    r.tap("E1e204ebe", res_id="source_anymemo")
    # E6e6eed14 DownloadTabFragment.onClick -> AnyMemoDownloaderActivity.<init>:
    # v == amButton branch starts the downloader activity.
    r.comment("AnyMemoDownloaderActivity started", "E6e6eed14")
    # Eb58ca0ea AnyMemoDownloaderActivity.<init> ->
    # AnyMemoDownloaderActivity.onCreate.
    r.comment("downloader activity onCreate", "Eb58ca0ea")
    # Eabeaf426 AnyMemoDownloaderActivity.onCreate ->
    # AnyMemoDownloaderFragment.onCreate: fragment attached.
    r.comment("AnyMemoDownloaderFragment created", "Eabeaf426")
    # E7fb331ae AnyMemoDownloaderFragment.onCreate -> S_DOWNLOAD_AM.
    r.comment("AnyMemo download page entered", "E7fb331ae")
    # E450c56c0 S_DOWNLOAD_AM ->
    # AbstractDownloaderFragment.onViewCreated@AM: lifecycle.
    r.comment("download fragment view created", "E450c56c0")
    # E553e8d3a AbstractDownloaderFragment.onViewCreated@AM ->
    # AbstractDownloaderFragment.refreshList@AM: call.
    r.comment("download list refresh started", "E553e8d3a")
    # E9827b63c AbstractDownloaderFragment.refreshList@AM ->
    # AbstractDownloaderFragment$RetrieveTask.onPreExecute@AM: async.
    r.comment("retrieve task shows its progress dialog", "E9827b63c")
    # Ec5d30f7f AbstractDownloaderFragment$RetrieveTask.onPreExecute@AM ->
    # AbstractDownloaderFragment$RetrieveTask.doInBackground@AM: async.
    r.comment("category list fetched from anymemo.org", "Ec5d30f7f")
    # E24b4ee5c AbstractDownloaderFragment$RetrieveTask.doInBackground@AM ->
    # AbstractDownloaderFragment$1.call@AM: the refresh Callable.
    r.comment("initial retrieve callable runs", "E24b4ee5c")
    # E76c5baf3 AbstractDownloaderFragment$1.call@AM ->
    # AbstractDownloaderFragment$RetrieveTask.onPostExecute@AM: async.
    r.comment("category list shown", "E76c5baf3")
    # E32fc9ed1 AbstractDownloaderFragment$RetrieveTask.onPostExecute@AM ->
    # AbstractDownloaderFragment$DownloadListAdapter$1.onClick@AM: the
    # initial list holds categories, so open the first category row
    # first (a second retrieve cycle, not a separate printed edge),
    # then tap the first database row, which is neither a category
    # nor a back row and therefore opens the download dialog. Row
    # titles come from the live service, so no id/text/desc exists
    # for either row; fixed coordinates are used with a why string.
    r.tap("E32fc9ed1", x=540, y=400,
          why="first download-list row: title comes from the live "
              "anymemo.org list, so no stable id, text, or desc exists")
    r.tap("E32fc9ed1", x=540, y=400,
          why="first database row inside the opened category: title "
              "comes from the live anymemo.org list, so no stable id, "
              "text, or desc exists")
    # E30961aed AbstractDownloaderFragment$DownloadListAdapter$1.onClick@AM ->
    # AbstractDownloaderFragment.showFetchDatabaseDialog@AM: call.
    r.comment("download confirmation dialog shown", "E30961aed")
    # Edbdccc47 AbstractDownloaderFragment.showFetchDatabaseDialog@AM ->
    # S_DLG_DOWNLOAD_CONFIRM_AM: dialog entered.
    r.comment("download confirmation dialog entered", "Edbdccc47")
    # E279c40e6 S_DLG_DOWNLOAD_CONFIRM_AM ->
    # AbstractDownloaderFragment$2.onClick@AM: tap Yes to download.
    r.tap("E279c40e6", text="Yes")
    # Edf112fb9 AbstractDownloaderFragment$2.onClick@AM ->
    # AbstractDownloaderFragment.startFetchDatabaseTask@AM: call.
    r.comment("fetch task started", "Edf112fb9")
    # E86dd5c3a AbstractDownloaderFragment.startFetchDatabaseTask@AM ->
    # AbstractDownloaderFragment$FetchDatabaseTask.onPreExecute@AM: async.
    r.comment("fetch task shows its progress dialog", "E86dd5c3a")
    # Eb150dbd7 AbstractDownloaderFragment$FetchDatabaseTask.onPreExecute@AM ->
    # AbstractDownloaderFragment$FetchDatabaseTask.doInBackground@AM: async.
    r.comment("fetch runs in the background", "Eb150dbd7")
    # E93f22026 AbstractDownloaderFragment$FetchDatabaseTask.doInBackground@AM ->
    # AnyMemoDownloaderFragment.fetchDatabase: call.
    r.comment("database fetch runs", "E93f22026")
    # E4dfe850b AnyMemoDownloaderFragment.fetchDatabase ->
    # DownloaderUtils.downloadFile: target edge; the file name ends
    # with .db, so fetchDatabase downloads it.
    r.comment("target: database file downloaded", "E4dfe850b")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
