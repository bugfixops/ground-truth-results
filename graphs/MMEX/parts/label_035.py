# batch 035 (label_035): com.money.manager.ex.core DateRange, DateRange$$Parcelable (and $1), DefinedDateRange (and $1), DefinedDateRangeName, DefinedDateRanges: 35 methods, 22 REACHABLE, 13 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_035.md; grep output: graphs/MMEX/parts/label_035.grep.txt.
# No e() edges: REACHABLE rows rest on auto_calls.json CALL records and on the batch 010, 011 and 013 edges (label_013.py:30, 35). The sup cut below drops the auto records that start in the UNREACHABLE methods.

sup(('DateRange$$Parcelable.writeToParcel', 'DateRange$$Parcelable.write'))
sup(('DateRange$$Parcelable$1.createFromParcel', 'DateRange$$Parcelable.<clinit>'), ('DateRange$$Parcelable$1.createFromParcel', 'DateRange$$Parcelable.<init>'), ('DateRange$$Parcelable$1.createFromParcel', 'DateRange$$Parcelable.read'))
sup(('DefinedDateRange$1.createFromParcel', 'DefinedDateRange.<clinit>'), ('DefinedDateRange$1.createFromParcel', 'DefinedDateRange.<init>(Parcel)'))
sup(('DefinedDateRange.<init>(Parcel)', 'DefinedDateRangeName.<clinit>'))

# ================================================================== UNREACHABLE (batch 035)

UNREACHABLE['DateRange$$Parcelable.<init>'] = ('no_trigger_in_app',
  'Constructor of the DateRange wrapper. Its only CALL record is from DateRange$$Parcelable$1.createFromParcel (auto_calls.json:16078-16079), which is itself UNREACHABLE. No other method creates a wrapper.',
  'auto_calls.json:16078-16079; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable.describeContents'] = ('framework_never_calls',
  'Bundle.hasFileDescriptors calls describeContents on the Parcelable values it checks, and Bundle.describeContents calls it at Bundle.java:1217. The dialog bundle holds the TransactionFilter wrapper (FilterDialogFragment.java:73), never a DateRange wrapper, so nothing calls this method. No auto record names it.',
  'FW-SRC core/java/android/os/Bundle.java:316-371, 1215-1221; SRC account/FilterDialogFragment.java:73; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable.getParcel'] = ('framework_never_calls',
  'ParcelWrapper accessor. Parcels.unwrap calls it on a DateRange wrapper, and no DateRange wrapper is ever created or unwrapped: the only DateRange$$Parcelable entry points reached are the static write and read (auto_calls.json:46224-46225, 46256-46257). FilterDialogFragment.java:86-87 unwraps the TransactionFilter wrapper (line 86) and an Account wrapper (line 87), never a DateRange wrapper. No auto record names it.',
  'SRC account/FilterDialogFragment.java:86-87; auto_calls.json:46224-46225, 46256-46257; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable.writeToParcel'] = ('framework_never_calls',
  'Parcel.writeParcelable calls writeToParcel only for a DateRange wrapper it is given. No DateRange wrapper is ever parcelled (no Parcels.wrap of a DateRange in label_035.grep.txt), and TransactionFilter$$Parcelable.write calls the static DateRange$$Parcelable.write instead (auto_calls.json:46224-46225). Its only auto edge, to write (auto_calls.json:16208-16209), is dropped by the sup line above.',
  'FW-SRC core/java/android/os/Parcel.java:1785-1791; auto_calls.json:16208-16209, 46224-46225; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable$1.createFromParcel'] = ('framework_never_calls',
  'Parcel.readParcelable calls createFromParcel only for a DateRange wrapper that was written with writeParcelable. None is (see DateRange$$Parcelable.writeToParcel), so the creator never runs. Its outgoing auto records (auto_calls.json:16070-16088) are dropped by the sup line above.',
  'FW-SRC core/java/android/os/Parcel.java:2841-2851; auto_calls.json:16070-16088; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable$1.newArray'] = ('framework_never_calls',
  'Creator method for typed arrays of DateRange wrappers. The framework calls it only when it reads a typed array of this class, and no such array is built or parcelled (label_035.grep.txt). No auto record names it.',
  'SRC core/DateRange.java:26-37 (no parcel code in the source class); label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DefinedDateRange.<init>(Parcel)'] = ('framework_never_calls',
  'Constructor used only by the CREATOR (DefinedDateRange$1.createFromParcel, auto_calls.json:17274-17275), which is UNREACHABLE: no DefinedDateRange is ever parcelled (label_035.grep.txt parcel-related block). The edge to DefinedDateRangeName.<clinit> (auto_calls.json:17442-17443) is dropped by the sup line above.',
  'SRC core/DefinedDateRange.java:49-54; auto_calls.json:17274-17275, 17442-17443; FW-SRC core/java/android/os/Parcel.java:2841-2851; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange.describeContents'] = ('framework_never_calls',
  'Parcelable describeContents for DefinedDateRange. Only the framework calls it, and no app code puts a DefinedDateRange into a Parcel or Bundle (label_035.grep.txt parcel-related block). The only creation site is DefinedDateRanges.java:163. No auto record names it.',
  'SRC core/DefinedDateRange.java:77-78; SRC core/DefinedDateRanges.java:162-170; FW-SRC core/java/android/os/Bundle.java:316-371; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange.writeToParcel'] = ('framework_never_calls',
  'Parcelable writeToParcel for DefinedDateRange. Only Parcel.writeParcelable calls it, and no DefinedDateRange is parcelled (see DefinedDateRange.describeContents). No auto record names it as a caller.',
  'SRC core/DefinedDateRange.java:82-87; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange$1.createFromParcel'] = ('framework_never_calls',
  'CREATOR method for DefinedDateRange. Parcel.readParcelable calls it only for a DefinedDateRange that was written with writeParcelable, and none is. Its outgoing auto records (auto_calls.json:17266-17267, 17274-17275) are dropped by the sup line above.',
  'SRC core/DefinedDateRange.java:58-60; FW-SRC core/java/android/os/Parcel.java:2841-2851; auto_calls.json:17266-17275; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method for DefinedDateRange. Called only when a typed array of DefinedDateRange is read, and none is built or parcelled (label_035.grep.txt).',
  'SRC core/DefinedDateRange.java:62-65; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRanges.contains'] = ('no_trigger_in_app',
  'Public method with no caller. The only app-side match for contains( in files that reference DefinedDateRanges is AccountTransactionListFragment.java:799, which is StatusFilter.contains on transactionStatus, not this method. No auto_calls.json CALL record names it.',
  'SRC core/DefinedDateRanges.java:79-81; SRC account/AccountTransactionListFragment.java:799; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRanges.getByNameId'] = ('no_trigger_in_app',
  'Public method with no caller: its only occurrence in the app source is the definition at DefinedDateRanges.java:50. No auto_calls.json CALL record names it.',
  'SRC core/DefinedDateRanges.java:50-55; label_035.grep.txt',
  'SOURCE')
