# R4 summary — LibreTorrent batch 48, rows 12 and 13 (Room auto-migrations)

Branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`, LibreTorrent
ONLY. No pushes, no branch edits, no work-file edits (the batch-48 merge-ready
file was read only), no tick marker written. Verdict files:
`phase3/verdicts/R4/48_12.md`, `phase3/verdicts/R4/48_13.md`; saved grep:
`phase3/verdicts/R4/grep_R4_autoMigrations.txt` (command + full output).

## Verdicts

| batch/row | method | old label | NEW label | confirmed_by |
| 48/12 | AppDatabase_Impl.getAutoMigrations(Map) | OPEN | OPEN | — |
| 48/13 | AppDatabase_Impl.getRequiredAutoMigrationSpecs() | OPEN | OPEN | — |

Both rows stay OPEN. No flip in either direction. No build, sampler, C1, or
device check claimed.

## What was verified this pass (both rows)

- Identities from `phase3/work/batch48-merge-ready.md`: row 12 =
  `AppDatabase_Impl.getAutoMigrations(Map)`, row 13 =
  `AppDatabase_Impl.getRequiredAutoMigrationSpecs()`, both OPEN.
- Room version 2.6.1 (`app/build.gradle`: `def ROOM_VERSION = '2.6.1'`,
  `androidx.room:room-runtime:$ROOM_VERSION`).
- `@Database` declaration, corpus `core/storage/AppDatabase.java:42-52`:
  entities only + version 9; NO `autoMigrations` element, NO spec element.
  (`@TypeConverters({UriConverter.class})` at :53 is not an auto-migration
  declaration.)
- App build path, `AppDatabase.java:81-86` (`buildDatabase`,
  `Room.databaseBuilder(...).addMigrations(...).build()`), called from
  `getInstance` at :74. Library side of `build()` for 2.6.1 unprinted.
- Saved corpus grep (R4): `getAutoMigrations|getRequiredAutoMigrationSpecs`
  ZERO in 281 app Java + ZERO in 73 res-layout XML + ZERO in
  test/androidTest other-sourcesets; `AutoMigration|autoMigrations` ZERO in
  281 app Java. Zero declarations + zero app callers verified — but, per the
  batch-48 conditional table, an app-tree zero alone cannot close a
  generated-dispatch row.

## What was attempted and NOT obtained (the single deciding gap, shared)

- 13 browser.search angles for the Room 2.6.1 runtime source
  (`RoomDatabase` init / `validateAutoMigrations` / `RoomOpenHelper` /
  `Builder.build`, `androidx.room:room-runtime` 2.6.1). Every source-code hit
  returned the same current Room 3 / KMP file
  (`RoomDatabase.android.kt`, googlesource commit
  e07e805b1b62404193b376b80b3fcaa2051a4444), fetched in full this pass
  (page id 1433643267769367865, 4330 lines). It shows `init()` calling
  `validateAutoMigrations(configuration)` (:474) and base
  `getAutoMigrations` (:686-694, deprecated "No longer implemented by
  generated") / `getRequiredAutoMigrationSpecs` (:958-962, same deprecation,
  returning `emptySet()`), but `validateAutoMigrations` occurs ONLY at its
  call site in that file — its BODY is common code, unprinted — and no caller
  of `getRequiredAutoMigrationSpecs` at open is printed at all.
- Per the task rule, the Room 3 print is NOT cited as deciding 2.6.1
  behaviour, and it could not decide even Room 3's unconditional-vs-declared
  question on this evidence. No 2.6.1 print was obtainable via the sanctioned
  search-and-fetch route; no 2.6.1 artifact exists locally on this VM.
- EXACT MISSING PRINT (the one item that would close both rows, possibly
  separately): the Room 2.6.1 `RoomDatabase` `Builder.build()` / `init()` /
  `validateAutoMigrations` path — i.e. the 2.6.1 body of
  `validateAutoMigrations` showing whether it calls the generated
  `getAutoMigrations(Map)` and/or `getRequiredAutoMigrationSpecs()`
  unconditionally at database open or only when auto-migrations / specs are
  declared. A generated 2.6.1 `AppDatabase_Impl` print showing which of the
  two methods the compiler emits for a zero-auto-migration database would
  also separate the rows.

## Why neither flip rule fires (both rows)

- REACHABLE INFERRED needs a printed unconditional-at-open invocation of the
  generated method on the app's 2.6.1 build path — not obtained.
- UNREACHABLE needs a printed declared-only invocation PLUS the verified zero
  declarations / zero callers — the zero side is verified, the printed side is
  missing.
- D3c analogy explicitly NOT extended: D3c rests on a printed
  `@TypeConverters` declaration for converter validation to validate; no
  auto-migration declaration exists here for either method's validation to
  validate.
- Kind note for a future flip (not applied): no_trigger_in_app, NOT
  closed_by_configuration — no builder flag disables auto-migrations; the
  `addMigrations`-only builder line configures manual migrations, it is not an
  auto-migration disablement. The trigger simply does not exist in app code.

## Revert conditions (per-row, in 48_12.md / 48_13.md)

- 48/12 → REACHABLE INFERRED on a printed 2.6.1 open-path call to generated
  `getAutoMigrations(Map)` even with an empty map; → UNREACHABLE
  no_trigger_in_app INFERRED on a printed 2.6.1 declared-only call path.
- 48/13 → REACHABLE INFERRED on a printed 2.6.1 open-path call to generated
  `getRequiredAutoMigrationSpecs()`; → UNREACHABLE no_trigger_in_app INFERRED
  on a printed 2.6.1 declared-only call path.
- The rows were judged separately: they play different roles in validation
  (migration list vs required-spec set), so a future print could still split
  them even though both stay OPEN today.
