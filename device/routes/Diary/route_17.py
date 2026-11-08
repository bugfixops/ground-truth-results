#!/usr/bin/env python3
"""Diary device route script: route_17.

Method: Diary.onRequestPermissionsResult
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Eced89c46 Ef166af87 E0ccb250b Edfef477b Ee0b1fbde
Printed route file: graphs/Diary/scratch route print for
    Diary.onRequestPermissionsResult, in
    ~/workspace/overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.onRequestPermissionsResult", verdict REACHABLE) and
    route_judgements.txt line 17 (correct, SOURCE, Diary.java:2212-2245).
Permissions (ROUTES.csv, all declared in AndroidManifest.xml:26-29):
    android.permission.WRITE_EXTERNAL_STORAGE
    android.permission.READ_EXTERNAL_STORAGE
    android.permission.WRITE_CALENDAR
    android.permission.READ_CALENDAR
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (Diary row of work-emulator ci/apps.csv has an
    empty setup cell).

Route summary (from the printed route and the trigger graph): launch
Diary from the launcher; onCreate takes the launcher branch today()
(Diary.java:497-512), which calls changeDate (Diary.java:2610-2617),
which calls load() (Diary.java:2573-2581). load() finds
READ_EXTERNAL_STORAGE not granted and calls requestPermissions with all
four permissions and REQUEST_READ, then returns (Diary.java:2400-2412).
Answering the system dialog calls onRequestPermissionsResult
(Diary.java:2212-2245); the REQUEST_READ branch reloads on
READ_EXTERNAL_STORAGE granted.

Permission handling -- read this before moving any line:
- The gate edge Edfef477b fires ONLY while the permissions are not
  granted. run_app.sh installs without auto-grant and runs pm clear
  first, so a fresh run starts ungranted; the script additionally
  revokes all four up front (r.deny, a no-op on a fresh install) so the
  gate holds even if the script is run standalone.
- The four r.grant calls are attached to the dialog edge Ee0b1fbde,
  AFTER the Allow tap, where they mirror the Allow outcome (a no-op
  once the dialog has granted them). They grant exactly the ROUTES.csv
  permissions and nothing else. They MUST NOT be moved before the
  launch: pre-granting would make load() skip requestPermissions, the
  dialog would never appear, and the route target would never fire.
- The Allow tap uses the dialog button text from the trigger text
  ("Tap Allow (or Deny)"). On emulator images whose permission dialog
  offers "While using the app" instead of "Allow", that button is the
  Allow equivalent and the tap text needs updating for that image.
- Lifecycle and CALL edges with no user action are logged with
  r.comment, per the D3 rules.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

PKG = "org.billthefarmer.diary"
ROUTE = "route_17"
EDGES = ["Ee6b8aa80", "Edd0b9192", "Eced89c46", "Ef166af87", "E0ccb250b",
         "Edfef477b", "Ee0b1fbde"]
# Exactly the ROUTES.csv permissions, in ROUTES.csv order. Nothing else
# is granted or revoked by this script.
PERMS = ["android.permission.WRITE_EXTERNAL_STORAGE",
         "android.permission.READ_EXTERNAL_STORAGE",
         "android.permission.WRITE_CALENDAR",
         "android.permission.READ_CALENDAR"]
DIARY = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route=ROUTE, edge_ids=EDGES,
               log_path=a.log, dry_run=a.dry_run, adb=a.adb,
               outdir=a.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher (MAIN/LAUNCHER
        # intent filter, AndroidManifest.xml:52-59). Setup first:
        # revoke all four ROUTES.csv permissions so the Edfef477b gate
        # (permissions not granted yet) holds; then launch the Diary
        # activity, the adb equivalent of the launcher tap.
        for perm in PERMS:
            r.deny(perm, edge="Ee6b8aa80")
        r.launch(DIARY, edge="Ee6b8aa80")
        # Edd0b9192 -- The system instantiates Diary, then onCreate
        # (Diary.java:441-443). No user action.
        r.comment("system instantiates Diary, then onCreate",
                  edge="Edd0b9192")
        # Eced89c46 -- Started from the launcher (no widget extra):
        # today() (Diary.java:497-512). No user action.
        r.comment("launcher start: today()", edge="Eced89c46")
        # Ef166af87 -- entryStack.clear(); changeDate(today's date)
        # (Diary.java:2610-2617). No user action.
        r.comment("today calls changeDate for today's date",
                  edge="Ef166af87")
        # E0ccb250b -- load() the entry of the start date; shown is
        # already true (Diary.java:2573-2581). No user action.
        r.comment("changeDate calls load for the start date",
                  edge="E0ccb250b")
        # Edfef477b -- No READ_EXTERNAL_STORAGE: requestPermissions(...
        # REQUEST_READ) and return (Diary.java:2400-2412). The system
        # shows the permission dialog. No user action.
        r.comment("load finds storage permission missing, requests "
                  "REQUEST_READ and returns; system shows dialog",
                  edge="Edfef477b")
        # Ee0b1fbde -- Tap Allow (or Deny) in the permission dialog
        # (REQUEST_READ). Allow is tapped so the REQUEST_READ branch
        # (Diary.java:2212-2245) reloads on READ_EXTERNAL_STORAGE
        # granted. The grant calls below mirror that Allow outcome;
        # see the header note -- they must stay after the tap.
        r.tap(edge="Ee0b1fbde", text="Allow")
        for perm in PERMS:
            r.grant(perm, edge="Ee0b1fbde")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
