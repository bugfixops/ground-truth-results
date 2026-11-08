# batch 091: PriceUpdaterBase (5 methods), SecurityPriceUpdaterBase (2) and WatchlistDataset (3).
# No e() edges: each REACHABLE method here already has its incoming CALL record in auto_calls.json, so the edge is kept from the auto set (D7).
# UNREACHABLE entries and sup pairs only. Rows and printed lines: graphs/MMEX/parts/label_091.md. Grep evidence: graphs/MMEX/parts/label_091.grep.txt.
# Each sup pair here has its destination in this batch, so this batch's owner writes it (D17(b)). The two WatchlistFragment sups cut a CHA record from a REACHABLE caller, the same pattern as batch 006 (D14).

UNREACHABLE['SecurityPriceUpdaterBase.<init>'] = (
  'no_trigger_in_app',
  'Constructor of SecurityPriceUpdaterBase, a concrete class (SecurityPriceUpdaterBase.java:28-33). No source line creates it, and no class extends it: YahooCsv, Morningstar, Yql, FixerService and ExchangeRateUpdaterBase extend PriceUpdaterBase directly. No class file other than its own references it, and no auto_calls.json record targets it.',
  'label_091.grep.txt:6-8, 10-34, 36-46; auto_calls.json:13114',
  'SOURCE')

UNREACHABLE['SecurityPriceUpdaterBase.downloadPrices'] = (
  'no_trigger_in_app',
  'Empty override of ISecurityPriceUpdater.downloadPrices (SecurityPriceUpdaterBase.java:35-38). The interface calls in WatchlistFragment (lines 363 and 474) list it as a CHA target, but the receiver is always a YahooCsv, Morningstar or Yql instance (SecurityPriceUpdaterFactory.java:42, 45, 48, 52), and no SecurityPriceUpdaterBase instance can exist. The three real overrides keep their own CHA records from the same callers, so the cut does not orphan them.',
  'SecurityPriceUpdaterFactory.java:40-52; WatchlistFragment.java:362-363, 472-474; auto_calls.json:14230-14231, 15234-15235; label_091.grep.txt:6-8, 36-46',
  'SOURCE')

UNREACHABLE['WatchlistDataset.<init>'] = (
  'no_trigger_in_app',
  'Constructor of WatchlistDataset, which extends Dataset (WatchlistDataset.java:32-40). No source line creates it (its only source lines are the declaration and this constructor), and no class file other than its own references it. No auto_calls.json record targets it. Its outgoing records (auto_calls.json:15292-15316) call methods owned by other batches, which have other callers, so they stay with those owners.',
  'WatchlistDataset.java:32-40; label_091.grep.txt:36-50; auto_calls.json:15292-15316',
  'SOURCE')

UNREACHABLE['WatchlistDataset.getAllColumns'] = (
  'no_trigger_in_app',
  'Override of the abstract Dataset.getAllColumns (Dataset.java:52). It runs only on a WatchlistDataset instance, and none is created (WatchlistDataset.<init>). The receivers of the getAllColumns calls in the source are concrete classes, none typed Dataset or RepositoryBase, so no CHA route reaches it. No incoming auto_calls.json record.',
  'WatchlistDataset.java:44-55; Dataset.java:52; label_091.grep.txt:56-70',
  'SOURCE')

UNREACHABLE['WatchlistDataset.getWatchlistSqlQuery'] = (
  'no_trigger_in_app',
  'Public method (WatchlistDataset.java:57-60). The only source line naming it is its declaration, so no source code calls it, and it runs only on a WatchlistDataset instance, which is never created. No incoming auto_calls.json record. Its outgoing records (auto_calls.json:15324, 15332) stay with the owners of MmxFileUtils.',
  'WatchlistDataset.java:57-60; label_091.grep.txt:53-54; auto_calls.json:15324-15332',
  'SOURCE')

# The dead constructor's bytecode call into PriceUpdaterBase.<init> cannot run; PriceUpdaterBase.<init> stays REACHABLE through the YahooCsv, Morningstar and Yql constructors (auto_calls.json:13342, 13502, 15406).
sup(('SecurityPriceUpdaterBase.<init>', 'PriceUpdaterBase.<init>'))

# The CHA records from the two REACHABLE WatchlistFragment callers to the unreachable base method are cut. The three real overrides keep their own CHA records from the same callers (auto_calls.json:14206-14222, 15210-15226).
sup(('WatchlistFragment.onPriceUpdateRequested', 'SecurityPriceUpdaterBase.downloadPrices'))
sup(('WatchlistFragment$4.onClick', 'SecurityPriceUpdaterBase.downloadPrices'))
