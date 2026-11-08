# ================================================================== batch 117 (label_117): InvestmentSettingsFragment (11 methods, its $1-$3 listeners 6), LookAndFeelSettings (10)
# Result: 27 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_117.md). Grep evidence: graphs/MMEX/parts/label_117.grep.txt.
# The batch file header says 27 methods; the 27 method lines are labelled here.
# Routes: SettingsFragment$4 (batch 116) starts InvestmentSettingsActivity, which creates InvestmentSettingsFragment; the fragment lifecycle edges are LIFECYCLE, as in label_114. LookAndFeelSettings methods are reached through auto CALL records only.
# This file writes:
#   - 3 GUI edges from the existing key S_INVESTMENT_SETTINGS (graph_def.py:10424; no SCREENS key is added here) to the three preference listeners,
#   - LIFECYCLE edges: InvestmentSettingsFragment.<init> -> onCreate -> onCreatePreferences -> onStart -> onStop,
#   - 1 REGISTER edge (onStart -> onEvent) and 1 ASYNC edge (AmountInputDialog$7.onClick -> onEvent) for EventBus (cls non_standard, as in label_050 and label_033).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7). No UNREACHABLE entry and no sup pair.

# ---- the investment settings screen: GUI edges from the page into this batch's listeners (dst owned here, D1, D6)

e('S_INVESTMENT_SETTINGS', 'InvestmentSettingsFragment$1.onPreferenceClick', 'GUI',
  'the asset allocation threshold row is tapped: the listener shows the amount dialog with requestId KEY_THRESHOLD',
  gui=['Open Settings, tap the investment preference, then tap the asset allocation threshold'],
  evidence='SRC settings/InvestmentSettingsFragment.java:111-119 (getInstance at 116, show at 117; printed this session)')

e('S_INVESTMENT_SETTINGS', 'InvestmentSettingsFragment$2.onPreferenceChange', 'GUI',
  'the quote provider list preference changes: the listener stores the provider and calls displayQuotesProvider (auto CALL, line 146)',
  gui=['Open Settings, tap the investment preference, then choose a quote provider'],
  evidence='SRC settings/InvestmentSettingsFragment.java:140-148 (printed this session)')

e('S_INVESTMENT_SETTINGS', 'InvestmentSettingsFragment$3.onPreferenceChange', 'GUI',
  'the exchange rate provider list preference changes: the listener stores the provider and calls displayExchangeRatesProvider (auto CALL, line 175)',
  gui=['Open Settings, tap the investment preference, then choose an exchange rate provider'],
  evidence='SRC settings/InvestmentSettingsFragment.java:169-177 (printed this session)')

# ---- fragment lifecycle (dst owned here; the framework calls these after the constructor and in order, INFERRED androidx lifecycle)

e('InvestmentSettingsFragment.<init>', 'InvestmentSettingsFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is constructed by InvestmentSettingsActivity.onCreate (setSettingFragment at line 28)',
  evidence='SRC settings/InvestmentSettingsActivity.java:20-32 (setSettingFragment at 28); SRC settings/InvestmentSettingsFragment.java:39-55')

e('InvestmentSettingsFragment.onCreate', 'InvestmentSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/InvestmentSettingsFragment.java:45-62')

e('InvestmentSettingsFragment.onCreatePreferences', 'InvestmentSettingsFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after the preference view is created (INFERRED androidx lifecycle)',
  evidence='SRC settings/InvestmentSettingsFragment.java:58-69')

e('InvestmentSettingsFragment.onStart', 'InvestmentSettingsFragment.onStop', 'LIFECYCLE',
  'the framework calls onStop when the user leaves the screen (INFERRED androidx lifecycle)',
  evidence='SRC settings/InvestmentSettingsFragment.java:65-76')

# ---- EventBus: onStart registers the fragment until onStop; the amount dialog OK button posts AmountEnteredEvent (D17 pattern)

e('InvestmentSettingsFragment.onStart', 'InvestmentSettingsFragment.onEvent', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe onEvent receives AmountEnteredEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at InvestmentSettingsFragment.java:68, @Subscribe on onEvent (line 80); library source not read, INFERRED',
  evidence='SRC settings/InvestmentSettingsFragment.java:65-86 (register at 68, unregister at 75, @Subscribe at 80)')

e('AmountInputDialog$7.onClick', 'InvestmentSettingsFragment.onEvent', 'ASYNC',
  'the amount dialog OK button posts AmountEnteredEvent on the EventBus; for the threshold dialog the event carries KEY_THRESHOLD and onEvent stores the amount',
  cls='non_standard', via='EventBus (greenrobot) post at AmountInputDialog.java:260 (auto record AmountInputDialog$7.onClick -> AmountEnteredEvent.<init>, line 260); subscriber registered in InvestmentSettingsFragment.onStart',
  evidence='SRC common/AmountInputDialog.java:252-264 (post at 260); SRC settings/InvestmentSettingsFragment.java:80-86; INFERRED EventBus delivery (library not read)')
