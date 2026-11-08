# ================================================================== batch 053 (label_053): QueryCategorySubCategory (13 methods),
# QueryReportIncomeVsExpenses (3), SQLDataSet (2), SQLTypeTransaction.<clinit> (1), TableAssets (2), TransactionStatus (3),
# ViewMobileData (4), WhereStatementGenerator (11). 39 methods: 30 REACHABLE, 9 UNREACHABLE.
# Rows and printed lines: graphs/MMEX/parts/label_053.md.
# No e() edges and no SCREENS: every REACHABLE row rests on an auto_calls.json CALL record, which the build adds.
# This file writes:
#   - UNREACHABLE entries for: QueryCategorySubCategory.getCategSubName, setCategSubName and setValueFromCursor (no caller
#     reaches them), SQLDataSet.getAllColumns, TableAssets.<init> and getAllColumns, TransactionStatus.<init>,
#     ViewMobileData.getAllColumns, and ViewMobileData.setWhere (its only call sits in a branch that never runs),
#   - 13 sup pairs: auto CALL records whose caller is UNREACHABLE (D14a), plus the never-taken-branch cut for
#     QueryReportIncomeVsExpenses.initialize -> ViewMobileData.setWhere (a judgment call, flagged in the report), and the three
#     CurrencyRepository.load -> WhereStatementGenerator records that batch 046 deferred here (CurrencyRepository.load is
#     UNREACHABLE in batch 046, label_046.py:62-80).

# ================================================================== QueryCategorySubCategory: UNREACHABLE

UNREACHABLE['QueryCategorySubCategory.getCategSubName'] = ('no_trigger_in_app',
    'Getter with no caller. No source file calls it, and no auto record has it as dst. CATEGSUBNAME appears only as an SQL alias in the query resource, not as a call',
    'QueryCategorySubCategory.java:66-68; res/raw/query_categorysubcategory.sql:6, 17', 'SOURCE')

UNREACHABLE['QueryCategorySubCategory.setCategSubName'] = ('no_trigger_in_app',
    'Its only caller is setValueFromCursor (line 105), which has no caller, so this setter is never reached; the auto CALL is cut by sup below',
    'QueryCategorySubCategory.java:105 (auto record setValueFromCursor -> setCategSubName)', 'SOURCE')

UNREACHABLE['QueryCategorySubCategory.setValueFromCursor'] = ('no_trigger_in_app',
    'Override of the protected Dataset.setValueFromCursor (Dataset.java:122). No caller: no auto record (exact or cha) has it as dst. The base method is called only on receivers typed QueryAccountBills, which resolve to that class override (HomeFragment.java:822-823, AccountRepository.java:84)',
    'QueryCategorySubCategory.java:91-106; Dataset.java:122; auto_calls.json (no record with this dst)', 'SOURCE')

# ================================================================== SQLDataSet, TableAssets, TransactionStatus, ViewMobileData: UNREACHABLE

UNREACHABLE['SQLDataSet.getAllColumns'] = ('no_trigger_in_app',
    'Returns null (stub). No caller: no auto record (exact or cha) has it as dst. The abstract Dataset.getAllColumns has no call site that could dispatch here',
    'SQLDataSet.java:27-30; auto_calls.json (no record)', 'SOURCE')

UNREACHABLE['TableAssets.<init>'] = ('no_trigger_in_app',
    'The class is never instantiated (no new TableAssets in the app source) and no auto record has the constructor as dst. Its two auto CALLs (Dataset.<init>, DatasetType.<clinit>) are cut by sup below',
    'TableAssets.java:30-32; grep of the app source (no new TableAssets)', 'SOURCE')

UNREACHABLE['TableAssets.getAllColumns'] = ('no_trigger_in_app',
    'Returns the column list. No caller: the class is never instantiated and no auto record has it as dst',
    'TableAssets.java:34-37', 'SOURCE')

UNREACHABLE['TransactionStatus.<init>'] = ('no_trigger_in_app',
    'Implicit default constructor: the class declares no constructor and only static members are used (getStatusAsString and getBackgroundColorFromStatus are static). No new TransactionStatus in the app source, and no auto record has it as dst',
    'TransactionStatus.java:29, 34, 75; grep of the app source (no new TransactionStatus)', 'SOURCE')

UNREACHABLE['ViewMobileData.getAllColumns'] = ('no_trigger_in_app',
    'Returns the column list. No caller: no auto record (exact or cha) has it as dst',
    'ViewMobileData.java:72-79; auto_calls.json (no record)', 'SOURCE')

UNREACHABLE['ViewMobileData.setWhere'] = ('branch_never_taken',
    'Its only caller is QueryReportIncomeVsExpenses.initialize (line 50), inside the guard if(!TextUtils.isEmpty(whereStatement)) at line 49. initialize is called only from the constructor (line 33) with null, and TextUtils.isEmpty(null) is true, so the guarded call never runs. The auto CALL (line 50) is cut by sup below as a call in a branch that never runs',
    'ViewMobileData.java:81-83; QueryReportIncomeVsExpenses.java:33, 46-50; TextUtils.isEmpty(null) is true (Android API contract; framework source not in fw_src)', 'INFERRED')

# ================================================================== sup (D14a and never-taken branch)

sup(('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.getAllColumns'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setCategId'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setCategName'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setCategSubName'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setSubCategId'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setSubcategoryName'),
    ('TableAssets.<init>', 'Dataset.<init>'),
    ('TableAssets.<init>', 'DatasetType.<clinit>'),
    ('QueryReportIncomeVsExpenses.initialize', 'ViewMobileData.setWhere'),
    ('ViewMobileData.setWhere', 'ViewMobileData.initialize'),
    ('CurrencyRepository.load', 'WhereStatementGenerator.<init>'),
    ('CurrencyRepository.load', 'WhereStatementGenerator.addStatement(String,String,Integer)'),
    ('CurrencyRepository.load', 'WhereStatementGenerator.getWhere'))
