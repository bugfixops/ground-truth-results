"""Device route script for Markor route_05.

Method: StoragePermissionActivity.processPermissionState
Printed route: graphs/Markor/scratch/route_print/route_05.txt
Edge ids in order:
  E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E9c895554 E3e6b548b
  Eddc4a6bc E932536b2 E1ee65d00 E02e1ab26 E38d9bf48 E2ff3aaf6 Ee55fac81
  Ec7d30384
ROUTES.csv permissions: WRITE_EXTERNAL_STORAGE
ROUTES.csv fixtures: (none)
Setup: push fixtures/Documents; first-run tutorial can trap a tool
Package: net.gsantner.markor_test
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
from harness import Runner

EDGE_IDS = [
    "E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4", "Eba46a594",
    "E9c895554", "E3e6b548b", "Eddc4a6bc", "E932536b2", "E1ee65d00",
    "E02e1ab26", "E38d9bf48", "E2ff3aaf6", "Ee55fac81", "Ec7d30384",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # No pre-launch permission setup here (rework, audit Finding 3):
    # this flow exists only when the storage permission is missing at
    # launch, so granting it before launch would prevent
    # StoragePermissionActivity from ever starting. See REPORT.md for the
    # remaining ROUTES.csv permissions-column question for the merger.

    # E211966cc: Tap the Markor launcher icon (process start).
    # MainActivity is the MAIN/LAUNCHER activity (AndroidManifest.xml:61-71).
    r.launch("net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: The system calls Application.onCreate -- no user action.
    r.comment("system calls Application.onCreate", "Ed6414d9f")
    # E0254b914: The MAIN/LAUNCHER intent starts MainActivity -- no separate
    # action; the same launcher tap as E211966cc starts it.
    r.comment("same launcher tap as E211966cc starts MainActivity", "E0254b914")
    # Ed25af8f4: The system calls Activity.onCreate -- no user action.
    r.comment("system calls Activity.onCreate", "Ed25af8f4")
    # Eba46a594: The system calls Activity.onStart then onResume -- no action.
    r.comment("system calls onStart then onResume", "Eba46a594")
    # E9c895554: MainActivity.onResume calls
    # StoragePermissionActivity.requestPermissions directly
    # (MainActivity.java:282) -- no user action.
    r.comment("onResume calls requestPermissions", "E9c895554")
    # E3e6b548b: The storage permission is missing, so requestPermissions
    # starts StoragePermissionActivity and finishes MainActivity
    # (StoragePermissionActivity.java:18-22) -- no user action; the
    # resume above fires it.
    r.comment("missing permission starts StoragePermissionActivity",
              "E3e6b548b")
    # Eddc4a6bc: The system calls Activity.onCreate (no own onCreate in
    # StoragePermissionActivity) -- no user action.
    r.comment("system calls base onCreate", "Eddc4a6bc")
    # E932536b2: The system calls onStart then onResume (inherited) -- none.
    r.comment("system calls inherited onStart then onResume", "E932536b2")
    # E1ee65d00: Activity.performResume calls onPostResume -- no user action.
    r.comment("system calls onPostResume", "E1ee65d00")
    # E02e1ab26: Base onPostResume posts onActivityFirstTimeVisible
    # (GsActivityBase.java:101-108; StoragePermissionActivity.java:27-30)
    # -- framework-driven, no user action.
    r.comment("posted onActivityFirstTimeVisible runs", "E02e1ab26")
    # E38d9bf48: onActivityFirstTimeVisible calls askForPermissions
    # directly -- no user action.
    r.comment("onActivityFirstTimeVisible calls askForPermissions",
              "E38d9bf48")
    # E2ff3aaf6: Answer the app's permission dialog with Yes.
    # StoragePermissionActivity.java:35: the dialog's positive button is
    # android.R.string.yes and its callback calls
    # GsContextUtils.requestExternalStoragePermission, which requests
    # WRITE_EXTERNAL_STORAGE (GsContextUtils.java:2401).
    r.tap("E2ff3aaf6", text="Yes")
    # Ee55fac81: Answer the system permission dialog with Allow.
    # The framework then calls onRequestPermissionsResult
    # (StoragePermissionActivity.java:64).
    r.tap("Ee55fac81", text="Allow")
    # Ec7d30384: onRequestPermissionsResult calls processPermissionState
    # directly (StoragePermissionActivity.java:66) -- no user action.
    r.comment("onRequestPermissionsResult calls processPermissionState",
              "Ec7d30384")

    r.done()


if __name__ == "__main__":
    main()
