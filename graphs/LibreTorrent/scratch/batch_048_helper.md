# LibreTorrent batch 48 source audit

Membership is exactly the 40 rows printed at the top of `batch_048_helper_printed.txt`. The evidence file includes `TorrentSortingComparator`, `AppDatabase`, `DatabaseMigration`, `RepositoryHelper`, a direct caller search, and a search for the generated `AppDatabase_Impl` source. The generated implementation is not present in the uploaded Java source, so its target methods remain OPEN rather than inferred from library behavior. The remaining rows also stay OPEN because the full app-entry-to-database/comparator routes and Room callback dispatch have not been established. No missing caller match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `TorrentSortingComparator.compare(TorrentInfo,TorrentInfo)int` | OPEN | `TorrentSortingComparator.java:41+`; comparator source printed; caller-to-list display route unresolved. |
| 2 | `TorrentSortingComparator.getSorting()TorrentSorting` | OPEN | `TorrentSortingComparator.java:35+`; body printed, complete comparator construction/use route unresolved. |
| 3 | `AppDatabase.<init>()V` | OPEN | Abstract database class printed; no complete construction route established. |
| 4 | `AppDatabase.buildDatabase(Context)AppDatabase` | OPEN | `AppDatabase.java:81+`; builder and `RepositoryHelper` use printed; full application startup route unresolved. |
| 5 | `AppDatabase.getInstance(Context)AppDatabase` | OPEN | `AppDatabase.java:69+`; direct repository caller printed; caller's complete entry route unresolved. |
| 6 | `AppDatabase_Impl.<init>()V` | OPEN | Generated class source search printed no uploaded source file; Room-generated implementation/call route unavailable for source confirmation. |
| 7 | `AppDatabase_Impl.clearAllTables()V` | OPEN | Generated class source absent from upload; API/framework call path unresolved. |
| 8 | `AppDatabase_Impl.createInvalidationTracker()InvalidationTracker` | OPEN | Generated class source absent from upload; Room construction dispatch unresolved. |
| 9 | `AppDatabase_Impl.createOpenHelper(DatabaseConfiguration)SupportSQLiteOpenHelper` | OPEN | Generated class source absent from upload; Room builder dispatch unresolved. |
| 10 | `AppDatabase_Impl.fastResumeDao()FastResumeDao` | OPEN | Generated class source absent from upload; complete database-use route unresolved. |
| 11 | `AppDatabase_Impl.feedDao()FeedDao` | OPEN | Generated class source absent from upload; complete database-use route unresolved. |
| 12 | `AppDatabase_Impl.getAutoMigrations(Map)List` | OPEN | Generated class source absent from upload; Room migration dispatch unresolved. |
| 13 | `AppDatabase_Impl.getRequiredAutoMigrationSpecs()Set` | OPEN | Generated class source absent from upload; Room migration dispatch unresolved. |
| 14 | `AppDatabase_Impl.getRequiredTypeConverters()Map` | OPEN | Generated class source absent from upload; Room converter dispatch unresolved. |
| 15 | `AppDatabase_Impl.tagInfoDao()TagInfoDao` | OPEN | Generated class source absent from upload; complete database-use route unresolved. |
| 16 | `AppDatabase_Impl.torrentDao()TorrentDao` | OPEN | Generated class source absent from upload; complete database-use route unresolved. |
| 17 | `AppDatabase_Impl$1.<init>(AppDatabase_Impl,int)V` | OPEN | Generated implementation/anonymous callback source absent from upload; Room callback route unresolved. |
| 18 | `AppDatabase_Impl$1.createAllTables(SupportSQLiteDatabase)V` | OPEN | Generated implementation source absent from upload; Room schema callback route unresolved. |
| 19 | `AppDatabase_Impl$1.dropAllTables(SupportSQLiteDatabase)V` | OPEN | Generated implementation source absent from upload; Room schema callback route unresolved. |
| 20 | `AppDatabase_Impl$1.onCreate(SupportSQLiteDatabase)V` | OPEN | Generated implementation source absent from upload; Room callback dispatch unresolved. |
| 21 | `AppDatabase_Impl$1.onOpen(SupportSQLiteDatabase)V` | OPEN | Generated implementation source absent from upload; Room callback dispatch unresolved. |
| 22 | `AppDatabase_Impl$1.onPostMigrate(SupportSQLiteDatabase)V` | OPEN | Generated implementation source absent from upload; Room migration callback dispatch unresolved. |
| 23 | `AppDatabase_Impl$1.onPreMigrate(SupportSQLiteDatabase)V` | OPEN | Generated implementation source absent from upload; Room migration callback dispatch unresolved. |
| 24 | `AppDatabase_Impl$1.onValidateSchema(SupportSQLiteDatabase)ValidationResult` | OPEN | Generated implementation source absent from upload; Room schema callback route unresolved. |
| 25 | `DatabaseMigration.<clinit>()V` | OPEN | `DatabaseMigration.java` definitions printed; complete database initialization route unresolved. |
| 26 | `DatabaseMigration.getMigrations(Context)Migration[]` | OPEN | `DatabaseMigration.java:43+` and `AppDatabase.java` builder printed; Room callback/entry route unresolved. |
| 27 | `DatabaseMigration$1.<init>(int,int)V` | OPEN | Migration declaration printed in `DatabaseMigration.java`; construction through database build not fully traced. |
| 28 | `DatabaseMigration$1.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |
| 29 | `DatabaseMigration$2.<init>(int,int)V` | OPEN | Migration declaration printed; construction through database build not fully traced. |
| 30 | `DatabaseMigration$2.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |
| 31 | `DatabaseMigration$3.<init>(int,int)V` | OPEN | Migration declaration printed; construction through database build not fully traced. |
| 32 | `DatabaseMigration$3.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |
| 33 | `DatabaseMigration$4.<init>(int,int)V` | OPEN | Migration declaration printed; construction through database build not fully traced. |
| 34 | `DatabaseMigration$4.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |
| 35 | `DatabaseMigration$5.<init>(int,int)V` | OPEN | Migration declaration printed; construction through database build not fully traced. |
| 36 | `DatabaseMigration$5.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |
| 37 | `DatabaseMigration$6.<init>(int,int)V` | OPEN | Migration declaration printed; construction through database build not fully traced. |
| 38 | `DatabaseMigration$6.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |
| 39 | `DatabaseMigration$7.<init>(int,int)V` | OPEN | Migration declaration printed; construction through database build not fully traced. |
| 40 | `DatabaseMigration$7.migrate(SupportSQLiteDatabase)V` | OPEN | Migration body printed; Room version-selection and callback dispatch unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
