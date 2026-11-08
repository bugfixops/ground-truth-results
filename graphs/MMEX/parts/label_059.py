# ================================================================== batch 059 (label_059): Account (34 methods) and
# Account$$Parcelable (6 methods: <clinit>, <init>, describeContents, getParcel, read, write).
# Result: 38 REACHABLE, 2 UNREACHABLE (Account.getType SOURCE; Account$$Parcelable.describeContents INFERRED).
# Rows and printed lines: graphs/MMEX/parts/label_059.md. Grep evidence for the generated UNREACHABLE row: graphs/MMEX/parts/label_059.grep.txt.
# The class is domainmodel/Account (the brief named ex/Account; the batch file and source use domainmodel).
# Most Account routes are the auto CALL records from AccountEditActivity and are not rewritten here (D7).
# This file writes:
#   - two library CALL edges from WatchlistFragment.onSaveInstanceState (Parcels.wrap, INFERRED) and one from
#     WatchlistFragment.onCreate (Parcels.unwrap, INFERRED); they reach the generated wrapper Account$$Parcelable,
#   - UNREACHABLE entries for Account.getType (no caller) and Account$$Parcelable.describeContents (framework never calls it),
#   - 3 sup pairs (D14a): the auto CALL records from the UNREACHABLE Account.getType (Account.java:120, 121).
# Interim (D8): Account$$Parcelable.read and write are reached through Account$$Parcelable$1.createFromParcel and
# Account$$Parcelable.writeToParcel, which are in batch 060; WatchlistFragment is in a batch that is not merged yet.

e('WatchlistFragment.onSaveInstanceState', 'Account$$Parcelable.<clinit>', 'CALL',
  'the watchlist fragment is saved: onSaveInstanceState puts Parcels.wrap(mAccount) into the state, the library creates the generated wrapper, and the first use of the class runs its static initializer',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): creates Account$$Parcelable, which initialises the class',
  evidence='SRC investment/watchlist/WatchlistFragment.java:276-281 (putParcelable of Parcels.wrap at 280); generated Account$$Parcelable.java is not in the tree: auto_calls.json record <clinit> -> Account$$Parcelable$1.<init> at Account$$Parcelable.java:23')

e('WatchlistFragment.onSaveInstanceState', 'Account$$Parcelable.<init>', 'CALL',
  'the same save path: Parcels.wrap calls the wrapper constructor with the Account (the restore path is the other caller, createFromParcel -> <init> at Account$$Parcelable.java:28, batch 060)',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): new Account$$Parcelable(Account)',
  evidence='SRC investment/watchlist/WatchlistFragment.java:280; generated Account$$Parcelable.java not in the tree: auto_calls.json record Account$$Parcelable$1.createFromParcel -> Account$$Parcelable.<init> at Account$$Parcelable.java:28')

e('WatchlistFragment.onCreate', 'Account$$Parcelable.getParcel', 'CALL',
  'the watchlist fragment is restored with a saved state (savedInstanceState non-null, line 120): Parcels.unwrap casts the wrapper and calls getParcel to get the Account',
  cls='non_standard',
  via='org.parceler.Parcels.unwrap (library, not read; INFERRED): calls getParcel on the ParcelWrapper',
  evidence='SRC investment/watchlist/WatchlistFragment.java:120-121 (condition at 120, Parcels.unwrap at 121)')

UNREACHABLE['Account.getType'] = ('no_trigger_in_app',
    'no app code calls Account.getType: the getType() call sites in app source are Dataset.getType (MmxContentProvider.java:161, 204, 242, 397, 433), NetworkInfo.getType (NetworkUtils.java:66) and the Gson TypeToken getType (RecentDatabasesProvider.java:208); auto_calls.json has no record into Account.getType; its three outgoing auto CALL records (Account.java:120, 121) are cut by the sup below (D14a)',
    'Account.java:119-122; MmxContentProvider.java:161; NetworkUtils.java:66; label_059.grep.txt section 5', 'SOURCE')

UNREACHABLE['Account$$Parcelable.describeContents'] = ('framework_never_calls',
    'the generated describeContents returns 0 and no app code calls describeContents or hasFileDescriptors (grep: definitions only); the framework calls it only in the unparcelled-map walk of Bundle.hasFileDescriptors (Bundle.java:316-362, calls at 329, 338, 349, 362), which Bundle.describeContents (1217) and Intent.describeContents (Intent.java:9553) reach, and Intent.describeContents has no caller in core/java or services/core/java; the system_server callers (AMS.java:4652, 4797, 5030, 7453, 7588) hold parcelled bundles and intents, so the walk does not run on this class there (INFERRED)',
    'Bundle.java:316-362; Bundle.java:1208-1220; Intent.java:9553; AMS.java:7453; label_059.grep.txt sections 1-4', 'INFERRED')

sup(('Account.getType', 'Account.getTypeName'),
    ('Account.getType', 'AccountTypes.<clinit>'),
    ('Account.getType', 'AccountTypes.get'))
