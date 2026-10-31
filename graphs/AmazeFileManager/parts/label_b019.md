STATUS: RUNNING 21:45

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| DataUtils.<init> | REACHABLE | | Called from DataUtilsHolder static initializer | SRC DataUtils.java:74-80 |
| DataUtils.getInstance | REACHABLE | | Called from MainFragment.onCreate (LIFECYCLE) | SRC MainFragment.java:207, DataUtils.java:82-84 |
| DataUtils.containsServer | REACHABLE | | Called from MainActivity.onActivityResult (LIFECYCLE) | SRC MainActivity.java:1624, DataUtils.java:86-88 |
| DataUtils.containsServer | REACHABLE | | Called from MainFragment list click handler (GUI) | SRC MainFragment.java:1349, DataUtils.java:90-103 |
| DataUtils.containsBooks | REACHABLE | | Called from RenameBookmark.onClick (GUI) | SRC RenameBookmark.java:65, DataUtils.java:105-107 |
| DataUtils.containsAccounts | UNREACHABLE | no_trigger_in_app | No app callers; grep shows only definition | SRC DataUtils.java:118-144 |
| DataUtils.clear | REACHABLE | | Called from registerOnDataChangedListener | SRC DataUtils.java:159-162, 147-157 |
| DataUtils.registerOnDataChangedListener | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:284, DataUtils.java:159-163 |
| DataUtils.contains | REACHABLE | | Called from containsServer (String overload) | SRC DataUtils.java:90-103, 164-171 |
| DataUtils.contains | REACHABLE | | Called from containsServer (array overload) | SRC DataUtils.java:86-88, 173-182 |
| DataUtils.removeBook | REACHABLE | | Called from RenameBookmark.onClick (GUI) | SRC RenameBookmark.java:142, DataUtils.java:186-191 |
| DataUtils.removeAccount | REACHABLE | | Called from MainActivity.deleteCloudAccount | SRC MainActivity.java:1825, DataUtils.java:194-218 |
| DataUtils.removeServer | REACHABLE | | Called from SftpConnectDialog.onClick (GUI) | SRC SftpConnectDialog.java:247, DataUtils.java:227-233 |
| DataUtils.addBook | REACHABLE | | Called from RenameBookmark.onClick (GUI) | SRC RenameBookmark.java:143, DataUtils.java:235-242 |
| DataUtils.addBook | REACHABLE | | Called from ItemPopupMenu.onMenuItemClick (GUI) | SRC ItemPopupMenu.java:113, DataUtils.java:250-265 |
| DataUtils.addAccount | REACHABLE | | Called from CloudLoaderAsyncTask.doInBackground (ASYNC) | SRC CloudLoaderAsyncTask.java:107, DataUtils.java:268-270 |
| DataUtils.addServer | REACHABLE | | Called from SftpConnectDialog editor action (GUI) | SRC SftpConnectDialog.java:349, DataUtils.java:272-274 |
| DataUtils.addHiddenFile | REACHABLE | | Called from MainFragment.addToHidden | SRC MainFragment.java:1553, DataUtils.java:276-284 |
| DataUtils.removeHiddenFile | REACHABLE | | Called from HiddenAdapter.onClick (GUI) | SRC HiddenAdapter.java:95, DataUtils.java:287-295 |
| DataUtils.setHistory | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:370, DataUtils.java:298-301 |
| DataUtils.getHistory | REACHABLE | | Called from GeneralDialogCreation.showHistoryDialog | SRC GeneralDialogCreation.java:1098, DataUtils.java:303-305 |
| DataUtils.addHistoryFile | REACHABLE | | Called from MainFragment back button (GUI) | SRC MainFragment.java:937, DataUtils.java:307-312 |
| DataUtils.sortBook | REACHABLE | | Called from RenameBookmark.onClick (GUI) | SRC RenameBookmark.java:144, DataUtils.java:314-316 |
| DataUtils.setServers | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:377, DataUtils.java:318-321 |
| DataUtils.setBooks | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:373, DataUtils.java:323-326 |
| DataUtils.setAccounts | UNREACHABLE | no_trigger_in_app | Never called; accounts added via addAccount only | SRC DataUtils.java:328-331 |
| DataUtils.getServers | REACHABLE | | Called from Drawer.addServersMenuItem | SRC Drawer.java:295-296, DataUtils.java:333-335 |
| DataUtils.getBooks | REACHABLE | | Called from Drawer.addBookmarksMenuItem | SRC Drawer.java:354-358, DataUtils.java:337-339 |
| DataUtils.getAccounts | REACHABLE | | Called from Drawer.addCloudMenuItem | SRC Drawer.java:309, DataUtils.java:341-343 |
| DataUtils.getAccount | REACHABLE | | Called from LoadFilesListTask.doInBackground (ASYNC) | SRC LoadFilesListTask.java:179, DataUtils.java:345-368 |
| DataUtils.isFileHidden | REACHABLE | | Called from LoadFilesListTask.doInBackground (ASYNC) | SRC LoadFilesListTask.java:131, DataUtils.java:371-373 |
| DataUtils.getHiddenFiles | REACHABLE | | Called from GeneralDialogCreation.showHiddenDialog | SRC GeneralDialogCreation.java:1120, DataUtils.java:375-377 |
| DataUtils.setHiddenFiles | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:369, DataUtils.java:379-381 |
| DataUtils.setGridfiles | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:371, DataUtils.java:383-389 |
| DataUtils.setListfiles | REACHABLE | | Called from MainActivity.onCreate (LIFECYCLE) | SRC MainActivity.java:372, DataUtils.java:391-397 |
| DataUtils.setPathAsGridOrList | REACHABLE | | Called from MainActivity.onOptionsItemSelected (FRAMEWORK) | SRC MainActivity.java:1009, DataUtils.java:399-401 |
| DataUtils.getListOrGridForPath | REACHABLE | | Called from MainFragment.onCreate (LIFECYCLE) | SRC MainFragment.java:219, DataUtils.java:403-406 |
| DataUtils.clearHistory | REACHABLE | | Called from GeneralDialogCreation dialog button (GUI) | SRC GeneralDialogCreation.java:1094, DataUtils.java:408-413 |
| DataUtils.getStorages | REACHABLE | | Called from MainActivityHelper.addStorage | SRC MainActivityHelper.java:117, DataUtils.java:415-417 |
| DataUtils.setStorages | REACHABLE | | Called from Drawer.setDrawerHeaderBackground | SRC Drawer.java:293, DataUtils.java:419-421 |
| DataUtils.getDrawerMetadata | REACHABLE | | Called from Drawer.onNavigationItemSelected (FRAMEWORK) | SRC Drawer.java:564, DataUtils.java:423-425 |
| DataUtils.putDrawerMetadata | REACHABLE | | Called from Drawer.addNewItem | SRC Drawer.java:464, DataUtils.java:427-430 |
| DataUtils.findLongestContainingDrawerItem | REACHABLE | | Called from Drawer.selectCorrectDrawerItem | SRC Drawer.java:673, DataUtils.java:436-438 |

STATUS: DONE 21:49
