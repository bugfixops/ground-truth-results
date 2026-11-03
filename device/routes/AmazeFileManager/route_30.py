#!/usr/bin/env python3
"""AmazeFileManager route_30: UtilsHandler.getSshAuthPrivateKeyColumn.

Method: UtilsHandler.getSshAuthPrivateKeyColumn
Edge ids in order:
    E393625fa E88f218aa E51ddec28 Eba2f1368 E9896632a E38acc839
    Ef2ac2d04
Printed route: edge list identical to the AmazeFileManager
ROUTES.csv route_30 row and to amazefilemanager_trigger_graph.json.
Permissions: none (ROUTES.csv permissions column empty; INTERNET
is a normal permission, and the SAF picker + drawer need no
storage grant).
Fixtures: gen:device_replay_key -> /sdcard/Download/device_replay_key
(the per-run client key staged by setup_route_30.py from
$OUTDIR/ssh_client_key; the file does not exist in any checkout
— it is generated per run by run_app.sh). Setup: setup_route_30.py
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
    server row, and creating one requires GetSshHostFingerprint
    Task to connect to a live SSH server — the throwaway sshd.
    The setup creates that saved row: FAB menu (res_id
    com.amaze.filemanager:id/fabs_menu) -> "Cloud Connection"
    (R.string.cloud_connection, MainActivity.java:1504) ->
    cloud sheet -> "SCP/SFTP Connection" row (res_id
    linear_layout_scp, fragment_sheet_cloud.xml; CloudSheet
    Fragment.java:110-117 opens SftpConnectDialog with
    edit=false) -> SFTP dialog (sftp_dialog.xml): the name
    field keeps its default "SCP/SFTP Connection"
    (R.string.scp_connection), address 10.0.2.2, port $SSH_PORT
    (portET selects all on focus, so typing replaces the
    default 22), username $SSH_USER (both from the environment
    exported by run_app.sh — never hardcoded), password empty
    (keypair auth) -> selectPemBTN -> system SAF picker (*/*)
    -> the pushed per-run client key -> PemToKeyPairTask parses
    it (OpenSSHKeyFile/OpenSSHKeyV1KeyFile converters accept the
    ssh-keygen ed25519 OpenSSH format, no passphrase) -> OK
    enabled -> tap "Create" (positiveText create in new mode)
    -> host fingerprint dialog -> tap "Yes" ->
    authenticateAndSaveSetup saves the row (drawer refreshes
    with a SERVERS_GROUP row labelled "SCP/SFTP Connection").
  - PICKER ASSUMPTIONS (live-run uncertainties, fail loudly):
    the DocumentsUI picker opens at its last-used location; the
    script first waits for the key filename, and if that times
    out opens the roots drawer (desc "Show roots") -> "Download"
    -> the filename. If the picker layout differs, the wait
    fails loudly (unclear, never wrong).
  - DRAWER ACTION VIEW: tapping a saved server row's BODY
    navigates to the folder; the EDIT dialog (this chain's
    showSftpDialog(title, path, edit=true)) opens only from the
    row's trailing action view (Drawer.java:474/494: the action
    view's onClickListener calls onNavigationItemActionClick,
    which for path ssh:/ calls showSftpDialog(title, path,
    true)). Every drawer row's action view shares res_id
    com.amaze.filemanager:id/imageButton, so plain tap(res_id)
    would pick the first row's icon (internal storage). The
    script uses tap_row_action(row_text="SCP/SFTP Connection",
    res_id=imageButton), which taps that row's icon only.
  - TARGET: showSftpDialog (edit mode, pre-filled) calls
    getSshAuthPrivateKeyName -> getSshAuthPrivateKeyColumn
    (reading the saved key column from the database) on dialog
    open — no further tap is needed after the row action tap.
  - This route was unscriptable ("creating [a saved row]
    requires GetSshHostFingerprintTask to connect to a live SSH
    server") until run_app.sh gained the throwaway sshd plus
    the harness gained tap_row_action and system-UI driving;
    it converts on those.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('E393625fa E88f218aa E51ddec28 Eba2f1368 E9896632a '
            'E38acc839 Ef2ac2d04').split()

CONNECTION_NAME = 'SCP/SFTP Connection'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_30', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    ssh_port = os.environ.get('SSH_PORT', '2222')
    ssh_user = os.environ.get('SSH_USER', 'runner')
    # E393625fa (precondition): create + save the SSH connection
    # through the SFTP dialog. The per-run client key was staged
    # into the gen dir by setup_route_30.py and pushed to
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
    # E38acc839 showSftpDialog -> getSshAuthPrivateKeyName:
    # direct call, no action.
    r.comment('getSshAuthPrivateKeyName()', 'E38acc839')
    # Ef2ac2d04 getSshAuthPrivateKeyName ->
    # getSshAuthPrivateKeyColumn: direct call. Target.
    r.comment('getSshAuthPrivateKeyColumn()', 'Ef2ac2d04')
    r.done()


if __name__ == '__main__':
    main()
