# ================================================================== batch 120 (label_120): SecuritySettingsFragment (6 methods + 3 listeners x 2 = 12), SettingsActivity (4), SettingsActivity_MembersInjector (5), SettingsBase (18)
# Result: 34 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_120.md). Grep evidence: graphs/MMEX/parts/label_120.grep.txt.
# Routes: SecuritySettingsActivity (batch 119) hosts SecuritySettingsFragment and owns the ENTERS edge to S_SECURITY_SETTINGS; the three listeners start PasscodeActivity, whose setResult returns to onActivityResult (RESULT edge written here). SettingsActivity is started by SettingsFragment$1 (batch 121), MainActivity.onDrawerMenuAndOptionMenuSelected and HomeFragment$2.onClick (INTENT edges written here); its settings-list branch is the page S_SETTINGS defined here.
# This file writes:
#   - SCREENS for S_SETTINGS (no part defines a settings-list page yet; batch 121 owns SettingsFragment and should reuse this key),
#   - INTENT edges into SettingsActivity.<init> (dst owned here, D1),
#   - LIFECYCLE edges for the fragment chain and the activity, GUI edges from S_SECURITY_SETTINGS, one RESULT edge, ENTERS from SettingsActivity.onCreate,
#   - 5 UNREACHABLE entries and 25 sup pairs cutting the outgoing auto records of the 5 unreachable methods (D14).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).

SCREENS.update({
    'S_SETTINGS': 'Settings list screen (SettingsActivity hosting SettingsFragment): the main settings preference list opened from the drawer menu and the home welcome view, with one entry per settings section (general, look and feel, behaviour, investment, budget, security, database); the per-database entry opens the same activity with PerDatabaseFragment instead (S_PER_DATABASE_SETTINGS)',
})

# ---- SecuritySettingsFragment: fragment lifecycle (framework calls; INFERRED androidx Fragment lifecycle, library source not read)

e('SecuritySettingsFragment.<init>', 'SecuritySettingsFragment.onCreate', 'LIFECYCLE',
  'SecuritySettingsActivity.onCreate calls setSettingFragment(new SecuritySettingsFragment()) (auto CALL, line 28); the fragment is committed and the FragmentManager then calls onCreate (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/SecuritySettingsActivity.java:8-30; SRC settings/BaseSettingsFragmentActivity.java:70-92; SRC settings/SecuritySettingsFragment.java:37-86')

e('SecuritySettingsFragment.onCreate', 'SecuritySettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: inherited PreferenceFragmentCompat code, not read); the method body is empty',
  evidence='SRC settings/SecuritySettingsFragment.java:48-91')

e('SecuritySettingsFragment.onCreatePreferences', 'SecuritySettingsFragment.onResume', 'LIFECYCLE',
  'the framework calls onResume after the preference view is created (INFERRED androidx Fragment lifecycle); onResume enables or disables the three passcode preferences',
  evidence='SRC settings/SecuritySettingsFragment.java:89-166')

# ---- SecuritySettingsFragment: the three passcode preferences (D9: the fragment uses its host screen S_SECURITY_SETTINGS)

e('S_SECURITY_SETTINGS', 'SecuritySettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the active passcode preference: the listener starts PasscodeActivity to enter a new passcode (startActivityPasscode, auto CALL line 60)',
  gui=['Open Settings > Security and tap the active passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:55-63 (listener created at 55; onPreferenceClick at 57-62, startActivityPasscode call at 60)')

e('S_SECURITY_SETTINGS', 'SecuritySettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the edit passcode preference: the listener starts PasscodeActivity to enter the previous passcode (startActivityPasscode, auto CALL line 71)',
  gui=['Open Settings > Security and tap the edit passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:66-74 (listener created at 66; onPreferenceClick at 68-73)')

e('S_SECURITY_SETTINGS', 'SecuritySettingsFragment$3.onPreferenceClick', 'GUI',
  'the user taps the disable passcode preference: the listener starts PasscodeActivity to enter the current passcode before clearing it (startActivityPasscode, auto CALL line 82)',
  gui=['Open Settings > Security and tap the disable passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:77-85 (listener created at 77; onPreferenceClick at 79-84)')

# ---- SecuritySettingsFragment: result of PasscodeActivity (RESULT; dst owned here)

e('PasscodeActivity$1.onClick', 'SecuritySettingsFragment.onActivityResult', 'RESULT',
  'PasscodeActivity sets RESULT_OK with the entered passcode (setResult, line 125) and the framework delivers the result to the fragment that called startActivityForResult (startActivityPasscode, line 174)',
  evidence='SRC com/money/manager/ex/PasscodeActivity.java:98-128 (onClick of PasscodeActivity$1 starts at line 101; setResult at 125); SRC settings/SecuritySettingsFragment.java:94-175')

# ---- SettingsActivity: the settings list activity (dst owned here, D1; the sources belong to batches 121, MainActivity and HomeFragment)

e('SettingsFragment$1.onPreferenceClick', 'SettingsActivity.<init>', 'INTENT',
  'the per-database preference of the settings list starts SettingsActivity with the PerDatabaseFragment extra (EXTRA_FRAGMENT), so showFragment shows PerDatabaseFragment',
  gui=['Open Settings and tap the per-database preference'],
  evidence='SRC settings/SettingsFragment.java:56-64 (anonymous class $1 is created at line 59: auto_calls SettingsFragment.onCreate -> SettingsFragment$1.<init>; intent at line 62)')

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'SettingsActivity.<init>', 'INTENT',
  'the Settings drawer item starts SettingsActivity without the extra, so showFragment shows SettingsFragment (the settings list)',
  gui=['Open the navigation drawer and choose Settings'],
  evidence='SRC home/MainActivity.java:665 (startActivity(new Intent(MainActivity.this, SettingsActivity.class)) in onDrawerMenuAndOptionMenuSelected, method at 589)')

e('HomeFragment$2.onClick', 'SettingsActivity.<init>', 'INTENT',
  'the home screen welcome view control starts SettingsActivity without the extra, so the settings list is shown',
  gui=['Home screen welcome view: tap the control that opens Settings'],
  evidence='SRC home/HomeFragment.java:595-600 (anonymous class $2 is created at line 596 in createWelcomeView: auto_calls HomeFragment.createWelcomeView -> HomeFragment$2.<init>; intent at line 599)')

e('SettingsActivity.<init>', 'SettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_004 AboutActivity)',
  evidence='SRC settings/SettingsActivity.java:31-46; FW-SRC core/java/android/app/ActivityThread.java:2724-2731 (as cited in label_004, not read in this batch)')

e('SettingsActivity.onCreate', 'SettingsActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate (INFERRED androidx activity lifecycle); onResume sets the title to R.string.settings',
  evidence='SRC settings/SettingsActivity.java:40-53')

e('SettingsActivity.onCreate', 'S_SETTINGS', 'ENTERS',
  'the settings list is shown: onCreate calls showFragment, which uses SettingsFragment unless the PerDatabaseFragment extra is present (the per-database branch is labelled in batch 119 as S_PER_DATABASE_SETTINGS)',
  evidence='SRC settings/SettingsActivity.java:40-72 (default SettingsFragment at lines 67-69)')

# ---- UNREACHABLE (each with a grep section in label_120.grep.txt)

UNREACHABLE['SettingsBase.get(String,int)'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has SettingsBase.get(String,int) as dst (with or without a receiver variant); no call in the settings package passes a String key with an int default (AppSettings.java:104 is get(R.string.pref_sort_payee, 0), the Integer overload); its outgoing records (to each subclass getPreferences, line 129) are cut by sup below',
    'settings/SettingsBase.java:128-130; label_120.grep.txt section B',
    'SOURCE')

UNREACHABLE['SettingsBase.getBooleanSetting(String)'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has the one-argument getBooleanSetting as dst; its only source reference is its own body calling the two-argument form (SettingsBase.java:107); every other call in the source root uses the two-argument form (SettingsBase.java:103; LookAndFeelSettings.java:52, 120)',
    'settings/SettingsBase.java:106-108; label_120.grep.txt section A',
    'SOURCE')

UNREACHABLE['SettingsActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
    'generated Dagger constructor: its only caller is SettingsActivity_MembersInjector.create (auto record, line 27), and create has no caller (see create); no app code builds the injector',
    'generated SettingsActivity_MembersInjector.java:27 (auto record); label_120.grep.txt section C',
    'SOURCE')

UNREACHABLE['SettingsActivity_MembersInjector.create'] = ('no_trigger_in_app',
    'generated Dagger factory: no auto_calls.json record has create as dst; DaggerMmxComponent.injectSettingsActivity (auto records at DaggerMmxComponent.java:433 and 435) calls the static helpers injectAppSettingsLazy and injectCoreLazy directly, so no MembersInjector instance is built; its outgoing record to <init> is cut by sup below',
    'generated SettingsActivity_MembersInjector.java:26-27 (auto record); DaggerMmxComponent.java:433-435 (auto records); label_120.grep.txt section C',
    'SOURCE')

UNREACHABLE['SettingsActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'generated MembersInjector method: no auto_calls.json record has injectMembers as dst, and only an injector instance (built by create, which has no caller) could call it through the interface; its outgoing records (to injectAppSettingsLazy at line 32 and injectCoreLazy at line 33) are cut by sup below',
    'generated SettingsActivity_MembersInjector.java:31-33 (auto records); label_120.grep.txt section C',
    'SOURCE')

# ---- sup pairs (D14): outgoing auto records of the five UNREACHABLE methods, one per exact (src, dst) in auto_calls.json

sup(('SettingsActivity_MembersInjector.create', 'SettingsActivity_MembersInjector.<init>'))
sup(('SettingsActivity_MembersInjector.injectMembers', 'SettingsActivity_MembersInjector.injectAppSettingsLazy'))
sup(('SettingsActivity_MembersInjector.injectMembers', 'SettingsActivity_MembersInjector.injectCoreLazy'))
sup(('SettingsBase.get(String,int)', 'AppSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'BehaviourSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'BudgetSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'GeneralSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'LookAndFeelSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'SyncPreferences.getPreferences'))
sup(('SettingsBase.get(String,int)@AppSettings', 'AppSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@BehaviourSettings', 'BehaviourSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@BudgetSettings', 'BudgetSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@GeneralSettings', 'GeneralSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@LookAndFeelSettings', 'LookAndFeelSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@SyncPreferences', 'SyncPreferences.getPreferences'))
sup(('SettingsBase.getBooleanSetting(String)', 'SettingsBase.getBooleanSetting(String,boolean)'))
sup(('SettingsBase.getBooleanSetting(String)@AppSettings', 'SettingsBase.getBooleanSetting(String,boolean)@AppSettings'))
sup(('SettingsBase.getBooleanSetting(String)@BehaviourSettings', 'SettingsBase.getBooleanSetting(String,boolean)@BehaviourSettings'))
sup(('SettingsBase.getBooleanSetting(String)@BudgetSettings', 'SettingsBase.getBooleanSetting(String,boolean)@BudgetSettings'))
sup(('SettingsBase.getBooleanSetting(String)@GeneralSettings', 'SettingsBase.getBooleanSetting(String,boolean)@GeneralSettings'))
sup(('SettingsBase.getBooleanSetting(String)@InvestmentSettings', 'SettingsBase.getBooleanSetting(String,boolean)@InvestmentSettings'))
sup(('SettingsBase.getBooleanSetting(String)@LookAndFeelSettings', 'SettingsBase.getBooleanSetting(String,boolean)@LookAndFeelSettings'))
sup(('SettingsBase.getBooleanSetting(String)@SyncPreferences', 'SettingsBase.getBooleanSetting(String,boolean)@SyncPreferences'))
