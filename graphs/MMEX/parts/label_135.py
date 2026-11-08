# ================================================================== batch 135 (label_135): YesNoDialog (7 methods, listeners $1 and $2), the five transactions/events classes (5), TutorialAccountsFragment (3), TutorialActivity (7), TutorialActivity_ViewBinding with $1 (5), TutorialFinancialOverviewFragment (4), TutorialGlobalFragment (4), TutorialPagerAdapter (4): 39 methods
# Result: 36 REACHABLE, 3 UNREACHABLE (YesNoDialog.getPurpose, TutorialActivity_ViewBinding.unbind, TutorialPagerAdapter.getPageTitle). getPageTitle is settled as framework_never_calls on INFERRED library behaviour and is flagged for the parent to review.
# Rows and reasons: graphs/MMEX/parts/label_135.md. Grep and auto_calls evidence: graphs/MMEX/parts/label_135.grep.txt.
# This file writes 1 SCREENS key (S_TUTORIAL; grep of graph_def.py and parts/*.py found no key for it), 20 e() edges and 3 UNREACHABLE entries.
# No sup pair is written. YesNoDialog.getPurpose has no auto_calls record in either direction. TutorialActivity_ViewBinding.unbind has 0 callers and outgoing auto records only to library calls (IllegalStateException.<init>, View.setOnClickListener); those edges are never reached, so no cut is needed.
# Every other REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived; D7) and is cited in the row, not written here.
# The five event constructors have no edge here: their CALL records come from YesNoDialog$1/$2.onClick and SplitCategoriesAdapter (batch 134, interim D8).

SCREENS.update({
    'S_TUTORIAL': 'Tutorial screen (TutorialActivity): five swipeable pages (accounts, transactions, global, financial overview, sync), the Skip control and the options menu',
})

MENU_KEY = env_text('the device has a hardware menu key: this theme has no action bar, so the options menu opens only from the menu key', ('hardware',))

# ---- TutorialActivity: first-run start, lifecycle, pager, skip control, result and options menu

e('MainActivity.showTutorial', 'TutorialActivity.<init>', 'INTENT',
  'startActivity(new Intent(this, TutorialActivity.class)) with FLAG_ACTIVITY_CLEAR_TOP: the first-run tutorial, started from showPrerequisite',
  needs_state=state_text('first run: the tutorial has not been dismissed (getShowTutorial is true; the default is true, BehaviourSettings.java:86-88)', ('settings',)),
  evidence='SRC home/MainActivity.java:812-817 (showTutorial; Intent 813, startActivity 816); SRC home/MainActivity.java:184 (showPrerequisite call), 1351-1353 (isTutorialNeeded), 1478-1482 (showTutorial at 1481); SRC settings/BehaviourSettings.java:86-88; SRC AndroidManifest.xml:314-319 (no intent-filter)')

e('TutorialActivity.<init>', 'TutorialActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate); SRC tutorial/TutorialActivity.java:49-73')

e('TutorialActivity.onCreate', 'S_TUTORIAL', 'ENTERS',
  'the tutorial screen is shown: setContentView (activity_tutorial) and the pager adapter are set',
  evidence='SRC tutorial/TutorialActivity.java:55, 61-63')

e('TutorialActivity.onCreate', 'TutorialActivity_ViewBinding.<init>(TutorialActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick skip handler',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated TutorialActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC tutorial/TutorialActivity.java:57; INFERRED ButterKnife generated binding (library and generated source not read); precedent graph_def.py:409-412 (PasscodeActivity)')

e('TutorialActivity.onCreate', 'TutorialPagerAdapter.getItem', 'FRAMEWORK',
  'the ViewPager asks the adapter for the first page when the adapter is set',
  evidence='SRC tutorial/TutorialActivity.java:61-63; INFERRED androidx ViewPager and FragmentStatePagerAdapter call getItem for the first page (androidx source not read); precedent graph_def.py:225 (AboutActivity.onCreate -> AboutTabAdapter.getItem)')

e('TutorialActivity.onCreate', 'TutorialPagerAdapter.getCount', 'FRAMEWORK',
  'the ViewPager reads the page count when the adapter is set (5 pages)',
  evidence='SRC tutorial/TutorialPagerAdapter.java:63-65; SRC tutorial/TutorialActivity.java:63; INFERRED androidx PagerAdapter (library not read); precedent graph_def.py:221')

e('S_TUTORIAL', 'TutorialPagerAdapter.getItem', 'GUI',
  'swipe between the tutorial pages: the ViewPager asks for the page fragment',
  gui=['Swipe between the tutorial pages'],
  evidence='SRC tutorial/TutorialActivity.java:61-63; INFERRED androidx ViewPager calls getItem on a page change (library source not read); precedent graph_def.py:229')

e('TutorialActivity.onCloseClicked', 'TutorialActivity.onActivityResult', 'RESULT',
  'the framework delivers the result of GeneralSettingsActivity (started for result at line 95) when it finishes; GeneralSettingsActivity calls no setResult, so the result code is RESULT_CANCELED, and this handler does not check resultCode',
  guard='requestCode is REQUEST_GENERAL_PREFERENCES (TutorialActivity.java:79)',
  evidence='SRC tutorial/TutorialActivity.java:76-96; grep section 8 (no setResult or finish in settings/GeneralSettingsActivity.java and settings/BaseSettingsFragmentActivity.java); FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult calls onActivityResult)')

e('S_TUTORIAL', 'TutorialActivity_ViewBinding$1.doClick', 'GUI',
  'tap the Skip control (skipTextView): the listener attached by the generated binding calls onCloseClicked',
  gui=['Tap Skip on the tutorial screen'],
  cls='non_standard', via='ButterKnife @OnClick binding (generated class TutorialActivity_ViewBinding$1, INFERRED, library and generated source not read)',
  evidence='SRC tutorial/TutorialActivity.java:90-91 (@OnClick at 90); SRC res/layout/activity_tutorial.xml:46 (skipTextView); auto TutorialActivity_ViewBinding$1.doClick -> TutorialActivity.onCloseClicked (TutorialActivity_ViewBinding.java:34)')

e('S_TUTORIAL', 'TutorialActivity.onCreateOptionsMenu', 'GUI',
  'press the menu key: PhoneWindow.preparePanel calls the callback onCreatePanelMenu, which calls onCreateOptionsMenu (the menu is inflated at TutorialActivity.java:101)',
  gui=['Press the hardware menu key'], env=MENU_KEY,
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:1916-1918 (KEYCODE_MENU opens the options panel), 580 (preparePanel), 631 (cb.onCreatePanelMenu); FW-SRC core/java/android/app/Activity.java:3386-3390 (onCreatePanelMenu calls onCreateOptionsMenu); SRC tutorial/TutorialActivity.java:98-103; SRC res/menu/menu_tutorial.xml; SRC AndroidManifest.xml:314-319 (NoTitleBar.Fullscreen theme)')

e('S_TUTORIAL', 'TutorialActivity.onOptionsItemSelected', 'GUI',
  'tap the settings item (action_settings) in the options menu: Activity.onMenuItemSelected calls onOptionsItemSelected',
  gui=['Press the hardware menu key and tap the settings item'], env=MENU_KEY,
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3450 (onOptionsItemSelected at 3450); SRC tutorial/TutorialActivity.java:105-118 (action_settings at 113, returns true at 114)')

# ---- YesNoDialog: created in EditTransactionCommonFunctions.onTransferSelected; AlertDialog buttons dispatch to the listeners

e('YesNoDialog.<init>', 'YesNoDialog.onCreateDialog', 'LIFECYCLE',
  'the DialogFragment calls onCreateDialog when the dialog is shown (dialog.show at EditTransactionCommonFunctions.java:1459)',
  needs_state=state_text('the transaction has split categories (hasSplitCategories, EditTransactionCommonFunctions.java:1448)', ('data',)),
  evidence='SRC transactions/YesNoDialog.java:58-85; SRC transactions/EditTransactionCommonFunctions.java:1446-1460; INFERRED androidx DialogFragment calls onCreateDialog after show (library not in the dataset)')

e('YesNoDialog.onCreateDialog', 'YesNoDialog$1.onClick', 'FRAMEWORK',
  'the No (negative) button of the AlertDialog: AlertController mButtonHandler sends the click and handleMessage calls the listener',
  evidence='FW-SRC core/java/com/android/internal/app/AlertController.java:125-145 (mButtonHandler.onClick), 158-168 (handleMessage calls the OnClickListener); SRC transactions/YesNoDialog.java:76-83 (setNegativeButton at 76); auto YesNoDialog$1.onClick -> DialogNegativeClickedEvent.<init> (YesNoDialog.java:81)')

e('YesNoDialog.onCreateDialog', 'YesNoDialog$2.onClick', 'FRAMEWORK',
  'the Yes (positive) button of the AlertDialog: same AlertController path as the No button',
  evidence='FW-SRC core/java/com/android/internal/app/AlertController.java:125-145, 158-168; SRC transactions/YesNoDialog.java:68-75 (setPositiveButton at 68); auto YesNoDialog$2.onClick -> DialogPositiveClickedEvent.<init> (YesNoDialog.java:73)')

# ---- TutorialAccountsFragment, TutorialFinancialOverviewFragment, TutorialGlobalFragment: lifecycle after the constructor (D21)

e('TutorialAccountsFragment.<init>', 'TutorialAccountsFragment.onCreate', 'LIFECYCLE',
  'the fragment manager runs the fragment lifecycle after the instance is created by getItem',
  evidence='SRC tutorial/TutorialAccountsFragment.java:34-41; INFERRED androidx FragmentStatePagerAdapter instantiates the fragment and runs its lifecycle (library not read)')

e('TutorialAccountsFragment.onCreate', 'TutorialAccountsFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC tutorial/TutorialAccountsFragment.java:39-56; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialFinancialOverviewFragment.<init>', 'TutorialFinancialOverviewFragment.onCreate', 'LIFECYCLE',
  'the fragment manager runs the fragment lifecycle after the instance is created by newInstance',
  evidence='SRC tutorial/TutorialFinancialOverviewFragment.java:49-60; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialFinancialOverviewFragment.onCreate', 'TutorialFinancialOverviewFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC tutorial/TutorialFinancialOverviewFragment.java:53-67; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialGlobalFragment.<init>', 'TutorialGlobalFragment.onCreate', 'LIFECYCLE',
  'the fragment manager runs the fragment lifecycle after the instance is created by newInstance',
  evidence='SRC tutorial/TutorialGlobalFragment.java:50-61; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialGlobalFragment.onCreate', 'TutorialGlobalFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC tutorial/TutorialGlobalFragment.java:54-68; INFERRED androidx Fragment lifecycle (library not read)')

# ---- UNREACHABLE: no caller in the source root, no auto_calls record

UNREACHABLE['YesNoDialog.getPurpose'] = ('no_trigger_in_app',
  'no caller in the source root: the grep matches only the definition, the getter has no auto_calls record, and nothing reads mPurpose through it',
  'SRC transactions/YesNoDialog.java:53-55; label_135.grep.txt section 1',
  'SOURCE')

UNREACHABLE['TutorialActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this) at TutorialActivity.java:57 discards the returned Unbinder, TutorialActivity has no onDestroy, and no caller exists in the source root (label_135.grep.txt section 2) or in auto_calls.json (0 callers)',
  'SRC tutorial/TutorialActivity.java:57; label_135.grep.txt section 2; python-printed auto_calls query (0 callers)',
  'INFERRED')

UNREACHABLE['TutorialPagerAdapter.getPageTitle'] = ('framework_never_calls',
  'the framework calls getPageTitle only from a title widget (TabLayout, PagerTitleStrip, PagerTabStrip; androidx source not read, INFERRED); the tutorial layout has no title widget and no class in the tutorial package creates one, so the call never happens',
  'SRC tutorial/TutorialPagerAdapter.java:68-70; SRC res/layout/activity_tutorial.xml (widget tags); label_135.grep.txt section 3',
  'INFERRED')
