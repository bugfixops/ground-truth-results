# ================================================================== batch 064 (label_064): Category (8 methods),
# Category$$Parcelable (7), Category$$Parcelable$1 (3). 18 methods in total.
# Result: 6 REACHABLE, 12 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_064.md.
# Evidence for the generated and library rows: graphs/MMEX/parts/label_064.grep.txt.
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - UNREACHABLE entries for Category.<init>(ContentValues) and Category.setParentId (SOURCE),
#     and for the ten Category$$Parcelable and Category$$Parcelable$1 methods (INFERRED, generated code),
#   - 8 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# No e() edges: the REACHABLE methods are reached by auto CALL records (D7). No SCREENS entry: the pages used
# (S_CATEGORY_LIST, S_BUDGET_DETAIL) are defined by batches 015, 016 and 029.

# ================================================================== UNREACHABLE: Category (source)

UNREACHABLE['Category.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no caller: the only construction in src/main is new Category() (no-arg, CategoryListFragment.java:399); the class scan finds 0 invokes of this constructor; RepositoryBase.newInstance is the no-arg resultType.newInstance() (RepositoryBase.java:109, 134); its auto CALL to EntityBase.<init>(ContentValues) is cut by sup below',
    'Category.java:39-41; Category.java:40 (auto record); CategoryListFragment.java:399; RepositoryBase.java:109, 134; label_064.grep.txt', 'SOURCE')

UNREACHABLE['Category.setParentId'] = ('no_trigger_in_app',
    'no caller: the only source reference is the definition (grep setParentId over src/main); the class scan finds 0 invokes of Category.setParentId in any class; no setter reflection (grep getMethod/getDeclaredMethod); its auto CALL to EntityBase.setInt is cut by sup below',
    'Category.java:55-57; Category.java:56 (auto record); label_064.grep.txt', 'SOURCE')

# ================================================================== UNREACHABLE: Category$$Parcelable and $1 (generated, INFERRED)

UNREACHABLE['Category$$Parcelable.<clinit>'] = ('no_trigger_in_app',
    'the static initializer runs on first use of the class; the class is never used: no class outside the group references Category$$Parcelable (class-file scan), and no Parcels.wrap call takes a Category (23 Parcels.wrap lines, none with a Category argument). Its auto CALL to $1.<init> is cut by sup below',
    'Category$$Parcelable.java:23 (generated; LineNumberTable of Category$$Parcelable.class, not on disk); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.<init>'] = ('no_trigger_in_app',
    'the constructor of the wrapper (Category argument); called only by Category$$Parcelable$1.createFromParcel (auto CALL, line 28), which is itself unreachable; that auto CALL is cut by sup below',
    'Category$$Parcelable.java:39-41 (generated); Category$$Parcelable.java:28 (auto record); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.describeContents'] = ('framework_never_calls',
    'Parcelable method of the wrapper; no Category is ever wrapped (grep and class-file scan, see the grep file), so no parcel of this class is written and the framework never calls it here (same shape as Account$$Parcelable.describeContents, batch 059)',
    'Category$$Parcelable.java:60 (generated); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'generated accessor of the wrapper (the erased bridge getParcel()Object is at line 12); its callers would be Parcels.unwrap or a @Parcel field holding a Category, and the class scan finds none (no class outside the group references Category$$Parcelable)',
    'Category$$Parcelable.java:65 (generated), bridge :12; label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.read'] = ('no_trigger_in_app',
    'called only by Category$$Parcelable$1.createFromParcel (auto CALL, line 28), which is unreachable; the body (lines 69-83) would build a Category through Category.<init>() (auto CALL at line 78, cut by sup below)',
    'Category$$Parcelable.java:69-83 (generated); Category$$Parcelable.java:78 and :28 (auto records); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.write'] = ('no_trigger_in_app',
    'called only by writeToParcel (auto CALL, line 45), which is unreachable; the auto record is cut by sup below',
    'Category$$Parcelable.java:49-56 (generated); Category$$Parcelable.java:45 (auto record)', 'INFERRED')

UNREACHABLE['Category$$Parcelable.writeToParcel'] = ('no_trigger_in_app',
    'the Parcelable.writeToParcel body; the framework calls it only when a Category$$Parcelable is written to a Parcel (Parcels.wrap or putParcelable), which never happens (no Category is wrapped, see the grep file). Its auto CALL to write is cut by sup below',
    'Category$$Parcelable.java:45-46 (generated); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable$1.<init>'] = ('no_trigger_in_app',
    'the CREATOR constructor; created only by the static initializer Category$$Parcelable.<clinit> (auto CALL, line 23), which is unreachable; the auto record is cut by sup below',
    'Category$$Parcelable.java:23 (generated; LineNumberTable of Category$$Parcelable$1.class)', 'INFERRED')

UNREACHABLE['Category$$Parcelable$1.createFromParcel'] = ('no_trigger_in_app',
    'the CREATOR callback; the framework calls it only for a parcel that holds a Category$$Parcelable, which is never written (see the grep file); its three auto CALLs (to <clinit>, <init> and read, line 28) are cut by sup below',
    'Category$$Parcelable.java:28 (generated; LineNumberTable of Category$$Parcelable$1.class); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable$1.newArray'] = ('no_trigger_in_app',
    'the CREATOR array factory; the framework calls it only for arrays of Category$$Parcelable, which never occur (no reference to this CREATOR outside the group)',
    'Category$$Parcelable.java:33 (generated; the erased bridge newArray(I)Object is at :23); label_064.grep.txt', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('Category.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'))
sup(('Category.setParentId', 'EntityBase.setInt'))
sup(('Category$$Parcelable.writeToParcel', 'Category$$Parcelable.write'))
sup(('Category$$Parcelable.read', 'Category.<init>()'))
sup(('Category$$Parcelable.<clinit>', 'Category$$Parcelable$1.<init>'))
sup(('Category$$Parcelable$1.createFromParcel', 'Category$$Parcelable.<clinit>'))
sup(('Category$$Parcelable$1.createFromParcel', 'Category$$Parcelable.<init>'))
sup(('Category$$Parcelable$1.createFromParcel', 'Category$$Parcelable.read'))
