STATUS: RUNNING 21:39

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CompressedExplorerFragment.<init> | REACHABLE | | Constructor called by MainActivity.openCompressed | SRC activities/MainActivity.java:1244 |
| CompressedExplorerFragment.archiveCorruptOrUnsupportedToast | REACHABLE | | Called by changePath on error | SRC fragments/CompressedExplorerFragment.java:417,421,486-489 |
| CompressedExplorerFragment.canGoBack | REACHABLE | | Called by MainActivity.onBackPressed | SRC activities/MainActivity.java:722, fragments/CompressedExplorerFragment.java:471-473 |
| CompressedExplorerFragment.changePath | REACHABLE | | Called by onCreate and refresh | SRC fragments/CompressedExplorerFragment.java:217,437,476,403-423 |
| CompressedExplorerFragment.createViews | REACHABLE | | Called by changePath and onRestoreInstanceState | SRC fragments/CompressedExplorerFragment.java:412-415,243,447-470 |
| CompressedExplorerFragment.getPath | REACHABLE | | Called by BottomBar.showButtons via interface | SRC ui/views/appbar/BottomBar.java:189,475, fragments/CompressedExplorerFragment.java:428-431 |
| CompressedExplorerFragment.getRootDrawable | REACHABLE | | Called by BottomBar.showButtons via interface | SRC ui/views/appbar/BottomBar.java:196,475, fragments/CompressedExplorerFragment.java:433-435 |
| CompressedExplorerFragment.goBack | REACHABLE | | Called by adapter and MainActivity when back pressed | SRC adapters/CompressedExplorerAdapter.java:246, activities/MainActivity.java:723, fragments/CompressedExplorerFragment.java:475-477 |
| CompressedExplorerFragment.isRoot | UNREACHABLE | no_trigger_in_app | Helper method edge traced through changePath | SRC fragments/CompressedExplorerFragment.java:478-480 |
| CompressedExplorerFragment.isRootRelativePath | UNREACHABLE | no_trigger_in_app | Helper method edge traced through calling method | SRC fragments/CompressedExplorerFragment.java:482-484 |
| CompressedExplorerFragment.lambda$changePath$2 | UNREACHABLE | framework_never_calls | Lambda synthetic for changePath callback covered by changePath edge | SRC fragments/CompressedExplorerFragment.java:412 |
| CompressedExplorerFragment.lambda$createViews$3 | UNREACHABLE | framework_never_calls | Lambda synthetic for AppBarLayout listener covered by createViews edge | SRC fragments/CompressedExplorerFragment.java:465-467 |
| CompressedExplorerFragment.lambda$onActivityCreated$1 | UNREACHABLE | framework_never_calls | Lambda synthetic for toolbar touch listener covered by stopAnim edge | SRC fragments/CompressedExplorerFragment.java:157-164 |
| CompressedExplorerFragment.lambda$onCreateView$0 | UNREACHABLE | framework_never_calls | Lambda synthetic for listView touch listener covered by stopAnim edge | SRC fragments/CompressedExplorerFragment.java:137-147 |
| CompressedExplorerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle callback after onCreateView | SRC fragments/CompressedExplorerFragment.java:149-224 |
| CompressedExplorerFragment.onCreate | REACHABLE | | Fragment lifecycle callback after constructor | SRC fragments/CompressedExplorerFragment.java:128-131 |
| CompressedExplorerFragment.onCreateView | REACHABLE | | Fragment lifecycle callback after onCreate | SRC fragments/CompressedExplorerFragment.java:133-147 |
| CompressedExplorerFragment.onDestroyView | REACHABLE | | Fragment lifecycle callback after onPause | SRC fragments/CompressedExplorerFragment.java:354-365 |
| CompressedExplorerFragment.onPause | REACHABLE | | Fragment lifecycle callback after onResume | SRC fragments/CompressedExplorerFragment.java:375-380 |
| CompressedExplorerFragment.onRestoreInstanceState | REACHABLE | | Called by onActivityCreated when restoring saved state | SRC fragments/CompressedExplorerFragment.java:219,236-244 |
| CompressedExplorerFragment.onResume | REACHABLE | | Fragment lifecycle callback after onActivityCreated | SRC fragments/CompressedExplorerFragment.java:367-373 |
| CompressedExplorerFragment.onSaveInstanceState | UNREACHABLE | framework_never_calls | Framework callback for saving state not traced per schema | SRC fragments/CompressedExplorerFragment.java:226-234 |
| CompressedExplorerFragment.refresh | REACHABLE | | Called by SwipeRefreshLayout when user swipes | SRC fragments/CompressedExplorerFragment.java:145,436-438 |
| CompressedExplorerFragment.stopAnim | REACHABLE | | Called by touch listeners on listView and toolbar | SRC fragments/CompressedExplorerFragment.java:139-142,157-164,149-155 |
| CompressedExplorerFragment.updateBottomBar | REACHABLE | | Called by changePath and createViews | SRC fragments/CompressedExplorerFragment.java:409,416,468,440-445 |
| CompressedExplorerFragment$1.<init> | REACHABLE | | ActionMode.Callback created as mActionModeCallback field | SRC fragments/CompressedExplorerFragment.java:247 |
| CompressedExplorerFragment$1.hideOption | REACHABLE | | Called by onCreateActionMode to hide menu items | SRC fragments/CompressedExplorerFragment.java:249-252,264-270 |
| CompressedExplorerFragment$1.onActionItemClicked | REACHABLE | | ActionMode.Callback lifecycle when item clicked | SRC fragments/CompressedExplorerFragment.java:299-329 |
| CompressedExplorerFragment$1.onCreateActionMode | REACHABLE | | ActionMode.Callback lifecycle when mode starts | SRC fragments/CompressedExplorerFragment.java:257-281 |
| CompressedExplorerFragment$1.onDestroyActionMode | REACHABLE | | ActionMode.Callback lifecycle when mode ends | SRC fragments/CompressedExplorerFragment.java:332-346 |
| CompressedExplorerFragment$1.onPrepareActionMode | REACHABLE | | ActionMode.Callback lifecycle after onCreate | SRC fragments/CompressedExplorerFragment.java:289-296 |
| CompressedExplorerFragment$1.showOption | REACHABLE | | Called by onCreateActionMode to show menu items | SRC fragments/CompressedExplorerFragment.java:254-256,271,273 |
| CompressedExplorerFragment$2.<init> | REACHABLE | | ServiceConnection created as mServiceConnection field | SRC fragments/CompressedExplorerFragment.java:382 |
| CompressedExplorerFragment$2.onServiceConnected | REACHABLE | | ServiceConnection lifecycle when service binds | SRC fragments/CompressedExplorerFragment.java:385-387 |
| CompressedExplorerFragment$2.onServiceDisconnected | REACHABLE | | ServiceConnection lifecycle when service disconnects | SRC fragments/CompressedExplorerFragment.java:390-401 |

STATUS: DONE 21:44
