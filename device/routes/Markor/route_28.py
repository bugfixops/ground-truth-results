#!/usr/bin/env python3
"""Markor route_28: GsSharedPreferencesPropertyBackend.getInt(String,int,SharedPreferences[]).

Method: GsSharedPreferencesPropertyBackend.getInt(String,int,SharedPreferences[])
Edge ids in order:
    E211966cc Ed6414d9f Edc435719 E24788e7f E93ccbb11
Printed route file: graphs/Markor/scratch/route_print/route_28.txt
    (verdict correct; method getInt(String,int,SharedPreferences[]),
    5 steps).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): push fixtures/Documents; first-run tutorial can trap a tool
    (verbatim). run_app.sh does pm clear and pushes fixtures, so this
    script does neither; the target runs in Application.onCreate,
    before any activity or tutorial appears, so no tutorial step is
    needed here.
Route shape: cold start only. Tapping the launcher icon starts the
    process; ApplicationObject.onCreate creates AppSettings, whose
    constructor reads an int preference via the int-resource overload
    of getInt, which delegates to the String overload (the target).
    Every edge after the launch is a lifecycle/framework or direct
    internal call with no user action.
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
    - AppSettings.java:79: constructor guard "if (getInt(R.string.
      pref_key__basic_color_scheme__bg_light, -999) == -999)".
    - GsSharedPreferencesPropertyBackend.java:277 (bytecode):
      getInt(int,...) delegates to getInt(String,...); source
      getInt(@StringRes...) returns getInt(rstr(keyResourceId),...).
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
    "E24788e7f",
    "E93ccbb11",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Markor route_28 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(package=args.package, route="route_28", edge_ids=EDGE_IDS,
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

    # E24788e7f -- AppSettings.<init> ->
    # GsSharedPreferencesPropertyBackend.getInt(int,int,
    # SharedPreferences[]) (CALL, direct call; AppSettings.java:79
    # bytecode). No user action.
    r.comment("AppSettings constructor reads int preference via getInt",
              "E24788e7f")

    # E93ccbb11 -- getInt(int,...) -> getInt(String,int,
    # SharedPreferences[]) (CALL, direct call;
    # GsSharedPreferencesPropertyBackend.java:277 bytecode). No user
    # action.
    r.comment("int overload delegates to String overload (target)",
              "E93ccbb11")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
