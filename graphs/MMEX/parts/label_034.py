# batch 034 (label_034): com.money.manager.ex.core.Core (18 methods), Core$1 and Core$2 (4), Core_Factory (4), Core_MembersInjector (5): 31 methods. Rows and printed lines: graphs/MMEX/parts/label_034.md.
# Evidence: graphs/MMEX/parts/label_034.grep.txt. CALL edges come from auto_calls.json and are not written here. Dagger-generated classes have no source: their labels are INFERRED.

e('Core.alert(int,int)', 'Core$1.onClick', 'FRAMEWORK',
  'the OK button of the no-network dialog is pressed: the dialog keeps the listener and calls its onClick',
  evidence='SRC core/Core.java:82-100 (setPositiveButton with the listener at 93, onClick at 95-97, show at 99); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:709-710 (positive button click handler), 125-147 (mButtonHandler sends the message), 160-167 (handleMessage calls onClick at 166), 1021-1023 (setButton with the listener)')

sup(('Core_MembersInjector.create', 'Core_MembersInjector.<init>'))  # create has no caller, so its call into <init> cannot run
sup(('Core_MembersInjector.injectMembers', 'Core_MembersInjector.injectOpenHelper'),  # injectMembers has no caller
    ('Core_MembersInjector.injectMembers', 'Core_MembersInjector.injectAppSettingsLazy'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_034.grep.txt)

UNREACHABLE['Core.isToDisplayChangelog'] = ('no_trigger_in_app',
  'No live caller. The only source reference is commented out (MainActivity.java:1495, inside the comment block of handleDeviceRotation). No caller record exists in auto_calls.json. Its caller Core.showChangelog is UNREACHABLE too',
  'SRC core/Core.java:271-274; SRC home/MainActivity.java:1493-1497 (commented call); label_034.grep.txt sections B and D',
  'SOURCE')

UNREACHABLE['Core.showChangelog'] = ('no_trigger_in_app',
  'No live caller. The only source reference is commented out (MainActivity.java:1496). No caller record exists in auto_calls.json. It creates the changelog dialog and its listener Core$2 (Core.java:325-326)',
  'SRC core/Core.java:318-337; SRC home/MainActivity.java:1496 (commented call); label_034.grep.txt sections B and D',
  'SOURCE')

UNREACHABLE['Core$2.<init>'] = ('no_trigger_in_app',
  'Created only in Core.showChangelog (the listener at Core.java:325-326). showChangelog has no caller, so this cannot run',
  'SRC core/Core.java:318-337; label_034.grep.txt section D (showChangelog -> Core$2.<init> at 325)',
  'SOURCE')

UNREACHABLE['Core$2.onClick'] = ('no_trigger_in_app',
  'The OK listener of the changelog dialog (Core.java:328-331). Its only creator is Core.showChangelog, which has no caller. No FRAMEWORK edge is written because the creator has no route',
  'SRC core/Core.java:318-337',
  'SOURCE')

UNREACHABLE['Core_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (no source in the source root). Its only caller record is Core_MembersInjector.create (Core_MembersInjector.java:28), and create has no caller. The component calls the static injectOpenHelper and injectAppSettingsLazy methods instead (DaggerMmxComponent.java:518-519). No MembersInjector<Core> reference exists in the app source',
  'auto_calls.json (Core_MembersInjector.java:28; 0 caller records for create); label_034.grep.txt sections A, C and D',
  'INFERRED')

UNREACHABLE['Core_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory with no caller record in auto_calls.json and no app source reference. The component does not call it (DaggerMmxComponent.java:518-519)',
  'auto_calls.json (0 caller records); label_034.grep.txt sections A and D',
  'INFERRED')

UNREACHABLE['Core_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method reached only through a MembersInjector<Core> reference, which no app code uses (section A). No caller record for any receiver in auto_calls.json (section D). The component calls the static methods directly (DaggerMmxComponent.java:518-519). Its two outgoing records (Core_MembersInjector.java:33-34) are cut by sup',
  'auto_calls.json (0 caller records; outgoing 33-34); label_034.grep.txt sections A, C and D',
  'INFERRED')

sup(('Core_Factory.get', 'Core.<init>'), ('Core_Factory.get', 'Core_MembersInjector.injectOpenHelper'), ('Core_Factory.get', 'Core_MembersInjector.injectAppSettingsLazy'), ('Core_Factory.newCore', 'Core.<init>'))
sup(('Core.showChangelog', 'Core$2.<init>'))

UNREACHABLE['Core_Factory.get'] = ('no_trigger_in_app',
  'Dagger-generated Provider<Core>.get (dagger.internal.Factory implements Provider). Its only wrapper is DoubleCheck around the Lazy<Core> of SettingsActivity.coreLazy, which calls get only when the Lazy is read. No app source calls coreLazy.get() or any get() on a Provider<Core>. Its three outgoing records are cut by sup above',
  'SRC settings/SettingsActivity.java:37 (the only Lazy<Core> injection point; no coreLazy.get call); label_034.grep.txt sections A, C, D; Core_Factory.class and DaggerMmxComponent.class (Provider<Core> constant pool; javap not installed)',
  'INFERRED')

UNREACHABLE['Core_Factory.newCore'] = ('no_trigger_in_app',
  'Dagger-generated static method with no caller record in auto_calls.json and no app source reference. The component calls create (DaggerMmxComponent.java:192), not newCore. Its only outgoing record (Core_Factory.java:47) is cut by sup above',
  'auto_calls Core_Factory.java:47 (0 caller records); label_034.grep.txt sections A, C, D; DaggerMmxComponent.java:192',
  'INFERRED')
