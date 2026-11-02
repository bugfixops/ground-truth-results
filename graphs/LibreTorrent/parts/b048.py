# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# LibreTorrent part b048 — converter C07 delivery.
# Base: audited A3 output helper/a3-g10/parts/b048.py (content below verbatim apart
# from this header; labels/kinds verified against the authoritative batch file:
# merger/staging-A1/graphs/LibreTorrent/scratch/merge-ready/batch48-merge-ready.md (A1-affected)).
# Stronger-evidence rule (b): checked the merger tree's graph_def.py (read-only) for
# every UNREACHABLE key in this part. The tree holds NO UNREACHABLE grade for any key
# in this part, so NO grade changes were made and no SOURCE was downgraded to INFERRED;
# every UNREACHABLE grade below stands exactly as audited.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/48/ (see REPORT-b048.md).
# Branch head at pre-test: f8676c8a (LibreTorrent b007 landed; merger-tree MERGED_PARTS
# tail b007.py matched the head's last part, so the pre-test base was not moving).
# This part does NOT claim F1. Merger adds nothing from this header; the merger owns
# MERGED_PARTS and the push.
# Merger notes (kept as audited): batch-48 rows 12/13 (AppDatabase_Impl auto-migration
# getters) stand as UNREACHABLE framework_never_calls INFERRED per decision A1-C3
# (weakest A1 flips; revert only on a printed Room 2.6.1 runtime call site).
# Batch 48 part (sorting comparator, AppDatabase + generated Room Impl, DatabaseMigration).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b048_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated Room source (AppDatabase_Impl, AppDatabase_Impl$1) is absent from
# final_java_only (generated at build time), so every _Impl edge below is
# INFERRED generated dispatch, never SOURCE. No pre-existing route is relied
# on; every REACHABLE row below has an edge here.

# Sorting comparator: RxJava .sorted() dispatch to Comparator.compare.
e('MainFragment.observeTorrents', 'TorrentSortingComparator.compare', 'CALL', 'Observed torrent list is sorted with the view-model comparator', cls='non_standard', via='Rx sorted() dispatch to Comparator.compare', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:293,341; SRC TorrentSortingComparator.java:40-45')
e('TorrentService.startUpdateForegroundNotify', 'TorrentSortingComparator.compare', 'CALL', 'Foreground notification list is sorted with the service comparator', cls='non_standard', via='Rx sorted() dispatch to Comparator.compare', evidence='INFERRED Rx dispatch; SRC service/TorrentService.java:287,304; SRC TorrentSortingComparator.java:40-45')
e('MainViewModel.setSort', 'TorrentSortingComparator.getSorting', 'CALL', 'Force sort reads the comparator sorting', cls='explicit', evidence='SRC ui/main/MainViewModel.java:91; SRC TorrentSortingComparator.java:35')

# AppDatabase construction chain.
e('AppDatabase_Impl.<init>', 'AppDatabase.<init>', 'CALL', 'Generated subclass constructor calls the abstract-class super constructor', cls='explicit', evidence='INFERRED compiler-inserted super call (generated source unprinted); SRC AppDatabase.java:81-87')
e('AppDatabase.getInstance', 'AppDatabase.buildDatabase', 'CALL', 'Singleton first access builds the database', cls='explicit', evidence='SRC AppDatabase.java:74; SRC AppDatabase.java:81-86')
e('RepositoryHelper.getTorrentRepository', 'AppDatabase.getInstance', 'CALL', 'Torrent repository construction opens the database singleton', cls='explicit', evidence='SRC RepositoryHelper.java:47; SRC AppDatabase.java:69-79')
e('AppDatabase.buildDatabase', 'AppDatabase_Impl.<init>', 'CALL', 'Room databaseBuilder.build() instantiates the generated implementation', cls='non_standard', via='Room databaseBuilder.build() instantiates the generated implementation', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('FeedRepositoryImpl.observeAllFeeds', 'AppDatabase_Impl.createInvalidationTracker', 'CALL', 'First observed DAO query makes Room create the invalidation tracker', cls='non_standard', via='Room creates the invalidation tracker when the first DAO query is observed', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:126-129; SRC AppDatabase.java:61-67')
e('AppDatabase_Impl.<init>', 'AppDatabase_Impl.createOpenHelper', 'CALL', 'Room calls createOpenHelper during database build/open', cls='non_standard', via='Room calls createOpenHelper during database build/open', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('TorrentRepositoryImpl.addFastResume', 'AppDatabase_Impl.fastResumeDao', 'CALL', 'Fast-resume write goes through the generated DAO accessor', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:91-93; SRC AppDatabase.java:63')
e('FeedRepositoryImpl.addFeed', 'AppDatabase_Impl.feedDao', 'CALL', 'Feed write goes through the generated DAO accessor', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC FeedRepositoryImpl.java:84-87; SRC AppDatabase.java:65')
e('AppDatabase_Impl.<init>', 'AppDatabase_Impl.getRequiredTypeConverters', 'CALL', 'Room database-build validation reads the required type converters', cls='non_standard', via='Room database-build validation dispatch', evidence='INFERRED Room dispatch; SRC AppDatabase.java:53,81-87')
e('TagRepositoryImpl.delete', 'AppDatabase_Impl.tagInfoDao', 'CALL', 'Tag delete goes through the generated DAO accessor', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TagRepositoryImpl.java:49-51; SRC AppDatabase.java:67')
e('TorrentRepositoryImpl.addTorrent', 'AppDatabase_Impl.torrentDao', 'CALL', 'Torrent write goes through the generated DAO accessor', cls='non_standard', via='virtual dispatch to the generated Impl override', evidence='INFERRED Room dispatch; SRC TorrentRepositoryImpl.java:56-58; SRC AppDatabase.java:61')

# Generated open-helper delegate and its callbacks.
e('AppDatabase_Impl.createOpenHelper', 'AppDatabase_Impl$1.<init>', 'CALL', 'Room creates the open-helper delegate during database build/open', cls='non_standard', via='Room creates the open-helper delegate during database build/open', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('AppDatabase_Impl$1.onCreate', 'AppDatabase_Impl$1.createAllTables', 'CALL', 'First creation creates all tables', cls='non_standard', via='Room open-helper delegate creates tables on first creation', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('AppDatabase_Impl.createOpenHelper', 'AppDatabase_Impl$1.onCreate', 'CALL', 'First database open runs the delegate onCreate', cls='non_standard', via='Room/SQLite first-open dispatch to the generated delegate', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('AppDatabase_Impl.createOpenHelper', 'AppDatabase_Impl$1.onOpen', 'CALL', 'Every database open runs the delegate onOpen', cls='non_standard', via='Room/SQLite every-open dispatch to the generated delegate', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('AppDatabase_Impl.createOpenHelper', 'AppDatabase_Impl$1.onPostMigrate', 'CALL', 'Database upgrade runs the delegate onPostMigrate', cls='non_standard', via='Room migration-path dispatch to the generated delegate (STATE gate: existing older-version database)', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('AppDatabase_Impl.createOpenHelper', 'AppDatabase_Impl$1.onPreMigrate', 'CALL', 'Database upgrade runs the delegate onPreMigrate', cls='non_standard', via='Room migration-path dispatch to the generated delegate (STATE gate: existing older-version database)', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')
e('AppDatabase_Impl.createOpenHelper', 'AppDatabase_Impl$1.onValidateSchema', 'CALL', 'Database open validates the schema through the delegate', cls='non_standard', via='Room schema-validation dispatch on open', evidence='INFERRED Room dispatch; SRC AppDatabase.java:81-87')

# DatabaseMigration: class init, registration, anonymous migrations.
e('DatabaseMigration.getMigrations', 'DatabaseMigration.<clinit>', 'FRAMEWORK', 'First use of getMigrations initialises the migration class', cls='non_standard', via='JVM class initialization on first active use of DatabaseMigration', evidence='INFERRED JVM dispatch; SRC DatabaseMigration.java:43-55')
e('AppDatabase.buildDatabase', 'DatabaseMigration.getMigrations', 'CALL', 'Database build registers the migration list', cls='explicit', evidence='SRC AppDatabase.java:84; SRC DatabaseMigration.java:43-55')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$1.<init>', 'CALL', 'Class initialisation constructs the Migration(1, 2) field', cls='explicit', evidence='SRC DatabaseMigration.java:57')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$1.migrate', 'CALL', 'Room invokes the registered Migration on version step 1 to 2', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v1 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,57-63')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$2.<init>', 'CALL', 'Class initialisation constructs the Migration(2, 3) field', cls='explicit', evidence='SRC DatabaseMigration.java:66')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$2.migrate', 'CALL', 'Room invokes the registered Migration on version step 2 to 3', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v2 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,67-72')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$3.<init>', 'CALL', 'Class initialisation constructs the Migration(3, 4) field', cls='explicit', evidence='SRC DatabaseMigration.java:75')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$3.migrate', 'CALL', 'Room invokes the registered Migration on version step 3 to 4', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v3 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,76-80')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$4.<init>', 'CALL', 'Class initialisation constructs the Migration(5, 6) field', cls='explicit', evidence='SRC DatabaseMigration.java:83')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$4.migrate', 'CALL', 'Room invokes the registered Migration on version step 5 to 6', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v5 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,84-89')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$5.<init>', 'CALL', 'Class initialisation constructs the Migration(6, 7) field', cls='explicit', evidence='SRC DatabaseMigration.java:92')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$5.migrate', 'CALL', 'Room invokes the registered Migration on version step 6 to 7', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v6 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,93-99')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$6.<init>', 'CALL', 'Class initialisation constructs the Migration(7, 8) field', cls='explicit', evidence='SRC DatabaseMigration.java:102')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$6.migrate', 'CALL', 'Room invokes the registered Migration on version step 7 to 8', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v7 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,103-106')
e('DatabaseMigration.<clinit>', 'DatabaseMigration$7.<init>', 'CALL', 'Class initialisation constructs the Migration(8, 9) field', cls='explicit', evidence='SRC DatabaseMigration.java:109')
e('DatabaseMigration.getMigrations', 'DatabaseMigration$7.migrate', 'CALL', 'Room invokes the registered Migration on version step 8 to 9', cls='non_standard', via='Room invokes a registered Migration when opening an older-version database (STATE gate: existing v8 database)', evidence='INFERRED Room dispatch; SRC DatabaseMigration.java:43-55,110-113')

UNREACHABLE.update({
    'AppDatabase_Impl.clearAllTables': ('no_trigger_in_app',
        'No printed app caller; saved full-tree grep over 252 app Java files has zero clearAllTables hits tree-wide, and the normal database-open path (buildDatabase, Room.databaseBuilder + addMigrations + build) does not call it.',
        'SRC AppDatabase.java:81-87',
        'INFERRED'),
    'AppDatabase_Impl.getAutoMigrations': ('framework_never_calls',
        'A1 2026-11-01: AppDatabase @Database declares entities + version 9 only, no auto-migrations; auto_calls.json shows zero callers; Room never collects auto-migrations.',
        'SRC AppDatabase.java:42-52',
        'INFERRED'),
    'AppDatabase_Impl.getRequiredAutoMigrationSpecs': ('framework_never_calls',
        'A1 2026-11-01: no auto-migration specs declared on AppDatabase; auto_calls.json shows zero callers; Room never collects specs.',
        'SRC AppDatabase.java:42-52',
        'INFERRED'),
    'AppDatabase_Impl$1.dropAllTables': ('closed_by_configuration',
        'Generated Impl source absent; saved full-tree grep has zero dropAllTables, fallbackToDestructiveMigration and onDowngrade hits, and buildDatabase uses addMigrations only with no destructive-migration fallback, so the downgrade/destructive trigger for this database is closed by configuration.',
        'SRC AppDatabase.java:81-87',
        'INFERRED'),
})

# No SUPPRESS entries: recomputed 2026-11-01 from auto_calls.json plus a
# bytecode invoke scan over work-emulator/classes/LibreTorrent/0 — zero
# callers of the four UNREACHABLE methods above anywhere in the class
# tree, and no REACHABLE method in this batch calls an UNREACHABLE
# method in bytecode. See REPORT.md for the full recomputation.
SUPPRESS.update(set())
