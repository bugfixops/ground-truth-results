"""Device route script: route_25.

Method: GsSharedPreferencesPropertyBackend.rstr
Printed route file: graphs/Markor/scratch/route_print/route_25.txt
Edge ids in order:
  E211966cc Ed6414d9f Edc435719 E24788e7f E99bf0b9a
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: (none)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Replay: cold-start MainActivity only. Application.onCreate constructs
AppSettings (ApplicationObject.java:42); AppSettings.<init> reads an
int preference (AppSettings.java:79), and that getInt resolves its key
resource via rstr (GsSharedPreferencesPropertyBackend.java:277).
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
    r = Runner(package=args.package, route="route_25",
               edge_ids=["E211966cc", "Ed6414d9f", "Edc435719", "E24788e7f",
                         "E99bf0b9a"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # No permissions listed in ROUTES.csv for this route, so no grant().
    # No fixtures listed for this route.
    # E211966cc: Tap the Markor launcher icon (process start).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: The system calls Application.onCreate -- no user action.
    # ApplicationObject.onCreate (ApplicationObject.java:39-42) is where
    # the next edge's AppSettings construction happens.
    r.comment("system lifecycle: Application.onCreate, no user action",
              "Ed6414d9f")
    # Edc435719: AppSettings.<init> -- direct call from
    # ApplicationObject.onCreate (ApplicationObject.java:42); no action.
    r.comment("direct call: AppSettings.<init>, no user action",
              "Edc435719")
    # E24788e7f: GsSharedPreferencesPropertyBackend.getInt -- direct
    # call (AppSettings.java:79: the constructor's -999 check reads the
    # basic-colour-scheme int preference); no user action.
    r.comment("direct call: getInt, no user action", "E24788e7f")
    # E99bf0b9a: GsSharedPreferencesPropertyBackend.rstr -- direct call
    # (GsSharedPreferencesPropertyBackend.java:277: getInt resolves the
    # key resource id to a string via rstr); no user action.
    r.comment("direct call: rstr, no user action", "E99bf0b9a")
    r.done()


if __name__ == "__main__":
    main()
