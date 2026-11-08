# batch 019 (label_019): BudgetViewModel (9 methods), BudgetsActivity (11) and BudgetSelectedEvent (1); rows and printed lines: graphs/MMEX/parts/label_019.md.
# Page S_BUDGETS is defined here (no budget-list page exists yet). CALL edges come from auto_calls.json, so none are written here; the BudgetViewModel methods are reached through BudgetEditActivity (another batch). Framework and EventBus claims are INFERRED where the library source was not read; grep evidence is in label_019.grep.txt.

SCREENS.update({
    'S_BUDGETS': 'Budgets screen (BudgetsActivity): the budget list (BudgetListFragment) opened from the navigation drawer; tapping a budget row shows its detail, and the Up arrow closes the screen',
})

# ---- BudgetsActivity: started from the navigation drawer, then the framework calls onCreate

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'BudgetsActivity.<init>', 'INTENT',
  'case R.id.menu_budgets: startActivity(new Intent(this, BudgetsActivity.class))',
  gui=['Open the navigation drawer and tap Budgets'],
  evidence='SRC home/MainActivity.java:589, 654-657; SRC home/MainActivity.java:1090-1093 (drawer item menu_budgets); SRC res/values/strings.xml:561; SRC AndroidManifest.xml:324-326 (no intent filter)')

e('BudgetsActivity.<init>', 'BudgetsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC budget/BudgetsActivity.java:41-53')

e('BudgetsActivity.onCreate', 'S_BUDGETS', 'ENTERS',
  'the budget list is shown: the layout is set and createFragments adds BudgetListFragment to R.id.fragmentMain',
  evidence='SRC budget/BudgetsActivity.java:45, 52, 106-130 (fragment transaction at 120-122)')

e('BudgetsActivity.onCreate', 'BudgetsActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options panel: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu (the toolbar becomes the action bar at line 47)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu called at 3388); SRC budget/BudgetsActivity.java:47, 57-63; INFERRED AppCompat decides when the panel is prepared (androidx not in fw_src)')

e('BudgetsActivity.onCreate', 'BudgetsActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state from the pause path: performPauseActivity calls callCallActivityOnSaveInstanceState, which calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/Activity.java:1495-1501 (onSaveInstanceState called at 1496); SRC budget/BudgetsActivity.java:87-92')

# ---- Up arrow: the toolbar sends android.R.id.home to the options callback

e('S_BUDGETS', 'BudgetsActivity.onOptionsItemSelected', 'GUI',
  'tap the Up (back) arrow in the toolbar: the framework passes android.R.id.home to onOptionsItemSelected; the override calls super, which finishes the activity',
  gui=['Tap the Up (back) arrow at the left of the Budgets toolbar'],
  evidence='SRC budget/BudgetsActivity.java:50 (setDisplayHomeAsUpEnabled), 66-78 (override, super at 77); SRC common/MmxBaseFragmentActivity.java:107-116 (home branch for the Up arrow, finish at 114); FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED AppCompat toolbar navigation click sends android.R.id.home to the window callback (androidx not in fw_src)')

# ---- EventBus: MmxBaseFragmentActivity.onStart registers the activity; BudgetsActivity.onEvent is the @Subscribe method

e('MmxBaseFragmentActivity.onStart', 'BudgetsActivity.onEvent', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by BudgetsActivity); tapping a budget row posts BudgetSelectedEvent (BudgetListFragment.onListItemClick), and EventBus calls onEvent until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141, @Subscribe on BudgetsActivity.onEvent (line 82); library source not read, INFERRED',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (onStart register at 141; onStop unregister at 146); SRC budget/BudgetsActivity.java:82-85 (@Subscribe at 82); SRC budget/BudgetListFragment.java:208-215 (post at 215); INFERRED EventBus library source not read')
