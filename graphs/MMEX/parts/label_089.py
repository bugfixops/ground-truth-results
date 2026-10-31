# ================================================================== batch 089 (label_089): 32 methods (graphs/MMEX/scratch/batches/batch_089.txt): PriceEditModel_MembersInjector (4), QuoteProviders (3), SecurityPriceModel.<init>, SecurityPriceUpdaterFactory (2), StocksCursorAdapter (3), StocksDataViewHolder.<init>, DummyContent (3 and DummyContent$DummyItem 2), AllPricesDownloadedEvent.<init>, PriceDownloadedEvent.<init>, PriceDownloadedEvent$$Parcelable (7 and its $1 with 3), PriceUpdateRequestEvent.<init>.
# Rows, printed lines and counts: graphs/MMEX/parts/label_089.md (13 REACHABLE, 19 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_089.grep.txt (sections A-E).
# This file writes:
#   - 0 SCREENS keys (no new screen: every batch method is a helper, a generated class or a Parcelable hook, D9);
#   - 2 e() edges, both FRAMEWORK (D7: no CALL edge already exists in auto_calls.json, and the two framework routes are not in auto_calls): WatchlistItemsFragment.onLoadFinished -> StocksCursorAdapter.newView and -> StocksCursorAdapter.bindView (both dst are owned by this batch, D1);
#   - 14 sup pairs (D14a): the auto CALL records whose caller is UNREACHABLE in this batch (PriceEditModel_MembersInjector.create and injectMembers, DummyContent.<clinit>, PriceDownloadedEvent$$Parcelable.writeToParcel, write, read, <clinit> and $1.createFromParcel);
#   - 19 UNREACHABLE entries: PriceEditModel_MembersInjector.<init>, create, injectMembers (generated, INFERRED); SecurityPriceUpdaterFactory.<init> (source, SOURCE); DummyContent.<clinit>, <init>, addItem, DummyContent$DummyItem.<init>, toString (source, SOURCE); PriceDownloadedEvent$$Parcelable.<clinit>, <init>, describeContents, getParcel, read, write, writeToParcel and PriceDownloadedEvent$$Parcelable$1.<init>, createFromParcel, newArray (generated, INFERRED).
# No new constants (D2).

# ---- framework edges: WatchlistItemsFragment.onLoadFinished hands the cursor to the adapter (changeCursor) and the framework then calls getView, which calls newView (no scrap view) and bindView (each visible row)

e('WatchlistItemsFragment.onLoadFinished', 'StocksCursorAdapter.newView', 'FRAMEWORK',
  'the loader result is handed to the adapter (adapter.changeCursor(data) swaps in the cursor and notifies the list); on the relayout the framework calls getView, which calls newView for a row that has no scrap view (the first layout of the data)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:324-327 (onLoadFinished, changeCursor at 327); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:348-353 (changeCursor calls swapCursor), 276-289 (getView calls newView at 285 when convertView is null); auto_calls framework_calls WatchlistItemsFragment.onLoadFinished lists StocksCursorAdapter.changeCursor but no newView or bindView record; INFERRED that StocksCursorAdapter uses the framework CursorAdapter behaviour (same pattern as label_087 PortfolioCursorAdapter)')

e('WatchlistItemsFragment.onLoadFinished', 'StocksCursorAdapter.bindView', 'FRAMEWORK',
  'the same relayout: the framework calls getView, which calls bindView for every visible row (the cursor columns are copied into the row views)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:324-327; SRC investment/StocksCursorAdapter.java:71 (bindView); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:289 (getView calls bindView); auto_calls framework_calls WatchlistItemsFragment.onLoadFinished lists no bindView record; INFERRED that StocksCursorAdapter uses the framework CursorAdapter behaviour (library not read)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('PriceEditModel_MembersInjector.create', 'PriceEditModel_MembersInjector.<init>'),
    ('PriceEditModel_MembersInjector.injectMembers', 'PriceEditModel_MembersInjector.injectDateTimeUtilsLazy'),
    ('DummyContent.<clinit>', 'DummyContent.addItem'),
    ('DummyContent.<clinit>', 'DummyContent$DummyItem.<init>'),
    ('PriceDownloadedEvent$$Parcelable.writeToParcel', 'PriceDownloadedEvent$$Parcelable.write'),
    ('PriceDownloadedEvent$$Parcelable.write', 'Money$$Parcelable.<clinit>'),
    ('PriceDownloadedEvent$$Parcelable.write', 'Money$$Parcelable.write'),
    ('PriceDownloadedEvent$$Parcelable.read', 'Money$$Parcelable.<clinit>'),
    ('PriceDownloadedEvent$$Parcelable.read', 'PriceDownloadedEvent.<init>'),
    ('PriceDownloadedEvent$$Parcelable.read', 'Money$$Parcelable.read'),
    ('PriceDownloadedEvent$$Parcelable.<clinit>', 'PriceDownloadedEvent$$Parcelable$1.<init>'),
    ('PriceDownloadedEvent$$Parcelable$1.createFromParcel', 'PriceDownloadedEvent$$Parcelable.<clinit>'),
    ('PriceDownloadedEvent$$Parcelable$1.createFromParcel', 'PriceDownloadedEvent$$Parcelable.<init>'),
    ('PriceDownloadedEvent$$Parcelable$1.createFromParcel', 'PriceDownloadedEvent$$Parcelable.read'))

# ================================================================== UNREACHABLE (batch 089). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['PriceEditModel_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only class-file referrer is create (grep section B1), and create has no referrer. The only auto record into <init> is create -> <init> (generated PriceEditModel_MembersInjector.java:23).',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceEditModel_MembersInjector.java:23 (generated)',
  'INFERRED')

UNREACHABLE['PriceEditModel_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated factory method (takes the Provider and returns a MembersInjector). No class file refers to create. DaggerMmxComponent refers only to the static injectDateTimeUtilsLazy (auto_calls DaggerMmxComponent.java:495).',
  'class-file parse (label_089.grep.txt B1, C); auto_calls DaggerMmxComponent.java:495 (generated)',
  'INFERRED')

UNREACHABLE['PriceEditModel_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (takes the PriceEditModel). Its only class-file referrer is the bridge injectMembers(Object), and that bridge has no referrer. Its outgoing record injectMembers -> injectDateTimeUtilsLazy (generated PriceEditModel_MembersInjector.java:28) is cut by the sup pair above.',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceEditModel_MembersInjector.java:28 (generated)',
  'INFERRED')

UNREACHABLE['SecurityPriceUpdaterFactory.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of a class whose only use is the static getUpdaterInstance. The source has no constructor and no new SecurityPriceUpdaterFactory, and no class file refers to <init>.',
  'SRC investment/SecurityPriceUpdaterFactory.java:32 (no constructor); label_089.grep.txt A5, B1',
  'SOURCE')

UNREACHABLE['DummyContent.<clinit>'] = ('no_trigger_in_app',
  'Static initializer of the Android template class DummyContent. Only DummyContent.java names the class in src, and no class file refers to it. Its static block (addItem at lines 45-47) therefore never runs.',
  'SRC investment/dummy/DummyContent.java:31, 43-47; label_089.grep.txt A4, B1',
  'SOURCE')

UNREACHABLE['DummyContent.<init>'] = ('no_trigger_in_app',
  'Default constructor of the template class DummyContent. No class file refers to it, and src has no new DummyContent.',
  'SRC investment/dummy/DummyContent.java:31; label_089.grep.txt A4, B1',
  'SOURCE')

UNREACHABLE['DummyContent.addItem'] = ('no_trigger_in_app',
  'Private static helper called only from the DummyContent static block (lines 45-47; auto_calls DummyContent.java:47). That block is unreachable (see DummyContent.<clinit>).',
  'SRC investment/dummy/DummyContent.java:43-50; auto_calls DummyContent.java:47',
  'SOURCE')

UNREACHABLE['DummyContent$DummyItem.<init>'] = ('no_trigger_in_app',
  'Constructed only by the DummyContent static block (lines 45-47; auto_calls DummyContent.java:47), which is unreachable.',
  'SRC investment/dummy/DummyContent.java:45-47, 58, 62; auto_calls DummyContent.java:47',
  'SOURCE')

UNREACHABLE['DummyContent$DummyItem.toString'] = ('no_trigger_in_app',
  'No DummyItem instance is ever created, and no class file refers to toString.',
  'SRC investment/dummy/DummyContent.java:58, 68; label_089.grep.txt B1',
  'SOURCE')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.<clinit>'] = ('no_trigger_in_app',
  'Static initializer of the parceler-generated wrapper. Its only class-file referrer is PriceDownloadedEvent$$Parcelable$1.createFromParcel (CREATOR construction). The wrapper exists only through Parcels.wrap in PriceDownloadedEventBundler.put (line 37), which is reached only from EditPriceDialog Icepick state, and EditPriceDialog is never constructed (label_089.grep.txt A1).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:37; SRC investment/EditPriceDialog.java:83, 89-91; class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:22 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.<init>'] = ('framework_never_calls',
  'Constructed only in PriceDownloadedEvent$$Parcelable$1.createFromParcel (auto_calls generated line 27). createFromParcel is the Parcelable.Creator the framework calls when it reads a Parcel that holds this type, and such a Parcel is produced only by the dead Parcels.wrap path.',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:27 (generated); SRC core/bundlers/PriceDownloadedEventBundler.java:37',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.describeContents'] = ('framework_never_calls',
  'Parcelable method. The framework calls it from Bundle.hasFileDescriptors (Bundle.java:329-330) only for a Parcelable value stored in a Bundle. The only putParcelable of this type is PriceDownloadedEventBundler.java:37, which is dead. No class file refers to describeContents.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Bundle.java:316-332 (call at 329-330); SRC core/bundlers/PriceDownloadedEventBundler.java:37; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.getParcel'] = ('no_trigger_in_app',
  'Accessor called by the parceler library through the bridge getParcel()Object. The library calls it only from Parcels.wrap and Parcels.unwrap, whose call sites in src are PriceDownloadedEventBundler.java:37 and 43, both dead. The bridge has no referrer (class-file parse). The library call is INFERRED (library jar not in repo).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:37, 43; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.read'] = ('framework_never_calls',
  'Called only by PriceDownloadedEvent$$Parcelable$1.createFromParcel (auto_calls generated line 27). It is reached only through the framework Creator path.',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:27, 80, 83 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.write'] = ('framework_never_calls',
  'Called only by PriceDownloadedEvent$$Parcelable.writeToParcel (auto_calls generated line 44). writeToParcel is reached only through the framework Parcelable path.',
  'class-file parse (label_089.grep.txt C); auto_calls PriceDownloadedEvent$$Parcelable.java:44 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.writeToParcel'] = ('framework_never_calls',
  'Parcelable.writeToParcel. Parcel.writeParcelable calls it (Parcel.java:1791) when a Parcel carries this object. The only object is made by the dead Parcels.wrap path. No class file refers to writeToParcel.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java:1785-1791 (call at 1791); SRC core/bundlers/PriceDownloadedEventBundler.java:37; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable$1.<init>'] = ('no_trigger_in_app',
  'Constructed by the CREATOR field initializer in PriceDownloadedEvent$$Parcelable.<clinit> (auto_calls generated line 22). That class initialisation is unreachable (see PriceDownloadedEvent$$Parcelable.<clinit>).',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:22 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable$1.createFromParcel'] = ('framework_never_calls',
  'Parcelable.Creator method. The framework calls it through Parcel.readParcelable (Parcel.java:2842; readParcelableCreator at 2867) only when a Parcel holds this type. The only such Parcel comes from the dead Parcels.wrap path.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java:2841-2842, 2867; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable$1.newArray'] = ('framework_never_calls',
  'Parcelable.Creator.newArray. The framework calls it from Parcel.createTypedArray (Parcel.java:2645) only when a typed array of this type is read. That needs the dead path.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java:2640-2645 (newArray at 2645); class-file parse (label_089.grep.txt C)',
  'INFERRED')
