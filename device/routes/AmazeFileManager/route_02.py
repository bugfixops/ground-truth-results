#!/usr/bin/env python3
"""AmazeFileManager route_02: FtpTileService.updateTileState.

Method: FtpTileService.updateTileState
Edge ids in order:
    Ef3576ae6 E4512b299 E8b69c932 Ef53ae484 E512ff7b5 E50e05168
    E0de2e376 E4da5d596 E134a9011 E383481b2 Ec90f8f52
Printed route: graphs/AmazeFileManager/scratch/route_print/
    FtpTileService.updateTileState.txt, verdict REACHABLE, 11 edges.
    This edge list matches methods.csv route_edge_ids for
    FtpTileService.updateTileState exactly and matches the D1 draft
    route_02 row exactly; no mismatch.
Permissions: WRITE_EXTERNAL_STORAGE (ROUTES.csv decision). MainActivity
    extends PermissionsActivity and requests storage permission on
    launch when missing (MainActivity.java:438-439); granting it in
    ROUTES.csv keeps the first-run permission gate from blocking the
    drawer steps. The FTP server itself needs no runtime permission.
Fixtures: none. Setup: the device/emulator must satisfy the network
    guard in the Start tap (see below); otherwise the lambda takes
    its no-connection branch and the route stops. Standard config:
    run_app.sh starts from `pm clear` and grants only the ROUTES.csv
    permissions above.

Mapping notes (printed source evidence):
  - MainActivity is the MAIN/LAUNCHER activity
    (AndroidManifest.xml:58, intent filter :61-65), so the script
    launches com.amaze.filemanager.debug/.activities.MainActivity.
  - The drawer toggle carries the "open drawer" description
    (Drawer.java:221, R.string.drawer_open = "Open navigation
    drawer", strings.xml:25), so the script opens the drawer by
    tapping that content description.
  - The drawer row is R.string.ftp = "FTP Server" (strings.xml:30);
    Drawer.java:402-414 builds that row and its lambda replaces
    R.id.content_frame with a new FtpServerFragment. Drawer.java:597
    dispatches the tap to the lambda and Drawer.java:535 commits
    the transaction on drawer close.
  - The trigger of this route is the IN-APP Start button, not a
    Quick Settings tile tap: FtpServerFragment.onCreateView inflates
    fragment_ftp (FtpServerFragment.java:100-104), binds ftpBtn to
    R.id.startStopButton (fragment_ftp.xml, button text
    @string/start_ftp = "Start", strings.xml:296, shown uppercased
    as "START" while stopped), and registers the click lambda at
    FtpServerFragment.java:132. The script therefore taps the
    button by resource id startStopButton, which is stable whether
    the label reads START or STOP.
  - Network guard on that tap (FtpServerFragment.java:132-147):
    startServer() runs only if isConnectedToWifi, or
    isConnectedToLocalNetwork, or isEnabledWifiHotspot. The local-
    network check accepts TYPE_ETHERNET or an rndis interface
    (FtpService.java:271-290), which an emulator's virtual network
    normally satisfies; a device with no network at all takes the
    no-connection branch instead (status text only, no broadcast).
  - Downstream chain is all framework/service dispatch, logged with
    r.comment: startServer() broadcasts ACTION_START_FTPSERVER
    (FtpServerFragment.java:376; receiver registered in the
    manifest at :206), FtpReceiver starts the service
    (FtpReceiver.java:24), FtpService.onStartCommand runs
    (FtpService.java:119-142) and its run() posts an EventBus event
    (FtpService.java:227) to the @Subscribe method
    (FtpTileService.java:26), which calls updateTileState()
    (FtpTileService.java:28).
  - Known replay caveat, recorded not hidden: FtpTileService
    registers for EventBus only in onStartListening
    (FtpTileService.java:31-35), i.e. while the tile is listening.
    The harness cannot add a Quick Settings tile (system UI it
    cannot drive), so if the replay log shows the EventBus post
    without an updateTileState call, the gap is tile registration,
    not the in-app trigger chain this script drives. The route is
    still scripted because its printed trigger is the in-app
    toggle, and every edge up to the EventBus post is drivable.
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ef3576ae6", "E4512b299", "E8b69c932", "Ef53ae484", "E512ff7b5",
    "E50e05168", "E0de2e376", "E4da5d596", "E134a9011", "E383481b2",
    "Ec90f8f52",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Amaze route_02")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_02", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ef3576ae6 S_ENTRY -> Drawer.onNavigationItemSelected: launch
    # MainActivity (MAIN/LAUNCHER) and open the navigation drawer.
    # The drawer toggle description is "Open navigation drawer"
    # (Drawer.java:221, strings.xml:25).
    r.launch(args.package + "/.activities.MainActivity", "Ef3576ae6")
    r.tap("Ef3576ae6", desc="Open navigation drawer")
    # The "FTP Server" row sits in the LASTGROUP rows at the end of
    # the drawer list (Drawer.java:402-414), so scroll to it first.
    r.scroll_to("Ef3576ae6", text="FTP Server")
    # E4512b299 Drawer.onNavigationItemSelected -> FtpServerFragment
    # .<init>: tap the "FTP Server" row (R.string.ftp,
    # strings.xml:30). Its lambda replaces content_frame with a new
    # FtpServerFragment (Drawer.java:402-414, dispatched at :597,
    # committed on drawer close at :535).
    r.tap("E4512b299", text="FTP Server")
    # E8b69c932 FtpServerFragment.<init> -> FtpServerFragment
    # .onCreate: fragment lifecycle. No user action.
    r.comment("fragment lifecycle: onCreate runs", "E8b69c932")
    # Ef53ae484 FtpServerFragment.onCreate -> FtpServerFragment
    # .onCreateView: onCreateView inflates R.layout.fragment_ftp
    # (FtpServerFragment.java:100-104). No user action.
    r.comment("onCreateView inflates fragment_ftp "
              "(FtpServerFragment.java:100-104)", "Ef53ae484")
    # E512ff7b5 FtpServerFragment.onCreateView -> FtpServerFragment
    # .lambda$onCreateView$0: ftpBtn.setOnClickListener registers
    # the lambda (FtpServerFragment.java:132). Registration only;
    # the tap itself is the next edge.
    r.comment("ftpBtn.setOnClickListener registers lambda "
              "(FtpServerFragment.java:132)", "E512ff7b5")
    # E50e05168 FtpServerFragment.lambda$onCreateView$0 ->
    # FtpServerFragment.startServer: tap the Start button. Tapped by
    # resource id startStopButton (fragment_ftp.xml; bound at
    # FtpServerFragment.java:112) so the tap is stable whether the
    # label reads START (stopped) or STOP (running). The lambda
    # calls startServer() only when not already running and a
    # Wi-Fi / local-network / hotspot connection exists
    # (FtpServerFragment.java:132-147; local-network check accepts
    # ethernet or rndis at FtpService.java:271-290).
    r.wait_for("E50e05168", res_id="startStopButton")
    r.tap("E50e05168", res_id="startStopButton")
    # E0de2e376 FtpServerFragment.startServer -> FtpReceiver
    # .onReceive: startServer() sends the ACTION_START_FTPSERVER
    # broadcast (FtpServerFragment.java:376; receiver in the
    # manifest at :206). No user action beyond the tap above.
    r.comment("startServer broadcasts ACTION_START_FTPSERVER "
              "(FtpServerFragment.java:376)", "E0de2e376")
    # E4da5d596 FtpReceiver.onReceive -> FtpService.<init>: the
    # receiver starts the service (FtpReceiver.java:24). Framework;
    # no user action.
    r.comment("FtpReceiver starts FtpService (FtpReceiver.java:24)",
              "E4da5d596")
    # E134a9011 FtpService.<init> -> FtpService.onStartCommand:
    # framework calls onStartCommand after the service starts
    # (FtpService.java:119-142). No user action.
    r.comment("framework calls FtpService.onStartCommand "
              "(FtpService.java:119-142)", "E134a9011")
    # E383481b2 FtpService.onStartCommand -> FtpTileService
    # .onFtpReceiverActions: FtpService.run() posts the
    # FtpReceiverActions event (FtpService.java:227), dispatched by
    # EventBus to the @Subscribe method (FtpTileService.java:26).
    # Framework/async dispatch; no user action.
    r.comment("EventBus post (FtpService.java:227) dispatches to "
              "@Subscribe onFtpReceiverActions (FtpTileService.java"
              ":26)", "E383481b2")
    # Ec90f8f52 FtpTileService.onFtpReceiverActions -> FtpTileService
    # .updateTileState: TARGET EDGE. onFtpReceiverActions calls
    # updateTileState() (FtpTileService.java:28). No user action;
    # see the header caveat about tile listening registration.
    r.comment("onFtpReceiverActions calls updateTileState "
              "(FtpTileService.java:28)", "Ec90f8f52")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
