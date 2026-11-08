# A1 mapper + Room — EVIDENCE (helper only, NOT the merger)

- Work dir: `/home/hatch/workspace/finish/work/LibreTorrent/helper/A1-mapper-room/` (raw outputs in `raw/`).
- Read-only inputs: branch tree `/home/hatch/workspace/finish/clone/` (work-2026-10-31, HEAD 6805252);
  batch files `graphs/LibreTorrent/scratch/merge-ready/batch{2,12,17,48}-merge-ready.md`;
  app source `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main`;
  bytecode `graphs/LibreTorrent/auto_calls.json` and `/home/hatch/workspace/finish/work-emulator/classes/LibreTorrent/0/`.
- Nothing was edited outside this work dir. No merge-ready file, graph_def, parts file,
  verification.csv, PROGRESS file, or AGENT_NOTES was touched. Nothing was pushed. No APK was copied.
- Scope limit (applies to every row below): the extracted classes dir contains app classes plus
  generated databinding classes, but NOT the databinding library runtime
  (`DataBindingUtil`, `ViewDataBinding`, `MergedDataBinderMapper` — `raw/find_runtime_classes.txt`
  is empty; `raw/ls_androidx_databinding.txt` lists only `DataBinderMapperImpl.class`,
  `DataBindingComponent.class`, `library/`) and NOT the Room runtime (`androidx/room/` absent).
  Library dispatch therefore had to be checked against printed library source where noted, and
  every verdict below says whether it depends on such a print.
- `confirmed_by` convention used here: INFERRED = reached only through generated code and/or
  unprinted framework/library dispatch, or (for UNREACHABLE) absence over the complete printed
  corpus named per row. No row below is claimed SOURCE, because no app-code call site names any
  of these 8 methods directly.

## Shared trigger base (databinding rows)

App-code databinding use, freshly grepped over the clone app source (`raw/app_source_greps.txt`):
`DataBindingUtil.inflate` / `setContentView` sites include
`ui/addtorrent/AddTorrentActivity.java:102` (`setContentView`), `ui/addfeed/AddFeedDialog.java:202`,
`ui/addtorrent/AddTorrentFilesFragment.java:81`, `ui/detailtorrent/DetailTorrentFragment.java:150`
(inflate) — consistent with the 30-file / 35-site counts already recorded in batch 12 / batch 17.
App-source grep for `DataBinderMapperImpl|InnerBrLookup|InnerLayoutIdLookup|DataBindingTriggerClass`
over all app Java: 0 hits (the `0` count line in `raw/app_source_greps.txt`).
37 generated `*BindingImpl` classes exist in the classes dir (`raw/find_bindingimpl_classes.txt`).

## 2/38 — libretorrent.DataBinderMapperImpl$InnerBrLookup.<init> ()V

- Proposed verdict: **UNREACHABLE, kind `no_trigger_in_app`, confirmed_by INFERRED** (generated code).
- Evidence:
  - `raw/javap_InnerBrLookup.txt:5` — the ctor is `private` and its body only calls `Object.<init>`;
    the class's only other member is `static {}` (line 11) building static `sKeys`. Nothing in the
    class itself instantiates it.
  - `raw/binrefs_InnerBrLookup.txt` — only 2 class files in the whole extracted tree name
    `InnerBrLookup`: its own file and `DataBinderMapperImpl.class`.
  - `raw/javap_DataBinderMapperImpl.txt:1054` — the mapper's ONLY reference to `InnerBrLookup` is
    `getstatic InnerBrLookup.sKeys` inside `convertBrIdToString` (line 1052). There is NO
    `invokespecial InnerBrLookup.<init>` anywhere in the mapper (full 1234-line dump searched).
  - `raw/auto_calls_lookups.txt` — callers of `InnerBrLookup.<init>`: count 0; its only
    framework_calls entry is `Object.<init>`.
  - Why private matters: a private ctor of a nested class can legally be invoked only by the
    class itself or its enclosing (nestmate) class — both printed, neither instantiates it. No
    other class can invoke it, and no class file outside those two even names the class.
  - Distinction from batch 18 row 1 (the same class's `<clinit>`, already REACHABLE INFERRED):
    `<clinit>` runs on first static-field access (`convertBrIdToString` reading `sKeys`);
    `<init>` requires an instance that is never created. The `<clinit>` verdict does not transfer
    to `<init>`, under any of the batch-17 options (M-printed / M-dispatch / M-dispatch-full /
    M-direct) — none of them constructs an instance.
- Caveat: reflective instantiation would leave no constant-pool reference; there is zero evidence
  for it (private ctor, no name reference outside the mapper), so it is not a basis for REACHABLE.

## 2/39 — libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<init> ()V

- Proposed verdict: **UNREACHABLE, kind `no_trigger_in_app`, confirmed_by INFERRED** (generated code).
- Evidence: identical in structure to 2/38.
  - `raw/javap_InnerLayoutIdLookup.txt:5` — `private` ctor, body only `Object.<init>`; `static {}` at
    line 11 builds static `sKeys` (layout-name → id map).
  - `raw/binrefs_InnerLayoutIdLookup.txt` — only its own file and `DataBinderMapperImpl.class`
    name the class.
  - `raw/javap_DataBinderMapperImpl.txt:1039` — the mapper's ONLY reference is
    `getstatic InnerLayoutIdLookup.sKeys` inside `getLayoutId` (line 1033). No `invokespecial`
    to its `<init>` exists in the mapper dump.
  - `raw/auto_calls_lookups.txt` — callers of `InnerLayoutIdLookup.<init>`: count 0.
  - Same `<clinit>` vs `<init>` distinction as 2/38 (batch 18 row 2 is the `<clinit>` row).

## 2/40 — DataBindingTriggerClass.<init> ()V

- Proposed verdict: **UNREACHABLE, kind `no_trigger_in_app`, confirmed_by INFERRED** (generated code).
- Evidence:
  - `raw/javap_DataBindingTriggerClass.txt` (whole file, 8 lines) — class
    `org.proninyaroslav.libretorrent.DataBindingTriggerClass` with a single public empty ctor and
    NO static initializer, NO fields, NO other members. There is no load-triggered code at all.
  - `raw/binrefs_DataBindingTriggerClass.txt` — exactly ONE class file in the whole extracted tree
    names it: its own file. No generated `*BindingImpl`, no mapper, no app class references it.
  - `raw/auto_calls_lookups.txt` — callers of `DataBindingTriggerClass.<init>`: count 0; its only
    framework_calls entry is `Object.<init>`.
  - App-source grep for `DataBindingTriggerClass`: 0 hits (`raw/app_source_greps.txt`).
  - Note on batch 2's conditional ("REACHABLE INFERRED only if the merger treats trigger-class
    loading as part of mapper load"): even under that convention this row would not run, because
    class loading runs `<clinit>`, and this class has none — loading it executes nothing. The
    `<init>` still needs an instantiation site, and none exists in any printed corpus.
- Caveat: as with 2/38–2/39, reflective instantiation has zero supporting evidence.

## 12/1 — databinding.DataBinderMapperImpl.<init> ()V

- Proposed verdict: **REACHABLE, confirmed_by INFERRED** (generated code + framework dispatch).
- Identity resolution (this row is NOT `org.proninyaroslav.libretorrent.databinding.DataBinderMapperImpl`):
  - No `databinding/DataBinderMapperImpl.class` exists in the classes dir
    (`raw/ls_databinding_mapper.txt` is empty; `ls` of that path fails).
  - `auto_calls.json` names the row `databinding.DataBinderMapperImpl.<init>` with callees
    `MergedDataBinderMapper.<init>` + `DataBinderMapperImpl.addMapper` — which matches EXACTLY the
    javap of `androidx/databinding/DataBinderMapperImpl.class` (see below). The row is the
    generated merged mapper in the `androidx.databinding` package.
- Trigger chain (each step printed except the first, hence INFERRED, never SOURCE):
  1. App code calls `DataBindingUtil.inflate` / `setContentView` (sites listed under "Shared
     trigger base"; e.g. `AddTorrentActivity.java:102`).
  2. Databinding runtime loads the merged mapper — this reflection step is NOT printable from
     the extracted classes (runtime absent), but it is the step the already-accepted batch 17
     D8 verdict presupposes: batch 17 rows 34/35/38/39/40 (libretorrent mapper `<clinit>`,
     `<init>`, both `getDataBinder` overloads, `getLayoutId`) are REACHABLE INFERRED under
     M-dispatch, and those methods can only run if a mapper instance exists.
  3. `raw/javap_androidx_DataBinderMapperImpl.txt` (whole file, 13 lines) — the merged mapper's
     ctor calls `MergedDataBinderMapper.<init>`, then `new libretorrent.DataBinderMapperImpl` +
     `libretorrent.DataBinderMapperImpl.<init>`, then `addMapper(...)` with that instance.
  4. Entailment (independent of step 2's mechanism): `raw/binrefs_DataBinderMapperImpl.txt` shows
     only 4 class files in the whole tree name `DataBinderMapperImpl` — the androidx mapper, the
     libretorrent mapper, and its two inner classes. The androidx mapper's ctor is therefore the
     SOLE instantiation site of the libretorrent mapper in all APK bytecode. If libretorrent
     `<init>` (batch 17/35) is reachable, the constructor that constructs it (this row) must
     have run. It would be incoherent to hold 17/35 REACHABLE while holding this row unreachable.
  5. `raw/auto_calls_lookups.txt` — the same two edges appear as generated-source edges:
     `databinding.DataBinderMapperImpl.<init>` → `libretorrent.DataBinderMapperImpl.<clinit>` and
     → `libretorrent.DataBinderMapperImpl.<init>` (`DataBinderMapperImpl.java:5`, dispatch exact).
- This does NOT copy batch 17's conclusion to a different class by assumption: the two classes
  are linked by a printed `new` + `<init>` edge in the merged mapper's own bytecode.

## 17/36 — libretorrent.DataBinderMapperImpl.collectDependencies ()Ljava/util/List;

- Proposed verdict: **REACHABLE, confirmed_by INFERRED** (generated code + printed library dispatch).
- Trigger chain:
  1. App `DataBindingUtil` use (shared trigger base) → merged mapper construction (12/1 chain).
  2. `raw/javap_androidx_DataBinderMapperImpl.txt` — merged mapper ctor calls
     `addMapper(libretorrent mapper)`.
  3. `raw/web_MergedDataBinderMapper_excerpt.txt` — printed AOSP library source
     (`MergedDataBinderMapper.addMapper`, fetched from the androidx data-binding repo): the
     javadoc states "MergedDataBinderMapper will also call
     `DataBinderMapper#collectDependencies()` on the provided mapper", and the body does
     `final List<DataBinderMapper> dependencies = mapper.collectDependencies();` followed by
     recursive `addMapper(dependency)`.
  4. `raw/javap_DataBinderMapperImpl.txt:1062-1077` — libretorrent `collectDependencies` builds an
     `ArrayList(1)`, adds a `baseAdapters.DataBinderMapperImpl`, returns it. (Its framework_calls
     entry in `raw/auto_calls_lookups.txt` matches: `ArrayList.<init>`, `ArrayList.add`,
     `DataBinderMapperImpl.<init>`.)
  5. Therefore `collectDependencies` runs during mapper registration — i.e. inside the merged
     mapper's constructor, on the first databinding use — not on some separate runtime-API path.
- Explicit flag for the merger: this OVERRIDES the batch 17 D8 rationale for this row
  ("runtime-API method, not on the inflate path; M-dispatch-full rejected"). That rationale was
  written before any library `addMapper` print existed. The new print shows the method IS on the
  M-dispatch path itself (registration during construction), so no M-dispatch-full adoption is
  needed to flip it. If the merger instead holds D8's "not on the inflate path" premise as a
  decision rather than an evidence claim, this row reverts to OPEN — but on the evidence printed
  here, the premise is false.
- `auto_calls.json` callers of `collectDependencies`: count 0 — expected, since the caller is
  library code absent from the graph's app-code edges; the library print supplies that edge.

## 17/37 — libretorrent.DataBinderMapperImpl.convertBrIdToString (I)Ljava/lang/String;

- Proposed verdict: **UNREACHABLE, kind `no_trigger_in_app`, confirmed_by INFERRED** (generated code).
- Evidence:
  - `raw/javap_DataBinderMapperImpl.txt:1052-1061` — the method body reads
    `InnerBrLookup.sKeys` and returns the name (or null). No caller is shown in any app or
    generated bytecode.
  - `raw/binrefs_convertBrIdToString.txt` — only `DataBinderMapperImpl.class` itself contains the
    method name in the whole extracted tree. No generated `*BindingImpl` calls it.
  - `raw/auto_calls_lookups.txt` — callers of `convertBrIdToString`: count 0; its only outgoing
    edge is to `InnerBrLookup.<clinit>` (the static-field access).
  - App-source grep for `convertBrIdToString|collectDependencies`: 0 hits, including 0 hits for
    `DataBindingUtil.convertBrIdToString` (`raw/grep_mapper_api_appsource.txt` is empty).
  - Library side (from the same AOSP print, `raw/web_MergedDataBinderMapper_excerpt.txt`):
    `MergedDataBinderMapper.convertBrIdToString` DOES iterate mappers and call each mapper's
    `convertBrIdToString` — but that merged method is itself only entered via
    `DataBindingUtil.convertBrIdToString`, a documented logging utility ("Converts the given BR
    id to its string representation which might be useful for logging purposes"), which no app
    code calls (grep 0 above) and no generated code calls (binary grep above). Unlike
    `collectDependencies`, there is no construction-time or inflate-time caller.
- Asymmetry with 17/36, stated plainly: 36 has a printed library caller on an app-reached path
  (`addMapper` during merged-mapper construction); 37's only library caller sits behind a
  logging utility the app never invokes.
- Caveat: the databinding library runtime classes are absent from the extracted set, so a
  hypothetical runtime-internal call other than via `DataBindingUtil.convertBrIdToString` cannot
  be excluded from APK bytecode alone. The proposal rests on (a) zero references in all extracted
  bytecode, (b) zero app-source references, (c) the documented entry point never being called.

## 48/12 — AppDatabase_Impl.getAutoMigrations (Map) — NOT DECIDED, stays OPEN

- Proposed verdict: **NO PROPOSAL — cannot be decided on the evidence printed here. Stays OPEN.**
- What was verified (all in `raw/`):
  - `raw/AppDatabase_java.txt` — fresh print of `AppDatabase.java`: `@Database` lists entities
    + `version = 9` only, NO `autoMigrations` attribute, NO `@AutoMigration` / `AutoMigrationSpec`
    anywhere; `buildDatabase` (`:83-85`) uses `Room.databaseBuilder(...).addMigrations(...).build()`.
    Room version for the app is 2.6.1 (`app/build.gradle`: `ROOM_VERSION = '2.6.1'`,
    `room-runtime:$ROOM_VERSION` — noted from the clone tree during this pass).
  - App-source grep for `getAutoMigrations|getRequiredAutoMigrationSpecs|AutoMigration`: 0 hits
    (`raw/app_source_greps.txt`, section G3).
  - `raw/javap_AppDatabase_Impl.txt:223-231` — the method exists, body only builds an empty
    `ArrayList` and returns it. `raw/auto_calls_lookups.txt` — callers: count 0; framework_calls
    entry is only `ArrayList.<init>`.
  - `raw/javap_AppDatabase_Impl.txt:17-48` (`createOpenHelper`) — constructs `RoomOpenHelper`
    with `(configuration, delegate, identityHash, legacyHash)` and does NOT call
    `getAutoMigrations`; `raw/javap_AppDatabase_Impl_1.txt` (the `RoomOpenHelper.Delegate`) contains
    no `AutoMigration` reference at all.
  - The database IS built at runtime: `AppDatabase.getInstance` callers in app source include
    `core/RepositoryHelper.java:47,56,72` — so IF Room calls this method at build/open, the call
    would be app-reached. But that conditional is exactly what is unprinted.
  - Room runtime classes are absent from the extracted classes dir (`androidx/room/` does not
    exist there), so no Room bytecode call site can be shown from this tree; web search found
    only current-main Room source (where these methods are deprecated back-compat shims), which
    is NOT 2.6.1 evidence and was not used.
- Why neither label is proposed: the method returning an empty list is consistent with BOTH
  "Room calls it at build/open and gets an empty list" (the batch 48 conditional for REACHABLE
  INFERRED) AND "Room never calls it when no auto-migrations are declared" (the batch 48
  conditional for UNREACHABLE). Absence of a declaration does not decide between them, and
  inventing a Room 2.6.1 dispatch from memory would violate the printed-evidence standard.
- What is missing (exact): a printed Room 2.6.1 runtime call site — `RoomOpenHelper`,
  `RoomDatabase.Builder.build`, or `RoomDatabase.init` bytecode/source showing whether it invokes
  `getAutoMigrations` — or a device-replay/CI observation of the call. Until then, stays OPEN.

## 48/13 — AppDatabase_Impl.getRequiredAutoMigrationSpecs () — NOT DECIDED, stays OPEN

- Proposed verdict: **NO PROPOSAL — cannot be decided on the evidence printed here. Stays OPEN.**
- Evidence is the same as 48/12, mutatis mutandis:
  - `raw/javap_AppDatabase_Impl.txt:214-222` — the method exists, body only builds an empty
    `HashSet` and returns it. `raw/auto_calls_lookups.txt` — callers: count 0; framework_calls
    entry is only `HashSet.<init>`.
  - No auto-migration spec is declared on `AppDatabase` (fresh print above); app-source grep for
    the method name: 0 hits; the generated `createOpenHelper` and the Delegate do not reference it.
  - Same missing item as 48/12: a printed Room 2.6.1 runtime call site for
    `getRequiredAutoMigrationSpecs` at database build/open (e.g. a required-spec validation step),
    or a device-replay/CI observation. An empty-set return is consistent with both "called, gets
    empty" and "never called". Do not bundle 48/13 into any other row's flip.

## Raw-output file list (all under helper/A1-mapper-room/raw/)

`javap_DataBinderMapperImpl.txt`, `javap_InnerBrLookup.txt`, `javap_InnerLayoutIdLookup.txt`,
`javap_DataBindingTriggerClass.txt`, `javap_androidx_DataBinderMapperImpl.txt`,
`javap_AppDatabase_Impl.txt`, `javap_AppDatabase_Impl_1.txt`, `javap_AppDatabase.txt`,
`javap_BR.txt`, `javap_baseAdapters_mapper.txt` (error note only: that class is absent from the
extracted set), `auto_calls_lookups.txt`, `app_source_greps.txt`, `AppDatabase_java.txt`,
`grep_mapper_api_appsource.txt` (empty = 0 hits), `binrefs_*.txt` (7 files),
`find_*.txt`, `ls_*.txt`, `web_MergedDataBinderMapper_excerpt.txt` (transcribed AOSP library
print with provenance header).
