#!/usr/bin/env python3
"""AmazeFileManager route_08 (DRAFT): SshConnectionPool$AsyncRemoveConnection.onPostExecute.

Method: SshConnectionPool$AsyncRemoveConnection.onPostExecute
Edge ids in order:
    E393625fa E88f218aa E51ddec28 Eba2f1368 E9896632a E973b24af
    E747b933b Ed024bdda Edf9fdb80 Eaa386f86 Ef1b214fb Ef65bce02
    E6c12ada4
Printed route: edge list identical to the new route_08 row in
ROUTES_ROW_NOTE.md and to amazefilemanager_trigger_graph.json.
(The old ROUTES.csv route_08 row carries a different 12-edge
list and an unscriptable status; this draft does NOT edit
ROUTES.csv — see ROUTES_ROW_NOTE.md for the exact replacement
row.)
Permissions: none (permissions column empty, as for route_30;
INTERNET is a normal permission, and the SAF picker + drawer
need no storage grant).
Fixtures: gen:device_replay_key -> /sdcard/Download/device_replay_key
(the per-run client key staged by setup_route_08.py from
$OUTDIR/ssh_client_key; the file does not exist in any checkout
— it is generated per run by run_app.sh). Setup: setup_route_08.py
copies the per-run client key into the gen dir; run_app.sh pushes
it to /sdcard/Download/device_replay_key before the script runs.
Standard configuration: run_app.sh starts from `pm clear` and
grants only the ROUTES.csv permissions. This route ALSO needs
run_app.sh invoked with WITH_SSH_SERVER=1 (the throwaway sshd
on the CI host; the emulator reaches it at 10.0.2.2:$SSH_PORT).
Without the server the run exits 2 before any route runs.

Mapping notes (printed source):
  - SETUP PRECONDITION (logged under E393625fa, before the
    chain's drawer tap): the chain's drawer item is a SAVED SSH
    server row, and the removeConnection guard needs a saved SSH
    host key (Eaa386f86 guard !isEmpty(sshHostKey), needs_state
    "A saved SSH host key exists for the SFTP host"). The setup
    creates that saved row exactly as route_30 does: FAB menu
    (res_id com.amaze.filemanager:id/fabs_menu) -> "Cloud
    Connection" (R.string.cloud_connection,
    MainActivity.java:1504) -> cloud sheet -> "SCP/SFTP
    Connection" row (res_id linear_layout_scp,
    fragment_sheet_cloud.xml; CloudSheet Fragment.java:110-117
    opens SftpConnectDialog with edit=false) -> SFTP dialog
    (sftp_dialog.xml): the name field keeps its default
    "SCP/SFTP Connection" (R.string.scp_connection), address
    10.0.2.2, port $SSH_PORT (portET selects all on focus, so
    typing replaces the default 22), username $SSH_USER (both
    from the environment exported by run_app.sh — never
    hardcoded), password empty (keypair auth) -> selectPemBTN
    -> system SAF picker (*/*) -> the pushed per-run client key
    -> PemToKeyPairTask parses it (OpenSSHKeyFile/
    OpenSSHKeyV1KeyFile converters accept the ssh-keygen
    ed25519 OpenSSH format, no passphrase) -> OK enabled -> tap
    "Create" (positiveText create in new mode) -> host
    fingerprint dialog -> tap "Yes" ->
    authenticateAndSaveSetup saves the row (drawer refreshes
    with a SERVERS_GROUP row labelled "SCP/SFTP Connection").
  - PICKER ASSUMPTIONS (live-run uncertainties, fail loudly):
    as in route_30: the DocumentsUI picker opens at its
    last-used location; the script first waits for the key
    filename, and if that times out opens the roots drawer
    (desc "Show roots") -> "Download" -> the filename. If the
    picker layout differs, the wait fails loudly (unclear,
    never wrong).
  - DRAWER ACTION VIEW: tapping a saved server row's BODY
    navigates to the folder; the EDIT dialog (this chain's
    showSftpDialog(title, path, edit=true)) opens only from the
    row's trailing action view (Drawer.java:474/494: the action
    view's onClickListener calls onNavigationItemActionClick,
    which for path ssh:/ calls showSftpDialog(title, path,
    true) at Drawer.java:626). Every drawer row's action view
    shares res_id com.amaze.filemanager:id/imageButton, so plain
    tap(res_id) would pick the first row's icon (internal
    storage). The script uses tap_row_action(row_text=
    "SCP/SFTP Connection", res_id=imageButton), which taps that
    row's icon only.
  - EDIT DIALOG (pre-filled, no field edits): showSftpDialog
    (MainActivity.java:1637) fills the dialog from the saved
    row's path (name, address, port, username; hasPassword
    false, keypairName from the saved row), and the positive
    button reads "Update" in edit mode (SftpConnectDialog.
    java:156: positiveText(edit ? R.string.update :
    R.string.create); strings.xml renders R.string.update as
    "UPDATE" — this draft taps text "Update" following
    route_30's "Create" convention against R.string.create
    ("CREATE"); the live-run text match is a dry-run-blind
    point the lead should confirm, exactly as for route_30).
    The script changes no field: tapping Update with the
    pre-filled values drives the chain.
  - GUARD (why the precondition satisfies Eaa386f86): on
    positive, the lambda reads sshHostKey =
    utilsHandler.getSshHostKey(deriveSftpPathFrom(hostname,
    port, username, getArguments password, selectedParsedKey
    Pair)) (SftpConnectDialog.java:171-176). In edit mode the
    stored password argument is null (keypair auth), and
    deriveSftpPathFrom returns ssh://user@host:port whenever
    password is null (SshClientUtils.java:269-273) — the same
    path the create flow saved — so getSshHostKey returns the
    fingerprint saved by the precondition, the guard
    !isEmpty(sshHostKey) holds, and removeConnection is called.
  - REMOVE CHAIN: removeConnection creates
    AsyncRemoveConnection(url, callback) and executes it
    (SshConnectionPool.java:94-95); AsyncTask.execute runs
    doInBackground (disconnects/removes the pooled connection
    if present, SshConnectionPool.java:291-298), and the
    framework then calls onPostExecute (SshConnectionPool.
    java:301), which runs the callback. TARGET: onPostExecute.
  - POST-TARGET CLEANUP — GROUNDING GAP, READ BEFORE MERGE:
    the task order for this draft said to wait for the
    host-fingerprint "Yes" dialog that the onPostExecute
    callback triggers and tap it. Printed source does NOT
    support that dialog on this path. In the !isEmpty branch
    (SftpConnectDialog.java:175-200) the callback runs
    GetSshHostFingerprintTask and, when the fingerprint
    matches the saved host key (the expected case: same
    throwaway sshd for the whole run), calls
    authenticateAndSaveSetup DIRECTLY — no dialog appears.
    The "Yes" dialog (R.string.yes, SftpConnectDialog.
    java:217) exists only in the else branch, when NO host key
    is stored — a branch this chain cannot take, because its
    guard requires a stored key, and it bypasses
    removeConnection entirely. The only dialog the callback
    can show is the mismatch dialog with positive button
    R.string.update_host_key ("Update Host Key",
    strings.xml:648, SftpConnectDialog.java:190), which fires
    only if the server host key changed mid-run. The cleanup
    below is therefore implemented as a GUARDED attempt, not
    an unconditional wait: it waits up to 30 s for "Yes" and
    taps it if it appears, but a timeout is logged as the
    expected no-dialog outcome and does NOT fail the run.
    The cleanup is logged under the target edge id for
    attribution only and is NOT a route edge. If a live run
    ever shows "Update Host Key" instead, that is a
    host-key-change signal for the lead to adjudicate — this
    draft deliberately does not tap it.
  - This route was unscriptable ("the only verified caller is
    gated on stored state that a pm-clear run cannot have
    without a prior live SSH server") until run_app.sh gained
    the throwaway sshd plus the harness gained tap_row_action
    and system-UI driving; it converts on those, exactly as
    route_30 did.
  - DRAFT NOTE: this file lives in the helper directory. Its
    sys.path line assumes the merged location
    (phase2/routes/AmazeFileManager/), as in route_30; when
    merged there it runs unchanged. A dry run from the helper
    directory needs PYTHONPATH set to the phase2 directory.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('E393625fa E88f218aa E51ddec28 Eba2f1368 E9896632a '
            'E973b24af E747b933b Ed024bdda Edf9fdb80 Eaa386f86 '
            'Ef1b214fb Ef65bce02 E6c12ada4').split()

CONNECTION_NAME = 'SCP/SFTP Connection'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_08', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    ssh_port = os.environ.get('SSH_PORT', '2222')
    ssh_user = os.environ.get('SSH_USER', 'runner')
    # E393625fa (precondition): create + save the SSH connection
    # through the SFTP dialog. The per-run client key was staged
    # into the gen dir by setup_route_08.py and pushed to
    # /sdcard/Download/device_replay_key by run_app.sh's fixture
    # phase before this script runs (see the ROUTES fixtures cell).
    # E393625fa S_ENTRY -> MainActivity.onResume: launch.
    r.launch(a.package + '/com.amaze.filemanager.activities.MainActivity', 'E393625fa')
    # FAB menu -> Cloud Connection -> cloud sheet -> SCP/SFTP row.
    r.tap('E393625fa', res_id='com.amaze.filemanager:id/fabs_menu')
    r.tap('E393625fa', text='Cloud Connection')
    r.tap('E393625fa',
          res_id='com.amaze.filemanager:id/linear_layout_scp')
    # SFTP dialog (create mode): name keeps its default
    # "SCP/SFTP Connection"; address, port (select-all on focus),
    # username; password empty (keypair auth).
    r.tap('E393625fa', res_id='com.amaze.filemanager:id/ipET')
    r.type_text('10.0.2.2', 'E393625fa')
    r.tap('E393625fa', res_id='com.amaze.filemanager:id/portET')
    r.type_text(ssh_port, 'E393625fa')
    r.tap('E393625fa', res_id='com.amaze.filemanager:id/usernameET')
    r.type_text(ssh_user, 'E393625fa')
    # selectPemBTN -> SAF picker -> the pushed client key.
    r.tap('E393625fa', res_id='com.amaze.filemanager:id/selectPemBTN')
    try:
        r.wait_for('E393625fa', text='device_replay_key', timeout=10)
        r.tap('E393625fa', text='device_replay_key')
    except TimeoutError:
        r.tap('E393625fa', desc='Show roots')
        r.tap('E393625fa', text='Download')
        r.tap('E393625fa', text='device_replay_key')
    # PEM parses (OpenSSH ed25519, no passphrase) -> OK enabled.
    r.tap('E393625fa', text='Create')
    # Host fingerprint dialog -> Yes -> saved.
    r.wait_for('E393625fa', text='Yes', timeout=30)
    r.tap('E393625fa', text='Yes')
    # E88f218aa MainActivity.onResume -> Drawer.refreshDrawer:
    # the drawer refreshes with the saved server row, no action.
    r.comment('Drawer refreshes with the saved server row', 'E88f218aa')
    # E51ddec28 refreshDrawer -> lambda$addNewItem$5: the saved
    # row's action view is created, no action.
    r.comment('Saved server row created with its action view', 'E51ddec28')
    # Eba2f1368 lambda -> onNavigationItemActionClick: open the
    # drawer, then tap THIS row's action view (not the first
    # row's icon — see header).
    r.tap('Eba2f1368', desc='Open navigation drawer')
    r.tap_row_action('Eba2f1368', CONNECTION_NAME,
                     'com.amaze.filemanager:id/imageButton')
    # E9896632a onNavigationItemActionClick -> showSftpDialog:
    # path ssh:/ opens the edit dialog, no action.
    r.comment('Edit dialog opens for the saved SSH connection', 'E9896632a')
    # E973b24af showSftpDialog -> SftpConnectDialog.<init>:
    # dialog created, no action.
    r.comment('SftpConnectDialog created', 'E973b24af')
    # E747b933b SftpConnectDialog.<init> -> onCreate:
    # framework lifecycle, no action.
    r.comment('SftpConnectDialog.onCreate()', 'E747b933b')
    # Ed024bdda onCreate -> onCreateDialog: the edit dialog is
    # built pre-filled from the saved row, no action.
    r.comment('Edit SFTP dialog built pre-filled', 'Ed024bdda')
    # Edf9fdb80 onCreateDialog -> lambda$onCreateDialog$9:
    # tap the positive button ("Update" in edit mode). This tap
    # drives the lambda, which reads the saved host key and
    # calls removeConnection (next edge).
    r.tap('Edf9fdb80', text='Update')
    # Eaa386f86 lambda -> SshConnectionPool.removeConnection:
    # guard !isEmpty(sshHostKey) holds via the precondition;
    # direct call, no further UI action.
    r.comment('removeConnection() called with saved host key present',
              'Eaa386f86')
    # Ef1b214fb removeConnection -> AsyncRemoveConnection.<init>:
    # direct call, no action.
    r.comment('AsyncRemoveConnection created', 'Ef1b214fb')
    # Ef65bce02 <init> -> doInBackground: AsyncTask.execute runs
    # the worker, no action.
    r.comment('doInBackground() disconnects/removes pooled connection',
              'Ef65bce02')
    # E6c12ada4 doInBackground -> onPostExecute: framework call.
    # TARGET.
    r.comment('onPostExecute() runs the callback', 'E6c12ada4')
    # POST-TARGET CLEANUP (not a route edge — see header
    # grounding gap): the onPostExecute callback's fingerprint
    # match path saves directly with no dialog, so no "Yes"
    # dialog is expected. Attempt the wait + tap, but treat a
    # timeout as the expected outcome, never as a failure.
    r.comment('POST-TARGET CLEANUP (not a route edge): guarded '
              'Yes-dialog attempt', 'E6c12ada4')
    try:
        r.wait_for('E6c12ada4', text='Yes', timeout=30)
        r.tap('E6c12ada4', text='Yes')
    except TimeoutError:
        r.comment('POST-TARGET CLEANUP: no Yes dialog appeared, '
                  'as expected on the fingerprint-match path',
                  'E6c12ada4')
    r.done()


if __name__ == '__main__':
    main()
