#!/usr/bin/env python3
"""AnkiDroid step2-item3 route_35: AnkiActivity.openUrl.

Method: AnkiActivity.openUrl
Table verdict: CORRECT (combined-merge redraw, route_table.md
    row 30). Final-sample method, new to the device set (not in
    the Push-2 ROUTES.csv); route number 35 is new, so no existing
    route number is rebound.
Route followed: the final BFS route (11 steps), identical to the
    redraw print (newsample-routes-30.log): deck picker -> sync on
    resume -> sync(null) -> not-logged-in dialog (hkey empty) ->
    Log in tap -> MyAccount -> Sign up tap -> openUrl.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b E553ad2d8 E566132dd E9dc72f95
    Eae5ab93a E2e661eb4 E1380bba5 Ec1d8317f E8f554e95
Preconditions/fixtures:
  - Collection open; not logged in to sync (hkey empty), so
    sync(String) shows the not-logged-in dialog directly without
    launching Connection.sync. No file fixture is pushed.
Mapping notes:
  - Tap texts verified in res (values/04-network.xml):
    sync-error dialog positive "Log in" (log_in, SyncErrorDialog
    DIALOG_USER_NOT_LOGGED_IN_SYNC positive), sign-up button
    "Sign up" (sign_up, my_account.xml sign_up_button).
  - The Sign up tap opens the registration page in an external
    browser via openUrl; the browser itself is outside this
    route's drive.
  - No live run is claimed by this script.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "E566132dd",
    "E9dc72f95", "Eae5ab93a", "E2e661eb4", "E1380bba5", "Ec1d8317f",
    "E8f554e95",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_35")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_35", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("DeckPicker resumed", edge="E553ad2d8")
    # E566132dd onResume -> DeckPicker.sync(): automatic.
    r.comment("sync starts on resume", edge="E566132dd")
    # E9dc72f95 sync() -> sync(String)@sync-null: null resolution.
    r.comment("sync with null resolution", edge="E9dc72f95")
    # Eae5ab93a sync(String)@sync-null -> S_DLG_SYNC_ERROR_NOT_LOGGED_IN:
    # hkey empty, so the not-logged-in dialog shows directly.
    r.comment("not-logged-in sync-error dialog shown", edge="Eae5ab93a")
    # E2e661eb4 S_DLG_SYNC_ERROR_NOT_LOGGED_IN -> DeckPicker.loginToSyncServer:
    # tap the login button of the sync-error dialog.
    r.tap(edge="E2e661eb4", text="Log in")
    # E1380bba5 loginToSyncServer -> S_MYACCOUNT: MyAccount opens.
    r.comment("MyAccount opened for login", edge="E1380bba5")
    # Ec1d8317f S_MYACCOUNT -> MyAccount$3.onClick: tap Sign up.
    r.tap(edge="Ec1d8317f", text="Sign up")
    # E8f554e95 MyAccount$3.onClick -> AnkiActivity.openUrl (target).
    r.comment("openUrl reached (target)", edge="E8f554e95")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
