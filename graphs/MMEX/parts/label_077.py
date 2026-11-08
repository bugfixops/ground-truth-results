# ================================================================== batch 077 (label_077): HomeFragment, 40 methods (graphs/MMEX/scratch/batches/batch_077.txt)
# Rows, printed lines and counts: graphs/MMEX/parts/label_077.md. No grep file: every row is REACHABLE, so no library or generated class is UNREACHABLE.
# Edges written here: the framework routes into HomeFragment (commit in MainActivity.initHomeFragment, activity lifecycle super calls, loaders,
# options menu, EventBus register and post, the Icepick reflection helper) and the user taps on the home screen (one new page, S_HOME).
# CALL edges come from auto_calls.json and are not written here (D7).
# The page S_HOME is new: no key for the home screen exists in SCREENS (grep of graph_def.py and parts). Its ENTERS edge belongs to batch 080 (MainActivity).
# UNREACHABLE: none. sup(): none (no auto CALL caller of a method in this batch is UNREACHABLE).

SCREENS.update({'S_HOME': 'The home screen: MainActivity shows HomeFragment with the account list, the + button, the search action, the account row menu and, when no account exists, the welcome view with Settings and Add account'})

# ---- commit in MainActivity.initHomeFragment: the framework runs the fragment lifecycle (MainActivity.java:1312-1322)
e('MainActivity.initHomeFragment', 'HomeFragment.onCreate', 'FRAMEWORK',
  'the fragment transaction commits (MainActivity.java:1320-1322) and the framework runs the fragment lifecycle, starting with onCreate',
  guard='no fragment with the HomeFragment tag is in the manager yet (MainActivity.java:1312-1313)',
  evidence='SRC home/MainActivity.java:1308-1322; SRC home/HomeFragment.java:148-165; INFERRED androidx FragmentManager runs onCreate after the commit (library not read)')

e('MainActivity.initHomeFragment', 'HomeFragment.onCreateView', 'FRAMEWORK',
  'after onCreate the framework inflates the fragment view through onCreateView (commit at MainActivity.java:1320-1322)',
  guard='no fragment with the HomeFragment tag is in the manager yet (MainActivity.java:1312-1313)',
  evidence='SRC home/MainActivity.java:1308-1322; SRC home/HomeFragment.java:167-170; INFERRED androidx FragmentManager (library not read)')

e('HomeFragment.onCreateView', 'HomeFragment.onViewCreated', 'FRAMEWORK',
  'the framework calls onViewCreated once onCreateView has returned the view',
  evidence='SRC home/HomeFragment.java:167-196, 198-203; INFERRED androidx Fragment lifecycle (library not read)')

e('HomeFragment.onCreate', 'HomeFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) (HomeFragment.java:158) makes the framework call onCreateOptionsMenu when the activity builds its options menu',
  evidence='SRC home/HomeFragment.java:158, 354-358; INFERRED androidx options menu dispatch (library not read); pattern label_073.py (PayeeListFragment.onActivityCreated to onCreateOptionsMenu)')

# ---- activity lifecycle: the super calls in MainActivity dispatch to the fragments
e('MainActivity.onStart', 'HomeFragment.onStart', 'FRAMEWORK',
  'MainActivity.onStart calls super.onStart (MainActivity.java:249) and the framework dispatches onStart to the fragments in the manager',
  evidence='SRC home/MainActivity.java:247-249; SRC home/HomeFragment.java:205-210; INFERRED androidx FragmentActivity dispatch (library not read); pattern graph_def.py:2071 (SearchActivity.onResume to AllDataListFragment.onResume)')

e('MainActivity.onResume', 'HomeFragment.onResume', 'FRAMEWORK',
  'super.onResume (MainActivity.java:273, inside try 272-276) dispatches onResume to the fragments',
  evidence='SRC home/MainActivity.java:271-276; SRC home/HomeFragment.java:378-401; INFERRED androidx FragmentActivity dispatch (library not read); pattern graph_def.py:2071')

e('MainActivity.onSaveInstanceState', 'HomeFragment.onSaveInstanceState', 'FRAMEWORK',
  'super.onSaveInstanceState (MainActivity.java:427) makes the framework save the fragment state through onSaveInstanceState',
  evidence='SRC home/MainActivity.java:423-428; SRC home/HomeFragment.java:482-486; INFERRED androidx FragmentManager saves fragment state (library not read)')

e('HomeFragment.onResume', 'HomeFragment.onStop', 'LIFECYCLE',
  'the user leaves the screen: the framework stops the fragment after it has resumed (same pattern as label_010.py:43)',
  evidence='SRC home/HomeFragment.java:212-217, 378-401; INFERRED androidx Fragment lifecycle (library not read)')

# ---- EventBus: register in onStart, delivery from the balance dialog
e('HomeFragment.onStart', 'HomeFragment.onEvent', 'REGISTER',
  'EventBus.register(this) in onStart (line 209) subscribes the @Subscribe onEvent(AmountEnteredEvent) method until onStop unregisters it',
  evidence='SRC home/HomeFragment.java:205-217, 490-491; pattern label_010.py:57 (AccountTransactionListFragment.onStart to onEvent, REGISTER)')

e('AmountInputDialog$7.onClick', 'HomeFragment.onEvent', 'ASYNC',
  'the OK button of the balance dialog posts AmountEnteredEvent (AmountInputDialog.java:260); EventBus delivers it to HomeFragment only while the fragment is registered (onStart to onStop)',
  guard='evalExpression() returns true (AmountInputDialog.java:258)',
  evidence='SRC common/AmountInputDialog.java:255-263; SRC home/HomeFragment.java:490-491, 205-217; pattern graph_def.py:4623 (CurrencyUIFeatures$3.onClick to onEvent, ASYNC)')

# ---- loaders: startLoaders restarts the two loaders; the framework calls the callbacks
e('HomeFragment.startLoaders', 'HomeFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader(LOADER_ACCOUNT_BILLS) and restartLoader(LOADER_INCOME_EXPENSES) (HomeFragment.java:535-536) make the LoaderManager call onCreateLoader',
  evidence='SRC home/HomeFragment.java:531-537; INFERRED androidx LoaderManager (library not read); pattern label_073.py:32-34')

e('HomeFragment.startLoaders', 'HomeFragment.onLoaderReset', 'FRAMEWORK',
  'the restart destroys the previous loader, which calls onLoaderReset on the callbacks (HomeFragment.java:535-536)',
  evidence='SRC home/HomeFragment.java:535-536; INFERRED androidx LoaderManager (library not read); pattern label_073.py:36-38')

e('HomeFragment.onCreateLoader', 'HomeFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor to onLoadFinished when the load completes',
  evidence='SRC home/HomeFragment.java:222-273, 287-288; INFERRED androidx Loader delivery (library not read); pattern label_073.py:27-29')

# ---- Icepick: the library loads the generated helper HomeFragment$$Icepick by reflection (not in the dataset)
e('HomeFragment.onCreate', 'HomeFragment$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State field: the library loads the generated helper by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at HomeFragment.java:163)',
  guard='savedInstanceState is not null (HomeFragment.java:161)',
  evidence='SRC home/HomeFragment.java:144, 161-164; the icepick library and the generated class are not in the dataset: INFERRED, source not read; pattern label_006.py:114-116')

e('HomeFragment.onCreate', 'HomeFragment$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at HomeFragment.java:163)',
  guard='savedInstanceState is not null (HomeFragment.java:161)',
  evidence='SRC home/HomeFragment.java:144, 161-164; the icepick library is not in the dataset: INFERRED, source not read; pattern label_006.py:118-120')

e('HomeFragment.onCreate', 'HomeFragment$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State field accountBalancedId',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at HomeFragment.java:163)',
  guard='savedInstanceState is not null (HomeFragment.java:161)',
  evidence='SRC home/HomeFragment.java:144, 161-164; the icepick library is not in the dataset: INFERRED, source not read; pattern label_006.py:122-124')

e('HomeFragment.onSaveInstanceState', 'HomeFragment$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick saves the @State field: the library loads the generated helper by reflection, which runs its static initialiser first if onCreate did not',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at HomeFragment.java:485)',
  evidence='SRC home/HomeFragment.java:144, 482-486; the icepick library is not in the dataset: INFERRED, source not read')

e('HomeFragment.onSaveInstanceState', 'HomeFragment$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection for the save',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at HomeFragment.java:485)',
  evidence='SRC home/HomeFragment.java:144, 482-486; the icepick library is not in the dataset: INFERRED, source not read')

e('HomeFragment.onSaveInstanceState', 'HomeFragment$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State field accountBalancedId',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at HomeFragment.java:485)',
  evidence='SRC home/HomeFragment.java:144, 482-486; the icepick library is not in the dataset: INFERRED, source not read; pattern label_006.py:126-134')

# ---- GUI edges from the one home screen S_HOME (MainActivity shows HomeFragment; its ENTERS edge is written by batch 080)
gui('S_HOME', 'HomeFragment.onOptionsItemSelected',
    'Tap the search action (menu_search) in the options menu of the home screen',
    evidence='SRC res/menu/home_menu.xml:18-28; SRC home/HomeFragment.java:360-365 (menu_search check at 364, startActivity SearchActivity at 365)')

gui('S_HOME', 'HomeFragment.onCreateContextMenu',
    'Long-press an account row in the account list (the list is registered for the context menu at line 735)',
    evidence='SRC home/HomeFragment.java:409-412, 735; INFERRED long-press on a registered view opens its context menu (Android source not read); pattern label_073.py:67-69')

gui('S_HOME', 'HomeFragment.onContextItemSelected',
    'Tap Edit, Balance account or Portfolio in the menu of an account row',
    evidence='SRC home/HomeFragment.java:450-478 (Edit 462, balance 470, portfolio 473); INFERRED the framework dispatches the chosen item to the fragment (library not read); pattern label_073.py:71-73')

gui('S_HOME', 'HomeFragment$1.onClick',
    'Tap the + floating action button at the bottom of the home screen',
    evidence='SRC res/layout/home_fragment.xml:153-165 (live fab; 167-178 commented out); SRC home/HomeFragment.java:184-193')

gui('S_HOME', 'HomeFragment$2.onClick',
    'Tap Settings in the welcome view, which is shown only when the account list is empty',
    needs_state=state_text('the account list is empty, so the welcome view with the Settings button is shown (HomeFragment.java:793-794)', ('account',)),
    evidence='SRC res/layout/welcome_layout.xml:101 (buttonSettings); SRC res/layout/home_fragment.xml:181-184; SRC home/HomeFragment.java:590-602, 792-794')
