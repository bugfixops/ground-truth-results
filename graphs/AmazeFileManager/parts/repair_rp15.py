# Repair batch 15: 40 methods
# Generated at 21:07

# SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair)
e('SshConnectionPool.create(String,int,String,String,String,KeyPair)', 'SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair)', 'CALL',
  evidence='SRC SshConnectionPool.java:222-223 new SshAuthenticationTask(host, port, hostKey, username, password, keyPair).execute().get()')

# SshAuthenticationTask.doInBackground
e('AsyncTask.execute', 'SshAuthenticationTask.doInBackground', 'ASYNC',
  evidence='SRC SshAuthenticationTask.java:114 @Override protected AsyncTaskResult<SSHClient> doInBackground(Void... voids); FW-SRC android/os/AsyncTask.java AsyncTask.execute() triggers doInBackground()')

# SshAuthenticationTask.lambda$onPostExecute$0
e('SshAuthenticationTask.onPostExecute', 'SshAuthenticationTask.lambda$onPostExecute$0', 'GUI',
  evidence='SRC SshAuthenticationTask.java:172 .setPositiveButton(R.string.ok, (dialog, which) -> dialog.dismiss())')

# SshAuthenticationTask.onPostExecute
e('AsyncTask.execute', 'SshAuthenticationTask.onPostExecute', 'ASYNC',
  evidence='SRC SshAuthenticationTask.java:158 @Override protected void onPostExecute(AsyncTaskResult<SSHClient> result); FW-SRC android/os/AsyncTask.java AsyncTask framework calls onPostExecute() after doInBackground()')

# SshAuthenticationTask$1.<init>
e('SshAuthenticationTask.doInBackground', 'SshAuthenticationTask$1.<init>', 'CALL',
  evidence='SRC SshAuthenticationTask.java:129-142 sshClient.authPublickey(username, new KeyProvider() { ... }) creates anonymous KeyProvider implementation')

# SshAuthenticationTask$1.getPrivate
e('KeyProvider.interface', 'SshAuthenticationTask$1.getPrivate', 'FRAMEWORK',
  evidence='SRC SshAuthenticationTask.java:131-133 @Override public PrivateKey getPrivate() { return privateKey.getPrivate(); }; INFERRED sshj library calls getPrivate() during authPublickey()')

# SshAuthenticationTask$1.getPublic
e('KeyProvider.interface', 'SshAuthenticationTask$1.getPublic', 'FRAMEWORK',
  evidence='SRC SshAuthenticationTask.java:136-138 @Override public PublicKey getPublic() { return privateKey.getPublic(); }; INFERRED sshj library calls getPublic() during authPublickey()')

# SshAuthenticationTask$1.getType
e('KeyProvider.interface', 'SshAuthenticationTask$1.getType', 'FRAMEWORK',
  evidence='SRC SshAuthenticationTask.java:141-143 @Override public KeyType getType() { return KeyType.fromKey(getPublic()); }; INFERRED sshj library calls getType() during authPublickey()')

# AbstractProgressiveService.getDataPackage
e('ServiceWatcherUtil.handler', 'AbstractProgressiveService.getDataPackage', 'CALL',
  evidence='SRC AbstractProgressiveService.java:200-202 public final synchronized DatapointParcelable getDataPackage(int index); javadoc mentions called by ServiceWatcherUtil#handlerThread and MainActivity#runOnUiThread')

# AbstractProgressiveService.getDataPackageSize
e('ServiceWatcherUtil.handler', 'AbstractProgressiveService.getDataPackageSize', 'CALL',
  evidence='SRC AbstractProgressiveService.java:204-206 public final synchronized int getDataPackageSize(); javadoc mentions called by ServiceWatcherUtil#handlerThread and MainActivity#runOnUiThread')

# AbstractProgressiveService.isDecryptService
e('ServiceWatcherUtil', 'AbstractProgressiveService.isDecryptService', 'CALL',
  evidence='SRC AbstractProgressiveService.java:219-221 @Override public boolean isDecryptService() { return false; }; method from ServiceWatcherInteractionInterface')

# AbstractProgressiveService.progressResumed
e('ServiceWatcherUtil', 'AbstractProgressiveService.progressResumed', 'CALL',
  evidence='SRC AbstractProgressiveService.java:75-81 @Override public void progressResumed(); method from ServiceWatcherInteractionInterface')

# RootHelper.<init>
UNREACHABLE['RootHelper.<init>'] = ('no_trigger_in_app', 'RootHelper contains only static methods, no constructor is explicitly called in app code', 'SRC RootHelper.java:36 public class RootHelper { ... all methods are static', 'SOURCE')

# RootHelper.generateBaseFile(DocumentFile)
e('RootHelper.getFilesList(String,boolean,boolean,RootHelper$GetModeCallBack)', 'RootHelper.generateBaseFile(DocumentFile)', 'CALL',
  evidence='SRC RootHelper.java:280-283 for (DocumentFile file : files) { result.add(RootHelper.generateBaseFile(file)); }')

# RootHelper.lambda$runShellCommandToList$0
e('RootHelper.runShellCommandToList', 'RootHelper.lambda$runShellCommandToList$0', 'CALL',
  evidence='SRC RootHelper.java:50 runShellCommandWithCallback(cmd, (commandCode, exitCode, output) -> result.addAll(output))')

# RootHelper.runNonRootShellCommand
UNREACHABLE['RootHelper.runNonRootShellCommand'] = ('no_trigger_in_app', 'Method is @deprecated and grep shows no app callers; replaced by runShellCommand', 'SRC RootHelper.java:93 @deprecated Use runShellCommand instead', 'SOURCE')

# Coders$DeflateDecoder$DeflateDecoderInputStream.close
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderInputStream.close'] = ('no_trigger_in_app', 'Library stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/Coders$DeflateDecoder$DeflateDecoderInputStream from Apache Commons Compress; source not read', 'INFERRED')

# Coders$DeflateDecoder$DeflateDecoderInputStream.read()
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderInputStream.read()'] = ('no_trigger_in_app', 'Library stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/Coders$DeflateDecoder$DeflateDecoderInputStream from Apache Commons Compress; source not read', 'INFERRED')

# Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[])
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[])'] = ('no_trigger_in_app', 'Library stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/Coders$DeflateDecoder$DeflateDecoderInputStream from Apache Commons Compress; source not read', 'INFERRED')

# Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[],int,int)
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[],int,int)'] = ('no_trigger_in_app', 'Library stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/Coders$DeflateDecoder$DeflateDecoderInputStream from Apache Commons Compress; source not read', 'INFERRED')

# SevenZFile$1.count
UNREACHABLE['SevenZFile$1.count'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZFile$1.read()
UNREACHABLE['SevenZFile$1.read()'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZFile$1.read(byte[])
UNREACHABLE['SevenZFile$1.read(byte[])'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZFile$1.read(byte[],int,int)
UNREACHABLE['SevenZFile$1.read(byte[],int,int)'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZOutputFile$1.<init>
UNREACHABLE['SevenZOutputFile$1.<init>'] = ('no_trigger_in_app', 'Anonymous inner class; source file not in src/main/java; no explicit app instantiation found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZOutputFile$1.write(int)
UNREACHABLE['SevenZOutputFile$1.write(int)'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZOutputFile$1.write(byte[])
UNREACHABLE['SevenZOutputFile$1.write(byte[])'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SevenZOutputFile$1.write(byte[],int,int)
UNREACHABLE['SevenZOutputFile$1.write(byte[],int,int)'] = ('no_trigger_in_app', 'Anonymous inner class stream method; source file not in src/main/java; no explicit app call sites found', 'INFERRED com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile$1 from Apache Commons Compress; source not read', 'INFERRED')

# SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)
e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)', 'CALL',
  evidence='SRC SftpConnectDialog.java:342-344 SSHClient result = SshConnectionPool.getInstance().getConnection(hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPair)')

# SshConnectionPool.lambda$create$1
UNREACHABLE['SshConnectionPool.lambda$create$1'] = ('no_trigger_in_app', 'Grep shows no lambda$create$1 in SshConnectionPool.java; likely misnamed or obsolete', 'SRC SshConnectionPool.java:189-212 create() methods have no lambda expressions', 'SOURCE')

# SshConnectionPool.lambda$expungeAllConnections$0
e('SshConnectionPool.expungeAllConnections', 'SshConnectionPool.lambda$expungeAllConnections$0', 'ASYNC',
  evidence='SRC SshConnectionPool.java:175 AppConfig.runInBackground(() -> { if(!connections.isEmpty()) { ... } })')

# SshConnectionPool.removeConnection - already in graph_def.py (SftpConnectDialog.lambda$onCreateDialog$0 -> removeConnection)

# ColorPickerDialog$SavedState.<clinit> - already in graph_def.py line 1612
# ColorPickerDialog$SavedState.<init>(Parcel) - already in graph_def.py line 1598, 1603, 1608
# ColorPickerDialog$SavedState.<init>(Parcelable) - already in graph_def.py line 1598
# ColorPickerDialog$SavedState.writeToParcel - already in graph_def.py line 1616
# CheckableCircleView.<init> - already in graph_def.py line 1959, 1963
# CheckableCircleView.onDraw - already in graph_def.py line 1971
# CheckableCircleView.setChecked - already in graph_def.py line 1967
# CheckableCircleView.setColor - already in graph_def.py line 1963

# (Note: ColorPickerDialog$SavedState, CheckableCircleView, and SshConnectionPool.removeConnection methods are already fully labeled in graph_def.py, no new edges needed)
