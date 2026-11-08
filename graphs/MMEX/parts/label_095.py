# batch 095 (label_095): 26 methods (graphs/MMEX/scratch/batches/batch_095.txt): YahooCsvQuoteDownloaderRetrofit (8: <init>, downloadPrices, finishIfAllDone, getYahooCsvService, onContentDownloaded, $1.<init>, $1.onFailure, $1.onResponse), YqlQueryGenerator (3), YqlSecurityPriceUpdaterRetrofit (10: <init>, downloadPrices, getPricesFromJson, getSecurityPriceFor, getYqlService, onContentDownloaded, readPrice, $1.<init>, $1.onFailure, $1.onResponse), CrashReportingTree (2), DebugTree (2), ErrorRaisedEvent (1).
# Rows, printed lines and counts: graphs/MMEX/parts/label_095.md (24 REACHABLE, 2 UNREACHABLE, 0 INCOMPLETE).
# Grep evidence: graphs/MMEX/parts/label_095.grep.txt (sections 1-6).
# This file writes:
#   - 0 SCREENS keys and 0 page edges (no GUI method in this batch);
#   - 6 e() edges, all with a destination in this batch (D1): 4 FRAMEWORK (Retrofit enqueue callbacks: downloadPrices -> $1.onResponse and $1.onFailure, for the CSV and the YQL downloaders) and 2 CALL (cls non_standard: the Timber.e calls in YahooCsv$1.onFailure and YqlSecurityPriceUpdaterRetrofit$1.onFailure dispatch to DebugTree.log);
#   - 2 UNREACHABLE entries (app source, SOURCE): CrashReportingTree.<init> and CrashReportingTree.log;
#   - 1 sup pair (D14): the auto CALL record CrashReportingTree.log -> ErrorRaisedEvent.<init> (its caller is UNREACHABLE in this batch).
# Not written (D7): every other auto CALL and CHA record into this batch (for example the factory's constructor calls, WatchlistFragment -> downloadPrices, DebugTree.<init> from MmexApplication.onCreate, DebugTree.log -> ErrorRaisedEvent.<init>); they come from graphs/MMEX/auto_calls.json and carry no needs_state. Their state gates (the quote provider setting) are kept in the batch rows only, and the callback edges below carry the gate.
# Known gap: the settings gate is on the callback edges, not on the auto CALL edges into the constructors and downloadPrices (D7), so those routes show no state gate in the graph.

# ---- gate texts (inline, D2). The CSV and YQL texts are the same strings as the state gates of batch 092 (parts/label_092.py)

# ================================================================== Yahoo CSV downloader: Retrofit callbacks (FRAMEWORK, library dispatch INFERRED)

e('YahooCsvQuoteDownloaderRetrofit.downloadPrices', 'YahooCsvQuoteDownloaderRetrofit$1.onResponse', 'FRAMEWORK',
  'Retrofit calls the Callback onResponse when the CSV request for a symbol gets a response; the method calls onContentDownloaded (line 71)',
  guard='symbols is not null and not empty (lines 60 and 62); the callback is queued for each symbol in the loop (line 84)',
  needs_state=state_text('the quote provider setting is YahooCsv (set in the Change provider dialog)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:59-62, 68-72, 82-84 (anonymous Callback at 68, onResponse at 70-72, enqueue at 84); SRC investment/SecurityPriceUpdaterFactory.java:47-48 (the YahooCsv case that creates this object); INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record YahooCsvQuoteDownloaderRetrofit$1.onResponse -> YahooCsvQuoteDownloaderRetrofit.onContentDownloaded (line 71)')

e('YahooCsvQuoteDownloaderRetrofit.downloadPrices', 'YahooCsvQuoteDownloaderRetrofit$1.onFailure', 'FRAMEWORK',
  'Retrofit calls the Callback onFailure when the CSV request fails before a response; the method closes the progress dialog (line 76) and logs through Timber (line 78)',
  guard='symbols is not null and not empty (lines 60 and 62); the callback is queued for each symbol in the loop (line 84)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  needs_state=state_text('the quote provider setting is YahooCsv (set in the Change provider dialog)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:59-62, 68, 74-79, 84 (onFailure at 75, closeProgressDialog at 76, Timber.e at 78, enqueue at 84); SRC investment/SecurityPriceUpdaterFactory.java:47-48; INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record YahooCsvQuoteDownloaderRetrofit$1.onFailure -> PriceUpdaterBase.closeProgressDialog (line 76)')

# ================================================================== Yahoo CSV failure path into the debug tree (CALL through Timber, library dispatch INFERRED)

e('YahooCsvQuoteDownloaderRetrofit$1.onFailure', 'DebugTree.log', 'CALL',
  'the Timber.e call at line 78 hands the failure to the planted trees; in the debug build the planted DebugTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='DebugTree is planted only in the debug branch (MmexApplication.java:134-135); the posted event needs a subscriber (DebugTree.java:45)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 78) calls each planted Tree.log (library source not read, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:74-79 (Timber.e at 78); SRC MmexApplication.java:134-135 (Timber.plant(new DebugTree()) in the debug branch); SRC log/DebugTree.java:34-46, 50; INFERRED Timber dispatch to planted trees (library not read)')

# ================================================================== Yql downloader: Retrofit callbacks (FRAMEWORK, library dispatch INFERRED). The YQL provider is the default

e('YqlSecurityPriceUpdaterRetrofit.downloadPrices', 'YqlSecurityPriceUpdaterRetrofit$1.onResponse', 'FRAMEWORK',
  'Retrofit calls the Callback onResponse with the YQL response; the method calls onContentDownloaded (line 90)',
  guard='symbols is not null and not empty (lines 75 and 77); the request is enqueued inside try (line 103)',
  needs_state=state_text('the quote provider setting is YahooYql (the default when the setting is unset)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:74-77, 87-91, 100-103 (anonymous Callback at 87, onResponse at 89-91, enqueue at 103); SRC investment/SecurityPriceUpdaterFactory.java:44-45, 50-52 (the YahooYql and default cases); SRC settings/InvestmentSettings.java:75; INFERRED Retrofit enqueue callback dispatch (library not read)')

e('YqlSecurityPriceUpdaterRetrofit.downloadPrices', 'YqlSecurityPriceUpdaterRetrofit$1.onFailure', 'FRAMEWORK',
  'Retrofit calls the Callback onFailure when the YQL request fails before a response; the method logs through Timber (line 95) and closes the progress dialog (line 96)',
  guard='symbols is not null and not empty (lines 75 and 77); the request is enqueued inside try (line 103)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  needs_state=state_text('the quote provider setting is YahooYql (the default when the setting is unset)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:74-77, 87, 93-97, 100-103 (onFailure at 94, Timber.e at 95, closeProgressDialog at 96, enqueue at 103); SRC investment/SecurityPriceUpdaterFactory.java:44-45, 50-52; SRC settings/InvestmentSettings.java:75; INFERRED Retrofit enqueue callback dispatch (library not read)')

e('YqlSecurityPriceUpdaterRetrofit$1.onFailure', 'DebugTree.log', 'CALL',
  'the Timber.e call at line 95 hands the failure to the planted trees; in the debug build the planted DebugTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='DebugTree is planted only in the debug branch (MmexApplication.java:134-135); the posted event needs a subscriber (DebugTree.java:45)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 95) calls each planted Tree.log (library source not read, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:93-97 (Timber.e at 95); SRC MmexApplication.java:134-135 (Timber.plant(new DebugTree()) in the debug branch); SRC log/DebugTree.java:34-46, 50; INFERRED Timber dispatch to planted trees (library not read)')

# ================================================================== UNREACHABLE (batch 095). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['CrashReportingTree.<init>'] = ('no_trigger_in_app',
  'The class is never instantiated in the app: the only Timber.plant of a CrashReportingTree is commented out (MmexApplication.java:137), and no other source line creates one (label_095.grep.txt sections 1, 2, 5). The implicit default constructor therefore has no caller. The class is annotated @Deprecated (CrashReportingTree.java:32).',
  'SRC log/CrashReportingTree.java:32-33; SRC MmexApplication.java:133-140; label_095.grep.txt sections 1, 2, 5',
  'SOURCE')

UNREACHABLE['CrashReportingTree.log'] = ('no_trigger_in_app',
  'Timber calls a tree log() only for trees that were planted with Timber.plant. CrashReportingTree is never planted: MmexApplication.java:137 is commented out, and the debug branch plants DebugTree (line 135) while the release branch plants ScreenTree and SysLogTree (lines 138-139). No instance exists, so log() has no caller. Its auto_calls record CrashReportingTree.log -> ErrorRaisedEvent.<init> is cut by the sup pair below.',
  'SRC log/CrashReportingTree.java:34-56 (log, post at 56); SRC MmexApplication.java:133-140; label_095.grep.txt sections 1, 2, 3, 6',
  'SOURCE')

# ================================================================== sup pairs (D14): auto CALL record whose caller is UNREACHABLE in this batch

sup(('CrashReportingTree.log', 'ErrorRaisedEvent.<init>'))
