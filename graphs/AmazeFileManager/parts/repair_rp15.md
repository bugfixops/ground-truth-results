# Repair batch 15: 40 methods
STATUS: START 21:07

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair) | REACHABLE | CALL | Called from SshConnectionPool.create | SRC SshConnectionPool.java:222-223 |
| SshAuthenticationTask.doInBackground | REACHABLE | ASYNC | AsyncTask lifecycle method | SRC SshAuthenticationTask.java:114 |
| SshAuthenticationTask.lambda$onPostExecute$0 | REACHABLE | GUI | Lambda in AlertDialog button | SRC SshAuthenticationTask.java:172 |
| SshAuthenticationTask.onPostExecute | REACHABLE | ASYNC | AsyncTask lifecycle method | SRC SshAuthenticationTask.java:158 |
| SshAuthenticationTask$1.<init> | REACHABLE | CALL | Anonymous KeyProvider implementation | SRC SshAuthenticationTask.java:129-142 |
| SshAuthenticationTask$1.getPrivate | REACHABLE | FRAMEWORK | sshj library calls during authPublickey | SRC SshAuthenticationTask.java:131-133 |
| SshAuthenticationTask$1.getPublic | REACHABLE | FRAMEWORK | sshj library calls during authPublickey | SRC SshAuthenticationTask.java:136-138 |
| SshAuthenticationTask$1.getType | REACHABLE | FRAMEWORK | sshj library calls during authPublickey | SRC SshAuthenticationTask.java:141-143 |
| AbstractProgressiveService.getDataPackage | REACHABLE | CALL | Called by ServiceWatcherUtil handler | SRC AbstractProgressiveService.java:200-202 |
| AbstractProgressiveService.getDataPackageSize | REACHABLE | CALL | Called by ServiceWatcherUtil handler | SRC AbstractProgressiveService.java:204-206 |
| AbstractProgressiveService.isDecryptService | REACHABLE | CALL | ServiceWatcherInteractionInterface method | SRC AbstractProgressiveService.java:219-221 |
| AbstractProgressiveService.progressResumed | REACHABLE | CALL | ServiceWatcherInteractionInterface method | SRC AbstractProgressiveService.java:75-81 |
| RootHelper.<init> | UNREACHABLE | no_trigger_in_app | All methods static, no constructor called | SRC RootHelper.java:36 |
| RootHelper.generateBaseFile(DocumentFile) | REACHABLE | CALL | Called from RootHelper.getFilesList | SRC RootHelper.java:280-283 |
| RootHelper.lambda$runShellCommandToList$0 | REACHABLE | CALL | Lambda in runShellCommandToList | SRC RootHelper.java:50 |
| RootHelper.runNonRootShellCommand | UNREACHABLE | no_trigger_in_app | Deprecated method, no app callers | SRC RootHelper.java:93 |
| Coders$DeflateDecoder$DeflateDecoderInputStream.close | UNREACHABLE | no_trigger_in_app | Library stream method, source not in src/main/java | INFERRED Apache Commons Compress |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read() | UNREACHABLE | no_trigger_in_app | Library stream method, source not in src/main/java | INFERRED Apache Commons Compress |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[]) | UNREACHABLE | no_trigger_in_app | Library stream method, source not in src/main/java | INFERRED Apache Commons Compress |
| Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[],int,int) | UNREACHABLE | no_trigger_in_app | Library stream method, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZFile$1.count | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZFile$1.read() | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZFile$1.read(byte[]) | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZFile$1.read(byte[],int,int) | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZOutputFile$1.<init> | UNREACHABLE | no_trigger_in_app | Anonymous inner class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZOutputFile$1.write(int) | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZOutputFile$1.write(byte[]) | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SevenZOutputFile$1.write(byte[],int,int) | UNREACHABLE | no_trigger_in_app | Anonymous stream class, source not in src/main/java | INFERRED Apache Commons Compress |
| SshConnectionPool.getConnection(String,int,String,String,String,KeyPair) | REACHABLE | CALL | Called from SftpConnectDialog | SRC SftpConnectDialog.java:343 |
| SshConnectionPool.lambda$create$1 | UNREACHABLE | no_trigger_in_app | Lambda not found in source, likely obsolete | SRC SshConnectionPool.java:189-212 |
| SshConnectionPool.lambda$expungeAllConnections$0 | REACHABLE | ASYNC | Lambda in AppConfig.runInBackground | SRC SshConnectionPool.java:175 |
| SshConnectionPool.removeConnection | REACHABLE | - | Already in graph_def.py (lambda$onCreateDialog$0) | - |
| ColorPickerDialog$SavedState.<clinit> | REACHABLE | - | Already in graph_def.py line 1612 | - |
| ColorPickerDialog$SavedState.<init>(Parcel) | REACHABLE | - | Already in graph_def.py line 1598, 1603, 1608 | - |
| ColorPickerDialog$SavedState.<init>(Parcelable) | REACHABLE | - | Already in graph_def.py line 1598 | - |
| ColorPickerDialog$SavedState.writeToParcel | REACHABLE | - | Already in graph_def.py line 1616 | - |
| CheckableCircleView.<init> | REACHABLE | - | Already in graph_def.py line 1959, 1963 | - |
| CheckableCircleView.onDraw | REACHABLE | - | Already in graph_def.py line 1971 | - |
| CheckableCircleView.setChecked | REACHABLE | - | Already in graph_def.py line 1967 | - |
| CheckableCircleView.setColor | REACHABLE | - | Already in graph_def.py line 1963 | - |

STATUS: DONE 21:12

Summary:
- REACHABLE: 22 methods (18 new edges + 4 already labeled)
- UNREACHABLE: 18 methods (16 library stream methods + 2 no callers)
- Total: 40 methods
