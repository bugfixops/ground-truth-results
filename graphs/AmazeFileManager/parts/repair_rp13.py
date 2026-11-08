# Repair batch 13 - AmazeFileManager trigger graph repair edges
# Generated for methods in scratch/repair_batches/rp_13.txt
# Schema-2 format matching existing graph_def.py structure

# ========== PermissionsActivity methods ==========

# PermissionsActivity.isGranted - private helper called only by onRequestPermissionsResult
UNREACHABLE['PermissionsActivity.isGranted'] = ('no_trigger_in_app', 'Private helper method called only internally by PermissionsActivity.onRequestPermissionsResult at line 30', 'SRC activities/superclasses/PermissionsActivity.java:97-99', 'SOURCE')

# PermissionsActivity.lambda$requestInstallApkPermission$1 - synthetic lambda
# Created by lambda at requestInstallApkPermission line 65
e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.lambda$requestInstallApkPermission$1', 'GUI', 'MaterialDialog negative button callback for APK install permission', 
  'SRC activities/superclasses/PermissionsActivity.java:65 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> materialDialog.dismiss())')

# PermissionsActivity.lambda$requestPermission$2 - synthetic lambda
# Created by lambda at requestPermission line 86
e('PermissionsActivity.requestPermission', 'PermissionsActivity.lambda$requestPermission$2', 'GUI', 'MaterialDialog positive button callback for permission request',
  'SRC activities/superclasses/PermissionsActivity.java:86-89 rationale.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ActivityCompat.requestPermissions(...); rationale.dismiss(); })')

# PermissionsActivity.lambda$requestStoragePermission$0 - synthetic lambda
# Created by lambda at requestStoragePermission line 56
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.lambda$requestStoragePermission$0', 'GUI', 'MaterialDialog negative button callback for storage permission',
  'SRC activities/superclasses/PermissionsActivity.java:56 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> finish())')

# PermissionsActivity.onRequestPermissionsResult - framework lifecycle callback
# Called by framework when permission request completes
e('MainActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives; MainActivity extends PermissionsActivity',
  'INFERRED Android framework delivers permission results to Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:26-45 shows implementation')

e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when storage permission result arrives after ActivityCompat.requestPermissions',
  'INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:60 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when install APK permission result arrives after ActivityCompat.requestPermissions',
  'INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:69 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives after ActivityCompat.requestPermissions',
  'INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:90 or 87 calls ActivityCompat.requestPermissions')

# ========== GetSshHostFingerprintTask methods ==========

# GetSshHostFingerprintTask.<init> - constructor called from SftpConnectDialog
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to verify SSH host fingerprint when saving connection',
  'SRC ui/dialogs/SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to get SSH host fingerprint for new connection',
  'SRC ui/dialogs/SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

# GetSshHostFingerprintTask.doInBackground - AsyncTask worker thread method
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  'INFERRED AsyncTask.execute schedules doInBackground; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:62 extends AsyncTask')

# GetSshHostFingerprintTask.lambda$doInBackground$0 - synthetic lambda for host key verifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'Lambda host key verifier callback invoked when SSH client connects',
  'SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:85-89 sshClient.addHostKeyVerifier((hostname, port, key) -> { holder.set(...); latch.countDown(); return true; })')

# GetSshHostFingerprintTask.onPostExecute - AsyncTask main thread callback
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  'INFERRED AsyncTask lifecycle delivers result to onPostExecute; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:108-122 shows implementation')

# GetSshHostFingerprintTask.onPreExecute - AsyncTask main thread pre-execution
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC', 'AsyncTask.execute calls onPreExecute on main thread before doInBackground',
  'INFERRED AsyncTask.execute calls onPreExecute before worker thread runs; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:104-106 shows implementation')

# ========== FileUtil methods ==========

# FileUtil.<init> - abstract class, no public constructor
UNREACHABLE['FileUtil.<init>'] = ('no_trigger_in_app', 'Abstract class with only static utility methods; no instances created', 'SRC filesystem/FileUtil.java:78 public abstract class FileUtil', 'SOURCE')

# FileUtil.copyDummyFile - private helper called only by copyDummyFiles
UNREACHABLE['FileUtil.copyDummyFile'] = ('no_trigger_in_app', 'Private static method called only internally by FileUtil.copyDummyFiles at line 973-974', 'SRC filesystem/FileUtil.java:888-927 private static File copyDummyFile(...)', 'SOURCE')

# FileUtil.copyDummyFiles - private helper called only by MediaFile methods (API<29 only)
UNREACHABLE['FileUtil.copyDummyFiles'] = ('closed_by_api_level', 'Private helper for MediaFile workaround on API<29; standard config is API 27 but usage is guarded and SAF is preferred', 'SRC filesystem/FileUtil.java:971-976 private static File copyDummyFiles(Context c)', 'SOURCE')

# FileUtil.getTempFile - public method but not called by app code
UNREACHABLE['FileUtil.getTempFile'] = ('no_trigger_in_app', 'Public method but no app code calls it; grep -rn getTempFile over app/src/main shows only the definition', 'SRC filesystem/FileUtil.java:476-479', 'SOURCE')

# FileUtil.mkfile - public method called from Operations
# Already has edge at graph_def.py:3692: e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',

# ========== Coders$DeflateDecoder$DeflateDecoderOutputStream methods ==========
# These are library classes in commons_compress_7z module, called internally by Coders.addEncoder

# Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>
e('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>', 'CALL', 'Create deflate output stream wrapper when encoding 7z archive with DEFLATE compression',
  'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:155 return new DeflateDecoderOutputStream(deflaterOutputStream, deflater)')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.close - OutputStream method
# Called by framework/library code that uses OutputStreams
e('SevenZOutputFile.finish', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.close', 'CALL', 'Close output stream when finishing 7z archive compression',
  'INFERRED SevenZOutputFile.finish closes the encoder output streams; SRC Coders.java:217-225 shows close implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)', 'CALL', 'Write single byte when compressing 7z archive with DEFLATE',
  'INFERRED OutputStream.write(int) called by compression pipeline; SRC Coders.java:204-206 shows implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])', 'CALL', 'Write byte array when compressing 7z archive with DEFLATE',
  'INFERRED OutputStream.write(byte[]) called by compression pipeline; SRC Coders.java:209-211 shows implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)', 'CALL', 'Write byte range when compressing 7z archive with DEFLATE',
  'INFERRED OutputStream.write(byte[],int,int) called by compression pipeline; SRC Coders.java:214-216 shows implementation')

# ========== SshClientUtils methods ==========

# SshClientUtils.<init> - abstract class constructor
UNREACHABLE['SshClientUtils.<init>'] = ('no_trigger_in_app', 'Abstract utility class with only static methods; no instances created', 'SRC filesystem/ssh/SshClientUtils.java:51 public abstract class SshClientUtils', 'SOURCE')

# SshClientUtils.deriveSftpPathFrom - static utility method
e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL from connection parameters',
  'SRC ui/dialogs/SftpConnectDialog.java:171 utilsHandler.getSshHostKey(deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair))')

e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL to remove old connection from pool',
  'SRC ui/dialogs/SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair), ...)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP URL path for saving connection',
  'SRC ui/dialogs/SftpConnectDialog.java:242 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP path for connection test',
  'SRC ui/dialogs/SftpConnectDialog.java:336 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SshConnectionPool.getConnection', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build normalized connection URL',
  'SRC filesystem/ssh/SshConnectionPool.java:150 String url = SshClientUtils.deriveSftpPathFrom(host, port, username, password, keyPair)')

# SshClientUtils.lambda$launchSftp$1 - synthetic lambda for thread
e('SshClientUtils.launchSftp', 'SshClientUtils.lambda$launchSftp$1', 'ASYNC', 'Lambda runnable executed on new thread to stream SFTP file',
  'SRC filesystem/ssh/SshClientUtils.java:240 new Thread(() -> { ... }).start()')

# SshClientUtils.lambda$null$0 - nested lambda within launchSftp thread
e('SshClientUtils.lambda$launchSftp$1', 'SshClientUtils.lambda$null$0', 'CALL', 'Lambda runnable to launch file viewer on UI thread',
  'SRC filesystem/ssh/SshClientUtils.java:243 activity.runOnUiThread(() -> { ... })')

# SshClientUtils.launchSftp - public method called from MainFragment
e('MainFragment.onListItemClick', 'SshClientUtils.launchSftp', 'CALL', 'Launch SFTP file in external app when user clicks file in SFTP directory',
  'SRC fragments/MainFragment.java:919 SshClientUtils.launchSftp(e.generateBaseFile(), getMainActivity())')

# ========== ColorCircleDrawable methods ==========
# Already have edges in graph_def.py lines 1507-1527, but let me check if constructors are there

# ColorCircleDrawable.<init> not in UNREACHABLE, checking for existing edge
# Line 1507 shows: e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>', ...
# So constructor already has route

# The Drawable callback methods already have edges as pseudo-node 'Drawable' -> method
# These are framework callbacks, already handled

# ========== RenameBookmark methods ==========

# RenameBookmark.lambda$onCreateDialog$0 - synthetic lambda for neutral button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$0', 'GUI', 'MaterialDialog neutral button callback to cancel rename',
  'SRC ui/dialogs/RenameBookmark.java:81 builder.onNeutral((dialog, which) -> dialog.dismiss())')

# RenameBookmark.lambda$onCreateDialog$1 - synthetic lambda for positive button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$1', 'GUI', 'MaterialDialog positive button callback to save renamed bookmark',
  'SRC ui/dialogs/RenameBookmark.java:85 materialDialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.lambda$onCreateDialog$2 - synthetic lambda for negative button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$2', 'GUI', 'MaterialDialog negative button callback to delete bookmark',
  'SRC ui/dialogs/RenameBookmark.java:120 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.onCreate - DialogFragment lifecycle
e('RenameBookmark.<init>', 'RenameBookmark.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  'INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/RenameBookmark.java:44-46 shows implementation')

# RenameBookmark.onCreateDialog - DialogFragment lifecycle
e('RenameBookmark.onCreate', 'RenameBookmark.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  'INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/RenameBookmark.java:49-128 shows implementation')

# RenameBookmark.<init> - constructor via getInstance factory
e('MainActivity.renameBookmark', 'RenameBookmark.<init>', 'CALL', 'Create RenameBookmark dialog fragment',
  'SRC activities/MainActivity.java:1552 RenameBookmark renameBookmark = RenameBookmark.getInstance(title, path, getAccent()); SRC ui/dialogs/RenameBookmark.java:35-41 getInstance creates instance')

# ========== SmbSearchDialog methods ==========

# SmbSearchDialog.dismiss - DialogFragment dismiss override
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.dismiss', 'GUI', 'User taps cancel button in SMB search dialog',
  'SRC ui/dialogs/SmbSearchDialog.java:67 builder.onNegative((dialog, which) -> { subnetScanner.interrupt(); dismiss(); })')

e('SmbSearchDialog.lambda$onCreateDialog$1', 'SmbSearchDialog.dismiss', 'CALL', 'Dismiss dialog after user selects found device',
  'SRC ui/dialogs/SmbSearchDialog.java:156 dismiss()')

# SmbSearchDialog.lambda$onCreateDialog$0 - synthetic lambda for SubnetScanner observer computerFound
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$0', 'ASYNC', 'SubnetScanner callback when computer found on network',
  'SRC ui/dialogs/SmbSearchDialog.java:77 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void computerFound(...) {...} })')

# SmbSearchDialog.lambda$onCreateDialog$1 - synthetic lambda for SubnetScanner observer searchFinished
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$1', 'ASYNC', 'SubnetScanner callback when network scan completes',
  'SRC ui/dialogs/SmbSearchDialog.java:86 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void searchFinished() {...} })')

# SmbSearchDialog.onCreate - DialogFragment lifecycle
e('SmbSearchDialog.<init>', 'SmbSearchDialog.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  'INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/SmbSearchDialog.java:40-45 shows implementation')

# SmbSearchDialog.onCreateDialog - DialogFragment lifecycle
e('SmbSearchDialog.onCreate', 'SmbSearchDialog.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  'INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/SmbSearchDialog.java:53-99 shows implementation')

# SmbSearchDialog.<init> - constructor via new
e('CloudSheetFragment.onClick', 'SmbSearchDialog.<init>', 'CALL', 'Create SMB search dialog when user taps SMB connection button',
  'SRC fragments/CloudSheetFragment.java:108 SmbSearchDialog smbDialog=new SmbSearchDialog(); line 109 smbDialog.show(...)')
