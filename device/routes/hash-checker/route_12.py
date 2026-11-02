#!/usr/bin/env python3
"""Device replay script for hash-checker route_12.

Method: MainActivity.getConfiguredBundleWithDataUri
Edges: E3706e5f1 Ebbb4dd85 E362db005 Ef8a9b253 Ea2fd772c
Printed route: graphs/hash-checker/scratch/route_print/MainActivity.getConfiguredBundleWithDataUri.txt
Permissions: none
Fixtures: Download/todo.txt (pushed to /sdcard/Download/todo.txt by run_app.sh)
Setup: any file as input (fixtures)

Flow: this is the other-app VIEW route. The script itself sends the
VIEW intent; there is no launcher launch, because a MAIN launch would
not carry a data URI. The intent is explicit (component set), with a
file:// data URI for the pushed fixture. MainActivity.create accepts
a content or file scheme (MainActivity.java:82-88), so the file
scheme satisfies the edge guard "intent scheme is content/file, or
ClipData present". An implicit intent was not used: the manifest VIEW
filter declares only the content scheme, so a file:// URI would not
match it implicitly, and the SEND filter carries CATEGORY_LAUNCHER
rather than DEFAULT, so the app is not offered in the share sheet;
only an explicit intent works (printed-route note on E3706e5f1).
The activity class is the manifest package
(com.smlnskgmail.jaman.hashchecker) plus .MainActivity, launched under
the flavor applicationId passed as --package.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

EDGES = ["E3706e5f1", "Ebbb4dd85", "E362db005", "Ef8a9b253", "Ea2fd772c"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    args = ap.parse_args()

    runner = Runner(package=args.package, route="route_12", edge_ids=EDGES,
                    log_path=args.log, dry_run=args.dry_run, adb=args.adb,
                    outdir=args.outdir)
    try:
        # E3706e5f1 S_ENTRY -> MainActivity.<init>@XURI
        # Trigger: another app sends an explicit VIEW intent with a
        # content:// URI (filter F2), or an explicit SEND with ClipData.
        # Sent here: explicit VIEW, file:// URI of the pushed fixture.
        # run_app.sh pushes the fixture to /sdcard/Download/todo.txt.
        runner.start_intent("E3706e5f1",
                            action="android.intent.action.VIEW",
                            data="file:///sdcard/Download/todo.txt",
                            component=args.package + "/com.smlnskgmail.jaman.hashchecker.MainActivity")
        # Ebbb4dd85 MainActivity.<init>@XURI -> MainActivity.onCreate@XURI
        # Trigger: the system instantiates MainActivity, then calls onCreate.
        runner.comment("lifecycle: MainActivity.onCreate (XURI)", "Ebbb4dd85")
        # E362db005 MainActivity.onCreate@XURI -> BaseActivity.onCreate@MainActivity_XURI
        # Trigger: direct call (super.onCreate).
        runner.comment("call: super.onCreate (XURI)", "E362db005")
        # Ef8a9b253 BaseActivity.onCreate@MainActivity_XURI -> MainActivity.create@XURI
        # Trigger: direct call (create()).
        runner.comment("call: create() (XURI)", "Ef8a9b253")
        # Ea2fd772c MainActivity.create@XURI -> MainActivity.getConfiguredBundleWithDataUri
        # Trigger: VIEW (content/file scheme) or SEND with ClipData:
        # bundle with the URI. The calculator then validates the file,
        # so the From button reads "File" (strings common_file).
        runner.wait_for("Ea2fd772c", text="File")
        runner.comment("call: getConfiguredBundleWithDataUri (target)",
                      "Ea2fd772c")
    finally:
        runner.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
