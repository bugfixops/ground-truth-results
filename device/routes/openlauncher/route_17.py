"""route_17: DeviceAdminReceiver.onReceive.

Method: DeviceAdminReceiver.onReceive
Edge ids (ROUTES.csv order): E15938fe2, E52bc2f77
Printed route file: graphs/openlauncher/scratch/overnight-20261101/
    scratch-outputs/routes_27_full.txt (route_17 section), cross-checked
    against graphs/openlauncher/verification.csv (path row route_17) and
    out/openlauncher_trigger_graph.json.
Permissions: none. BIND_DEVICE_ADMIN in AndroidManifest.xml:84-94 is the
    receiver's own permission attribute, not a runtime permission, so it
    is not granted or listed (see ROUTES_NOTES.md, route_17 note).
Fixtures: none. Setup: none (openlauncher has no setup; run_app.sh does
    pm clear before invoking this script).

Trigger: the user activates OpenLauncher as a device administrator, the
system sends DEVICE_ADMIN_ENABLED to the manifest receiver, and the
receiver's onReceive runs (empty body, util/DeviceAdminReceiver.java:7-12).
"""

import argparse
import os
import sys

# Repo-root derivation (corrected; see helper REPORT.md).
# __file__ here is device/routes/openlauncher/route_17.py, so
# dirname(abspath(__file__)) is device/routes/openlauncher/ and three
# further dirnames give routes -> device -> the repo root. Three
# dirnames from __file__ itself would land on device/ and the import
# below would fail (verified from a sibling helper's failure).
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, REPO_ROOT)

from device.harness import Runner  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--adb", default="adb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_17",
               edge_ids=["E15938fe2", "E52bc2f77"],
               log_path=args.log, dry_run=args.dry_run,
               adb=args.adb, outdir=args.outdir)

    # E15938fe2: S_ENTRY -> DeviceAdminReceiver.<init> --
    # "The user activates OpenLauncher as device admin: the system sends
    # DEVICE_ADMIN_ENABLED to the manifest receiver" (trigger graph).
    # The trigger gui lists the Settings path (Security > Device
    # administrators > activate OpenLauncher). Settings menu labels vary
    # by emulator image, so this script opens the same system screen
    # directly with the documented ADD_DEVICE_ADMIN intent, which the
    # Settings path itself reaches (DeviceAdminAdd). The receiver
    # component is the manifest receiver (AndroidManifest.xml:84-94).
    r.start_intent(
        edge="E15938fe2",
        action="android.app.action.ADD_DEVICE_ADMIN",
        extras={"android.app.extra.DEVICE_ADMIN":
                "com.benny.openlauncher/"
                "com.benny.openlauncher.util.DeviceAdminReceiver"})
    # Activate button wording varies by AOSP image ("Activate this
    # device admin app" vs "Activate"); try the long form first, then
    # the short form. In dry mode the first tap is planned and the
    # fallback is never reached.
    try:
        r.tap(text="Activate this device admin app", edge="E15938fe2")
    except (LookupError, RuntimeError):
        r.tap(text="Activate", edge="E15938fe2")

    # E52bc2f77: DeviceAdminReceiver.<init> -> DeviceAdminReceiver.onReceive
    # -- "BroadcastReceiver.onReceive (empty body)". No user action: the
    # activation broadcast delivers onReceive, whose body is empty
    # (util/DeviceAdminReceiver.java:7-12).
    r.comment("DeviceAdminReceiver.onReceive: empty body; delivered by "
              "the DEVICE_ADMIN_ENABLED broadcast on activation",
              edge="E52bc2f77")
    r.screenshot("route_17_done", edge="E52bc2f77")

    r.done()


if __name__ == "__main__":
    main()
