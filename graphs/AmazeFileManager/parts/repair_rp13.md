STATUS: START 21:07

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| PermissionsActivity.isGranted | UNREACHABLE | no_trigger_in_app | Private helper method called only internally by PermissionsActivity.onRequestPermissionsResult at line 30 | SRC activities/superclasses/PermissionsActivity.java:97-99 |
| PermissionsActivity.lambda$requestInstallApkPermission$1 | REACHABLE | GUI | MaterialDialog negative button callback for APK install permission | SRC activities/superclasses/PermissionsActivity.java:65 |
| PermissionsActivity.lambda$requestPermission$2 | REACHABLE | GUI | MaterialDialog positive button callback for permission request | SRC activities/superclasses/PermissionsActivity.java:86-89 |
| PermissionsActivity.lambda$requestStoragePermission$0 | REACHABLE | GUI | MaterialDialog negative button callback for storage permission | SRC activities/superclasses/PermissionsActivity.java:56 |
| PermissionsActivity.onRequestPermissionsResult | REACHABLE | SYSTEM | Framework callback when permission result arrives | INFERRED Android framework + SRC activities/superclasses/PermissionsActivity.java:26-45 |
| GetSshHostFingerprintTask.<init> | REACHABLE | CALL | Instantiated from SftpConnectDialog.onCreateDialog | SRC ui/dialogs/SftpConnectDialog.java:178,203 |
| GetSshHostFingerprintTask.doInBackground | REACHABLE | ASYNC | AsyncTask worker thread execution | INFERRED AsyncTask + SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:76-102 |
| GetSshHostFingerprintTask.lambda$doInBackground$0 | REACHABLE | CALL | Lambda host key verifier callback invoked by SSH client | SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:85-89 |
| GetSshHostFingerprintTask.onPostExecute | REACHABLE | ASYNC | AsyncTask main thread callback after doInBackground | INFERRED AsyncTask + SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:108-122 |
| GetSshHostFingerprintTask.onPreExecute | REACHABLE | ASYNC | AsyncTask pre-execution on main thread | INFERRED AsyncTask + SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:104-106 |
| FileUtil.<init> | UNREACHABLE | no_trigger_in_app | Abstract class with only static utility methods; no instances created | SRC filesystem/FileUtil.java:78 |
| FileUtil.copyDummyFile | UNREACHABLE | no_trigger_in_app | Private static method called only internally by FileUtil.copyDummyFiles | SRC filesystem/FileUtil.java:888-927 |
| FileUtil.copyDummyFiles | UNREACHABLE | closed_by_api_level | Private helper for MediaFile workaround on API<29; standard config is API 27 but usage guarded and SAF preferred | SRC filesystem/FileUtil.java:971-976 |
| FileUtil.getTempFile | UNREACHABLE | no_trigger_in_app | Public method but no app code calls it | SRC filesystem/FileUtil.java:476-479; grep shows no callers |
| FileUtil.mkfile | REACHABLE | CALL | Already has edge in graph_def.py:3692 from Operations.mkFile | SRC graph_def.py:3692 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.<init> | REACHABLE | CALL | Created by Coders$DeflateDecoder.encode for 7z DEFLATE compression | SRC commons_compress_7z/.../Coders.java:155 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.close | REACHABLE | CALL | Called by SevenZOutputFile.finish to close compression stream | INFERRED OutputStream close + SRC Coders.java:217-225 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int) | REACHABLE | CALL | Called by compression pipeline for single byte writes | INFERRED OutputStream write + SRC Coders.java:204-206 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[]) | REACHABLE | CALL | Called by compression pipeline for byte array writes | INFERRED OutputStream write + SRC Coders.java:209-211 |
| Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int) | REACHABLE | CALL | Called by compression pipeline for byte range writes | INFERRED OutputStream write + SRC Coders.java:214-216 |
| SshClientUtils.<init> | UNREACHABLE | no_trigger_in_app | Abstract utility class with only static methods; no instances created | SRC filesystem/ssh/SshClientUtils.java:51 |
| SshClientUtils.deriveSftpPathFrom | REACHABLE | CALL | Called from SftpConnectDialog and SshConnectionPool to build SFTP URLs | SRC ui/dialogs/SftpConnectDialog.java:171,176,242,336; SRC filesystem/ssh/SshConnectionPool.java:150 |
| SshClientUtils.lambda$launchSftp$1 | REACHABLE | ASYNC | Lambda runnable executed on new thread to stream SFTP file | SRC filesystem/ssh/SshClientUtils.java:240 |
| SshClientUtils.lambda$null$0 | REACHABLE | CALL | Nested lambda to launch file viewer on UI thread | SRC filesystem/ssh/SshClientUtils.java:243 |
| SshClientUtils.launchSftp | REACHABLE | CALL | Called from MainFragment.onListItemClick to open SFTP files | SRC fragments/MainFragment.java:919 |
| ColorCircleDrawable.draw | REACHABLE | FRAMEWORK | Already has edge in graph_def.py:1511 from pseudo-node Drawable | SRC graph_def.py:1511 |
| ColorCircleDrawable.getOpacity | REACHABLE | FRAMEWORK | Already has edge in graph_def.py:1527 from pseudo-node Drawable | SRC graph_def.py:1527 |
| ColorCircleDrawable.onBoundsChange | REACHABLE | FRAMEWORK | Already has edge in graph_def.py:1515 from pseudo-node Drawable | SRC graph_def.py:1515 |
| ColorCircleDrawable.setAlpha | REACHABLE | FRAMEWORK | Already has edge in graph_def.py:1519 from pseudo-node Drawable | SRC graph_def.py:1519 |
| ColorCircleDrawable.setColorFilter | REACHABLE | FRAMEWORK | Already has edge in graph_def.py:1523 from pseudo-node Drawable | SRC graph_def.py:1523 |
| RenameBookmark.lambda$onCreateDialog$0 | REACHABLE | GUI | MaterialDialog neutral button callback to cancel rename | SRC ui/dialogs/RenameBookmark.java:81 |
| RenameBookmark.lambda$onCreateDialog$1 | REACHABLE | GUI | MaterialDialog positive button callback to save renamed bookmark | SRC ui/dialogs/RenameBookmark.java:85 |
| RenameBookmark.lambda$onCreateDialog$2 | REACHABLE | GUI | MaterialDialog negative button callback to delete bookmark | SRC ui/dialogs/RenameBookmark.java:120 |
| RenameBookmark.onCreate | REACHABLE | LIFECYCLE | DialogFragment lifecycle callback after instantiation | INFERRED androidx DialogFragment + SRC ui/dialogs/RenameBookmark.java:44-46 |
| RenameBookmark.onCreateDialog | REACHABLE | LIFECYCLE | DialogFragment lifecycle to build dialog after onCreate | INFERRED androidx DialogFragment + SRC ui/dialogs/RenameBookmark.java:49-128 |
| SmbSearchDialog.dismiss | REACHABLE | GUI | Called from cancel button and device selection callbacks | SRC ui/dialogs/SmbSearchDialog.java:67,156 |
| SmbSearchDialog.lambda$onCreateDialog$0 | REACHABLE | ASYNC | SubnetScanner callback when computer found on network | SRC ui/dialogs/SmbSearchDialog.java:77 |
| SmbSearchDialog.lambda$onCreateDialog$1 | REACHABLE | ASYNC | SubnetScanner callback when network scan completes | SRC ui/dialogs/SmbSearchDialog.java:86 |
| SmbSearchDialog.onCreate | REACHABLE | LIFECYCLE | DialogFragment lifecycle callback after instantiation | INFERRED androidx DialogFragment + SRC ui/dialogs/SmbSearchDialog.java:40-45 |
| SmbSearchDialog.onCreateDialog | REACHABLE | LIFECYCLE | DialogFragment lifecycle to build dialog after onCreate | INFERRED androidx DialogFragment + SRC ui/dialogs/SmbSearchDialog.java:53-99 |

STATUS: DONE 21:09
