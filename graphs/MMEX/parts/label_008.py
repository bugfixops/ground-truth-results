# ================================================================== batch 008 (label_008): AccountListActivity, AccountListFragment (with its $1, $2, $3 listeners), AccountEditViewHolder and its ButterKnife binding, AccountSpinnerAdapter
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_008.md.
# Every edge below has a batch 008 method as its destination. GUI edges start on the page S_ACCOUNT_LIST; ENTERS edges end on it.
# Already in auto_calls.json, so not written here: AccountListActivity.onCreate -> AccountListFragment.<init> (AccountListActivity.java:47),
# AccountEditActivity.initializeControls -> AccountEditViewHolder.<init> (AccountEditActivity.java:294), the AccountListFragment action calls
# (startAccountListEditActivity, showDeleteConfirmationDialog, setResult), the $1/$2/$3 constructors, and the BaseListFragment calls that reach getSubTitle.
# AccountSpinnerAdapter is never instantiated in the app, so it has no incoming edge and no sup pair is needed.

SCREENS.update({
    'S_ACCOUNT_LIST': 'Account list: AccountListActivity (another app sends PICK or EDIT) or the Accounts screen opened from the navigation drawer; account names, the search box, the + button, and an Edit or Delete menu for each account',
})

# ---- AccountListActivity: started only by another app (exported PICK or EDIT intent, manifest 198-203); no in-app start (label_008.grep.txt)

e('S_ENTRY', 'AccountListActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported AccountListActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to AccountListActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:198-203; FW-SRC core/java/android/app/ActivityThread.java:2665-2672; FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

e('S_ENTRY', 'AccountListActivity.<clinit>', 'ENTRY',
  'the first AccountListActivity instance (the exported-intent start above) initialises the class; FRAGMENTTAG (line 37) is computed at run time, so the static initialiser runs',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to AccountListActivity (exported=true)', ('other_app',)),
  evidence='SRC account/AccountListActivity.java:35-37; SRC AndroidManifest.xml:198-203; INFERRED the JVM runs a static initialiser before the first instance (Java language rule, not read from a source)')

e('AccountListActivity.<init>', 'AccountListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC account/AccountListActivity.java:39-57')

e('AccountListActivity.onCreate', 'S_ACCOUNT_LIST', 'ENTERS',
  'the account list is shown in the activity',
  evidence='SRC account/AccountListActivity.java:47-55')

e('AccountListActivity.onCreate', 'AccountListFragment.onActivityCreated', 'FRAMEWORK',
  'the fragment is committed (line 55); the FragmentManager calls onActivityCreated later, in the fragment lifecycle',
  evidence='SRC account/AccountListActivity.java:47-55; INFERRED androidx FragmentManager calls onActivityCreated after the transaction commits (library not read)')

gui('S_ACCOUNT_LIST', 'AccountListActivity.onKeyUp', 'Press Back while the activity opened by another app is in front',
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3272; FW-SRC core/java/android/view/KeyEvent.java:2709-2715; SRC account/AccountListActivity.java:59-68')

# ---- AccountListFragment: the drawer route (MainActivity drawer item menu_account, auto_calls) -> showFragment(Class) -> reflection

e('MainActivity.showFragment(Class)', 'AccountListFragment.<init>', 'CALL',
  'the drawer item Accounts (R.id.menu_account) calls showFragment(AccountListFragment.class), which creates the fragment with classFragment.newInstance()',
  cls='non_standard', via='Class.newInstance reflection in MainActivity.showFragment(Class) (MainActivity.java:743)',
  gui=['Open the navigation drawer and tap Accounts'],
  evidence='SRC home/MainActivity.java:633-634 (case R.id.menu_account); SRC home/MainActivity.java:734-752 (newInstance at 743); SRC home/MainActivity.java:863-866 (drawer item menu_account)')

e('MainActivity.showFragment_Internal', 'AccountListFragment.onActivityCreated', 'FRAMEWORK',
  'the drawer fragment is committed (replace at 1460-1462, commit at 1466); the FragmentManager calls onActivityCreated later, in the fragment lifecycle',
  evidence='SRC home/MainActivity.java:1446-1466; INFERRED androidx FragmentManager calls onActivityCreated after the transaction commits (library not read)')

e('AccountListFragment.onActivityCreated', 'S_ACCOUNT_LIST', 'ENTERS',
  'the Accounts list is shown in the main screen (the fragment is set up in onActivityCreated)',
  evidence='SRC account/AccountListFragment.java:63-96')

# ---- AccountListFragment: loader lifecycle (androidx LoaderManager; library not read)

e('AccountListFragment.onActivityCreated', 'AccountListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader starts the account loader and the LoaderManager calls onCreateLoader; restartLoader (lines 216 and 277) calls it again after a search or a delete',
  evidence='SRC account/AccountListFragment.java:90, 216, 277; INFERRED androidx LoaderManager.initLoader calls the LoaderCallbacks (library not read)')

e('AccountListFragment.onCreateLoader', 'AccountListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC account/AccountListFragment.java:157-175; SRC common/MmxCursorLoader.java:32; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('AccountListFragment.onLoadFinished', 'AccountListFragment.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (fragment destroyed or loader restarted) and the LoaderManager calls onLoaderReset',
  evidence='SRC account/AccountListFragment.java:178-184; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read; FW-SRC has no LoaderManager.java)')

# ---- AccountListFragment: the context menu (registered in onActivityCreated, line 84)

e('AccountListFragment.onListItemClick', 'AccountListFragment.onCreateContextMenu', 'FRAMEWORK',
  'openContextMenu(v) (line 259) asks the framework to show the context menu; the framework calls the fragment, the listener set by registerForContextMenu (line 84), to fill the menu',
  evidence='SRC account/AccountListFragment.java:84, 255-260; FW-SRC core/java/android/app/Activity.java:3791-3793; FW-SRC core/java/android/view/View.java:6448-6449 and 12578-12588; FW-SRC core/java/android/view/ViewGroup.java:860-866; FW-SRC core/java/com/android/internal/policy/DecorView.java:796-797 (window-level path after that not read); FW-SRC core/java/android/app/Fragment.java:1937-1938 (registerForContextMenu sets the listener; androidx version INFERRED)')

gui('S_ACCOUNT_LIST', 'AccountListFragment.onContextItemSelected', 'Tap Edit or Delete in the menu of an account row',
  evidence='SRC account/AccountListFragment.java:114-152; FW-SRC core/java/android/app/Activity.java:3466-3473 (FEATURE_CONTEXT_MENU: onContextItemSelected at 3470, then mFragments.dispatchContextItemSelected at 3473); INFERRED androidx FragmentManager dispatches the item to the fragment (library not read)')

# ---- AccountListFragment: user actions on the list

gui('S_ACCOUNT_LIST', 'AccountListFragment.onListItemClick', 'Tap an account row',
  evidence='SRC account/AccountListFragment.java:255-260; auto_calls record AbsListFragment$1.onItemClick -> AccountListFragment.onListItemClick (AbsListFragment.java:44)')

gui('S_ACCOUNT_LIST', 'AccountListFragment.onFloatingActionButtonClicked', 'Tap the + button',
  evidence='SRC account/AccountListFragment.java:94-95, 250-252; auto_calls record BaseListFragment$2.onClick -> AccountListFragment.onFloatingActionButtonClicked (BaseListFragment.java:244)')

gui('S_ACCOUNT_LIST', 'AccountListFragment.onQueryTextChange', 'Type in the search box of the account list',
  evidence='SRC account/AccountListFragment.java:214-218; auto_calls record BaseListFragment.onPreQueryTextChange@AccountListFragment -> AccountListFragment.onQueryTextChange (BaseListFragment.java:226)')

# ---- AccountListFragment$1, $2, $3: the dialog listeners of the delete flow
# $1 = OK of the in-use message (captures only the fragment, descriptor (AccountListFragment)V); $2 = Cancel of the delete confirmation
# (captures only the fragment); $3 = OK of the delete confirmation (captures accountId, descriptor (AccountListFragment,I)V, and calls AccountRepository.delete).
# The auto_calls line table puts the $3 constructor at line 268 and the $2 constructor at line 269; the source order is the listener order, so the table is not used for the citation.

gui('S_ACCOUNT_LIST', 'AccountListFragment$1.onClick', 'Tap Delete on an account that is used, then tap OK on the message',
  evidence='SRC account/AccountListFragment.java:131-145 (isAccountUsed 133; OK listener 138-143; dismiss 141); method_list descriptor AccountListFragment$1.<init>(Lcom/money/manager/ex/account/AccountListFragment;)V')

gui('S_ACCOUNT_LIST', 'AccountListFragment$2.onClick', 'Tap Delete on an account, then tap Cancel on the confirmation',
  evidence='SRC account/AccountListFragment.java:280-285 (negative listener; cancel at 283); method_list descriptor AccountListFragment$2.<init>(Lcom/money/manager/ex/account/AccountListFragment;)V')

gui('S_ACCOUNT_LIST', 'AccountListFragment$3.onClick', 'Tap Delete on an account, then tap OK on the confirmation',
  evidence='SRC account/AccountListFragment.java:269-279 (positive listener; delete 273; restart 277); auto_calls record AccountListFragment$3.onClick -> AccountRepository.delete (AccountListFragment.java:273); method_list descriptor AccountListFragment$3.<init>(Lcom/money/manager/ex/account/AccountListFragment;I)V')

# ---- AccountEditViewHolder: the ButterKnife binding is built by reflection (library and generated source not read)

e('AccountEditViewHolder.<init>', 'AccountEditViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, parent) constructs the generated binding for this holder',
  cls='non_standard', via='ButterKnife.bind(this, parent) (library): the generated AccountEditViewHolder_ViewBinding is constructed by reflection (INFERRED, library and generated source not read)',
  evidence='SRC account/AccountEditViewHolder.java:38-40; method_list descriptor AccountEditViewHolder_ViewBinding.<init>(Lcom/money/manager/ex/account/AccountEditViewHolder;Landroid/view/View;)V; INFERRED generated class not in the source root')

# ================================================================== UNREACHABLE (batch 008)

UNREACHABLE['AccountEditViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this, parent) at AccountEditViewHolder.java:39 discards the returned Unbinder, the holder never calls unbind, and no caller record exists in auto_calls.json (label_008.grep.txt)',
  'SRC account/AccountEditViewHolder.java:38-40; label_008.grep.txt; python-printed auto_calls query (0 callers)',
  'INFERRED')

UNREACHABLE['AccountSpinnerAdapter.<init>'] = ('no_trigger_in_app',
  'the class is never instantiated in the app: the only mention outside its own file is the todo comment at SingleAccountWidgetConfigureActivity.java:142, so the constructor has no caller (label_008.grep.txt)',
  'SRC account/AccountSpinnerAdapter.java:30; SRC widget/SingleAccountWidgetConfigureActivity.java:142; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getCount'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:76; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getDropDownView'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:45; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getItem'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:88; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getItemId'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:99; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getItemViewType'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:149; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getView'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:133; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getViewTypeCount'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:168; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.hasStableIds'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:110; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.isEmpty'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:179; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.registerDataSetObserver'] = ('no_trigger_in_app',
  'DataSetObserver registration on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:55; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.unregisterDataSetObserver'] = ('no_trigger_in_app',
  'DataSetObserver unregistration on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:66; label_008.grep.txt',
  'SOURCE')
