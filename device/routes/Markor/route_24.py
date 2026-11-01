"""Device route script: route_24.

Method: GsSharedPreferencesPropertyBackend.gp
Printed route file: graphs/Markor/scratch/route_print/route_24.txt
Edge ids in order:
  E211966cc Ed6414d9f Edc435719 Eab4b9c7d E107691bf E06d84d50
ROUTES.csv permissions: (none)
ROUTES.csv fixtures: (none)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test

Replay: cold-start MainActivity only. Application.onCreate constructs
AppSettings (ApplicationObject.java:42); on a fresh install / after
run_app.sh's pm clear, the stored basic-colour-scheme key is absent, so
AppSettings.<init> takes the -999 branch (AppSettings.java:79) and calls
setEditorBasicColor, which writes the colours via setInt -> gp.
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
    r = Runner(package=args.package, route="route_24",
               edge_ids=["E211966cc", "Ed6414d9f", "Edc435719", "Eab4b9c7d",
                         "E107691bf", "E06d84d50"],
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
    # Eab4b9c7d: AppSettings.setEditorBasicColor -- direct call
    # (AppSettings.java:81). It runs on a fresh start because the
    # basic-colour-scheme key reads -999 (AppSettings.java:79) after
    # run_app.sh's pm clear; no user action.
    r.comment("direct call: setEditorBasicColor (fresh-prefs branch), "
              "no user action", "Eab4b9c7d")
    # E107691bf: GsSharedPreferencesPropertyBackend.setInt -- direct
    # call (AppSettings.java:721: setEditorBasicColor writes fg/bg via
    # setInt); no user action.
    r.comment("direct call: setInt, no user action", "E107691bf")
    # E06d84d50: GsSharedPreferencesPropertyBackend.gp -- direct call
    # (GsSharedPreferencesPropertyBackend.java:269: setInt resolves the
    # SharedPreferences via gp); no user action.
    r.comment("direct call: gp, no user action", "E06d84d50")
    r.done()


if __name__ == "__main__":
    main()
