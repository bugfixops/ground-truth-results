# batch 043 (label_043): com.money.manager.ex.core.ioc.DaggerMmxComponent, methods 1-40 of 79 (40 methods). Rows and printed lines: graphs/MMEX/parts/label_043.md.
# Evidence: graphs/MMEX/parts/label_043.grep.txt. CALL edges come from auto_calls.json and are not written here.
# DaggerMmxComponent is Dagger-generated and has no source file in the source root: its labels are INFERRED.
# "SRC <path>" in the citations means final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/<path>.

# inject(EditPriceDialog) has no caller, so its call into injectEditPriceDialog cannot run.
sup(('DaggerMmxComponent.inject(EditPriceDialog)', 'DaggerMmxComponent.injectEditPriceDialog'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_043.grep.txt)

UNREACHABLE['DaggerMmxComponent.inject(StockRepositorySql)'] = ('no_trigger_in_app',
  'No live caller. The only reference to this injection in app source is commented out (datalayer/StockRepositorySql.java:43). auto_calls.json has no caller record for it, and every live iocComponent.inject call in app source passes this (grep section A)',
  'SRC datalayer/StockRepositorySql.java:43 (commented call); auto_calls.json (no caller record); label_043.grep.txt section A',
  'SOURCE')

UNREACHABLE['DaggerMmxComponent.inject(StockHistoryRepositorySql)'] = ('no_trigger_in_app',
  'No live caller. The only reference to this injection in app source is commented out (datalayer/StockHistoryRepositorySql.java:49). auto_calls.json has no caller record for it, and every live iocComponent.inject call in app source passes this (grep section A)',
  'SRC datalayer/StockHistoryRepositorySql.java:49 (commented call); auto_calls.json (no caller record); label_043.grep.txt section A',
  'SOURCE')

UNREACHABLE['DaggerMmxComponent.inject(EditPriceDialog)'] = ('no_trigger_in_app',
  'No live caller. No app code instantiates EditPriceDialog. The only reference to its constructor outside the class, WatchlistItemsFragment.java:255, is commented out, and PriceEditActivity.java:198-204 and WatchlistItemsFragment.java:246-252 only read or write ARG_ constants. auto_calls.json has zero records that call EditPriceDialog.<init>; its only EditPriceDialog.<init> record is the outgoing call to DaggerMmxComponent.inject(EditPriceDialog) at EditPriceDialog.java:91',
  'SRC investment/EditPriceDialog.java:69,89-91; investment/watchlist/WatchlistItemsFragment.java:246-252,255 (255 commented); investment/PriceEditActivity.java:198-204; label_043.grep.txt sections C and F',
  'SOURCE')

UNREACHABLE['DaggerMmxComponent.inject(ISecurityPriceUpdater)'] = ('no_trigger_in_app',
  'No live caller. core/ioc/MmxComponent.java:96 declares inject(ISecurityPriceUpdater), but no call site uses it: every live iocComponent.inject call in app source passes this, and the one class that implements ISecurityPriceUpdater and injects itself (MorningstarPriceUpdater.java:66) resolves to inject(MorningstarPriceUpdater). auto_calls.json has no caller record',
  'SRC core/ioc/MmxComponent.java:96; investment/morningstar/MorningstarPriceUpdater.java:66; label_043.grep.txt section A',
  'SOURCE')
