"""MMEX route_17: Authenticator.addAccount.

Method: Authenticator.addAccount
Edge ids (in route order):
    E5fc12eb9 E608059ee E5e89100e E202d507b
Printed route source:
    graphs/MMEX/scratch/route_print_final2/Authenticator.addAccount.txt
    (edges verified identical to the verification.csv path row for
    Authenticator.addAccount).
Permissions: none (the route's ENV gate is other_app, not a permission
    gate; no runtime grant is needed).
Fixtures: none.
Setup: none (apps.csv MMEX setup is effectively none; this route is
    driven through the system Settings app and never goes through
    MainActivity, so the first-run tutorial / database prerequisite
    does not apply).
Caveat: the tap target below lives in the system Settings UI, not in
    MMEX layout. It is grounded in MMEX's own res/xml/authenticator.xml
    (android:label="@string/app_name") plus res/values/strings.xml:19
    (app_name = "MoneyManagerEx"), which is exactly the label the
    printed route says the Add account list shows. The entry text on
    a given system image is system UI, so confirm it against a real
    dump on the replay image if the tap misses.
Run (from the repo root, after merge to device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_17.py --package
    com.money.manager.ex --log steps/route_17.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E5fc12eb9", "E608059ee", "E5e89100e", "E202d507b",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_17", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E5fc12eb9: Open the system Settings "Add account" list.
        # The printed route's entry is the system Settings app adding
        # an account of type example.com (res/xml/authenticator.xml:20)
        # while AccountManager binds AuthenticatorService
        # (AndroidManifest.xml:455-465, exported=false, intent-filter
        # android.accounts.AccountAuthenticator). The service cannot
        # be bound directly from adb (exported=false, bound by the
        # system AccountManagerService), so the reachable adb path is
        # the Settings Add account screen, which is what the printed
        # route describes.
        r.start_intent(action="android.settings.ADD_ACCOUNT_SETTINGS",
                       edge="E5fc12eb9")
        # E608059ee: Choosing the MMEX entry makes AccountManager bind
        # AuthenticatorService and the framework creates the service,
        # then calls onCreate (sync/adapter/AuthenticatorService.java:
        # 33-37, which constructs the Authenticator). The bind itself
        # is system work triggered by the tap below, so this edge is
        # a comment here and the tap is logged against the next edge.
        r.comment("AccountManager binds AuthenticatorService; framework "
                  "creates the service and calls onCreate",
                  edge="E608059ee")
        # E5e89100e: Tap the MMEX entry in the Add account list.
        # res/xml/authenticator.xml sets android:label="@string/
        # app_name" and res/values/strings.xml:19 gives app_name =
        # "MoneyManagerEx", the label the printed route says the list
        # shows. Tapping it makes the framework call onBind, which
        # returns the authenticator binder (sync/adapter/
        # AuthenticatorService.java:42-45).
        r.tap(text="MoneyManagerEx", edge="E5e89100e")
        # E202d507b: The binder stub dispatches addAccount (sync/
        # adapter/Authenticator.java:43-46). No further tap: addAccount
        # returns null, so no account is created and no further UI
        # appears; that null return is the method's own behaviour,
        # not a script failure.
        r.comment("binder stub dispatches Authenticator.addAccount, "
                  "which returns null (no account created)",
                  edge="E202d507b")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
