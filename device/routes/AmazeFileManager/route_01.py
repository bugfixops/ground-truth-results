#!/usr/bin/env python3
"""AmazeFileManager route_01: CloudIconDataFetcher.cancel.

Method: CloudIconDataFetcher.cancel
Edge ids in order:
    Ef3576ae6 Ec93a3d5b Edd7ffae0 E5f0bd603 E7c3c57fd Eb41c849f
    E64795b93 E64b023f9 E23f4cc5e E18952e7d E3e591ceb E2cf492c6
    Ef4cf00cb E0c630bc8
Printed route: graphs/AmazeFileManager/scratch/route_print/
    CloudIconDataFetcher.cancel.txt, verdict REACHABLE, 14 edges.
    This edge list matches methods.csv route_edge_ids for
    CloudIconDataFetcher.cancel exactly and matches the D1 draft
    route_01 row exactly; no mismatch.
Permissions: WRITE_EXTERNAL_STORAGE (ROUTES.csv decision). MainActivity
    extends PermissionsActivity and requests storage permission on
    launch when missing (MainActivity.java:438-439); granting it in
    ROUTES.csv keeps the first-run permission gate from blocking the
    drawer steps. No other runtime permission is needed: the app list
    comes from the package manager, and the Glide chain needs none.
Fixtures: none. Setup: standard config only (run_app.sh starts from
    `pm clear` and grants only the ROUTES.csv permissions above).
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions.

Mapping notes (printed source evidence):
  - MainActivity is the MAIN/LAUNCHER activity
    (AndroidManifest.xml:58, intent filter :61-65), so the script
    launches com.amaze.filemanager.debug/.activities.MainActivity.
  - The drawer toggle carries the "open drawer" description
    (Drawer.java:221, R.string.drawer_open = "Open navigation
    drawer", strings.xml:25), so the script opens the drawer by
    tapping that content description.
  - The drawer row is R.string.apps = "App Manager"
    (strings.xml:29); Drawer.java:418-428 builds that row and its
    lambda replaces R.id.content_frame with a new AppsListFragment.
    Drawer.java:597 dispatches the tap to the lambda and
    Drawer.java:535 commits the transaction on drawer close.
  - AppsListFragment.onActivityCreated builds the Glide preloader
    with GlideApp.with(app) (AppsListFragment.java:98); that single
    call starts the whole Glide module/factory/loader chain below.
    No further user action drives it, so edges after the row tap
    are logged with r.comment.
  - The target edge is framework-invoked: Glide calls cancel() on
    the fetcher when a load is cancelled. CloudIconDataFetcher
    .cancel() itself is a no-op (CloudIconDataFetcher.java:55-58),
    so the script logs it with r.comment rather than inventing a
    tap; the replay log's cancel evidence comes from Glide
    teardown of the AppsListFragment requests.
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
    "Ef3576ae6", "Ec93a3d5b", "Edd7ffae0", "E5f0bd603", "E7c3c57fd",
    "Eb41c849f", "E64795b93", "E64b023f9", "E23f4cc5e", "E18952e7d",
    "E3e591ceb", "E2cf492c6", "Ef4cf00cb", "E0c630bc8",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_01")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_01", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ef3576ae6 S_ENTRY -> Drawer.onNavigationItemSelected: launch
    # MainActivity (MAIN/LAUNCHER) and open the navigation drawer.
    # The drawer toggle description is "Open navigation drawer"
    # (Drawer.java:221, strings.xml:25).
    r.launch(args.package + "/.activities.MainActivity", "Ef3576ae6")
    r.tap("Ef3576ae6", desc="Open navigation drawer")
    # The "App Manager" row sits in the LASTGROUP rows at the end of
    # the drawer list (Drawer.java:418-428), so scroll to it first.
    r.scroll_to("Ef3576ae6", text="App Manager")
    # Ec93a3d5b Drawer.onNavigationItemSelected -> AppsListFragment
    # .<init>: tap the "App Manager" row (R.string.apps,
    # strings.xml:29). Its lambda replaces content_frame with a new
    # AppsListFragment (Drawer.java:418-428, dispatched at :597,
    # committed on drawer close at :535).
    r.tap("Ec93a3d5b", text="App Manager")
    # Edd7ffae0 AppsListFragment.<init> -> AppsListFragment.onCreate:
    # fragment lifecycle. No user action.
    r.comment("fragment lifecycle: onCreate runs", "Edd7ffae0")
    # E5f0bd603 AppsListFragment.onCreate -> AppsListFragment
    # .onActivityCreated: fragment lifecycle. No user action.
    r.comment("fragment lifecycle: onActivityCreated runs", "E5f0bd603")
    # E7c3c57fd AppsListFragment.onActivityCreated -> GlideApp.with
    # (Fragment)#2: onActivityCreated builds the ListPreloader with
    # GlideApp.with(app) (AppsListFragment.java:98). No user action
    # beyond the row tap above.
    r.comment("GlideApp.with(app) in onActivityCreated (AppsListFragment"
              ".java:98)", "E7c3c57fd")
    # Eb41c849f GlideApp.with(Fragment)#2 -> GeneratedAppGlideModule
    # Impl.<init>: Glide instantiates its generated module on first
    # with() call (@GlideModule on AmazeFileManagerModule.java:17).
    # Framework; no user action.
    r.comment("Glide instantiates GeneratedAppGlideModuleImpl",
              "Eb41c849f")
    # E64795b93 GeneratedAppGlideModuleImpl.<init> -> GeneratedApp
    # GlideModuleImpl.registerComponents: Glide calls it to register
    # custom components. Framework; no user action.
    r.comment("Glide calls registerComponents", "E64795b93")
    # E64b023f9 GeneratedAppGlideModuleImpl.registerComponents ->
    # AmazeFileManagerModule.registerComponents: generated code
    # delegates to the app module. Framework; no user action.
    r.comment("generated module delegates to AmazeFileManagerModule",
              "E64b023f9")
    # E23f4cc5e AmazeFileManagerModule.registerComponents ->
    # CloudIconModelFactory.<init>: registry.prepend(String, Bitmap,
    # new CloudIconModelFactory(context))
    # (AmazeFileManagerModule.java:22). Framework; no user action.
    r.comment("registerComponents creates CloudIconModelFactory "
              "(AmazeFileManagerModule.java:22)", "E23f4cc5e")
    # E18952e7d CloudIconModelFactory.<init> -> CloudIconModelFactory
    # .build: Glide calls ModelLoaderFactory.build to create the
    # ModelLoader. Framework; no user action.
    r.comment("Glide calls CloudIconModelFactory.build", "E18952e7d")
    # E3e591ceb CloudIconModelFactory.build -> CloudIconModelLoader
    # .<init>: build returns new CloudIconModelLoader(context)
    # (CloudIconModelFactory.java:23-26). Framework; no user action.
    r.comment("factory builds CloudIconModelLoader "
              "(CloudIconModelFactory.java:23-26)", "E3e591ceb")
    # E2cf492c6 CloudIconModelLoader.<init> -> CloudIconModelLoader
    # .buildLoadData: Glide calls buildLoadData when loading an
    # image. Framework; no user action.
    r.comment("Glide calls CloudIconModelLoader.buildLoadData",
              "E2cf492c6")
    # Ef4cf00cb CloudIconModelLoader.buildLoadData ->
    # CloudIconDataFetcher.<init>: buildLoadData returns a LoadData
    # wrapping new CloudIconDataFetcher(context, s, width, height)
    # (CloudIconModelLoader.java:25-31). Framework; no user action.
    r.comment("buildLoadData creates CloudIconDataFetcher "
              "(CloudIconModelLoader.java:25-31)", "Ef4cf00cb")
    # E0c630bc8 CloudIconDataFetcher.<init> -> CloudIconDataFetcher
    # .cancel: TARGET EDGE. Glide framework lifecycle: cancel is
    # called if the load is cancelled; the method body is a no-op
    # (CloudIconDataFetcher.java:55-58). Framework; no user action,
    # so no tap is invented for it.
    r.comment("Glide framework calls CloudIconDataFetcher.cancel "
              "(CloudIconDataFetcher.java:55-58, no-op body)",
              "E0c630bc8")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
