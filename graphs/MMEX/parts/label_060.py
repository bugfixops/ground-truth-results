# ================================================================== batch 060 (label_060): Account$$Parcelable.writeToParcel,
# Account$$Parcelable$1.<init>, Account$$Parcelable$1.createFromParcel, Account$$Parcelable$1.newArray (Account methods 41-44 of 44).
# Result: 3 REACHABLE, 1 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_060.md). The generated class is not in the source root;
# its methods were read from the build class files (constant-pool strings, INFERRED). Grep evidence: graphs/MMEX/parts/label_060.grep.txt.
# Edges written here: the two parcel round trips of the AccountEditActivity saved state (the save in onSaveInstanceState,
# the restore in restoreInstanceState). The Parceler library is not read, so the wrap and unwrap hops are INFERRED.
# $1.<init> is REACHABLE only through the auto CALL record Account$$Parcelable.<clinit> -> Account$$Parcelable$1.<init>
# (auto_calls.json:24976-24978); <clinit> belongs to batch 059 (open point in label_060.md).
# No CALL edge is written (D7): every CALL into an owned method here is an auto record.
# No sup pairs (D14a): no auto CALL record starts in newArray (none does), and no UNREACHABLE method of this batch has an auto record.

# ---- saved state: AccountEditActivity.onSaveInstanceState wraps mAccount and the framework parcels the bundle (AccountEditActivity.java:204)

e('AccountEditActivity.onSaveInstanceState', 'Account$$Parcelable.writeToParcel', 'FRAMEWORK',
  'Parcels.wrap(mAccount) puts an Account wrapper in the saved-state bundle; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='outState.putParcelable(KEY_ACCOUNT_ENTITY, Parcels.wrap(mAccount)) at AccountEditActivity.java:204; the framework parcels the saved-state bundle (Bundle.writeToParcel, FW-SRC Bundle.java:1229, sent by ActivityThread activityStopped, FW-SRC ActivityThread.java:3930-3935); Parcel.writeValue calls writeParcelable (FW-SRC Parcel.java:1785-1791), which calls p.writeToParcel (FW-SRC Parcel.java:1791). Parcels.wrap returns the generated wrapper (parceler library not read, INFERRED)',
  evidence='SRC account/AccountEditActivity.java:196-209 (line 204); FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; FW-SRC core/java/android/app/ActivityThread.java:3930-3935; label_060.grep.txt block A; INFERRED parceler library not read')

# ---- saved state: AccountEditActivity.restoreInstanceState unwraps the saved Account (AccountEditActivity.java:587)

e('AccountEditActivity.restoreInstanceState', 'Account$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the Account wrapper; the first getParcelable unparcels the bundle, and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the activity is recreated from a saved state: onCreate calls restoreInstanceState (line 103) only when savedInstanceState is not null (line 102)',
  cls='non_standard', via='savedInstanceState.getParcelable(KEY_ACCOUNT_ENTITY) at AccountEditActivity.java:587 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readValue calls readParcelable (FW-SRC Parcel.java:2744-2745, 2841-2851), which reads the CREATOR field (FW-SRC Parcel.java:2894) and calls creator.createFromParcel (FW-SRC Parcel.java:2851)',
  evidence='SRC account/AccountEditActivity.java:102-103, 586-599 (line 587); FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2744-2745, 2841-2851, 2894; label_060.grep.txt block A')

# ================================================================== UNREACHABLE: the typed-array creator (no typed array of Account wrappers is parcelled)

UNREACHABLE['Account$$Parcelable$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC Parcel.java:2640-2645, c.newArray(N) at 2645), that is, when app code reads a typed array of Account wrappers with this creator. No app code builds or reads such an array: the Account arrays and lists in the source root are declarations and service return values, none parcelled (label_060.grep.txt blocks B and C), and no app code names Account$$Parcelable.CREATOR (block D, empty). No auto_calls.json record has newArray as dst or $1.newArray as src. The Parceler library is not read: whether it calls newArray itself is INFERRED',
  'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_060.grep.txt blocks B, C, D; generated class not in the source root (build class file: newArray descriptor (I)[Lcom/money/manager/ex/domainmodel/Account$$Parcelable;, label_060.grep.txt constant-pool block)',
  'INFERRED')
