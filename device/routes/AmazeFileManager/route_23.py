#!/usr/bin/env python3
"""AmazeFileManager route_23: PemToKeyPairTask.toastOnParseError.

Method: PemToKeyPairTask.toastOnParseError
Edge ids in order:
    E393625fa E88f218aa E51ddec28 Eba2f1368 E9896632a E973b24af
    E747b933b Ed024bdda E83d7c4eb Ece114399 E99fa54db E8cb8ea76
    E9b91a366
Printed route: edge list identical to the AmazeFileManager
ROUTES.csv route_23 row (as changed by the accompanying row
note) and to amazefilemanager_trigger_graph.json. The first
five edges are the same drawer chain as route_30; the route
diverges after showSftpDialog into the SftpConnectDialog
lifecycle and the bad-key picker path instead of route_30's
getSshAuthPrivateKeyColumn tail.
Permissions: none (ROUTES.csv permissions column empty;
INTERNET is a normal permission, and the SAF picker + drawer
need no storage grant).
Fixtures: gen:device_replay_key -> /sdcard/Download/device_replay_key
(the per-run client key staged by setup_route_23.py from
$OUTDIR/ssh_client_key; the file does not exist in any checkout
— it is generated per run by run_app.sh) AND
device/routes/AmazeFileManager/amaze_bad_key.txt ->
/sdcard/Download/amaze_bad_key.txt (repo text fixture, plain
non-PEM text that no converter can parse; see below).
Setup: setup_route_23.py copies the per-run client key into
the gen dir; run_app.sh pushes both fixtures to
/sdcard/Download before the script runs.
Standard configuration: run_app.sh starts from `pm clear` and
grants only the ROUTES.csv permissions. This route ALSO needs
run_app.sh invoked with WITH_SSH_SERVER=1 (the throwaway sshd
on the CI host; the emulator reaches it at 10.0.2.2:$SSH_PORT).
Without the server the run exits 2 before any route runs.

Mapping notes (printed source):
  - SETUP PRECONDITION (logged under E393625fa, before the
    chain's drawer tap): identical to route_30. The chain's
    drawer item is a SAVED SSH server row, and creating one
    requires GetSshHostFingerprintTask to connect to a live SSH
    server — the throwaway sshd. The setup creates that saved
    row: FAB menu (res_id
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
    script first waits for the bad-key filename, and if that
    times out opens the roots drawer (desc "Show roots") ->
    "Download" -> the filename. If the picker layout differs,
    the wait fails loudly (unclear, never wrong). This is the
    same fallback route_30 uses for the valid key.
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
  - EDIT DIALOG (edit=true, SftpConnectDialog.java:102-130):
    the dialog is pre-filled from the saved row (name, address,
    port, username; selectPemBTN shows the saved keypair name).
    Nothing in it needs editing for this route: the bad key is
    picked through selectPemBTN, exactly as in create mode.
  - BAD KEY (PemToKeyPairTask.java:81-118): doInBackground
    tries four converters in order (JcaPem, OpenSshPem,
    OpenSshV1Pem, PuttyPrivateKey), each returning null on
    failure. The fixture amaze_bad_key.txt is plain non-PEM
    text with no key header, so all four return null; with
    passwordFinder still null, the task sets paused=true and
    calls publishProgress(new IOException("No converter
    available to parse selected PEM")), which triggers
    onProgressUpdate on the main thread. onProgressUpdate
    (PemToKeyPairTask.java:121-160) shows a MaterialDialog
    titled R.string.ssh_key_prompt_passphrase ("Please enter
    key passphrase.") with a password field, positive OK and
    negative R.string.cancel.
  - CANCEL BUTTON TEXT (live-run uncertainty, handled by
    fallback): the negative button is R.string.cancel, whose
    strings.xml value is "CANCEL". Existing Amaze scripts tap
    title-case labels for all-caps resources (route_30 taps
    "Create" for R.string.create = "CREATE"), so the script
    first taps "Cancel" and, only if that raises LookupError,
    taps "CANCEL". In dry-run mode the first tap is planned
    and the fallback never runs.
  - CANCEL NODE AMBIGUITY (live-run uncertainty, not
    dry-run-verifiable): while the passphrase dialog is up,
    the underlying edit SFTP dialog also carries a negative
    Cancel button. The script waits for the passphrase title
    first, so the top dialog is present, but printed source
    alone does not establish which Cancel node uiautomator
    returns first in document order. Without the discriminator
    below, a wrong tap would have been a silent pass (target
    edge logged unconditionally); with the check it fails
    loudly: after the Cancel tap, in live-run mode only, the
    script waits again briefly for the passphrase title; if
    that wait succeeds the passphrase dialog is still present,
    so the tap hit the wrong Cancel and the script raises; if
    it raises TimeoutError the passphrase dialog is gone, so
    the correct Cancel was tapped. In dry-run mode the check
    is skipped entirely because dry-run wait_for never raises.
  - TARGET: the passphrase dialog's negative callback
    (PemToKeyPairTask.java:153-157) dismisses the dialog,
    calls toastOnParseError(result), then cancel(true).
    toastOnParseError (PemToKeyPairTask.java:189-194) shows
    the toast "Unable to read selected PEM: ..." — no further
    tap is needed after the Cancel tap.

NOTE ON FILE LOCATION: this draft is written for its final
location, device/phase2/routes/AmazeFileManager/route_23.py,
so its sys.path line matches route_30's. From the helper
directory it still runs in dry-run mode when PYTHONPATH
includes device/phase2 (see the verification note).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('E393625fa E88f218aa E51ddec28 Eba2f1368 E9896632a '
            'E973b24af E747b933b Ed024bdda E83d7c4eb Ece114399 '
            'E99fa54db E8cb8ea76 E9b91a366').split()

CONNECTION_NAME = 'SCP/SFTP Connection'
BAD_KEY_NAME = 'amaze_bad_key.txt'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_23', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    ssh_port = os.environ.get('SSH_PORT', '2222')
    ssh_user = os.environ.get('SSH_USER', 'runner')
    # E393625fa (precondition): create + save the SSH connection
    # through the SFTP dialog, exactly as route_30 does. The
    # per-run client key was staged into the gen dir by
    # setup_route_23.py and pushed to
    # /sdcard/Download/device_replay_key by run_app.sh's fixture
    # phase before this script runs (see the ROUTES fixtures cell).
    # E393625fa S_ENTRY -> MainActivity.onResume: launch.
    r.launch(a.package + '/.activities.MainActivity', 'E393625fa')
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
    # Trigger: "Refresh drawer on activity resume".
    r.comment('Drawer refreshes with the saved server row', 'E88f218aa')
    # E51ddec28 refreshDrawer -> lambda$addNewItem$5: the saved
    # row's action view is created, no action. Trigger:
    # "refreshDrawer creates menu items with lambdas via
    # addNewItem; lambda $5 is one of the menu item onClick
    # handlers".
    r.comment('Saved server row created with its action view', 'E51ddec28')
    # Eba2f1368 lambda$addNewItem$5 -> onNavigationItemActionClick:
    # open the drawer, then tap THIS row's action view (not the
    # first row's icon — see header). Trigger: "Direct call"
    # (Drawer.java:494 bytecode: action view onClickListener).
    r.tap('Eba2f1368', desc='Open navigation drawer')
    r.tap_row_action('Eba2f1368', CONNECTION_NAME,
                     'com.amaze.filemanager:id/imageButton')
    # E9896632a onNavigationItemActionClick -> showSftpDialog:
    # path ssh:/ opens the edit dialog, no action. Trigger:
    # "Direct call" (Drawer.java:626 bytecode:
    # showSftpDialog(title, path, true)).
    r.comment('Edit dialog opens for the saved SSH connection', 'E9896632a')
    # E973b24af MainActivity.showSftpDialog ->
    # SftpConnectDialog.<init>: the dialog object is created,
    # no action. Trigger: "Creates SFTP dialog".
    r.comment('SftpConnectDialog created', 'E973b24af')
    # E747b933b SftpConnectDialog.<init> -> onCreate: framework
    # lifecycle, no action. Trigger: "Framework calls
    # DialogFragment.onCreate".
    r.comment('Framework calls DialogFragment.onCreate', 'E747b933b')
    # Ed024bdda SftpConnectDialog.onCreate -> onCreateDialog:
    # framework lifecycle, no action; after it the pre-filled
    # edit dialog is visible. Trigger: "Framework calls
    # DialogFragment.onCreateDialog to create the dialog".
    r.comment('Edit dialog visible, pre-filled from the saved row',
              'Ed024bdda')
    # E83d7c4eb SftpConnectDialog.onCreateDialog ->
    # onActivityResult: tap selectPemBTN (SftpConnectDialog
    # .java:141-146: ACTION_GET_CONTENT, type */*), then pick
    # the BAD key in the system SAF picker. Trigger: "Framework
    # delivers activity result when user picks SSH key file".
    r.tap('E83d7c4eb', res_id='com.amaze.filemanager:id/selectPemBTN')
    try:
        r.wait_for('E83d7c4eb', text=BAD_KEY_NAME, timeout=10)
        r.tap('E83d7c4eb', text=BAD_KEY_NAME)
    except TimeoutError:
        r.tap('E83d7c4eb', desc='Show roots')
        r.tap('E83d7c4eb', text='Download')
        r.tap('E83d7c4eb', text=BAD_KEY_NAME)
    # Ece114399 SftpConnectDialog.onActivityResult ->
    # PemToKeyPairTask.doInBackground: onActivityResult executes
    # the task (SftpConnectDialog.java:322), no UI action.
    # Trigger: "onActivityResult executes PemToKeyPairTask".
    r.comment('onActivityResult executes PemToKeyPairTask', 'Ece114399')
    # E99fa54db PemToKeyPairTask.doInBackground ->
    # onProgressUpdate: all four converters fail on the plain
    # text fixture, so doInBackground publishes the "No
    # converter available to parse selected PEM" IOException.
    # Trigger: "doInBackground calls publishProgress which
    # triggers onProgressUpdate on main thread". Wait for the
    # passphrase dialog this produces before tapping Cancel.
    r.wait_for('E99fa54db', text='Please enter key passphrase.',
               timeout=30)
    # E8cb8ea76 PemToKeyPairTask.onProgressUpdate ->
    # lambda$onProgressUpdate$1: tap Cancel in the passphrase
    # dialog. Trigger: "User taps Cancel button in passphrase
    # dialog". See the header note on Cancel vs CANCEL.
    try:
        r.tap('E8cb8ea76', text='Cancel')
    except LookupError:
        r.tap('E8cb8ea76', text='CANCEL')
    # Live-run-only discriminator for the two-Cancel ambiguity
    # (see header): if the passphrase dialog is still present
    # after the Cancel tap, the tap hit the wrong Cancel and
    # the run must fail loudly instead of logging the target
    # edge unconditionally. Skipped in dry-run mode, where
    # wait_for never raises and would break the dry run.
    # Logged under E8cb8ea76 only; edge order unchanged.
    if not r.dry_run:
        try:
            r.wait_for('E8cb8ea76',
                       text='Please enter key passphrase.', timeout=5)
        except TimeoutError:
            pass
        else:
            raise RuntimeError(
                'passphrase dialog still present after Cancel tap: '
                'wrong Cancel tapped')
    # E9b91a366 lambda$onProgressUpdate$1 -> toastOnParseError:
    # the Cancel callback calls toastOnParseError(result) then
    # cancel(true). No further tap. Trigger: "Cancel callback
    # shows toast error before canceling task". Target.
    r.comment('toastOnParseError(result) — target', 'E9b91a366')
    r.done()


if __name__ == '__main__':
    main()
