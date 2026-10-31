# ================================================================== batch 090 (label_090): MorningstarPriceUpdater (7 methods), MorningstarPriceUpdater$1 (4), MorningstarPriceUpdater$2 (2), MorningstarPriceUpdater_Factory (4), MorningstarPriceUpdater_MembersInjector (5), SymbolConverter (4), ExchangeRateUpdaterBase (1), FixerService (6), FixerService$1 (3). 36 methods in all (graphs/MMEX/scratch/batches/batch_090.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_090.md (28 REACHABLE, 8 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_090.grep.txt (sections 1-6).
# This file writes:
#   - 6 e() edges (FRAMEWORK): processInParallel -> MorningstarPriceUpdater$1.onNext, onCompleted, onError; processInParallel -> MorningstarPriceUpdater$2.call (RxJava callbacks, library dispatch INFERRED); FixerService.downloadPrices -> FixerService$1.onResponse, onFailure (Retrofit callbacks, library dispatch INFERRED);
#   - 9 sup pairs (D14a): the auto CALL records whose caller is UNREACHABLE (Factory.create, Factory.get, Factory.newMorningstarPriceUpdater, MembersInjector.create, MembersInjector.injectMembers, ExchangeRateUpdaterBase.<init>);
#   - 8 UNREACHABLE entries: Factory.<init>, Factory.create, Factory.get, Factory.newMorningstarPriceUpdater, MembersInjector.<init>, create, injectMembers (generated, INFERRED, grep.txt sections 4-5); ExchangeRateUpdaterBase.<init> (app source, SOURCE).
# No SCREENS key (no new screen). No new constants (D2). Not written: no CALL edge that is already in auto_calls.json (D7). The watchlist and currency entry points stay interim (batches 092, 094 and the currency batches, not merged; D8).

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onNext', 'FRAMEWORK',
  'RxJava calls the Subscriber onNext for each emitted value; the method updates progress (line 213)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:193-213 (Subscriber created at 193; onNext at 211-213); INFERRED RxJava Subscriber dispatch (library not read); auto_calls.json record MorningstarPriceUpdater$1.onNext -> PriceUpdaterBase.setProgress (line 213)',
  via='RxJava Subscriber callback (library not read, INFERRED)')

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onCompleted', 'FRAMEWORK',
  'RxJava calls the Subscriber onCompleted when the observable completes; the method calls finishIfAllDone (line 197)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:193-213 (Subscriber created at 193; onCompleted at 196-197); INFERRED RxJava Subscriber dispatch (library not read); auto_calls.json record MorningstarPriceUpdater$1.onCompleted -> MorningstarPriceUpdater.finishIfAllDone (line 197)',
  via='RxJava Subscriber callback (library not read, INFERRED)')

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onError', 'FRAMEWORK',
  'RxJava calls the Subscriber onError when a request fails; the method sets progress and calls finishIfAllDone (line 207)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:193-213 (Subscriber created at 193; onError at 201-207); INFERRED RxJava Subscriber dispatch (library not read); auto_calls.json record MorningstarPriceUpdater$1.onError -> MorningstarPriceUpdater.finishIfAllDone (line 207)',
  via='RxJava Subscriber callback (library not read, INFERRED)')

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$2.call', 'FRAMEWORK',
  'RxJava calls the Action1 (doOnNext) for each emitted value; the body calls parse (line 189) and savePrice (line 190)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:185-191 (doOnNext Action1 created at 186; call at 188-191); INFERRED RxJava Action1 dispatch (library not read); auto_calls.json records MorningstarPriceUpdater$2.call -> MorningstarPriceUpdater.parse (line 189) and -> savePrice (line 190)',
  via='RxJava Action1 callback (library not read, INFERRED)')

e('FixerService.downloadPrices', 'FixerService$1.onResponse', 'FRAMEWORK',
  'Retrofit calls the Callback onResponse with the response; the method calls onContentDownloaded (line 79)',
  evidence='SRC investment/prices/FixerService.java:76-80 (anonymous Callback created at 76; onResponse at 78-79); SRC investment/prices/FixerService.java:93 (enqueue(callback)); INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record FixerService$1.onResponse -> FixerService.onContentDownloaded (line 79)',
  via='Retrofit enqueue callback (library not read, INFERRED)')

e('FixerService.downloadPrices', 'FixerService$1.onFailure', 'FRAMEWORK',
  'Retrofit calls the Callback onFailure when the request fails; the method closes the progress dialog (line 84)',
  evidence='SRC investment/prices/FixerService.java:83-84 (onFailure; closeProgressDialog at 84); SRC investment/prices/FixerService.java:93 (enqueue(callback)); INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record FixerService$1.onFailure -> PriceUpdaterBase.closeProgressDialog (line 84)',
  via='Retrofit enqueue callback (library not read, INFERRED)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(('MorningstarPriceUpdater_Factory.create', 'MorningstarPriceUpdater_Factory.<init>'),
    ('MorningstarPriceUpdater_Factory.get', 'MorningstarPriceUpdater_MembersInjector.injectStockHistoryRepository'),
    ('MorningstarPriceUpdater_Factory.get', 'MorningstarPriceUpdater_MembersInjector.injectStockRepository'),
    ('MorningstarPriceUpdater_Factory.get', 'MorningstarPriceUpdater.<init>'),
    ('MorningstarPriceUpdater_Factory.newMorningstarPriceUpdater', 'MorningstarPriceUpdater.<init>'),
    ('MorningstarPriceUpdater_MembersInjector.create', 'MorningstarPriceUpdater_MembersInjector.<init>'),
    ('MorningstarPriceUpdater_MembersInjector.injectMembers', 'MorningstarPriceUpdater_MembersInjector.injectStockHistoryRepository'),
    ('MorningstarPriceUpdater_MembersInjector.injectMembers', 'MorningstarPriceUpdater_MembersInjector.injectStockRepository'),
    ('ExchangeRateUpdaterBase.<init>', 'PriceUpdaterBase.<init>'))

# ================================================================== UNREACHABLE (batch 090). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['MorningstarPriceUpdater_Factory.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (flags 0x1, takes three Providers). Its only caller record is create (auto_calls.json, MorningstarPriceUpdater_Factory.java:45), and create has no caller: no class file has a Methodref to create or to the Factory, and the component refers only to the MembersInjector. The app source has no reference to the class.',
  'label_090.grep.txt section 4 (METHODS list; line 214: no class refers to the Factory) and section 1; auto_calls.json record MorningstarPriceUpdater_Factory.java:45 (section 5, line 286)',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_Factory.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory method (flags 0x9). No caller: no class file has a Methodref to create (label_090.grep.txt section 4), and DaggerMmxComponent refers only to the MembersInjector inject methods (lines 141-142), not to the Factory. No app source reference (section 1).',
  'class-file parse (label_090.grep.txt section 4, lines 141-142 and 214); grep of the app source root (section 1)',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_Factory.get'] = ('no_trigger_in_app',
  'Dagger-generated provider method (flags 0x1). Its only entry is create, which has no caller. Its outgoing records (to MorningstarPriceUpdater.<init> and to the two MembersInjector inject methods) are cut by the sup pairs above.',
  'auto_calls.json records MorningstarPriceUpdater_Factory.java:33, 34, 36 (label_090.grep.txt section 5, lines 283-285); section 4 line 214',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_Factory.newMorningstarPriceUpdater'] = ('no_trigger_in_app',
  'Dagger-generated static method (flags 0x9). No class file has a Methodref to it (label_090.grep.txt section 4). Its only outgoing record, to MorningstarPriceUpdater.<init>, is cut by the sup pair above.',
  'auto_calls.json record MorningstarPriceUpdater_Factory.java:50 (label_090.grep.txt section 5, line 287); section 4',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (flags 0x1, takes the two Providers). Its only caller record is create (auto_calls.json, MorningstarPriceUpdater_MembersInjector.java:31), and create has no caller (see create below).',
  'auto_calls.json record MorningstarPriceUpdater_MembersInjector.java:31 (label_090.grep.txt section 5, line 277); section 4 line 215',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory method (flags 0x9). No class file has a Methodref to create (label_090.grep.txt section 4). DaggerMmxComponent calls the static inject methods directly (DaggerMmxComponent.java:502 and 504), not create. No app source reference (section 1).',
  'class-file parse (label_090.grep.txt section 4, lines 141-142 and 215); auto_calls.json record MorningstarPriceUpdater_MembersInjector.java:31 (section 5, line 277); grep of the app source root (section 1)',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (flags 0x1, takes the updater). No class file has a Methodref to it (label_090.grep.txt section 4), and the component refers only to the static inject methods. Its outgoing records (to injectStockRepository at line 37 and injectStockHistoryRepository at line 38) are cut by the sup pairs above. The synthetic bridge injectMembers(Object) (flags 0x1041) is not in this batch (open point in label_090.md).',
  'class-file parse (label_090.grep.txt section 4, line 107); auto_calls.json records MorningstarPriceUpdater_MembersInjector.java:37-38 (section 5, lines 278-279)',
  'INFERRED')

UNREACHABLE['ExchangeRateUpdaterBase.<init>'] = ('no_trigger_in_app',
  'Constructor of a base class (ExchangeRateUpdaterBase.java:26-30) with no subclass and no referencing class: the app source has no reference to the class other than its own declaration, and no build class file refers to it (label_090.grep.txt section 4, line 210). Its only outgoing record, to PriceUpdaterBase.<init> (ExchangeRateUpdaterBase.java:29), is cut by the sup pair above.',
  'SRC investment/prices/ExchangeRateUpdaterBase.java:26-30; label_090.grep.txt sections 1, 4 (line 210), 5 (line 248)',
  'SOURCE')
