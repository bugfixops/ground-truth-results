STATUS: START 22:11

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| PemToKeyPairTask.<init>(InputStream,Callback) | REACHABLE | - | Constructor called from SftpConnectDialog when user selects PEM key file for SSH connection | SRC PemToKeyPairTask.java:95-97; caller: SftpConnectDialog via grep |
| PemToKeyPairTask.doInBackground | REACHABLE | - | AsyncTask framework calls doInBackground on worker thread after execute() | SRC PemToKeyPairTask.java:108-131; AsyncTask lifecycle |
| PemToKeyPairTask.lambda$onProgressUpdate$0 | REACHABLE | - | Lambda registered as MaterialDialog positive button listener in onProgressUpdate | SRC PemToKeyPairTask.java:147-157 |
| PemToKeyPairTask.lambda$onProgressUpdate$1 | REACHABLE | - | Lambda registered as MaterialDialog negative button listener in onProgressUpdate | SRC PemToKeyPairTask.java:159-163 |
| PemToKeyPairTask.lambda$onProgressUpdate$2 | REACHABLE | - | Lambda registered as WarnableTextInputValidator callback in onProgressUpdate | SRC PemToKeyPairTask.java:167-172 |
| PemToKeyPairTask.onPostExecute | REACHABLE | - | AsyncTask framework calls onPostExecute on UI thread with result | SRC PemToKeyPairTask.java:177-181; AsyncTask lifecycle |
| PemToKeyPairTask.onProgressUpdate | REACHABLE | - | AsyncTask framework calls onProgressUpdate on UI thread after publishProgress | SRC PemToKeyPairTask.java:133-175; AsyncTask lifecycle |
| PemToKeyPairTask.toastOnParseError | REACHABLE | - | Called from lambda$onProgressUpdate$1 to show PEM parse error toast | SRC PemToKeyPairTask.java:183-186; caller: line 161 |
| PemToKeyPairTask$1.<init> | REACHABLE | - | Anonymous PasswordFinder created by lambda$onProgressUpdate$0 | SRC PemToKeyPairTask.java:148-156 |
| PemToKeyPairTask$1.reqPassword | REACHABLE | - | Called by sshj library converters (OpenSSHKeyFile, OpenSSHKeyV1KeyFile, PuTTYKeyFile) when password-protected key needs decryption | SRC PemToKeyPairTask.java:150-152; sshj library callbacks |
| PemToKeyPairTask$1.shouldRetry | REACHABLE | - | Called by sshj library converters after password attempt to check retry policy | SRC PemToKeyPairTask.java:154-156; sshj library callbacks |
| PrefFrag.lambda$onCreate$0 | REACHABLE | - | Lambda registered as OnPreferenceChangeListener for fingerprint checkbox | SRC PrefFrag.java:94-111 |
| PrefFrag.lambda$onPreferenceClick$1 | REACHABLE | - | Lambda for grid columns dialog single choice callback | SRC PrefFrag.java:135-140 |
| PrefFrag.lambda$onPreferenceClick$2 | REACHABLE | - | Lambda for theme selection dialog callback | SRC PrefFrag.java:147-152 |
| PrefFrag.lambda$onPreferenceClick$3 | REACHABLE | - | Lambda for master password input callback | SRC PrefFrag.java:227 |
| PrefFrag.lambda$onPreferenceClick$4 | REACHABLE | - | Lambda for master password dialog positive button | SRC PrefFrag.java:233-248 |
| PrefFrag.lambda$onPreferenceClick$5 | REACHABLE | - | Lambda for master password dialog negative button | SRC PrefFrag.java:250 |
| PrefFrag.onCreate | REACHABLE | - | Android framework calls onCreate when fragment is created | SRC PrefFrag.java:69-121; Fragment lifecycle |
| PrefFrag.onCreateView | REACHABLE | - | Android framework calls onCreateView to inflate fragment layout | SRC PrefFrag.java:268-274; Fragment lifecycle |
| PrefFrag.onPreferenceClick | REACHABLE | - | Android framework calls when user taps a preference item | SRC PrefFrag.java:125-266; OnPreferenceClickListener |
| PrefFrag.restartPC | REACHABLE | - | Static utility to restart activity with fade animation | SRC PrefFrag.java:255-264; called from lambdas |
| PrepareCopyTask.doNotReplaceFiles | REACHABLE | - | Removes conflicting files from copy list and continues dialog flow | SRC PrepareCopyTask.java:248-261; called from onEndDialog and lambda |
| PrepareCopyTask.lambda$checkConflicts$0 | REACHABLE | - | Lambda callback for HybridFile.forEachChildrenFile iteration | SRC PrepareCopyTask.java:121-127 |
| PrepareCopyTask.lambda$showDialog$1 | REACHABLE | - | Lambda for conflict dialog positive (skip) button | SRC PrepareCopyTask.java:198-202 |
| PrepareCopyTask.lambda$showDialog$2 | REACHABLE | - | Lambda for conflict dialog negative (overwrite) button | SRC PrepareCopyTask.java:203-207 |
| PrepareCopyTask.onEndDialog | REACHABLE | - | State machine that handles conflict resolution dialog flow | SRC PrepareCopyTask.java:223-246; called from onPostExecute and recursively |
| PrepareCopyTask.onPostExecute | REACHABLE | - | AsyncTask framework calls on UI thread after doInBackground completes | SRC PrepareCopyTask.java:131-150; AsyncTask lifecycle |
| PrepareCopyTask.onPreExecute | REACHABLE | - | AsyncTask framework calls before doInBackground starts | SRC PrepareCopyTask.java:74-77; AsyncTask lifecycle |
| PrepareCopyTask.replaceFiles | REACHABLE | - | Advances counter to skip conflict checking and continues dialog flow | SRC PrepareCopyTask.java:263-274; called from onEndDialog and lambda |
| PrepareCopyTask.showDialog | REACHABLE | - | Shows MaterialDialog for file conflict resolution | SRC PrepareCopyTask.java:163-221; called from onEndDialog |
| PrepareCopyTask$CopyNode.getConflictingFiles | REACHABLE | - | Getter for conflictingFiles list | SRC PrepareCopyTask.java:364-366; called from onEndDialog |
| PrepareCopyTask$CopyNode.getFilesToCopy | REACHABLE | - | Getter for filesToCopy list | SRC PrepareCopyTask.java:360-362; called from onEndDialog |
| PrepareCopyTask$CopyNode.getPath | REACHABLE | - | Getter for path string | SRC PrepareCopyTask.java:356-358; called from onEndDialog |
| PrepareCopyTask$CopyNode.getUnvisitedChildNode | REACHABLE | - | Returns first child node not in visited set for BFS traversal | SRC PrepareCopyTask.java:368-376; called from goToNextNode |
| PrepareCopyTask$CopyNode.goToNextNode | REACHABLE | - | BFS traversal to get next node in copy tree | SRC PrepareCopyTask.java:337-350; called from onEndDialog |
| PrepareCopyTask$CopyNode.hasStarted | REACHABLE | - | Returns true if BFS traversal has been initialized | SRC PrepareCopyTask.java:352-354; called from onEndDialog |
| PrepareCopyTask$CopyNode.startCopy | REACHABLE | - | Initializes BFS queue and visited set for copy traversal | SRC PrepareCopyTask.java:326-331; called from onEndDialog |
| ProcessViewerFragment$CustomServiceConnection.onServiceConnected | REACHABLE | - | Android framework calls when service binding succeeds | SRC ProcessViewerFragment.java:315-333; ServiceConnection callback |
| ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected | REACHABLE | - | Android framework calls when service connection drops | SRC ProcessViewerFragment.java:339-340; ServiceConnection callback |
| ProcessViewerFragment$CustomServiceConnection$1.<init> | REACHABLE | - | Anonymous ProgressListener created in onServiceConnected | SRC ProcessViewerFragment.java:326-337 |

STATUS: DONE 22:15

