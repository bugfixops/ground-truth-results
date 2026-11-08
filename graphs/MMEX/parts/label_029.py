# batch 029 (label_029): com.money.manager.ex.common.CategoryListFragment, methods 1-40 of 43 (the class, its constructor, the anonymous listeners $1-$8 and their constructors). Batch 030 holds $8.onChildClick, $9.<init> and $9.onGroupClick. Rows and printed lines: graphs/MMEX/parts/label_029.md.
# Page S_CATEGORY_LIST is defined at graph_def.py:1214 and reused here (D9). Its ENTERS edge is written here, from onActivityCreated (the list is set up and shown there).
# CALL edges come from auto_calls.json (the constructors, the calls inside this class, the listener <init> records, the receiver records "...@CategoryListFragment"), so none are written here.
# Library classes (androidx Fragment, LoaderManager, the context menu dispatch, the fragment state save) are not in fw_src: those claims are INFERRED (source not read). FW-SRC is cited only for printed ranges (AbsListView, View, AlertDialog, AlertController).
# No sup cut in this batch: every auto edge out of the methods of this batch can run on API 27 (see label_029.md).
# No UNREACHABLE entry in this batch: every method has a route (see label_029.md, all rows REACHABLE). grep output: graphs/MMEX/parts/label_029.grep.txt.

# ---- lifecycle and loader callbacks (androidx; library source not read: INFERRED where stated)

e('CategoryListActivity.onCreate', 'CategoryListFragment.onActivityCreated', 'LIFECYCLE',
  'the activity adds the fragment in onCreate (fragment transaction, committed); the framework then calls onActivityCreated on it',
  guard='the fragment is not yet in the fragment manager (CategoryListActivity.java:65); a restored fragment is not added again',
  evidence='SRC common/CategoryListActivity.java:63-70 (fragment added and committed); SRC common/CategoryListFragment.java:96-98; INFERRED androidx FragmentManager calls onActivityCreated after the commit (library source not read)')

e('CategoryListFragment.onActivityCreated', 'S_CATEGORY_LIST', 'ENTERS',
  'the category list screen is shown: onActivityCreated sets up the list, the search menu, the context menu and the + button (lines 101-144)',
  evidence='SRC common/CategoryListFragment.java:96-145; SRC common/CategoryListActivity.java:63-70')

e('CategoryListFragment.onActivityCreated', 'CategoryListFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state (checked ids and the filter) while the fragment is alive, for example when the activity is stopped',
  evidence='SRC common/CategoryListFragment.java:96-98, 239-247; INFERRED androidx FragmentManager saves state through onSaveInstanceState (library source not read)')

e('CategoryListFragment.onActivityCreated', 'CategoryListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader(ID_LOADER_CATEGORYSUB, null, this) asks the LoaderManager for the loader; when no loader exists yet, the callbacks get onCreateLoader',
  evidence='SRC common/CategoryListFragment.java:79, 138; INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library source not read)')

e('CategoryListFragment.restartLoader', 'CategoryListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader(ID_LOADER_CATEGORYSUB) asks the LoaderManager to create a new loader for the new query, so onCreateLoader runs again',
  evidence='SRC common/CategoryListFragment.java:443-445; INFERRED androidx LoaderManager.restartLoader creates the new loader (library source not read)')

e('CategoryListFragment.onCreateLoader', 'CategoryListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader returned at line 275 delivers its cursor to the callbacks when the load finishes; onLoadFinished runs with that cursor',
  evidence='SRC common/CategoryListFragment.java:252-275, 289-290; INFERRED androidx Loader delivers the result to LoaderCallbacks.onLoadFinished (library source not read)')

e('CategoryListFragment.restartLoader', 'CategoryListFragment.onLoaderReset', 'FRAMEWORK',
  'restarting the loader resets the previous one first, so the callbacks get onLoaderReset',
  guard='a loader for id 0 exists already (initLoader ran in onActivityCreated, line 138)',
  evidence='SRC common/CategoryListFragment.java:138, 280-286, 443-445; INFERRED androidx LoaderManager.restartLoader destroys the old loader and calls onLoaderReset (library source not read)')

# ---- user actions on the category list (page S_CATEGORY_LIST)

gui('S_CATEGORY_LIST', 'CategoryListFragment.onCreateContextMenu', 'Long-press a category or subcategory row of the list',
  evidence='SRC common/CategoryListFragment.java:130 (registerForContextMenu on the list), 159-178; FW-SRC core/java/android/widget/AbsListView.java:3223-3246 (performLongPress shows the menu for the child), 3291-3301; FW-SRC core/java/android/view/View.java:12578-12589 (createContextMenu calls the registered listener at 12588); INFERRED the step from showContextMenuForChild to createContextMenu (source not read); INFERRED ExpandableListView long-press (not in fw_src)')

gui('S_CATEGORY_LIST', 'CategoryListFragment.onContextItemSelected', 'Tap Edit, Delete or View transactions in the menu of a row',
  evidence='SRC common/CategoryListFragment.java:175-177 (menu items), 180-227 (switch on the item); INFERRED the context menu item is dispatched to the fragment that registered the menu (androidx; library source not read)')

# ---- dialog buttons: the dialog-creating method calls the listener through AlertDialog (FRAMEWORK, as in label_024)

e('CategoryListFragment.showDialogDeleteCategorySub', 'CategoryListFragment$1.onClick', 'FRAMEWORK',
  'the cannot-delete dialog shows an OK button; the click dismisses the dialog',
  needs_state=state_text('the row is a subcategory (subCategId > 0, line 455) or the category is used by account transactions (CategoryService.isCategoryUsed true, line 457)', ('data',)),
  evidence='SRC common/CategoryListFragment.java:455-472; SRC servicelayer/CategoryService.java:143-147; FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:125-147, 160-167, 344-362, 1021-1023')

e('CategoryListFragment.showDialogDeleteCategorySub', 'CategoryListFragment$2.onClick', 'FRAMEWORK',
  'the confirm delete dialog shows a Cancel button; the click cancels the dialog',
  needs_state=state_text('the row is a category (subCategId <= 0, line 455) and no account transaction uses it (CategoryService.isCategoryUsed false, line 457)', ('data',)),
  evidence='SRC common/CategoryListFragment.java:455-457, 477-506; SRC servicelayer/CategoryService.java:143-147; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 125-147, 160-167')

e('CategoryListFragment.showDialogDeleteCategorySub', 'CategoryListFragment$3.onClick', 'FRAMEWORK',
  'the confirm delete dialog shows an OK button; the click deletes the category row and restarts the loader',
  needs_state=state_text('the row is a category (subCategId <= 0, line 455) and no account transaction uses it (CategoryService.isCategoryUsed false, line 457)', ('data',)),
  evidence='SRC common/CategoryListFragment.java:455-457, 477-499 (delete at 487-492, restartLoader at 497); SRC servicelayer/CategoryService.java:143-147; FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1023, 125-147, 160-167')

e('CategoryListFragment.showDialogEditCategoryName', 'CategoryListFragment$4.onClick', 'FRAMEWORK',
  'the category name dialog shows a Cancel button; the click cancels the dialog',
  evidence='SRC common/CategoryListFragment.java:560-565; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 125-147, 160-167')

e('CategoryListFragment.showDialogEditCategoryName', 'CategoryListFragment$5.onClick', 'FRAMEWORK',
  'the category name dialog shows an OK button; the click inserts or updates the category and restarts the loader',
  evidence='SRC common/CategoryListFragment.java:534-559 (createNew 543, update 550, restartLoader 557); FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1023, 125-147, 160-167')

e('CategoryListFragment.showDialogEditSubCategoryName', 'CategoryListFragment$6.onClick', 'FRAMEWORK',
  'the subcategory dialog shows a Cancel button; the click cancels the dialog',
  evidence='SRC common/CategoryListFragment.java:650-655; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 125-147, 160-167')

e('CategoryListFragment.showDialogEditSubCategoryName', 'CategoryListFragment$7.onClick', 'FRAMEWORK',
  'the subcategory dialog shows an OK button; the click inserts or updates the subcategory row and restarts the loader',
  evidence='SRC common/CategoryListFragment.java:614-649 (returns early at 620-621; restartLoader 647); FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1023, 125-147, 160-167')

e('CategoryListFragment.showTypeSelectorDialog', 'CategoryListFragment$10.onClick', 'FRAMEWORK',
  'the type dialog shows a neutral Cancel button; the click dismisses the dialog',
  evidence='SRC common/CategoryListFragment.java:724-729 (setNeutralButton at 724); FW-SRC core/java/com/android/internal/app/AlertController.java:1029-1030, 125-147, 160-167')

e('CategoryListFragment.showTypeSelectorDialog', 'CategoryListFragment$11.onClick', 'FRAMEWORK',
  'a row of the single-choice type list is tapped (category or subcategory); the matching add dialog opens',
  evidence='SRC common/CategoryListFragment.java:707-721 (which == 0 at 714; showDialogEditCategoryName 715, showDialogEditSubCategoryName 717); FW-SRC core/java/com/android/internal/app/AlertController.java:1134-1146 (single-choice item click calls the listener at 1142)')
