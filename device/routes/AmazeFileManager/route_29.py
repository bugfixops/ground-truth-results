#!/usr/bin/env python3
"""AmazeFileManager route_29: HybridFile$11.<init>.

Method: HybridFile$11.<init>
Edge ids in order:
    E13267468 E84fa3666 E766a13d0 Ece10abda Ec1142890 E70854c04
    E5887a330
Printed route: edge list identical to the AmazeFileManager
ROUTES.csv route_29 row and to amazefilemanager_trigger_graph.json.
Permissions: WRITE_EXTERNAL_STORAGE only (the copy flow reads
the Download file list; the app declares WRITE, not READ).
Fixtures: device/routes/AmazeFileManager/amaze_search.txt ->
/sdcard/Download/amaze_search.txt (repo text fixture, pushed by
run_app.sh) and gen:device_replay_key ->
/sdcard/Download/device_replay_key (per-run client key staged by
setup_route_29.py from $OUTDIR/ssh_client_key). Setup:
setup_route_29.py copies the per-run SSH client key into the gen
dir; run_app.sh pushes it before the script runs.
Standard configuration: run_app.sh starts from `pm clear` and
grants only the ROUTES.csv permissions. This route ALSO needs
run_app.sh invoked with WITH_SSH_SERVER=1 (the throwaway sshd
on the CI host; the emulator reaches it at 10.0.2.2:$SSH_PORT).
Without the server the run exits 2 before any route runs.

Mapping notes (printed source):
  - SETUP PRECONDITION (logged under E13267468): the encrypt
    target must be an SFTP file, so the script first creates +
    saves the SSH connection (same dialog as route_30: FAB
    menu -> "Cloud Connection" -> cloud sheet -> "SCP/SFTP
    Connection" row -> SftpConnectDialog create mode, address
    10.0.2.2, port $SSH_PORT, username $SSH_USER, keypair auth
    via device_replay_key, "Create", fingerprint "Yes"), then
    copies amaze_search.txt INTO the SFTP folder (Download nav
    -> long-press row -> Copy -> drawer row BODY tap navigates
    to the SFTP folder -> "Paste"; same as route_07), so the
    SFTP folder contains exactly the file to encrypt.
  - ENCRYPT: the per-row popup (ItemPopupMenu, inflated from
    item_extras) opens from the row's overflow button
    (ItemViewHolder.about = res_id properties). Every row
    shares that res_id, so the script uses tap_row_action
    (row_text='amaze_search.txt', res_id=properties) — the
    SFTP root may also list the CI home's files, and the wrong
    row's popup would encrypt the wrong file. The popup shows
    "Encrypt" for a non-.aze file (RecyclerAdapter.java:976-978;
    title @string/crypt_encrypt = "Encrypt"). Encrypt case
    (ItemPopupMenu.java:132) builds an EncryptService intent
    with the row's mode (SFTP) and source file, then the
    warning dialog (positive "Got it!", R.string.warning_
    confirm) and the authenticate dialog (password + confirm +
    save-as pre-filled "<name>.aze", positive "OK") start
    encryption. The passphrase typed here is a throwaway test
    value for the test file, not a credential.
  - CHAIN: EncryptService.<init> -> onCreate -> onStartCommand
    -> CryptUtil.<init> (constructor starts encryption) ->
    encrypt -> HybridFile.getOutputStream (the target is the
    save-as file in the SFTP folder) -> $11.<init> (the SFTP
    branch creates an anonymous SshClientTemplate). Target.
  - PICKER ASSUMPTIONS: as in route_30 (DocumentsUI last-used
    location; "Show roots" -> "Download" fallback; fail loudly).
  - This route was unscriptable ("reaching it needs an SSH
    target file, i.e. a live SSH server") until run_app.sh
    gained the throwaway sshd plus the harness gained
    tap_row_action and system-UI driving; it converts on those.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('E13267468 E84fa3666 E766a13d0 Ece10abda Ec1142890 '
            'E70854c04 E5887a330').split()

MAIN = 'com.amaze.filemanager/com.amaze.filemanager.activities.MainActivity'
SOURCE_DIR = '/sdcard/Download'
FILE_ROW = 'amaze_search.txt'
CONNECTION_NAME = 'SCP/SFTP Connection'
TEST_PASSWORD = 'test-password'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_29', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    ssh_port = os.environ.get('SSH_PORT', '2222')
    ssh_user = os.environ.get('SSH_USER', 'runner')
    # E13267468 (precondition 1): create + save the SSH
    # connection through the SFTP dialog (mirrors route_30).
    r.launch(a.package + '/com.amaze.filemanager.activities.MainActivity', 'E13267468')
    r.tap('E13267468', res_id='com.amaze.filemanager:id/fabs_menu')
    r.tap('E13267468', text='Cloud Connection')
    r.tap('E13267468',
          res_id='com.amaze.filemanager:id/linear_layout_scp')
    r.tap('E13267468', res_id='com.amaze.filemanager:id/ipET')
    r.type_text('10.0.2.2', 'E13267468')
    r.tap('E13267468', res_id='com.amaze.filemanager:id/portET')
    r.type_text(ssh_port, 'E13267468')
    r.tap('E13267468', res_id='com.amaze.filemanager:id/usernameET')
    r.type_text(ssh_user, 'E13267468')
    r.tap('E13267468', res_id='com.amaze.filemanager:id/selectPemBTN')
    try:
        r.wait_for('E13267468', text='device_replay_key', timeout=10)
        r.tap('E13267468', text='device_replay_key')
    except TimeoutError:
        r.tap('E13267468', desc='Show roots')
        r.tap('E13267468', text='Download')
        r.tap('E13267468', text='device_replay_key')
    r.tap('E13267468', text='Create')
    r.wait_for('E13267468', text='Yes', timeout=30)
    r.tap('E13267468', text='Yes')
    # E13267468 (precondition 2): copy the file into the SFTP
    # folder (same as route_07's copy flow).
    r.start_intent('E13267468', extras={'path': SOURCE_DIR},
                   component=MAIN)
    r.wait_for('E13267468', text=FILE_ROW, timeout=30)
    r.long_tap('E13267468', text=FILE_ROW)
    r.wait_for('E13267468', desc='Copy', timeout=30)
    r.tap('E13267468', desc='Copy')
    r.tap('E13267468', desc='Open navigation drawer')
    r.tap('E13267468', text=CONNECTION_NAME)
    r.wait_for('E13267468', text='Paste', timeout=30)
    r.tap('E13267468', text='Paste')
    # The SFTP folder now lists the copied file.
    r.wait_for('E13267468', text=FILE_ROW, timeout=60)
    # E13267468 (encrypt trigger): the copied file's row popup
    # -> Encrypt -> warning "Got it!" -> authenticate dialog
    # (password twice; save-as keeps its pre-filled .aze name)
    # -> OK starts EncryptService.
    r.tap_row_action('E13267468', FILE_ROW,
                     'com.amaze.filemanager:id/properties')
    r.wait_for('E13267468', text='Encrypt', timeout=30)
    r.tap('E13267468', text='Encrypt')
    r.wait_for('E13267468', text='Got it!', timeout=30)
    r.tap('E13267468', text='Got it!')
    r.tap('E13267468',
          res_id='com.amaze.filemanager:id/edit_text_dialog_encrypt_password')
    r.type_text(TEST_PASSWORD, 'E13267468')
    r.tap('E13267468',
          res_id='com.amaze.filemanager:id/edit_text_dialog_encrypt_password_confirm')
    r.type_text(TEST_PASSWORD, 'E13267468')
    r.tap('E13267468', text='OK')
    # E13267468 EncryptService.<init>: the OK tap starts the
    # service for the SFTP source file.
    r.comment('EncryptService started for the SFTP source', 'E13267468')
    # E84fa3666 EncryptService.<init> -> onCreate: lifecycle.
    r.comment('Service.onCreate', 'E84fa3666')
    # E766a13d0 onCreate -> onStartCommand: lifecycle.
    r.comment('Service.onStartCommand', 'E766a13d0')
    # Ece10abda onStartCommand -> CryptUtil.<init>: the
    # constructor starts the encryption process.
    r.comment('CryptUtil constructor starts encryption', 'Ece10abda')
    # Ec1142890 CryptUtil.<init> -> encrypt: encrypt() runs.
    r.comment('encrypt() runs', 'Ec1142890')
    # E70854c04 encrypt -> HybridFile.getOutputStream: encrypt
    # opens an output stream on the target (save-as) HybridFile.
    r.comment('getOutputStream on the SFTP target', 'E70854c04')
    # E5887a330 getOutputStream -> HybridFile$11.<init>:
    # the SFTP branch creates an anonymous SshClientTemplate.
    # Target.
    r.comment('SFTP branch creates SshClientTemplate', 'E5887a330')
    r.done()


if __name__ == '__main__':
    main()
