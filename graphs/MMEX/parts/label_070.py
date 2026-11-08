# ================================================================== batch 070 (label_070): SplitCategory (19 methods),
# SplitCategory$$Parcelable (7 methods), SplitCategory$$Parcelable$1 (3 methods). 29 methods in total.
# Result: 24 REACHABLE, 5 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_070.md).
# SplitCategory is a @Parcel class. Its Parceler class SplitCategory$$Parcelable and the CREATOR $1 are generated at build time,
# so they are not in the source root; their methods were read from the build class files (constant-pool strings, INFERRED).
# Grep and class-file evidence: graphs/MMEX/parts/label_070.grep.txt.
# Edges written here (D1, destinations owned by this batch):
#   - FRAMEWORK writeToParcel from the five Parcels.wrap sites of the split lists,
#   - FRAMEWORK createFromParcel from the five Parcels.unwrap sites (restore paths and intent extras),
#   - CALL non_standard getParcel from the same five unwrap sites (Parcels.unwrap calls the generated getParcel; library not read, INFERRED).
# The Parceler library is not read, so the wrap, unwrap and element hops are INFERRED.
# write, read, $$Parcelable.<init>, $$Parcelable.<clinit> and $1.<init> are REACHABLE through auto CALL records (auto_calls.json).
# No CALL edge duplicates an auto record (D7): no auto record names getParcel.
# sup pairs (D14a): the three auto CALL records whose caller is UNREACHABLE here (getAccountId, setAccountId, getTransId).

# ================================================================== the wrap sites (FRAMEWORK writeToParcel)

_WRITE_SITES = (
    ('CheckingTransactionEditActivity.onSaveInstanceState',
     'transactions/CheckingTransactionEditActivity.java:175-177',
     'saved state: the split lists are wrapped into the saved-state bundle; when the framework saves the state it parcels the bundle and writes the element wrappers',
     'SRC transactions/CheckingTransactionEditActivity.java:162-177'),
    ('RecurringTransactionEditActivity.onSaveInstanceState',
     'recurring/transactions/RecurringTransactionEditActivity.java:191-192',
     'saved state of the recurring editor: the same wrap of the split lists into the saved-state bundle',
     'SRC recurring/transactions/RecurringTransactionEditActivity.java:178-192'),
    ('SplitCategoriesActivity.onSaveInstanceState',
     'transactions/SplitCategoriesActivity.java:184-187',
     'saved state of the split screen: the adapter list and the deleted list are wrapped into the saved-state bundle',
     'SRC transactions/SplitCategoriesActivity.java:181-187'),
    ('SplitCategoriesActivity.onActionDoneClick',
     'transactions/SplitCategoriesActivity.java:172-173',
     'the split screen returns the list to its caller in a result intent; the result extras are parcelled when the result is delivered',
     'SRC transactions/SplitCategoriesActivity.java:149-173; INFERRED intent extras are parcelled when the result crosses the binder (Intent.writeToParcel not read)'),
    ('EditTransactionCommonFunctions.showSplitCategoriesForm',
     'transactions/EditTransactionCommonFunctions.java:1522-1523',
     'the split screen is started with the list in its intent extras; the extras are parcelled when the activity starts',
     'SRC transactions/EditTransactionCommonFunctions.java:1511-1523; INFERRED intent extras are parcelled on startActivity (Intent.writeToParcel not read)'),
)
for _src, _where, _why, _ev in _WRITE_SITES:
    e(_src, 'SplitCategory$$Parcelable.writeToParcel', 'FRAMEWORK', _why,
      cls='non_standard',
      via='Parcels.wrap at ' + _where + '; Parcel.writeParcelable calls writeToParcel on the element wrapper (FW-SRC core/java/android/os/Parcel.java:1785-1791)',
      evidence=_ev + '; FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; INFERRED the parceler library writes each element wrapper with writeParcelable (library not read)')

# ================================================================== the unwrap sites (FRAMEWORK createFromParcel, CALL getParcel)

_READ_SITES = (
    ('CheckingTransactionEditActivity.restoreInstanceState',
     'transactions/CheckingTransactionEditActivity.java:655-657',
     'saved state: restoreInstanceState reads the split lists from the saved-state bundle; the framework reads the element wrapper with its CREATOR, which calls createFromParcel',
     'SRC transactions/CheckingTransactionEditActivity.java:647-657'),
    ('RecurringTransactionEditActivity.restoreInstanceState',
     'recurring/transactions/RecurringTransactionEditActivity.java:555-556',
     'saved state of the recurring editor: the same read of the split lists from the saved-state bundle',
     'SRC recurring/transactions/RecurringTransactionEditActivity.java:547-556'),
    ('SplitCategoriesActivity.onCreate',
     'transactions/SplitCategoriesActivity.java:91-92',
     'the split screen restores its saved lists in onCreate when the saved bundle is not null',
     'SRC transactions/SplitCategoriesActivity.java:82-97'),
    ('SplitCategoriesActivity.handleIntent',
     'transactions/SplitCategoriesActivity.java:247-251',
     'the split screen reads the lists from its start intent extras',
     'SRC transactions/SplitCategoriesActivity.java:236-251; INFERRED intent getParcelableExtra unparcels as Bundle.getParcelable (Intent not read)'),
    ('EditTransactionCommonFunctions.onActivityResult',
     'transactions/EditTransactionCommonFunctions.java:890-895',
     'the result of the split screen is read back from its result intent extras',
     'SRC transactions/EditTransactionCommonFunctions.java:848-895; INFERRED intent getParcelableExtra unparcels as Bundle.getParcelable (Intent not read)'),
)
for _src, _where, _why, _ev in _READ_SITES:
    e(_src, 'SplitCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK', _why,
      cls='non_standard',
      via='Parcels.unwrap at ' + _where + '; the framework unparcels the Parcelable (Bundle.getParcelable, FW-SRC core/java/android/os/Bundle.java:938-939) and Parcel.readParcelable calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894)',
      evidence=_ev + '; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; INFERRED the parceler library reads the lists from the wrapper (library not read)')
    e(_src, 'SplitCategory$$Parcelable.getParcel', 'CALL',
      'Parcels.unwrap calls getParcel on each element wrapper and returns the SplitCategory list',
      cls='non_standard',
      via='Parcels.unwrap at ' + _where + ' (the parceler library calls the generated getParcel; library source not read, INFERRED)',
      evidence=_ev + '; INFERRED parceler library not read')

# ================================================================== UNREACHABLE: the accessors with no caller

UNREACHABLE['SplitCategory.getAccountId'] = ('no_trigger_in_app',
    'no caller: ISplitTransaction declares getAccountId (line 35), but no call site in the source root has a split-typed receiver; the getAccountId() call sites are on Account, AccountTransaction, RecurringTransaction and AccountTransactionDisplay receivers; no auto_calls.json record has dst SplitCategory.getAccountId or ISplitTransaction.getAccountId; its one auto record (src SplitCategory.getAccountId) is cut by sup below',
    'domainmodel/SplitCategory.java:87-90; database/ISplitTransaction.java:35; label_070.grep.txt sections 3, 4', 'SOURCE')

UNREACHABLE['SplitCategory.setAccountId'] = ('no_trigger_in_app',
    'no caller: the only declarations are ISplitTransaction.java:36 and SplitCategory.java:92; the setAccountId call sites are on transactionEntity (ITransactionEntity, implemented by AccountTransaction and RecurringTransaction, auto cha records), and SplitCategory does not implement ITransactionEntity; its one auto record (src SplitCategory.setAccountId) is cut by sup below',
    'domainmodel/SplitCategory.java:92-95; database/ISplitTransaction.java:36; database/ITransactionEntity.java:50; label_070.grep.txt sections 3, 4', 'SOURCE')

UNREACHABLE['SplitCategory.getTransId'] = ('no_trigger_in_app',
    'no caller: getTransId is not declared on ISplitTransaction, its only definitions in the source root are SplitCategory.java:132 and SplitRecurringCategory.java:134, and no call site or auto_calls.json record names it; its one auto record (src SplitCategory.getTransId) is cut by sup below',
    'domainmodel/SplitCategory.java:132-134; domainmodel/SplitRecurringCategory.java:134; label_070.grep.txt section 3', 'SOURCE')

# ================================================================== UNREACHABLE: generated describeContents and the typed-array creator

UNREACHABLE['SplitCategory$$Parcelable.describeContents'] = ('framework_never_calls',
    'generated describeContents returns 0 (INFERRED from the class file). No app code calls describeContents (label_070.grep.txt section 2, no call site). The framework calls it on Parcelable values it receives directly (Bundle values and Intent extras through hasFileDescriptors, FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218). The element wrappers of the split lists sit inside the list wrapper, not as direct bundle or intent values, so the framework does not call describeContents on them (INFERRED: the list wrapper is not read). No auto record names it',
    'FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218; label_070.grep.txt sections 2, 5', 'INFERRED')

UNREACHABLE['SplitCategory$$Parcelable$1.newArray'] = ('framework_never_calls',
    'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC core/java/android/os/Parcel.java:2640-2645), that is, when app code reads a typed array of SplitCategory wrappers. No app code does: the source root has no createTypedArray or writeTypedArray call, and its newArray implementations are DefinedDateRange, CategorySub and ValuePieEntry only (label_070.grep.txt section 2). No auto_calls.json record has newArray as dst or $1.newArray as src. Whether the Parceler library calls newArray is INFERRED (library not read)',
    'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_070.grep.txt sections 2, 5', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('SplitCategory.getAccountId', 'EntityBase.getInt'),
    ('SplitCategory.setAccountId', 'EntityBase.setInt'),
    ('SplitCategory.getTransId', 'EntityBase.getInt'))
