# ---- Helper batch_034 label part (2026-10-27)

# GetSshHostFingerprintTask - AsyncTask for fetching SSH host fingerprints during SFTP setup

# Constructor called from SftpConnectDialog button callback
e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'Instantiate task to fetch host fingerprint when positive button clicked',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'Instantiate task to fetch host fingerprint in else branch (no existing key)',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

# execute() triggers AsyncTask lifecycle
e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC',
  'AsyncTask framework calls onPreExecute when execute() invoked',
  evidence='SRC SftpConnectDialog.java:199 }).execute(); triggers framework lifecycle')

e('GetSshHostFingerprintTask.onPreExecute', 'GetSshHostFingerprintTask.doInBackground', 'LIFECYCLE',
  'AsyncTask framework calls doInBackground after onPreExecute',
  evidence='SRC GetSshHostFingerprintTask.java:80 protected AsyncTaskResult<PublicKey> doInBackground(Void... voids)')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC',
  'AsyncTask framework calls onPreExecute when execute() invoked (second call site)',
  evidence='SRC SftpConnectDialog.java:229 }).execute(); triggers framework lifecycle')

# doInBackground creates lambda for HostKeyVerifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL',
  'Lambda passed to SSHClient.addHostKeyVerifier, invoked when host key received',
  evidence='SRC GetSshHostFingerprintTask.java:86 sshClient.addHostKeyVerifier((hostname, port, key) -> {...')

# AsyncTask completes and calls onPostExecute
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'LIFECYCLE',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC GetSshHostFingerprintTask.java:117 protected void onPostExecute(AsyncTaskResult<PublicKey> result)')

# No UNREACHABLE methods in this batch
