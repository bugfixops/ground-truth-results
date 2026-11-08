# ---- Helper batch_033 label part (2025-01-18)

# GeneralDialogCreation$1 - AsyncTask in deleteFilesDialog, calculating file sizes for delete confirmation
# Called from MainFragment and ItemPopupMenu menu handlers (R.id.delete action)
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation$1.<init>', 'CALL',
  'AsyncTask created at line 214 to calculate sizes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:214')

e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.onPreExecute', 'ASYNC',
  'AsyncTask lifecycle',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:222-228')

e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.doInBackground', 'ASYNC',
  'AsyncTask lifecycle',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:230-262')

e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.updateViews', 'CALL',
  'Called from doInBackground to update progress',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:259')

e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.onProgressUpdate', 'ASYNC',
  'AsyncTask lifecycle',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:266-276')

e('GeneralDialogCreation$1.onProgressUpdate', 'GeneralDialogCreation$1.updateViews', 'CALL',
  'Called from onProgressUpdate',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:275-276')

e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.onPostExecute', 'ASYNC',
  'AsyncTask lifecycle',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:280-283')

e('GeneralDialogCreation$1.onPostExecute', 'GeneralDialogCreation$1.updateViews', 'CALL',
  'Called from onPostExecute',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:282')

# GeneralDialogCreation$2 - SimpleTextWatcher in showEncryptAuthenticateDialog
# Called from ItemPopupMenu encrypt action
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation$2.<init>', 'CALL',
  'TextWatcher created at line 770',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:770')

e('GeneralDialogCreation$2.<init>', 'GeneralDialogCreation$2.onTextChanged', 'GUI',
  'TextWatcher callback when password fields change',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:772-776')

# GeneralDialogCreation$SizeFormatter - IValueFormatter for pie chart in properties dialog
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation$SizeFormatter.<init>', 'CALL',
  'SizeFormatter instantiated for chart',
  evidence='INFERRED ui/dialogs/GeneralDialogCreation.java:587-598, used in PieData.setValueFormatter; instantiation in chart setup code not directly visible in app source, created by chart library')

e('GeneralDialogCreation$SizeFormatter.<init>', 'GeneralDialogCreation$SizeFormatter.getFormattedValue', 'FRAMEWORK',
  'Chart library calls getFormattedValue to format pie chart values',
  evidence='INFERRED source not read; IValueFormatter.getFormattedValue called by MPAndroidChart library')

# GenerateHashesTask - AsyncTask to generate MD5/SHA256 hashes in properties dialog
e('GeneralDialogCreation.showPropertiesDialog', 'GenerateHashesTask.<init>', 'CALL',
  'GenerateHashesTask created in properties dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:461')

e('GenerateHashesTask.<init>', 'GenerateHashesTask.doInBackground', 'ASYNC',
  'AsyncTask lifecycle',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:50-92')

e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.getMD5Checksum', 'CALL',
  'Called for non-SSH files',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:83')

e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.getSHA256Checksum', 'CALL',
  'Called for non-SSH files',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:84')

e('GenerateHashesTask.getMD5Checksum', 'GenerateHashesTask.createChecksum', 'CALL',
  'getMD5Checksum calls createChecksum',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:125')

e('GenerateHashesTask.<init>', 'GenerateHashesTask.onPostExecute', 'ASYNC',
  'AsyncTask lifecycle',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:96-116')

e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$0', 'GUI',
  'Lambda set as long-click listener for MD5 layout',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:102')

e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$1', 'GUI',
  'Lambda set as long-click listener for SHA256 layout',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:108')

# GenerateHashesTask$1 and $2 - Anonymous SshClientSessionTemplate subclasses for SFTP hash calculation
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask$1.<init>', 'CALL',
  'Anonymous SshClientSessionTemplate for MD5 via SSH',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:56-66, guarded by file.isSftp()')

e('GenerateHashesTask$1.<init>', 'GenerateHashesTask$1.execute', 'CALL',
  'SshClientUtils.execute calls the template execute method',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:56-66')

e('GenerateHashesTask.doInBackground', 'GenerateHashesTask$2.<init>', 'CALL',
  'Anonymous SshClientSessionTemplate for SHA256 via SSH',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:67-78, guarded by file.isSftp()')

e('GenerateHashesTask$2.<init>', 'GenerateHashesTask$2.execute', 'CALL',
  'SshClientUtils.execute calls the template execute method',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:67-78')

# GeneratedAppGlideModuleImpl - Generated by Glide annotation processor from AmazeFileManagerModule
# Glide framework calls these during Glide.with() initialization
e('GlideApp.with', 'GeneratedAppGlideModuleImpl.<init>', 'CALL',
  'Glide library instantiates GeneratedAppGlideModuleImpl during initialization',
  evidence='INFERRED GlideApp.with called from AppsListFragment.java:98, AppsAdapterPreloadModel.java:28, RecyclerPreloadModelProvider.java:30, etc.; Glide annotation processor generates GeneratedAppGlideModuleImpl from @GlideModule on AmazeFileManagerModule.java:17-23; source not read')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.registerComponents', 'CALL',
  'Glide calls registerComponents during initialization',
  evidence='INFERRED Glide library initialization sequence; source not read')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.applyOptions', 'CALL',
  'Glide calls applyOptions during initialization',
  evidence='INFERRED Glide library initialization sequence; source not read')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.isManifestParsingEnabled', 'CALL',
  'Glide queries manifest parsing setting',
  evidence='INFERRED Glide library initialization sequence; source not read')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.getExcludedModuleClasses', 'CALL',
  'Glide queries excluded modules',
  evidence='INFERRED Glide library initialization sequence; source not read')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.getRequestManagerFactory', 'CALL',
  'Glide calls to get the request manager factory',
  evidence='INFERRED Glide library initialization sequence; source not read')

# GeneratedRequestManagerFactory - Generated by Glide annotation processor
e('GeneratedAppGlideModuleImpl.getRequestManagerFactory', 'GeneratedRequestManagerFactory.<init>', 'CALL',
  'Glide instantiates GeneratedRequestManagerFactory',
  evidence='INFERRED Glide library initialization; source not read')

e('GeneratedRequestManagerFactory.<init>', 'GeneratedRequestManagerFactory.build', 'CALL',
  'Glide calls build to create RequestManager instances',
  evidence='INFERRED Glide library RequestManager creation; source not read')

# GenericCopyUtil - File copy utility used by CopyService
e('CopyService.onStartCommand', 'GenericCopyUtil.<init>', 'CALL',
  'GenericCopyUtil created in CopyService',
  evidence='SRC asynchronous/services/CopyService.java:474')

e('GenericCopyUtil.<init>', 'GenericCopyUtil.copy', 'CALL',
  'copy method called to start copy operation',
  evidence='INFERRED GenericCopyUtil.copy is public entry point after construction; usage context in CopyService')

e('GenericCopyUtil.copy', 'GenericCopyUtil.startCopy', 'CALL',
  'copy delegates to startCopy',
  evidence='SRC utils/files/GenericCopyUtil.java:422-427')

e('GenericCopyUtil.startCopy', 'GenericCopyUtil.copyFile', 'CALL',
  'startCopy calls appropriate copyFile overload',
  evidence='SRC utils/files/GenericCopyUtil.java:338-343')

e('GenericCopyUtil.copyFile', 'GenericCopyUtil.doCopy', 'CALL',
  'All copyFile overloads delegate to doCopy',
  evidence='SRC utils/files/GenericCopyUtil.java:435, 447, 459, 470')

# All methods in batch_033 are REACHABLE
# No UNREACHABLE methods in this batch
