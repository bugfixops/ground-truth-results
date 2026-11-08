# ---- Helper batch_029 label part (2024-01-10)

# FtpReceiver - BroadcastReceiver for FTP service control
# Registered in manifest with exported="true" and receives intents from FtpServerFragment, FtpTileService, and FtpNotification
e('FtpServerFragment.startServer', 'FtpReceiver.onReceive', 'INTENT', 
  'sendBroadcast ACTION_START_FTPSERVER triggers receiver',
  evidence='SRC FtpServerFragment.java:376 sendBroadcast(ACTION_START_FTPSERVER), manifest line 206 registers receiver')

e('FtpServerFragment.stopServer', 'FtpReceiver.onReceive', 'INTENT',
  'sendBroadcast ACTION_STOP_FTPSERVER triggers receiver',
  evidence='SRC FtpServerFragment.java:383 sendBroadcast(ACTION_STOP_FTPSERVER), manifest line 206 registers receiver')

e('FtpTileService.onClick', 'FtpReceiver.onReceive', 'INTENT',
  'sendBroadcast ACTION_START/STOP_FTPSERVER from tile service',
  evidence='SRC FtpTileService.java:48,54 sendBroadcast(ACTION_STOP/START_FTPSERVER), manifest line 206 registers receiver')

e('FtpNotification.buildNotification', 'FtpReceiver.onReceive', 'INTENT',
  'PendingIntent.getBroadcast for stop action in notification',
  evidence='SRC FtpNotification.java:50-51 PendingIntent.getBroadcast(stopIntent with ACTION_STOP_FTPSERVER), manifest line 206 registers receiver')

# Note: FtpReceiver.onReceive calls FtpService start/stop but FtpService is not in this batch

# FtpNotification - Notification builder for FTP service
e('FtpService.onStartCommand', 'FtpNotification.startNotification', 'CALL',
  'FtpService calls startNotification when starting foreground',
  evidence='SRC FtpService.java:140 Notification notification = FtpNotification.startNotification(getApplicationContext(), isStartedByTile)')

e('FtpNotification.startNotification', 'FtpNotification.buildNotification', 'CALL',
  'startNotification calls buildNotification',
  evidence='SRC FtpNotification.java:65-66 NotificationCompat.Builder builder = buildNotification(...)')

e('FtpServerFragment.onFtpReceiveActions', 'FtpNotification.updateNotification', 'CALL',
  'Fragment updates notification when FTP status changes',
  evidence='SRC FtpServerFragment.java:355 FtpNotification.updateNotification(getContext(), STARTED_FROM_TILE.equals(signal))')

e('FtpNotification.updateNotification', 'FtpNotification.buildNotification', 'CALL',
  'updateNotification calls buildNotification',
  evidence='SRC FtpNotification.java:84-85 NotificationCompat.Builder builder = buildNotification(...)')

# FoldersPref - PreferenceFragment for managing bookmark folders
e('PreferencesActivity.selectItem', 'FoldersPref.onCreate', 'LIFECYCLE',
  'PreferenceFragment instantiated and onCreate called by PreferencesActivity',
  evidence='SRC PreferencesActivity.java:261 loadPrefFragment(new FoldersPref(), R.string.sidebar_folders_title)')

e('FoldersPref.onCreate', 'FoldersPref.onPreferenceClick', 'GUI',
  'Preferences set click listener to this fragment',
  evidence='SRC FoldersPref.java:58 findPreference(PreferencesConstants.PREFERENCE_SHORTCUT).setOnPreferenceClickListener(this); line 64 p.setOnPreferenceClickListener(this)')

e('FoldersPref.onPreferenceClick', 'FoldersPref.loadCreateDialog', 'CALL',
  'Click on PREFERENCE_SHORTCUT loads create dialog',
  evidence='SRC FoldersPref.java:90-95 if(preference.getKey().equals(PreferencesConstants.PREFERENCE_SHORTCUT)) ... loadCreateDialog()')

e('FoldersPref.onPreferenceClick', 'FoldersPref.loadEditDialog', 'CALL',
  'Click on PathSwitchPreference EDIT action loads edit dialog',
  evidence='SRC FoldersPref.java:82-85 case PathSwitchPreference.EDIT: loadEditDialog((PathSwitchPreference) preference)')

e('FoldersPref.onPreferenceClick', 'FoldersPref.loadDeleteDialog', 'CALL',
  'Click on PathSwitchPreference DELETE action loads delete dialog',
  evidence='SRC FoldersPref.java:86-88 case PathSwitchPreference.DELETE: loadDeleteDialog((PathSwitchPreference) preference)')

e('FoldersPref.loadCreateDialog', 'FoldersPref.disableButtonIfTitleEmpty', 'CALL',
  'Create dialog calls helper to validate title',
  evidence='SRC FoldersPref.java:116 disableButtonIfTitleEmpty(txtShortcutName, dialog)')

e('FoldersPref.loadCreateDialog', 'FoldersPref.disableButtonIfNotPath', 'CALL',
  'Create dialog calls helper to validate path',
  evidence='SRC FoldersPref.java:117 disableButtonIfNotPath(txtShortcutPath, dialog)')

e('FoldersPref.loadEditDialog', 'FoldersPref.disableButtonIfTitleEmpty', 'CALL',
  'Edit dialog calls helper to validate title',
  evidence='SRC FoldersPref.java:172 disableButtonIfTitleEmpty(editText1, dialog)')

e('FoldersPref.loadEditDialog', 'FoldersPref.disableButtonIfNotPath', 'CALL',
  'Edit dialog calls helper to validate path',
  evidence='SRC FoldersPref.java:173 disableButtonIfNotPath(editText2, dialog)')

e('FoldersPref.disableButtonIfNotPath', 'FoldersPref$1.afterTextChanged', 'GUI',
  'Creates anonymous SimpleTextWatcher, framework calls afterTextChanged on text change',
  evidence='SRC FoldersPref.java:223-228 new SimpleTextWatcher() { @Override public void afterTextChanged(Editable s) {...} }')

e('FoldersPref.disableButtonIfTitleEmpty', 'FoldersPref$2.afterTextChanged', 'GUI',
  'Creates anonymous SimpleTextWatcher, framework calls afterTextChanged on text change',
  evidence='SRC FoldersPref.java:233-237 new SimpleTextWatcher() { @Override public void afterTextChanged(Editable s) {...} }')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B029 = {
    'FtpReceiver.<clinit>': ('framework_never_calls', 'Static initializer for TAG field, executed when class loads', 'SRC FtpReceiver.java:13 static final String TAG = FtpReceiver.class.getSimpleName()', 'SOURCE'),
    
    'FtpReceiver.<init>': ('framework_never_calls', 'Default constructor, called by Android framework when instantiating receiver', 'SRC FtpReceiver.java:11 public class FtpReceiver extends BroadcastReceiver - framework instantiates receivers', 'INFERRED'),
    
    'FoldersPref.<init>': ('framework_never_calls', 'Default constructor, called by Android framework when instantiating fragment', 'SRC FoldersPref.java:35 public class FoldersPref extends PreferenceFragment - framework instantiates fragments', 'INFERRED'),
    
    'FoldersPref.onResume': ('framework_never_calls', 'Lifecycle method called by framework, but only calls onCreate(null) which recreates all preferences', 'SRC FoldersPref.java:73-76 onResume() { super.onResume(); onCreate(null); }', 'SOURCE'),
    
    'FoldersPref$1.<init>': ('framework_never_calls', 'Constructor for anonymous inner class, never called directly', 'SRC FoldersPref.java:223 new SimpleTextWatcher() creates instance', 'SOURCE'),
    
    'FoldersPref$2.<init>': ('framework_never_calls', 'Constructor for anonymous inner class, never called directly', 'SRC FoldersPref.java:233 new SimpleTextWatcher() creates instance', 'SOURCE'),
    
    'FtpNotification.<init>': ('no_trigger_in_app', 'Private constructor, all methods are static', 'SRC FtpNotification.java:25 public class FtpNotification has only static methods (startNotification, updateNotification, buildNotification, removeNotification)', 'SOURCE'),
    
    'FtpNotification.removeNotification': ('no_trigger_in_app', 'Private method never called in the app', 'SRC FtpNotification.java:93-97 private static void removeNotification - grep shows no callers', 'SOURCE'),
}

# Lambda methods - need to check if they're callback references
# These will be marked as reachable through their dialog button click listeners
e('FoldersPref.loadCreateDialog', 'FoldersPref.lambda$loadCreateDialog$0', 'GUI',
  'Lambda registered as onClick listener for dialog positive button',
  evidence='SRC FoldersPref.java:119-137 dialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(view -> { ... })')

e('FoldersPref.loadEditDialog', 'FoldersPref.lambda$loadEditDialog$2', 'GUI',
  'Lambda registered as onClick listener for dialog positive button',
  evidence='SRC FoldersPref.java:175-196 dialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(view -> { ... })')

e('FoldersPref.loadDeleteDialog', 'FoldersPref.lambda$loadDeleteDialog$3', 'GUI',
  'Lambda registered as onClick listener for dialog positive button',
  evidence='SRC FoldersPref.java:212-222 dialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(view -> { ... })')

# lambda$null$1 is the inner lambda in loadEditDialog's onClick
e('FoldersPref.lambda$loadEditDialog$2', 'FoldersPref.lambda$null$1', 'ASYNC',
  'Inner lambda passed to AppConfig.runInBackground',
  evidence='SRC FoldersPref.java:192-194 AppConfig.runInBackground(() -> utilsHandler.renameBookmark(...))')
