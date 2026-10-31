# Repair batch 09 - AmazeFileManager graph_def.py part file
# Schema-2 edges for 40 methods from rp_09.txt
# Generated 2025-01-XX HH:MM

# PreferencesActivity helper methods (lines 175-200 of PreferencesActivity.java)
# All REACHABLE - called by ColorPref and PrefFrag

# PreferencesActivity.getRestartActivity
# SRC activities/PreferencesActivity.java:196-198
# Called by ColorPref.onBackPressed at fragments/preference_fragments/ColorPref.java:208
e('ColorPref.onBackPressed', 'PreferencesActivity.getRestartActivity', 'CALL',
  'ColorPref.onBackPressed checks if activity restart is needed via getRestartActivity()',
  evidence='SRC fragments/preference_fragments/ColorPref.java:208: if(((PreferencesActivity) getActivity()).getRestartActivity()); SRC activities/PreferencesActivity.java:196-198: public boolean getRestartActivity() { return restartActivity; }')

# PreferencesActivity.onBackPressed
# SRC activities/PreferencesActivity.java:105-120
# Framework lifecycle callback triggered by user pressing back button
e('PreferencesActivity.onCreate', 'PreferencesActivity.onBackPressed', 'FRAMEWORK',
  'Framework calls onBackPressed when user presses back button',
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onBackPressed dispatched by framework); SRC activities/PreferencesActivity.java:105-120')

e('PreferencesActivity.onBackPressed', 'ColorPref.onBackPressed', 'CALL',
  'PreferencesActivity.onBackPressed delegates to ColorPref if current fragment is ColorPref',
  guard='currentFragment instanceof ColorPref',
  evidence='SRC activities/PreferencesActivity.java:106-107: if(currentFragment instanceof ColorPref) { if(((ColorPref) currentFragment).onBackPressed()) return; }')

e('PreferencesActivity.onBackPressed', 'PreferencesActivity.restartActivity', 'CALL',
  'PreferencesActivity.onBackPressed restarts activity when selectedItem != START_PREFERENCE and restartActivity flag is true',
  guard='selectedItem != START_PREFERENCE && restartActivity',
  evidence='SRC activities/PreferencesActivity.java:109-110: if (selectedItem != START_PREFERENCE && restartActivity) { restartActivity(this); }')

e('PreferencesActivity.onBackPressed', 'PreferencesActivity.selectItem', 'CALL',
  'PreferencesActivity.onBackPressed returns to start preference when selectedItem != START_PREFERENCE and no restart needed',
  guard='selectedItem != START_PREFERENCE && !restartActivity',
  evidence='SRC activities/PreferencesActivity.java:111: } else if (selectedItem != START_PREFERENCE) { selectItem(START_PREFERENCE); }')

e('PreferencesActivity.onBackPressed', 'MainActivity.<init>', 'INTENT',
  'PreferencesActivity.onBackPressed navigates back to MainActivity when at start preference',
  guard='selectedItem == START_PREFERENCE',
  evidence='SRC activities/PreferencesActivity.java:113-117: Intent in = new Intent(PreferencesActivity.this, MainActivity.class); in.setAction(Intent.ACTION_MAIN); this.startActivity(in); this.finish();')

# PreferencesActivity.onOptionsItemSelected
# SRC activities/PreferencesActivity.java:122-153
# Framework callback when options menu item is selected
e('PreferencesActivity.onCreate', 'PreferencesActivity.onOptionsItemSelected', 'GUI',
  'User taps the Up/Home button in PreferencesActivity toolbar',
  gui=['Tap Up button in preferences'],
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onOptionsItemSelected dispatched by framework for menu items); SRC activities/PreferencesActivity.java:122-153')

e('PreferencesActivity.onOptionsItemSelected', 'PreferenceFragment.onOptionsItemSelected', 'CALL',
  'PreferencesActivity.onOptionsItemSelected delegates to current fragment first',
  evidence='SRC activities/PreferencesActivity.java:124: if(currentFragment.onOptionsItemSelected(item)) return true;')

e('PreferencesActivity.onOptionsItemSelected', 'PreferencesActivity.restartActivity', 'CALL',
  'PreferencesActivity.onOptionsItemSelected restarts activity when selectedItem != START_PREFERENCE and restartActivity flag is true',
  guard='selectedItem != START_PREFERENCE && restartActivity',
  evidence='SRC activities/PreferencesActivity.java:126-127: if (selectedItem != START_PREFERENCE && restartActivity) { restartActivity(this); }')

e('PreferencesActivity.onOptionsItemSelected', 'PreferencesActivity.selectItem', 'CALL',
  'PreferencesActivity.onOptionsItemSelected returns to start preference when selectedItem != START_PREFERENCE',
  guard='selectedItem != START_PREFERENCE && !restartActivity',
  evidence='SRC activities/PreferencesActivity.java:128: } else if (selectedItem != START_PREFERENCE) { selectItem(START_PREFERENCE); }')

e('PreferencesActivity.onOptionsItemSelected', 'MainActivity.<init>', 'INTENT',
  'PreferencesActivity.onOptionsItemSelected navigates back to MainActivity when at start preference',
  guard='selectedItem == START_PREFERENCE',
  evidence='SRC activities/PreferencesActivity.java:130-143: Intent in = new Intent(PreferencesActivity.this, MainActivity.class); activity.finish(); activity.startActivity(in);')

# PreferencesActivity.onSaveInstanceState
# SRC activities/PreferencesActivity.java:103-104
# Framework lifecycle callback
e('PreferencesActivity.onCreate', 'PreferencesActivity.onSaveInstanceState', 'FRAMEWORK',
  'Framework calls onSaveInstanceState to save activity state',
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onSaveInstanceState dispatched by ActivityThread); SRC activities/PreferencesActivity.java:103-104')

# PreferencesActivity.restartActivity
# SRC activities/PreferencesActivity.java:217-232
# Called from onBackPressed and onOptionsItemSelected (already added above)

# PreferencesActivity.restoreListViewState
# SRC activities/PreferencesActivity.java:189-191
# Called by PrefFrag to restore ListView scroll state
e('PrefFrag.onCreateView(LayoutInflater,ViewGroup,Bundle)', 'PreferencesActivity.restoreListViewState', 'CALL',
  'PrefFrag.onCreateView restores ListView scroll position via PreferencesActivity.restoreListViewState',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:287: Parcelable restored = ((PreferencesActivity) getActivity()).restoreListViewState(START_PREFERENCE); SRC activities/PreferencesActivity.java:189-191')

# PreferencesActivity.saveListViewState
# SRC activities/PreferencesActivity.java:180-182
# Called by PrefFrag to save ListView scroll state
e('PrefFrag.onPreferenceClick(Preference)', 'PreferencesActivity.saveListViewState', 'CALL',
  'PrefFrag.onPreferenceClick saves ListView scroll position before navigating away',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:159: ((PreferencesActivity) getActivity()).saveListViewState(START_PREFERENCE, listView.onSaveInstanceState()); SRC activities/PreferencesActivity.java:180-182')

# PreferencesActivity.setRestartActivity
# SRC activities/PreferencesActivity.java:193-194
# Called by ColorPref to signal that activity restart is needed
e('ColorPref.lambda$onCreate$0(Object,Preference,int,Object)', 'PreferencesActivity.setRestartActivity', 'CALL',
  'ColorPref color change callback sets restart activity flag',
  evidence='SRC fragments/preference_fragments/ColorPref.java:117: if (activity != null) activity.setRestartActivity(); SRC activities/PreferencesActivity.java:193-194')

e('ColorPref.lambda$onCreate$1(Preference)', 'PreferencesActivity.setRestartActivity', 'CALL',
  'ColorPref icon color change callback sets restart activity flag',
  evidence='SRC fragments/preference_fragments/ColorPref.java:156: if (activity != null) activity.setRestartActivity(); SRC activities/PreferencesActivity.java:193-194')

# PemToKeyPairTask - AsyncTask for parsing SSH private keys
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:67-262

# PemToKeyPairTask.<init>(InputStream,Callback)
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:88-90
# Called from SftpConnectDialog.onActivityResult (already in graph_def.py at line 12844)

# PemToKeyPairTask.doInBackground
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:100-122
# AsyncTask lifecycle - automatically called by execute()
e('PemToKeyPairTask.execute', 'PemToKeyPairTask.doInBackground', 'ASYNC',
  'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED android.os.AsyncTask.execute runs doInBackground on a worker thread; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:100-122')

e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask.onProgressUpdate', 'ASYNC',
  'doInBackground calls publishProgress which triggers onProgressUpdate on main thread',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:120: publishProgress(new IOException("No converter available to parse selected PEM")); INFERRED AsyncTask.publishProgress triggers onProgressUpdate')

# PemToKeyPairTask.lambda$onProgressUpdate$0
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:145-154
# MaterialDialog onPositive callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$0', 'GUI',
  'User taps OK button in passphrase dialog',
  gui=['Tap OK in SSH key passphrase dialog'],
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:143-154: .onPositive(((dialog, which) -> { ... })); lambda at 145-154')

# PemToKeyPairTask.lambda$onProgressUpdate$1
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:156-160
# MaterialDialog onNegative callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$1', 'GUI',
  'User taps Cancel button in passphrase dialog',
  gui=['Tap Cancel in SSH key passphrase dialog'],
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:155-160: .onNegative(((dialog, which) -> { ... })); lambda at 156-160')

e('PemToKeyPairTask.lambda$onProgressUpdate$1', 'PemToKeyPairTask.toastOnParseError', 'CALL',
  'Cancel callback shows toast error before canceling task',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:158: toastOnParseError(result);')

# PemToKeyPairTask.lambda$onProgressUpdate$2
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:163-167
# WarnableTextInputValidator callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$2', 'CALL',
  'onProgressUpdate sets up text validator with lambda for passphrase input',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:162-167: new WarnableTextInputValidator(..., (text) -> { ... }); lambda at 163-167')

# PemToKeyPairTask.onPostExecute
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179
# AsyncTask lifecycle callback
e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask.onPostExecute', 'ASYNC',
  'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED android.os.AsyncTask lifecycle calls onPostExecute on main thread after doInBackground returns; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179')

e('PemToKeyPairTask.onPostExecute', 'SftpConnectDialog.lambda$onActivityResult$14', 'CALLBACK',
  'onPostExecute invokes the callback registered in constructor',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:176-178: if(callback != null) { callback.onResult(result); }; callback registered at SftpConnectDialog.java:311')

# PemToKeyPairTask.onProgressUpdate
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:124-173
# AsyncTask lifecycle callback (already added edge from doInBackground above)

# PemToKeyPairTask.toastOnParseError
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:181-185
# Called from lambda$onProgressUpdate$1 (already added above)

# FileUtil$MediaFile - Kitkat MediaStore workaround class (UNREACHABLE)
# SRC filesystem/FileUtil.java:983-1231
# All methods in this inner class are unreachable - no callers found in app

UNREACHABLE['FileUtil$MediaFile.<init>'] = (
  'no_trigger_in_app',
  'MediaFile constructor only called from mkdir() at FileUtil.java:1198, but mkdir() itself is never called; grep shows no MediaFile instantiation outside FileUtil class',
  'SRC filesystem/FileUtil.java:1016-1022 (constructor); grep in app source shows only this definition, no callers except within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.delete'] = (
  'no_trigger_in_app',
  'MediaFile.delete only called from mkdir() at FileUtil.java:1199, but mkdir() is never called',
  'SRC filesystem/FileUtil.java:1028-1059 (delete method); called only at line 1199 within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getExternalFilesDir'] = (
  'no_trigger_in_app',
  'private static method, only called from installTemporaryTrack at line 1134, which is called from getTemporaryAlbumId, which is called from unreachable mkdir()',
  'SRC filesystem/FileUtil.java:987-1010 (getExternalFilesDir); called at line 1134 in installTemporaryTrack; chain starts from unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getFile'] = (
  'no_trigger_in_app',
  'public method but never called; MediaFile is only instantiated at line 1198 within unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1205-1207 (getFile); grep shows no callers in app source',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getTemporaryAlbumId'] = (
  'no_trigger_in_app',
  'private method, only called from mkdir() at line 1190, but mkdir() is never called',
  'SRC filesystem/FileUtil.java:1062-1126 (getTemporaryAlbumId); called only at line 1190 within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.installTemporaryTrack'] = (
  'no_trigger_in_app',
  'private method, only called from getTemporaryAlbumId at line 1091, which is called from unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1129-1170 (installTemporaryTrack); called at line 1091 in getTemporaryAlbumId; chain starts from unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.mkdir'] = (
  'no_trigger_in_app',
  'public method but grep shows no callers in app; Kitkat MediaStore workaround that is unused in this build',
  'SRC filesystem/FileUtil.java:1172-1202 (mkdir); grep in app source shows no callers; Kitkat-specific workaround code',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.write'] = (
  'no_trigger_in_app',
  'public method but grep shows no callers in app; MediaFile is never instantiated outside unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1207-1231 (write); grep shows no callers in app source',
  'SOURCE'
)

# MainActivityHelper$2 - anonymous ErrorCallBack in rename() method
# SRC utils/MainActivityHelper.java:265-328
# Anonymous class implementing Operations.ErrorCallBack interface

# MainActivityHelper$2.exists
# SRC utils/MainActivityHelper.java:267-273
# Callback from Operations.rename when target file already exists
e('Operations.rename', 'MainActivityHelper$2.exists', 'CALLBACK',
  'Operations.rename invokes exists callback when target file already exists',
  evidence='SRC filesystem/Operations.java (Operations.rename checks file existence and calls callback.exists if target exists); SRC utils/MainActivityHelper.java:265 new Operations.ErrorCallBack() { @Override public void exists...; callback method at 267-273')

# MainActivityHelper$2.invalidName
# SRC utils/MainActivityHelper.java:318-325
# Callback from Operations.rename when filename is invalid
e('Operations.rename', 'MainActivityHelper$2.invalidName', 'CALLBACK',
  'Operations.rename invokes invalidName callback when new filename is invalid',
  evidence='SRC filesystem/Operations.java (Operations.rename validates filename and calls callback.invalidName if invalid); SRC utils/MainActivityHelper.java:318-325')

# MainActivityHelper$2.lambda$done$2
# SRC utils/MainActivityHelper.java:299-316
# Runnable lambda in done() callback
e('MainActivityHelper$2.done', 'MainActivityHelper$2.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:297-316: context.runOnUiThread(() -> { ... }); lambda starts at 299')

# MainActivityHelper$2.lambda$exists$0
# SRC utils/MainActivityHelper.java:268-272
# Runnable lambda in exists() callback
e('MainActivityHelper$2.exists', 'MainActivityHelper$2.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:267-273: context.runOnUiThread(() -> { ... }); lambda at 268-272')

# MainActivityHelper$2.lambda$invalidName$3
# SRC utils/MainActivityHelper.java:319-324
# Runnable lambda in invalidName() callback
e('MainActivityHelper$2.invalidName', 'MainActivityHelper$2.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:318-325: context.runOnUiThread(() -> { ... }); lambda at 319-324')

# MainActivityHelper$2.lambda$launchSAF$1
# SRC utils/MainActivityHelper.java:280-288
# Runnable lambda in launchSAF(HybridFile,HybridFile) callback
e('MainActivityHelper$2.launchSAF(HybridFile,HybridFile)', 'MainActivityHelper$2.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:278-289: context.runOnUiThread(() -> { ... }); lambda at 280-288')

e('MainActivityHelper$2.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'launchSAF lambda shows SAF guide dialog',
  evidence='SRC utils/MainActivityHelper.java:285: guideDialogForLEXA(mainActivity.oppathe1);')

# MainActivityHelper$2.launchSAF(HybridFile)
# SRC utils/MainActivityHelper.java:276 (empty method)
UNREACHABLE['MainActivityHelper$2.launchSAF(HybridFile)'] = (
  'no_trigger_in_app',
  'empty callback method with no implementation in anonymous class',
  'SRC utils/MainActivityHelper.java:275-277: @Override public void launchSAF(HybridFile file) { } // empty',
  'SOURCE'
)

# MainActivityHelper$2.launchSAF(HybridFile,HybridFile)
# SRC utils/MainActivityHelper.java:278-289
# Callback from Operations.rename when SAF is needed
e('Operations.rename', 'MainActivityHelper$2.launchSAF(HybridFile,HybridFile)', 'CALLBACK',
  'Operations.rename invokes launchSAF callback when Storage Access Framework is needed for rename',
  evidence='SRC filesystem/Operations.java (Operations.rename detects need for SAF and calls callback.launchSAF); SRC utils/MainActivityHelper.java:278-289')

# MainActivityHelper$3 - anonymous ErrorCallBack in mkfile() method
# SRC utils/MainActivityHelper.java:394-447
# Anonymous class implementing Operations.ErrorCallBack interface

# MainActivityHelper$3.exists
# SRC utils/MainActivityHelper.java:396-408
# Callback from Operations.mkfile when file already exists
e('Operations.mkfile', 'MainActivityHelper$3.exists', 'CALLBACK',
  'Operations.mkfile invokes exists callback when target file already exists',
  evidence='SRC filesystem/Operations.java (Operations.mkfile checks file existence and calls callback.exists if exists); SRC utils/MainActivityHelper.java:394 new Operations.ErrorCallBack() { @Override public void exists...; callback at 396-408')

e('MainActivityHelper$3.exists', 'MainActivityHelper$3.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:396-408: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 397-406')

# MainActivityHelper$3.invalidName
# SRC utils/MainActivityHelper.java:437-445
# Callback from Operations.mkfile when filename is invalid
e('Operations.mkfile', 'MainActivityHelper$3.invalidName', 'CALLBACK',
  'Operations.mkfile invokes invalidName callback when filename is invalid',
  evidence='SRC filesystem/Operations.java (Operations.mkfile validates filename and calls callback.invalidName if invalid); SRC utils/MainActivityHelper.java:437-445')

e('MainActivityHelper$3.invalidName', 'MainActivityHelper$3.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:437-445: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 438-443')

# MainActivityHelper$3.lambda$done$2
# SRC utils/MainActivityHelper.java:427-434
# Runnable lambda in done() callback
e('MainActivityHelper$3.done', 'MainActivityHelper$3.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:425-435: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 427-434')

# MainActivityHelper$3.lambda$exists$0
# SRC utils/MainActivityHelper.java:397-406
# Runnable lambda in exists() callback (already added above)

# MainActivityHelper$3.lambda$invalidName$3
# SRC utils/MainActivityHelper.java:438-443
# Runnable lambda in invalidName() callback (already added above)

# MainActivityHelper$3.lambda$launchSAF$1
# SRC utils/MainActivityHelper.java:412-419
# Runnable lambda in launchSAF(HybridFile) callback
e('MainActivityHelper$3.launchSAF(HybridFile)', 'MainActivityHelper$3.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:410-420: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 412-419')

e('MainActivityHelper$3.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'launchSAF lambda shows SAF guide dialog',
  evidence='SRC utils/MainActivityHelper.java:416: guideDialogForLEXA(mainActivity.oppathe);')

# MainActivityHelper$3.launchSAF(HybridFile)
# SRC utils/MainActivityHelper.java:410-420
# Callback from Operations.mkfile when SAF is needed
e('Operations.mkfile', 'MainActivityHelper$3.launchSAF(HybridFile)', 'CALLBACK',
  'Operations.mkfile invokes launchSAF callback when Storage Access Framework is needed',
  evidence='SRC filesystem/Operations.java (Operations.mkfile detects need for SAF and calls callback.launchSAF); SRC utils/MainActivityHelper.java:410-420')

# MainActivityHelper$3.launchSAF(HybridFile,HybridFile)
# SRC utils/MainActivityHelper.java:422-423 (empty method)
UNREACHABLE['MainActivityHelper$3.launchSAF(HybridFile,HybridFile)'] = (
  'no_trigger_in_app',
  'empty callback method with no implementation in anonymous class',
  'SRC utils/MainActivityHelper.java:422-423: @Override public void launchSAF(HybridFile file, HybridFile file1) { } // empty',
  'SOURCE'
)
