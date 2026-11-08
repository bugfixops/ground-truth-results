# ================================================================== batch 069 (label_069): RecurringTransaction setters and the Parceler classes
# RecurringTransaction$$Parcelable (<clinit>, <init>, describeContents, getParcel, read, write, writeToParcel) and
# RecurringTransaction$$Parcelable$1 (<init>, createFromParcel, newArray). RecurringTransaction methods 41-57 of 57 (17 methods).
# Result: 15 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_069.md). The generated classes are not in the source root;
# their methods were read from the build class files (constant pool and bytecode, INFERRED). Grep evidence: graphs/MMEX/parts/label_069.grep.txt.
# Edges written here: the saved-state round trip of RecurringTransactionEditActivity (save in onSaveInstanceState, restore in restoreInstanceState).
# The Parceler library is not read, so the wrap and unwrap hops are INFERRED.
# The setters and the bytecode-reached Parceler methods are REACHABLE through auto_calls.json records; no CALL edge is written for them (D7).
# No sup pairs (D14a): no auto CALL record starts in describeContents or newArray (grep block E). No gui() calls: the setter routes are auto records.

# ---- saved state: RecurringTransactionEditActivity.onSaveInstanceState wraps the transaction and the framework parcels the bundle (line 181)

e('RecurringTransactionEditActivity.onSaveInstanceState', 'RecurringTransaction$$Parcelable.writeToParcel', 'FRAMEWORK',
  'Parcels.wrap(mCommon.transactionEntity) puts a RecurringTransaction wrapper in the saved-state bundle; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='outState.putParcelable(KEY_MODEL, Parcels.wrap(mCommon.transactionEntity)) at recurring/transactions/RecurringTransactionEditActivity.java:181; the framework parcels the saved-state bundle (Bundle.writeToParcel, FW-SRC core/java/android/os/Bundle.java:1229, sent by ActivityThread activityStopped, FW-SRC core/java/android/app/ActivityThread.java:3930-3935); Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791). Parcels.wrap returns the generated wrapper (parceler library not read, INFERRED)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:178-181, 399-404, 442 (runtime type RecurringTransaction); FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; FW-SRC core/java/android/app/ActivityThread.java:3930-3935; label_069.grep.txt blocks A, F, H; INFERRED parceler library not read')

# ---- saved state: RecurringTransactionEditActivity.restoreInstanceState unparcels the saved transaction (line 549) and unwraps it (line 549)

e('RecurringTransactionEditActivity.restoreInstanceState', 'RecurringTransaction$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the RecurringTransaction wrapper; the first getParcelable unparcels the bundle, and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the restore runs only when onCreate gets a saved bundle: onCreate calls restoreInstanceState at line 109 only when savedInstanceState is not null (line 108)',
  cls='non_standard', via='savedInstanceState.getParcelable(KEY_MODEL) at recurring/transactions/RecurringTransactionEditActivity.java:549 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readParcelable reads the CREATOR field (FW-SRC core/java/android/os/Parcel.java:2894) and calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:102, 107-110, 547-549; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_069.grep.txt blocks A, F, H; INFERRED parceler library not read')

e('RecurringTransactionEditActivity.restoreInstanceState', 'RecurringTransaction$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper read from the saved bundle and returns the RecurringTransaction',
  guard='the same guard as the createFromParcel edge: restoreInstanceState runs only when onCreate gets a saved bundle (lines 108-109)',
  cls='non_standard', via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_MODEL)) at recurring/transactions/RecurringTransactionEditActivity.java:549 (parceler library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:108-109, 547-549; label_069.grep.txt blocks A, E, F; INFERRED parceler library not read')

# ================================================================== UNREACHABLE: describeContents and the typed-array creator

UNREACHABLE['RecurringTransaction$$Parcelable.describeContents'] = ('framework_never_calls',
  'generated describeContents returns 0 (class file bytes 03 ac: iconst_0, ireturn). No app code calls it: the SRC scan finds only definitions (DefinedDateRange, CategorySub, ValuePieEntry; StatusFilter is commented out) and no call site (label_069.grep.txt block C). The framework calls describeContents on Parcelable values only in Bundle.java (lines 329, 338, 349, 362) and Intent.java:9553 (block D). The walk at Bundle.java:324-340 runs only when mParcelledData is null; the icicle that ActivityManagerService.activityStopped checks (line 7453) is parcelled, so that walk does not reach this wrapper (INFERRED: the binder path is not read). No auto record names it',
  'FW-SRC core/java/android/os/Bundle.java:316-340; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:7448-7455; label_069.grep.txt blocks C, D, E, F, H',
  'INFERRED')

UNREACHABLE['RecurringTransaction$$Parcelable$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method (bytecode 1b bd 00 07 b0: iload_1, anewarray, areturn). The framework calls Creator.newArray only from Parcel.createTypedArray (FW-SRC core/java/android/os/Parcel.java:2645, c.newArray(N)); the other 33 newArray hits in core/java and services/core/java are definitions (label_069.grep.txt block D). createTypedArray is not called from app source (block C has no createTypedArray or readTypedArray hit), so no typed array of RecurringTransaction wrappers is read. No auto_calls.json record has newArray as dst or $1.newArray as src (block E). Whether the Parceler library calls newArray is INFERRED (library not read)',
  'FW-SRC core/java/android/os/Parcel.java:2640-2646; label_069.grep.txt blocks C, D, E, F, H',
  'INFERRED')
