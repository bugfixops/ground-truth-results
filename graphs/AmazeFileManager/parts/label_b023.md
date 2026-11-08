STATUS: RUNNING 22:59

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| Drawer$1.<init> | REACHABLE | | Anonymous ActionBarDrawerToggle constructor, created in Drawer constructor | SRC Drawer.java:217-223 shows new ActionBarDrawerToggle(...) { override methods } |
| Drawer$1.onDrawerClosed | REACHABLE | | Callback invoked by framework when drawer closes | SRC Drawer.java:224-226 shows public void onDrawerClosed(View view) calling Drawer.this.onDrawerClosed() |
| Drawer$1.onDrawerOpened | REACHABLE | | Callback invoked by framework when drawer opens | SRC Drawer.java:228-231 shows public void onDrawerOpened(View drawerView) with comment |
| Drawer$2.<init> | REACHABLE | | Anonymous ImageLoader.ImageListener constructor, created in setDrawerHeaderBackground | SRC Drawer.java:657 shows mImageLoader.get(path1, new ImageLoader.ImageListener() { |
| Drawer$2.onResponse | REACHABLE | | Callback invoked by Volley ImageLoader on successful image load | SRC Drawer.java:658-662 shows @Override onResponse setting headerImageView bitmap |
| Drawer$2.onErrorResponse | REACHABLE | | Callback invoked by Volley ImageLoader on image load error | SRC Drawer.java:664-665 shows @Override onErrorResponse(VolleyError error) {} |
| DummyFileGenerator.<init> | UNREACHABLE | no_trigger_in_app | Abstract test-only class with @RestrictTo(TESTS), no app source instantiation | SRC DummyFileGenerator.java:45-48 shows @RestrictTo(RestrictTo.Scope.TESTS) public abstract class |
| DummyFileGenerator.createFile | UNREACHABLE | no_trigger_in_app | Test-only static method with @RestrictTo(TESTS), grep shows no app callers | SRC DummyFileGenerator.java:54-82 shows @RestrictTo(RestrictTo.Scope.TESTS) public static method |
| EditTextColorStateUtil.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods, constructor never called | SRC EditTextColorStateUtil.java:18 shows public class, no instantiation found in app |
| EditTextColorStateUtil.setTint | REACHABLE | | Static method called from SmbConnectDialog.onCreateView to set EditText tint | SRC SmbConnectDialog.java:156-158 shows three calls to EditTextColorStateUtil.setTint(context, editText, accentColor) |
| EditTextColorStateUtil.createEditTextColorStateList | REACHABLE | | Private helper called from setTint method | SRC EditTextColorStateUtil.java:20-23 shows setTint calling createEditTextColorStateList(context, color) |
| EncryptDecryptUtils.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods, constructor never called | SRC EncryptDecryptUtils.java:34 shows public class, no instantiation found in app |
| EncryptDecryptUtils.startEncryption | REACHABLE | | Static method called from encrypt dialog and menu to start encryption service | SRC GeneralDialogCreation.java:695 and ItemPopupMenu.java:147 show calls to EncryptDecryptUtils.startEncryption |
| EncryptDecryptUtils.decryptFile | REACHABLE | | Static method called from decrypt menu and file open to decrypt files | SRC ItemPopupMenu.java:197 and MainFragment.java:905 show calls to EncryptDecryptUtils.decryptFile |
| EncryptDecryptUtils.findEncryptedEntry | REACHABLE | | Private helper called from decryptFile to query database | SRC EncryptDecryptUtils.java:77 shows decryptFile calling findEncryptedEntry(main.getContext(), sourceFile.getPath()) |
| EncryptDecryptUtils$1.<init> | REACHABLE | | Anonymous DecryptButtonCallbackInterface constructor, created in decryptFile | SRC EncryptDecryptUtils.java:87-98 shows new DecryptButtonCallbackInterface() { override methods } |
| EncryptDecryptUtils$1.confirm | REACHABLE | | Callback invoked when decrypt password confirmed, runs DecryptService | SRC EncryptDecryptUtils.java:89-92 shows @Override confirm(Intent intent) calling ServiceWatcherUtil.runService |
| EncryptDecryptUtils$1.failed | REACHABLE | | Callback invoked when decrypt password fails | SRC EncryptDecryptUtils.java:94-97 shows @Override failed() showing toast message |
| EncryptService.<init> | REACHABLE | | Service constructor, instantiated by framework when started | SRC EncryptService.java:40 shows public class EncryptService extends AbstractProgressiveService |
| EncryptService.onCreate | REACHABLE | | Service lifecycle method, called by framework on service creation | SRC EncryptService.java:66-71 shows @Override onCreate() registering broadcast receiver |
| EncryptService.onStartCommand | REACHABLE | | Service lifecycle method, called by framework when service started via Intent | SRC EncryptService.java:73-120 shows @Override onStartCommand setting up notification and starting BackgroundTask |
| EncryptService.onBind | REACHABLE | | Service lifecycle method, called by framework when binding to service | SRC EncryptService.java:209-212 shows @Override onBind(Intent intent) returning mBinder |
| EncryptService.onDestroy | REACHABLE | | Service lifecycle method, called by framework on service destruction | SRC EncryptService.java:214-218 shows @Override onDestroy() unregistering cancelReceiver |
| EncryptService.getNotificationManager | REACHABLE | | Getter called by AbstractProgressiveService parent to manage notifications | SRC EncryptService.java:122-125 shows @Override protected returning notificationManager |
| EncryptService.getNotificationBuilder | REACHABLE | | Getter called by AbstractProgressiveService parent for notification updates | SRC EncryptService.java:127-130 shows @Override protected returning notificationBuilder |
| EncryptService.getNotificationId | REACHABLE | | Getter called by AbstractProgressiveService parent for notification ID | SRC EncryptService.java:132-135 shows @Override protected returning NotificationConstants.ENCRYPT_ID |
| EncryptService.getTitle | REACHABLE | | Getter called by AbstractProgressiveService parent for notification title | SRC EncryptService.java:137-141 shows @Override protected returning R.string.crypt_encrypting |
| EncryptService.getNotificationCustomViewSmall | REACHABLE | | Getter called by AbstractProgressiveService parent for small notification view | SRC EncryptService.java:143-146 shows @Override protected returning customSmallContentViews |
| EncryptService.getNotificationCustomViewBig | REACHABLE | | Getter called by AbstractProgressiveService parent for big notification view | SRC EncryptService.java:148-151 shows @Override protected returning customBigContentViews |
| EncryptService.getProgressListener | REACHABLE | | Getter for progress listener, may be called by parent or binding clients | SRC EncryptService.java:153-156 shows public returning progressListener |
| EncryptService.setProgressListener | REACHABLE | | Setter for progress listener, may be called by binding clients | SRC EncryptService.java:158-162 shows @Override public setProgressListener |
| EncryptService.getDataPackages | REACHABLE | | Getter called by AbstractProgressiveService parent for data packages | SRC EncryptService.java:164-167 shows @Override protected returning dataPackages |
| EncryptService.getProgressHandler | REACHABLE | | Getter called by AbstractProgressiveService parent for progress handler | SRC EncryptService.java:169-172 shows @Override protected returning progressHandler |
| EncryptService$1.<init> | REACHABLE | | Anonymous BroadcastReceiver constructor, created as cancelReceiver field | SRC EncryptService.java:220 shows private BroadcastReceiver cancelReceiver = new BroadcastReceiver() { |
| EncryptService$1.onReceive | REACHABLE | | Callback invoked by framework when cancel broadcast received | SRC EncryptService.java:222-226 shows @Override onReceive setting progressHandler cancelled |
| EncryptService$BackgroundTask.<init> | REACHABLE | | AsyncTask constructor, instantiated in onStartCommand | SRC EncryptService.java:117 shows new BackgroundTask().execute() |
| EncryptService$BackgroundTask.doInBackground | REACHABLE | | AsyncTask method, called by framework on background thread | SRC EncryptService.java:176-203 shows @Override doInBackground performing encryption |
| EncryptService$BackgroundTask.lambda$doInBackground$0 | REACHABLE | | Lambda callback from progressHandler.setProgressListener | SRC EncryptService.java:182 shows setProgressListener((speed) -> publishResults(speed, false, false)) |
| EncryptService$BackgroundTask.onPostExecute | REACHABLE | | AsyncTask method, called by framework on UI thread after doInBackground | SRC EncryptService.java:205-207 shows @Override onPostExecute finalizing notification and stopping service |

STATUS: DONE 23:02
