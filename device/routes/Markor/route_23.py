"""Device route script: route_23.

Method: GsSharedPreferencesPropertyBackend.getStringListOne
Printed route file: graphs/Markor/scratch/route_print/route_23.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Ecbe70212 Eaff9bcbe
  Ea3ea96a6 Ed983bbc6 Eb01f439f E090e1957 E7b101054 Eb085a8fa
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: (none)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Replay: cold-start MainActivity only. Creating the notebook page reads
the popular-files preference list (MarkorFileBrowserFactory
.updateFsViewerOpts -> AppSettings.getPopularFiles ->
getStringList -> getStringListOne), which runs regardless of the list
contents, so no tap, file, or permission is needed beyond the launch.
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
    r = Runner(package=args.package, route="route_23",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Ecbe70212", "Eaff9bcbe", "Ea3ea96a6", "Ed983bbc6",
                         "Eb01f439f", "E090e1957", "E7b101054", "Eb085a8fa"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # No permissions listed in ROUTES.csv for this route, so no grant().
    # No fixtures listed for this route; run_app.sh pushes Documents
    # per setup, but this route needs none of it.
    # E211966cc: Tap the Markor launcher icon (process start).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: The system calls Application.onCreate -- no user action.
    r.comment("system lifecycle: Application.onCreate, no user action",
              "Ed6414d9f")
    # E0254b914: MAIN/LAUNCHER intent starts MainActivity -- already
    # started by the launch above, no further action.
    r.comment("MainActivity already started by the E211966cc launch",
              "E0254b914")
    # Ed25af8f4: The system calls Activity.onCreate -- no user action.
    r.comment("system lifecycle: Activity.onCreate, no user action",
              "Ed25af8f4")
    # Ecbe70212: SectionsPagerAdapter.createFragment -- after setAdapter
    # the pager asks the adapter for the first page fragment, the
    # notebook tab (MainActivity.java:105-106, 509-526); framework
    # driven, no user action.
    r.comment("framework: pager creates notebook fragment, no action",
              "Ecbe70212")
    # Eaff9bcbe: GsFileBrowserFragment.onViewCreated -- the
    # FragmentManager attaches the fragment and creates its view
    # (GsFileBrowserFragment.java:107); framework driven, no action.
    r.comment("framework: fragment onViewCreated, no user action",
              "Eaff9bcbe")
    # Ea3ea96a6: MainActivity.getFilesystemFragmentOptions -- virtual /
    # interface call from GsFileBrowserFragment.onViewCreated
    # (GsFileBrowserFragment.java:119); no user action.
    r.comment("call: getFilesystemFragmentOptions, no user action",
              "Ea3ea96a6")
    # Ed983bbc6: MarkorFileBrowserFactory.prepareFsViewerOpts -- direct
    # call (MainActivity.java:462); no user action.
    r.comment("direct call: prepareFsViewerOpts, no user action",
              "Ed983bbc6")
    # Eb01f439f: MarkorFileBrowserFactory.updateFsViewerOpts -- direct
    # call (MarkorFileBrowserFactory.java:75); no user action.
    r.comment("direct call: updateFsViewerOpts, no user action",
              "Eb01f439f")
    # E090e1957: AppSettings.getPopularFiles -- direct call
    # (MarkorFileBrowserFactory.java:86: opts.popularFiles =
    # appSettings.getPopularFiles()); no user action.
    r.comment("direct call: getPopularFiles, no user action", "E090e1957")
    # E7b101054: GsSharedPreferencesPropertyBackend.getStringList --
    # direct call (AppSettings.java:680: getPopularFiles reads
    # getStringList of the popular-documents key); no user action.
    r.comment("direct call: getStringList, no user action", "E7b101054")
    # Eb085a8fa: GsSharedPreferencesPropertyBackend.getStringListOne --
    # direct call (GsSharedPreferencesPropertyBackend.java:258); the
    # preference read runs regardless of list contents, no user action.
    r.comment("direct call: getStringListOne, no user action", "Eb085a8fa")
    r.done()


if __name__ == "__main__":
    main()
