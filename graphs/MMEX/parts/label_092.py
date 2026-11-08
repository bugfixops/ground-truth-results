# ---- batch 092: WatchlistFragment (methods 1-40 of 55; WatchlistFragment$1 and $2 included).
# Edges are written for the destinations that this batch owns (D1). CALL edges already in auto_calls.json are not repeated (D7).
# UNREACHABLE entries: none. All 40 methods are REACHABLE (label_092.md, label_092.grep.txt).
# sup pairs: none (no UNREACHABLE caller in this batch).

SCREENS.update({
    'S_WATCHLIST': 'Watchlist screen (WatchlistFragment, shown inside MainActivity for one investment account): the account header with the favourite star, the account spinner in the action bar, the list of watched securities, and the options menu (update prices, export prices, purge history, change provider)',
})

# ---- fragment lifecycle and screen entry

e('WatchlistFragment.<init>', 'WatchlistFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor',
  evidence='SRC investment/watchlist/WatchlistFragment.java:93-125; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onCreate', 'WatchlistFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC WatchlistFragment.java:115-125, 142; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onCreateView', 'S_WATCHLIST', 'ENTERS',
  'the watchlist screen is shown: onCreateView inflates the layout and replaces the list fragment in fragmentMain',
  evidence='SRC WatchlistFragment.java:148 (layout inflate), 159-172 (child fragment replace at 171-172)')

e('WatchlistFragment.onCreateView', 'WatchlistFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView',
  evidence='SRC WatchlistFragment.java:142-183, 186-194; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onActivityCreated', 'WatchlistFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated',
  evidence='SRC WatchlistFragment.java:128-132, 186-194; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onStart', 'WatchlistFragment.onResume', 'LIFECYCLE',
  'the framework calls onResume after onStart',
  evidence='SRC WatchlistFragment.java:128-132, 197-205; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onResume', 'WatchlistFragment.onStop', 'LIFECYCLE',
  'the framework calls onStop when the watchlist screen is left (after onPause, which is not in this batch)',
  evidence='SRC WatchlistFragment.java:135-139; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onResume', 'WatchlistFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state while the watchlist screen is shown or left',
  evidence='SRC WatchlistFragment.java:277-281; same pattern as AccountTransactionListFragment (graph_def.py:823); INFERRED androidx Fragment lifecycle (library source not read)')

# ---- options menu

e('WatchlistFragment.onCreateView', 'WatchlistFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the fragment has its options menu enabled, so the host activity calls onCreateOptionsMenu when it builds its options menu',
  guard='setHasOptionsMenu(true) at line 178 has run (in onCreateView)',
  evidence='SRC WatchlistFragment.java:178, 213-245; INFERRED androidx FragmentManager dispatch (library source not read)')

gui('S_WATCHLIST', 'WatchlistFragment.onOptionsItemSelected',
    'Tap an item of the options menu of the watchlist screen: update prices, export prices, purge history or change provider',
    evidence='SRC res/menu/menu_watchlist.xml (menu_update_prices, menu_export_prices, menu_purge_history, menu_change_provider); SRC WatchlistFragment.java:254-274; INFERRED androidx FragmentManager dispatch (library source not read)')

# ---- the provider dialog opened by Change provider (the list click is dispatched by the platform AlertController)

gui('S_WATCHLIST', 'WatchlistFragment$1.onClick',
    'Tap a provider name in the quote provider dialog that the Change provider menu item opens',
    cls='non_standard',
    via='platform AlertDialog single-choice list: AlertController.java:1138-1142 calls mOnClickListener.onClick on an item click (FW-SRC read)',
    evidence='SRC WatchlistFragment.java:384-398 (setSingleChoiceItems at 386, onClick at 388-396); FW-SRC core/java/android/app/AlertDialog.java:936-941; FW-SRC core/java/com/android/internal/app/AlertController.java:1112, 1138-1142')

# ---- the update runnable is run on the UI thread by the platform

e('WatchlistFragment.completePriceUpdate', 'WatchlistFragment$2.run', 'FRAMEWORK',
  'getActivity().runOnUiThread runs the Runnable directly when the caller is already on the UI thread, otherwise it posts the Runnable to the handler',
  evidence='SRC WatchlistFragment.java:402-413 (runOnUiThread at 404, run at 406); FW-SRC core/java/android/app/Activity.java:6170-6176')

# ---- EventBus: registered in onStart (line 131), unregistered in onStop (line 138); the subscribers are the four @Subscribe methods

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(AllPricesDownloadedEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives AllPricesDownloadedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 285 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 285-288; INFERRED EventBus library source not read')

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives PriceDownloadedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 290 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 290-293; INFERRED EventBus library source not read')

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(PriceUpdateRequestEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives PriceUpdateRequestEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 295 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 295-298; INFERRED EventBus library source not read')

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(ErrorRaisedEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives ErrorRaisedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 300 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 300-303; INFERRED EventBus library source not read')

# ---- state gates for the price providers (InvestmentSettings.getQuoteProvider; the default is YahooYql at line 75)

STATE_YAHOO_CSV = state_text('the quote provider setting is YahooCsv (set in the Change provider dialog)', ('settings',))
STATE_MORNINGSTAR = state_text('the quote provider setting is Morningstar (set in the Change provider dialog)', ('settings',))
STATE_YAHOO_YQL = state_text('the quote provider setting is YahooYql (the default when the setting is unset)', ('settings',))

ENV_ERROR_LOGGED = env_text(
    'an error is logged through Timber while the watchlist fragment is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)',
    ('other',))

# ---- ASYNC: EventBus posts from the price downloaders, the watchlist items and the Timber trees into the subscribers

e('YahooCsvQuoteDownloaderRetrofit.finishIfAllDone', 'WatchlistFragment.onEvent(AllPricesDownloadedEvent)', 'ASYNC',
  'the CSV downloader posts AllPricesDownloadedEvent when every symbol is done; the registered watchlist fragment reloads its data',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_YAHOO_CSV,
  cls='non_standard', via='EventBus post at YahooCsvQuoteDownloaderRetrofit.java:100 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:91-100 (post at 100); SRC WatchlistFragment.java:131, 285-288; SRC settings/InvestmentSettings.java:74-86')

e('MorningstarPriceUpdater.finishIfAllDone', 'WatchlistFragment.onEvent(AllPricesDownloadedEvent)', 'ASYNC',
  'the Morningstar updater posts AllPricesDownloadedEvent when every symbol is done; the registered watchlist fragment reloads its data',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_MORNINGSTAR,
  cls='non_standard', via='EventBus post at MorningstarPriceUpdater.java:274 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:263-275 (post at 274); SRC WatchlistFragment.java:131, 285-288; SRC investment/SecurityPriceUpdaterFactory.java:41-42')

e('YahooCsvQuoteDownloaderRetrofit.onContentDownloaded', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'the CSV downloader posts the parsed PriceDownloadedEvent for a downloaded quote (only when the parse succeeded)',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_YAHOO_CSV,
  cls='non_standard', via='EventBus post at YahooCsvQuoteDownloaderRetrofit.java:124 (post(event)) to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:103-125 (post at 124); SRC WatchlistFragment.java:290-293')

e('YqlSecurityPriceUpdaterRetrofit.onContentDownloaded', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'the YQL downloader (the default provider) posts a PriceDownloadedEvent for each downloaded symbol; the registered watchlist fragment updates the price',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_YAHOO_YQL,
  cls='non_standard', via='EventBus post at YqlSecurityPriceUpdaterRetrofit.java:130 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:113-131 (post at 130); SRC investment/SecurityPriceUpdaterFactory.java:44-45, 50-52; SRC settings/InvestmentSettings.java:75; SRC WatchlistFragment.java:290-293')

e('FixerService.onContentDownloaded', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'FixerService posts a PriceDownloadedEvent for each currency rate it downloads; EventBus also delivers it to the registered watchlist fragment, which then runs onPriceDownloaded with the currency code',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  cls='non_standard', via='EventBus post at FixerService.java:120 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/prices/FixerService.java:100-121 (post at 120); SRC WatchlistFragment.java:290-293, 330-337; INFERRED EventBus library dispatch (library source not read)')

e('WatchlistItemsFragment.onContextItemSelected', 'WatchlistFragment.onEvent(PriceUpdateRequestEvent)', 'ASYNC',
  'the user chooses Download price in the context menu of a watchlist row; EventBus delivers PriceUpdateRequestEvent to the registered watchlist fragment',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  cls='non_standard', via='EventBus post at WatchlistItemsFragment.java:236 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:215-238 (post at 236); SRC WatchlistFragment.java:131, 295-298')

e('DebugTree.log', 'WatchlistFragment.onEvent(ErrorRaisedEvent)', 'ASYNC',
  'a debug build logs an error through Timber while the watchlist fragment is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent, which shows a toast',
  env=ENV_ERROR_LOGGED,
  guard='the fragment is registered (lines 131 and 138), and DebugTree posts only when a subscriber exists (DebugTree.java:45)',
  cls='non_standard', via='EventBus post at DebugTree.java:46 to the @Subscribe method onEvent(ErrorRaisedEvent) (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:34-47 (minLevel INFO, post at 46); SRC MmexApplication.java:134-135 (DebugTree planted in the debug branch); SRC WatchlistFragment.java:300-303')

e('ScreenTree.log', 'WatchlistFragment.onEvent(ErrorRaisedEvent)', 'ASYNC',
  'a release build logs an error through Timber while the watchlist fragment is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent, which shows a toast',
  env=ENV_ERROR_LOGGED,
  guard='the fragment is registered (lines 131 and 138), and ScreenTree posts only when a subscriber exists (ScreenTree.java:26)',
  cls='non_standard', via='EventBus post at ScreenTree.java:27 to the @Subscribe method onEvent(ErrorRaisedEvent) (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:15-28 (minLevel INFO, post at 27); SRC MmexApplication.java:136-139 (ScreenTree planted in the release branch); SRC WatchlistFragment.java:300-303')
