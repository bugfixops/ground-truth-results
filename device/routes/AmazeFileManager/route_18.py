#!/usr/bin/env python3
"""AmazeFileManager route_18: ShareAdapter$ViewHolder.lambda$render$0.

Method: ShareAdapter$ViewHolder.lambda$render$0
Edge ids in order:
    Ef3576ae6 Ec93a3d5b Edd7ffae0 E5f0bd603 E44015116 E995dff1e
    Ee4436fb7 E6fd8d564 Ea16ad820 E6f5e3da5 Ea76a1112 E029349f9
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ShareAdapter_ViewHolder.lambda_render_0.txt, verdict REACHABLE,
    12 edges. The print's edge list matches methods.csv
    route_edge_ids and the d1_routes_draft.csv route_18 row
    exactly (no mismatch).
Permissions: READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
    (MainActivity's storage gate, MainActivity.java:436-484; the
    work-emulator baseline had storage granted before start).
Fixtures: none. Setup: none beyond the standard config, except
    the emulator must offer at least one ACTION_SEND_MULTIPLE
    resolver for an .apk mime type (see the ShareTask note below).
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (the storage pair above).

Mapping notes (printed source):
  - The drawer entry is the "App Manager" row: Drawer.java:418-428
    adds the row with R.string.apps ("App Manager",
    res/values/strings.xml:29) whose lambda replaces the content
    frame with a new AppsListFragment, committed when the drawer
    closes (Drawer.java:535). The drawer itself is opened with
    the ActionBarDrawerToggle navigation icon, whose content
    description is R.string.drawer_open ("Open navigation
    drawer", res/values/strings.xml:25, Drawer.java:221). The
    Apps row sits below the fold in a 16-row drawer (UI map),
    so the script scrolls to it before tapping.
  - The per-app overflow is the rowlayout properties button:
    AppsAdapter.getView calls showPopup(holder.about, rowItem)
    (AppsAdapter.java:132-135), and AppHolder.about is
    R.id.properties (AppHolder.java:33,
    res/layout/rowlayout.xml:94). showPopup sets an
    OnClickListener that shows a PopupMenu inflated from
    res/menu/app_options.xml, whose share item is R.id.share
    with title "Share" (res/values/strings.xml:70); its share
    case calls FileUtils.shareFiles (AppsAdapter.java:181-185).
  - This route does NOT go through the system share chooser.
    FileUtils.shareFiles executes ShareTask (FileUtils.java:373),
    and ShareTask.onPostExecute builds an in-app MaterialDialog
    titled R.string.share ("Share") whose adapter is a new
    ShareAdapter (ShareTask.java:121-131); the dialog, not a
    chooser activity, lists the targets. If no target existed,
    onPostExecute would toast R.string.no_app_found instead,
    but ShareTask also appends the Bluetooth target whenever
    com.android.bluetooth is installed (ShareTask.java:104-115),
    so the dialog is non-empty on a stock emulator image.
  - The target lambda is the row click listener created by
    render: ShareAdapter$ViewHolder.render sets
    rootView.setOnClickListener (ShareAdapter.java:72-76), and
    the lambda body dismisses the dialog and starts the chosen
    target intent. render's root view is the simplerow layout
    root (ShareAdapter.java:49 inflates R.layout.simplerow),
    whose root RelativeLayout is clickable with id "second"
    (res/layout/simplerow.xml). Tapping the first such row
    invokes lambda$render$0; the target app then opens and the
    route ends there, which is the intended final step.
  - The harness import below searches upward for the directory
    containing device/harness/harness.py instead of the template's
    fixed four-level climb, because this helper copy lives one
    level shallower than device/routes/<App>/; the same file
    therefore imports unchanged after the merger moves it there.
"""

import argparse
import os
import sys

_here = os.path.abspath(__file__)
for _depth in (3, 4):
    _root = _here
    for _ in range(_depth):
        _root = os.path.dirname(_root)
    if os.path.isfile(os.path.join(_root, "device", "harness", "harness.py")):
        sys.path.insert(0, _root)
        break
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ef3576ae6", "Ec93a3d5b", "Edd7ffae0", "E5f0bd603", "E44015116",
    "E995dff1e", "Ee4436fb7", "E6fd8d564", "Ea16ad820", "E6f5e3da5",
    "Ea76a1112", "E029349f9",
]

PKG = "com.amaze.filemanager.debug"
MAIN = PKG + "/com.amaze.filemanager.activities.MainActivity"


def main(argv=None):
    parser = argparse.ArgumentParser(description="AmazeFileManager route_18")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_18", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ef3576ae6 S_ENTRY -> Drawer.onNavigationItemSelected:
    # launch MainActivity (MAIN/LAUNCHER, AndroidManifest.xml
    # :61-65). The drawer callback itself fires on the App
    # Manager tap in the next block.
    r.launch(MAIN, "Ef3576ae6")
    # Ec93a3d5b Drawer.onNavigationItemSelected ->
    # AppsListFragment.<init>: open the drawer, scroll to the
    # App Manager row, and tap it; the row lambda replaces the
    # content frame with AppsListFragment (Drawer.java:418-428).
    r.tap("Ec93a3d5b", desc="Open navigation drawer")
    r.scroll_to("Ec93a3d5b", text="App Manager")
    r.tap("Ec93a3d5b", text="App Manager")
    # Edd7ffae0 AppsListFragment.<init> -> AppsListFragment
    # .onCreate: fragment lifecycle. No user action.
    r.comment("fragment lifecycle: onCreate", "Edd7ffae0")
    # E5f0bd603 AppsListFragment.onCreate -> AppsListFragment
    # .onActivityCreated: fragment lifecycle. No user action.
    r.comment("fragment lifecycle: onActivityCreated", "E5f0bd603")
    # E44015116 AppsListFragment.onActivityCreated ->
    # AppsAdapter.<init>: onActivityCreated constructs the
    # adapter (AppsListFragment.java:100-103). The app list
    # loads asynchronously, so wait for a row overflow button
    # (R.id.properties) before touching a row.
    r.wait_for("E44015116", res_id="properties", timeout=30)
    # E995dff1e AppsAdapter.<init> -> FileUtils.shareFiles:
    # tap the first app row's overflow button (R.id.properties,
    # which showPopup wires to the PopupMenu), then tap Share
    # in that menu; the share case calls FileUtils.shareFiles
    # (AppsAdapter.java:181-185).
    r.tap("E995dff1e", res_id="properties")
    r.tap("E995dff1e", text="Share")
    # Ee4436fb7 FileUtils.shareFiles -> ShareTask.doInBackground:
    # shareFiles executes ShareTask (FileUtils.java:373).
    # Wait for the in-app share dialog (title "Share",
    # ShareTask.java:122) to appear, which proves doInBackground
    # finished and onPostExecute built the dialog.
    r.wait_for("Ee4436fb7", text="Share", timeout=30)
    # E6fd8d564 ShareTask.doInBackground -> ShareTask
    # .onPostExecute: AsyncTask framework posts the result.
    # No user action.
    r.comment("AsyncTask framework calls onPostExecute", "E6fd8d564")
    # Ea16ad820 ShareTask.onPostExecute -> ShareAdapter.<init>:
    # onPostExecute constructs ShareAdapter for the target
    # intents and shows the dialog (ShareTask.java:121-131).
    # No user action beyond the wait above.
    r.comment("onPostExecute builds ShareAdapter and shows the "
              "in-app share dialog", "Ea16ad820")
    # E6f5e3da5 ShareAdapter.<init> -> ShareAdapter
    # .onBindViewHolder: RecyclerView binds the dialog rows.
    # No user action.
    r.comment("RecyclerView binds the share-target rows", "E6f5e3da5")
    # Ea76a1112 ShareAdapter.onBindViewHolder ->
    # ShareAdapter$ViewHolder.render: binding calls render
    # (ShareAdapter.java:50-52). No user action.
    r.comment("onBindViewHolder calls render", "Ea76a1112")
    # E029349f9 ShareAdapter$ViewHolder.render ->
    # ShareAdapter$ViewHolder.lambda$render$0: render set the row
    # click listener (ShareAdapter.java:72-76). Tap the first
    # dialog row (simplerow root, R.id.second) to invoke the
    # lambda: it dismisses the dialog and starts the chosen
    # target intent, which ends the route.
    r.tap("E029349f9", res_id="second")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
