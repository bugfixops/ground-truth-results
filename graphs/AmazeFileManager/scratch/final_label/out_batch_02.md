STATUS: RUNNING 23:34

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| DummyFileGenerator.createFile | UNREACHABLE | no_trigger_in_app | Test-only utility method annotated @RestrictTo(RestrictTo.Scope.TESTS) and @VisibleForTesting(otherwise = VisibleForTesting.NONE); grep -rn over src/main/java finds no calls in the app | utils/test/DummyFileGenerator.java:54-59 |
| EditTextColorStateUtil.<init> | UNREACHABLE | no_trigger_in_app | Utility class with only static methods; no instantiation found in app (grep -rn "new EditTextColorStateUtil" finds nothing) | utils/EditTextColorStateUtil.java:18-45 |
| EncryptService$1.onReceive | REACHABLE | FRAMEWORK | Framework dispatches broadcast when user taps notification action or ProcessViewerFragment sends TAG_BROADCAST_CRYPT_CANCEL | asynchronous/services/EncryptService.java:68,92,226-230 |
| FastScroller.<init>(Context,AttributeSet) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| Indicator.<init>(Context) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| Indicator.<init>(Context,AttributeSet) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| MainFragment$2.getSpanSize | REACHABLE | FRAMEWORK | GridLayoutManager calls getSpanSize to determine span for each position | fragments/MainFragment.java:341-349 |
| MainFragment$3.onActionItemClicked | REACHABLE | FRAMEWORK | Framework dispatches onActionItemClicked when user selects action mode menu item | fragments/MainFragment.java:461,623; adapters/RecyclerAdapter.java:192 |
| MainFragment$3.onCreateActionMode | REACHABLE | FRAMEWORK | Framework calls onCreateActionMode when action mode is created | fragments/MainFragment.java:461,482 |
| MainFragment$3.onPrepareActionMode | REACHABLE | FRAMEWORK | Framework calls onPrepareActionMode to refresh action mode menu before showing | fragments/MainFragment.java:461,520 |
| MainFragment$4.onReceive | REACHABLE | FRAMEWORK | Framework dispatches broadcast MainActivity.KEY_INTENT_LOAD_LIST to reload file list | fragments/MainFragment.java:776-779,1421 |
| PrepareCopyTask$CopyNode.getConflictingFiles | UNREACHABLE | no_trigger_in_app | Getter method never called; PrepareCopyTask.onEndDialog accesses field conflictingFiles directly instead of calling getter | asynchronous/asynctasks/PrepareCopyTask.java:237-240,390-392 |
| PrepareCopyTask$CopyNode.getFilesToCopy | UNREACHABLE | no_trigger_in_app | Getter method never called; PrepareCopyTask.onEndDialog accesses field filesToCopy directly instead of calling getter | asynchronous/asynctasks/PrepareCopyTask.java:237-240,386-388 |
| RecyclerPreloadSizeProvider$SizeViewTarget.onResourceReady | UNREACHABLE | framework_never_calls | SizeViewTarget is created only to call getSize() for measurement; no resource is loaded so Glide never calls onResourceReady; method body is empty stub | adapters/glide/RecyclerPreloadSizeProvider.java:72-81 |
| ScrimInsetsRelativeLayout.draw | UNREACHABLE | no_trigger_in_app | ScrimInsetsRelativeLayout custom view never used in app; grep finds no XML layout references and no Java instantiation | ui/views/ScrimInsetsRelativeLayout.java:82-113 |
| ScrimInsetsRelativeLayout.fitSystemWindows | UNREACHABLE | no_trigger_in_app | ScrimInsetsRelativeLayout custom view never used in app; grep finds no XML layout references and no Java instantiation | ui/views/ScrimInsetsRelativeLayout.java:70-80 |
| ScrimInsetsRelativeLayout.onAttachedToWindow | UNREACHABLE | no_trigger_in_app | ScrimInsetsRelativeLayout custom view never used in app; grep finds no XML layout references and no Java instantiation | ui/views/ScrimInsetsRelativeLayout.java:116-122 |
| ScrimInsetsRelativeLayout.onDetachedFromWindow | UNREACHABLE | no_trigger_in_app | ScrimInsetsRelativeLayout custom view never used in app; grep finds no XML layout references and no Java instantiation | ui/views/ScrimInsetsRelativeLayout.java:124-130 |
| ScrimInsetsRelativeLayout.setOnInsetsCallback | UNREACHABLE | no_trigger_in_app | ScrimInsetsRelativeLayout custom view never used in app; grep finds no XML layout references and no Java instantiation | ui/views/ScrimInsetsRelativeLayout.java:137-139 |
| ServiceWatcherUtil$1.run | REACHABLE | FRAMEWORK | Handler posts and dispatches Runnable on main thread | utils/ServiceWatcherUtil.java:75-77,80 |
| SevenZFile$1.read() | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| SevenZFile$1.read(byte[]) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| SftpConnectDialog.onActivityResult | REACHABLE | RESULT | Framework delivers activity result when user picks SSH key file | ui/dialogs/SftpConnectDialog.java:334,473 |
| SftpConnectDialog.onCreate | REACHABLE | LIFECYCLE | Framework calls DialogFragment.onCreate | ui/dialogs/SftpConnectDialog.java:74,123 (extends DialogFragment) |
| SftpConnectDialog.onCreateDialog | REACHABLE | LIFECYCLE | Framework calls DialogFragment.onCreateDialog to create the dialog | ui/dialogs/SftpConnectDialog.java:123 |
| ShareAdapter.getItemId | REACHABLE | FRAMEWORK | RecyclerView calls getItemId for stable IDs | utils/share/ShareAdapter.java:52; utils/MainActivityHelper.java:320 |
| ShareAdapter.onBindViewHolder | REACHABLE | FRAMEWORK | RecyclerView calls onBindViewHolder to bind data to ViewHolder | utils/share/ShareAdapter.java:61; utils/MainActivityHelper.java:320 |
| ShareAdapter.onCreateViewHolder | REACHABLE | FRAMEWORK | RecyclerView calls onCreateViewHolder to create ViewHolder instances | utils/share/ShareAdapter.java:47; utils/MainActivityHelper.java:320 |
| SshAuthenticationTask$1.getPrivate | REACHABLE | CALL | SSHJ library calls getPrivate to retrieve private key for authentication | asynchronous/asynctasks/ssh/SshAuthenticationTask.java:89,95 |
| SshAuthenticationTask$1.getType | REACHABLE | CALL | SSHJ library calls getType to determine key algorithm type | asynchronous/asynctasks/ssh/SshAuthenticationTask.java:100 |
| SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| SshAuthenticationTask.doInBackground | REACHABLE | ASYNC | AsyncTask.execute runs doInBackground on worker thread | asynchronous/asynctasks/ssh/SshAuthenticationTask.java:107; ssh/PemToKeyPairTask.java:92 |
| SshAuthenticationTask.onPostExecute | REACHABLE | ASYNC | AsyncTask runs onPostExecute on main thread after doInBackground completes | asynchronous/asynctasks/ssh/SshAuthenticationTask.java:146 |
| SshClientTemplate.<init>(String) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| SshConnectionPool$AsyncRemoveConnection.doInBackground | REACHABLE | ASYNC | AsyncTask.execute runs doInBackground on worker thread | filesystem/ssh/SshConnectionPool.java:165,218 |
| StreamSource.read() | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| StreamSource.read(byte[],int,int) | INCOMPLETE | NOT IN method_list.json | Method not found in method_list.json; skipped per batch instructions | N/A |
| SubnetScanner$1.run | REACHABLE | FRAMEWORK | Handler posts Runnable to main thread when device is discovered | utils/SubnetScanner.java:83-86 |
| SubnetScanner$Task.call | REACHABLE | ASYNC | ExecutorService invokes Callable.call on worker thread | utils/SubnetScanner.java:67,73,115 |
| SubnetScanner.run | REACHABLE | FRAMEWORK | ExecutorService dispatches Runnable.run on worker thread | utils/SubnetScanner.java:58; utils/MainActivityHelper.java:415-416 |

STATUS: DONE 23:42
