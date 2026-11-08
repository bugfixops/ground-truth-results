STATUS: RUNNING 23:09

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| FtpReceiver.<clinit> | UNREACHABLE | framework_never_calls | Static initializer for TAG field, executed when class loads | SRC FtpReceiver.java:13 static final String TAG = FtpReceiver.class.getSimpleName() |
| FtpReceiver.<init> | UNREACHABLE | framework_never_calls | Default constructor, called by Android framework when instantiating receiver | SRC FtpReceiver.java:11 public class FtpReceiver extends BroadcastReceiver |
| FtpReceiver.onReceive | REACHABLE | | BroadcastReceiver method triggered by ACTION_START/STOP_FTPSERVER intents | SRC FtpReceiver.java:16-27 onReceive method, FtpServerFragment.java:376,383, FtpTileService.java:48,54, FtpNotification.java:50 |
| FoldersPref.<init> | UNREACHABLE | framework_never_calls | Default constructor, called by Android framework when instantiating fragment | SRC FoldersPref.java:35 public class FoldersPref extends PreferenceFragment |
| FoldersPref.disableButtonIfNotPath | REACHABLE | | Helper method to validate path field in dialogs | SRC FoldersPref.java:223-229 method definition, called from lines 117,173 |
| FoldersPref.disableButtonIfTitleEmpty | REACHABLE | | Helper method to validate title field in dialogs | SRC FoldersPref.java:232-237 method definition, called from lines 116,172 |
| FoldersPref.lambda$loadCreateDialog$0 | REACHABLE | | Lambda onClick listener for create dialog positive button | SRC FoldersPref.java:119-137 setOnClickListener(view -> { ... }) |
| FoldersPref.lambda$loadDeleteDialog$3 | REACHABLE | | Lambda onClick listener for delete dialog positive button | SRC FoldersPref.java:212-222 setOnClickListener(view -> { ... }) |
| FoldersPref.lambda$loadEditDialog$2 | REACHABLE | | Lambda onClick listener for edit dialog positive button | SRC FoldersPref.java:175-196 setOnClickListener(view -> { ... }) |
| FoldersPref.lambda$null$1 | REACHABLE | | Inner lambda passed to AppConfig.runInBackground | SRC FoldersPref.java:192-194 runInBackground(() -> utilsHandler.renameBookmark(...)) |
| FoldersPref.loadCreateDialog | REACHABLE | | Shows dialog to create new bookmark folder | SRC FoldersPref.java:99-138 method definition, called from line 95 |
| FoldersPref.loadDeleteDialog | REACHABLE | | Shows dialog to delete bookmark folder | SRC FoldersPref.java:199-223 method definition, called from line 88 |
| FoldersPref.loadEditDialog | REACHABLE | | Shows dialog to edit bookmark folder | SRC FoldersPref.java:140-198 method definition, called from line 85 |
| FoldersPref.onCreate | REACHABLE | | PreferenceFragment lifecycle method, loads preferences | SRC FoldersPref.java:44-68 method definition, PreferencesActivity.java:261 instantiates fragment |
| FoldersPref.onPreferenceClick | REACHABLE | | Handles clicks on preferences to show dialogs | SRC FoldersPref.java:78-98 method definition, set as listener at lines 58,64 |
| FoldersPref.onResume | UNREACHABLE | framework_never_calls | Lifecycle callback that calls onCreate(null) | SRC FoldersPref.java:73-76 onResume() { super.onResume(); onCreate(null); } |
| FoldersPref$1.<init> | UNREACHABLE | framework_never_calls | Constructor for anonymous TextWatcher inner class | SRC FoldersPref.java:223 new SimpleTextWatcher() creates instance |
| FoldersPref$1.afterTextChanged | REACHABLE | | TextWatcher callback for path validation | SRC FoldersPref.java:224-228 afterTextChanged override in anonymous class |
| FoldersPref$2.<init> | UNREACHABLE | framework_never_calls | Constructor for anonymous TextWatcher inner class | SRC FoldersPref.java:233 new SimpleTextWatcher() creates instance |
| FoldersPref$2.afterTextChanged | REACHABLE | | TextWatcher callback for title validation | SRC FoldersPref.java:234-237 afterTextChanged override in anonymous class |
| FtpNotification.<init> | UNREACHABLE | no_trigger_in_app | Private constructor, all methods are static | SRC FtpNotification.java:25 public class FtpNotification - only static methods used |
| FtpNotification.buildNotification | REACHABLE | | Builds notification for FTP service | SRC FtpNotification.java:30-59 method definition, called from lines 65,84 |
| FtpNotification.removeNotification | UNREACHABLE | no_trigger_in_app | Private method never called in the app | SRC FtpNotification.java:93-97 private static void removeNotification - no callers |
| FtpNotification.startNotification | REACHABLE | | Creates initial notification when FTP service starts | SRC FtpNotification.java:61-68 method definition, FtpService.java:140 calls it |
| FtpNotification.updateNotification | REACHABLE | | Updates notification with FTP server address | SRC FtpNotification.java:70-90 method definition, FtpServerFragment.java:355 calls it |

STATUS: DONE 23:11
