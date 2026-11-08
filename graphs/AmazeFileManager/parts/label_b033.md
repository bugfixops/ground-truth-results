STATUS: RUNNING 23:19

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| GeneralDialogCreation$1.<init> | REACHABLE | | AsyncTask created in deleteFilesDialog at line 214, called from MainFragment.java:660 and ItemPopupMenu.java:123 menu handlers | SRC ui/dialogs/GeneralDialogCreation.java:214 |
| GeneralDialogCreation$1.doInBackground | REACHABLE | | AsyncTask lifecycle method called by framework | SRC ui/dialogs/GeneralDialogCreation.java:230-262 |
| GeneralDialogCreation$1.onPostExecute | REACHABLE | | AsyncTask lifecycle method called by framework | SRC ui/dialogs/GeneralDialogCreation.java:280-283 |
| GeneralDialogCreation$1.onPreExecute | REACHABLE | | AsyncTask lifecycle method called by framework | SRC ui/dialogs/GeneralDialogCreation.java:222-228 |
| GeneralDialogCreation$1.onProgressUpdate | REACHABLE | | AsyncTask lifecycle; publishProgress called at line 259 | SRC ui/dialogs/GeneralDialogCreation.java:259, 266-276 |
| GeneralDialogCreation$1.updateViews | REACHABLE | | Called from onProgressUpdate and onPostExecute | SRC ui/dialogs/GeneralDialogCreation.java:259, 275-276, 282, 285-321 |
| GeneralDialogCreation$2.<init> | REACHABLE | | SimpleTextWatcher anonymous class created in showEncryptAuthenticateDialog, called from ItemPopupMenu.java:168 | SRC ui/dialogs/GeneralDialogCreation.java:770 |
| GeneralDialogCreation$2.onTextChanged | REACHABLE | | TextWatcher callback when password fields change | SRC ui/dialogs/GeneralDialogCreation.java:772-776 |
| GeneralDialogCreation$SizeFormatter.<init> | REACHABLE | | IValueFormatter created for pie chart in properties dialog | SRC ui/dialogs/GeneralDialogCreation.java:587-589 |
| GeneralDialogCreation$SizeFormatter.getFormattedValue | REACHABLE | | MPAndroidChart library calls to format pie chart values | INFERRED ui/dialogs/GeneralDialogCreation.java:592-598; IValueFormatter interface method called by chart library; library source not read |
| GenerateHashesTask$1.<init> | REACHABLE | | Anonymous SshClientSessionTemplate for MD5 via SSH, created at line 56 | SRC asynchronous/asynctasks/GenerateHashesTask.java:56-66, guarded by file.isSftp() at line 55 |
| GenerateHashesTask$1.execute | REACHABLE | | SshClientUtils.execute calls template execute method | SRC asynchronous/asynctasks/GenerateHashesTask.java:56-66 |
| GenerateHashesTask$2.<init> | REACHABLE | | Anonymous SshClientSessionTemplate for SHA256 via SSH, created at line 67 | SRC asynchronous/asynctasks/GenerateHashesTask.java:67-78, guarded by file.isSftp() at line 55 |
| GenerateHashesTask$2.execute | REACHABLE | | SshClientUtils.execute calls template execute method | SRC asynchronous/asynctasks/GenerateHashesTask.java:67-78 |
| GenerateHashesTask.<init> | REACHABLE | | Created in showPropertiesDialog for hash generation | SRC ui/dialogs/GeneralDialogCreation.java:461-462 |
| GenerateHashesTask.createChecksum | REACHABLE | | Called from getMD5Checksum | SRC asynchronous/asynctasks/GenerateHashesTask.java:125, 150-162 |
| GenerateHashesTask.doInBackground | REACHABLE | | AsyncTask lifecycle method | SRC asynchronous/asynctasks/GenerateHashesTask.java:50-92 |
| GenerateHashesTask.getMD5Checksum | REACHABLE | | Called from doInBackground for non-SFTP files | SRC asynchronous/asynctasks/GenerateHashesTask.java:83, 122-130 |
| GenerateHashesTask.getSHA256Checksum | REACHABLE | | Called from doInBackground for non-SFTP files | SRC asynchronous/asynctasks/GenerateHashesTask.java:84, 132-149 |
| GenerateHashesTask.lambda$onPostExecute$0 | REACHABLE | | Lambda set as long-click listener for MD5 layout | SRC asynchronous/asynctasks/GenerateHashesTask.java:102-106 |
| GenerateHashesTask.lambda$onPostExecute$1 | REACHABLE | | Lambda set as long-click listener for SHA256 layout | SRC asynchronous/asynctasks/GenerateHashesTask.java:108-112 |
| GenerateHashesTask.onPostExecute | REACHABLE | | AsyncTask lifecycle method | SRC asynchronous/asynctasks/GenerateHashesTask.java:96-116 |
| GeneratedAppGlideModuleImpl.<init> | REACHABLE | | Glide library instantiates during initialization when GlideApp.with() called | INFERRED GlideApp.with() called from AppsListFragment.java:98, AppsAdapterPreloadModel.java:28, RecyclerPreloadModelProvider.java:30; Glide generates from @GlideModule on AmazeFileManagerModule.java:17; library source not read |
| GeneratedAppGlideModuleImpl.applyOptions | REACHABLE | | Glide calls during initialization sequence | INFERRED Glide library initialization; library source not read |
| GeneratedAppGlideModuleImpl.getExcludedModuleClasses | REACHABLE | | Glide queries excluded modules during init | INFERRED Glide library initialization; library source not read |
| GeneratedAppGlideModuleImpl.getRequestManagerFactory | REACHABLE | | Glide calls to get request manager factory | INFERRED Glide library initialization; library source not read |
| GeneratedAppGlideModuleImpl.isManifestParsingEnabled | REACHABLE | | Glide queries manifest parsing setting | INFERRED Glide library initialization; library source not read |
| GeneratedAppGlideModuleImpl.registerComponents | REACHABLE | | Glide calls to register custom components | INFERRED Glide library calls; delegates to AmazeFileManagerModule.registerComponents at AmazeFileManagerModule.java:20-23; library source not read |
| GeneratedRequestManagerFactory.<init> | REACHABLE | | Glide instantiates when getRequestManagerFactory returns it | INFERRED Glide library RequestManager creation; library source not read |
| GeneratedRequestManagerFactory.build | REACHABLE | | Glide calls to create RequestManager instances for each context | INFERRED Glide library RequestManager creation; library source not read |
| GenericCopyUtil.<init> | REACHABLE | | Created in CopyService.onStartCommand | SRC asynchronous/services/CopyService.java:474 |
| GenericCopyUtil.copy | REACHABLE | | Public entry point called after construction in CopyService | SRC utils/files/GenericCopyUtil.java:417-427 |
| GenericCopyUtil.copyFile(BufferedInputStream,BufferedOutputStream) | REACHABLE | | Called from startCopy | SRC utils/files/GenericCopyUtil.java:338, 453-460 |
| GenericCopyUtil.copyFile(BufferedInputStream,FileChannel) | REACHABLE | | Called from startCopy | SRC utils/files/GenericCopyUtil.java:340, 432-440 |
| GenericCopyUtil.copyFile(FileChannel,BufferedOutputStream) | REACHABLE | | Called from startCopy | SRC utils/files/GenericCopyUtil.java:342, 465-472 |
| GenericCopyUtil.copyFile(FileChannel,FileChannel) | REACHABLE | | Called from startCopy | SRC utils/files/GenericCopyUtil.java:343, 442-451 |
| GenericCopyUtil.doCopy | REACHABLE | | All copyFile overloads delegate to doCopy | SRC utils/files/GenericCopyUtil.java:437, 449, 459, 470, 474-487 |
| GenericCopyUtil.startCopy | REACHABLE | | Called from copy method | SRC utils/files/GenericCopyUtil.java:424, 105-411 |

STATUS: DONE 23:25
