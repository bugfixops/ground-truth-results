# ================================================================== batch 119 (label_119): PerDatabaseFragment (10 methods), PerDatabaseFragment$1 to $8 (16), PreferenceConstants (2), SecuritySettingsActivity (2): 30 methods
# Result: 30 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_119.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_119.grep.txt.
# SCREENS: S_PER_DATABASE_SETTINGS (new; the per-database list is a separate screen in SettingsActivity, D9) and S_SECURITY_SETTINGS (new; no S_SECURITY* key exists).
# The settings list (SettingsFragment) has no SCREENS key, so this part does not write GUI edges from it.
# Edges: INTENT SettingsFragment$6 -> SecuritySettingsActivity.<init> (dst owned here, D1); LIFECYCLE chains; ENTERS; GUI from the two pages to the listeners; RESULT CurrencyListFragment.setResult -> PerDatabaseFragment.onActivityResult.
# Not written: CALL edges (D7: every app call in this batch is an auto CALL record); the INTENT from PerDatabaseFragment$5 and $8 into CurrencyListActivity.<init> (owned by the CurrencyListActivity batch, D1); the INTENT from SettingsFragment$1 into SettingsActivity.<init> (owned by the SettingsActivity batch).
# No UNREACHABLE entries: every method has a route (see label_119.md).

SCREENS.update({
    'S_PER_DATABASE_SETTINGS': 'Per-database settings screen (SettingsActivity hosting PerDatabaseFragment, opened from the per-database preference of the settings list): the preference list from preferences_per_database.xml with the user name, date format, base currency, financial year start, and default account',
    'S_SECURITY_SETTINGS': 'Security settings screen (SecuritySettingsActivity): the security preference list hosted by SecuritySettingsFragment, opened from the passcode preference of the settings list',
})

# ---- SettingsFragment passcode preference -> SecuritySettingsActivity (INTENT into this batch's activity)

e('SettingsFragment$6.onPreferenceClick', 'SecuritySettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), SecuritySettingsActivity.class)) from the passcode preference',
  gui=['Open Settings and tap the security (passcode) preference'],
  evidence='SRC settings/SettingsFragment.java:124-131 (listener set at 126; onPreferenceClick 128-130; startActivity at 129); auto_calls: SettingsFragment.onCreate -> SettingsFragment$6.<init> (SettingsFragment.java:126)')

# ---- SecuritySettingsActivity: lifecycle and page

e('SecuritySettingsActivity.<init>', 'SecuritySettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_114 BudgetSettingsActivity)',
  evidence='SRC settings/SecuritySettingsActivity.java:22-30 (class declaration, no explicit constructor; onCreate at 25-29); INFERRED framework launch order (constructor, then onCreate)')

e('SecuritySettingsActivity.onCreate', 'S_SECURITY_SETTINGS', 'ENTERS',
  'the security settings screen is shown',
  evidence='SRC settings/SecuritySettingsActivity.java:25-29 (setSettingFragment(new SecuritySettingsFragment()) at line 28)')

# ---- PerDatabaseFragment: lifecycle and page (SettingsActivity.showFragment creates the fragment, auto CALL)

e('PerDatabaseFragment.<init>', 'PerDatabaseFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is committed by setSettingFragment (SettingsActivity.java:71)',
  evidence='SRC settings/PerDatabaseFragment.java:59-68 (constructor, onCreate); SRC settings/SettingsActivity.java:63 (new PerDatabaseFragment), 71 (setSettingFragment); INFERRED androidx FragmentManager (library not in the dataset; source not read)')

e('PerDatabaseFragment.onCreate', 'PerDatabaseFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/PerDatabaseFragment.java:64-68 (onCreate, super call), 70-75 (onCreatePreferences); same pattern as label_114.py line 47')

e('PerDatabaseFragment.onCreatePreferences', 'S_PER_DATABASE_SETTINGS', 'ENTERS',
  'the per-database preference list (preferences_per_database) is added and shown',
  evidence='SRC settings/PerDatabaseFragment.java:70-75 (addPreferencesFromResource at 71; initializeControls at 73)')

# ---- the page's preference changes and clicks (GUI from the page, D6)

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$1.onPreferenceChange', 'GUI',
  'the user changes the user name preference (pref_user_name); the listener saves it through MmexApplication.setUserName',
  evidence='SRC settings/PerDatabaseFragment.java:103-110 (listener set at 103; onPreferenceChange 105-109); auto_calls: $1.onPreferenceChange -> MmexApplication.setUserName (line 106)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$2.onPreferenceChange', 'GUI',
  'the user picks a date format (pref_date_format); the listener saves it with InfoService.setInfoValue and updates the summary',
  evidence='SRC settings/PerDatabaseFragment.java:125-135 (listener set at 125; onPreferenceChange 128-134); auto_calls: $2.onPreferenceChange -> InfoService.setInfoValue (line 129), -> getDateFormatFromMask (line 130)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$3.onPreferenceChange', 'GUI',
  'the user enters the financial year start day (pref_financial_year_startdate); the listener validates it, saves it, and shows a toast on a parse error',
  evidence='SRC settings/PerDatabaseFragment.java:151-175 (listener set at 151; onPreferenceChange 153-174); auto_calls: $3.onPreferenceChange -> UIHelper.showToast (line 158), -> InfoService.setInfoValue (line 166)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$4.onPreferenceChange', 'GUI',
  'the user picks the financial year start month (pref_financial_year_startmonth); the listener saves it with InfoService.setInfoValue',
  evidence='SRC settings/PerDatabaseFragment.java:203-219 (listener set at 203; onPreferenceChange 206-217); auto_calls: $4.onPreferenceChange -> InfoService.setInfoValue (line 210)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$5.onPreferenceClick', 'GUI',
  'the user taps the base currency preference (pref_base_currency); the currency list opens for a pick (ACTION_PICK, startActivityForResult at line 244); the result returns to onActivityResult',
  evidence='SRC settings/PerDatabaseFragment.java:238-248 (listener set at 238; onPreferenceClick 240-247; startActivityForResult at 244)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$6.onPreferenceChange', 'GUI',
  'the user picks the default account (pref_default_account); the listener loads the account name and saves the id in GeneralSettings',
  evidence='SRC settings/PerDatabaseFragment.java:297-311 (listener set at 297; onPreferenceChange 299-310); auto_calls: $6.onPreferenceChange -> AccountRepository.loadName (line 303), -> GeneralSettings.setDefaultAccountId (line 307)')

# ---- the base currency changed dialog (shown on this page, D9): its two buttons

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$7.onClick', 'GUI',
  'the OK button of the base currency changed dialog (showCurrencyChangeNotification); no action',
  evidence='SRC settings/PerDatabaseFragment.java:327-344 (dialog built at 327-335; positive listener 331-336; onClick 333-334); auto_calls: onActivityResult -> showCurrencyChangeNotification (line 90)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$8.onClick', 'GUI',
  'the Open currencies button of the same dialog: CurrencyListActivity opens for editing (ACTION_EDIT)',
  evidence='SRC settings/PerDatabaseFragment.java:337-344 (neutral listener 337-344; onClick 339-343; setAction at 341)')

# ---- the currency pick result (RESULT, D1: the dst is owned here)

e('CurrencyListFragment.setResult', 'PerDatabaseFragment.onActivityResult', 'RESULT',
  'the currency list returns RESULT_OK with the picked currency id (ACTION_PICK, opened from the base currency preference, PerDatabaseFragment$5.onPreferenceClick)',
  evidence='SRC currency/list/CurrencyListFragment.java:297-321 (setResult; putExtra at 309; setResult(RESULT_OK) at 314); SRC settings/PerDatabaseFragment.java:77-93 (onActivityResult reads INTENT_RESULT_CURRENCYID at 82)')
