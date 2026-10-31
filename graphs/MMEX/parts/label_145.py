# ================================================================== batch 145 (label_145): Parceler wrapper Money$$Parcelable and its $1 creator (10 methods, 1 class)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_145.md (4 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_145.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 6 UNREACHABLE entries and 4 sup pairs.
# No e() edge is written: every route into this batch is an auto CALL record in auto_calls.json (D7). The live routes come from SearchParameters$$Parcelable.write (line 66) and .read (line 124), owned by batch 108 (merged).
# Each Money$$Parcelable method is generated Parceler code, so each UNREACHABLE entry is confirmed_by INFERRED (D16) and rests on the grep and class-file output in label_145.grep.txt (D5).
# sup pairs (D14a): the auto CALL records from the two UNREACHABLE callers in this batch are cut. createFromParcel (row 9) has three records at line 27, and writeToParcel (row 7) has one at line 44. The targets stay reachable through the live SearchParameters routes.

# ---- UNREACHABLE entries: (kind, reason, evidence, confirmed_by)

UNREACHABLE['Money$$Parcelable.<init>'] = ('framework_never_calls',
    'the only caller is Money$$Parcelable$1.createFromParcel (auto record line 27); the framework calls that creator only for a parcel that names this class, and no Money$$Parcelable is ever written (no app Parcels.wrap takes a Money)',
    'grep A1 (wrap and unwrap arguments), A2 (no Money$$Parcelable in app source), C1, C3 (line 27); FW-SRC Parcel.java:2841-2851, 2867 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable.describeContents'] = ('framework_never_calls',
    'the framework calls it only from Bundle.hasFileDescriptors, for a Parcelable value in a bundle; no Money$$Parcelable is put in a bundle (the only Parcelable put of a wrapped Money is the dead PriceDownloadedEventBundler.java:37 wrap of a PriceDownloadedEvent)',
    'grep B3 (putParcelable sites), A1, C3 (no auto record calls it); FW-SRC Bundle.java:316-332 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'the ParcelWrapper accessor that Parcels.unwrap calls on a wrapper object; no app Parcels.unwrap receives a Money wrapper, and no app code makes a Money$$Parcelable (library behaviour INFERRED)',
    'grep A1 (distinct argument list), A2, C2 (public 0x0001 with bridge 0x1041), C3 (no auto record calls it)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable.writeToParcel'] = ('framework_never_calls',
    'Parcel.writeParcelable calls it only for a Money$$Parcelable instance, and none is created; its auto call to write (line 44) is cut by sup',
    'grep A1, A2, C1, C3 (line 44); FW-SRC Parcel.java:1785-1791 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable$1.createFromParcel'] = ('framework_never_calls',
    'the framework calls it through Parcel.readParcelable (Parcel.java:2842, 2851) only for a parcel that names this class, and none is written (see Money$$Parcelable.<init>); its three auto calls (line 27) are cut by sup',
    'grep A1, A2, C2, C3 (line 27); FW-SRC Parcel.java:2841-2851, 2867 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable$1.newArray'] = ('framework_never_calls',
    'the framework calls a Creator newArray only from Parcel.createTypedArray, and the app has no createTypedArray, readTypedArray or writeTypedArray call',
    'grep B1 (count 0), C2 (public 0x0001); FW-SRC Parcel.java:2640-2645 (grep D1)',
    'INFERRED')

# ---- sup pairs (D14a): auto CALL records from the UNREACHABLE callers in this batch

sup(('Money$$Parcelable$1.createFromParcel', 'Money$$Parcelable.<clinit>'))  # createFromParcel is UNREACHABLE (row 9), so its auto call at line 27 cannot run
sup(('Money$$Parcelable$1.createFromParcel', 'Money$$Parcelable.<init>'))  # same record family, line 27: <init> is UNREACHABLE (row 2)
sup(('Money$$Parcelable$1.createFromParcel', 'Money$$Parcelable.read'))  # same record family, line 27: read stays REACHABLE through SearchParameters$$Parcelable.read (line 124)
sup(('Money$$Parcelable.writeToParcel', 'Money$$Parcelable.write'))  # writeToParcel is UNREACHABLE (row 7), so its auto call at line 44 cannot run; write stays REACHABLE through SearchParameters$$Parcelable.write (line 66)
