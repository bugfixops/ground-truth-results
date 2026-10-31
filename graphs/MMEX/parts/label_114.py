# ================================================================== batch 114 (label_114): BehaviourSettingsFragment (13 methods), BudgetSettings (4), BudgetSettingsActivity (2), BudgetSettingsFragment (5), DatabaseSettings (3), DatabaseSettingsActivity (2)
# Result: 28 REACHABLE, 1 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_114.md). Grep evidence: graphs/MMEX/parts/label_114.grep.txt.
# The batch file header says 29 methods; its 36 lines are 29 method lines plus 7 comment lines. The 29 method lines are labelled here.
# Routes: the Settings list (SettingsFragment, anonymous classes $3, $5, $7) opens the Behaviour, Budget and Database settings activities. The activities create their fragments (auto CALL records). The fragment lifecycle edges are LIFECYCLE, as in label_005, label_010 and label_018.
# This file writes:
#   - SCREENS for S_BEHAVIOUR_SETTINGS, S_BUDGET_SETTINGS and S_DATABASE_SETTINGS (none existed in SCREENS; D9),
#   - INTENT edges into BudgetSettingsActivity.<init> and DatabaseSettingsActivity.<init> (their destinations are owned here; D1; the BehaviourSettingsActivity INTENT belongs to its own batch),
#   - LIFECYCLE edges into the three activity onCreate methods and the three fragment onCreate methods, plus the fragment chain onCreate -> onCreatePreferences -> onStart -> onStop,
#   - ENTERS edges from the two activity onCreate methods, GUI edges from S_BEHAVIOUR_SETTINGS, and one REGISTER edge for the time-picker lambda,
#   - 1 UNREACHABLE entry (BudgetSettings.setShowSimpleView) and 1 sup pair (D14).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).

SCREENS.update({
    'S_BEHAVIOUR_SETTINGS': 'Behaviour settings screen (BehaviourSettingsActivity): the preference list from preferences_behaviour.xml, with the repeating transaction check (time picker) and the bank SMS automation preferences',
    'S_BUDGET_SETTINGS': 'Budget settings screen (BudgetSettingsActivity): the preference list from preferences_budget.xml, shown by BudgetSettingsFragment',
    'S_DATABASE_SETTINGS': 'Database settings screen (DatabaseSettingsActivity): the database preference list hosted by DatabaseSettingsFragment',
})

# ---- SettingsFragment start sites (INTENT edges into this batch's activities; dst owned here, D1)

e('SettingsFragment$5.onPreferenceClick', 'BudgetSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), BudgetSettingsActivity.class)) from the budget preference',
  gui=['Open Settings and tap the budget preference'],
  evidence='SRC settings/SettingsFragment.java:114-118 (anonymous class $5 is created at line 113: auto_calls SettingsFragment.onCreate -> SettingsFragment$5.<init>)')

e('SettingsFragment$7.onPreferenceClick', 'DatabaseSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), DatabaseSettingsActivity.class)) from the database preference',
  gui=['Open Settings and tap the database preference'],
  evidence='SRC settings/SettingsFragment.java:140-144 (anonymous class $7 is created at line 139: auto_calls SettingsFragment.onCreate -> SettingsFragment$7.<init>)')

# ---- BudgetSettingsActivity

e('BudgetSettingsActivity.<init>', 'BudgetSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_004 AboutActivity)',
  evidence='SRC settings/BudgetSettingsActivity.java:19-30; FW-SRC core/java/android/app/ActivityThread.java:2724-2731 (as cited in label_004, not read in this batch)')

e('BudgetSettingsActivity.onCreate', 'S_BUDGET_SETTINGS', 'ENTERS',
  'the Budget settings screen is shown',
  evidence='SRC settings/BudgetSettingsActivity.java:19-30 (setSettingFragment(new BudgetSettingsFragment()) at line 28)')

# ---- BudgetSettingsFragment (fragment lifecycle; library source not read: INFERRED)

e('BudgetSettingsFragment.<init>', 'BudgetSettingsFragment.onCreate', 'LIFECYCLE',
  'BaseSettingsFragmentActivity.setSettingFragment replaces the content with the fragment (line 78) and commits the transaction (line 91); the FragmentManager then calls onCreate',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:70-92; SRC settings/BudgetSettingsActivity.java:19-30; INFERRED androidx Fragment lifecycle (library source not read; the same pattern as label_018)')

e('BudgetSettingsFragment.onCreate', 'BudgetSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/BudgetSettingsFragment.java:19-60 (onCreatePreferences inflates R.xml.preferences_budget)')

e('BudgetSettingsFragment.onCreatePreferences', 'BudgetSettingsFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after the preference view is created (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/BudgetSettingsFragment.java:19-60')

e('BudgetSettingsFragment.onStart', 'BudgetSettingsFragment.onStop', 'LIFECYCLE',
  'the user leaves the Budget settings screen and the framework stops the fragment (onResume and onPause are not methods of this class, so this edge skips them; INFERRED)',
  evidence='SRC settings/BudgetSettingsFragment.java:19-60')

# ---- BehaviourSettingsFragment (the activity creates it at BehaviourSettingsActivity.java:32; that CALL is auto)

e('BehaviourSettingsFragment.<init>', 'BehaviourSettingsFragment.onCreate', 'LIFECYCLE',
  'BehaviourSettingsActivity.onCreate calls setSettingFragment (line 32): the fragment is committed (BaseSettingsFragmentActivity.java:78, 91) and the FragmentManager then calls onCreate (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/BehaviourSettingsActivity.java:19-40; SRC settings/BaseSettingsFragmentActivity.java:70-92; SRC settings/BehaviourSettingsFragment.java:39-166')

e('BehaviourSettingsFragment.onCreate', 'BehaviourSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read); onCreatePreferences then calls initializeNotificationTime and initializeSmsAutomation (lines 57-58)',
  evidence='SRC settings/BehaviourSettingsFragment.java:45-59')

e('BehaviourSettingsFragment.onCreatePreferences', 'BehaviourSettingsFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after the preference view is created (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/BehaviourSettingsFragment.java:52-66')

e('BehaviourSettingsFragment.onStart', 'BehaviourSettingsFragment.onStop', 'LIFECYCLE',
  'the user leaves the Behaviour settings screen and the framework stops the fragment (onResume and onPause are not methods of this class, so this edge skips them; INFERRED)',
  evidence='SRC settings/BehaviourSettingsFragment.java:62-73')

# ---- BehaviourSettingsFragment click listeners and the time-picker callback

e('S_BEHAVIOUR_SETTINGS', 'BehaviourSettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the repeating transaction check preference (PreferenceConstants.PREF_REPEATING_TRANSACTION_CHECK, line 78): the listener calls showTimePicker',
  evidence='SRC settings/BehaviourSettingsFragment.java:77-89 (listener at 81, onPreferenceClick at 83, showTimePicker call at 84, setOnPreferenceClickListener at 88)')

e('S_BEHAVIOUR_SETTINGS', 'BehaviourSettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the bank SMS automation preference (PreferenceConstants.PREF_SMS_AUTOMATIC_TRANSACTIONS, line 122): the listener checks the RECEIVE_SMS permission inside an SDK_INT >= 23 test (line 132) or turns the setting off',
  evidence='SRC settings/BehaviourSettingsFragment.java:118-164 (listener at 126, onPreferenceClick at 129-161, setBankSmsTrans at 154); the minSdk value was not read, so the SDK_INT test is not resolved')

e('BehaviourSettingsFragment.showTimePicker', 'BehaviourSettingsFragment.lambda$showTimePicker$0', 'REGISTER',
  'showTimePicker passes the lambda to a new TimePickerDialog (lines 101-106) and shows it (line 114); the dialog calls the lambda when the user sets the time',
  evidence='SRC settings/BehaviourSettingsFragment.java:91-115 (lambda at 101-104, setNotificationTime at 103)')

# ---- UNREACHABLE (D14 cut of its one outgoing auto record)

UNREACHABLE['BudgetSettings.setShowSimpleView'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration (BudgetSettings.java:45) in the whole source root, and no auto_calls.json record has it as dst; its one outgoing record (-> SettingsBase.set(Integer,boolean)@BudgetSettings, line 46) is cut by sup below',
    'settings/BudgetSettings.java:45-47; label_114.grep.txt section A',
    'SOURCE')

sup(('BudgetSettings.setShowSimpleView', 'SettingsBase.set(Integer,boolean)@BudgetSettings'))  # setShowSimpleView has no caller (BudgetSettings.java:46)

# ---- DatabaseSettingsActivity

e('DatabaseSettingsActivity.<init>', 'DatabaseSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_004 AboutActivity)',
  evidence='SRC settings/DatabaseSettingsActivity.java:19-30; FW-SRC core/java/android/app/ActivityThread.java:2724-2731 (as cited in label_004, not read in this batch)')

e('DatabaseSettingsActivity.onCreate', 'S_DATABASE_SETTINGS', 'ENTERS',
  'the Database settings screen is shown',
  evidence='SRC settings/DatabaseSettingsActivity.java:19-30 (setSettingFragment(new DatabaseSettingsFragment()) at line 28)')
