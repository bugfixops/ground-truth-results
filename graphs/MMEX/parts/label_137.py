# ================================================================== batch 137 (label_137): MmxDatabaseUtils (20 methods), MmxDatabaseUtils_Factory (4), MmxDatabaseUtils_MembersInjector (6); 30 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_137.md (18 REACHABLE, 12 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_137.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 12 UNREACHABLE entries and 21 sup pairs.
# Every route into this batch is a CALL edge from auto_calls.json (USE_AUTO, D7), so none is written here. Batch 137 owns no framework callback.
# The callers of this batch's methods are in batches 115, 080, 077, 041, 040, 123, 054, 055, 049 and 044 (all merged), so no route is interim (D8).
# sup() cuts the auto CALL records whose caller is UNREACHABLE in this batch, so the bytecode edge cannot run (D14). The sup pairs are listed by group below.
# Evidence labels: SRC = printed line of the source tree; INFERRED = generated Dagger code or javac behaviour, source not read (not in the repo).

# ---- createDatabase group: no caller for the public overloads; createDatabase_Internal and its callees never run

sup(('MmxDatabaseUtils.createDatabase()', 'MmxDatabaseUtils.createDatabase(String)'))  # createDatabase() has no caller
sup(('MmxDatabaseUtils.createDatabase(String)', 'MmxDatabaseUtils.createDatabase_Internal'))  # createDatabase(String) has no caller
sup(('MmxDatabaseUtils.createDatabase_Internal', 'MmxDatabaseUtils.cleanupFilename'))  # createDatabase_Internal has no caller
sup(('MmxDatabaseUtils.createDatabase_Internal', 'DatabaseManager.getDefaultDatabaseDirectory'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'DatabaseManager.<init>'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'AppSettings.getDatabaseSettings'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'AppSettings.<init>'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'DatabaseSettings.setDatabasePath'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'MmxDatabaseUtils.getContext'))

# ---- Dagger factory (generated, INFERRED): no caller of create, get or newMmxDatabaseUtils

sup(('MmxDatabaseUtils_Factory.create', 'MmxDatabaseUtils_Factory.<init>'))  # create has no caller
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils.<clinit>'))  # get has no caller
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils.<init>'))
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils_MembersInjector.injectMDatabasesLazy'))
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils_MembersInjector.injectOpenHelper'))
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils_MembersInjector.injectInfoRepositorySqlLazy'))
sup(('MmxDatabaseUtils_Factory.newMmxDatabaseUtils', 'MmxDatabaseUtils.<clinit>'))  # newMmxDatabaseUtils has no caller
sup(('MmxDatabaseUtils_Factory.newMmxDatabaseUtils', 'MmxDatabaseUtils.<init>'))

# ---- Dagger members injector (generated, INFERRED): create has no caller, so the injector object is never built; injectMembers has no caller

sup(('MmxDatabaseUtils_MembersInjector.create', 'MmxDatabaseUtils_MembersInjector.<init>'))  # create has no caller
sup(('MmxDatabaseUtils_MembersInjector.injectMembers', 'MmxDatabaseUtils_MembersInjector.injectInfoRepositorySqlLazy'))  # injectMembers has no caller
sup(('MmxDatabaseUtils_MembersInjector.injectMembers', 'MmxDatabaseUtils_MembersInjector.injectOpenHelper'))
sup(('MmxDatabaseUtils_MembersInjector.injectMembers', 'MmxDatabaseUtils_MembersInjector.injectMDatabasesLazy'))

# ---- UNREACHABLE: SOURCE = no caller in the app source (grep output: graphs/MMEX/parts/label_137.grep.txt)

UNREACHABLE['MmxDatabaseUtils.createDatabase()'] = (
  'no_trigger_in_app',
  'public no-argument overload with no caller. No createDatabase call on an MmxDatabaseUtils receiver exists in the source root: the createDatabase calls in the app are FileStorageHelper.createDatabase(Intent) (SelectDatabaseActivity.java:83, MainActivity.java:331). Its only callee is createDatabase(String).',
  'utils/MmxDatabaseUtils.java:133-135; grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.createDatabase(String)'] = (
  'no_trigger_in_app',
  'public overload whose only caller is createDatabase(), which has no caller. Its only callee is createDatabase_Internal (line 147).',
  'utils/MmxDatabaseUtils.java:143-152; grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.createDatabase_Internal'] = (
  'no_trigger_in_app',
  'private; its only caller is createDatabase(String) (line 147), which is UNREACHABLE. Its callees (cleanupFilename, DatabaseManager, AppSettings, DatabaseSettings, getContext at lines 264-285) never run.',
  'utils/MmxDatabaseUtils.java:261-288; auto_calls createDatabase_Internal records (lines 264, 267, 285); grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.cleanupFilename'] = (
  'no_trigger_in_app',
  'private; its only caller is createDatabase_Internal (line 264), which is UNREACHABLE. No other auto record into it.',
  'utils/MmxDatabaseUtils.java:264, 290-303; grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.isEncryptedDatabase'] = (
  'no_trigger_in_app',
  'public static with no caller: the grep of the source root finds only its declaration, and no auto record has it as callee.',
  'utils/MmxDatabaseUtils.java:74-76; grep label_137.grep.txt',
  'SOURCE')

# ---- UNREACHABLE: INFERRED = generated Dagger code (not in the repo; source not read); no caller in auto_calls.json or the bytecode

UNREACHABLE['MmxDatabaseUtils_Factory.<init>'] = (
  'no_trigger_in_app',
  'constructor of the Dagger factory, reached only from MmxDatabaseUtils_Factory.create (auto record at line 53). create has no caller, so the constructor never runs. Generated code: INFERRED, source not read.',
  'auto_calls.json (create -> <init>, MmxDatabaseUtils_Factory.java:53); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_Factory.create'] = (
  'no_trigger_in_app',
  'static factory of the Dagger factory with no caller: no auto record has it as callee, and DaggerMmxComponent.class has no reference to MmxDatabaseUtils_Factory (binary grep count 0). MmxComponent declares only inject(MmxDatabaseUtils) at line 101, with no provision method, so the component never asks for a factory. Generated code: INFERRED, source not read.',
  'core/ioc/MmxComponent.java:101; auto_calls.json; graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_Factory.get'] = (
  'no_trigger_in_app',
  'instance method of the Dagger factory with no caller: no auto record has it as callee, and no class in the build references MmxDatabaseUtils_Factory except the factory itself. Its CALLs (lines 38-43) are cut by sup. Generated code: INFERRED, source not read.',
  'auto_calls.json (get -> <clinit>, <init>, injectX at lines 38-43); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_Factory.newMmxDatabaseUtils'] = (
  'no_trigger_in_app',
  'generated helper of the Dagger factory with no caller. Its CALLs to MmxDatabaseUtils.<clinit> and <init> (line 58) are cut by sup. Generated code: INFERRED, source not read.',
  'auto_calls.json (newMmxDatabaseUtils -> <clinit>, <init>, line 58); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_MembersInjector.<init>'] = (
  'no_trigger_in_app',
  'constructor of the Dagger members injector, reached only from MmxDatabaseUtils_MembersInjector.create (auto record at line 36). create has no caller. Generated code: INFERRED, source not read.',
  'auto_calls.json (create -> <init>, MmxDatabaseUtils_MembersInjector.java:36); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_MembersInjector.create'] = (
  'no_trigger_in_app',
  'static factory of the Dagger members injector with no caller: no auto record has it as callee. DaggerMmxComponent.injectMmxDatabaseUtils calls the three static injectX methods directly (DaggerMmxComponent.java:533, 535, 537), so no injector object is built. Generated code: INFERRED, source not read.',
  'auto_calls.json (DaggerMmxComponent.injectMmxDatabaseUtils -> injectX at 533, 535, 537); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_MembersInjector.injectMembers'] = (
  'no_trigger_in_app',
  'instance method reached only through the MembersInjector interface on an injector object, which only create would build; create has no caller. No auto record has injectMembers as callee. Its three CALLs (lines 42-44) are cut by sup. Generated code: INFERRED, source not read.',
  'auto_calls.json (injectMembers -> injectX at lines 42-44); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')
