# label_046.py: batch 046 (40 methods in 7 classes): RepositoryModule (3), RepositoryModule_ProvideStockHistoryRepositoryFactory (4),
# RepositoryModule_ProvideStockRepositoryFactory (4), CurrencyChartActivity (5), CurrencyEditActivity (9), CurrencyEditViewHolder (2),
# CurrencyRepository (13). Result: 35 REACHABLE, 5 UNREACHABLE, 0 UNRESOLVED.
# Rows and printed lines: graphs/MMEX/parts/label_046.md. Grep evidence: graphs/MMEX/parts/label_046.grep.txt.
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - 8 edges that auto data cannot give (INTENT starts, LIFECYCLE, FRAMEWORK menu, ENTERS screen),
#   - 2 non-standard CALL edges into the Dagger factory get() methods (Lazy hop, INFERRED),
#   - 4 sup pairs: auto CALL records whose caller is UNREACHABLE in this batch and whose callee is also in batch 046 (D14).
# Edges into a method of this batch are written here (destination owner, D1).
# The Dagger generated classes and the DoubleCheck/Lazy hop are INFERRED (generated code not read in the source root).

# ================================================================== CurrencyChartActivity (screen entry, lifecycle, menu)

e('CurrencyListFragment.onContextItemSelected', 'CurrencyChartActivity.<init>', 'INTENT',
  'context-menu item 1 (chart) of the currency list builds an Intent for CurrencyChartActivity (ACTION_VIEW, symbol and base-currency extras) and starts it',
  evidence='SRC currency/list/CurrencyListFragment.java:155 (registerForContextMenu), 257-262 (case 1: Intent, extras, startActivity); SRC AndroidManifest.xml:320-323 (CurrencyChartActivity, no intent filter); FW-SRC core/java/android/app/Instrumentation.java:1170-1176 (newActivity: loadClass().newInstance()); FW-SRC core/java/android/app/ActivityThread.java:2669 (newActivity call). Source batch 049 is not merged; this edge is written here because the destination is in batch 046.')

e('CurrencyChartActivity.<init>', 'CurrencyChartActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('CurrencyChartActivity.onCreate', 'CurrencyChartActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu (inflates menu_currency_chart)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); SRC res/menu/menu_currency_chart.xml (item action_settings, showAsAction never)')

e('CurrencyChartActivity.onCreateOptionsMenu', 'CurrencyChartActivity.onOptionsItemSelected', 'FRAMEWORK',
  'the user selects an item of the chart options menu (action_settings, in the overflow): the framework calls onOptionsItemSelected. No S_ screen key exists for the chart screen (no new constants), so the edge starts at the menu builder; this is a decision for the coordinator (see label_046.md)',
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450); SRC currency/CurrencyChartActivity.java:61-74; SRC res/menu/menu_currency_chart.xml:17-18')

# ================================================================== CurrencyEditActivity (entry, lifecycle, screen)

e('CurrencyUIFeatures.startCurrencyEditActivity', 'CurrencyEditActivity.<init>', 'INTENT',
  'startCurrencyEditActivity builds an Intent for CurrencyEditActivity (ACTION_EDIT with KEY_CURRENCY_ID, or ACTION_INSERT when the id is null) and starts it',
  evidence='SRC currency/CurrencyUIFeatures.java:213-225 (Intent 215, ACTION_EDIT 219, ACTION_INSERT 221, startActivity 224); callers: SRC currency/list/CurrencyListFragment.java:245 (case 0, edit), 326 (FAB, insert); SRC currency/recycler/CurrencyRecyclerListFragment.java:173 (batch 050); SRC AndroidManifest.xml:219-226 (exported, EDIT/INSERT filters)')

e('CurrencyEditActivity.<init>', 'CurrencyEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('CurrencyEditActivity.onCreate', 'S_CURRENCY_EDIT', 'ENTERS',
  'the currency edit form is shown',
  evidence='SRC currency/CurrencyEditActivity.java:82 (setContentView R.layout.currency_edit_activity), 83 (showStandardToolbarActions)')

e('CurrencyEditActivity.onCreate', 'CurrencyEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity when it is paused (and on configuration change); the saved bundle is passed back to onCreate',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (performPauseActivity calls callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/ActivityThread.java:4713-4722; FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState)')

# ================================================================== Dagger factory get() (Lazy hop; INFERRED)

e('MorningstarPriceUpdater.savePrice', 'RepositoryModule_ProvideStockRepositoryFactory.get', 'CALL',
  'savePrice calls stockRepository.get(), a Dagger Lazy<StockRepositorySql>; the Lazy runs the factory provider get(), which calls RepositoryModule.provideStockRepository',
  cls='non_standard', via='Dagger Lazy<StockRepositorySql>.get: DoubleCheck calls the generated factory provider get (library and generated code INFERRED; not read)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:75 (@Inject Lazy<StockRepositorySql>), 278, 281 (stockRepository.get()); 190 (savePrice called from MorningstarPriceUpdater$2.call); SRC core/ioc/RepositoryModule.java:32-35; auto record RepositoryModule_ProvideStockRepositoryFactory.get -> RepositoryModule.provideStockRepository (factory line 29)')

e('MorningstarPriceUpdater.savePrice', 'RepositoryModule_ProvideStockHistoryRepositoryFactory.get', 'CALL',
  'savePrice calls stockHistoryRepository.get(), a Dagger Lazy<StockHistoryRepositorySql>; the Lazy runs the factory provider get(), which calls RepositoryModule.provideStockHistoryRepository',
  cls='non_standard', via='Dagger Lazy<StockHistoryRepositorySql>.get: DoubleCheck calls the generated factory provider get (library and generated code INFERRED; not read)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:76 (@Inject Lazy<StockHistoryRepositorySql>), 284 (stockHistoryRepository.get()); 190; SRC core/ioc/RepositoryModule.java:37-40; auto record RepositoryModule_ProvideStockHistoryRepositoryFactory.get -> RepositoryModule.provideStockHistoryRepository (factory line 29)')

# ================================================================== sup cuts (D14): auto CALL records whose caller is UNREACHABLE and whose callee is in batch 046

sup(('CurrencyRepository.load', 'CurrencyRepository.first'),
    ('CurrencyRepository.first', 'CurrencyRepository.query'),
    ('RepositoryModule_ProvideStockRepositoryFactory.proxyProvideStockRepository', 'RepositoryModule.provideStockRepository'),
    ('RepositoryModule_ProvideStockHistoryRepositoryFactory.proxyProvideStockHistoryRepository', 'RepositoryModule.provideStockHistoryRepository'))
# Not written here (callee in a later batch, that batch writes them): CurrencyRepository.load -> WhereStatementGenerator.<init>,
# addStatement(String,String,Integer), getWhere (batch 053); CurrencyRepository.query -> Currency.fromCursor (batch 065) and
# RepositoryBase.openCursor(String[],String,String[]) (batch 056).

# ================================================================== UNREACHABLE (batch 046)

UNREACHABLE['CurrencyRepository.load'] = ('no_trigger_in_app',
  'Public helper with no caller. No auto record has it as dst, and no source file calls CurrencyRepository.load (grep label_046.grep.txt section B). Its auto CALL to first (CurrencyRepository.java:58) is cut with sup; its auto CALLs to WhereStatementGenerator (55-58) are cut by batch 053.',
  'SRC currency/CurrencyRepository.java:54-59; label_046.grep.txt sections B and H',
  'SOURCE')

UNREACHABLE['CurrencyRepository.first'] = ('no_trigger_in_app',
  'Its only caller is load (auto CALL at CurrencyRepository.java:58), which has no caller, so first is never reached. The auto CALL to query (136) is cut with sup.',
  'SRC currency/CurrencyRepository.java:135-137, 58; auto_calls record load -> first (58); label_046.grep.txt section B',
  'SOURCE')

UNREACHABLE['CurrencyRepository.query'] = ('no_trigger_in_app',
  'Its only caller is first (auto CALL at CurrencyRepository.java:136), which is UNREACHABLE. Its auto CALLs to Currency.fromCursor (147, batch 065) and RepositoryBase.openCursor (140, batch 056) are cut by those batches.',
  'SRC currency/CurrencyRepository.java:139-153, 136; auto_calls records (grep section B); label_046.grep.txt section B',
  'SOURCE')

UNREACHABLE['RepositoryModule_ProvideStockRepositoryFactory.proxyProvideStockRepository'] = ('no_trigger_in_app',
  'Dagger proxy static method on the generated factory. No auto record has it as dst. DaggerMmxComponent.initialize calls the factory create (DaggerMmxComponent.java:196), not this proxy. Its auto CALL to RepositoryModule.provideStockRepository (factory line 40) is cut with sup.',
  'auto_calls record proxyProvideStockRepository -> RepositoryModule.provideStockRepository (RepositoryModule_ProvideStockRepositoryFactory.java:40); DaggerMmxComponent.java:196; out/build_report.txt:602; label_046.grep.txt section C',
  'INFERRED')

UNREACHABLE['RepositoryModule_ProvideStockHistoryRepositoryFactory.proxyProvideStockHistoryRepository'] = ('no_trigger_in_app',
  'Dagger proxy static method on the generated factory. No auto record has it as dst. DaggerMmxComponent.initialize calls the factory create (DaggerMmxComponent.java:199), not this proxy. Its auto CALL to RepositoryModule.provideStockHistoryRepository (factory line 40) is cut with sup.',
  'auto_calls record proxyProvideStockHistoryRepository -> RepositoryModule.provideStockHistoryRepository (RepositoryModule_ProvideStockHistoryRepositoryFactory.java:40); DaggerMmxComponent.java:199; out/build_report.txt:600; label_046.grep.txt section C',
  'INFERRED')

# The Done and Cancel listeners of MmxBaseFragmentActivity are shared by every toolbar screen, and their auto CALL edges
# fan out by class hierarchy. A CurrencyEditActivity receiver runs only its own override, so the other overrides are cut here.
# Each cut target keeps its own route through its onOptionsItemSelected edge.
sup(('MmxBaseFragmentActivity$2.onClick', 'CheckingTransactionEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'RecurringTransactionEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'AccountEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'SplitCategoriesActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'InvestmentTransactionEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'CheckingTransactionEditActivity.onActionCancelClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'RecurringTransactionEditActivity.onActionCancelClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'AccountEditActivity.onActionCancelClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'InvestmentTransactionEditActivity.onActionCancelClick'))
