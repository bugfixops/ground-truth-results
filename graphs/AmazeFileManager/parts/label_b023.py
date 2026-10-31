# ---- Helper batch_023 label part (2025-01-10)

# Drawer$1 - Anonymous ActionBarDrawerToggle created in Drawer constructor
e('Drawer.<init>', 'Drawer$1.<init>', 'EXPLICIT', 'Creates anonymous ActionBarDrawerToggle in Drawer constructor when !isDrawerLocked',
  evidence='SRC Drawer.java:217-223 shows mDrawerToggle = new ActionBarDrawerToggle(...) { override methods }')

e('DrawerLayout.setDrawerListener', 'Drawer$1.onDrawerClosed', 'FRAMEWORK', 'Framework invokes onDrawerClosed callback when drawer closes',
  evidence='SRC Drawer.java:224-226 shows public void onDrawerClosed(View view) calling Drawer.this.onDrawerClosed()')

e('DrawerLayout.setDrawerListener', 'Drawer$1.onDrawerOpened', 'FRAMEWORK', 'Framework invokes onDrawerOpened callback when drawer opens',
  evidence='SRC Drawer.java:228-231 shows public void onDrawerOpened(View drawerView) with comment')

# Drawer$2 - Anonymous ImageLoader.ImageListener created in setDrawerHeaderBackground
e('Drawer.setDrawerHeaderBackground', 'Drawer$2.<init>', 'EXPLICIT', 'Creates anonymous ImageLoader.ImageListener in setDrawerHeaderBackground',
  evidence='SRC Drawer.java:657 shows mImageLoader.get(path1, new ImageLoader.ImageListener() {')

e('ImageLoader.get', 'Drawer$2.onResponse', 'FRAMEWORK', 'Volley ImageLoader invokes onResponse on successful image load',
  evidence='SRC Drawer.java:658-662 shows @Override onResponse setting headerImageView bitmap')

e('ImageLoader.get', 'Drawer$2.onErrorResponse', 'FRAMEWORK', 'Volley ImageLoader invokes onErrorResponse on image load error',
  evidence='SRC Drawer.java:664-665 shows @Override onErrorResponse(VolleyError error) {}')

# EditTextColorStateUtil - Utility class with static methods
e('SmbConnectDialog.onCreateView', 'EditTextColorStateUtil.setTint', 'CALL', 'SmbConnectDialog calls setTint to style EditText fields',
  evidence='SRC SmbConnectDialog.java:156-158 shows three calls EditTextColorStateUtil.setTint(context, editText, accentColor)')

e('EditTextColorStateUtil.setTint', 'EditTextColorStateUtil.createEditTextColorStateList', 'CALL', 'setTint calls private helper to create ColorStateList',
  evidence='SRC EditTextColorStateUtil.java:20-23 shows ColorStateList editTextColorStateList = createEditTextColorStateList(context, color)')

# EncryptDecryptUtils - Encryption utility class with static methods
e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'EncryptDecryptUtils.startEncryption', 'CALL', 'Dialog callback invokes startEncryption after user enters filename',
  evidence='SRC GeneralDialogCreation.java:695 shows EncryptDecryptUtils.startEncryption(c, intentParcelable.getPath(), password, intent)')

e('ItemPopupMenu.onMenuItemClick', 'EncryptDecryptUtils.startEncryption', 'CALL', 'Encrypt menu action invokes startEncryption',
  evidence='SRC ItemPopupMenu.java:147 shows EncryptDecryptUtils.startEncryption(context, rowItem.generateBaseFile().getPath(), password, intent)')

e('ItemPopupMenu.onMenuItemClick', 'EncryptDecryptUtils.decryptFile', 'CALL', 'Decrypt menu action invokes decryptFile',
  evidence='SRC ItemPopupMenu.java:197 shows EncryptDecryptUtils.decryptFile(context, mainActivity, mainFragment, ...)' )

e('MainFragment.onItemClick', 'EncryptDecryptUtils.decryptFile', 'CALL', 'Clicking encrypted file invokes decryptFile',
  evidence='SRC MainFragment.java:905 shows EncryptDecryptUtils.decryptFile(getContext(), getMainActivity(), ma, openMode, ...)')

e('EncryptDecryptUtils.decryptFile', 'EncryptDecryptUtils.findEncryptedEntry', 'CALL', 'decryptFile calls private helper to find database entry',
  evidence='SRC EncryptDecryptUtils.java:77 shows encryptedEntry = findEncryptedEntry(main.getContext(), sourceFile.getPath())')

# EncryptDecryptUtils$1 - Anonymous DecryptButtonCallbackInterface
e('EncryptDecryptUtils.decryptFile', 'EncryptDecryptUtils$1.<init>', 'EXPLICIT', 'Creates anonymous DecryptButtonCallbackInterface in decryptFile',
  evidence='SRC EncryptDecryptUtils.java:87-88 shows DecryptButtonCallbackInterface decryptButtonCallbackInterface = new DecryptButtonCallbackInterface() {')

e('GeneralDialogCreation.showDecryptDialog', 'EncryptDecryptUtils$1.confirm', 'CALL', 'Dialog invokes confirm callback when password matches',
  evidence='SRC EncryptDecryptUtils.java:89-92 shows @Override confirm(Intent intent) calling ServiceWatcherUtil.runService')

e('GeneralDialogCreation.showDecryptDialog', 'EncryptDecryptUtils$1.failed', 'CALL', 'Dialog invokes failed callback when password does not match',
  evidence='SRC EncryptDecryptUtils.java:94-97 shows @Override failed() showing toast R.string.crypt_decryption_fail_password')

# EncryptService - Service for encryption
e('EncryptDecryptUtils.startEncryption', 'EncryptService.<init>', 'SYSTEM', 'Framework creates EncryptService when started via Intent',
  evidence='SRC EncryptDecryptUtils.java:59 shows ServiceWatcherUtil.runService(c, intent) with EncryptService intent')

e('Context.startService', 'EncryptService.onCreate', 'LIFECYCLE', 'Framework calls onCreate when service created',
  evidence='SRC EncryptService.java:66-71 shows @Override onCreate() registering broadcast receiver')

e('Context.startService', 'EncryptService.onStartCommand', 'LIFECYCLE', 'Framework calls onStartCommand when service started',
  evidence='SRC EncryptService.java:73-120 shows @Override onStartCommand extracting intent extras and starting BackgroundTask')

e('Context.bindService', 'EncryptService.onBind', 'LIFECYCLE', 'Framework calls onBind when clients bind to service',
  evidence='SRC EncryptService.java:209-212 shows @Override onBind(Intent intent) returning mBinder')

e('Context.stopService', 'EncryptService.onDestroy', 'LIFECYCLE', 'Framework calls onDestroy when service destroyed',
  evidence='SRC EncryptService.java:214-218 shows @Override onDestroy() unregistering cancelReceiver')

e('AbstractProgressiveService.publishResults', 'EncryptService.getNotificationManager', 'CALL', 'Parent calls getter to manage notifications',
  evidence='SRC EncryptService.java:122-125 shows @Override protected getNotificationManager() returning notificationManager')

e('AbstractProgressiveService.publishResults', 'EncryptService.getNotificationBuilder', 'CALL', 'Parent calls getter for notification updates',
  evidence='SRC EncryptService.java:127-130 shows @Override protected getNotificationBuilder() returning notificationBuilder')

e('AbstractProgressiveService.publishResults', 'EncryptService.getNotificationId', 'CALL', 'Parent calls getter for notification ID',
  evidence='SRC EncryptService.java:132-135 shows @Override protected getNotificationId() returning NotificationConstants.ENCRYPT_ID')

e('AbstractProgressiveService.initNotificationViews', 'EncryptService.getTitle', 'CALL', 'Parent calls getTitle for notification title resource',
  evidence='SRC EncryptService.java:137-141 shows @Override protected getTitle(boolean move) returning R.string.crypt_encrypting')

e('AbstractProgressiveService.updateNotification', 'EncryptService.getNotificationCustomViewSmall', 'CALL', 'Parent calls getter for small notification view',
  evidence='SRC EncryptService.java:143-146 shows @Override protected getNotificationCustomViewSmall() returning customSmallContentViews')

e('AbstractProgressiveService.updateNotification', 'EncryptService.getNotificationCustomViewBig', 'CALL', 'Parent calls getter for big notification view',
  evidence='SRC EncryptService.java:148-151 shows @Override protected getNotificationCustomViewBig() returning customBigContentViews')

e('ObtainableServiceBinder.getService', 'EncryptService.getProgressListener', 'CALL', 'Binding clients may call getter to access progress listener',
  evidence='SRC EncryptService.java:153-156 shows public getProgressListener() returning progressListener')

e('ObtainableServiceBinder.getService', 'EncryptService.setProgressListener', 'CALL', 'Binding clients may call setter to register progress listener',
  evidence='SRC EncryptService.java:158-162 shows @Override public setProgressListener(ProgressListener progressListener)')

e('AbstractProgressiveService.addFirstDatapoint', 'EncryptService.getDataPackages', 'CALL', 'Parent calls getter for data packages list',
  evidence='SRC EncryptService.java:164-167 shows @Override protected getDataPackages() returning dataPackages')

e('AbstractProgressiveService.publishResults', 'EncryptService.getProgressHandler', 'CALL', 'Parent calls getter for progress handler',
  evidence='SRC EncryptService.java:169-172 shows @Override protected getProgressHandler() returning progressHandler')

# EncryptService$1 - BroadcastReceiver for cancel
e('EncryptService.onCreate', 'EncryptService$1.<init>', 'EXPLICIT', 'Creates anonymous BroadcastReceiver as cancelReceiver field',
  evidence='SRC EncryptService.java:220 shows private BroadcastReceiver cancelReceiver = new BroadcastReceiver() {')

e('Context.sendBroadcast', 'EncryptService$1.onReceive', 'SYSTEM', 'Framework invokes onReceive when TAG_BROADCAST_CRYPT_CANCEL broadcast sent',
  evidence='SRC EncryptService.java:222-226 shows @Override onReceive setting progressHandler.setCancelled(true)')

# EncryptService$BackgroundTask - AsyncTask performing encryption
e('EncryptService.onStartCommand', 'EncryptService$BackgroundTask.<init>', 'EXPLICIT', 'onStartCommand creates BackgroundTask to perform encryption',
  evidence='SRC EncryptService.java:117 shows new BackgroundTask().execute()')

e('AsyncTask.execute', 'EncryptService$BackgroundTask.doInBackground', 'ASYNC', 'AsyncTask framework calls doInBackground on worker thread',
  evidence='SRC EncryptService.java:176-203 shows @Override doInBackground(Void... params) performing encryption via CryptUtil')

e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.lambda$doInBackground$0', 'CALL', 'doInBackground sets lambda as progress listener callback',
  evidence='SRC EncryptService.java:182 shows progressHandler.setProgressListener((speed) -> publishResults(speed, false, false))')

e('AsyncTask.execute', 'EncryptService$BackgroundTask.onPostExecute', 'ASYNC', 'AsyncTask framework calls onPostExecute on UI thread after completion',
  evidence='SRC EncryptService.java:205-207 shows @Override onPostExecute(Void aVoid) finalizing notification and calling stopSelf()')

# UNREACHABLE methods
UNREACHABLE_PART_B023 = {
    'DummyFileGenerator.<init>': ('no_trigger_in_app', 'Abstract test-only class with @RestrictTo(TESTS) annotation, no app source instantiation found', 'SRC DummyFileGenerator.java:45-48', 'SOURCE'),
    'DummyFileGenerator.createFile': ('no_trigger_in_app', 'Test-only static method with @RestrictTo(TESTS) annotation, grep -rn DummyFileGenerator in app source shows no callers', 'SRC DummyFileGenerator.java:54-82', 'SOURCE'),
    'EditTextColorStateUtil.<init>': ('no_trigger_in_app', 'Utility class with only static methods, constructor never instantiated in app source', 'SRC EditTextColorStateUtil.java:18', 'SOURCE'),
    'EncryptDecryptUtils.<init>': ('no_trigger_in_app', 'Utility class with only static methods, constructor never instantiated in app source', 'SRC EncryptDecryptUtils.java:34', 'SOURCE'),
}
