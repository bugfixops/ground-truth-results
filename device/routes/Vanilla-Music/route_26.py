"""Device replay script for Vanilla-Music route_26.

Method: PermissionRequestActivity.onRequestPermissionsResult
Edge ids: E47380ade E0fd35a14 Eb667910e E1adb6602 Ed86f23af E8799b914
    E9c3875c1 E10cdb1ad
Printed route source: graphs/Vanilla-Music/verification.csv path row
    (result correct; ref LibraryActivity.java:188;
    PermissionRequestActivity.java:96-105,105,118-126,41-50,60-61) and
    device/routes/Vanilla-Music/ROUTES.csv route_26.
Permissions (ROUTES.csv): android.permission.READ_EXTERNAL_STORAGE;
    android.permission.WRITE_EXTERNAL_STORAGE. These are the REQUEST SET
    of the permission dialog, not pre-grants: this route IS the
    permission flow, so the script revokes both first (fresh-install /
    ungranted start state). If run_app pre-granted them, the warning
    banner would never appear and the route could not run; see
    ROUTES_NOTES.md ambiguity 5.
Fixtures: none (no STATE file gate).
Setup: push fixtures/Music + media scan (run_app setup step).
Standard config: run_app does pm clear before this script; the script
    starts by launching the app.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

PKG_DEFAULT = "ch.blinkenlights.android.vanilla"
EDGE_IDS = ["E47380ade", "E0fd35a14", "Eb667910e", "E1adb6602", "Ed86f23af",
            "E8799b914", "E9c3875c1", "E10cdb1ad"]
BANNER = "Vanilla Music needs read permission to display your music library"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route="route_26", edge_ids=EDGE_IDS,
               log_path=a.log, dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    # E47380ade: S_ENTRY -> LibraryActivity.<init>
    # MAIN / LAUNCHER intent starts LibraryActivity.
    # Revoke the request set first: this route must start ungranted.
    r.deny("android.permission.READ_EXTERNAL_STORAGE", "E47380ade")
    r.deny("android.permission.WRITE_EXTERNAL_STORAGE", "E47380ade")
    r.launch("ch.blinkenlights.android.vanilla/.LibraryActivity",
             "E47380ade")
    # E0fd35a14: LibraryActivity.<init> -> LibraryActivity.onCreate
    # Activity lifecycle callback; no user action.
    r.comment("lifecycle: onCreate runs on launch", "E0fd35a14")
    # Eb667910e: LibraryActivity.onCreate -> PermissionRequestActivity.showWarning
    # Direct call; the warning banner is inflated into the library layout.
    r.comment("direct call: showWarning inflates the banner", "Eb667910e")
    # E1adb6602: showWarning -> PermissionRequestActivity$1.onClick
    # Tap the storage permission warning banner.
    r.wait_for("E1adb6602", text=BANNER, timeout=30)
    r.tap("E1adb6602", text=BANNER)
    # Ed86f23af: $1.onClick -> requestPermissions. Direct call.
    r.comment("direct call: banner click invokes requestPermissions",
              "Ed86f23af")
    # E8799b914: requestPermissions -> PermissionRequestActivity.<init>
    # havePermissions is false, so the activity is started; no action.
    r.comment("activity start: system creates PermissionRequestActivity",
              "E8799b914")
    # E9c3875c1: PermissionRequestActivity.<init> -> onCreate.
    # Activity lifecycle callback; no user action.
    r.comment("lifecycle: onCreate runs on activity start", "E9c3875c1")
    # E10cdb1ad: onCreate -> onRequestPermissionsResult
    # requestPermissions(allPerms, 0): answer the system dialog. Either
    # answer reaches onRequestPermissionsResult; Allow keeps the library
    # usable downstream.
    r.tap("E10cdb1ad", text="Allow")
    r.done()


if __name__ == "__main__":
    main()
