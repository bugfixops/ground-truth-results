# label_045.py: batch 045 (39 methods in 9 classes): DbModule, DbModule$1, DbModule_ProvideDatabaseFactory,
# DbModule_ProvideOpenHelperFactory, DbModule_ProvideSqlBriteFactory, MmxModule, MmxModule_ProvideAppContextFactory,
# MmxModule_ProvideAppSettingsFactory, MmxModule_ProvideApplicationFactory, MmxModule_ProvideSharedPreferencesFactory.
# Evidence: graphs/MMEX/parts/label_045.md (table) and label_045.grep.txt (sections A-D).
#
# Labels: 32 REACHABLE (routes through auto CALL edges and merged rows, plus the e() hops below) and
# 7 UNREACHABLE (the Dagger proxyProvideX static helpers: generated, no caller in SRC or any class file).
# The auto CALL edges already present (factory get -> provideX, proxy -> provideX, create -> <init>, initialize -> create,
# injectX chains) are not repeated here. None of the e() pairs below exists in auto_calls.json (checked before writing).
# Every Dagger/Lazy/Provider hop is cls='non_standard' with via=...

# --- Dagger Provider<T>.get() hops between generated factories and their providers (generated code not in SRC: INFERRED)

e('DbModule_ProvideDatabaseFactory.get', 'DbModule_ProvideSqlBriteFactory.get', 'CALL',
  'DbModule_ProvideDatabaseFactory.get passes the result of its Provider<SqlBrite> argument into DbModule.provideDatabase',
  cls='non_standard',
  via='Dagger Provider<SqlBrite>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED DbModule.java:61 provideDatabase(SqlBrite sqlBrite, MmxOpenHelper helper) takes a SqlBrite argument; generated factory not in SRC')

e('DbModule_ProvideDatabaseFactory.get', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'DbModule_ProvideDatabaseFactory.get passes the result of its Provider<MmxOpenHelper> argument into DbModule.provideDatabase',
  cls='non_standard',
  via='Dagger Provider<MmxOpenHelper>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED DbModule.java:61 provideDatabase(SqlBrite sqlBrite, MmxOpenHelper helper) takes an MmxOpenHelper argument; generated factory not in SRC')

e('DbModule_ProvideOpenHelperFactory.get', 'MmxModule_ProvideApplicationFactory.get', 'CALL',
  'DbModule_ProvideOpenHelperFactory.get passes the result of its Provider<MmexApplication> argument into DbModule.provideOpenHelper',
  cls='non_standard',
  via='Dagger Provider<MmexApplication>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED DbModule.java:46 provideOpenHelper(MmexApplication app) takes an MmexApplication argument; generated factory not in SRC')

e('MmxModule_ProvideAppSettingsFactory.get', 'MmxModule_ProvideApplicationFactory.get', 'CALL',
  'MmxModule_ProvideAppSettingsFactory.get passes the result of its Provider<MmexApplication> argument into MmxModule.provideAppSettings',
  cls='non_standard',
  via='Dagger Provider<MmexApplication>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED MmxModule.java:67 provideAppSettings(MmexApplication application) takes an MmexApplication argument; generated factory not in SRC')

# --- Dagger Lazy<T>.get() consumer sites (SRC call site; DoubleCheck calls the factory provider: library/generated, INFERRED)

e('MmxContentProvider.insert', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.insert calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :168 (openHelper.get().getWritableDatabase()) inside insert (151)')

e('MmxContentProvider.update', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.update calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :198 (openHelper.get().getWritableDatabase()) inside update (191)')

e('MmxContentProvider.delete', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.delete calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :247 (openHelper.get().getWritableDatabase()) inside delete (228)')

e('MmxContentProvider.query_internal', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.query_internal calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :384 (openHelper.get().getReadableDatabase()) inside query_internal (372)')

e('DatabaseSettingsFragment.onCreate', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'DatabaseSettingsFragment.onCreate calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC settings/DatabaseSettingsFragment.java:58 (field Lazy<MmxOpenHelper> openHelper), :85 (openHelper.get().getSQLiteVersion()) inside onCreate (62)')

e('DatabaseSettingsFragment.refreshDbVersion', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'DatabaseSettingsFragment.refreshDbVersion calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC settings/DatabaseSettingsFragment.java:58 (field Lazy<MmxOpenHelper> openHelper), :136 (openHelper.get().getReadableDatabase()) inside refreshDbVersion (131)')

e('Core.getLastPayeeUsed', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'Core.getLastPayeeUsed calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC core/Core.java:71 (field Lazy<MmxOpenHelper> openHelper), :147 (openHelper.get().getReadableDatabase().query(sql)) inside getLastPayeeUsed (135)')

e('MmxDatabaseUtils.checkIntegrity', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxDatabaseUtils.checkIntegrity calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC utils/MmxDatabaseUtils.java:101 (field Lazy<MmxOpenHelper> openHelper), :114 (openHelper.get().getReadableDatabase()) inside checkIntegrity (113)')

e('MmxDatabaseUtils.getTableNamesFromDb', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxDatabaseUtils.getTableNamesFromDb calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC utils/MmxDatabaseUtils.java:101 (field Lazy<MmxOpenHelper> openHelper), :339 (openHelper.get().getReadableDatabase()) inside getTableNamesFromDb (338)')

e('BudgetAdapter.loadTotalFor', 'DbModule_ProvideDatabaseFactory.get', 'CALL',
  'BudgetAdapter.loadTotalFor calls databaseLazy.get() (Lazy<BriteDatabase>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<BriteDatabase>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC budget/BudgetAdapter.java:85 (field Lazy<BriteDatabase> databaseLazy), :278 (databaseLazy.get().query(query)) inside loadTotalFor (265)')

e('UIHelper.getThemeId', 'MmxModule_ProvideAppSettingsFactory.get', 'CALL',
  'UIHelper.getThemeId calls appSettingsLazy.get() (Lazy<AppSettings>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<AppSettings>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC core/UIHelper.java:78 (field Lazy<AppSettings> appSettingsLazy), :178 (appSettingsLazy.get().getGeneralSettings().getTheme()) inside getThemeId (175)')

e('AppSettings.getPreferences', 'MmxModule_ProvideSharedPreferencesFactory.get', 'CALL',
  'AppSettings.getPreferences calls sharedPreferences.get() (Lazy<SharedPreferences>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<SharedPreferences>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC settings/AppSettings.java:44 (field Lazy<SharedPreferences> sharedPreferences), :57 (return sharedPreferences.get()) inside getPreferences (56)')

# --- Dagger component paths to providers whose Context/MmexApplication argument is supplied by a provider (INFERRED)

e('DaggerMmxComponent.getCurrencyService', 'MmxModule_ProvideAppContextFactory.get', 'CALL',
  'DaggerMmxComponent.getCurrencyService passes the Context from the provideAppContext provider into CurrencyService_Factory.newCurrencyService',
  cls='non_standard',
  via='Dagger Provider<Context>.get: generated component calls the DoubleCheck-wrapped provider (generated code, INFERRED; not read)',
  evidence='INFERRED DaggerMmxComponent.java:159 calls CurrencyService_Factory.newCurrencyService, whose descriptor takes android.content.Context (CurrencyService_Factory.class, label_045.grep.txt B); DaggerMmxComponent.class references MmxModule_ProvideAppContextFactory (grep B)')

e('BudgetAdapter.loadTotalFor', 'DbModule$1.log', 'CALL',
  'BudgetAdapter.loadTotalFor runs a BriteDatabase.query; with logging enabled the SqlBrite Logger (DbModule$1.log) receives the message',
  cls='non_standard',
  via='SqlBrite BriteDatabase.query calls the Logger.log callback when setLoggingEnabled(true) (library behaviour, INFERRED; library source not read)',
  evidence='SRC budget/BudgetAdapter.java:278 (databaseLazy.get().query(query)); SRC DbModule.java:55-57 (Logger.log body), :69 (db.setLoggingEnabled(true))')

# --- sup(): cut the 7 auto proxy -> provide CALL edges (callers are UNREACHABLE; generated, no caller)

sup(('DbModule_ProvideDatabaseFactory.proxyProvideDatabase', 'DbModule.provideDatabase'))
sup(('DbModule_ProvideOpenHelperFactory.proxyProvideOpenHelper', 'DbModule.provideOpenHelper'))
sup(('DbModule_ProvideSqlBriteFactory.proxyProvideSqlBrite', 'DbModule.provideSqlBrite'))
sup(('MmxModule_ProvideAppContextFactory.proxyProvideAppContext', 'MmxModule.provideAppContext'))
sup(('MmxModule_ProvideAppSettingsFactory.proxyProvideAppSettings', 'MmxModule.provideAppSettings'))
sup(('MmxModule_ProvideApplicationFactory.proxyProvideApplication', 'MmxModule.provideApplication'))
sup(('MmxModule_ProvideSharedPreferencesFactory.proxyProvideSharedPreferences', 'MmxModule.provideSharedPreferences'))

# --- UNREACHABLE: generated Dagger proxy helpers with no caller (grep A: 0 SRC hits; grep B: name only in its own factory class)

UNREACHABLE['DbModule_ProvideDatabaseFactory.proxyProvideDatabase'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in DbModule_ProvideDatabaseFactory.class (grep B)',
    'DbModule_ProvideDatabaseFactory.java:47; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['DbModule_ProvideOpenHelperFactory.proxyProvideOpenHelper'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in DbModule_ProvideOpenHelperFactory.class (grep B)',
    'DbModule_ProvideOpenHelperFactory.java:37; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['DbModule_ProvideSqlBriteFactory.proxyProvideSqlBrite'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in DbModule_ProvideSqlBriteFactory.class (grep B)',
    'DbModule_ProvideSqlBriteFactory.java:30; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideAppContextFactory.proxyProvideAppContext'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideAppContextFactory.class (grep B)',
    'MmxModule_ProvideAppContextFactory.java:30; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideAppSettingsFactory.proxyProvideAppSettings'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideAppSettingsFactory.class (grep B)',
    'MmxModule_ProvideAppSettingsFactory.java:39; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideApplicationFactory.proxyProvideApplication'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideApplicationFactory.class (grep B)',
    'MmxModule_ProvideApplicationFactory.java:30; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideSharedPreferencesFactory.proxyProvideSharedPreferences'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideSharedPreferencesFactory.class (grep B)',
    'MmxModule_ProvideSharedPreferencesFactory.java:31; label_045.grep.txt A, B',
    'INFERRED')
