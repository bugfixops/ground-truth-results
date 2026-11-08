#!/usr/bin/env python3
"""Device replay script for hash-checker route_24.

Method: SharedPreferencesSettings.saveStringPreference
Printed route: graphs/hash-checker/scratch/route_print/SharedPreferencesSettings.saveStringPreference.txt
Edge ids (in route order, from ROUTES.csv):
    E34de2c31 E7aab529b E05dade98 Eef3f66b5 E5c325194 E7b74b251
Permissions: (none)
Fixtures: (none)
Setup: any file as input (fixtures)
Status in ROUTES.csv: scripted

FIRST-LAUNCH ASSUMPTION (read before running): edge Eef3f66b5 carries
the guard "preference key_language is not stored yet: first launch after
install (if !settings.languageIsInitialized(), App.java:154)". This
script is therefore scriptable ONLY on a fresh install / cleared app
data. run_app.sh guarantees that with pm clear before each script; this
script itself performs NO clearing, fixture push, or permission grant.

One script block per route edge, in route order. This whole route runs
inside Application.onCreate, before any activity is visible, so every
edge except the launch is a comment(); the final block waits for the
main screen only to prove App.onCreate completed and the app reached
the calculator screen. Launching MainActivity is what creates the App
object: Android instantiates the Application before any component.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

EDGE_IDS = [
    "E34de2c31", "E7aab529b", "E05dade98", "Eef3f66b5", "E5c325194",
    "E7b74b251",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()
    runner = Runner(package=args.package, route="route_24",
                    edge_ids=EDGE_IDS, log_path=args.log,
                    dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E34de2c31: S_ENTRY -> App.<init>
        # Trigger: "Android starts the app process; the Application object
        # is created before any component". Launching the launcher
        # activity is the way to start the process; the manifest package
        # is com.smlnskgmail.jaman.hashchecker, so .MainActivity resolves
        # under the flavor applicationId given by --package. App is the
        # android:name=".App" application in AndroidManifest.xml:9.
        runner.launch(args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity",
                      "E34de2c31")
        # E7aab529b: App.<init> -> App.onCreate
        # Trigger: "Application.onCreate runs right after construction"
        # (App.java:53). Lifecycle edge, no user action.
        runner.comment("lifecycle: App.onCreate", "E7aab529b")
        # E05dade98: App.onCreate -> App.setLocale
        # Trigger: "Direct call" (App.java:80).
        runner.comment("call: App.setLocale", "E05dade98")
        # Eef3f66b5: App.setLocale -> LanguageConfigImpl.setLanguage(Language)
        # Trigger: "Virtual/interface call that can dispatch to this
        # implementation" (App.java:165). Guard: first launch only
        # (language not yet initialised); guaranteed by run_app.sh pm
        # clear before this script, NOT by any step here.
        runner.comment("call: LanguageConfigImpl.setLanguage (first-launch guard)",
                       "Eef3f66b5")
        # E5c325194: LanguageConfigImpl.setLanguage(Language) ->
        # SharedPreferencesSettings.saveLanguage
        # Trigger: "Virtual/interface call that can dispatch to this
        # implementation" (LanguageConfigImpl.java:28).
        runner.comment("call: SharedPreferencesSettings.saveLanguage", "E5c325194")
        # E7b74b251: SharedPreferencesSettings.saveLanguage ->
        # SharedPreferencesSettings.saveStringPreference
        # Trigger: "Direct call" (SharedPreferencesSettings.java:59).
        # saveStringPreference writes to SharedPreferences: no UI of its
        # own. Observable used: the calculator screen appears once
        # App.onCreate (which contains this whole chain) has finished
        # (fragment_hash_calculator.xml, tv_selected_hash_type).
        runner.wait_for("E7b74b251",
                        res_id=args.package + ":id/tv_selected_hash_type")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
