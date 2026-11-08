STATUS: START 22:44
STATUS: DONE 22:48

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| SmbConnectDialog$3.afterTextChanged | REACHABLE | - | Already has routes in graph_def.py | - |
| SmbConnectDialog$4.afterTextChanged | REACHABLE | - | Already has routes in graph_def.py | - |
| SmbSearchDialog$1.computerFound | REACHABLE | - | Already has routes in graph_def.py | - |
| SmbSearchDialog$1.lambda$computerFound$0 | REACHABLE | - | Already has routes in graph_def.py | - |
| SmbSearchDialog$1.lambda$searchFinished$1 | REACHABLE | - | Already has routes in graph_def.py | - |
| SmbSearchDialog$1.searchFinished | REACHABLE | - | Already has routes in graph_def.py | - |
| SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair) | REACHABLE | CALL | 7-parameter constructor delegates to Object.<init> and field assignments | SRC SshAuthenticationTask.java:95-105 |
| SshAuthenticationTask.doInBackground | REACHABLE | - | Already has routes in graph_def.py | - |
| SshAuthenticationTask.lambda$onPostExecute$0 | REACHABLE | CALL | Lambda callback for AlertDialog dismiss button | SRC SshAuthenticationTask.java:180 |
| SshAuthenticationTask.onPostExecute | REACHABLE | FRAMEWORK | Called by AsyncTask framework after doInBackground; shows error toasts and dialogs | SRC SshAuthenticationTask.java:161-184 |
| SshAuthenticationTask$1.<init> | REACHABLE | CALL | Anonymous KeyProvider implementation created in doInBackground for key-based auth | SRC SshAuthenticationTask.java:130-144 |
| SshAuthenticationTask$1.getPrivate | REACHABLE | FRAMEWORK | Called by SSHJ library during key-based authentication | SRC SshAuthenticationTask.java:132-134 |
| SshAuthenticationTask$1.getPublic | REACHABLE | FRAMEWORK | Called by SSHJ library during key-based authentication | SRC SshAuthenticationTask.java:136-138 |
| SshAuthenticationTask$1.getType | REACHABLE | FRAMEWORK | Called by SSHJ library to determine key type | SRC SshAuthenticationTask.java:140-142 |
| SshClientUtils.deriveSftpPathFrom | REACHABLE | - | Already has routes in graph_def.py | - |
| SshConnectionPool.getConnection(String,int,String,String,String,KeyPair) | REACHABLE | - | Already has routes in graph_def.py | - |
| SshConnectionPool.lambda$create$1 | REACHABLE | CALL | Lambda callback for PemToKeyPairTask; stores result and signals latch | SRC SshConnectionPool.java:214-217 |
| SshConnectionPool.lambda$expungeAllConnections$0 | REACHABLE | CALL | Lambda run in background to disconnect all SSH connections | SRC SshConnectionPool.java:181-187 |
| SshConnectionPool.removeConnection | REACHABLE | - | Already has routes in graph_def.py | - |
| SshConnectionPool$AsyncRemoveConnection.<init> | REACHABLE | - | Already has routes in graph_def.py | - |
| SshConnectionPool$AsyncRemoveConnection.doInBackground | REACHABLE | - | Already has routes in graph_def.py | - |
| SshConnectionPool$AsyncRemoveConnection.onPostExecute | REACHABLE | - | Already has routes in graph_def.py | - |
| Statvfs$Response.getRawFileSystemId | REACHABLE | - | Already has routes in graph_def.py | - |
| StreamServer.lambda$new$0 | REACHABLE | - | Already has routes in graph_def.py | - |
| StreamSource.getFile | UNREACHABLE | no_trigger_in_app | Getter method never called; StreamSource only used internally by StreamServer for streaming | SRC StreamSource.java:115-117; grep shows no callers |
| StreamSource.getName | UNREACHABLE | no_trigger_in_app | Getter method never called; HTTP streaming uses read() methods not getName | SRC StreamSource.java:111-113; grep shows no callers |
| StreamSource.read() | REACHABLE | FRAMEWORK | Called by parent RandomAccessStream for single-byte reads during HTTP streaming | SRC StreamSource.java:76-80 |
| StreamSource.read(byte[],int,int) | REACHABLE | FRAMEWORK | Called by parent RandomAccessStream for multi-byte reads during HTTP streaming | SRC StreamSource.java:82-86 |
| SubnetScanner.getResults | UNREACHABLE | no_trigger_in_app | Method returns discovered computers list but never called; SmbSearchDialog uses observer callbacks instead | SRC SubnetScanner.java:187-189; grep shows no callers |
| SubnetScanner.onFound | REACHABLE | CALL | Private method called by run() to notify observer when computer discovered | SRC SubnetScanner.java:175-181 |
| SubnetScanner.run | REACHABLE | - | Already has routes in graph_def.py | - |
| SubnetScanner.tryWithBroadcast | REACHABLE | - | Already has routes in graph_def.py | - |
| TabFragment.onPageSelected | REACHABLE | - | Already has routes in graph_def.py | - |
| TabFragment$ScreenSlidePagerAdapter.getCount | REACHABLE | - | Already has routes in graph_def.py | - |
| TabFragment$ScreenSlidePagerAdapter.getItem | REACHABLE | - | Already has routes in graph_def.py | - |
| TabFragment$ScreenSlidePagerAdapter.getItemPosition | REACHABLE | - | Already has routes in graph_def.py | - |
| ThemedImageButton.<init>(Context) | REACHABLE | FRAMEWORK | Constructor called by Android framework when inflating from XML | SRC ThemedImageButton.java:16-18 |
| ThemedImageButton.<init>(Context,AttributeSet) | REACHABLE | FRAMEWORK | Constructor called by Android framework when inflating from XML with attributes | SRC ThemedImageButton.java:20-22 |
| ThemedImageButton.getAccessibilityClassName | REACHABLE | - | Already has routes in graph_def.py | - |
| ThemedImageButton.onSetAlpha | REACHABLE | - | Already has routes in graph_def.py | - |

## Summary
- Total methods: 40
- REACHABLE: 37 (23 already routed, 14 new routes added)
- UNREACHABLE: 3 (StreamSource.getFile, StreamSource.getName, SubnetScanner.getResults)
- INCOMPLETE: 0

## Notes
- 23 methods already had complete routes in graph_def.py and required no additional work
- 14 methods needed new edge entries added to repair_rp34.py
- 3 methods are unreachable: getter methods that are never called from app code
- All SSH authentication task methods are reachable through the SSH connection setup flow
- StreamSource read methods are reachable through HTTP streaming parent class framework calls
- ThemedImageButton constructors are reachable through Android XML inflation framework
