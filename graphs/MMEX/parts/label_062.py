# ================================================================== batch 062 (label_062): AccountTransaction$$Parcelable.describeContents,
# getParcel, read, write, writeToParcel, AccountTransaction$$Parcelable$1.<init>, createFromParcel, newArray (AccountTransaction methods 41-48 of 48).
# Result: 6 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_062.md). The generated classes are not in the source root;
# their methods were read from the build class files (constant-pool strings, INFERRED). Grep evidence: graphs/MMEX/parts/label_062.grep.txt.
# Edges written here: the two parcel round trips of the CheckingTransactionEditActivity saved state (save in onSaveInstanceState,
# restore in restoreInstanceState). The Parceler library is not read, so the wrap and unwrap hops are INFERRED.
# read, write and $1.<init> are REACHABLE through auto CALL records (auto_calls.json); $1.<init> is called by <clinit>, which belongs to batch 061.
# No CALL edge is written (D7): every bytecode CALL into an owned method here is an auto record.
# No sup pairs (D14a): no auto CALL record starts in describeContents or newArray.

# ---- saved state: CheckingTransactionEditActivity.onSaveInstanceState wraps the transaction and the framework parcels the bundle (line 167)

e('CheckingTransactionEditActivity.onSaveInstanceState', 'AccountTransaction$$Parcelable.writeToParcel', 'FRAMEWORK',
  'Parcels.wrap(mCommon.transactionEntity) puts an AccountTransaction wrapper in the saved-state bundle; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='outState.putParcelable(KEY_TRANSACTION_ENTITY, Parcels.wrap(mCommon.transactionEntity)) at transactions/CheckingTransactionEditActivity.java:166-167; the framework parcels the saved-state bundle (Bundle.writeToParcel, FW-SRC core/java/android/os/Bundle.java:1229, sent by ActivityThread activityStopped, FW-SRC core/java/android/app/ActivityThread.java:3930-3935); Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791). Parcels.wrap returns the generated wrapper (parceler library not read, INFERRED)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:162-167, 390-395, 776 (runtime type AccountTransaction); FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; FW-SRC core/java/android/app/ActivityThread.java:3930-3935; label_062.grep.txt blocks A and F; INFERRED parceler library not read')

# ---- saved state: CheckingTransactionEditActivity.restoreInstanceState unparcels the saved transaction (line 648) and unwraps it (line 649)

e('CheckingTransactionEditActivity.restoreInstanceState', 'AccountTransaction$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the AccountTransaction wrapper; the first getParcelable unparcels the bundle, and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the restore runs only when onCreate gets a saved bundle: onCreate calls restoreInstanceState (line 107) only when savedInstanceState is not null (line 106)',
  cls='non_standard', via='savedInstanceState.getParcelable(KEY_TRANSACTION_ENTITY) at transactions/CheckingTransactionEditActivity.java:648 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readParcelable reads the CREATOR field (FW-SRC core/java/android/os/Parcel.java:2894) and calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-649; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_062.grep.txt blocks A and F; INFERRED parceler library not read')

e('CheckingTransactionEditActivity.restoreInstanceState', 'AccountTransaction$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper read from the saved bundle and returns the AccountTransaction',
  guard='the same guard as the createFromParcel edge: restoreInstanceState runs only when onCreate gets a saved bundle (lines 106-107)',
  cls='non_standard', via='Parcels.unwrap(parcelTx) at transactions/CheckingTransactionEditActivity.java:649 (parceler library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-649; label_062.grep.txt blocks A and F; INFERRED parceler library not read')

# ================================================================== UNREACHABLE: describeContents and the typed-array creator

UNREACHABLE['AccountTransaction$$Parcelable.describeContents'] = ('framework_never_calls',
  'generated describeContents returns 0. No app code calls describeContents (label_062.grep.txt block C, empty). The framework reaches it only through Bundle.hasFileDescriptors walking an unparcelled map (Bundle.java:324-336) and Bundle.describeContents (Bundle.java:1215-1218). The saved-state bundle is checked in ActivityManagerService.activityStopped (line 7453) after binder parcelling, when mParcelledData is set, so that check does not call describeContents on the wrapper (INFERRED: the binder and ActivityThread marshalling path is not read). No auto record names it',
  'FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:7447-7453; label_062.grep.txt blocks C and G',
  'INFERRED')

UNREACHABLE['AccountTransaction$$Parcelable$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC core/java/android/os/Parcel.java:2640-2645, c.newArray(N) at 2645), that is, when app code reads a typed array of AccountTransaction wrappers. No app code does: the source root has no createTypedArray, writeTypedArray or CREATOR reference, and its newArray implementations are DefinedDateRange, CategorySub and ValuePieEntry only (label_062.grep.txt block B). No auto_calls.json record has newArray as dst or $1.newArray as src. Whether the Parceler library calls newArray is INFERRED (library not read)',
  'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_062.grep.txt blocks B and E; generated class not in the source root (build class file descriptor (I)[Lcom/money/manager/ex/domainmodel/AccountTransaction$$Parcelable;, block E)',
  'INFERRED')
