#!/usr/bin/env python3
"""AmazeFileManager route_03: ApkImageDataFetcher.cancel.

Method: ApkImageDataFetcher.cancel
Edge ids in order:
    Ef3576ae6 Ec93a3d5b Edd7ffae0 E5f0bd603 E7c3c57fd Eb41c849f
    E64795b93 E64b023f9 E8c852b7d E4c6b48e5 Effa2e952 E44ea6c85
    Ec3267b09 Ec0f6b33b
Printed route: graphs/AmazeFileManager/scratch/route_print/
    ApkImageDataFetcher.cancel.txt, verdict REACHABLE, 14 edges.
    This edge list matches methods.csv route_edge_ids for
    ApkImageDataFetcher.cancel exactly and matches the D1 draft
    route_03 row exactly; no mismatch.
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
  - This route takes the APK branch of the same module: the app
    module registers ApkImageModelLoaderFactory first
    (AmazeFileManagerModule.java:21), before the cloud factory on
    :22, and the loader creates ApkImageDataFetcher
    (ApkImageModelLoader.java:27). The target cancel edge is
    framework-invoked Glide lifecycle (INFERRED in the print, no
    app source line), so the script logs it with r.comment rather
    than inventing a tap; the replay log's cancel evidence comes
    from Glide teardown of the AppsListFragment requests.
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
    "Eb41c849f", "E64795b93", "E64b023f9", "E8c852b7d", "E4c6b48e5",
    "Effa2e952", "E44ea6c85", "Ec3267b09", "Ec0f6b33b",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_03", EDGE_IDS, args.log,
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
    # E8c852b7d AmazeFileManagerModule.registerComponents ->
    # ApkImageModelLoaderFactory.<init>: registry.prepend(String,
    # Drawable, new ApkImageModelLoaderFactory(...))
    # (AmazeFileManagerModule.java:21). Framework; no user action.
    r.comment("registerComponents creates ApkImageModelLoaderFactory "
              "(AmazeFileManagerModule.java:21)", "E8c852b7d")
    # E4c6b48e5 ApkImageModelLoaderFactory.<init> ->
    # ApkImageModelLoaderFactory.build: Glide framework calls build
    # on registered factories. Framework; no user action.
    r.comment("Glide calls ApkImageModelLoaderFactory.build",
              "E4c6b48e5")
    # Effa2e952 ApkImageModelLoaderFactory.build ->
    # ApkImageModelLoader.<init>: build returns new
    # ApkImageModelLoader(packageManager)
    # (ApkImageModelLoaderFactory.java:25). Framework; no user action.
    r.comment("factory builds ApkImageModelLoader "
              "(ApkImageModelLoaderFactory.java:25)", "Effa2e952")
    # E44ea6c85 ApkImageModelLoader.<init> -> ApkImageModelLoader
    # .buildLoadData: Glide framework calls buildLoadData.
    # Framework; no user action.
    r.comment("Glide calls ApkImageModelLoader.buildLoadData",
              "E44ea6c85")
    # Ec3267b09 ApkImageModelLoader.buildLoadData ->
    # ApkImageDataFetcher.<init>: buildLoadData returns a LoadData
    # wrapping new ApkImageDataFetcher(packageManager, s)
    # (ApkImageModelLoader.java:27). Framework; no user action.
    r.comment("buildLoadData creates ApkImageDataFetcher "
              "(ApkImageModelLoader.java:27)", "Ec3267b09")
    # Ec0f6b33b ApkImageDataFetcher.<init> -> ApkImageDataFetcher
    # .cancel: TARGET EDGE. Glide framework lifecycle (INFERRED in
    # the print, no app source line): cancel is called if the load
    # is cancelled. Framework; no user action, so no tap is
    # invented for it.
    r.comment("Glide framework calls ApkImageDataFetcher.cancel "
              "(framework lifecycle, INFERRED in print)", "Ec0f6b33b")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
