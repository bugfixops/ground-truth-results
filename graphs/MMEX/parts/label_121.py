# ================================================================== batch 121 (label_121): SettingsFragment (6 methods), SettingsFragment$1 to $10 (20), SyncPreferences (13); 39 methods
# Result: 38 REACHABLE, 1 UNREACHABLE, 0 INCOMPLETE (rows: graphs/MMEX/parts/label_121.md). Grep evidence: graphs/MMEX/parts/label_121.grep.txt.
# This file writes:
#   - LIFECYCLE from BaseSettingsFragmentActivity.setSettingFragment to SettingsFragment.onCreate (fragment commit; the pattern of label_115),
#   - LIFECYCLE from SettingsFragment.onCreate to onCreatePreferences (framework dispatch through PreferenceFragmentCompat.onCreate),
#   - RESULT from SettingsFragment$10.onPreferenceClick to SettingsFragment.onActivityResult (startActivityForResult at line 230),
#   - 10 GUI edges from S_SETTINGS to SettingsFragment$1..$10.onPreferenceClick (D6),
#   - 1 UNREACHABLE entry (SyncPreferences.clear) and 1 sup pair (D14).
# S_SETTINGS is not redefined here: label_120.py line 12 defines it (D9). No S_SETTINGS SCREENS entry is written by this file.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).
# INTENT edges from the listeners to activities are not written here: their destinations belong to other batches (D1).

# ---- the settings list fragment: setSettingFragment commits it, the FragmentManager runs onCreate, then onCreatePreferences

e('SettingsFragment.<init>', 'SettingsFragment.onCreate', 'LIFECYCLE',
  'the settings list fragment is committed by SettingsActivity.showFragment (line 71); the FragmentManager then runs onCreate of SettingsFragment',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:71-92 (tx.replace 78, tx.commit 91); SRC settings/SettingsActivity.java:68-71 (new SettingsFragment at 68, setSettingFragment at 71); INFERRED androidx FragmentManager (library not in the dataset; source not read)')

e('SettingsFragment.onCreate', 'SettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'super.onCreate (line 48) is PreferenceFragmentCompat.onCreate, which calls the overridden onCreatePreferences (framework dispatch; INFERRED from the framework contract)',
  evidence='SRC settings/SettingsFragment.java:48 (super.onCreate), 195-198 (empty body); auto_calls.json framework_calls SettingsFragment.onCreate lists PreferenceFragmentCompat.onCreate')

# ---- the General settings listener returns its result to onActivityResult

e('SettingsFragment$10.onPreferenceClick', 'SettingsFragment.onActivityResult', 'RESULT',
  'startActivityForResult (line 230) starts GeneralSettingsActivity with REQUEST_GENERAL_PREFERENCES; the framework delivers the result to onActivityResult, which calls getActivity().recreate() (line 206)',
  evidence='SRC settings/SettingsFragment.java:226-232 (start at 230), 200-208 (onActivityResult; recreate at 206); precedent DatabaseSettingsFragment.requestBackup -> onActivityResult (graph_def.py line 10378)')

# ---- GUI edges from the settings list page (S_SETTINGS, label_120.py line 12) to each listener (D6)

e('S_SETTINGS', 'SettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the per-database preference (R.string.pref_per_database, line 54): the listener starts SettingsActivity with EXTRA_FRAGMENT = PerDatabaseFragment (lines 62-64); the INTENT edge to SettingsActivity.<init> is batch 120\'s',
  evidence='SRC settings/SettingsFragment.java:59-67 (listener set at 59, onPreferenceClick 61, putExtra 63, startActivity 64)')

e('S_SETTINGS', 'SettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the look and feel preference (PreferenceConstants.PREF_LOOK_FEEL, line 70): the listener starts LookFeelSettingsActivity (line 77)',
  evidence='SRC settings/SettingsFragment.java:70-80 (listener set at 74, onPreferenceClick 76, startActivity 77)')

e('S_SETTINGS', 'SettingsFragment$3.onPreferenceClick', 'GUI',
  'the user taps the behaviour preference (R.string.pref_behaviour, line 83): the listener starts BehaviourSettingsActivity (line 90)',
  evidence='SRC settings/SettingsFragment.java:83-93 (listener set at 87, onPreferenceClick 89, startActivity 90)')

e('S_SETTINGS', 'SettingsFragment$4.onPreferenceClick', 'GUI',
  'the user taps the investment preference (R.string.pref_investment, line 96): the listener starts InvestmentSettingsActivity (line 103)',
  evidence='SRC settings/SettingsFragment.java:96-106 (listener set at 100, onPreferenceClick 102, startActivity 103)')

e('S_SETTINGS', 'SettingsFragment$5.onPreferenceClick', 'GUI',
  'the user taps the budget preference (R.string.pref_budget, line 109): the listener starts BudgetSettingsActivity (line 116)',
  evidence='SRC settings/SettingsFragment.java:109-119 (listener set at 113, onPreferenceClick 115, startActivity 116)')

e('S_SETTINGS', 'SettingsFragment$6.onPreferenceClick', 'GUI',
  'the user taps the security preference (PreferenceConstants.PREF_SECURITY, line 122): the listener starts SecuritySettingsActivity (line 129)',
  evidence='SRC settings/SettingsFragment.java:122-132 (listener set at 126, onPreferenceClick 128, startActivity 129)')

e('S_SETTINGS', 'SettingsFragment$7.onPreferenceClick', 'GUI',
  'the user taps the database preference (PreferenceConstants.PREF_DATABASE, line 135): the listener starts DatabaseSettingsActivity (line 142)',
  evidence='SRC settings/SettingsFragment.java:135-145 (listener set at 139, onPreferenceClick 141, startActivity 142)')

e('S_SETTINGS', 'SettingsFragment$8.onPreferenceClick', 'GUI',
  'the user taps the synchronisation preference (R.string.pref_synchronization, line 149): the listener starts SyncPreferencesActivity (line 156); the INTENT edge is batch 122\'s',
  evidence='SRC settings/SettingsFragment.java:149-160 (listener set at 153, onPreferenceClick 155, startActivity 156)')

e('S_SETTINGS', 'SettingsFragment$9.onPreferenceClick', 'GUI',
  'the user taps the version preference (PreferenceConstants.PREF_VERSION_NAME, line 162): the listener starts AboutActivity (line 170)',
  evidence='SRC settings/SettingsFragment.java:162-174 (listener set at 166, onPreferenceClick 169, startActivity 170)')

e('S_SETTINGS', 'SettingsFragment$10.onPreferenceClick', 'GUI',
  'the user taps the general preference (PreferenceConstants.PREF_GENERAL, line 220): the listener starts GeneralSettingsActivity with startActivityForResult (line 230); the INTENT edge is batch 116\'s',
  evidence='SRC settings/SettingsFragment.java:217-233 (listener set at 226, onPreferenceClick 228, startActivityForResult 230)')

# ---- UNREACHABLE (D14 cut of its one outgoing auto record)

UNREACHABLE['SyncPreferences.clear'] = ('no_trigger_in_app',
    'no live caller: its only caller is SyncManager.resetPreferences (SyncManager.java:257, getPreferences().clear()); resetPreferences has no live caller: its only other mention in the source root is the reset listener at SyncPreferenceFragment.java:262, which is commented out, and no auto_calls.json record has it as dst; see label_121.grep.txt section A',
    'settings/SyncPreferences.java:40-42; sync/SyncManager.java:256-258; sync/SyncPreferenceFragment.java:252-276; label_121.grep.txt section A',
    'SOURCE')

sup(('SyncPreferences.clear', 'SyncPreferences.getPreferences'))  # clear has no caller; its one outgoing record (SyncPreferences.java:41) is cut (D14)
sup(('SyncManager.resetPreferences', 'SyncPreferences.clear'))  # resetPreferences has no live caller (D14); its call to clear (SyncManager.java:257) is cut
