#!/usr/bin/env python3
"""AnkiDroid route_21: CustomTabsFallback.openUri.

Method: CustomTabsFallback.openUri
Target verdict: WRONG (route_table.md route 21)
Route followed: the CORRECTED route, never the printed BFS route.
    hkey-empty NOT_LOGGED_IN variant prefix (sync -> sync(String) with
    hkey empty -> showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC)
    -> variant page -> $1.onPositive -> loginToSyncServer ->
    MyAccount), then the printed tail. The BFS route assembles the
    onPostExecute head onto the variant page and is never used.
    The script uses the menu sync entry, not the onResume entry:
    onResume sync needs mSyncOnResume, which is set only on a
    LOG_IN_FOR_SYNC RESULT_OK return, while any sync() entry reaches
    the same sync(String) step.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b Eb3058057 Ec0803f80 Ea7de4e36
    E09320b5f Eec8a8c70 E76c5b69f E81c3cc95 E2e661eb4 E1380bba5
    Ec1d8317f E8f554e95 E53ecbf1f E18706b49 Ede4b407f
Sources: route_table.md route 21; helper/b6fix-r19-24/
    CORRECTED_ROUTES.md route 21.
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (graph env on
    Eb3058057; see route_16 for the full manifest list).
Fixtures: no sync account configured, so hkey is empty (this is the
    guard that selects the NOT_LOGGED_IN variant, DeckPicker
    .java:1280-1282); MyAccount in STATE_LOG_IN (hkey empty,
    MyAccount.java:92-95); no custom-tabs browser installed, so the
    fallback runs (packageName null, fallback non-null).
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - Menu and dialog selectors ("Sync", the dialog positive button,
    "Sign up") are UI strings not fixed by the graph edges; verify
    each against a live uiautomator dump before a real run.
  - NO LOGIN IS PERFORMED. loginToSyncServer only starts MyAccount;
    the target is reached from the MyAccount login screen by tapping
    Sign up, which opens the register URL. No AnkiWeb account or
    credential is needed, and no step past a login is attempted.
  - The register URL is the https string from MyAccount.java:195-202;
    the script does not type or visit any other URL.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "Eb3058057", "Ec0803f80",
    "Ea7de4e36", "E09320b5f", "Eec8a8c70", "E76c5b69f", "E81c3cc95",
    "E2e661eb4", "E1380bba5", "Ec1d8317f", "E8f554e95", "E53ecbf1f",
    "E18706b49", "Ede4b407f",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_21")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_21", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # Eb3058057 DeckPicker.onCreate -> S_DECKPICKER.
    r.comment("DeckPicker page shown, collection open", edge="Eb3058057")
    # Ec0803f80 S_DECKPICKER -> DeckPicker.onOptionsItemSelected:
    # open the options menu.
    r.tap(edge="Ec0803f80", desc="Sync")
    # Ea7de4e36 DeckPicker.onOptionsItemSelected -> DeckPicker.sync():
    # the menu sync case. Automatic after the tap.
    r.comment("sync requested from menu", edge="Ea7de4e36")
    # E09320b5f DeckPicker.sync() -> DeckPicker.sync(String):
    # sync(null) unconditionally (DeckPicker.java:1267). Automatic.
    r.comment("sync with null argument", edge="E09320b5f")
    # Eec8a8c70 DeckPicker.sync(String) ->
    # DeckPicker.showSyncErrorDialog(int): hkey EMPTY branch, direct
    # to the error dialog (DeckPicker.java:1280-1282). No Connection
    # sync and no onPostExecute run on this branch. Automatic.
    r.comment("hkey empty, error dialog requested", edge="Eec8a8c70")
    # E76c5b69f DeckPicker.showSyncErrorDialog(int) ->
    # DeckPicker.showSyncErrorDialog(int,String). Automatic.
    r.comment("error dialog with message", edge="E76c5b69f")
    # E81c3cc95 DeckPicker.showSyncErrorDialog(int,String) ->
    # S_DLG_SYNC_ERROR_NOT_LOGGED_IN: guard dialog id is
    # DIALOG_USER_NOT_LOGGED_IN_SYNC (0), hkey empty. Automatic.
    r.comment("not-logged-in sync error dialog shown",
              edge="E81c3cc95")
    # E2e661eb4 S_DLG_SYNC_ERROR_NOT_LOGGED_IN ->
    # DeckPicker.loginToSyncServer: the not-logged-in dialog positive
    # button (SyncErrorDialog.java:80-81). Tap it.
    r.tap(edge="E2e661eb4", text="Log in")
    # E1380bba5 DeckPicker.loginToSyncServer -> S_MYACCOUNT:
    # MyAccount started (DeckPicker.java:1570-1573). Automatic.
    # NO LOGIN IS PERFORMED HERE.
    r.comment("MyAccount login screen shown, no login performed",
              edge="E1380bba5")
    # Ec1d8317f S_MYACCOUNT -> MyAccount$3.onClick: tap Sign up in
    # the login view (MyAccount.java:195-202). No account needed.
    r.tap(edge="Ec1d8317f", text="Sign up")
    # E8f554e95 MyAccount$3.onClick -> AnkiActivity.openUrl:
    # openUrl(register_url). Automatic after the tap.
    r.comment("register URL opened", edge="E8f554e95")
    # E53ecbf1f AnkiActivity.openUrl -> CompatV16.openUrl: on API 27
    # CompatV21 does not override openUrl, so CompatV16 runs
    # (CompatHelper.java:35-36, CompatV16.java:77). Automatic.
    r.comment("compat openUrl dispatched", edge="E53ecbf1f")
    # E18706b49 CompatV16.openUrl ->
    # CustomTabActivityHelper.openCustomTab (custom-tab call at
    # CompatV16.java:86). Automatic.
    r.comment("custom tab requested", edge="E18706b49")
    # Ede4b407f CustomTabActivityHelper.openCustomTab ->
    # CustomTabsFallback.openUri: guard no custom-tabs browser
    # installed (packageName null, fallback non-null). Automatic;
    # this is the target edge.
    r.comment("custom-tabs fallback opened the URI",
              edge="Ede4b407f")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
