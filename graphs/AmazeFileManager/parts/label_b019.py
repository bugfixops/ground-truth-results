# ---- Helper batch_019 label part (2025-01-27)

# DataUtils methods - singleton data holder for app-wide state

# Private constructor - called by singleton holder
e('DataUtils$DataUtilsHolder.<clinit>', 'DataUtils.<init>', 'CALL',
  'Static initializer creates singleton instance',
  evidence='SRC DataUtils.java:74-80')

# getInstance - called from many screens to access the singleton
e('MainFragment.onCreate', 'DataUtils.getInstance', 'LIFECYCLE', 
  'Fragment onCreate calls getInstance to initialize dataUtils field',
  evidence='SRC MainFragment.java:200-207, DataUtils.java:82-84')

# containsServer(String[]) - called to check if server exists
e('MainActivity.onActivityResult', 'DataUtils.containsServer', 'LIFECYCLE',
  'Activity result handler checks if server configuration exists',
  evidence='SRC MainActivity.java:1624, DataUtils.java:86-88')

# containsServer(String) - overload called with path string
e('MainFragment.onListItemClicked', 'DataUtils.containsServer', 'GUI',
  'Click handler checks server by path',
  evidence='SRC MainFragment.java:1349, DataUtils.java:90-103')

# containsBooks - called to check if bookmark exists
e('RenameBookmark.onClick', 'DataUtils.containsBooks', 'GUI',
  'Dialog click handler checks if bookmark already exists',
  evidence='SRC RenameBookmark.java:65, DataUtils.java:105-107')

# clear - resets all data structures
e('DataUtils.registerOnDataChangedListener', 'DataUtils.clear', 'CALL',
  'Listener registration calls clear to reset state',
  evidence='SRC DataUtils.java:159-162, 147-157')

# registerOnDataChangedListener - called from MainActivity.onCreate
e('MainActivity.onCreate', 'DataUtils.registerOnDataChangedListener', 'LIFECYCLE',
  'Activity onCreate registers data change listener',
  evidence='SRC MainActivity.java:277-284, DataUtils.java:159-163')

# contains(String, ArrayList) - private helper called internally
e('DataUtils.containsServer', 'DataUtils.contains', 'CALL',
  'containsServer String overload calls private contains helper',
  evidence='SRC DataUtils.java:90-103, 164-171')

# contains(String[], ArrayList) - private helper called internally
e('DataUtils.containsServer', 'DataUtils.contains', 'CALL',
  'containsServer array overload calls private contains helper',
  evidence='SRC DataUtils.java:86-88, 173-182')

# removeBook - called to delete a bookmark
e('RenameBookmark.onClick', 'DataUtils.removeBook', 'GUI',
  'Dialog click handler removes old bookmark',
  evidence='SRC RenameBookmark.java:142, DataUtils.java:186-191')

# removeAccount - called to remove cloud account
e('MainActivity.deleteCloudAccount', 'DataUtils.removeAccount', 'CALL',
  'Cloud account deletion removes from DataUtils',
  evidence='SRC MainActivity.java:1825, DataUtils.java:194-218')

# removeServer - called to delete server configuration
e('SftpConnectDialog.onClick', 'DataUtils.removeServer', 'GUI',
  'Dialog click handler removes server',
  evidence='SRC SftpConnectDialog.java:247, DataUtils.java:227-233')

# addBook(String[]) - called to add bookmark without refresh
e('RenameBookmark.onClick', 'DataUtils.addBook', 'GUI',
  'Dialog click adds bookmark after rename',
  evidence='SRC RenameBookmark.java:143, DataUtils.java:235-242')

# addBook(String[], boolean) - called to add bookmark with optional refresh
e('ItemPopupMenu.onMenuItemClick', 'DataUtils.addBook', 'GUI',
  'Popup menu item adds bookmark with drawer refresh',
  evidence='SRC ItemPopupMenu.java:113, DataUtils.java:250-265')

# addAccount - called to store cloud account
e('CloudLoaderAsyncTask.doInBackground', 'DataUtils.addAccount', 'ASYNC',
  'Background task adds authenticated cloud account',
  evidence='SRC CloudLoaderAsyncTask.java:107, DataUtils.java:268-270')

# addServer - called to store server configuration
e('SftpConnectDialog.onEditorAction', 'DataUtils.addServer', 'GUI',
  'SFTP dialog editor action adds server',
  evidence='SRC SftpConnectDialog.java:349, DataUtils.java:272-274')

# addHiddenFile - called to mark file as hidden
e('MainFragment.addToHidden', 'DataUtils.addHiddenFile', 'CALL',
  'Fragment method adds file to hidden list',
  evidence='SRC MainFragment.java:1553, DataUtils.java:276-284')

# removeHiddenFile - called to unmark file as hidden
e('HiddenAdapter.onClick', 'DataUtils.removeHiddenFile', 'GUI',
  'Adapter click handler removes file from hidden list',
  evidence='SRC HiddenAdapter.java:95, DataUtils.java:287-295')

# setHistory - called to initialize history from database
e('MainActivity.onCreate', 'DataUtils.setHistory', 'LIFECYCLE',
  'Activity onCreate loads history from persistent storage',
  evidence='SRC MainActivity.java:370, DataUtils.java:298-301')

# getHistory - called to retrieve history for display
e('GeneralDialogCreation.showHistoryDialog', 'DataUtils.getHistory', 'CALL',
  'Dialog creation retrieves history list',
  evidence='SRC GeneralDialogCreation.java:1098, DataUtils.java:303-305')

# addHistoryFile - called when navigating to path
e('MainFragment.goBackItemClick', 'DataUtils.addHistoryFile', 'GUI',
  'Back button click adds path to history',
  evidence='SRC MainFragment.java:937, DataUtils.java:307-312')

# sortBook - called to sort bookmarks alphabetically
e('RenameBookmark.onClick', 'DataUtils.sortBook', 'GUI',
  'After adding bookmark, sort the list',
  evidence='SRC RenameBookmark.java:144, DataUtils.java:314-316')

# setServers - called to initialize servers from database
e('MainActivity.onCreate', 'DataUtils.setServers', 'LIFECYCLE',
  'Activity onCreate loads server list from persistent storage',
  evidence='SRC MainActivity.java:377, DataUtils.java:318-321')

# setBooks - called to initialize bookmarks from database
e('MainActivity.onCreate', 'DataUtils.setBooks', 'LIFECYCLE',
  'Activity onCreate loads bookmarks from persistent storage',
  evidence='SRC MainActivity.java:373, DataUtils.java:323-326')

# getServers - called to retrieve server list
e('Drawer.addServersMenuItem', 'DataUtils.getServers', 'CALL',
  'Drawer retrieves server list to populate menu',
  evidence='SRC Drawer.java:295-296, DataUtils.java:333-335')

# getBooks - called to retrieve bookmark list
e('Drawer.addBookmarksMenuItem', 'DataUtils.getBooks', 'CALL',
  'Drawer retrieves bookmarks to populate menu',
  evidence='SRC Drawer.java:354-358, DataUtils.java:337-339')

# getAccounts - called to retrieve cloud accounts
e('Drawer.addCloudMenuItem', 'DataUtils.getAccounts', 'CALL',
  'Drawer retrieves cloud accounts for menu',
  evidence='SRC Drawer.java:309, DataUtils.java:341-343')

# getAccount - called to get specific cloud account
e('LoadFilesListTask.doInBackground', 'DataUtils.getAccount', 'ASYNC',
  'Background task retrieves cloud account for file listing',
  evidence='SRC LoadFilesListTask.java:179, DataUtils.java:345-368')

# isFileHidden - called to check if file should be hidden
e('LoadFilesListTask.doInBackground', 'DataUtils.isFileHidden', 'ASYNC',
  'Background task checks hidden status to filter files',
  evidence='SRC LoadFilesListTask.java:131, DataUtils.java:371-373')

# getHiddenFiles - called to retrieve all hidden files
e('GeneralDialogCreation.showHiddenDialog', 'DataUtils.getHiddenFiles', 'CALL',
  'Dialog creation retrieves hidden files tree',
  evidence='SRC GeneralDialogCreation.java:1120, DataUtils.java:375-377')

# setHiddenFiles - called to initialize hidden files from database
e('MainActivity.onCreate', 'DataUtils.setHiddenFiles', 'LIFECYCLE',
  'Activity onCreate loads hidden files from persistent storage',
  evidence='SRC MainActivity.java:369, DataUtils.java:379-381')

# setGridfiles - called to initialize grid view preferences
e('MainActivity.onCreate', 'DataUtils.setGridfiles', 'LIFECYCLE',
  'Activity onCreate loads grid view paths from database',
  evidence='SRC MainActivity.java:371, DataUtils.java:383-389')

# setListfiles - called to initialize list view preferences
e('MainActivity.onCreate', 'DataUtils.setListfiles', 'LIFECYCLE',
  'Activity onCreate loads list view paths from database',
  evidence='SRC MainActivity.java:372, DataUtils.java:391-397')

# setPathAsGridOrList - called when user changes view mode
e('MainActivity.onOptionsItemSelected', 'DataUtils.setPathAsGridOrList', 'FRAMEWORK',
  'Menu item selection sets view mode for path',
  evidence='SRC MainActivity.java:1009, DataUtils.java:399-401')

# getListOrGridForPath - called to determine view mode for path
e('MainFragment.onCreate', 'DataUtils.getListOrGridForPath', 'LIFECYCLE',
  'Fragment onCreate retrieves view mode preference',
  evidence='SRC MainFragment.java:219, DataUtils.java:403-406')

# clearHistory - called when user clears history
e('GeneralDialogCreation.lambda$showHistoryDialog', 'DataUtils.clearHistory', 'GUI',
  'Dialog negative button clears history',
  evidence='SRC GeneralDialogCreation.java:1094, DataUtils.java:408-413')

# getStorages - called to retrieve storage volumes
e('MainActivityHelper.addStorage', 'DataUtils.getStorages', 'CALL',
  'Helper adds to storage list via getter',
  evidence='SRC MainActivityHelper.java:117, DataUtils.java:415-417')

# setStorages - called to initialize storage volumes
e('Drawer.setDrawerHeaderBackground', 'DataUtils.setStorages', 'CALL',
  'Drawer initialization sets storage directories',
  evidence='SRC Drawer.java:293, DataUtils.java:419-421')

# getDrawerMetadata - called to retrieve menu item metadata
e('Drawer.onNavigationItemSelected', 'DataUtils.getDrawerMetadata', 'FRAMEWORK',
  'Navigation item selection retrieves associated metadata',
  evidence='SRC Drawer.java:564, DataUtils.java:423-425')

# putDrawerMetadata - called to store menu item metadata
e('Drawer.addNewItem', 'DataUtils.putDrawerMetadata', 'CALL',
  'Adding drawer item stores its metadata',
  evidence='SRC Drawer.java:464, DataUtils.java:427-430')

# findLongestContainingDrawerItem - called to find matching menu item
e('Drawer.selectCorrectDrawerItem', 'DataUtils.findLongestContainingDrawerItem', 'CALL',
  'Drawer selects item by finding longest path prefix',
  evidence='SRC Drawer.java:673, DataUtils.java:436-438')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B019 = {
    'DataUtils.containsAccounts': ('no_trigger_in_app', 'Method is defined but has no callers in app source; grep shows only definition in DataUtils.java:118', 'SRC DataUtils.java:118-144', 'SOURCE'),
    'DataUtils.setAccounts': ('no_trigger_in_app', 'Setter is never called in app source; accounts are added via addAccount but never bulk-set', 'SRC DataUtils.java:328-331', 'SOURCE'),
}
