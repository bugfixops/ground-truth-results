#!/usr/bin/env python3
"""Diary route_25: FileProvider.buildPath (provider path construction).

Method: FileProvider.buildPath
Edge ids in order:
    E33515afc Eb7d77e9a E837eed8c Ecd7e7fc1 Ee37ab436
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt,
    section "FileProvider.buildPath" (verdict correct, SOURCE,
    FileProvider.java:594-617); path row 26 of
    graphs/Diary/verification.csv. Edge details:
    graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (standard replay start: run_app.sh does
    pm clear, then this script launches Diary).
Route shape: start the app process in any way. ActivityThread
    installs the manifest providers when the process binds, before any
    activity or receiver runs (FW-SRC ActivityThread.java:5720-5722,
    6236-6239); the non-exported FileProvider (AndroidManifest.xml:
    119-127, authority org.billthefarmer.diary.fileprovider) is
    instantiated, attachInfo runs its export/grant sanity checks and
    asks for the path strategy (FileProvider.java:369-376), the
    strategy is not yet in the static sCache on this fresh process so
    it is parsed from the FILE_PROVIDER_PATHS meta-data
    (FileProvider.java:554-568), and parsePathStrategy calls buildPath
    for each root of res/xml/filepaths.xml (external-path, cache-path,
    root-path; FileProvider.java:594-617, filepaths.xml:3-5).
    There is no UI action that targets buildPath: launching the app is
    the whole driver, and every later edge is framework or internal.
    The fresh process matters for the sCache-miss guard (FileProvider.
    java:556-568): run_app.sh's pm clear stops the app, so this launch
    creates a new process with an empty sCache.
Provider source note: the FileProvider in this upload is the support
    library copy at java/android/support/v4/content/FileProvider.java
    (not org.billthefarmer.diary); the printed lines above are from
    that file.
"""

import argparse
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E33515afc", "Eb7d77e9a", "E837eed8c", "Ecd7e7fc1", "Ee37ab436",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_25 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(args.package, "route_25", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # E33515afc -- Any start of the app process: ActivityThread
    # instantiates the non-exported FileProvider before any activity
    # or receiver runs (FW-SRC ActivityThread.java:5720-5722;
    # SRC AndroidManifest.xml:119-127). Realised as launching Diary,
    # which creates the app process.
    r.launch("org.billthefarmer.diary/.Diary", "E33515afc")

    # Eb7d77e9a -- localProvider.attachInfo(context, info)
    # (FW-SRC ActivityThread.java:5720-5722, 6236-6239). Framework
    # edge, no user action.
    r.comment("ActivityThread calls attachInfo on the provider",
              "Eb7d77e9a")

    # E837eed8c -- mStrategy = getPathStrategy(context, info.authority)
    # after the export/grant sanity checks (FileProvider.java:369-376).
    # Internal call, no user action.
    r.comment("attachInfo asks for the path strategy", "E837eed8c")

    # Ecd7e7fc1 -- sCache miss: parse the FILE_PROVIDER_PATHS meta-data
    # (FileProvider.java:556-568). Fresh process, so the authority is
    # not yet cached. Internal call, no user action.
    r.comment("sCache miss, so parsePathStrategy runs", "Ecd7e7fc1")

    # Ee37ab436 -- buildPath(target, path) for each root of
    # filepaths.xml (external-path, cache-path, root-path)
    # (FileProvider.java:594-617; res/xml/filepaths.xml:3-5).
    # Internal call, no user action.
    r.comment("parsePathStrategy calls buildPath for each root",
              "Ee37ab436")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
