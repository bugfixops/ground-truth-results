# ================================================================== batch 055 (label_055)
# CurrencyRepositorySql (2), CurrencyRepositorySql_Factory (4), InfoRepositorySql (5), InfoRepositorySql_Factory (3),
# PayeeRepository (6), QueryAllDataRepository (4), RecurringTransactionRepository (7). 31 methods.
# Result: 28 REACHABLE, 3 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_055.md.
# Auto CALL records (auto_calls.json) are not rewritten here (D7). This file writes:
#   - 4 non_standard CALL edges for the Dagger Provider and Lazy hops into the generated factories
#     (these get() calls are not source calls, so auto_calls.json has no record for them),
#   - 3 UNREACHABLE entries (app source, no caller anywhere in src/main),
#   - 1 sup pair (D14a): the auto CALL from the UNREACHABLE QueryAllDataRepository.add.
# Open point: CurrencyService_Factory.get is batch 047's; label_047.py:40 says UNREACHABLE, but the bytecode shows
# FormatUtilities_Factory.get -> CurrencyService_Factory.get (offset 25). The edge belongs to batch 047 (D1: owner by destination).

# ================================================================== CurrencyRepositorySql_Factory.get: Provider hop

e('CurrencyService_Factory.get', 'CurrencyRepositorySql_Factory.get', 'CALL',
  'CurrencyService_Factory.get calls its repository Provider (mRepositoryProvider.get); the Provider is the CurrencyRepositorySql_Factory instance built in DaggerMmxComponent.initialize',
  evidence='INFERRED app/build/intermediates/javac/debug/classes/com/money/manager/ex/currency/CurrencyService_Factory.class: get offset 8 contextProvider.get, offset 25 mRepositoryProvider.get (invokeinterface Provider.get), offset 33 injectMRepository; core/ioc/DaggerMmxComponent.class initialize offset 86 (CurrencyRepositorySql_Factory.create), 89 putfield, 98 getfield (passed to CurrencyService_Factory.create)',
  cls='non_standard',
  via='javax.inject.Provider mRepositoryProvider (generated field), whose runtime class is CurrencyRepositorySql_Factory')

# ================================================================== InfoRepositorySql_Factory.get: Lazy hops

e('MmxDatabaseUtils.fixDuplicates', 'InfoRepositorySql_Factory.get', 'CALL',
  'fixDuplicates calls infoRepositorySqlLazy.get() (line 158); the Lazy wraps the InfoRepositorySql_Factory Provider, so get() runs the factory get before loadAll and delete',
  evidence='SRC utils/MmxDatabaseUtils.java:102 (@Inject Lazy field), 158 (get), 159 (loadAll), 169 (delete); GEN core/ioc/DaggerMmxComponent.class injectMmxDatabaseUtils offset 24 getfield infoRepositorySqlProvider, 27 DoubleCheck.lazy, 30 MembersInjector.injectInfoRepositorySqlLazy',
  cls='non_standard',
  via='dagger.internal.DoubleCheck (the Lazy), then javax.inject.Provider.get on InfoRepositorySql_Factory')

e('Passcode.savePasscode', 'InfoRepositorySql_Factory.get', 'CALL',
  'savePasscode calls infoRepositorySqlLazy.get() (line 158) before insert or update; savePasscode is reached from setPasscode (line 80)',
  evidence='SRC core/Passcode.java:47 (@Inject Lazy field), 78-80 (setPasscode calls savePasscode), 153-158 (savePasscode, get at 158); GEN core/ioc/DaggerMmxComponent.class injectPasscode offset 2 getfield infoRepositorySqlProvider, 5 DoubleCheck.lazy, 8 MembersInjector.injectInfoRepositorySqlLazy',
  cls='non_standard',
  via='dagger.internal.DoubleCheck (the Lazy), then javax.inject.Provider.get on InfoRepositorySql_Factory')

e('Passcode.clearPasscode_Internal', 'InfoRepositorySql_Factory.get', 'CALL',
  'clearPasscode_Internal calls infoRepositorySqlLazy.get() (line 136) before the delete; reached from clearPasscode (line 85)',
  evidence='SRC core/Passcode.java:83-85 (clearPasscode calls clearPasscode_Internal), 135-136 (get at 136), 137 onward (repo.delete with Info.INFONAME); GEN core/ioc/DaggerMmxComponent.class injectPasscode offsets 2-8 (same Lazy wiring as above)',
  cls='non_standard',
  via='dagger.internal.DoubleCheck (the Lazy), then javax.inject.Provider.get on InfoRepositorySql_Factory')

# ================================================================== UNREACHABLE: app source with no caller

UNREACHABLE['QueryAllDataRepository.add'] = ('no_trigger_in_app',
    'no caller: QueryAllDataRepository is constructed in one place (CalculateRunningBalanceTask2.java:182) and only query() is called on it; add(AccountTransactionDisplay) is a plain method that calls insert(entity.contentValues), not an override, and no auto CALL record names it',
    'datalayer/QueryAllDataRepository.java:55-57; account/CalculateRunningBalanceTask2.java:182-183; grep of src/main: QueryAllDataRepository appears in 2 files only', 'SOURCE')

UNREACHABLE['QueryAllDataRepository.getAllColumns'] = ('no_trigger_in_app',
    'no caller: the override is reached only by a getAllColumns() call whose receiver is QueryAllDataRepository, and there is none (the getAllColumns() call sites in src/main have other receiver types, e.g. QueryAllData at AllDataListFragment.java:243); no CHA or exact auto record names it',
    'datalayer/QueryAllDataRepository.java:40-53; common/AllDataListFragment.java:243; account/CalculateRunningBalanceTask2.java:182-183', 'SOURCE')

UNREACHABLE['RecurringTransactionRepository.getAllColumns'] = ('no_trigger_in_app',
    'no caller: RecurringTransactionRepository is used only for constructor, load, first, insert, update and delete in its call sites (MmxContentProvider, MainActivity, RecurringTransactionService, CheckingTransactionEditActivity, RecurringTransactionEditActivity, RecurringTransactionListFragment); the only getAllColumns() call near them is on QueryBillDeposits (RecurringTransactionListFragment.java:224); no CHA or exact auto record names it',
    'datalayer/RecurringTransactionRepository.java:39-57; recurring/transactions/RecurringTransactionListFragment.java:224', 'SOURCE')

# ================================================================== sup (D14a): auto CALL whose caller is UNREACHABLE here

sup(('QueryAllDataRepository.add', 'RepositoryBase.insert'))
