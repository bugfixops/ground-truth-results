# ================================================================== batch 111 (label_111): CategoryService (10), InfoService (7), InfoService_MembersInjector (4), PayeeService (7); 28 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_111.md. Class-file and grep evidence: graphs/MMEX/parts/label_111.grep.txt.
# 21 methods are REACHABLE and 7 are UNREACHABLE. No e(...) edges are written: every incoming edge to a batch 111 method is an auto CALL record (D7).
# sup pairs cut the auto records whose caller is UNREACHABLE in this batch (D14): 3 from CategoryService.createNewSubcategory, 5 from PayeeService.loadByName,
# 1 from PayeeService.exists, 1 from InfoService_MembersInjector.create and 1 from InfoService_MembersInjector.injectMembers.
# InfoService.insertRaw(SQLiteDatabase,String,String) has no outgoing auto record, so it needs no sup pair.
# Sources outside this batch (D1, interim until those batches merge): CheckingTransactionEditActivity.handleIntent and externalIntegration (exported ACTION_INSERT activity),
# IntentDataParameters.parseData, SplitCategoriesAdapter.bindCategory, QifRecord.getSplitCategory, MainActivity.onCreate, Passcode.loadPasscode,
# MmxOpenHelper.initDatabase, initDateFormat and initBaseCurrency, MmexApplication, CategoryListFragment and PayeeListFragment (batches 029 and 073 are REACHABLE for these callers).

# ---- UNREACHABLE (no_trigger_in_app). Tuple: (kind, reason, evidence, confirmed_by). Evidence: graphs/MMEX/parts/label_111.grep.txt.

UNREACHABLE['CategoryService.createNewSubcategory'] = ('no_trigger_in_app',
  'No caller in the app. The only occurrence of the name in the source is its definition. The category dialogs call createNew, getList, update and isCategoryUsed, never createNewSubcategory. No auto record has it as destination. Its three outgoing records are cut by sup pairs.',
  'SRC servicelayer/CategoryService.java:71-87 (definition); label_111.grep.txt section 1 (createNewSubcategory: definition only); auto_calls 2548-2550 (outgoing only)',
  'SOURCE')

UNREACHABLE['InfoService.insertRaw(SQLiteDatabase,String,String)'] = ('no_trigger_in_app',
  'No caller. The only insertRaw call in the app is MmxOpenHelper.java:296, and its db argument is a SupportSQLiteDatabase, so the SupportSQLiteDatabase overload is resolved (auto_calls 1162). No auto record has this overload as destination. It has no outgoing auto record, so no sup pair is needed.',
  'SRC servicelayer/InfoService.java:63-70 (definition); SRC database/MmxOpenHelper.java:256 (db is SupportSQLiteDatabase), 296; label_111.grep.txt section 1 (insertRaw); auto_calls 1162',
  'SOURCE')

UNREACHABLE['PayeeService.exists'] = ('no_trigger_in_app',
  'No caller. The grep for exists( finds the definition (PayeeService.java:105) and no call to PayeeService.exists in the app (the other hits belong to File, Repository and Service classes). No auto record has it as destination. Its outgoing record exists -> loadByName (line 108, auto_calls 2665) is cut by a sup pair.',
  'SRC servicelayer/PayeeService.java:105-110; label_111.grep.txt section 1 (exists); auto_calls 2665 (outgoing only)',
  'SOURCE')

UNREACHABLE['PayeeService.loadByName'] = ('no_trigger_in_app',
  'Its only caller is exists (PayeeService.java:108), and exists has no caller. No other source line or auto record calls loadByName. Its five outgoing records (auto_calls 2653-2657) are cut by sup pairs.',
  'SRC servicelayer/PayeeService.java:43-63, 108; label_111.grep.txt section 1 (loadByName); auto_calls 2665 (incoming), 2653-2657 (outgoing)',
  'SOURCE')

UNREACHABLE['InfoService_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller is create (auto_calls 2683), and create has no caller: no class file refers to create, and DaggerMmxComponent refers only to injectRepository.',
  'label_111.grep.txt sections 1, 2, 3 and 4 (auto_calls 2683); class-file parse of InfoService_MembersInjector.class (method table and self references)',
  'INFERRED')

UNREACHABLE['InfoService_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No class file refers to it: the binary grep finds the class name only in DaggerMmxComponent.class and in the injector class, and the parse of DaggerMmxComponent.class has no reference to create. No auto record has create as destination.',
  'label_111.grep.txt sections 1, 2, 3 and 4 (auto_calls 2683 outgoing, cut by sup pair)',
  'INFERRED')

UNREACHABLE['InfoService_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance injector (takes an InfoService). No class file calls it: DaggerMmxComponent refers only to injectRepository. The only reference inside the class is the synthetic bridge injectMembers(Object) (access 0x1041), which nothing refers to. No auto record has injectMembers as destination. Its outgoing record to injectRepository (auto_calls 2684) is cut by a sup pair.',
  'label_111.grep.txt sections 2, 3 and 4 (auto_calls 2684 outgoing, cut by sup pair)',
  'INFERRED')

# ---- sup pairs (D14): the auto records whose caller is UNREACHABLE in this batch. Names are the exact auto_calls names.

sup(('CategoryService.createNewSubcategory', 'Dataset.getUri'),
    ('CategoryService.createNewSubcategory', 'ServiceBase.getContext'),
    ('CategoryService.createNewSubcategory', 'CategoryRepository.<init>'),
    ('PayeeService.loadByName', 'EntityBase.loadFromCursor'),
    ('PayeeService.loadByName', 'Payee.<init>()'),
    ('PayeeService.loadByName', 'PayeeRepository.getAllColumns'),
    ('PayeeService.loadByName', 'Dataset.getUri'),
    ('PayeeService.loadByName', 'ServiceBase.getContext'),
    ('PayeeService.exists', 'PayeeService.loadByName'),
    ('InfoService_MembersInjector.create', 'InfoService_MembersInjector.<init>'),
    ('InfoService_MembersInjector.injectMembers', 'InfoService_MembersInjector.injectRepository'))
