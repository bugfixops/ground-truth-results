#!/usr/bin/env python3
"""AnkiDroid step2-item3 route_33: FullSyncer.syncURL.

Method: FullSyncer.syncURL
Table verdict: CORRECT (combined-merge redraw, route_table.md
    row 19). Final-sample method, new to the device set (not in
    the Push-2 ROUTES.csv); route number 33 is new, so no existing
    route number is rebound.
Route followed: the final BFS route (19 steps), identical to the
    redraw print (newsample-routes-30.log): deck picker -> sync on
    resume -> sync(null) -> sync-task post-execute -> sync(download)
    on the fullSync + empty-collection branch -> Connection.sync
    -> SYNC task -> doInBackgroundSync -> FullSyncer.download ->
    HttpSyncer.req chain -> FullSyncer.syncURL.
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b E553ad2d8 E566132dd E9dc72f95
    Ebb41c7a4 Eafa3e29c E6f0d3ce4 Eedf35254 Ed60c6dbd E14a95115
    E0407582b E08b01837 Eb6092981 E90e8c8e9 Ea5042e15 E4ca0f18c
    Ec68f6b60
Preconditions/fixtures:
  - Collection open but empty; full sync with download
    resolution (the empty-collection branch: the sync-task
    listener passes the literal "download" there). Sync runs
    automatically on resume (DeckPicker.java:705), so no user
    action is needed after launch. No file fixture is pushed.
Mapping notes:
  - No GUI steps: every step after launch is automatic.
  - PRE-REAL-RUN CHECK: the drawn print shows no login guard on
    this branch, but the download performs an HTTP request to the
    sync server. If no sync account is configured, the route may
    diverge at the sync step; verify the account/network setup
    before a real run. The script drives the drawn route as
    printed and claims no live run.
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
    "E9dc72f95", "Ebb41c7a4", "Eafa3e29c", "E6f0d3ce4", "Eedf35254",
    "Ed60c6dbd", "E14a95115", "E0407582b", "E08b01837", "Eb6092981",
    "E90e8c8e9", "Ea5042e15", "E4ca0f18c", "Ec68f6b60",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_33")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_33", edge_ids=EDGE_IDS,
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
    # Ebb41c7a4 sync(String)@sync-null -> DeckPicker$17.onPostExecute.
    r.comment("sync task finishes, listener runs", edge="Ebb41c7a4")
    # Eafa3e29c onPostExecute -> sync(String)@sync-download:
    # fullSync + empty-collection branch passes "download".
    r.comment("download resolution taken", edge="Eafa3e29c")
    # E6f0d3ce4 sync(String)@sync-download -> Connection.sync@sync-download.
    r.comment("Connection.sync with download payload", edge="E6f0d3ce4")
    # Eedf35254 Connection.sync -> Connection.doInBackground@SYNC-download.
    r.comment("SYNC task instance created", edge="Eedf35254")
    # Ed60c6dbd doInBackground@SYNC -> doOneInBackground@SYNC-download.
    r.comment("task delegates to doOneInBackground", edge="Ed60c6dbd")
    # E14a95115 doOneInBackground -> doInBackgroundSync@sync-download.
    r.comment("SYNC download branch taken", edge="E14a95115")
    # E0407582b doInBackgroundSync -> FullSyncer.download.
    r.comment("FullSyncer download starts", edge="E0407582b")
    # E08b01837 FullSyncer.download -> HttpSyncer.req(String)@FullSyncer.
    r.comment("sync request issued", edge="E08b01837")
    # Eb6092981 req(String) -> req(String,InputStream).
    r.comment("request overload chain", edge="Eb6092981")
    # E90e8c8e9 req(String,InputStream) -> req(String,InputStream,int).
    r.comment("request overload chain", edge="E90e8c8e9")
    # Ea5042e15 req(...,int) -> req(...,int,JSONObject).
    r.comment("request overload chain", edge="Ea5042e15")
    # E4ca0f18c req(...,JSONObject) -> req(...,JSONObject,CancelCallback).
    r.comment("request overload chain", edge="E4ca0f18c")
    # Ec68f6b60 req(...,CancelCallback) -> FullSyncer.syncURL (target).
    r.comment("syncURL reached (target)", edge="Ec68f6b60")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
