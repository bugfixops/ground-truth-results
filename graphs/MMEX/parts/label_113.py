# ================================================================== batch 113 (label_113): AppSettings (9 methods), AppSettings_Factory (4), AppSettings_MembersInjector (4), BaseSettingsFragmentActivity (4), BehaviourSettings (14), BehaviourSettingsActivity (3): 38 methods
# Result: 29 REACHABLE, 9 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_113.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_113.grep.txt.
# Auto CALL records (auto_calls.json) are not rewritten here (D7). The routes that the auto data cannot give are written here:
#   - the Behaviour preference in SettingsFragment starts BehaviourSettingsActivity by an explicit intent (INTENT), then the activity lifecycle (LIFECYCLE), and the activity enters page S_BEHAVIOUR_SETTINGS (ENTERS),
#   - the SMS permission answer goes back to BehaviourSettingsActivity.onRequestPermissionsResult (FRAMEWORK, settings gate, D19),
#   - the EventBus subscriber BaseSettingsFragmentActivity.onEvent gets two ASYNC edges (the same routes as MmxBaseFragmentActivity.onEvent in batch 032).
# This file writes:
#   - SCREENS: S_BEHAVIOUR_SETTINGS (no settings page exists in the SCREENS keys; the activity is one screen, D9),
#   - e() edges whose destination this batch owns (D1),
#   - UNREACHABLE entries: AppSettings.getInvestmentSettings and BehaviourSettings.getIncomeExpensePeriod (SOURCE); AppSettings_Factory (4) and AppSettings_MembersInjector.create, .<init>, .injectMembers (INFERRED, generated code, evidence in label_113.grep.txt),
#   - sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch.

SCREENS.update({
    'S_BEHAVIOUR_SETTINGS': 'Behaviour settings screen (BehaviourSettingsActivity hosts BehaviourSettingsFragment; the notification time and the SMS automation switch are set on this screen)',
})

# ---- BehaviourSettingsActivity: explicit intent from the settings list, lifecycle, the page, and the SMS permission answer

e('SettingsFragment$3.onPreferenceClick', 'BehaviourSettingsActivity.<init>', 'INTENT',
  'the Behaviour preference in the settings list starts BehaviourSettingsActivity with an explicit intent, and the framework instantiates the manifest-declared activity',
  evidence='SRC settings/SettingsFragment.java:87 (listener created), 89-93 (onPreferenceClick), 90 (startActivity(new Intent(getActivity(), BehaviourSettingsActivity.class))); SRC AndroidManifest.xml:253-255 (declared, no intent-filter, not exported)')

e('BehaviourSettingsActivity.<init>', 'BehaviourSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor of the activity (INFERRED framework launch order, not re-read in this batch)',
  evidence='SRC settings/BehaviourSettingsActivity.java:26-27 (class declaration, no explicit constructor), 29-33 (onCreate); INFERRED framework launch order (constructor, then onCreate)')

e('BehaviourSettingsActivity.onCreate', 'S_BEHAVIOUR_SETTINGS', 'ENTERS',
  'the activity shows the Behaviour settings page: onCreate installs BehaviourSettingsFragment through setSettingFragment',
  evidence='SRC settings/BehaviourSettingsActivity.java:29-33 (setSettingFragment(new BehaviourSettingsFragment()) at 32); SRC settings/BaseSettingsFragmentActivity.java:71-92')

e('BehaviourSettingsFragment$2.onPreferenceClick', 'BehaviourSettingsActivity.onRequestPermissionsResult', 'FRAMEWORK',
  'the SMS automation switch is turned on while RECEIVE_SMS is not granted: the fragment requests it with ActivityCompat.requestPermissions (request code 1), and the framework returns the answer to the activity',
  needs_state=state_text('the SMS automation switch is turned on while the RECEIVE_SMS permission is not granted', ('settings',)),
  evidence='SRC settings/BehaviourSettingsFragment.java:129 (onPreferenceClick), 138 (getBankSmsTrans), 140 (granted test), 144-147 (else branch: ActivityCompat.requestPermissions(getActivity(), ..., 1)); SRC settings/BehaviourSettingsActivity.java:36-39 (override, requestCode == 1); INFERRED framework answer path not re-read in this batch')

# ---- BaseSettingsFragmentActivity: EventBus subscriber, two ASYNC routes (the same routes that batch 032 writes for MmxBaseFragmentActivity.onEvent)

e('DebugTree.log', 'BaseSettingsFragmentActivity.onEvent', 'ASYNC',
  'a debug build logs an error through Timber while a settings activity is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent (the subclass inherits the registration from MmxBaseFragmentActivity.onStart)',
  env=env_text('an error is logged through Timber while a settings activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:45-46 (posts only when a subscriber exists); SRC MmexApplication.java:134-135 (DebugTree in the debug branch); SRC settings/BaseSettingsFragmentActivity.java:52-55 (@Subscribe onEvent(ErrorRaisedEvent)); SRC common/MmxBaseFragmentActivity.java:141 (register in onStart); INFERRED EventBus library source not read')

e('ScreenTree.log', 'BaseSettingsFragmentActivity.onEvent', 'ASYNC',
  'a release build logs an error through Timber while a settings activity is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent (the debug build plants DebugTree instead)',
  env=env_text('an error is logged through Timber while a settings activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:26-27; SRC MmexApplication.java:134-140 (ScreenTree in the else branch, release only); SRC settings/BaseSettingsFragmentActivity.java:52-55; SRC common/MmxBaseFragmentActivity.java:141; INFERRED EventBus library source not read')

# ================================================================== UNREACHABLE: source evidence (SOURCE)

UNREACHABLE['AppSettings.getInvestmentSettings'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration in the whole source root, and no bytecode CALL record targets it (auto_calls.json: 0 incoming records)',
    'settings/AppSettings.java:87-92; label_113.grep.txt sections 5',
    'SOURCE')

UNREACHABLE['BehaviourSettings.getIncomeExpensePeriod'] = ('no_trigger_in_app',
    'no caller: the only other occurrence in the source root is HomeFragment.java:252, a commented-out line; no bytecode CALL record targets it (auto_calls.json: 0 incoming records)',
    'settings/BehaviourSettings.java:61-65; label_113.grep.txt sections 5, 6',
    'SOURCE')

# ================================================================== UNREACHABLE: generated Dagger methods (INFERRED, D16)

UNREACHABLE['AppSettings_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is AppSettings_Factory.create (auto_calls.json: AppSettings_Factory.class bytecode line 35), and create has no caller',
    'AppSettings_Factory.class bytecode line 35 (generated; class file final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/settings/AppSettings_Factory.class); label_113.grep.txt sections 2, 3, 4',
    'INFERRED')

UNREACHABLE['AppSettings_Factory.create'] = ('no_trigger_in_app',
    'generated static factory with no caller: no source reference (label_113.grep.txt section 1), no incoming auto_calls record, and the component builds AppSettings through MmxModule_ProvideAppSettingsFactory (DaggerMmxComponent.java:189)',
    'AppSettings_Factory.class bytecode line 35 (generated); label_113.grep.txt sections 1-4',
    'INFERRED')

UNREACHABLE['AppSettings_Factory.get'] = ('no_trigger_in_app',
    'generated provider method with no caller: no incoming auto_calls record and no source reference; the component uses MmxModule_ProvideAppSettingsFactory (DaggerMmxComponent.java:189), not this factory',
    'AppSettings_Factory.class bytecode line 27-28 (generated); label_113.grep.txt sections 1-4',
    'INFERRED')

UNREACHABLE['AppSettings_Factory.newAppSettings'] = ('no_trigger_in_app',
    'generated method with no caller: no incoming auto_calls record and no source reference; it is reached only from AppSettings_Factory.get, which is itself unreachable',
    'AppSettings_Factory.class bytecode line 39 (generated); label_113.grep.txt sections 1-4',
    'INFERRED')

UNREACHABLE['AppSettings_MembersInjector.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is AppSettings_MembersInjector.create (auto_calls.json: AppSettings_MembersInjector.class bytecode line 23), and create has no caller',
    'AppSettings_MembersInjector.class bytecode line 23 (generated; class file final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/settings/AppSettings_MembersInjector.class); label_113.grep.txt sections 2, 3',
    'INFERRED')

UNREACHABLE['AppSettings_MembersInjector.create'] = ('no_trigger_in_app',
    'generated static factory with no caller: no source reference (label_113.grep.txt section 1) and no incoming auto_calls record; the component calls injectSharedPreferences directly (DaggerMmxComponent.java:511), not create or injectMembers',
    'AppSettings_MembersInjector.class bytecode line 23 (generated); label_113.grep.txt sections 1-3',
    'INFERRED')

UNREACHABLE['AppSettings_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'generated members-injector method with no caller: no incoming auto_calls record and no source reference; the component reaches injectSharedPreferences directly (DaggerMmxComponent.java:511), not through injectMembers',
    'AppSettings_MembersInjector.class bytecode line 28 (generated); label_113.grep.txt sections 1, 3, 4',
    'INFERRED')

# ================================================================== sup (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AppSettings.getInvestmentSettings', 'InvestmentSettings.<init>'))  # the unreachable getter's call into the investment settings constructor (AppSettings.java:89)
sup(('AppSettings.getInvestmentSettings', 'SettingsBase.getContext'))  # AppSettings.java:89
sup(('BehaviourSettings.getIncomeExpensePeriod', 'SettingsBase.get(Integer,String)@BehaviourSettings'))  # BehaviourSettings.java:62
sup(('BehaviourSettings.getIncomeExpensePeriod', 'SettingsBase.getContext'))  # BehaviourSettings.java:63
sup(('AppSettings_Factory.create', 'AppSettings_Factory.<init>'))  # AppSettings_Factory.class bytecode line 35
sup(('AppSettings_Factory.get', 'AppSettings_MembersInjector.injectSharedPreferences'))  # AppSettings_Factory.class bytecode line 28
sup(('AppSettings_Factory.get', 'AppSettings.<init>'))  # AppSettings_Factory.class bytecode line 27
sup(('AppSettings_Factory.newAppSettings', 'AppSettings.<init>'))  # AppSettings_Factory.class bytecode line 39
sup(('AppSettings_MembersInjector.create', 'AppSettings_MembersInjector.<init>'))  # AppSettings_MembersInjector.class bytecode line 23
sup(('AppSettings_MembersInjector.injectMembers', 'AppSettings_MembersInjector.injectSharedPreferences'))  # AppSettings_MembersInjector.class bytecode line 28
