# ---- resume batch rb_09 (2026-10-28)

# FtpNotification methods
e('FtpService.onStartCommand', 'FtpNotification.startNotification', 'CALL', 'create FTP server start notification',
  evidence='SRC asynchronous/services/ftp/FtpService.java:140')

# FtpReceiver static initializer
e('FtpReceiver.<init>', 'FtpReceiver.<clinit>', 'CALL', 'static field TAG initialized at class load',
  evidence='SRC asynchronous/services/ftp/FtpReceiver.java:13')

# FtpTileService EventBus subscriber
e('FtpService.onStartCommand', 'FtpTileService.onFtpReceiverActions', 'ASYNC', 'EventBus posts FtpReceiverActions signal',
  evidence='SRC asynchronous/services/ftp/FtpTileService.java:26; INFERRED EventBus.post dispatches to @Subscribe methods')

# GeneralDialogCreation deleteFilesDialog AsyncTask ($1)
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation$1.<init>', 'CALL', 'anonymous AsyncTask instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:211')
e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.onPreExecute', 'LIFECYCLE', 'AsyncTask.onPreExecute before doInBackground',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:220; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.onPreExecute', 'GeneralDialogCreation$1.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground runs on worker thread',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:227; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.onProgressUpdate', 'LIFECYCLE', 'publishProgress triggers onProgressUpdate',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:259; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute after doInBackground completes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:264; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.onProgressUpdate', 'GeneralDialogCreation$1.updateViews', 'CALL', 'update dialog views with progress',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:274')
e('GeneralDialogCreation$1.onPostExecute', 'GeneralDialogCreation$1.updateViews', 'CALL', 'update dialog views with final data',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:280')

# GeneralDialogCreation showEncryptAuthenticateDialog TextWatcher ($2)
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation$2.<init>', 'CALL', 'anonymous TextWatcher instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:770')
e('GeneralDialogCreation$2.<init>', 'GeneralDialogCreation$2.onTextChanged', 'LIFECYCLE', 'TextWatcher.onTextChanged when text changes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:772; password fields add this listener at 779-781')

# GeneralDialogCreation SizeFormatter
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation$SizeFormatter.<init>', 'CALL', 'chart value formatter instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:508')
e('GeneralDialogCreation$SizeFormatter.<init>', 'GeneralDialogCreation$SizeFormatter.getFormattedValue', 'CALL', 'chart library calls formatter for each data point',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:592; INFERRED MPAndroidChart IValueFormatter interface')

# GeneralDialogCreation showCompressDialog lambdas
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$28', 'CALL', 'lambda: positive button callback',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:962')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$29', 'CALL', 'lambda: validator callback for text input',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:969')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$30', 'CALL', 'lambda: post runnable to set cursor position',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:990')

# GeneralDialogCreation public methods
e('MainFragment.onOptionsItemSelected', 'GeneralDialogCreation.showCompressDialog', 'CALL', 'show compress dialog from menu',
  evidence='SRC fragments/MainFragment.java:738')
e('TextEditorActivity.onOptionsItemSelected', 'GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CALL', 'show file properties dialog',
  evidence='SRC activities/TextEditorActivity.java:369')
e('SmbConnectDialog.onCreateDialog', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL', 'show SMB help dialog',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:164')

# GenerateHashesTask lambdas
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$0', 'CALL', 'lambda: MD5 long-click listener',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:107')
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$1', 'CALL', 'lambda: SHA256 long-click listener',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:112')

# GetSshHostFingerprintTask AsyncTask
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'SSH fingerprint task instantiated',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178')
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'LIFECYCLE', 'AsyncTask.onPreExecute before doInBackground',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:112; INFERRED AsyncTask lifecycle')
e('GetSshHostFingerprintTask.onPreExecute', 'GetSshHostFingerprintTask.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground gets SSH host key',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:77; INFERRED AsyncTask lifecycle')
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'lambda: HostKeyVerifier callback',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:84')
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute returns result',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:117; INFERRED AsyncTask lifecycle')

# UNREACHABLE methods

UNREACHABLE['FtpNotification.<init>'] = ('no_trigger_in_app', 'all methods are static; constructor never called', 'SRC ui/notifications/FtpNotification.java:24-61', 'SOURCE')

UNREACHABLE['FtpNotification.removeNotification'] = ('no_trigger_in_app', 'private static method with no call sites in app source', 'SRC ui/notifications/FtpNotification.java:98', 'SOURCE')

# GlideOptions, GlideRequest, GlideRequests are Glide-generated classes
# Source files do not exist in src/main (generated at build time)
# Per KIRO_CONVERT_APPS section 3, library/generated class methods are INFERRED

UNREACHABLE['GlideOptions.<init>'] = ('no_trigger_in_app', 'Glide-generated class; no direct instantiation found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.apply'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.autoClone'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.clone'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.lock'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.addListener'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.apply'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.downsample'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.listener'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.optionalCenterInside'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.optionalFitCenter'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.set'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.transform(Transformation)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequests.as'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequests.setRequestOptions'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

# HybridFile$10$1 - RemoteFileInputStream subclass with custom close inside getInputStream(Context)
e('HybridFile.getInputStream(Context)', 'HybridFile$10.<init>', 'CALL', 'anonymous SFtpClientTemplate instantiated for SFTP stream',
  evidence='SRC filesystem/HybridFile.java:948')
e('HybridFile$10.execute', 'HybridFile$10$1.<init>', 'CALL', 'anonymous RemoteFileInputStream subclass instantiated',
  evidence='SRC filesystem/HybridFile.java:952')
e('HybridFile$10$1.<init>', 'HybridFile$10$1.close', 'CALL', 'close() method called when stream is closed',
  evidence='SRC filesystem/HybridFile.java:954; overrides RemoteFileInputStream.close()')

