STATUS: RUNNING 21:54

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| MainFragment$1.<init> | REACHABLE | | Constructor called when MainFragment.onActivityCreated creates listener | SRC MainFragment.java:310 |
| MainFragment$1.onGlobalLayout | REACHABLE | | Framework callback invoked by ViewTreeObserver when layout changes | SRC MainFragment.java:310-328 |
| MainFragment$2.<init> | REACHABLE | | Constructor called when setGridLayoutSpanSizeLookup creates lookup | SRC MainFragment.java:341 |
| MainFragment$2.getSpanSize | REACHABLE | | Framework callback invoked by GridLayoutManager to query span sizes | SRC MainFragment.java:343-351 |
| MainFragment$3.<init> | REACHABLE | | Constructor called when RecyclerAdapter accesses mActionModeCallback field | SRC MainFragment.java:461, RecyclerAdapter.java:192 |
| MainFragment$3.hideOption | REACHABLE | | Called by onCreateActionMode and onPrepareActionMode to hide menu items | SRC MainFragment.java:462-465, called at 481-483, 521-635 |
| MainFragment$3.initMenu | REACHABLE | | Called by onCreateActionMode at line 480 | SRC MainFragment.java:469-474, called at 480 |
| MainFragment$3.onActionItemClicked | REACHABLE | | Framework callback when user selects action mode menu item | SRC MainFragment.java:638-747 |
| MainFragment$3.onCreateActionMode | REACHABLE | | Framework callback when action mode is created via startSupportActionMode | SRC MainFragment.java:475-504, RecyclerAdapter.java:192 |
| MainFragment$3.onDestroyActionMode | REACHABLE | | Framework callback when action mode is destroyed | SRC MainFragment.java:748-759 |
| MainFragment$3.onPrepareActionMode | REACHABLE | | Framework callback to update menu, called after onCreateActionMode and on invalidate | SRC MainFragment.java:510-635 |
| MainFragment$3.showOption | REACHABLE | | Called by onCreateActionMode and onPrepareActionMode to show menu items | SRC MainFragment.java:467-470, called at 485, 521-635 |
| MainFragment$4.<init> | REACHABLE | | Constructor called when MainFragment.onResume accesses receiver2 field | SRC MainFragment.java:776, accessed at 1421 |
| MainFragment$4.onReceive | REACHABLE | | Broadcast receiver callback invoked when KEY_INTENT_LOAD_LIST broadcast is sent | SRC MainFragment.java:777-825, registered at 1421 |
| MainFragment$4$1.<init> | REACHABLE | | Constructor called when MainFragment$4.onReceive creates MediaScannerConnectionClient | SRC MainFragment.java:798 |
| MainFragment$4$1.onMediaScannerConnected | REACHABLE | | Framework callback invoked when MediaScannerConnection connects | SRC MainFragment.java:799-801 |
| MainFragment$4$1.onScanCompleted | REACHABLE | | Framework callback invoked when MediaScannerConnection completes scan | SRC MainFragment.java:802-805 |
| MainFragment$5.<init> | REACHABLE | | Constructor called when MainFragment.onResume accesses decryptReceiver field | SRC MainFragment.java:828, accessed at 1427 |
| MainFragment$5.onReceive | REACHABLE | | Broadcast receiver callback invoked when DECRYPT_BROADCAST is sent | SRC MainFragment.java:829-836, registered at 1427 |
| MainFragment$6.<init> | REACHABLE | | Constructor called when onSearchCompleted creates AsyncTask | SRC MainFragment.java:1640 |
| MainFragment$6.doInBackground | REACHABLE | | AsyncTask callback executed on thread pool via executeOnExecutor | SRC MainFragment.java:1641-1645, executed at 1653 |
| MainFragment$6.onPostExecute | REACHABLE | | AsyncTask callback executed on UI thread after doInBackground completes | SRC MainFragment.java:1646-1651 |
| MainFragment$7.<init> | REACHABLE | | Constructor called when launchSMB creates Thread | SRC MainFragment.java:1658 |
| MainFragment$7.lambda$run$0 | REACHABLE | | Lambda passed to runOnUiThread, invoked on UI thread | SRC MainFragment.java:1671 |
| MainFragment$7.run | REACHABLE | | Thread run method executed when thread starts | SRC MainFragment.java:1659-1690 |
| MapEntry.<init> | REACHABLE | | Constructor called by SearchTextTask.doInBackground | SRC MapEntry.java:16, SearchTextTask.java:67 |
| MediaStoreHack.<clinit> | UNREACHABLE | framework_never_calls | No static initializer block in source, class has no static initialization code | SRC MediaStoreHack.java:1-280 shows no static block |
| MediaStoreHack.<init> | UNREACHABLE | no_trigger_in_app | No constructor calls found in app, all MediaStoreHack methods are static | SRC MediaStoreHack.java:1-280 shows only static methods, grep shows no new MediaStoreHack |
| MediaStoreHack.delete | REACHABLE | | Called by MediaStoreHack.mkdir at line 253 | SRC MediaStoreHack.java:61-78, called at 253 |
| MediaStoreHack.getExternalFilesDir | REACHABLE | | Called by MediaStoreHack.installTemporaryTrack at line 208 | SRC MediaStoreHack.java:80-82, called at 208 |
| MediaStoreHack.getInputStream | REACHABLE | | Called by GenericCopyUtil.doCopy at line 173 | SRC MediaStoreHack.java:85-101, GenericCopyUtil.java:173 |
| MediaStoreHack.getOutputStream | REACHABLE | | Called by GenericCopyUtil.doCopy and FileUtil.getOutputStream | SRC MediaStoreHack.java:103-113, GenericCopyUtil.java:273, FileUtil.java:184 |
| MediaStoreHack.getTemporaryAlbumId | REACHABLE | | Called by MediaStoreHack.mkdir at line 237 | SRC MediaStoreHack.java:138-204, called at 237 |
| MediaStoreHack.getUriFromFile | REACHABLE | | Called by MainFragment.onListItemClicked, FileUtil.getDocumentFile, FileUtil.scanFile | SRC MediaStoreHack.java:115-136, MainFragment.java:983, FileUtil.java:122, FileUtil.java:392 |
| MediaStoreHack.installTemporaryTrack | REACHABLE | | Called by MediaStoreHack.getTemporaryAlbumId at line 141 | SRC MediaStoreHack.java:207-228, called at 141 |
| MediaStoreHack.mkdir | REACHABLE | | Called by FileUtil.mkdir at line 511 | SRC MediaStoreHack.java:230-256, FileUtil.java:511 |
| MediaStoreHack.mkfile | REACHABLE | | Called by FileUtil.mkfile at line 581 | SRC MediaStoreHack.java:258-267, FileUtil.java:581 |

STATUS: DONE 21:59
