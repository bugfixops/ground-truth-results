# Repair Batch 09 - AmazeFileManager Methods

STATUS: START 20:50
STATUS: DONE 20:52

## Summary
- Total methods: 40
- REACHABLE: 29
- UNREACHABLE: 11
- INCOMPLETE: 0

## Method Classification

### REACHABLE (29 methods)

| Method | Evidence Lines |
|--------|----------------|
| PreferencesActivity.getRestartActivity | Called by ColorPref.onBackPressed; SRC activities/PreferencesActivity.java:196-198, fragments/preference_fragments/ColorPref.java:208 |
| PreferencesActivity.onBackPressed | Framework lifecycle callback; SRC activities/PreferencesActivity.java:105-120 |
| PreferencesActivity.onOptionsItemSelected | Framework menu callback; SRC activities/PreferencesActivity.java:122-153 |
| PreferencesActivity.onSaveInstanceState | Framework lifecycle callback; SRC activities/PreferencesActivity.java:103-104 |
| PreferencesActivity.restartActivity | Called from onBackPressed and onOptionsItemSelected; SRC activities/PreferencesActivity.java:217-232 |
| PreferencesActivity.restoreListViewState | Called by PrefFrag.onCreateView; SRC activities/PreferencesActivity.java:189-191, fragments/preference_fragments/PrefFrag.java:287 |
| PreferencesActivity.saveListViewState | Called by PrefFrag.onPreferenceClick; SRC activities/PreferencesActivity.java:180-182, fragments/preference_fragments/PrefFrag.java:159 |
| PreferencesActivity.setRestartActivity | Called by ColorPref lambdas; SRC activities/PreferencesActivity.java:193-194, fragments/preference_fragments/ColorPref.java:117,156 |
| PemToKeyPairTask.<init>(InputStream,Callback) | Called from SftpConnectDialog.onActivityResult; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:88-90, ui/dialogs/SftpConnectDialog.java:311 |
| PemToKeyPairTask.doInBackground | AsyncTask lifecycle; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:100-122 |
| PemToKeyPairTask.lambda$onProgressUpdate$0 | MaterialDialog onPositive callback; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:145-154 |
| PemToKeyPairTask.lambda$onProgressUpdate$1 | MaterialDialog onNegative callback; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:156-160 |
| PemToKeyPairTask.lambda$onProgressUpdate$2 | WarnableTextInputValidator callback; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:163-167 |
| PemToKeyPairTask.onPostExecute | AsyncTask lifecycle; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179 |
| PemToKeyPairTask.onProgressUpdate | AsyncTask lifecycle; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:124-173 |
| PemToKeyPairTask.toastOnParseError | Called from lambda$onProgressUpdate$1; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:181-185 |
| MainActivityHelper$2.exists | Operations.rename callback; SRC utils/MainActivityHelper.java:267-273 |
| MainActivityHelper$2.invalidName | Operations.rename callback; SRC utils/MainActivityHelper.java:318-325 |
| MainActivityHelper$2.lambda$done$2 | Runnable lambda in done callback; SRC utils/MainActivityHelper.java:299-316 |
| MainActivityHelper$2.lambda$exists$0 | Runnable lambda in exists callback; SRC utils/MainActivityHelper.java:268-272 |
| MainActivityHelper$2.lambda$invalidName$3 | Runnable lambda in invalidName callback; SRC utils/MainActivityHelper.java:319-324 |
| MainActivityHelper$2.lambda$launchSAF$1 | Runnable lambda in launchSAF callback; SRC utils/MainActivityHelper.java:280-288 |
| MainActivityHelper$2.launchSAF(HybridFile,HybridFile) | Operations.rename callback; SRC utils/MainActivityHelper.java:278-289 |
| MainActivityHelper$3.exists | Operations.mkfile callback; SRC utils/MainActivityHelper.java:396-408 |
| MainActivityHelper$3.invalidName | Operations.mkfile callback; SRC utils/MainActivityHelper.java:437-445 |
| MainActivityHelper$3.lambda$done$2 | Runnable lambda in done callback; SRC utils/MainActivityHelper.java:427-434 |
| MainActivityHelper$3.lambda$exists$0 | Runnable lambda in exists callback; SRC utils/MainActivityHelper.java:397-406 |
| MainActivityHelper$3.lambda$invalidName$3 | Runnable lambda in invalidName callback; SRC utils/MainActivityHelper.java:438-443 |
| MainActivityHelper$3.lambda$launchSAF$1 | Runnable lambda in launchSAF callback; SRC utils/MainActivityHelper.java:412-419 |
| MainActivityHelper$3.launchSAF(HybridFile) | Operations.mkfile callback; SRC utils/MainActivityHelper.java:410-420 |

### UNREACHABLE (11 methods)

| Method | Reason | Evidence Lines |
|--------|--------|----------------|
| FileUtil$MediaFile.<init> | no_trigger_in_app: Only called from mkdir() which is never called | SRC filesystem/FileUtil.java:1016-1022; grep shows no callers except within unreachable mkdir() |
| FileUtil$MediaFile.delete | no_trigger_in_app: Only called from mkdir() which is never called | SRC filesystem/FileUtil.java:1028-1059; called only at line 1199 within unreachable mkdir() |
| FileUtil$MediaFile.getExternalFilesDir | no_trigger_in_app: Only called from installTemporaryTrack chain starting from unreachable mkdir() | SRC filesystem/FileUtil.java:987-1010; called at line 1134 in installTemporaryTrack |
| FileUtil$MediaFile.getFile | no_trigger_in_app: Never called; MediaFile only instantiated in unreachable mkdir() | SRC filesystem/FileUtil.java:1205-1207; grep shows no callers in app |
| FileUtil$MediaFile.getTemporaryAlbumId | no_trigger_in_app: Only called from mkdir() which is never called | SRC filesystem/FileUtil.java:1062-1126; called only at line 1190 within unreachable mkdir() |
| FileUtil$MediaFile.installTemporaryTrack | no_trigger_in_app: Only called from getTemporaryAlbumId which is called from unreachable mkdir() | SRC filesystem/FileUtil.java:1129-1170; called at line 1091 in getTemporaryAlbumId |
| FileUtil$MediaFile.mkdir | no_trigger_in_app: Kitkat MediaStore workaround that is unused | SRC filesystem/FileUtil.java:1172-1202; grep shows no callers; Kitkat-specific code |
| FileUtil$MediaFile.write | no_trigger_in_app: Never called; MediaFile never instantiated outside unreachable mkdir() | SRC filesystem/FileUtil.java:1207-1231; grep shows no callers in app |
| MainActivityHelper$2.launchSAF(HybridFile) | no_trigger_in_app: Empty callback method with no implementation | SRC utils/MainActivityHelper.java:275-277; empty method body |
| MainActivityHelper$3.launchSAF(HybridFile,HybridFile) | no_trigger_in_app: Empty callback method with no implementation | SRC utils/MainActivityHelper.java:422-423; empty method body |

### INCOMPLETE (0 methods)

None.

## Notes

### PreferencesActivity Helper Methods
All 8 helper methods (getRestartActivity, setRestartActivity, saveListViewState, restoreListViewState, onBackPressed, onOptionsItemSelected, onSaveInstanceState, restartActivity) are REACHABLE and actively used by ColorPref and PrefFrag to manage preference navigation and state preservation.

### PemToKeyPairTask
All 6 methods of PemToKeyPairTask are REACHABLE. This AsyncTask parses SSH private keys (OpenSSH, PuTTY formats) and is triggered from SftpConnectDialog when the user selects a private key file for SSH/SFTP authentication.

### FileUtil$MediaFile
All 8 methods in the MediaFile inner class are UNREACHABLE. This class implements a Kitkat-era MediaStore workaround for external SD card access, but the mkdir() entry point is never called in the app. The app uses SAF (Storage Access Framework) instead for external storage operations.

### MainActivityHelper Anonymous Classes
MainActivityHelper$2 (rename callback) has 7 methods: 6 REACHABLE, 1 UNREACHABLE (empty launchSAF overload).
MainActivityHelper$3 (mkfile callback) has 7 methods: 6 REACHABLE, 1 UNREACHABLE (empty launchSAF overload).

Both anonymous classes implement Operations.ErrorCallBack interface to handle file operation results and errors asynchronously.
