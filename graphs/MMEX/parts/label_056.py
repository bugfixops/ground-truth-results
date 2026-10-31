# ================================================================== batch 056 (label_056): RepositoryBase (16 methods),
# Select (8), SplitCategoriesRepository (7), SplitRecurringCategoriesRepository (8).
# Result: 30 REACHABLE, 9 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_056.md.
# Every bytecode CALL of this batch is already in auto_calls.json (D7), so this file writes no e() edges and no SCREENS.
# This file writes:
#   - UNREACHABLE entries for the 4 base-class helpers with no caller (add, bulkInsert, bulkUpdate, bulkDelete),
#     query(Class,String), Select.where(String,long[]), the two getAllColumns overrides and the recurring loadSplitCategoriesFor,
#   - 17 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.

# ================================================================== UNREACHABLE: base class and Select

UNREACHABLE['RepositoryBase.add'] = ('no_trigger_in_app',
    'the base add has no caller: PayeeService.createNew calls the PayeeRepository.add override (PayeeService.java:98) and no auto CALL record resolves to RepositoryBase.add; its body only forwards to insert',
    'datalayer/RepositoryBase.java:87-89; servicelayer/PayeeService.java:98', 'SOURCE')

UNREACHABLE['RepositoryBase.bulkDelete'] = ('no_trigger_in_app',
    'protected batch helper with no caller: grep of src/main finds only its definition, and no auto CALL record targets it',
    'datalayer/RepositoryBase.java:234-245', 'SOURCE')

UNREACHABLE['RepositoryBase.bulkInsert'] = ('no_trigger_in_app',
    'protected batch helper with no caller: grep of src/main finds only its definition, and no auto CALL record targets it',
    'datalayer/RepositoryBase.java:149-151', 'SOURCE')

UNREACHABLE['RepositoryBase.bulkUpdate'] = ('no_trigger_in_app',
    'protected batch helper with no caller: grep of src/main finds only its definition, and no auto CALL record targets it',
    'datalayer/RepositoryBase.java:213-224', 'SOURCE')

UNREACHABLE['RepositoryBase.query(Class,String)'] = ('no_trigger_in_app',
    'protected query with a String selection and no caller: both query call sites in src/main (CategoryService.java:118, CurrencyService.java:183) pass a Select and resolve to query(Class,Select); no auto CALL record targets query(Class,String)',
    'datalayer/RepositoryBase.java:168-171; servicelayer/CategoryService.java:116-118; currency/CurrencyService.java:179-183', 'SOURCE')

UNREACHABLE['Select.where(String,long[])'] = ('no_trigger_in_app',
    'the long varargs overload has no caller: no auto CALL record targets it and grep of src/main finds no where call with a long argument',
    'datalayer/Select.java:75-85', 'SOURCE')

# ================================================================== UNREACHABLE: Split repositories

UNREACHABLE['SplitCategoriesRepository.getAllColumns'] = ('no_trigger_in_app',
    'column-list override with no caller: no auto CALL record targets the Split override; the getAllColumns call sites resolve to other classes (for example QueryAccountBills.getAllColumns, HomeFragment.java:243)',
    'datalayer/SplitCategoriesRepository.java:40-49; home/HomeFragment.java:243', 'SOURCE')

UNREACHABLE['SplitRecurringCategoriesRepository.getAllColumns'] = ('no_trigger_in_app',
    'column-list override with no caller: no auto CALL record targets the recurring override; the getAllColumns call sites resolve to other classes',
    'datalayer/SplitRecurringCategoriesRepository.java:40-49', 'SOURCE')

UNREACHABLE['SplitRecurringCategoriesRepository.loadSplitCategoriesFor'] = ('no_trigger_in_app',
    'no caller: the loadSplitCategoriesFor call sites in src/main are on SplitCategoriesRepository only (CheckingTransactionEditActivity.java:399, QifRecord.java:145); no auto CALL record targets the recurring version',
    'datalayer/SplitRecurringCategoriesRepository.java:56-74; transactions/CheckingTransactionEditActivity.java:399; servicelayer/qif/QifRecord.java:145', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('RepositoryBase.add', 'RepositoryBase.insert'))
sup(('RepositoryBase.bulkInsert', 'Dataset.getUri'))
sup(('RepositoryBase.bulkInsert', 'RepositoryBase.getContext'))
sup(('RepositoryBase.bulkUpdate', 'MmxContentProvider.<clinit>'))
sup(('RepositoryBase.bulkUpdate', 'MmxContentProvider.getAuthority'))
sup(('RepositoryBase.bulkUpdate', 'RepositoryBase.getContext'))
sup(('RepositoryBase.bulkDelete', 'MmxContentProvider.<clinit>'))
sup(('RepositoryBase.bulkDelete', 'MmxContentProvider.getAuthority'))
sup(('RepositoryBase.bulkDelete', 'RepositoryBase.getContext'))
sup(('RepositoryBase.query(Class,String)', 'RepositoryBase.query(Class,Select)'))
sup(('RepositoryBase.query(Class,String)', 'Select.where(String)'))
sup(('RepositoryBase.query(Class,String)', 'Select.<init>()'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'SplitRecurringCategory.<clinit>'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'SplitRecurringCategory.loadFromCursor'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'SplitRecurringCategory.<init>'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'Dataset.getUri'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'RepositoryBase.getContext'))
