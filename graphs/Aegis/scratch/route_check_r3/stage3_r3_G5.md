# Stage 3 route check R3-G5 (Aegis schema 2, round 3, read-only)

Date: 2026-10-27. Sources: graph_def.py hand edges and ST_/ENV_ constants; tools/show_route.py output (--dedupe); app source under final_java_only/Aegis/app/Aegis-#v3.4.2/app/src/main/java/com/beemdevelopment/aegis and AndroidManifest.xml; framework fw_src/android-8.1.0_r1 (only ActivityThread.java:5740 was printed). Generated Dagger and Hilt code is not on disk and was marked UNCLEAR. Conservative reading applied where unsure (noted per step).

| Route | Target | Steps | ERROR steps | UNCLEAR steps | OK |
|---|---|---|---|---|---|
| 1 | JsonUtils.optString | 12 | 6, 11 | 2, 3, 5, 9 | 6 |
| 2 | EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1 | 15 | 12 | 2, 3, 7, 8, 14, 15 | 8 |
| 3 | UUIDMap$Value.<init>(UUID) | 16 | 8, 13, 14 | 2, 3, 9 | 10 |
| 4 | Hilt_AegisApplication.<init> | 2 | none | none | 2 |
| 5 | AegisApplication.<init> | 1 | none | none | 1 |
| Total | 5 routes | 46 | 6 | 13 | 27 |

## Route 1: JsonUtils.optString

Steps 1-12. ERROR: 6, 11. UNCLEAR: 2, 3, 5, 9. OK: 1, 4, 7, 8, 10, 12 (6 steps).
Route-level note: the route states state=- but step 9 needs an icon pack already on disk (see step 9).

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Printed: FW ActivityThread.java:5740 `mInstrumentation.callApplicationOnCreate(app);` (framework call holds). Hilt superclass override is generated code, not on disk. Source AegisApplication.java:6 extends AegisApplicationBase and has no onCreate, as the edge says. Fix: none needed.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated body not on disk. Printed AegisApplicationBase.java:45-47 (onCreate, super.onCreate() at 46).

Step 5 (Ebdc15ea3, DaggerAegisApplication..SingletonCImpl.getVaultManager -> SwitchingProvider.get): UNCLEAR. Generated Dagger code, not on disk. The edge text itself says the provider builds the VaultManager.

Step 6 (E29463d22, SwitchingProvider.get -> AegisModule.provideIconPackManager): ERROR. Printed AegisModule.java:26-27 (provideIconPackManager returns new IconPackManager(context)) and AegisModule.java:37-40 (provideVaultManager takes context and auditLogRepository and returns new VaultManager; no IconPackManager). Step 5 says this chain builds the VaultManager, so the link to the IconPackManager provider is not on the getVaultManager path. The edge has no guard; a switch case in the generated SwitchingProvider.get (not on disk) would have to select the IconPackManager binding, and the edge does not carry it. Conservative reading: the ERROR rests on the module source and on step 5's text. Fix proposed: remove E29463d22 from this getVaultManager route. IconPackManager is injected by the activity: AegisActivity.java:55-56 (@Inject protected IconPackManager _iconPackManager), in the Hilt injection that runs inside super.onCreate (AegisActivity.java:67, per the existing hand edge for AegisActivity.onCreate). The cold-start chain to IconPackManager should start there in a separate route.

Step 9 (E49405253, IconPackManager.rescanIconPacks -> IconPack.fromBytes): UNCLEAR (needs earlier run). Printed IconPackManager.java:135-158: listFiles null return (136-138); for loop (140); isDirectory skip (141-143); UUID parse skip (146-151); versionDir non-null (153-154); pack.json open inside try (156); fromBytes (158). The guard text matches these lines. But the icons dir is filesDir/icons (IconPackManager.java:32) and nothing creates it at startup; on a fresh install listFiles is null and the method returns at line 137. The needed pack comes from an earlier run: IconPackManager.importPack creates the pack dir (IconPackManager.java:91 mkdirs) and writes pack.json (IconPackManager.java:119). The edge has no needs_state. The text is not wrong, so per the convention this is UNCLEAR, not ERROR. Fix proposed: needs_state=ST_ICON_PACK_INSTALLED on this edge (constant already defined and used at graph_def.py:1165); the route state should not read "-".

Step 11 (Ee733309d, IconPack.fromJson -> IconPack$Icon.fromJson): ERROR. Printed IconPack.java:117 (getJSONArray("icons")), 120 `for (int i = 0; i < array.length(); i++) {`, 121 `Icon icon = Icon.fromJson(array.getJSONObject(i));`. The enclosing for loop is not listed as a guard. The call runs only for each entry of the icons array, so the route needs at least one icon in the pack. Fix proposed: add guard 'the icons array has at least one entry: the for loop runs (IconPack.java:120)'.

Steps 1, 4, 7, 8, 10, 12: OK (edge, class, guard and cited lines hold; step 1 AndroidManifest.xml:22 android:name=".AegisApplication"; step 4 AegisApplicationBase.java:47 and EntryPoint at :116-120; step 7 AegisModule.java:27; step 8 IconPackManager.java:33 unconditional in constructor; step 10 IconPack.java:130 unconditional; step 12 IconPack.java:198 with no enclosing if or for, and JsonUtils.java:13 optString exists).

## Route 2: EntryAdapter.lambda$doesAnyGroupMatchSearchFilter$1

Steps 1-15. ERROR: 12. UNCLEAR: 2, 3, 7, 8, 14, 15. OK: 1, 4, 5, 6, 9, 10, 11, 13 (8 steps).
Route-level note: the route states state=- and env=-, but the chain needs: a search submitted earlier and restored (step 8), SEARCH_IN_GROUPS enabled (step 14), at least one vault group (step 15), and a non-empty entry list (step 12). On a fresh install MainActivity.onStart returns to the intro before the list loads (MainActivity.java:942-947), and this route does not pass through that gate.
Lambda naming (checked from the built class, not javap, which is not installed): the compiled EntryAdapter.class LineNumberTable (transformDebugClassesWithAsm) gives lambda$doesAnyGroupMatchSearchFilter$1 = line 227 (group filter, (Set,VaultGroup)), lambda$doesAnyGroupMatchSearchFilter$2 = line 229 (anyMatch predicate, (String,String)), lambda$isEntryFiltered$0 = lines 206-209.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Same as route 1 step 2 (FW ActivityThread.java:5740 holds; Hilt superclass is generated).

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated body not on disk.

Step 7 (E8e6d6f10, MainActivity.onCreate -> MainActivity.onCreateOptionsMenu): UNCLEAR. The timing of the menu callback is androidx behaviour (source not on disk). Printed MainActivity.java:193-196 (super.onCreate at 194, setSupportActionBar at 196) and 1011-1016 (onCreateOptionsMenu). Nothing in the app source decides when the menu is created.

Step 8 (Ed60e6cbd, MainActivity.onCreateOptionsMenu -> EntryListView.setSearchFilter): UNCLEAR (needs earlier run). Printed MainActivity.java:1011-1080. No return or enclosing if lies between 1011 and 1065, and the call at 1073 sits in the else-if at 1070, so the guard text (1066-1073) is correct. But _submittedSearchQuery is set only by onQueryTextSubmit (MainActivity.java:1040) or restored from saved state (MainActivity.java:202-205, when savedInstanceState is not null). A cold start has savedInstanceState null, so the branch cannot run. The edge has no needs_state. Fix proposed: needs_state = 'a search was submitted in an earlier MainActivity instance (MainActivity.java:1040) and this instance was recreated with the saved state (MainActivity.java:205)'. No existing ST_ constant covers this.

Step 12 (E11bbf486, EntryAdapter.calculateShownEntries -> EntryAdapter.isEntryFiltered): ERROR. Printed EntryAdapter.java:299-305: the call at 302 (if (!isEntryFiltered(entry))) sits inside for (VaultEntry entry : entries) at 301. The edge lists no guard, so the loop condition (at least one entry) is missing. Fix proposed: add guard 'the entries list has at least one entry: the for loop runs (EntryAdapter.java:301)'; needs_state ST_VAULT_ENTRIES (existing, graph_def.py:62), which is a cross-run state and so also needs an earlier run.

Step 14 (E399cebc2, lambda$isEntryFiltered$0 -> EntryAdapter.doesAnyGroupMatchSearchFilter): UNCLEAR (needs earlier run). Printed EntryAdapter.java:206-209: the guard text matches the || chain (the group call runs only if SEARCH_IN_GROUPS is set and the first three tests are false). But the default mask is SEARCH_IN_ISSUER | SEARCH_IN_NAME (Preferences.java:198), so SEARCH_IN_GROUPS is off on a fresh install and the call never runs. The bit is saved by Preferences.setSearchBehaviorMask (Preferences.java:208) after an earlier settings change. The edge has no needs_state. Fix proposed: needs_state = 'the search mask has SEARCH_IN_GROUPS saved by an earlier settings change (Preferences.java:208; default at Preferences.java:198 excludes it)'.

Step 15 (E4bf8b9e0, doesAnyGroupMatchSearchFilter -> lambda$doesAnyGroupMatchSearchFilter$1): UNCLEAR (needs earlier run). Printed EntryAdapter.java:226-229. The class file maps $1 to line 227 (the group filter), which matches the edge's description ("keeps the groups that the entry belongs to"). The evidence cites line 229, which is the anyMatch predicate $2 (graph_def.py:2563); that is the same pipeline, so the target is right but the evidence focus is off. The $1 lambda runs once per VaultGroup in _groups (EntryAdapter.java:226). _groups is null until setGroups (EntryAdapter.java:57, 339), and with no vault group it never runs. The needed group comes from an earlier run and no needs_state is set. Fix proposed: needs_state = 'the vault holds at least one group (the loop over _groups at EntryAdapter.java:226-227 runs)'; no existing ST_ constant covers groups. Evidence: cite line 227 for $1.

Steps 1, 4, 5, 6, 9, 10, 11, 13: OK. Step 1 AndroidManifest.xml:22; step 4 AegisApplicationBase.java:45-67 (ENTERS, no guard); step 5 AndroidManifest.xml:43-51 (MainActivity MAIN/LAUNCHER); step 6 ActivityThread.java:2729-2731, 2741 and MainActivity.java:193-194; step 9 EntryListView.java:280 (unconditional in setSearchFilter, 279-284); step 10 EntryAdapter.java:271-273 (if encloses the call); step 11 EntryAdapter.java:280 (unconditional in refreshEntryList, 277-283); step 13 guard _searchFilter != null at EntryAdapter.java:200 encloses the allMatch at 205 (JDK allMatch behaviour, no JDK source on disk; standard, not read).

## Route 3: UUIDMap$Value.<init>(UUID)

Steps 1-16. ERROR: 8, 13, 14. UNCLEAR: 2, 3, 9. OK: 1, 4, 5, 6, 7, 10, 11, 12, 15, 16 (10 steps).
Route-level note: the route states state=- and env=-, but steps 8-16 need a vault file on disk (ST_VAULT_FILE, graph_def.py:51) and an unloaded vault (ST_UNLOCKED is false at a cold start, graph_def.py:70). show_route printed one descriptive line per step and no separate guard or needs_state field, so the guard text was read from that line.

Step 2 (E5b266140, AegisApplication.<init> -> Hilt_AegisApplication.onCreate): UNCLEAR. Same verdict as route 1 step 2 and route 2 step 2: the Hilt superclass is generated; FW ActivityThread.java:5740 holds.

Step 3 (E1ef992ce, Hilt_AegisApplication.onCreate -> AegisApplicationBase.onCreate): UNCLEAR. Generated Hilt body, not on disk (show_route evidence is INFERRED).

Step 8 (Ea3a957ec, MainActivity.onStart -> VaultRepository.readVaultFile): ERROR. Printed MainActivity.java:938-975: the call at 954 (vaultFile = VaultRepository.readVaultFile(this);) sits inside `if (!_vaultManager.isVaultLoaded()) {` at 951, with try at 953. The edge text is only "Direct call", so the enclosing if is missing. The early return at 942-948 (isVaultInitNeeded) must also be passed, and that gate is not listed. Fix: guard 'the vault is not loaded yet in this process and the intro is not needed (MainActivity.java:942-951)'; needs_state ST_VAULT_FILE (graph_def.py:51).

Step 9 (Eb6841a0c, VaultRepository.readVaultFile -> VaultFile.fromBytes): UNCLEAR (needs earlier run). Printed VaultRepository.java:65-71: `return VaultFile.fromBytes(fileBytes);` at 70, inside try (68) after file.readFully(). There is no enclosing if or for. The call needs the vault file to exist, a cross-run state (ST_VAULT_FILE). The edge has no needs_state. Fix: needs_state=ST_VAULT_FILE.

Step 10 (E3e94653f, VaultFile.fromBytes -> VaultFile.fromJson): OK. Printed VaultFile.java:79-82: the call at 82 is inside try (80) with no enclosing if or for; it inherits the ST_VAULT_FILE gate from step 9.

Step 11 (E50406d09, VaultFile.fromJson -> VaultFile$Header.fromJson): OK. Printed VaultFile.java:62-68: the version check at 64-66 is a throw and does not enclose the call at 68, which is inside try (63).

Step 12 (Ed2faa897, VaultFile$Header.fromJson -> SlotList.fromJson): OK. Printed VaultFile.java:144-150: the early return at 145-147 (both slots and params null) is not an enclosing guard; the call at 150 is inside try (149). The edge does not mention the early return.

Step 13 (E82b2faaf, SlotList.fromJson -> Slot.fromJson): ERROR. Printed SlotList.java:23-29: `Slot slot = Slot.fromJson(obj);` at 29 is inside `for (int i = 0; i < array.length(); i++) {` at 27. The edge has no for-loop guard. Fix: guard 'the slots array has at least one entry: the for loop at SlotList.java:27 runs'.

Step 14 (Ea4e52413, Slot.fromJson -> RawSlot.<init>(UUID,byte[],CryptParameters)): ERROR. Printed Slot.java:118-133: `slot = new RawSlot(uuid, key, keyParams);` at 133 is inside `switch (obj.getInt("type")) {` (131) with `case Slot.TYPE_RAW:` at 132. The edge has no switch-case guard, the same pattern as route 1 step 6. Fix: guard 'the slot type is TYPE_RAW (switch case at Slot.java:132)'.

Step 15 (E45ae012f, RawSlot.<init> -> Slot.<init>(UUID,byte[],CryptParameters)): OK. Printed RawSlot.java:12-13: protected RawSlot(UUID,byte[],CryptParameters) calls super(uuid, key, keyParams) unconditionally. Slot.java:40 defines the matching protected constructor.

Step 16 (E7af35710, Slot.<init> -> UUIDMap$Value.<init>(UUID)): OK. Printed Slot.java:40-41 (super(uuid) at 41) and grep of UUIDMap.java: `protected Value(UUID uuid)` at line 141, the target.

Steps 1, 4, 5, 6, 7: OK. Step 1 AndroidManifest.xml:22 android:name=".AegisApplication"; step 4 AegisApplicationBase.java:45-67 (full onCreate printed, ENTERS, no enclosing guard); step 5 AndroidManifest.xml:44-51 (MAIN/LAUNCHER filter); step 6 ActivityThread.java:2729-2731, 2741 and MainActivity.java:192-194; step 7 ActivityThread.java:2741 (performStart) and MainActivity.java:938-940 (onStart, unconditional after performStart).

## Route 4: Hilt_AegisApplication.<init>

Steps 1-2. ERROR: 0. UNCLEAR: 0. OK: 1, 2 (2 steps).
Route-level note: the route states state=- and env=-; neither step needs a state. The route is a constructor-only chain with no guards.

Step 1 (E14b4e906, S_ENTRY -> AegisApplication.<init>): OK. Printed AndroidManifest.xml:21-27: android:name=".AegisApplication" at line 22 (same as route 3 step 1).

Step 2 (Ecaf88dff, AegisApplication.<init> -> Hilt_AegisApplication.<init>): OK. The evidence the show_route printed is SRC AegisApplication.java:6, which reads `public class AegisApplication extends AegisApplicationBase {`. That line alone does not show Hilt_AegisApplication, so the cited evidence is weak. The superclass rewrite is done by the Hilt build step, so the check used the compiled class: build/intermediates/classes/debug/jacocoDebug/dirs/com/beemdevelopment/aegis/AegisApplication.class, read as a constant pool (read-only, stdout only), gives this = com/beemdevelopment/aegis/AegisApplication, super = com/beemdevelopment/aegis/Hilt_AegisApplication. The implicit super() call is therefore to Hilt_AegisApplication.<init>. Suggested evidence fix: cite the compiled class, not AegisApplication.java:6. The Hilt_AegisApplication body itself stays generated (UNCLEAR for any edge that goes into it, such as route 1 step 2).

## Route 5: AegisApplication.<init>

Step 1. ERROR: 0. UNCLEAR: 0. OK: 1 (1 step).
Route-level note: state=- and env=-; no state is needed.

Step 1 (E14b4e906, S_ENTRY -> AegisApplication.<init>): OK. Printed AndroidManifest.xml:21-27: android:name=".AegisApplication" at line 22 (the same edge as route 3 step 1 and route 4 step 1). The edge's description also says a backup or restore start uses the base Application class instead. That is a framework claim I did not check (no ActivityThread backup source was printed), so it is not part of this verdict.
