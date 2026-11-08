#!/usr/bin/env python3
"""AmazeFileManager route_04: GlideRequests.load(Integer).

Method: GlideRequests.load(Integer)
Edge ids in order:
    E3f6c0e47 E961aba14 E45bf8d26 E771f72f3 Ee8714c30 E9c7cd787
Printed route: graphs/AmazeFileManager/scratch/route_print/
    GlideRequests.load(Integer).txt, verdict REACHABLE, 6 edges.
    This edge list matches methods.csv route_edge_ids for
    GlideRequests.load(Integer) exactly and matches the D1 draft
    route_04 row exactly; no mismatch.
Permissions: WRITE_EXTERNAL_STORAGE (ROUTES.csv decision). MainActivity
    extends PermissionsActivity and requests storage permission on
    launch when missing (MainActivity.java:438-439); the archive
    viewer also has to read the pushed zip fixture from shared
    storage, so the grant is genuinely required here, not just a
    first-run convenience.
Fixtures: route04.zip, pushed by replay setup (not by this script)
    to /sdcard/Download/route04.zip. Contents required by the
    scripted steps: a folder entry named "sub" containing at least
    one file (e.g. sub/note.txt), plus at least one entry at the
    archive root is not required but harmless. The script opens the
    archive with an ACTION_VIEW intent whose data URI must match
    the pushed path exactly (see the setup contract below).
Setup: replay setup pushes route04.zip to
    /sdcard/Download/route04.zip BEFORE running this script; the
    script itself does not push it, because no fixture file ships
    with this helper dir and push_fixture with a nonexistent local
    path would fail a real run. Standard config: run_app.sh starts
    from `pm clear` and grants only the ROUTES.csv permissions
    above.

Mapping notes (printed source evidence):
  - The printed route starts at the back press, so it has NO entry
    edge for opening the archive. The setup steps below (VIEW
    intent, tap into "sub") are therefore logged under the first
    edge id E3f6c0e47 and are marked as setup, not as edge steps;
    the actual E3f6c0e47 action is the r.back() call.
  - Archive entry by intent: MainActivity's VIEW intent filter
    covers application/zip (AndroidManifest.xml:79-90).
    checkForExternalIntent treats a non-folder VIEW intent as an
    archive (MainActivity.java:522-526: openzip=true, zippath=
    sanitized URI), and goToMain then calls openCompressed(zippath)
    (MainActivity.java:796-799). openCompressed adds a
    CompressedExplorerFragment for that path
    (MainActivity.java:1240-1250), whose onCreateView reads the
    file from the URI path (CompressedExplorerFragment.java:167)
    and whose onActivityCreated calls changePath("") for the root
    listing (:217). The script's VIEW intent therefore needs no
    file-list navigation and no archive-dialog tap.
  - Entering the subfolder: a directory row's tap calls
    changePath(newPath) (CompressedExplorerAdapter.java:262-271),
    and the row title for a directory is the entry name
    (CompressedExplorerAdapter.java:221-226 area: directory branch
    sets txtTitle to the item name). The script taps the text
    "sub". After this tap, relativeDirectory is "sub", so
    canGoBack() is true (CompressedExplorerFragment.java:490-495:
    canGoBack is !isRootRelativePath), which is exactly the guard
    the printed goBack step needs.
  - Back dispatch: MainActivity.onBackPressed sends Back to the
    archive fragment when the frame holds a
    CompressedExplorerFragment with no action mode and canGoBack()
    (MainActivity.java:719-724), which calls goBack()
    (CompressedExplorerFragment.java:494-495: changePath(parent)),
    whose decompressor callback calls createViews
    (:412-415). createViews rebinds the parent (root) listing
    through the RecyclerView adapter (:448-456), so
    onBindViewHolder runs again for the root rows.
  - Target edge: onBindViewHolder's non-goback branch loads
    GlideApp.with(compressedExplorerFragment).load(rowItem.iconData
    .image) (CompressedExplorerAdapter.java:217). iconData.image
    is an int drawable resource (IconDataParcelable.java:19), so
    this is the load(Integer) overload. The rebound root listing
    contains the "sub" directory row, a non-goback row, so this
    branch is taken. No fixed coordinates are used anywhere.
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E3f6c0e47", "E961aba14", "E45bf8d26", "E771f72f3", "Ee8714c30",
    "E9c7cd787",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_04")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_04", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # E3f6c0e47 S_ENTRY -> MainActivity.onBackPressed. SETUP (not an
    # edge step; the printed route has no entry edge, so setup is
    # logged under this first edge id): open the pushed fixture
    # archive in the viewer. MainActivity's VIEW filter covers
    # application/zip (AndroidManifest.xml:79-90); a non-folder VIEW
    # intent sets openzip/zippath (MainActivity.java:522-526) and
    # goToMain calls openCompressed(zippath) (:796-799), which adds
    # the CompressedExplorerFragment (:1240-1250). The data URI
    # must match the replay-setup push path exactly.
    r.start_intent("E3f6c0e47", action="android.intent.action.VIEW",
                   data="file:///sdcard/Download/route04.zip",
                   mime="application/zip")
    # SETUP continued (same edge id): enter the "sub" folder so that
    # canGoBack() is true for the back press below. A directory row
    # tap calls changePath(newPath)
    # (CompressedExplorerAdapter.java:262-271); the row title is the
    # folder name "sub".
    r.wait_for("E3f6c0e47", text="sub")
    r.tap("E3f6c0e47", text="sub")
    # E3f6c0e47, the actual edge action: press Back. MainActivity
    # .onBackPressed dispatches to the archive fragment when it is
    # at the frame with no action mode and canGoBack()
    # (MainActivity.java:719-724). At this point the viewer is in
    # "sub", so canGoBack() is true (CompressedExplorerFragment
    # .java:490-495).
    r.back("E3f6c0e47")
    # E961aba14 MainActivity.onBackPressed -> CompressedExplorer
    # Fragment.goBack: the dispatched call (MainActivity.java:723).
    # No user action beyond the back press above.
    r.comment("MainActivity dispatches Back to CompressedExplorer"
              "Fragment.goBack (MainActivity.java:723)", "E961aba14")
    # E45bf8d26 CompressedExplorerFragment.goBack -> Compressed
    # ExplorerFragment.changePath: goBack calls changePath(parent)
    # (CompressedExplorerFragment.java:494-495). No user action.
    r.comment("goBack calls changePath(parent) "
              "(CompressedExplorerFragment.java:494-495)", "E45bf8d26")
    # E771f72f3 CompressedExplorerFragment.changePath -> Compressed
    # ExplorerFragment.createViews: the decompressor callback calls
    # createViews(elements, finalfolder) on success
    # (CompressedExplorerFragment.java:412-415). No user action.
    r.comment("changePath callback calls createViews "
              "(CompressedExplorerFragment.java:412-415)", "E771f72f3")
    # Ee8714c30 CompressedExplorerFragment.createViews ->
    # CompressedExplorerAdapter.onBindViewHolder: createViews sets
    # the adapter on the RecyclerView (or regenerates it), and the
    # RecyclerView framework binds the parent listing's rows.
    # Framework; no user action.
    r.comment("RecyclerView framework binds the rebound parent "
              "listing rows", "Ee8714c30")
    # E9c7cd787 CompressedExplorerAdapter.onBindViewHolder ->
    # GlideRequests.load(Integer): TARGET EDGE. The non-goback
    # branch loads GlideApp.with(compressedExplorerFragment).load
    # (rowItem.iconData.image) (CompressedExplorerAdapter.java:217);
    # iconData.image is an int drawable resource
    # (IconDataParcelable.java:19), i.e. the load(Integer) overload.
    # The rebound root listing contains the "sub" directory row, a
    # non-goback row, so this branch runs. Framework/bind-time;
    # no user action beyond the back press above.
    r.comment("onBindViewHolder loads rowItem.iconData.image "
              "(CompressedExplorerAdapter.java:217, int resource)",
              "E9c7cd787")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
