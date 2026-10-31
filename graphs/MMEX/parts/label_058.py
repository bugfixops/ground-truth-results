# ================================================================== batch 058 (label_058): StockRepository (12 methods),
# StockRepositorySql (6), StockRepositorySql_Factory (3), StockRepository_Factory (3).
# Result: 14 REACHABLE, 10 UNREACHABLE (rows in graphs/MMEX/parts/label_058.md). Generated-class evidence: graphs/MMEX/parts/label_058.grep.txt.
# This file writes only:
#   - UNREACHABLE entries for 4 source methods with no caller (load(Integer[]), loadForSymbols, getEntities, StockRepositorySql.delete),
#   - UNREACHABLE entries for the 6 Dagger-generated factory methods (INFERRED),
#   - 18 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# No e() edges: every REACHABLE method already has an auto CALL record into it (auto_calls.json, USE_AUTO), and the Lazy hop
# into StockRepositorySql.<init> is already in graph_def.py (batch 046, line 3675). No ENV_/STATE_ constants, no imports.

# ------------------------------------------------------------------ UNREACHABLE: source methods with no caller

UNREACHABLE['StockRepository.load(Integer[])'] = ('no_trigger_in_app',
    'public, but no caller anywhere: the app loads a stock by an int id (InvestmentTransactionEditActivity.java:107, load(int)) and never by an id array; the auto CALLs out of this method are cut by sup below',
    'StockRepository.java:92 (decl), 95-109 (body); grep of the source root: no caller',
    'SOURCE')

UNREACHABLE['StockRepository.loadForSymbols'] = ('no_trigger_in_app',
    'public, but no caller anywhere (the name occurs only at its declaration, StockRepository.java:114); the auto CALLs out of this method are cut by sup below',
    'StockRepository.java:114 (decl), 117-126 (body); grep of the source root: no caller',
    'SOURCE')

UNREACHABLE['StockRepository.getEntities'] = ('no_trigger_in_app',
    'private helper; its only callers are load(Integer[]) (line 109) and loadForSymbols (line 126), both unreachable above; its auto CALL to Stock.from (line 192) is cut by sup below',
    'StockRepository.java:189 (decl), 192; callers at lines 109 and 126',
    'SOURCE')

UNREACHABLE['StockRepositorySql.delete'] = ('no_trigger_in_app',
    'delete(int) has no caller: no auto_calls record into it and no source call on a StockRepositorySql receiver; it does not override SqlRepositoryBase.delete(String, String...), so the base overload does not reach it; its CALL to SqlRepositoryBase.delete is cut by sup below',
    'StockRepositorySql.java:47-50; SqlRepositoryBase.java:50',
    'SOURCE')

# ------------------------------------------------------------------ UNREACHABLE: Dagger-generated factories (INFERRED; grep evidence in label_058.grep.txt)

UNREACHABLE['StockRepository_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is StockRepository_Factory.create (auto record, line 25), which has no caller',
    'StockRepository.java:44 (@Inject constructor, the reason Dagger generates the factory); auto_calls StockRepository_Factory.java:25',
    'INFERRED')

UNREACHABLE['StockRepository_Factory.create'] = ('no_trigger_in_app',
    'generated factory method; no auto_calls record into it and no source reference; DaggerMmxComponent.initialize (auto records) calls no StockRepository factory',
    'auto_calls StockRepository_Factory.java:25 (its own CALL, cut by sup); label_058.grep.txt',
    'INFERRED')

UNREACHABLE['StockRepository_Factory.get'] = ('no_trigger_in_app',
    'generated factory method; no caller; its CALL to StockRepository.<init> (line 21) is cut by sup below',
    'auto_calls StockRepository_Factory.java:21; label_058.grep.txt',
    'INFERRED')

UNREACHABLE['StockRepositorySql_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is StockRepositorySql_Factory.create (auto record, line 25), which has no caller; Dagger uses the RepositoryModule provider for StockRepositorySql instead',
    'StockRepositorySql.java:39 (@Inject constructor, the reason Dagger generates the factory); auto_calls StockRepositorySql_Factory.java:25',
    'INFERRED')

UNREACHABLE['StockRepositorySql_Factory.create'] = ('no_trigger_in_app',
    'generated factory method; no auto_calls record into it and no source reference; DaggerMmxComponent.initialize builds the StockRepositorySql provider with RepositoryModule_ProvideStockRepositoryFactory.create (auto line 196) instead',
    'auto_calls StockRepositorySql_Factory.java:25 (its own CALL, cut by sup); label_058.grep.txt',
    'INFERRED')

UNREACHABLE['StockRepositorySql_Factory.get'] = ('no_trigger_in_app',
    'generated factory method; no caller; its CALL to StockRepositorySql.<init> (line 21) is cut by sup below',
    'auto_calls StockRepositorySql_Factory.java:21; label_058.grep.txt',
    'INFERRED')

# ------------------------------------------------------------------ sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(
    # load(Integer[]): six callees
    ('StockRepository.load(Integer[])', 'MmxDatabaseUtils.<clinit>'),
    ('StockRepository.load(Integer[])', 'StockRepository.getEntities'),
    ('StockRepository.load(Integer[])', 'RepositoryBase.openCursor(String[],String,String[],String)'),
    ('StockRepository.load(Integer[])', 'MmxDatabaseUtils.makePlaceholders'),
    ('StockRepository.load(Integer[])', 'MmxDatabaseUtils.<init>'),
    ('StockRepository.load(Integer[])', 'RepositoryBase.getContext'),
    # loadForSymbols: the same six callees
    ('StockRepository.loadForSymbols', 'MmxDatabaseUtils.<clinit>'),
    ('StockRepository.loadForSymbols', 'StockRepository.getEntities'),
    ('StockRepository.loadForSymbols', 'RepositoryBase.openCursor(String[],String,String[],String)'),
    ('StockRepository.loadForSymbols', 'MmxDatabaseUtils.makePlaceholders'),
    ('StockRepository.loadForSymbols', 'MmxDatabaseUtils.<init>'),
    ('StockRepository.loadForSymbols', 'RepositoryBase.getContext'),
    # getEntities, StockRepositorySql.delete
    ('StockRepository.getEntities', 'Stock.from'),
    ('StockRepositorySql.delete', 'SqlRepositoryBase.delete'),
    # generated factories
    ('StockRepository_Factory.get', 'StockRepository.<init>'),
    ('StockRepository_Factory.create', 'StockRepository_Factory.<init>'),
    ('StockRepositorySql_Factory.get', 'StockRepositorySql.<init>'),
    ('StockRepositorySql_Factory.create', 'StockRepositorySql_Factory.<init>'),
)
