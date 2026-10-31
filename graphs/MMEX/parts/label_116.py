# ================================================================== batch 116 (label_116): GeneralSettingsActivity (3), GeneralSettingsFragment (7) and its listeners $1-$4 (8), InvestmentPreferencesViewHolder (1), InvestmentSettings (8), InvestmentSettingsActivity (2): 29 methods
# Result: 28 REACHABLE, 1 UNREACHABLE (InvestmentSettings.getPreferences), 0 INCOMPLETE. Rows and reasons: graphs/MMEX/parts/label_116.md. Grep and auto_calls evidence: graphs/MMEX/parts/label_116.grep.txt.
# The brief said 35 methods. batch_116.txt has 35 lines in total: 6 comment lines and 29 method lines. The 29 method lines are labelled here.
# This file writes 2 SCREENS keys (S_GENERAL_SETTINGS and S_INVESTMENT_SETTINGS; grep of graph_def.py and parts/*.py found no key for either screen), 15 e() edges, 1 UNREACHABLE entry and 1 sup pair.
# Every other REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived; D7) and is cited in the row, not written here.

SCREENS.update({
    'S_GENERAL_SETTINGS': 'General settings screen (GeneralSettingsActivity with GeneralSettingsFragment): application language, theme, default status, default payee and the anonymous usage data switch',
    'S_INVESTMENT_SETTINGS': 'Investment settings screen (InvestmentSettingsActivity with InvestmentSettingsFragment): asset allocation threshold, quote provider and exchange rate provider',
})

# ---- GeneralSettingsActivity: the two intents that open it, then the framework's lifecycle calls

e('SettingsFragment$10.onPreferenceClick', 'GeneralSettingsActivity.<init>', 'INTENT',
  'startActivityForResult(new Intent(getActivity(), GeneralSettingsActivity.class)) from the general preference',
  gui=['Open Settings and tap the general preference'],
  evidence='SRC settings/SettingsFragment.java:226-233 (listener; Intent at 229; startActivityForResult at 230)')

e('TutorialActivity.onCloseClicked', 'GeneralSettingsActivity.<init>', 'INTENT',
  'new Intent(this, GeneralSettingsActivity.class) and startActivityForResult from the Skip control of the tutorial (@OnClick R.id.skipTextView)',
  gui=['Tap the skip control on the tutorial screen'],
  evidence='SRC tutorial/TutorialActivity.java:90-96 (@OnClick at 90; Intent at 93; startActivityForResult at 95)')

e('GeneralSettingsActivity.<init>', 'GeneralSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC settings/GeneralSettingsActivity.java:28-31')

e('GeneralSettingsActivity.onCreate', 'S_GENERAL_SETTINGS', 'ENTERS',
  'the general settings screen is shown: setSettingFragment replaces the content with GeneralSettingsFragment',
  evidence='SRC settings/GeneralSettingsActivity.java:28-31 (setSettingFragment at 30); SRC settings/BaseSettingsFragmentActivity.java:71-78')

e('GeneralSettingsActivity.onCreate', 'GeneralSettingsActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate: ActivityThread.handleResumeActivity calls performResume (same chain as CalculatorActivity.onCreate, graph_def.py:2207)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3556, 3608; FW-SRC core/java/android/app/Activity.java:7098-7107; SRC settings/GeneralSettingsActivity.java:34-38')

# ---- GeneralSettingsFragment: the fragment transaction starts it, then super.onCreate reaches onCreatePreferences

e('GeneralSettingsFragment.<init>', 'GeneralSettingsFragment.onCreate', 'LIFECYCLE',
  'the fragment transaction (replace at line 78) is committed and the framework then runs the onCreate of the new fragment',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:71-78; INFERRED androidx FragmentManager runs the fragment lifecycle after a commit (library not in the dataset)')

e('GeneralSettingsFragment.onCreate', 'GeneralSettingsFragment.onCreatePreferences', 'FRAMEWORK',
  'super.onCreate (PreferenceFragmentCompat.onCreate) calls onCreatePreferences',
  evidence='SRC settings/GeneralSettingsFragment.java:39-42 (super.onCreate at 40); INFERRED androidx PreferenceFragmentCompat.onCreate calls onCreatePreferences (library not in the dataset)')

# ---- GeneralSettingsFragment listeners: the framework calls onPreferenceChange when the user changes a value (GUI from the screen)

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$1.onPreferenceChange', 'GUI',
  'the application language list preference changes: the listener updates the summary and restarts the activity',
  gui=['Change the application language on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:62-72 (listener set at 62; setSummaryListPreference at 66; restartActivity at 68)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$2.onPreferenceChange', 'GUI',
  'the theme list preference changes: the listener restarts the activity',
  gui=['Change the theme on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:79-88 (listener set at 79; restartActivity at 84)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$3.onPreferenceChange', 'GUI',
  'the default status list preference changes: the listener updates the summary',
  gui=['Change the default status on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:96-102 (listener set at 96; setSummaryListPreference at 99)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$4.onPreferenceChange', 'GUI',
  'the default payee list preference changes: the listener updates the summary',
  gui=['Change the default payee option on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:110-116 (listener set at 110; setSummaryListPreference at 113)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment.lambda$initializeControls$0', 'GUI',
  'the anonymous usage data switch (pref_anonymous_usage) is toggled: the lambda sets the analytics opt-out',
  gui=['Toggle the anonymous usage data switch on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:122-128 (listener set at 122; setOptOut at 125)')

# ---- InvestmentSettingsActivity: the intent from the investment preference, then the lifecycle calls

e('SettingsFragment$4.onPreferenceClick', 'InvestmentSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), InvestmentSettingsActivity.class)) from the investment preference',
  gui=['Open Settings and tap the investment preference'],
  evidence='SRC settings/SettingsFragment.java:100-106 (listener; Intent at 103)')

e('InvestmentSettingsActivity.<init>', 'InvestmentSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC settings/InvestmentSettingsActivity.java:26-29')

e('InvestmentSettingsActivity.onCreate', 'S_INVESTMENT_SETTINGS', 'ENTERS',
  'the investment settings screen is shown: setSettingFragment replaces the content with InvestmentSettingsFragment',
  evidence='SRC settings/InvestmentSettingsActivity.java:26-29 (setSettingFragment at 28); SRC settings/BaseSettingsFragmentActivity.java:71-78')

# ================================================================== InvestmentSettings.getPreferences: UNREACHABLE (source and grep evidence)

UNREACHABLE['InvestmentSettings.getPreferences'] = ('no_trigger_in_app',
    'no caller reaches it: its only incoming auto records are receiver variants of the inherited SettingsBase get, set, getBooleanSetting and getIntSetting with receiver InvestmentSettings (the @InvestmentSettings nodes), and those variant chains have no entry, because no app code calls an inherited get, set, getBooleanSetting or getIntSetting on an InvestmentSettings receiver (every InvestmentSettings use constructs the object and calls only its own getters and setters; AppSettings.getInvestmentSettings has no caller)',
    'settings/InvestmentSettings.java:48-50; settings/SettingsBase.java:52, 72-149; label_116.grep.txt sections 1-5',
    'SOURCE')

# ================================================================== sup (D14): the auto CALL record out of the UNREACHABLE method

sup(('InvestmentSettings.getPreferences', 'SettingsBase.getContext'))  # getPreferences has no caller (InvestmentSettings.java:49 calls getContext)

# Open point for the builder, not cut here: the generic cha records SettingsBase.get, set, getBooleanSetting and getIntSetting -> InvestmentSettings.getPreferences (SettingsBase.java:72, 84, 90, 98, 112, 116, 129, 145, 149) are owned by the SettingsBase batch. If the builder keeps them, getPreferences would look reachable from the generic SettingsBase nodes. Not run here (the builder is not run).

# ---- sup for part 116 (2026-10-30): receiver cut, no InvestmentSettings receiver runs an inherited SettingsBase accessor (no caller of the @InvestmentSettings chains; graphs/MMEX/parts/label_116.grep.txt)
sup(('SettingsBase.get(String,String)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,String)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(Integer,String)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,boolean)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getBooleanSetting(String,boolean)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,boolean)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getIntSetting', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,int)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,String)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,boolean)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getBooleanSetting(String,boolean)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getIntSetting@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(Integer,String)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,int)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,String)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,boolean)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
