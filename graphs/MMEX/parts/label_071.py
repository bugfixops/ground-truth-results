# ================================================================== batch 071 (label_071): SplitRecurringCategory (19 methods),
# SplitRecurringCategory$$Parcelable (7) and SplitRecurringCategory$$Parcelable$1 (3).
# Result: 24 REACHABLE, 5 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_071.md). Grep evidence: graphs/MMEX/parts/label_071.grep.txt.
# Accessors, create, setters, loadFromCursor and <clinit> need no edge here: their routes are auto CALL records (auto_calls.json).
# The generated Parceler classes are not in the source root; their methods were read from the build class files (INFERRED).
# Edges written here (every destination is in this batch, D1):
#   - FRAMEWORK edges for the split-list parcel round trips: the split form Intent, the activity result, the checking editor's
#     saved state, and the split screen's own Intent, saved state and result;
#   - non_standard CALL edges to getParcel from the Parcels.unwrap sites (the parceler library calls it; INFERRED);
#   - UNREACHABLE entries for the three accessors with no caller and for the two generated framework callbacks;
#   - sup pairs (D14a): the auto CALL records of the UNREACHABLE accessors into EntityBase.

# ---- split form: showSplitCategoriesForm puts the split list in the Intent that starts SplitCategoriesActivity

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the split form Intent carries Parcels.wrap(splitsToShow); startActivityForResult marshals the Intent, the wrapper parcels the list, and each SplitRecurringCategory element is written through its generated writeToParcel',
  cls='non_standard',
  via='intent.putExtra(KEY_SPLIT_TRANSACTION, Parcels.wrap(splitsToShow)) at transactions/EditTransactionCommonFunctions.java:1522; getActivity().startActivityForResult at 1528; Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791); the list wrapper element writes are parceler library code (INFERRED)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1511-1529; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- checking editor saved state: onSaveInstanceState wraps the split list; restoreInstanceState unwraps it

e('CheckingTransactionEditActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the saved-state bundle holds Parcels.wrap(mCommon.mSplitTransactions); when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard',
  via='outState.putParcelable(KEY_SPLIT_TRANSACTION, Parcels.wrap(mCommon.mSplitTransactions)) at transactions/CheckingTransactionEditActivity.java:175 (method starts at 162); framework parcelling as in batch 062 (FW-SRC core/java/android/os/Parcel.java:1785-1791; Bundle.java:1229)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:162-178; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

e('CheckingTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the split list wrapper; the first getParcelable unparcels it and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the restore runs only when onCreate gets a saved bundle: onCreate calls restoreInstanceState (line 107) only when savedInstanceState is not null (line 106)',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at transactions/CheckingTransactionEditActivity.java:655 (the deleted list at 657); Bundle.getParcelable unparcels (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readParcelable calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-660; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('CheckingTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on each split list wrapper read from the saved bundle and returns the list of SplitRecurringCategory',
  guard='the same guard as the createFromParcel edge: restoreInstanceState runs only when onCreate gets a saved bundle (lines 106-107)',
  cls='non_standard',
  via='Parcels.unwrap(...getParcelable(KEY_SPLIT_TRANSACTION)) at transactions/CheckingTransactionEditActivity.java:655 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-660; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- activity result: EditTransactionCommonFunctions.onActivityResult unwraps the split lists returned by SplitCategoriesActivity

e('EditTransactionCommonFunctions.onActivityResult', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the result Intent carries the split list wrapper; getParcelableExtra unparcels it and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the SPLIT_TX request branch: case RequestCodes.SPLIT_TX (line 889)',
  cls='non_standard',
  via='data.getParcelableExtra(SplitCategoriesActivity.INTENT_RESULT_SPLIT_TRANSACTION) at transactions/EditTransactionCommonFunctions.java:890 (the deleted list at 893); Bundle unparcel and Parcel.readParcelable as in the restore edge (FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:848, 889-896; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('EditTransactionCommonFunctions.onActivityResult', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper returned by SplitCategoriesActivity and returns the list',
  guard='the SPLIT_TX request branch (line 889)',
  cls='non_standard',
  via='mSplitTransactions = Parcels.unwrap(data.getParcelableExtra(...)) at transactions/EditTransactionCommonFunctions.java:890 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:889-896; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- split screen: SplitCategoriesActivity receives the Intent, restores its saved state, returns the result and saves its state

e('SplitCategoriesActivity.handleIntent', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the split form Intent carries the split list wrapper; getParcelableExtra unparcels it and the framework reads the wrapper with its CREATOR',
  cls='non_standard',
  via='intent.getParcelableExtra(KEY_SPLIT_TRANSACTION) at transactions/SplitCategoriesActivity.java:247 (the deleted list at 251); FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC transactions/SplitCategoriesActivity.java:236-252; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.handleIntent', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the form Intent',
  cls='non_standard',
  via='Parcels.unwrap(intent.getParcelableExtra(KEY_SPLIT_TRANSACTION)) at transactions/SplitCategoriesActivity.java:247 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/SplitCategoriesActivity.java:236-252; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onCreate', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle of the split screen holds the split list wrapper; the first getParcelable unparcels it and the framework reads it with the CREATOR',
  guard='the restore runs only when onCreate gets a saved bundle (line 90)',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at transactions/SplitCategoriesActivity.java:91 (the deleted list at 92); FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onCreate', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the split screen saved state',
  guard='the same guard as the createFromParcel edge (line 90)',
  cls='non_standard',
  via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION)) at transactions/SplitCategoriesActivity.java:91 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onActionDoneClick', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the edited split list goes back to the caller in the result Intent built with Parcels.wrap; setResult hands it to the caller, which marshals the Intent and calls writeToParcel on each wrapper',
  cls='non_standard',
  via='result.putExtra(INTENT_RESULT_SPLIT_TRANSACTION, Parcels.wrap(allSplitTransactions)) at transactions/SplitCategoriesActivity.java:172; setResult(RESULT_OK, result) at 174; FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC transactions/SplitCategoriesActivity.java:149-175; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the split screen saved state holds Parcels.wrap of the split list; when the framework saves the state, the bundle is parcelled and writeToParcel runs',
  cls='non_standard',
  via='outState.putParcelable(KEY_SPLIT_TRANSACTION, Parcels.wrap(mAdapter.splitTransactions)) at transactions/SplitCategoriesActivity.java:184 (the deleted list at 187); FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC transactions/SplitCategoriesActivity.java:181-189; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- recurring editor saved state: RecurringTransactionEditActivity.onSaveInstanceState wraps the split lists (lines 191-192);
#      restoreInstanceState (line 547, called under the guard at line 108) unwraps them (lines 555-556)

e('RecurringTransactionEditActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the recurring editor saved state holds Parcels.wrap of the split list and of the deleted list; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard',
  via='outState.putParcelable(KEY_SPLIT_TRANSACTION, Parcels.wrap(mCommon.mSplitTransactions)) at recurring/transactions/RecurringTransactionEditActivity.java:191 (the deleted list at 192; the method starts at 178); FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:178, 191-192; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block A and block F; INFERRED parceler library not read')

e('RecurringTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the recurring editor saved state holds the split list wrapper; the first getParcelable unparcels the bundle and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='restoreInstanceState runs only when onCreate gets a saved bundle: the call at line 109 is under the check at line 108',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at recurring/transactions/RecurringTransactionEditActivity.java:555 (the deleted list at 556; the method starts at 547); FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:96-109, 547-556; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block A and block F; INFERRED parceler library not read')

e('RecurringTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the recurring editor saved state and returns the list',
  guard='the same guard as the createFromParcel edge (line 108)',
  cls='non_standard',
  via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION)) at recurring/transactions/RecurringTransactionEditActivity.java:555 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:108-109, 555; label_071.grep.txt block A; INFERRED parceler library not read')

# ---- the wrap site of the split form also starts the generated class: Parcels.wrap creates SplitRecurringCategory$$Parcelable
#      for the elements, so its static initializer and constructor run here (library, INFERRED; same convention as batch 059)

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitRecurringCategory$$Parcelable.<clinit>', 'CALL',
  'the split form is opened with the split list: Parcels.wrap(splitsToShow) makes the library create the generated wrapper, and the first use of the class runs its static initializer, which creates SplitRecurringCategory$$Parcelable$1',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): creates SplitRecurringCategory$$Parcelable, which initialises the class',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522 (Parcels.wrap); generated SplitRecurringCategory$$Parcelable.java is not in the source root: auto_calls.json record <clinit> -> SplitRecurringCategory$$Parcelable$1.<init> at SplitRecurringCategory$$Parcelable.java:23')

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitRecurringCategory$$Parcelable.<init>', 'CALL',
  'the same wrap: Parcels.wrap calls the wrapper constructor with each SplitRecurringCategory element of the list',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): new SplitRecurringCategory$$Parcelable(SplitRecurringCategory)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522; generated class not in the source root: auto_calls.json record SplitRecurringCategory$$Parcelable$1.createFromParcel -> SplitRecurringCategory$$Parcelable.<init> at SplitRecurringCategory$$Parcelable.java:28')

# ================================================================== UNREACHABLE: accessors with no caller

UNREACHABLE['SplitRecurringCategory.getAccountId'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has SplitRecurringCategory.getAccountId as dst (no exact record, and no cha record from the ISplitTransaction interface), and every getAccountId() call in the source root is on a transaction, recurring, account or adapter receiver (label_071.grep.txt block D)',
    'domainmodel/SplitRecurringCategory.java:89-91; database/ISplitTransaction.java:35; domainmodel/SplitCategory.java:87; label_071.grep.txt block D',
    'SOURCE')

UNREACHABLE['SplitRecurringCategory.setAccountId'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has SplitRecurringCategory.setAccountId as dst, and every setAccountId( call in the source root is on a transaction entity, the adapter or the own class of another type (label_071.grep.txt block D)',
    'domainmodel/SplitRecurringCategory.java:94-96; database/ISplitTransaction.java:36; label_071.grep.txt block D',
    'SOURCE')

UNREACHABLE['SplitRecurringCategory.getTransId'] = ('no_trigger_in_app',
    'no caller: getTransId is not declared on ISplitTransaction, its only definitions are SplitRecurringCategory.java:134 and SplitCategory.java:132, and no call site or auto_calls.json record names it; the repository filters on the TRANSID column constant instead (datalayer/SplitRecurringCategoriesRepository.java:58)',
    'domainmodel/SplitRecurringCategory.java:134-136; domainmodel/SplitCategory.java:132; datalayer/SplitRecurringCategoriesRepository.java:58; label_071.grep.txt block D',
    'SOURCE')

# ================================================================== UNREACHABLE: generated Parceler callbacks the framework never calls here

UNREACHABLE['SplitRecurringCategory$$Parcelable.describeContents'] = ('framework_never_calls',
    'generated describeContents returns 0 (INFERRED from the build class file). No app code calls describeContents (label_071.grep.txt block C: every match is a definition). The framework calls it only inside the Bundle.hasFileDescriptors map walk, which runs when the bundle is unparcelled (Bundle.java:316-336; the call is at line 329). The Intent check that runs on startActivityForResult is in system_server (ActivityStarter.startActivityMayWait, ActivityStarter.java:681-682) and there the extras are still parcelled (mParcelledData is set, Bundle.java:320-321), so no wrapper is asked for its contents; the saved-state check (ActivityManagerService.java:7453) runs after binder parcelling, the same case as batch 062. No auto record names it',
    'FW-SRC services/core/java/com/android/server/am/ActivityStarter.java:672-682; FW-SRC core/java/android/content/Intent.java:6958-6959; FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1220; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:7453; label_071.grep.txt blocks C and G',
    'INFERRED')

UNREACHABLE['SplitRecurringCategory$$Parcelable$1.newArray'] = ('framework_never_calls',
    'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC core/java/android/os/Parcel.java:2640-2645, c.newArray(N) at 2645), that is, when app code reads a typed array of SplitRecurringCategory wrappers. No app code does: the source root has no createTypedArray, writeTypedArray or readTypedArray call (label_071.grep.txt block B), and no auto_calls.json record has newArray as dst. Whether the parceler library calls newArray is INFERRED (library not read)',
    'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_071.grep.txt blocks B and E',
    'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('SplitRecurringCategory.getAccountId', 'EntityBase.getInt'),
    ('SplitRecurringCategory.setAccountId', 'EntityBase.setInt'),
    ('SplitRecurringCategory.getTransId', 'EntityBase.getInt'))
