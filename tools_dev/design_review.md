# Design review: trigger-graph tooling v2 (`tools_dev/DESIGN.md`, review iteration 0)

Verdict: **CHANGES_REQUESTED**: 1 HIGH, 5 MEDIUM, 17 NIT.

I read all of DESIGN.md (sections 1-20) against the workflow brief (the design step's prompt in the workflow definition), `work/tools/{build_graph,list_methods,coverage_methods}.py`, `viewer_template.html`, `graphs/Currency/graph_def.py`, the Currency/Diary `out/` folders, the handoff notes and the `.design_scratch/` evidence. I also ran read-only probes on the dataset to check specific claims (listed under Verified assumptions). Per the step instructions I did not run any build or test suite.

The design is detailed and most of it holds up. The method universe and JaCoCo reconciliation (question 1), naming (2), bytecode parser scope (3), the parts layout (6) and the ownership split (7) are settled. The blocking problems are in RTA liveness (H1, M1), in the users of the resource-id map (M2), in manifest citations (M3), in the semantics of the override API across parallel parts (M4), and in the v1-compat regression oracle (M5).

Mapping to the seven review questions: (1) universe: M1 (data-binding liveness), N3, N4. (2) naming: no findings. (3) parser: N5. (4) RTA/lambdas: H1, M1, N6, N7, N8, N16. (5) inventory/res-id map: M2, M3, N9, N10, N11. (6) build_graph v2: H1, M4, M5, N12, N15, N17. (7) ownership/contracts: N1, N2, N13, N14.

## Findings

### 1. [HIGH] Liveness pruning computes a greatest fixpoint, so self-justifying instantiation cycles stay REACHABLE (section 11.6)

Problem: 11.6 starts with every auto edge enabled. It runs the BFS, computes live classes, drops untraversable edges and repeats "until nothing is dropped". That is the greatest fixpoint. Take a class C whose only creation site is in a method that can be reached only through an edge that requires C. That edge keeps C live, and the live C keeps the edge, so the cycle justifies itself. Example: `Node.split()` contains `new Node(...)`, and the only path to it is `n.split()` on a `Node`-typed receiver (a CHA edge requiring `Node`). The result is `Node.split` REACHABLE although no path ever creates a `Node`. Two classes that create each other inside dispatched methods behave the same way.

Standard RTA computes the least fixpoint. The design's own stated effect ("a method reachable only through dispatch on a class whose every creation site is itself unreachable is not reported REACHABLE") does not hold for these cycles. This is priority (1) of the design, no false REACHABLE introduced by tooling. Separately, the fixed cap of 50 rounds can trip on valid input (exit 3): rounds are bounded by the number of edges, not by 50.

Fix: replace the iteration in 11.6 with an upward (least-fixpoint) iteration. Keep everything else (same `bfs`, same `requires` format, pruned edges still listed in the report):

```python
live = {c for c, r in instantiated.items() if r['always_live']}
while True:
    ok = lambda x: (not x['requires'] or
                    any(all(set(hop) & live for hop in alt) for alt in x['requires']))
    E = manual_edges + [x for x in auto_copies if ok(x)]
    prev = bfs(adjacency(E), allow_setup=True, allow_env=True)
    reached = {base(n) for n in prev}
    grown = live | {c for c, r in instantiated.items() if reached & set(r['sites'])}
    if grown == live:
        break
    live = grown
# E is final: verdicts, paths, JSON and CSV use E; auto copies not in E are "pruned (receiver class never live)".
```

`live` grows every round, so the loop ends within `len(instantiated) + 1` rounds. Make that the internal-error bound instead of 50. Add unit tests: a class that instantiates only itself, and two classes that instantiate each other (both expected UNRESOLVED), plus one class created on a reachable path (expected REACHABLE).

### 2. [MEDIUM] Classes that libraries create never become live, so most data-binding and some generated code is pruned (sections 9.2, 6.4, 10.6 item 13)

Problem: under 9.2 and 11.6, a class with only `new` sources becomes live only when a universe method that contains one of its `new` sites is reached. Several classes are created only inside code that the library (not the app) calls:

- Data binding: `new XBindingImpl(...)` occurs only in `<app package>/DataBinderMapperImpl.getDataBinder`. I verified that in LibreTorrent `ActivityAddTorrentBindingImpl` is referenced only by `DataBinderMapperImpl.class` and itself. The library calls `getDataBinder`, and no auto edge reaches it. App code calls binding setters on the abstract base type: `binding.setViewModel(viewModel)` occurs 14 times in LibreTorrent, `setViewModel` is abstract in the `*Binding` classes and concrete in `*BindingImpl` (32 declarations). These CHA edges require `*BindingImpl` to be live, so liveness prunes them and the binding methods stay UNRESOLVED. 9.2 source 5 makes only `androidx/databinding/DataBinderMapperImpl` itself always-live, which does not reach the `new` sites. This undercuts 6.4's data-binding decision ("their creation goes through DataBinderMapperImpl (new sites, plus library reflection)") for LibreTorrent's 720 data-binding methods.
- Glide: the app's `AppGlideModule` subclass is created in `GeneratedAppGlideModuleImpl.<init>`, which Glide calls reflectively.
- ButterKnife: `*_ViewBinding` (Omni-Notes, MMEX) and `*$$ViewBinder` (openlauncher) are created reflectively by `ButterKnife.bind`.
- Framework: `framework_created` has no source for `<application android:backupAgent>`. That attribute is present in Aegis (`.AegisBackupAgent`) and MMEX (`.core.MoneyManagerBackupAgentHelper`).

Fix:
- 9.2: add source 6, `library-created:<creator class>`, which makes a class always-live. It covers every app class with a `new` site inside a method of a class whose simple name is `DataBinderMapperImpl` (any package) or `GeneratedAppGlideModuleImpl`.
- Extend source 5 to every class with `generated_kind = butterknife`.
- 10.6 item 13: add source `application-attr` for the `<application>` attributes `android:backupAgent` and `android:appComponentFactory`.
- Acceptance (A's tests): in LibreTorrent, no edge into a `*BindingImpl` method is pruned by liveness.

### 3. [MEDIUM] Case labels come only from int constants, so Aegis and AnyMemo get no menu guards (sections 8.3, 9.7, 10.3)

Problem: a label is created only when one operand of `if_icmpeq`/`if_icmpne` is `{('int', k)}`. Aegis and AnyMemo have non-final R fields, so they dispatch menus with if-chains on `getstatic` values whose operand Value is `('res', 'id', name)`. Evidence: `if (itemId == R.id.action_settings)` at Aegis `MainActivity.java:1088`; AnyMemo has 14 source files with `== R.id.` and none with `case R.id.`. In these two apps, which are exactly the ones 8.3's `res` token was added for, no call gets a `case R.id.<name>` guard or a `switch case R.id.<name>: ` trigger. v1's `gui_steps` therefore cannot name menu items, and modelers lose the guard text. Also unspecified: the label of the not-equal successor, the text of a `('default', pc)` label, the text for non-id resource types, and the text for framework ids.

Fix (8.3 and 9.7):
- An `if_icmpeq`/`if_icmpne` whose one operand is exactly `{('int', k)}` or `{('res', t, n)}` gives the equal successor the label `('case', k, pc)` or `('case-res', t, n, pc)`.
- The not-equal successor keeps the incoming label.
- Guard text is `case R.<t>.<n>` when `k` maps to `<t>/<n>` in `res_ids` or comes from a `res` token, `case android.R.<t>.<n>` for FW-MEMORY ids, `case <k>` otherwise, and `default` for the default successor.
- The trigger prefix `switch case R.id.<name>: ` applies to id labels from both sources.
- Add an Aegis acceptance test: `MainActivity.onOptionsItemSelected → MainActivity.startPreferencesActivity()` (overloaded, hence the parameter list) carries the guard `case R.id.action_settings` (`MainActivity.java:1088-1089`).

### 4. [MEDIUM] Manifest source citations fail for 6 of the 13 apps, Currency included (section 10.1)

Problem: 10.1 resolves relative component names "against the source manifest's package attribute". The source manifests of Aegis, AnyMemo, Currency, Diary, LibreTorrent and Markor have no `package` attribute (the namespace is in `build.gradle`; Aegis's `namespace packageName` is not even a string literal). Currency also uses names without a dot (`android:name="Main"`, lines 19-59), which Android treats as relative. As written, Currency's 9 app components would be cited "APK AndroidManifest.xml (merged; from a library or generated)", which is false. No planned test would catch it, because `test_axml` checks only the APK side.

Fix: resolution rule for a source `android:name` value N.
- N is relative if it starts with `.` or contains no `.`.
- Resolve a relative N with P = the manifest `package` attribute. Failing that, use the first `namespace` string literal (regex `namespace\s*=?\s*["']([\w.]+)["']`) in `<module_root>/build.gradle` or `build.gradle.kts`.
- Failing both, match by suffix: the APK component whose fully qualified name ends with `'.' + N.lstrip('.')`, if exactly one does.
- If no rule gives a unique match: `cite.src = null` plus a warning.
- An absolute N must equal the APK name.
- Add a test: all 10 Currency components (9 app components plus the harness receiver at line 69) have `cite.src` pointing at `src/main/AndroidManifest.xml:<line>`.

### 5. [MEDIUM] `suppress`/`override`/`confirm` match against an undefined edge set, producing false V6 errors across parallel parts (sections 11.4 step 4, 11.5 V6, 12.2, 12.5)

Problem: 11.4 applies, in order, AUTO_OPTIONS filtering (step 2), manual replacement (step 3) and then suppress/override/confirm (step 4), where "matching nothing is an error" (V6). Consequences:

- Part A writes a manual edge X→Y while part B suppresses or overrides the auto edge X→Y. B gets V6 although nothing is wrong. With 11 parallel part writers, edges on area boundaries make this likely.
- Setting `AUTO_OPTIONS['cha'] = False` (or `lambdas`, `register`, ...) turns every existing suppress/override of the affected edges into a V6 error.
- 12.2's `AUTO` ("before merging") does not say whether it is filtered, so the 12.5 loop can target edges that are later filtered or replaced.
- The 12.5 loop calls `override` without `match_kind`, so it rewrites every auto edge of that pair, not only the reactive one.

Fix:
- Matching set: the full calls.json edge list, unfiltered and before replacement, matched by (base src, base dst[, kind]). For an `@` src, the match is the variant copy after step 5.
- V6 fires only when no calls.json edge matches.
- A matched edge that AUTO_OPTIONS filtered or a manual pair replaced counts as "no effect". It is listed in `build_report.txt` under `no-effect suppress/override/confirm`, not raised as an error.
- `AUTO` in the part namespace is that same full list.
- The 12.5 example passes `match_kind=x['kind']`.

### 6. [MEDIUM] The v1-compatibility oracle compares against `out/` folders that may be stale (sections 11.2, 17, 18)

Problem: the regression compares a v1-mode build with `graphs/Currency/out/` and `graphs/Diary/out/`. A concurrent workflow is rebuilding Diary: at the time of this review its `graph_def.py` (17:09) is newer than its `out/` (17:08). Diary's `out/` is therefore not a fixed function of its current inputs. Including it in `test_build_graph_v1compat.py` makes the unit suite, which is an install gate, flaky, and a mismatch would be misread as a v2 regression. That the current v1 script reproduces Currency's `out/` is assumed, not checked.

Fix: make the v1 script itself the oracle.
- Snapshot `graph_def.py`, `method_list.json` and `coverage_baseline.json` (plus a dummy `auto/` folder for the "with auto/" case) into a temp graph dir.
- Build with the v1 script into temp folder A: `work/tools/build_graph.py` before install, `work/tools/_backup_v1/build_graph.py` after.
- Build with the v2 file in v1 mode into temp folder B.
- Gate: A and B are byte-identical in all four files.
- Also compare A with `graphs/Currency/out/`. It must match; a mismatch is reported as pre-existing staleness, not as a v2 failure.
- For Diary, only the A-vs-B comparison is a gate (integration and install verification only, not part of the unit suite); A-vs-`out/` is reported as "Diary out/ is stale" when it differs.

### 7. [NIT] Package scaffolding and the v1 file copies have no owner (section 4.1)

`tests/__init__.py` is not listed. Python 3.14's `unittest discover -s tests -t .` raises "Start directory is not importable" without it (checked in `unittest/loader.py`). `tglib/__init__.py` is owned by I, but A and B import `tglib` first. The byte-identical copies of `list_methods.py`, `coverage_methods.py` and `viewer_template.html` have owner "none".

Fix: A creates an empty `tglib/__init__.py` and `tests/__init__.py` as its first deliverable. I copies the three v1 files (and checks byte identity) before building v2.

### 8. [NIT] `jsonio.guard_path` is required but not in jsonio's API (sections 4.1, 13, 16)

16 says every v2 writer uses `guard_path`, but 4.1 lists jsonio as "JSON writer, atomic write, sha256 helper". The allowed root for build_graph's `--out`/`out/` and for the standalone CLIs is not given.

Fix: add `guard_path(path, allowed_root) -> str` (resolves symlinks, raises `ProtectedPathError`) and `sha256_file(path) -> str` to jsonio (owner A). Allowed roots:

- extract_app: `<graphs>/<App>/auto/`.
- Standalone CLIs: the directory of `--out`, which must end in `/auto`.
- build_graph: the resolved `--out` dir or `<gdir>/out`.

### 9. [NIT] Membership of the `excluded` list is ambiguous (sections 6.2, 6.5)

X5-X7 say "excluded, listed", X8-X10 only "excluded", X1 "counted only".

Fix: in 6.5, state that `excluded` lists every method with code that is not in the universe under rules X2-X10. X1 is counted only. X4 has no code and is not listed (natives go to the inventory).

### 10. [NIT] Small corrections to the `generated_kind` table (section 6.4)

The `build-config` row refers to `--keep-buildconfig`, which no CLI defines. Aegis's top-level `GoogleAuthProtos` matches no rule.

Fix: delete the `build-config` row and the flag. Change the protobuf rule to "simple top-level name ends with `Protos`, or nested in such a class, or transitive super `GeneratedMessageLite`/`GeneratedMessageV3`".

### 11. [NIT] Interpreter contract details B depends on (sections 8.3, 8.4)

- Specify that in `('param', i)`, `i` is the 0-based parameter ordinal excluding the receiver, not the local slot (long/double count as one), so it lines up with `InvokeSite.args[i]`.
- A local that is missing in one predecessor joins to `{('unknown',)}`.
- A Code attribute may carry several LineNumberTable attributes; merge them.

### 12. [NIT] Consumer lookup key and event precedence (section 9.4)

- Specify which owner `consumers.classify` receives: the `('ext', type)` from `hierarchy.resolve`, falling back to the Methodref owner. Otherwise an app subclass of `AlertDialog$Builder` falls to `unknown`.
- Event 5 (`java/util/*` add/put/...) is tested before the table. Otherwise `List.add` hits the `unknown` row with review `unknown-consumer` instead of `collection`.
- The `*` async row cannot check "(View and Activity subclasses)", because framework hierarchies are unknown. Drop the parenthetical and state "any owner".
- The anonymous-class exception ("no event 1 or 2") should be evaluated on the terminal events after following event-2 hops.

### 13. [NIT] `select` must apply JVMS 5.4.5 can-override (section 9.1)

Skip private declarations, and package-private declarations in a different runtime package, when walking the superclass chain. Give the app-case return shape (`('app', class, method)`, as `resolve` does).

### 14. [NIT] Switch-map `<clinit>` is listed as a collapse target that no raw edge can reach (sections 9.5, 9.6)

9.5 lists "switch-map `<clinit>`" as an excluded target, but 9.6 creates clinit edges only into universe `<clinit>` methods, so no raw edge ever enters `Foo$1.<clinit>`.

Fix: either drop it from the 9.5 list, or let 9.6 create raw clinit edges into excluded `<clinit>` methods as well (they are then collapsed).

### 15. [NIT] Resource-source lookup is underspecified (sections 5, 10.1)

"Every module root of the checkout", the "source set" of a listed source dir, and the rank of listed `test` dirs are undefined. The variant ordering also ranks the build type above a full-variant source set.

Fix:
- Module roots are directories under `checkout_root` (no `build` or dot components) that contain `src/main/AndroidManifest.xml`. Order: class-dir module roots in `class_files.json` order, then the rest sorted by path.
- The source set of a listed dir is the path component after its last `/src/`.
- Priority: full variant, then build type, then flavors (longest first), then `main`.
- Listed `test*`/`androidTest*` dirs are never candidates.

### 16. [NIT] Unknown arsc chunk types and compact entries are unspecified (section 10.2)

Say what happens with package-level chunk types other than 0x0201/0x0202 (0x0203 library, 0x0204/0x0205 overlayable, 0x0206 staged alias): skip them by size. Decode `FLAG_COMPACT` (0x0008) entries, whose key index is the first u16, rather than raising `AxmlError`.

### 17. [NIT] ButterKnife view ids are missed (section 10.5)

`target.fab = Utils.findRequiredViewAsType(source, R.id.fab, ...)` runs in `K_ViewBinding.<init>`, not in K, so "assigned ... in any method of K" never fires (Omni-Notes, MMEX).

Fix: match puts of `('field', K, f)` in any analysed method of any class.

### 18. [NIT] Error semantics of the graph API conflict (sections 11.4, 11.5, 12.3)

`suppress(src, dst, reason, kind=None)` makes a missing reason a `TypeError`, which 12.3 handles as exit 2 with nothing written. V6 says a missing reason is a reported error (exit 1). V7 does not say whether the invalid edge is kept.

Fix: use the signature `suppress(src, dst, reason=None, kind=None)`, so the brief's `suppress(src, dst)` call reaches V6. A missing or empty reason is V6. An `e()` call that fails V7 records the error and drops the edge.

### 19. [NIT] Exit code 1 for `extract_app --all` conflicts with section 4.3 (section 13)

13 has `--all` exit 1 when any app fails, but 4.3 reserves 1 for build_graph.

Fix: in 4.3, also allow 1 for `extract_app --all` ("completed, at least one app failed").

### 20. [NIT] Unclear who appends the HANDOFF section (section 18 step 4)

18 step 4 does not say whether the integration step or the install step appends the "Tooling v2" section to HANDOFF.md, so it could be appended twice.

Fix: the integration step appends it. The install step only checks that it exists.

### 21. [NIT] Several calls.json record shapes are undefined (section 9.7)

4.2 rule 5 says each schema fixes key order and list sort keys, but 9.7 gives no shape or sort key for `ext_dispatch`, `unresolved_sites`, `unresolved_callbacks`, `failures` or `stats`, nor the key order of `instantiated`.

Fix, for example:
- `ext_dispatch`: `[{src, line, pc, owner, name, desc, overriders}]` sorted by (src, pc).
- `unresolved_sites`: `[{src, line, pc, owner, name, desc, reason}]` sorted by (src, pc).
- `unresolved_callbacks`: `[{src, line, pc, consumer, param_type, class, reason}]` sorted by (src, pc).
- `failures`: `[{method: [class, name, desc], message}]` sorted by method.
- `instantiated`: keys sorted.

### 22. [NIT] Odd part-file names and subdirectories are silently ignored (section 12.1)

A `*.py` in `parts/` that does not match the name regex (and does not start with `_` or `.`), or a subdirectory, is silently ignored today. A part written by a parallel agent could vanish without notice.

Fix: make either case an error (exit 2).

### 23. [NIT] `SRC` evidence on generated code that has no source (section 9.7)

Data-binding, Hilt and Room classes have no source in the checkout, but their edges would carry `SRC <File>:<line>`, which claims source evidence.

Fix: for classes with `generated = true` and no `source_path`, use `INFERRED bytecode <File>:<line> (generated, no source in checkout)`.

## Verified assumptions

- Currency and Diary universes. `graphs/Currency/method_list.json` equals the JaCoCo union without harness and BuildConfig (143) plus the two K1 constructors `Data.<init>` and `Singleton.<init>`. Diary's equals 285 plus `FileUtils.<init>`. Same triples; neither app has a simple-name clash, so the v2 names equal v1's.
- Harness classes. Every app's report has exactly 3 harness classes under `<pkg>/JacocoInstrument/`, so the X1 path-segment rule matches them.
- `class_files.json` shape (all 13 apps): one key, the APK file name, and that APK exists under `app/`. Two class dirs for AmazeFileManager and AnkiDroid. Aegis's class dir is `classes/debug/transformDebugClassesWithAsm/dirs/`. Variant components and `src/` source sets are compatible with the `variant_source_sets` rule.
- Build outputs. No `R.class`/`R$*.class`, `R.txt`, `R.jar` or manifest under any `build/`, and no `res/navigation*` dir in the sources (checked with find).
- Resource ids are consistent. Distinct `0x7f` Integer pool constants resolve in the APK's `resources.arsc` at 99.3-100% (Currency, Diary, Markor, LibreTorrent, AmazeFileManager, Vanilla-Music; probe built on the scratch `apkres.arsc_names`).
- APK manifest. Currency's has exactly 10 components, all with fully qualified names (decoded).
- JaCoCo XML. The DOCTYPE references `report.dtd`, keys come from `class@name`/`method@name`/`method@desc`, and hits from the METHOD counter. Classes with zero methods are listed: hash-checker's `DaggerAppComponent` carries `Ldagger/internal/DaggerGenerated;` and has 0 reported methods, while `DaggerAppComponent$Builder` has no annotation and 5 reported methods. This confirms that X6 is per class and does not propagate.
- Markor's third-party sources exist under `app/thirdparty/java/other/...`, so `find_source` rank 2 applies and they are not generated.
- Currency precedents in `graph_def.py`: the edges cited in 9.4, 9.6, 9.7 and 11.5 exist (lines 67-89, 180-186, 254-267, 486) and `Singleton.getList` is DEAD for the stated reason. In `Main.java:1043-1103`, the dialog lambda passes through the private `updateDialog` into `AlertDialog.Builder.setPositiveButton`/`setNegativeButton`.
- v1 code. `build_graph.py`'s helpers, 10 CSV columns, evidence labels, report wording and the template path next to the script match the design's description. `list_methods.py` sorts by `(class, name, desc)` and writes flags `static`, `synthetic`.
- Viewer. It splits on `@`, groups by `m.split('.')[0]`, and its BFS skips REGISTER edges, self-loops and `needs_state`, with no env check. That equals v1 `bfs(..., allow_env=True)`.
- No name collisions: no existing `graph_def.py` defines `USE_AUTO`, `AUTO`, `AUTO_OPTIONS`, `METHODS`, `INFO`, `INVENTORY`, `PART`, `OWNS`, `suppress`, `override` or `confirm`.
- Section 3 numbers. The scratch outputs (`facts_out.txt`, `more_out.txt`, `cha_out.txt`, `flow_out.txt`) contain them: majors {51, 52, 55, 61}, per-rule counts consistent with the universe table (`facts.py` counts overlapping rules, so Aegis's 40 K1-shaped constructors against 39 kept is consistent with first-match-wins if one sits in an X5/X6 class; I did not identify which one), accessor and bridge shapes, the 3/36/4 generated-only callers, opcode presence, metafactory as the only bootstrap, and no indy in openlauncher, Vanilla-Music, AnyMemo and AnkiDroid.
- Opcode table. The 8.2 length table covers 0x00-0xff completely and correctly, including switch padding and `wide`. JaCoCo filter semantics (Enum, EnumEmptyConstructor, PrivateEmptyNoArgConstructor, Synthetic/Bridge, AnnotationGenerated, synthetic classes skipped) correspond to X5-X10 and K1. I checked both against my knowledge of JVMS and JaCoCo, not against JaCoCo's source.
- Python is 3.14.5.

## Unverified or wrong assumptions

- Wrong: relative manifest names resolve "against the source manifest's package attribute" (10.1). Six of 13 source manifests have no `package` attribute, and Currency uses dot-less relative names (finding 4).
- Wrong: the liveness effect in 11.6 does not hold for self-justifying cycles (finding 1).
- Wrong or incomplete: data-binding creation "goes through DataBinderMapperImpl (new sites, plus library reflection)" (6.4). The `new` sites sit in a method only the library calls, so 11.6 never makes `*BindingImpl` live (finding 2).
- Incomplete: framework creation (9.2 source 3, 10.6 item 13) omits `<application android:backupAgent>`, which Aegis and MMEX use (finding 2).
- Incomplete: switch-case guards from the res-id map (10.3, 8.3) assume int constants. Aegis and AnyMemo compare `getstatic R$id` values in if-chains (finding 3).
- Unverified: that the current v1 `build_graph.py` reproduces `graphs/Currency/out/` byte for byte. I did not run it (no builds); the report wording matches the current script. Diary's `out/` is being rewritten by a concurrent workflow (finding 6).
- Unverified (I checked only Currency and Diary): the per-app universe, generated-method and names-changed numbers in sections 3, 6.4 and 7.1 for the other 11 apps. They rest on the scratch prototypes, which are deleted after integration. `verify_analyzer.txt` must reproduce them, as the design already requires.
- Unverified: the 9.5 acceptance that all 36 AnyMemo generated-only methods get an incoming edge. It is plausible from the design's rules (a)-(c), but only A's tests can confirm it.
- Missing: `tests/__init__.py`. The documented discovery command requires it (finding 7).
