# L5 verdicts — Room residuals (batch 48) + UriConverter ctor (batch 4)

Task-3 rows ONLY. Identities verified first from
`phase3/work/batch48-merge-ready.md` and `phase3/work/batch4-merge-ready.md`
(copies, read-only). Old labels are the OPEN labels in those files.
Saved greps: `phase3/greps/L5/grep_48_07_clearAllTables.txt`,
`grep_48_19_dropAllTables.txt`, `grep_48_12_13_autoMigrations.txt`,
`grep_4_11_uriconverter.txt`, `grep_othersets_destructive.txt`.
AppDatabase.java print: corpus `core/storage/AppDatabase.java`
(`@Database` :42–52, `buildDatabase` :81–86, `addMigrations` :84, no
fallback of any kind). No build/sampler/C1 claimed. No tick written.

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 48/7 | AppDatabase_Impl.clearAllTables | OPEN | UNREACHABLE no_trigger_in_app | INFERRED | D31: zero `clearAllTables` hits in all 281 app Java files and all 73 res-layout XML (saved grep); zero in test/androidTest other-sourcesets; Room print (RoomDatabase, googlesource commit e07e805b1b62404193b376b80b3fcaa2051a4444, RoomDatabase.android.kt) shows `clearAllTables()` as an abstract PUBLIC API (:1008) with no internal caller in the init/open path printed (init :468–476 calls createConnectionManager/createInvalidationTracker/validateAutoMigrations/validateTypeConverters only) — i.e. the only possible caller is app code, and app code has none | A printed app-code `clearAllTables` (or `db.clearAllTables`) call, or a printed Room-internal call to it |
| 48/12 | AppDatabase_Impl.getAutoMigrations(Map) | OPEN | OPEN | — | STAYS OPEN per D31: no deciding print obtained. App Room version is 2.6.1 (app/build.gradle: `def ROOM_VERSION = '2.6.1'`, saved grep room_version.txt). Attempted print: RoomDatabase.android.kt (googlesource, commit e07e805b1b62404193b376b80b3fcaa2051a4444 — current Room 3/KMP, NOT the app's 2.6.1) shows init() calling validateAutoMigrations(configuration) (:474) and a base getAutoMigrations(autoMigrationSpecs) (:686–694) whose KMP wrapper createAutoMigrations calls it (:700–716), but the validateAutoMigrations BODY (common code, not in this file) is unprinted, so it is NOT shown whether getAutoMigrations runs unconditionally at open or only when auto-migrations are declared. App side is confirmed: `@Database` :42–52 lists entities + version 9 only, zero `@AutoMigration`/`AutoMigrationSpec` hits in 281 Java + 73 res-layout (saved grep) | A printed Room 2.6.1 Builder.build()/init/validateAutoMigrations path showing either (a) unconditional getAutoMigrations call at open → REACHABLE INFERRED, or (b) call only when auto-migrations are declared → UNREACHABLE no_trigger_in_app INFERRED (none declared) |
| 48/13 | AppDatabase_Impl.getRequiredAutoMigrationSpecs() | OPEN | OPEN | — | STAYS OPEN per D31, same missing print as 48/12: the Room 3 print shows the BASE getRequiredAutoMigrationSpecs() returning emptySet() (:958–962) and the KMP wrapper delegating to it (:968–978), but NOT the generated Impl's override nor any caller of it at open, and NOT the app's Room 2.6.1 open path. App side confirmed: no auto-migration specs declared (`@Database` :42–52; zero AutoMigrationSpec hits, saved grep) | A printed Room 2.6.1 open-path call to the generated getRequiredAutoMigrationSpecs, or a printed generated Impl showing it is called only when specs are declared (→ UNREACHABLE no_trigger_in_app INFERRED, none declared) |
| 48/19 | AppDatabase_Impl$1.dropAllTables(SupportSQLiteDatabase) | OPEN | UNREACHABLE closed_by_configuration | INFERRED | D31: zero `dropAllTables`, `fallbackToDestructiveMigration`, `fallbackToDestructiveMigrationOnDowngrade`, `allowDestructiveMigration*`, `onDowngrade` hits in all 281 app Java files + 73 res-layout + test/androidTest other-sourcesets (saved greps); printed buildDatabase (AppDatabase.java :81–86) uses `.addMigrations(DatabaseMigration.getMigrations(appContext))` only, with NO destructive-migration fallback configured — so the only library path to dropAllTables (downgrade/destructive migration) is closed by this database's configuration | A printed fallback configuration (fallbackToDestructiveMigration / OnDowngrade) for this database, or a printed Room/generated dispatch calling dropAllTables in this configuration |
| 4/11 | UriConverter.<init> | OPEN | UNREACHABLE no_trigger_in_app | INFERRED | D13/D32 test, all three premises verified from printed source: (i) ALL methods static — UriConverter.java:27 class, static toUri :30–32, static fromUri :36–38, no instance members, no explicit ctor; (ii) zero `new UriConverter` sites in all 281 app Java files (only hits: AppDatabase.java:36 import, :53 `@TypeConverters({UriConverter.class})`, UriConverter.java:27 definition) and zero in 73 res-layout XML and zero in test/androidTest other-sourcesets (saved grep); (iii) no framework/library construction path printed — Room registration (`@TypeConverters`) is class-reference only, and D3c covers only getRequiredConverters methods, not this ctor | A printed `new UriConverter` site, or printed generated Room code instantiating UriConverter |

## Flips in this file: 3
- 48/7 OPEN → UNREACHABLE no_trigger_in_app INFERRED
- 48/19 OPEN → UNREACHABLE closed_by_configuration INFERRED
- 4/11 OPEN → UNREACHABLE no_trigger_in_app INFERRED

## Stays OPEN: 2 (48/12, 48/13)
- Failing premise for both: no deciding Room open-path print (see rows).
  The attempted Room 3 print is recorded above with version/commit and
  lines; it does NOT decide unconditional-vs-declared-only, and it is
  not the app's Room version, so neither row is flipped on it.
