#!/usr/bin/env python3
"""AmazeFileManager route_07: SshAuthenticationTask$1.getPublic.

Method: SshAuthenticationTask$1.getPublic
Edge ids in order:
    E6b899d64 E1a11c9d3 E2893b094 Ed4036ed5 Eb25bb213 Ea09956cb
    E8fc7f103 Eaf0babf6 E6202e994 E791408d8 Ea364138c E7f65d2ff
Printed route: edge list identical to the AmazeFileManager
ROUTES.csv route_07 row and to amazefilemanager_trigger_graph.json.
Permissions: WRITE_EXTERNAL_STORAGE only (the copy flow reads
the Download file list; the app declares WRITE, not READ).
Fixtures: device/routes/AmazeFileManager/amaze_search.txt ->
/sdcard/Download/amaze_search.txt (repo text fixture, pushed by
run_app.sh) and gen:device_replay_key ->
/sdcard/Download/device_replay_key (per-run client key staged by
setup_route_07.py from $OUTDIR/ssh_client_key). Setup:
setup_route_07.py copies the per-run SSH client key into the gen
dir; run_app.sh pushes it before the script runs.
Standard configuration: run_app.sh starts from `pm clear` and
grants only the ROUTES.csv permissions. This route ALSO needs
run_app.sh invoked with WITH_SSH_SERVER=1 (the throwaway sshd
on the CI host; the emulator reaches it at 10.0.2.2:$SSH_PORT).
Without the server the run exits 2 before any route runs.

Mapping notes (printed source):
  - SETUP PRECONDITION (logged under E6b899d64): the copy
    target must be an SSH location, so a saved SSH connection
    must exist first. The setup mirrors route_30's (same
    dialog, same key, same fingerprint): FAB menu
    (com.amaze.filemanager:id/fabs_menu) -> "Cloud Connection"
    -> cloud sheet -> "SCP/SFTP Connection" row
    (linear_layout_scp) -> SftpConnectDialog (create mode):
    name keeps its default "SCP/SFTP Connection", address
    10.0.2.2, port $SSH_PORT (select-all on focus), username
    $SSH_USER (both from run_app.sh's environment, never
    hardcoded), password empty (keypair auth) -> selectPemBTN
    -> SAF picker -> device_replay_key (OpenSSH ed25519 parses
    via PemToKeyPairTask's OpenSSH converters) -> "Create" ->
    fingerprint "Yes" -> saved SERVERS row.
  - COPY: navigate to Download via a path-extra intent (the
    route_28/09 pattern), long-press the amaze_search.txt row
    (action mode opens), tap the icon-only Copy button
    (content-desc "Copy", contextual.xml showAsAction="always"
    without withText) -> setPaste(pasteHelper) (MainFragment
    .java:719-729). The Paste menu item (activity_extra.xml,
    showAsAction="ifRoom|withText") is visible only while
    pasteHelper is non-null (MainActivity.java:758).
  - PASTE INTO SFTP: open the drawer (desc "Open navigation
    drawer") and tap the saved row BODY (text "SCP/SFTP
    Connection") — the row body navigates to the SFTP folder,
    while the row's action view would open the edit dialog
    (route_30's path). Then tap text "Paste": MainActivity
    .java:1025 takes path = getCurrentPath() (the SFTP folder)
    and starts PrepareCopyTask -> CopyService with the SFTP
    target.
  - CHAIN: CopyService.<init> -> HybridFile.mkdir (CopyService
    creates the target directory) -> SshClientUtils.execute
    (SFtpClientTemplate) -> execute (SshClientTemplate) ->
    SshConnectionPool.getConnection -> create -> create(6-arg)
    -> SshAuthenticationTask.<init> -> doInBackground ->
    $1.<init> (anonymous KeyProvider for key-based auth) ->
    getType -> getPublic (SSHJ calls getType, then getPublic
    for the key algorithm type). Target: getPublic.
  - NAVIGATION AUTH NOTE: opening the SFTP folder may itself
    authenticate (firing getPublic) before the paste; that does
    not change the verdict (JaCoCo hit = reached) and the script
    still completes the copy chain, so every chain step is
    exercised.
  - PICKER ASSUMPTIONS: as in route_30 (DocumentsUI last-used
    location; "Show roots" -> "Download" fallback; fail loudly).
  - This route was unscriptable ("reaching getPublic() requires
    an SSH handshake with a live SSH server") until run_app.sh
    gained the throwaway sshd plus the harness gained
    system-UI driving; it converts on those.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..'))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = ('E6b899d64 E1a11c9d3 E2893b094 Ed4036ed5 Eb25bb213 Ea09956cb '
            'E8fc7f103 Eaf0babf6 E6202e994 E791408d8 Ea364138c '
            'E7f65d2ff').split()

MAIN = 'com.amaze.filemanager/com.amaze.filemanager.activities.MainActivity'
SOURCE_DIR = '/sdcard/Download'
FILE_ROW = 'amaze_search.txt'
CONNECTION_NAME = 'SCP/SFTP Connection'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True)
    ap.add_argument('--log', required=True)
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--adb', default='adb')
    a = ap.parse_args()
    r = Runner(a.package, 'route_07', EDGE_IDS, a.log,
               dry_run=a.dry_run, adb=a.adb, outdir=a.outdir)
    ssh_port = os.environ.get('SSH_PORT', '2222')
    ssh_user = os.environ.get('SSH_USER', 'runner')
    # E6b899d64 (precondition 1): create + save the SSH
    # connection through the SFTP dialog (mirrors route_30).
    r.launch(a.package + '/com.amaze.filemanager.activities.MainActivity', 'E6b899d64')
    r.tap('E6b899d64', res_id='com.amaze.filemanager:id/fabs_menu')
    r.tap('E6b899d64', text='Cloud Connection')
    r.tap('E6b899d64',
          res_id='com.amaze.filemanager:id/linear_layout_scp')
    r.tap('E6b899d64', res_id='com.amaze.filemanager:id/ipET')
    r.type_text('10.0.2.2', 'E6b899d64')
    r.tap('E6b899d64', res_id='com.amaze.filemanager:id/portET')
    r.type_text(ssh_port, 'E6b899d64')
    r.tap('E6b899d64', res_id='com.amaze.filemanager:id/usernameET')
    r.type_text(ssh_user, 'E6b899d64')
    r.tap('E6b899d64', res_id='com.amaze.filemanager:id/selectPemBTN')
    try:
        r.wait_for('E6b899d64', text='device_replay_key', timeout=10)
        r.tap('E6b899d64', text='device_replay_key')
    except TimeoutError:
        r.tap('E6b899d64', desc='Show roots')
        r.tap('E6b899d64', text='Download')
        r.tap('E6b899d64', text='device_replay_key')
    r.tap('E6b899d64', text='Create')
    r.wait_for('E6b899d64', text='Yes', timeout=30)
    r.tap('E6b899d64', text='Yes')
    # E6b899d64 (precondition 2): copy a file (Download ->
    # action-mode Copy -> setPaste).
    r.start_intent('E6b899d64', extras={'path': SOURCE_DIR},
                   component=MAIN)
    r.wait_for('E6b899d64', text=FILE_ROW, timeout=30)
    r.long_tap('E6b899d64', text=FILE_ROW)
    r.wait_for('E6b899d64', desc='Copy', timeout=30)
    r.tap('E6b899d64', desc='Copy')
    # E6b899d64 (precondition 3): navigate to the SFTP folder
    # (row BODY tap navigates; the action view would edit),
    # then Paste with the SFTP folder as the target.
    r.tap('E6b899d64', desc='Open navigation drawer')
    r.tap('E6b899d64', text=CONNECTION_NAME)
    r.wait_for('E6b899d64', text='Paste', timeout=30)
    r.tap('E6b899d64', text='Paste')
    # E6b899d64 S_ENTRY -> CopyService.<init>: the paste starts
    # CopyService for the SFTP target.
    r.comment('CopyService started for the SFTP target', 'E6b899d64')
    # E1a11c9d3 CopyService.<init> -> HybridFile.mkdir:
    # CopyService creates the target directory.
    r.comment('CopyService creates the target directory', 'E1a11c9d3')
    # E2893b094 HybridFile.mkdir -> SshClientUtils.execute
    # (SFtpClientTemplate): direct call.
    r.comment('mkdir executes the SFTP client template', 'E2893b094')
    # Ed4036ed5 execute(SFtpClientTemplate) ->
    # execute(SshClientTemplate): direct call.
    r.comment('Template dispatch', 'Ed4036ed5')
    # Eb25bb213 execute(SshClientTemplate) ->
    # SshConnectionPool.getConnection(String): the template's url.
    r.comment('execute obtains a pooled/new SSHClient', 'Eb25bb213')
    # Ea09956cb getConnection -> create(String): no pooled
    # client (fresh run), so create(url).
    r.comment('No pooled client: create(url)', 'Ea09956cb')
    # E8fc7f103 create(String) -> create(String,int,String,
    # String,String,KeyPair): direct call.
    r.comment('create dispatches to the 6-arg form', 'E8fc7f103')
    # Eaf0babf6 create(6-arg) -> SshAuthenticationTask.<init>:
    # direct call.
    r.comment('SshAuthenticationTask created with the KeyPair',
              'Eaf0babf6')
    # E6202e994 SshAuthenticationTask.<init> -> doInBackground:
    # AsyncTask.execute runs doInBackground on a worker thread.
    r.comment('AsyncTask executes doInBackground', 'E6202e994')
    # E791408d8 doInBackground -> SshAuthenticationTask$1.<init>:
    # anonymous KeyProvider for key-based authentication.
    r.comment('KeyProvider created for key-based auth', 'E791408d8')
    # Ea364138c $1.<init> -> $1.getType: SSHJ calls getType to
    # determine the key algorithm type.
    r.comment('SSHJ calls getType', 'Ea364138c')
    # E7f65d2ff $1.getType -> $1.getPublic: getPublic obtains
    # the public key for type determination. Target.
    r.comment('getPublic obtains the public key', 'E7f65d2ff')
    r.done()


if __name__ == '__main__':
    main()
