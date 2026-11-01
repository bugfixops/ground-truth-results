#!/usr/bin/env python3
"""Markor route_30: GsSharedPreferencesPropertyBackend.<init> (cold-start AppSettings init).

Method: GsSharedPreferencesPropertyBackend.<init>
Edge ids in order:
    E211966cc Ed6414d9f Edc435719 E7a4440cf
Printed route file: graphs/Markor/scratch/route_print/route_30.txt
    (verdict correct; method GsSharedPreferencesPropertyBackend.<init>,
    4 steps).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): push fixtures/Documents; first-run tutorial can trap a tool
    (verbatim). run_app.sh does pm clear and pushes fixtures, so this
    script does neither; the target runs in Application.onCreate,
    before any activity or tutorial appears, so no tutorial step is
    needed here.
Route shape: cold start only. Tapping the launcher icon starts the
    process; ApplicationObject.onCreate creates AppSettings, whose
    constructor's super(...) call constructs the preference backend
    (the target). Every edge after the launch is a lifecycle/framework
    or direct internal call with no user action.
GUI mapping evidence:
    - Launcher icon: AndroidManifest.xml declares application
      android:name=".ApplicationObject" and activity
      ".activity.MainActivity" with a MAIN/LAUNCHER intent filter
      (AndroidManifest.xml:63-70 in the clone; the route print cites
      AndroidManifest.xml:39-40 for the entry). The launch is realised
      as r.launch of the fully qualified MainActivity class: the
      manifest class package is net.gsantner.markor, while the replay
      package is net.gsantner.markor_test, so the shorthand
      ".activity.MainActivity" under the test package would resolve
      to a class that does not exist; the full class name is used.
    - ApplicationObject.java:39 onCreate, :42 new AppSettings(...).
    - AppSettings.java:73 (bytecode; constructor source):
      "super(context, SHARED_PREF_APP);" -- AppSettings extends
      GsSharedPreferencesPropertyBackend.
    - GsSharedPreferencesPropertyBackend.java:72: backend constructor
      "public GsSharedPreferencesPropertyBackend(final Context context,
      final String prefAppName)".
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
from harness import Runner  # noqa: E402

EDGE_IDS = [
    "E211966cc",
    "Ed6414d9f",
    "Edc435719",
    "E7a4440cf",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Markor route_30 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_30", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # No permissions listed in ROUTES.csv for this route: no grant().

    # E211966cc -- Tap the Markor launcher icon (ENTRY; the process
    # starts when the launcher icon is tapped, before any activity).
    # Realised as launching MainActivity, the adb equivalent of the
    # launcher tap (MAIN/LAUNCHER, AndroidManifest.xml:63-70).
    r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
             "E211966cc")

    # Ed6414d9f -- The system calls Application.onCreate (LIFECYCLE).
    # No user action; the system performs this step.
    r.comment("system calls ApplicationObject.onCreate", "Ed6414d9f")

    # Edc435719 -- ApplicationObject.onCreate -> AppSettings.<init>
    # (CALL, direct call; ApplicationObject.java:42). No user action.
    r.comment("onCreate creates AppSettings", "Edc435719")

    # E7a4440cf -- AppSettings.<init> ->
    # GsSharedPreferencesPropertyBackend.<init> (CALL, direct call;
    # AppSettings.java:73 bytecode, super(context, SHARED_PREF_APP)).
    # No user action.
    r.comment("AppSettings super call constructs backend (target)",
              "E7a4440cf")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
