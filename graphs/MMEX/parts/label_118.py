# ================================================================== batch 118 (label_118): LookFeelPreferenceFragment (15 methods), LookFeelSettingsActivity (2)
# Result: 17 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_118.md). Grep evidence: graphs/MMEX/parts/label_118.grep.txt.
# Route: SettingsFragment$2 (Settings list, Look and feel item) -INTENT-> LookFeelSettingsActivity.<init> -LIFECYCLE-> onCreate -ENTERS-> S_LOOK_FEEL.
# The activity's onCreate builds the fragment (auto CALL record), which runs onCreate and creates six listeners (auto CALL records).
# GUI edges from S_LOOK_FEEL go to the six onPreferenceChange listeners (D6).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).
# No UNREACHABLE entries and no sup pairs in this batch.

SCREENS.update({
    'S_LOOK_FEEL': 'Look and feel settings screen (LookFeelSettingsActivity hosts LookFeelPreferenceFragment): the account visibility, transaction period, font and font size preferences from preferences_look_and_feel.xml',
})

# ---- Settings list start site (INTENT edge into this batch's activity; dst owned here, D1)

e('SettingsFragment$2.onPreferenceClick', 'LookFeelSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), LookFeelSettingsActivity.class)) from the look and feel preference',
  gui=['Open Settings and tap the look and feel preference'],
  evidence='SRC settings/SettingsFragment.java:74-80 (start at line 77; anonymous class $2 is created at line 74: auto_calls.json SettingsFragment.onCreate -> SettingsFragment$2.<init>, record at line 1575)')

# ---- LookFeelSettingsActivity

e('LookFeelSettingsActivity.<init>', 'LookFeelSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_114 BudgetSettingsActivity)',
  evidence='SRC settings/LookFeelSettingsActivity.java:22-29')

e('LookFeelSettingsActivity.onCreate', 'S_LOOK_FEEL', 'ENTERS',
  'the look and feel settings screen is shown',
  evidence='SRC settings/LookFeelSettingsActivity.java:25-29 (setSettingFragment(new LookFeelPreferenceFragment()) at line 28)')

# ---- LookFeelPreferenceFragment

e('LookFeelPreferenceFragment.<init>', 'LookFeelPreferenceFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is created',
  evidence='SRC settings/LookFeelPreferenceFragment.java:45-171 (framework lifecycle INFERRED)')

e('LookFeelPreferenceFragment.onCreate', 'LookFeelPreferenceFragment.onCreatePreferences', 'LIFECYCLE',
  'the inherited PreferenceFragmentCompat.onCreate calls the overridden onCreatePreferences (INFERRED, not read)',
  evidence='SRC settings/LookFeelPreferenceFragment.java:173-176')

# ---- GUI edges from the look and feel page to the preference listeners (D6)

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$1.onPreferenceChange', 'GUI',
  'the user toggles Show open accounts',
  gui=['Open Settings > Look and feel and toggle the open accounts checkbox'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:63-70 (listener registered at line 63; method at 65-69)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$2.onPreferenceChange', 'GUI',
  'the user toggles Show favourite accounts',
  gui=['Open Settings > Look and feel and toggle the favourite accounts checkbox'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:82-89 (listener registered at line 82; method at 84-88)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$3.onPreferenceChange', 'GUI',
  'the user toggles Hide Reconciled Amounts',
  gui=['Open Settings > Look and feel and toggle Hide Reconciled Amounts'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:97-103 (listener at line 97; method at 99-102)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$4.onPreferenceChange', 'GUI',
  'the user picks a new period in Show transactions',
  gui=['Open Settings > Look and feel and pick a value in Show transactions'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:125-134 (listener at line 125; method at 127-133)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$5.onPreferenceChange', 'GUI',
  'the user picks a font',
  gui=['Open Settings > Look and feel and pick a font'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:141-153 (listener at line 141; method at 143-152)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$6.onPreferenceChange', 'GUI',
  'the user picks a font size',
  gui=['Open Settings > Look and feel and pick a font size'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:160-169 (listener at line 160; method at 163-168)')
