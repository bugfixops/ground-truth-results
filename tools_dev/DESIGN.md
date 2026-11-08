# Trigger-graph tooling v2: design

Status: revision 1, answering `design_review.json` (review iteration 0: 1 HIGH, 5 MEDIUM, 17 NIT; every finding is
answered in section 20). The first version was written in the design-review loop because the preceding design step produced no
DESIGN.md (its session ended at the output-token limit while still reasoning); its measurement scripts and outputs in
`tools_dev/.design_scratch/` (cf.py, gap.py, facts.py, naming.py, flow.py, probe_res.py, apkres.py, plus cha_stats.py and
probe_more.py added in iteration 0) are the evidence base cited below as `[scratch:<file>]`; facts checked in revision 1
are marked `revision-1` (read-only greps and class-dir scans, plus one v1 build in a temp folder that was deleted). The scratch folder is development-only
evidence: it is never installed, and the integration step deletes it once `verify_analyzer.txt` reproduces the
section 3 numbers.

## 1. Overview

v2 turns the mechanical half of the per-app trigger-graph work into tools, so that modelers (human or agent) only write
the edges that need understanding (pages, gestures, framework semantics, guards). Three extractors read one dataset app
read-only and write `graphs/<App>/auto/`: `universe.json` (the method set, reconciled with the JaCoCo reports, with
deterministic node names), `inventory.json` + `INVENTORY.md` (manifest, resources, resource-id map, registration and
component-start sites, framework base types; facts with citations, no pages) and `calls.json` (the app-internal call
graph: exact and RTA-filtered CHA dispatch, lambda and callback-object hand-offs, accessor/bridge/generated-code
collapsing, class-initialisation edges). `build_graph.py` v2 keeps the v1 code path byte-for-byte for every graph
directory that does not opt in, and adds an opt-in mode (`USE_AUTO = True`) that merges the auto edges under the manual
ones (manual wins), splits definitions across `parts/` files owned by parallel agents, and turns the baseline
contradictions into errors. Everything is pure Python 3.14 standard library; there is no JDK, no network, no pip.

Design priorities, in order: (1) no false REACHABLE and no false DEAD verdict introduced by tooling; (2) v1 behaviour
unchanged unless opted in; (3) deterministic output (same inputs, same bytes); (4) enough automation that the 4,000+
method apps are feasible; (5) speed.

## 2. Constraints and locked technology stack

- Runtime: CPython 3.14 (`python3`), always invoked as `python3 -I`. Standard library only: `struct`, `zipfile`,
  `xml.etree.ElementTree` (JaCoCo reports), `xml.parsers.expat` (source XML with line numbers), `json`, `csv`, `ast`,
  `re`, `os`, `sys`, `io`, `copy`, `argparse`, `hashlib`, `collections`, `dataclasses`, `functools`, `itertools`,
  `types`, `time`, `tempfile`, `shutil`, `filecmp`, `unittest`, `traceback`, `contextlib`, `random` (tests only, fixed
  seeds). No third-party code, no subprocess calls to external programs (no `javap`, `aapt`, `java`). `subprocess` is
  used only by tests and by the install verification, and only as `subprocess.run([sys.executable, '-I', '-B',
  <script>, ...], cwd=<temp dir>, capture_output=True, text=True, timeout=600)`: an argument list, never a shell,
  never another program.
- Unit tests run as `python3 -I -B -m unittest discover -s tests -t .` (`-B`: no `__pycache__` is written, so
  running the suite from `work/tools/` after install leaves no files behind). Tests that need v1 functions read the v1
  script's source and `exec` it into a fresh dict with `__name__ = 'v1_build_graph'` (17.1); they never import it.
- `-I` removes the script directory from `sys.path`. Every CLI script inserts the directory that contains the `tglib`
  package as `sys.path[0]` before importing it (see 4.3).
- The workspace is not a git repository: no commits, no worktrees.
- Read-only: `work/final_java_only/`, `/Users/darshan/Desktop/yang/final_java_only/` (ignored duplicate, never read),
  `/Users/darshan/Desktop/yang/share/`, `work/share_example/`, the PDFs and prompt `.md` files.
- Never written: `graphs/Currency/{graph_def.py,method_list.json,coverage_baseline.json,out/}`; in `graphs/Diary/`
  everything except `graphs/Diary/auto/`; `work/.agents/tasks/`.
- Development happens only in `work/tools_dev/`. `work/tools/` is touched only by the final install step (section 18).
- Dataset paths contain `#`: every shell command quotes them; Python code never builds shell strings.
- Output budget: all `auto/` folders together stay under 300 MB (estimate below 100 MB).

## 3. Dataset facts this design rests on (verified)

| Fact | Evidence |
|---|---|
| Class-file major versions: 61 (Aegis 544, Currency 27, LibreTorrent 688), 55 (AnyMemo 633), 52 (AmazeFileManager app 468, Diary, hash-checker, Markor, MMEX, Omni-Notes, Vanilla-Music), 51 (AmazeFileManager `commons_compress_7z` 39, AnkiDroid 676, openlauncher 250). So versions {51, 52, 55, 61}; no jsr/ret is legal (>= 51). | [scratch:facts_out.txt] |
| Two class dirs: AmazeFileManager (app + commons_compress_7z), AnkiDroid (AnkiDroid + api). Aegis's dir is `.../classes/debug/transformDebugClassesWithAsm/dirs/` (Hilt ASM output). No duplicate class names across dirs. | class_files.json, [scratch:gap.py] |
| No `R.class`/`R$*.class` in any class dir, no `R.txt`, no `R.jar`, no merged manifest under `build/` (only `intermediates/javac` or `intermediates/classes`). | [prev step find runs] |
| All 13 APKs contain `resources.arsc` and a binary `AndroidManifest.xml` (the merged manifest); every `res/` entry has the standard `res/<type>[-qualifiers]/<name>` path (no shortened names). | [scratch:probe_more.py] |
| No app has a navigation graph (`res/navigation*` absent in source and APK). | [prev step res survey] |
| JaCoCo method sets of the Monkey and APE reports are identical in all 13 apps; every JaCoCo class exists in the class dirs. | [scratch:naming.py, facts.py] |
| Bootstrap methods: only `LambdaMetafactory.metafactory` (javac ran with inline string concat). Implementation handle kinds 5, 6, 7, 8, 9 all occur (method references and constructor references). openlauncher, Vanilla-Music, AnyMemo and AnkiDroid contain no invokedynamic at all (anonymous classes only). | [scratch:flow_out.txt] |
| Opcodes present: tableswitch and lookupswitch in all apps; `wide` (hash-checker 1, AmazeFileManager 2); `multianewarray` (openlauncher 3, Markor 1, AnkiDroid 14); `ldc_w`, `ldc2_w`, `invokeinterface`, `invokedynamic`. Every method has a LineNumberTable. | [scratch:flow_out.txt] |
| Resource ids are inlined int constants (`ldc 0x7f......`) in 11 apps; Aegis and AnyMemo reference `R$id.x`, `R$string.x`, ... via `getstatic` (non-final R), so the field name is the resource name. | [scratch:probe_res.py] |
| `access$NNN` accessors have either 0 invokes plus field access, or exactly 1 invoke; every bridge and every synthetic `<init>` has exactly 1 invoke. | [scratch:probe_more.py] |
| JaCoCo-reported methods whose only bytecode callers are `@*Generated*` (excluded) classes: Aegis 3 (`AegisModule.provide*`), AnyMemo 36, hash-checker 4 (`*Module.*Helper`). | [scratch:probe_more.py] |
| Coverage caveat (orchestrator): `merged.ec` is the union of coverage segments 1..N; the launch dump (segment 00000) is never included, so in 9 of 13 apps some Monkey first-launch code looks unhit. No tool change: reports label "never hit" as "not hit in segments 1..N". | orchestrator note |
| v1 reference: `work/tools/build_graph.py` has sha256 `ba2d9d4cbe19034e86781347cabb9e47a0ca0c120618ecf28dedf621efc14c83` (md5 `3e630932...`, the hash Diary's `TOOL_ISSUES.md` records). Run on a temp copy of Currency's three inputs it reproduces all four files of `graphs/Currency/out/` byte for byte, its stdout equals `build_report.txt`, exit 0. The other v1 files (sha256): `list_methods.py` `1c9b25ca3be74f285a48fc30d98e95ac1a6b66c80da09167e9f8cab6673d3f0c`, `coverage_methods.py` `5333f2f5774657ced2de92caa3ed3a2b6229244fdce1cfafd4aa275be05b3726`, `viewer_template.html` `631a6fb62e9419f8b2fd7a29ea1ff23e383bcc26872d3094b2b0eaf9f870d23e`. All four are pinned in `tests/v1ref.py` (17.1). | revision-1 run, temp dir deleted |
| Source manifests: Aegis, AnyMemo, Currency, Diary, LibreTorrent and Markor have no `package` attribute (namespace in `build.gradle`; Aegis's is `namespace packageName`, not a literal). Currency and Diary name components without a dot (`android:name="Main"`). `<application android:backupAgent>` occurs in Aegis (`.AegisBackupAgent`) and MMEX (`.core.MoneyManagerBackupAgentHelper`). | revision-1 grep |
| Library-created generated classes: `DataBinderMapperImpl` (two per app: `androidx/databinding/` and the app package) in AnyMemo, LibreTorrent, MMEX; `*BindingImpl` LibreTorrent 37, AnyMemo 3, created only in the app-package `DataBinderMapperImpl` (LibreTorrent `ActivityAddTorrentBindingImpl` is referenced by no other class); `com/bumptech/glide/GeneratedAppGlideModuleImpl` in Aegis and AmazeFileManager; ButterKnife `*_ViewBinding` MMEX 15, Omni-Notes 12, `*$$ViewBinder` openlauncher 15. | revision-1 class-dir scan |
| Aegis and AnyMemo dispatch menus with `if` chains on `getstatic R$id` values (Aegis `MainActivity.java:1088` `if (itemId == R.id.action_settings)`, call at 1089; AnyMemo has no `case R.id.`). | review finding 3, rechecked |

The universe gap is fully explained by the rules of section 6 in all 13 apps (zero unexplained methods in either
direction, [scratch:facts_out.txt]):

| App | list_methods-style | JaCoCo (excl. harness) | v2 universe (reported + kept) | Main gap categories |
|---|---:|---:|---:|---|
| Aegis | 3100 | 2957 | 2994 (2955 + 39) | 58 @DaggerGenerated, 266 synthetic, 17+17 enum values/valueOf, 12 enum ctors, 12 synthetic classes |
| AmazeFileManager | 3018 | 2982 | 2981 (2978 + 3) | 504 synthetic, enum, 19 synthetic classes |
| AnkiDroid | 4237 | 4178 | 4186 (4174 + 12) | 452 synthetic, enum, 17 synthetic classes |
| AnyMemo | 2626 | 2192 | 2206 (2190 + 16) | 446 @DaggerGenerated, 236 synthetic, enum |
| Currency | 145 | 145 | 145 (143 + 2) | BuildConfig (2) out, `Data.<init>`, `Singleton.<init>` kept |
| Diary | 286 | 287 | 286 (285 + 1) | BuildConfig out, `FileUtils.<init>` kept |
| hash-checker | 661 | 525 | 529 (523 + 6) | 133 @DaggerGenerated, enum, synthetic |
| LibreTorrent | 4808 | 4728 | 4732 (4726 + 6) | 179 synthetic, enum (7 enum-constant-body ctors are reported and kept) |
| Markor | 2888 | 2855 | 2859 (2853 + 6) | 184 synthetic, enum |
| MMEX | 4329 | 4269 | 4270 (4267 + 3) | 407 synthetic, enum |
| Omni-Notes | 1471 | 1426 | 1454 (1424 + 30) | 98 synthetic, enum |
| openlauncher | 934 | 901 | 900 (899 + 1) | 111 synthetic, enum, 13 synthetic classes |
| Vanilla-Music | 1485 | 1468 | 1473 (1466 + 7) | 116 synthetic, enum |

"list_methods-style" is the v1 `list_methods.py` rule without JacocoInstrument/BuildConfig; "JaCoCo" includes BuildConfig.
The v2 universe for Currency and Diary equals their current `method_list.json` (same triples, same node names).

## 4. Module layout, ownership and shared conventions

### 4.1 Files under `work/tools_dev/`

| Path | Owner | Purpose |
|---|---|---|
| `tglib/__init__.py`, `tests/__init__.py` | A | empty package markers, A's first deliverable (`unittest discover -s tests -t .` needs `tests/__init__.py`) |
| `tests/v1ref.py` | A | v1 reference helpers shared by A's and I's tests: `V1_SHA256` (the four pinned hashes of section 3), `v1_script()` (17.1), `load_v1()` (exec of the v1 source into a dict) |
| `tglib/jsonio.py` | A | `write_json(path, obj, allowed_root)`, `write_text(path, text, allowed_root)` (atomic, 4.2 rule 5), `sha256_file(path) -> str` (hex digest of the file bytes), `guard_path(path, allowed_root) -> str` (returns `os.path.realpath(path)`; raises `ProtectedPathError(path, allowed_root)` unless that real path lies inside `os.path.realpath(allowed_root)` by `os.path.commonpath`), `ProtectedPathError` |
| `tglib/appdata.py` | A | dataset layout: class/source dirs, APK, JaCoCo paths, modules, variant, source lookup |
| `tglib/classfile.py` | A | class-file parser (constant pool, members, attributes) |
| `tglib/bytecode.py` | A | opcode table, instruction decoder, CFG, abstract interpreter, site records |
| `tglib/hierarchy.py` | A | class hierarchy over app classes, JVMS resolution/selection, subtype queries |
| `tglib/naming.py` | A | node names (v1-compatible + clash disambiguation) |
| `tglib/consumers.py` | A | consumer table (REGISTER/ASYNC/CALL), callback-interface method names, protocols, class factories, DI passthroughs |
| `tglib/universe.py` | A | universe builder + JaCoCo reconciliation; CLI writes `universe.json` |
| `tglib/callgraph.py` | A | RTA call graph; CLI writes `calls.json` |
| `tglib/axml.py` | B | binary XML (AXML) and `resources.arsc` decoders |
| `tglib/resources.py` | B | layouts, menus, preference XML, navigation, other `res/xml` from APK binary XML + source XML citations |
| `tglib/android_model.py` | B | framework base-type table, callback names per base family, component-start APIs, reflection APIs, built-in `android.R` table |
| `tglib/inventory.py` | B | inventory assembler; CLI writes `inventory.json` and `INVENTORY.md` |
| `tglib/v2graph.py` | I | v2 graph builder (load, merge, BFS, checks, outputs) |
| `build_graph.py` | I | CLI dispatcher: v1 path (verbatim) or v2 builder |
| `extract_app.py` | I | per-app / all-app extraction driver, aligned coverage, AUTO_SUMMARY tables |
| `list_methods.py`, `coverage_methods.py`, `viewer_template.html` | I | copied from `work/tools/` before I writes any v2 code, sha256 checked against `tests/v1ref.V1_SHA256`; never edited (the v1 path needs the template next to the script) |
| `tests/test_classfile.py`, `test_bytecode.py`, `test_appdata.py`, `test_naming.py`, `test_universe.py`, `test_callgraph.py` | A | |
| `tests/test_axml.py`, `test_resources.py`, `test_inventory.py` | B | |
| `tests/test_build_graph_v1compat.py`, `test_build_graph_v2.py`, `test_extract.py` | I | |
| `tests/fixtures/analyzer/`, `tests/fixtures/inventory/`, `tests/fixtures/graphs/` | A, B, I respectively | synthetic inputs |
| `verify_analyzer.txt`, `verify_inventory.txt`, `verify_integration.txt` | A, B, I | what was run, results |
| `README.md` (draft of `work/tools/README.md`) | I | user documentation |

A = implementer 1 (bytecode parser, universe, call graph, RTA). B = implementer 2 (manifest/resource/registration
inventory). I = integration step (build_graph v2, extraction runs, AUTO_SUMMARY, docs). A and B never edit each
other's files. B imports A's modules read-only (`appdata`, `classfile`, `bytecode`, `hierarchy`, `consumers`, `jsonio`, and from
`callgraph` only `callback_methods` and `harvest_sams`);
A imports nothing from B (A reads B's output file `inventory.json`, not B's code). If B needs a change in an A module,
B records it in `verify_inventory.txt` under "requests to A" and the integration step resolves it.

Order of work: A first delivers the two `__init__.py` files and `tests/v1ref.py`, then `jsonio`, `appdata`, `classfile`, `bytecode` (with the API of 8.4), then `hierarchy`,
`consumers` and `callgraph.callback_methods`/`harvest_sams`, because B depends on them; B starts with `axml`, `resources`, `android_model`, which need no A code, and codes its bytecode-dependent parts
against the API in 8.4.

### 4.2 Pipeline and data contracts

```
dataset app ──► universe.py ──► auto/universe.json ─┬─► inventory.py ──► auto/inventory.json, auto/INVENTORY.md
                                                    │                        │
                                                    └──────► callgraph.py ◄──┘ ──► auto/calls.json
extract_app.py also writes auto/coverage_baseline.json (aligned with universe.json) and auto/extract_report.txt
build_graph.py (USE_AUTO) reads auto/{universe,calls,inventory,coverage_baseline}.json + graph_def.py + parts/*.py
```

Contract rules shared by all three JSON files:

1. A method is identified by its key `(class, name, desc)` (JVM internal class name, method name, descriptor) and, if it
   is in the universe, by its `node` name. `universe.json` is the only authority for node names; `inventory.json` and
   `calls.json` copy node names from it and never compute names themselves.
2. A class is identified by its internal name (`org/billthefarmer/currency/Main`).
3. A code site is `(node or method key, pc)`; `line` is derived from the LineNumberTable (8.4).
4. Every JSON file starts with `"schema"`, `"app"` and, for files derived from another, the sha256 of the exact bytes of
   each input file (`"universe_sha256"`, `"inventory_sha256"`). A consumer that finds a mismatching hash refuses to run
   (exit 2, "stale input").
5. Files are UTF-8, written by `jsonio.write_json(path, obj, allowed_root)`: `json.dumps(obj, indent=1, ensure_ascii=False)` + `"\n"`,
   dict key order exactly as constructed (each schema below fixes the order), lists sorted as each schema states,
   written to `<path>.tmp-<pid>` in the same directory then `os.replace`d (atomic). On any exception the temp file is
   removed and the exception propagates. `write_json` and `write_text` call `guard_path(path, allowed_root)` first.
   Allowed roots: `extract_app.py` and the standalone CLIs of `universe.py`, `callgraph.py` and `inventory.py`: the
   directory that contains `--out` (and `--md`), which must be named `auto` (otherwise exit 2 before anything runs);
   `extract_app.py` passes `<graphs>/<App>/auto`. `build_graph.py` v2: the resolved `--out` directory, else
   `<gdir>/out`; an `--out` that resolves inside `<gdir>/auto` or inside the dataset root
   (`<script dir>/../final_java_only`, the `extract_app.py` default) is refused (exit 2). The v1 code path keeps v1's
   plain writes (11.2).

Who reads what (the shared data contracts; a consumer reads only the fields listed, so producers may add keys at the end
of a record without breaking consumers, but never rename or reorder the listed ones):

| File (producer) | Consumer | Fields consumed |
|---|---|---|
| `universe.json` (A) | `inventory.py` (B) | `methods[]`: `node`, `class`, `name`, `desc`, `ext_override`, `generated`, `generated_kind`; `classes[]`: `class`, `display`, `super`, `interfaces`, `ext_supertypes`, `inner`, `generated`, `generated_kind`, `in_universe`, `source_path` |
| `universe.json` (A) | `callgraph.py` (A) | everything (same owner) |
| `universe.json` (A) | `build_graph.py` v2 (I) | `methods[]` (all fields, as `INFO`), `counts`, `warnings` |
| `inventory.json` (B) | `callgraph.py` (A) | `framework_created[]` (`class`, `source`, `cite`), `res_ids`, `fw_res_ids` |
| `inventory.json` (B) | `build_graph.py` v2 (I) | `classes{}`: `callbacks`, `listener_callbacks`, `family`; the whole file as `INVENTORY` |
| `calls.json` (A) | `build_graph.py` v2 (I) | `edges[]` (all fields), `instantiated{}`, `excluded_candidates[]`, `stats` |
| `coverage_baseline.json` (I) | `build_graph.py` v2 (I) | `methods[]`: `node`, `jacoco_reported`, `monkey`, `ape` |

Hand-written fixture files (A's inventory fixture, B's universe fixtures, I's synthetic `auto/` folders) follow these
field lists, so each owner tests against the contract rather than against the other owner's code.

### 4.3 CLI conventions

- Library modules with a CLI (`universe.py`, `callgraph.py`, `inventory.py`) start with
  `if __name__ == '__main__': sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` before
  `from tglib import ...`, so `python3 -I tools/tglib/universe.py ...` works. Top-level scripts (`build_graph.py`,
  `extract_app.py`) insert their own directory.
- Arguments are parsed with `argparse`. Exit codes for every v2 CLI: 0 success; 1 completed with reported errors
  (build_graph, as v1; and `extract_app.py` given several apps or `--all` when at least one app failed, section 13);
  2 usage or input error (missing/stale/invalid input; nothing written); 3 data inconsistency detected (for example a
  universe rule violation; nothing written); 4 output write failure.
- Messages: progress and warnings go to stderr as `<tool>: <app>: <message>`; errors as `<tool>: ERROR: <message>`.
  No `logging` configuration. Every warning is also stored in the output JSON (`"warnings"` list) or report file.
- Paths given on the command line may be relative to the current directory; outputs record dataset paths relative to
  the app's `app/` folder and graph paths relative to the graph dir, never absolute paths (keeps outputs portable and
  deterministic).

## 5. Dataset access (`tglib/appdata.py`, owner A)

`appdata.load(app_root) -> AppLayout`, where `app_root` is `work/final_java_only/<App>`. Fields (all paths absolute
inside the object, relative in outputs):

- `name` (folder name, e.g. `hash-checker`), `app_dir` (`<app_root>/app`), `apk` (the single key of `class_files.json`,
  joined to `app_dir`; must exist).
- `class_dirs`: list of `ClassDir(path, rel, module_root, variant)` in `class_files.json` order. `module_root` is the
  path prefix before the first `/build/` component. `variant` is the path component after `intermediates/javac/` or
  `intermediates/classes/` (`debug`, `fdroidDebug`, `proDebug`, `thirdPartyStoresDebug`, `baseDebug`,
  `flavorAtestDebug`, `playDebug`, `flavorDefaultDebug`).
- `source_dirs`: `class_files.json` "sourcefiles" in order. The source set of a listed dir is the path component after
  its last `/src/` (`app/src/fdroid/java/` → `fdroid`); a dir without `/src/` has none.
- `checkout_root`: first path component of the first class dir (`Currency-#v1.58`).
- `module_roots`: every directory under `checkout_root` whose relative path has no component named `build` or starting
  with `.` and that contains `src/main/AndroidManifest.xml`. Order: the class dirs' module roots in `class_files.json`
  order (duplicates dropped), then the others sorted by path (openlauncher's `app/libs/*`, MMEX's `money/`,
  `androidSVG/`, ...). The variant of a module root is its class dir's variant, else the first class dir's variant.
- Test source sets: a source set whose lowercased name starts with `test` or `androidtest`. Files under
  `<module>/src/<test set>/` are never resource, manifest or source candidates, whether listed or not.
- `variant_source_sets(module_root)`: split the variant V into camel-case words (`flavorDefaultDebug` → `flavor`,
  `Default`, `Debug`; the last word is the build type). A directory `S` under `<module_root>/src/` (not a test set)
  applies when `S.lower()` equals the lowercased concatenation of one run of consecutive words of V. Priority order:
  S equal to V (full variant), then the build type, then the other applying sets by length descending (ties by name),
  then `main` (Android's overlay order: variant > build type > flavors > main). Examples (dirs that exist):
  AmazeFileManager `fdroidDebug` → `debug`, `fdroid`, `main` (not `play`); hash-checker `thirdPartyStoresDebug` →
  `debug`, `thirdPartyStores`, `main` (not `googlePlay`); LibreTorrent `baseDebug` → `debug`, `main` (not `play`,
  `release`).
- `jacoco`: `{'monkey': <app_root>/monkey/report/report.xml, 'ape': <app_root>/ape/report/report.xml}`.
- `find_source(class_internal, source_file) -> SourceHit(path_rel, rank, candidates)`: index, once per app, every
  `*.java` under `checkout_root` whose path has no component named `build` or starting with `.` and is not under a test
  source set; candidates are files whose path ends with `/<package dir>/<SourceFile>`. Rank 0: inside a listed source
  dir whose source set applies to its module's variant; rank 1: inside another listed dir; rank 2: unlisted dirs (Markor's
  `app/thirdparty/java/...`). Best = lowest rank, then shortest path, then lexicographic. `None` when no candidate.

Validation: `class_files.json` must be a one-key object whose value has non-empty `classfiles` and `sourcefiles`
string lists, every class dir must exist; otherwise `AppDataError` (CLIs exit 2). JaCoCo reports are required by
`universe.py` and `extract_app.py` (missing: exit 2), optional elsewhere.

## 6. Question 1: the method universe (`tglib/universe.py`, owner A)

### 6.1 Decision

Universe = every method JaCoCo reports in the union of the Monkey and APE `report.xml` files, minus the JacocoInstrument
harness, `BuildConfig` and `R`/`R$*` classes; plus every private empty no-argument constructor with a body that JaCoCo
filters as trivial, kept with `jacoco_reported = false` (the Currency precedent: `Data.<init>` and `Singleton.<init>` are
in Currency's 145 methods and show blank hit flags in `methods.csv`). Every other method with a body that JaCoCo does not
report is excluded with a named rule. Generated code that JaCoCo does report (data binding, Hilt `Hilt_*` classes,
ButterKnife, Glide, Room, Parceler, Icepick, protobuf, some Dagger builders) stays in the universe, tagged
`generated = true` with a `generated_kind`.

Rationale: JaCoCo is the oracle the study measures with; a universe that differs from it either creates targets that
can never be observed (methods JaCoCo cannot report) or loses methods that can be hit. The trivial-constructor carve-out
keeps the hand-built Currency graph valid and costs nothing (those methods simply never count as hit or as targets).
Keeping reported generated code avoids a universe smaller than the oracle; the tag lets modelers handle it in bulk and
lets the study filter it later.

### 6.2 Rules (applied to each parsed method in this order; first match wins)

| Rule | Exact test | Effect | Mirrors |
|---|---|---|---|
| X1 harness | class internal name has a path segment equal to `JacocoInstrument` | excluded, counted only | coverage harness |
| X2 build-config | simple class name `BuildConfig` and the class is generated (6.4) | excluded, listed | brief |
| X3 r-class | simple class name `R` or starting with `R$`, generated | excluded, listed (none exist in the dataset) | brief |
| X4 no-code | no Code attribute (abstract, native, interface abstract) | not a method node; natives listed by the inventory | — |
| X5 synthetic-class | class has ACC_SYNTHETIC (switch-map holders `Foo$1`) | excluded, listed | JaCoCo SyntheticFilter |
| X6 generated-annotation | the class itself, or the method, carries a RuntimeVisible or RuntimeInvisible annotation whose simple type name contains `Generated` (`dagger/internal/DaggerGenerated`, `javax/annotation/Generated`, ...). The outer class's annotation does not propagate (JaCoCo checks each class file; hash-checker's `DaggerAppComponent$Builder` is reported) | excluded, listed; this rule is what 9.5 calls generated-annotated code | JaCoCo AnnotationGeneratedFilter |
| X7 synthetic-method | method has ACC_SYNTHETIC and its name does not start with `lambda$` (accessors `access$NNN`, bridges, synthetic constructors, `$values`, `$deserializeLambda$`) | excluded, listed, used for collapsing (9.5) | JaCoCo SyntheticFilter, BridgeFilter |
| X8 enum-values | class has ACC_ENUM, super is `java/lang/Enum`, method `values` with desc `()[L<this>;` | excluded, listed | JaCoCo EnumFilter |
| X9 enum-valueOf | same class test, method `valueOf` with desc `(Ljava/lang/String;)L<this>;` | excluded, listed | JaCoCo EnumFilter |
| X10 enum-empty-ctor | same class test, `<init>(Ljava/lang/String;I)V` whose code is exactly the 7 bytes `2a 2b 1c b7 hi lo b1` with the Methodref naming `java/lang/Enum.<init>(Ljava/lang/String;I)V` | excluded, listed | JaCoCo EnumEmptyConstructorFilter |
| K1 private-empty-noarg | `<init>()V`, ACC_PRIVATE, code exactly `2a b7 hi lo b1` (aload_0, invokespecial super `<init>()V`, return), not reported by JaCoCo | kept, `jacoco_reported = false`, `rule = private-empty-noarg` | JaCoCo PrivateEmptyNoArgConstructorFilter |
| R reported | `(class, name, desc)` is in the JaCoCo union | kept, `jacoco_reported = true`, `rule = reported` | — |
| U unexplained | has code, not reported, no rule matched | fatal (exit 3) listing every case; `--allow-unexplained` keeps them with `jacoco_reported = false`, `rule = unexplained` and a warning | — |

Enum constant bodies (`TorrentSorting$SortingColumns$1`, `CardPlayerState$1`) have the enum class, not
`java/lang/Enum`, as super; X8-X10 do not apply and JaCoCo reports them (AnyMemo 3, LibreTorrent 7). Lambda bodies
(`lambda$...`, ACC_SYNTHETIC) are reported and kept.

"Listed" means a record in `universe.json` `excluded` (6.5): every method that has code and is not in the universe
under X2, X3 or X5-X10. X1 (harness) methods are only counted in `counts.excluded.harness`; X4 methods have no code and
are not listed (natives appear in the inventory's `natives`, 10.6 item 18).

### 6.3 Reconciliation (both directions, all fatal on violation)

1. Parse both reports with `xml.etree.ElementTree` (the DOCTYPE references `report.dtd`; ElementTree does not fetch it).
   Key = `(class@name, method@name, method@desc)`. If the Monkey and APE key sets differ, the union is used and a
   warning lists the difference (never observed).
2. Every reported key outside X1-X3 must exist in the class dirs with code and must not match X5-X10; otherwise exit 3
   (`JaCoCo-reported method <key> is excluded by rule <r>` or `... missing from class dirs`).
3. Every unreported method with code outside X1-X4 must match X5-X10 or K1; otherwise rule U.
4. `universe.json` records `counts` (parsed classes, methods with code, reported, kept-unreported, excluded per rule,
   generated) and the full `excluded` list, so the reconciliation can be audited without re-running.

Acceptance: section 3's table, exactly; zero unexplained in all 13 apps; for Currency and Diary the universe key set and
node names equal those of `graphs/<App>/method_list.json` named by v1's `method_names` (loaded with
`tests/v1ref.load_v1()`, 17.1).

### 6.4 `generated` and `generated_kind`

`generated = true` iff the class has no SourceFile attribute or `appdata.find_source` finds no source file for it (BuildConfig, data binding, Hilt, Dagger,
ButterKnife, Glide, Room, Parceler, Icepick, protobuf; Markor's `thirdparty/` sources are found, so they are not
generated). Nested classes use their own SourceFile attribute (which names the outer file). `generated_kind` is the
first matching rule, tested only when `generated` is true:

| Kind | Test (simple name = after the last `/`) |
|---|---|
| `databinding` | transitive super is `androidx/databinding/ViewDataBinding` or `android/databinding/ViewDataBinding`; or simple name `BR`, `DataBinderMapperImpl`, `DataBinderMapperImpl$*`, `DataBindingComponent`, `DataBindingTriggerClass`; or package ends with `/generated/callback` |
| `hilt` | simple name starts with `Hilt_` or contains `_HiltComponents` or ends with `_GeneratedInjector` or `_ComponentTreeDeps`; or package starts with `hilt_aggregated_deps` or `dagger/hilt/` |
| `dagger` | simple name starts with `Dagger` or ends with `_Factory`, `_MembersInjector`, `_Provide*Factory` (regex `_Provides?\w*Factory$`) or nested in such a class |
| `butterknife` | simple name ends with `_ViewBinding` or contains `$$ViewBinder` |
| `glide` | simple name in `GlideApp`, `GlideOptions`, `GlideRequest`, `GlideRequests`, `GeneratedAppGlideModuleImpl`, `GeneratedRequestManagerFactory` |
| `room` | simple name ends with `_Impl` or contains `_Impl$` |
| `parceler` | simple name contains `$$Parcelable` |
| `icepick` | simple name contains `$$Icepick` |
| `protobuf` | the top-level simple name (`simple.split('$')[0]`) ends with `Protos` (Aegis `GoogleAuthProtos` and its nested classes), or the transitive super is `com/google/protobuf/GeneratedMessageLite` or `com/google/protobuf/GeneratedMessageV3` |
| `android-manifest` | simple name `Manifest` or starting with `Manifest$` |
| `other` | none of the above |

Expected generated methods in the universe (prototype): LibreTorrent 866 (720 data binding), Aegis 553, MMEX 581, AnyMemo
166, AmazeFileManager 180, openlauncher 40, Omni-Notes 35, hash-checker 6, AnkiDroid 2, the other four 0.

Data-binding decision: kept (JaCoCo reports these methods, so they can be hit and can be targets), tagged
`generated_kind = databinding`. Their calls into app code are extracted like any other code (binding `executeBindings`
and `_internalCallback*` methods call view-model and handler methods). They are created by library code:
`androidx/databinding/DataBinderMapperImpl` by name (9.2 source 5), and every `*BindingImpl` and the app-package
`DataBinderMapperImpl` inside `DataBinderMapperImpl` methods that only the library calls (9.2 source 6), so they are
always live and app calls such as `binding.setViewModel(vm)` on the abstract `*Binding` type keep their edges. The
library's own calls into binding code (`executeBindings` from the frame callback, the inflate path) are not auto edges;
modelers add them in bulk through the read-only `INFO` mapping in part files (12.2). The study filters them with the `generated`/`generated_kind` CSV
columns (11.7).

### 6.5 `universe.json` (schema `tg-universe/1`)

Top-level keys in this order: `schema`, `app`, `dataset` (`app_dir`, `apk`, `class_dirs` [rel], `variants`),
`jacoco` (`monkey`, `ape` [paths relative to the app root], `reported_methods`, `same_method_sets`), `counts`, `classes`,
`methods`, `excluded`, `warnings`.

- `classes`: every parsed class (universe or not, harness excluded), sorted by internal name. Record:
  `class`, `display` (naming 7.2), `super`, `interfaces`, `access` (list of flag names), `kind`
  (`class|interface|enum|annotation`), `outer` (from InnerClasses/EnclosingMethod), `inner`
  (`top|member|local|anonymous`; anonymous = InnerClasses entry for this class with `inner_name_index == 0`),
  `enclosing_method` (method key `[class, name, desc]` or null), `source_file`, `source_path`, `source_rank`,
  `generated`, `generated_kind`, `class_dir` (index), `major`, `ext_supertypes` (sorted transitive external supertypes,
  computed with `hierarchy.py`), `in_universe` (has a universe method), `excluded_rule` (`synthetic-class`,
  `generated-annotation`, `harness`, `build-config`, `r-class` or null).
- `methods`: universe methods sorted by `(class, name, desc)` (the v1 `method_list.json` order). Record:
  `node`, `class`, `name`, `desc`, `access`, `flags` (v1-compatible: `static`, `synthetic` in that order),
  `source_file`, `line` (smallest line of the LineNumberTable, or null), `jacoco_reported`, `rule`, `generated`,
  `generated_kind`, `ext_override`, `ext_override_basis`, `overrides_app` (nodes of the app methods it directly
  overrides or implements, nearest declaration on each supertype path, sorted).
- `ext_override` is true iff the method is not static, not private, not `<init>`/`<clinit>`, not `lambda$`, and one of:
  basis `object` — `(name, desc)` is `equals(Ljava/lang/Object;)Z`, `hashCode()I`, `toString()Ljava/lang/String;`,
  `finalize()V` or `clone()Ljava/lang/Object;`; basis `bridge` — an X7 bridge in the same class delegates to it and no app
  supertype declares the bridge's signature; basis `structural` — the class has an external supertype other than
  `java/lang/Object` and no app supertype (including excluded app-dir classes) declares `(name, desc)`. `structural` is
  a candidate (framework class files are not available); the inventory's curated callback table (`CALLBACKS`, 10.4) confirms the
  common ones.
- `excluded`: `{class, name, desc, rule, detail}` for every method with code excluded under X2, X3 or X5-X10 (not X1,
  not X4; 6.2), sorted by `(class, name, desc)`; `rule` is the rule name of 6.2 (`build-config`, `synthetic-class`,
  ...), `detail` names the annotation type, the accessor's single invoke target, the enum class, etc. (null when there
  is nothing to add).

Size: about 0.5 KB per method, below 3 MB for the largest app.

## 7. Question 2: deterministic node names (`tglib/naming.py`, owner A)

### 7.1 Decision

Keep the v1 rule (`build_graph.method_names` + `param_names`) for every app without simple-name clashes, and add two
deterministic disambiguation steps that only fire where v1 would merge two methods into one node. Currency's and
Diary's names are unchanged (prototype: 0 names differ); the apps whose names would change (Aegis 10, AmazeFileManager 2,
AnkiDroid 69, AnyMemo 14, LibreTorrent 63, MMEX 14) have no hand-built graph yet.

### 7.2 Algorithm (input: the universe keys; only universe methods get node names)

1. Class display name. `simple` = internal name after the last `/` (nested classes keep `Outer$Inner`, anonymous
   `Outer$1`). `top` = `simple.split('$')[0]`. Group the classes that have universe methods by `top`. A group whose
   members come from two or more packages is a clash group. For each package `P` in a clash group take the smallest
   `k >= 1` such that the last `k` segments of `P` differ from the last `k` segments of every other package `Q` in the
   group (a package with fewer than `k` segments contributes all of its segments); if `k` reaches the number of
   segments of `P`, use all of `P`. The display name of every class in the group is `<those segments joined by '/'>/<simple>`
   (the default package would be `_root_`; none occurs). All members of a clash group get a prefix; no member is
   privileged.
2. `short = display + '.' + method name` (constructors `<init>`, static initialisers `<clinit>`, lambdas `lambda$m$0`).
3. If `short` is unique in the universe, `node = short`. Otherwise `node = short + '(' + params + ')'` with v1's
   `param_names` (simple innermost class names, primitives by name, `[]` per array dimension, so `Object[]`).
4. If several nodes are still equal, every member of that colliding set uses fully qualified parameter types instead:
   dotted package, nested `$` kept, primitives by name, `[]` per dimension (`GlideApp.with(android.app.Fragment)`,
   `GlideApp.with(androidx.fragment.app.Fragment)`, `PriorityConverter.convert(org.libtorrent4j.Priority[])`). Other
   overloads of the same short name keep their step-3 names.
5. If a collision remains (impossible for distinct keys), raise `NamingError` (exit 3).

Invariants asserted after naming: names unique; no name contains `@`, whitespace or a newline; the text before the first
`.` contains no `.` (the viewer groups by `m.split('.')[0]` and splits variants on `@`). Excluded methods never get node
names; diagnostics refer to them as `~<simple class>.<name><desc>`.

Clash groups in the dataset: AnkiDroid `api/Utils` vs `libanki/Utils`; LibreTorrent `drawer/TagItem` vs `tag/TagItem`,
`drawer/TagsAdapter(+$1)` vs `tag/TagsAdapter(+$1)`, `baseAdapters/BR` vs `libretorrent/BR`,
`databinding/DataBinderMapperImpl` vs `libretorrent/DataBinderMapperImpl`; AnyMemo `baseAdapters/BR` vs `fantastischmemo/BR`
(and DataBinderMapperImpl); MMEX `baseAdapters/BR` vs `ex/BR` (and DataBinderMapperImpl); Aegis four Hilt codegen
groups (`aggregatedroot/codegen/_com_..._AegisApplication` vs `processedrootsentinel/codegen/...`,
`codegen/_com_..._EntryPoint` vs `hilt_aggregated_deps/_com_..._EntryPoint`).

## 8. Question 3a: the class-file parser and bytecode layer (owner A)

### 8.1 `tglib/classfile.py`

`parse_class(data: bytes, path: str) -> ClassFile`; raises `ClassFormatError(path, offset, message)`. Rules:

- Magic `CAFEBABE`; accept major 45..69 (dataset: 51, 52, 55, 61); a major above 61 adds a warning.
- Constant pool tags 1 Utf8, 3 Integer, 4 Float, 5 Long and 6 Double (two slots), 7 Class, 8 String, 9 Fieldref,
  10 Methodref, 11 InterfaceMethodref, 12 NameAndType, 15 MethodHandle (reference kind 1..9), 16 MethodType, 17 Dynamic,
  18 InvokeDynamic, 19 Module, 20 Package. Any other tag is a ClassFormatError. Utf8 is modified UTF-8: decode with
  `bytes.decode('utf-8')` when the data has no `C0 80` and no `ED` byte, else a dedicated decoder (two-byte NUL,
  CESU-8 surrogate pairs combined).
- Header: access, this, super (0 only for `java/lang/Object`), interfaces; fields and methods with access, name,
  descriptor and attributes.
- Attributes decoded (all others skipped by length): class: `SourceFile`, `InnerClasses`, `EnclosingMethod`,
  `BootstrapMethods`, `NestHost`, `NestMembers`, `RuntimeVisibleAnnotations`, `RuntimeInvisibleAnnotations`;
  field: `ConstantValue`, both annotation attributes; method: `Code` (max_stack, max_locals, code bytes, exception
  table, nested `LineNumberTable`; a Code attribute may carry several LineNumberTable attributes (JVMS 4.7.12): their
  entries are merged, sorted by `(start_pc, line)`, exact duplicates dropped; `LocalVariableTable`, `StackMapTable` and
  others skipped), both annotation attributes. Every other attribute (`Signature`, `Exceptions`, `MethodParameters`,
  `Record`, `PermittedSubclasses`, type annotations, `SourceDebugExtension`, ...) is skipped by its length.
  Annotations are parsed per JVMS 4.7.16 (element values `B C D F I J S Z s e c @ [`); only annotation type descriptors
  are kept (plus nothing else).
- Every attribute must consume exactly its declared length and the file must end after the class attributes; otherwise
  ClassFormatError.
- Data model (frozen dataclasses): `ClassFile(path, major, minor, access, name, super, interfaces, fields, methods,
  source_file, inner_classes [(inner, outer, inner_name, access)], enclosing_method, bootstrap_methods
  [(handle_index, (arg indices))], nest_host, nest_members, annotations, pool)`, `Method(access, name, desc, code,
  annotations)`, `Code(max_stack, max_locals, bytecode, handlers [(start, end, handler, catch_type or None)],
  lines [(start_pc, line)] sorted)`. `ConstantPool` helpers: `utf8(i)`, `class_name(i)`, `member_ref(i) -> (tag, owner,
  name, desc)`, `method_handle(i) -> (kind, member_ref)`, `loadable(i)` for ldc (`('int', v)`, `('float', v)`,
  `('long', v)`, `('double', v)`, `('str', s)`, `('class', name)`, `('methodtype', desc)`, `('methodhandle', ...)`,
  `('dynamic', ...)`).
- `load_classes(layout) -> dict[name, ClassFile]` walks the class dirs in order, files sorted, parses every `*.class`;
  a duplicate class name across dirs is fatal (exit 3, never observed).

### 8.2 Opcode lengths (`tglib/bytecode.py`)

| Opcodes | Length in bytes |
|---|---|
| 0x00-0x0f (nop, aconst_null, iconst_m1..5, lconst, fconst, dconst) | 1 |
| 0x10 bipush, 0x12 ldc | 2 |
| 0x11 sipush, 0x13 ldc_w, 0x14 ldc2_w | 3 |
| 0x15-0x19 iload..aload, 0x36-0x3a istore..astore, 0xa9 ret, 0xbc newarray | 2 |
| 0x1a-0x35, 0x3b-0x83, 0x85-0x98, 0xac-0xb1, 0xbe, 0xbf, 0xc2, 0xc3 (implicit-index loads/stores, array access, stack, arithmetic, conversions, compares, returns, arraylength, athrow, monitors) | 1 |
| 0x84 iinc | 3 |
| 0x99-0xa8 (if<cond>, if_icmp<cond>, if_acmp<cond>, goto, jsr), 0xb2-0xb8 (get/put static/field, invokevirtual/special/static), 0xbb new, 0xbd anewarray, 0xc0 checkcast, 0xc1 instanceof, 0xc6 ifnull, 0xc7 ifnonnull | 3 |
| 0xb9 invokeinterface (index u2, count u1, zero u1), 0xba invokedynamic (index u2, two zero bytes), 0xc8 goto_w, 0xc9 jsr_w | 5 |
| 0xc5 multianewarray (index u2, dimensions u1) | 4 |
| 0xaa tableswitch | `1 + pad + 12 + 4*(high-low+1)`, `pad = (4 - (pc+1) % 4) % 4`; requires `low <= high` |
| 0xab lookupswitch | `1 + pad + 8 + 8*npairs`; requires `npairs >= 0` and strictly increasing keys |
| 0xc4 wide | 4 for wide iload..aload/istore..astore/ret; 6 for wide iinc; any other modified opcode is an error |
| 0xca-0xff | invalid (BytecodeError) |

`decode(code) -> list[Insn]` (pc, opcode, length, operands: index, local, constant, branch targets, switch table,
dimensions). Decoding must end exactly at the code length and every branch, switch and handler target must be an
instruction start; otherwise BytecodeError. jsr/jsr_w/ret decode (they are illegal from version 51 on); the abstract
interpreter rejects them.

### 8.3 Abstract interpreter

`analyze(cf, method, classes) -> MethodFacts` runs a forward data-flow over the CFG (leaders: pc 0, branch/switch
targets, instructions after branches/switches/returns/athrow, handler starts; an exceptional edge from every
instruction inside a protected range to its handler with stack `[('exc',)]`). State = (operand stack of Values, locals
map, case label). A Value is a frozenset of at most 16 tokens; a larger union becomes `{('unknown',)}`. Long/double
occupy two slots (second slot `('top',)`). Join = slot-wise union; a local slot present in only some predecessors
joins to `{('unknown',)}`; differing stack heights at a join are a BytecodeError.
A block is re-processed at most 64 times, after which its entry state is widened to all-unknown (termination guard;
never expected to trigger).

Tokens: `('this',)` (local 0 of instance methods, also uninitialised `this` in constructors), `('param', i)` (`i` =
0-based ordinal of the declared parameter, receiver excluded, a long/double parameter counting once; so it lines up
with `InvokeSite.args[i]` of a call to this method), `('null',)`, `('int', v)` (iconst, bipush, sipush, ldc Integer), `('str', s)` (ldc String), `('class', name)` (ldc
Class), `('new', class, pc)` (kept through `dup` and the `<init>` call), `('lambda', pc)` (LambdaMetafactory site),
`('indy', pc)` (other invokedynamic), `('field', owner, name, desc, static)` (getfield/getstatic), `('res', type, name)`
(getstatic of a field whose owner's simple name matches `R$[a-z]+`; Aegis and AnyMemo), `('ret', pc)` (result of the
invoke at pc; for a static method listed in `consumers.PASSTHROUGH` the result is the first argument's Value instead,
9.5), `('arr', pc)`, `('exc',)`, `('num',)` (non-constant primitive), `('unknown',)`. checkcast passes values
through; arithmetic produces `('num',)`; array loads produce `('unknown',)`; stack shuffles (dup, dup_x1, dup_x2, dup2,
dup2_x1, dup2_x2, swap, pop, pop2) move values per JVMS slot semantics.

Case labels (the decision a site sits under). A label is `('case', keys, pc)` or `('default', pc)`; `keys` is a
non-empty tuple of key tokens, each `('int', k)` or `('res', type, name)`, with int keys in ascending order.

- tableswitch/lookupswitch at `pc`: every distinct case target T other than the default target gets
  `('case', keys_T, pc)`, where `keys_T` holds every key that jumps to T (so `case R.id.a: case R.id.b:` sharing one
  body keeps both keys); the default target gets `('default', pc)` (keys that also jump there are subsumed).
- `if_icmpeq`/`if_icmpne` at `pc` where exactly one of the two operand Values is a single key token (`{('int', k)}` or
  `{('res', t, n)}`, the latter being Aegis's and AnyMemo's `getstatic R$id.x`): the equal successor (the branch target
  of `if_icmpeq`, the fall-through of `if_icmpne`) gets `('case', (token,), pc)`; the not-equal successor keeps the
  incoming label, so each test of an `if`/`else if` chain labels only its own body. Every other conditional branch
  leaves both successors with the incoming label.
- A new label replaces the incoming one (the innermost decision wins). At a join, equal labels stay; different labels,
  or a label joined with no label, give no label (so `if (id == R.id.a || id == R.id.b)` has no label; documented).

Every site records the label in effect at its pc; the call graph turns it into guard and trigger text (9.7).

### 8.4 Site records (API consumed by `callgraph.py` and by B's `inventory.py`)

```
MethodFacts(key, invokes: list[InvokeSite], indys: list[IndySite], news: list[NewSite], fields: list[FieldSite],
            switches: list[SwitchSite], returns: list[Value], failed: str | None)
InvokeSite(pc, line, op, owner, name, desc, interface_ref, receiver, args, label)   # op: virtual|special|static|interface
IndySite(pc, line, bsm, name, desc, captured, impl, sam_desc, instantiated_desc, label)
                                   # bsm: (owner, name); impl: (handle kind 1..9, owner, name, desc) for LambdaMetafactory
NewSite(pc, line, cls)
FieldSite(pc, line, op, owner, name, desc, value, receiver)                          # value only for puts
SwitchSite(pc, line, key, cases: dict[int, int], default)
```

`line(pc)` is the line of the last entry, in the merged `(start_pc, line)` order of 8.1, with `start_pc <= pc` (None
without a table). Lists are in pc order. `analyze_all(classes) -> dict[key, MethodFacts]` covers every method with code in every parsed class
except the harness. A method whose analysis fails gets `failed = <message>` and no sites; the calling CLI reports it and
exits 3 (the prototype analysed every method of all 13 apps, so a failure is a bug, not an expected input).

Performance budget: all methods of LibreTorrent (about 5,000 with code) parsed and analysed in under 30 s on the M1
(the prototype took about 1 s per app).

## 9. Question 3b: call resolution, RTA and auto edges (`tglib/hierarchy.py`, `tglib/callgraph.py`, `tglib/consumers.py`, owner A)

### 9.1 Hierarchy and JVMS resolution (`hierarchy.py`)

`Hierarchy(classes)` covers every parsed class-dir class (universe or excluded, harness omitted); everything else is
external and known only by name. API: `is_app(c)`, `superclass(c)`, `interfaces(c)`, `ext_supertypes(c)` (transitive
external names reached through app classes), `subtypes(c)` (transitive app subtypes, reverse index), `concrete_subtypes(c)`
(`c` itself if concrete, plus app subclasses/implementors without ACC_ABSTRACT/ACC_INTERFACE), and:

- `resolve(owner, name, desc, interface_ref)`: JVMS 5.4.3.3 (class: the class, its app superclasses, then a
  maximally-specific app superinterface method) or 5.4.3.4 (interface: the interface, then its app superinterfaces).
  Returns `('app', class, method)`, `('ext', type)` (the first external type where the search leaves the app
  hierarchy, or the owner itself if external) or `('missing',)`.
- `select(receiver, name, desc, resolved)`: JVMS 5.4.6 for a resolved non-private method (`resolved` is `resolve`'s
  result): walk the receiver's superclass chain, starting at the receiver, for a declaration with that name and
  descriptor that can override the resolved method (JVMS 5.4.5, simplified): skip declarations that are private or
  static, and, when the resolved method is an app method with package access, skip declarations in a class of another
  package than the resolved method's class (an external resolved method counts as public or protected). The first
  declaration kept is the result `('app', class, method)` (the same shape as `resolve`; `method` is the
  `classfile.Method`). If the walk reaches an external superclass first, return an app default method from a
  maximally-specific app superinterface if one exists (flag `ext_super_uncertain`), else `('ext', superclass)`. If
  the selected method is a bridge (ACC_BRIDGE), decode its single invoke on `this` and re-select
  `(receiver, name, desc')`, at most 2 levels (bridges collapse at selection time, keeping the receiver precise). The
  transitive clause of JVMS 5.4.5 (overriding through an intermediate public override of a package-access method) is
  not modelled; this is a documented limitation, not a measured absence.

### 9.2 Instantiation set (static RTA)

A class is instantiated when at least one source holds; `calls.json` records every class's sources:

1. `new`: a `new C` instruction in any analysed method (universe or excluded code, so Dagger factories count).
2. `ctor-ref`: a LambdaMetafactory site with implementation kind 8 (`C::new`).
3. `framework:<what>`: `inventory.json` `framework_created` (manifest components, the Application, the
   `<application>` attributes `android:backupAgent` and `android:appComponentFactory`, activity-alias targets, layout
   custom views and fragments, `app:layout_behavior` classes, menu action view/provider classes, custom preferences and
   preference fragments; 10.6 item 13).
4. `reflection`: constant-class reflective factories (`consumers.CLASS_FACTORIES`): `Class.newInstance` on
   `('class', C)`; `Constructor.newInstance` on the result of `getConstructor`/`getDeclaredConstructor` of
   `('class', C)`; `Class.forName("<dotted app class>")` whose result reaches `newInstance`/`getConstructor`/
   `getDeclaredConstructor` in the same method; `ViewModelProvider.get(Class)` and `get(String, Class)` (androidx and
   `android/arch`); `OneTimeWorkRequest$Builder.<init>(Class)`, `PeriodicWorkRequest$Builder.<init>(Class, ...)`,
   `OneTimeWorkRequest.from(Class)`; `Room.databaseBuilder(Context, Class, String)` and
   `Room.inMemoryDatabaseBuilder(Context, Class)` (instantiates `<C>_Impl` when that class exists);
   `Fragment.instantiate(Context, String[, Bundle])` (platform and androidx) and `FragmentFactory.instantiate(ClassLoader,
   String)` with a constant string.
5. `library-reflection`: classes that libraries create by name: `androidx/databinding/DataBinderMapperImpl`, any
   class whose simple name is `GeneratedAppGlideModuleImpl`, and every class with `generated_kind = butterknife`
   (`*_ViewBinding`, `*$$ViewBinder`, created reflectively by `ButterKnife.bind`).
6. `library-created:<creator class>`: every app class with a `new` or `ctor-ref` site inside any method of a creator
   class. Creator classes: simple name `DataBinderMapperImpl` (any package), simple name `GeneratedAppGlideModuleImpl`,
   and `generated_kind = butterknife` classes. Their methods run only when the library calls them (data binding's
   `getDataBinder`, Glide's generated module constructor, ButterKnife's binding constructors), so no auto edge ever
   reaches these `new` sites. One level only: a class created inside a method of a source-6 class (for example an
   `OnClickListenerImpl` created in `executeBindings`) is not source 6; it becomes live when that method is reached.
   Effect: LibreTorrent's 37 and AnyMemo's 3 `*BindingImpl` classes, the app's `AppGlideModule` subclass and the
   app-package `DataBinderMapperImpl` are always live.

Not sources (documented gaps, all visible as `excluded_candidates` or as liveness-pruned edges, both counted in the
reports): JSON deserialisers (`Gson.fromJson(..., Class)` and similar), `Parcelable.Creator` objects called by the
framework, `Class.forName` with a non-constant name, `ServiceLoader`, and any other library reflection not listed in
sources 4-6.

Lambdas are not classes and are never CHA candidates; their bodies are connected at their creation site (9.4).
Rationale: in callback-heavy code (Markor's `GsCallback$a1.callback` has hundreds of lambda implementations) adding
every lambda body as a dispatch candidate of every functional-interface call would create thousands of false polymorphic
edges, while the creation-site edge plus parameter-flow classification already records the real relationship.

Liveness class (used by build_graph's pruning, 11.6): `always_live = true` if a source of kind 3, 4, 5 or 6 holds or a
`new` or `ctor-ref` site lies in excluded code (Dagger factories, accessors); otherwise the class becomes live when a
universe method listed in its `sites` is reached. Source 6 only changes liveness: those classes already have a `new`
source, so the static RTA instantiation set is the same with or without it.

### 9.3 Resolution of each call site (method M in class K)

| Instruction | Rule | Edge |
|---|---|---|
| invokestatic | resolve from the owner through app superclasses | app target: `exact`; external: `ext_calls` entry |
| invokespecial `<init>` | exactly `owner.<init>(desc)`, no walk (implicit and explicit super/this constructor calls are explicit invokespecial in bytecode) | `exact` |
| invokespecial, private target | the resolved private method | `exact` |
| invokespecial, other (`super.m()`, `I.super.m()`) | search from the named owner upward for the first non-abstract app declaration (interface owner: its default method) | `exact`; external: `ext_calls` |
| invokevirtual/invokeinterface, resolved method private | nestmate private call (class files >= 55) | `exact` |
| same, receiver precise | receiver Value contains only `('new', C, pc)` tokens: `select(C)` for each C | `exact` if one target, else `cha`; no instantiation requirement |
| same, static owner is an app class or interface | S = `concrete_subtypes(owner)`; S_I = S ∩ instantiated; for each C in S_I, `select(C)` (this also covers methods the owner inherits from a framework class and app subclasses override; classes selecting the framework method add an `ext_calls` entry) | one edge per app target; `dispatch = exact` if `select` gives one result over all of S, else `cha`; `candidates` = number of app targets; `requires[t]` = the classes of S_I selecting t |
| same, static owner external (a framework or library type, e.g. a `View` or `Runnable` variable) | no CHA; record `ext_calls`; record `ext_dispatch` with up to 10 instantiated app overriders when some exist (skipped for the five `java/lang/Object` methods) | none |
| invokedynamic, LambdaMetafactory `metafactory`/`altMetafactory`, app implementation | kind 6/7, or kind 5/9 to a private method: the implementation method; kind 5/9 to a non-private method (method reference): bound receiver = first captured value, resolved like a virtual call; unbound: CHA over the implementation owner; kind 8: `C.<init>` | edge kind from 9.4, origin `auto-lambda` |
| invokedynamic, external implementation (`String::valueOf`) or other bootstrap (StringConcatFactory, ObjectMethods, SwitchBootstraps) | no edge; counted in `stats` | none |

Rows are tried top to bottom and the first match decides (a precise receiver beats the owner rows; inside
generated-annotated code the 9.5 rules come before the external-owner row). Calls to excluded synthetic or generated
methods are then collapsed (9.5).

Uninstantiated candidates: targets selected only by classes in S \ S_I are kept, but apart: they are written to
`excluded_candidates` as complete edge records (9.7) with `review = uninstantiated`, `requires = []` and the receiver
classes listed, and never become graph edges unless `AUTO_OPTIONS['uninstantiated']` is set (11.3). A target selected
by an instantiated class as well is an ordinary edge (its `requires` names only the instantiated classes). A site with T
empty and no excluded candidate goes to `unresolved_sites` with reason `only lambda implementations`
when the owner is a functional interface that the app's invokedynamic sites implement (those bodies are connected at
their creation sites, 9.4), else `no concrete implementation`.

### 9.4 Lambda and callback-object hand-offs (`consumers.py`)

Tracked values: every `('lambda', pc)` token; every `('new', C, pc)` token of an app class C; `('this',)` tokens (class
K). Consumer events of a tracked token in M:

1. Passed as argument j of an invoke whose callee is external, that is `hierarchy.resolve` gives `('ext', T)` or
   `('missing',)`: look up the consumer table with owner T (the Methodref owner when the result is `missing`; so an app
   subclass of `AlertDialog$Builder` is looked up as `android/app/AlertDialog$Builder`), the method name and the
   argument position. Event 5 is tested first and, when it matches, the table is not consulted. For `this`, only this
   event type counts, only in M itself (`this` does not follow event-2 hops) and only when the table has a
   non-`unknown` entry (passing `this` to `Toast.makeText` or `new Intent(this, ...)` is ignored).
2. Passed as argument j of an invoke whose callee is an app method P (exact or cha targets): continue with P's
   `('param', j)` events, up to 3 app-method hops; the edge's `trigger` names the wrapper (`via Main.updateDialog`).
3. Receiver of an invokeinterface/invokevirtual whose method name is the lambda's functional method name: `CALL`
   (invoked directly).
4. Stored by putfield/putstatic: `stored`. 5. Stored into an array (aastore) or passed to an external callee whose
   owner T (as in event 1) starts with `java/util/` and whose name is one of `add`, `addAll`, `put`, `offer`, `push`,
   `set`, `addFirst`, `addLast`: `collection` (tested before event 1). 6. Returned: `returned`. 7. None: `unconsumed`.

Event 2 is a hop, not a terminal event: the events that decide are the terminal ones (1, 3-7) found in M or in the
callees reached through at most 3 event-2 hops. Lambdas get one edge per lambda (creator → body) from all terminal
events. Callback objects get edges only from terminal events of type 1 (they need a consumer parameter type to find the
callback methods), except anonymous classes: when no terminal event of an anonymous class instance is of type 1, its
terminal events 3-7 give REGISTER edges to every method the class declares with `ext_override = true`, with the event
as `review` (a stored anonymous listener is usually registered later from a field).

Edge kind = `CALL` if any event is CALL, else `ASYNC` if any is ASYNC, else `REGISTER`. `review` is null when the
deciding event is a table entry of family `listener`, `dialog`, `sync` or `async`; otherwise it is the reason
(`reactive`, `unknown-consumer`, `stored`, `collection`, `returned`, `unconsumed`, `structural-callback`). Unknown
consumers therefore become REGISTER edges flagged for review, as the brief requires; REGISTER never makes anything
reachable, so a wrong guess there cannot create a false REACHABLE.

Consumer table (`CONSUMERS`, first match wins; `*` matches any owner; owners match the internal name or a listed
prefix):

| Family | Owner | Method names | Kind |
|---|---|---|---|
| sync | `java/util/Collections`, `java/util/Arrays` | `sort` | CALL |
| sync | `java/util/List`, `ArrayList`, `LinkedList`, `Collection`, `java/lang/Iterable`, `java/util/Set`, `HashSet`, `java/util/Iterator` | `sort`, `forEach`, `removeIf`, `replaceAll`, `forEachRemaining` | CALL |
| sync | `java/util/Map`, `HashMap`, `TreeMap`, `LinkedHashMap`, `java/util/concurrent/ConcurrentHashMap` | `forEach`, `compute`, `computeIfAbsent`, `computeIfPresent`, `merge`, `replaceAll` | CALL |
| sync | prefix `java/util/stream/`; `java/util/Optional` (`map`, `flatMap`, `filter`, `ifPresent`, `ifPresentOrElse`, `orElseGet`, `orElseThrow`); `java/util/Comparator` (`comparing*`, `thenComparing*`); `java/io/File` (`listFiles`, `list`) | as listed (all for streams) | CALL |
| async | `java/util/concurrent/Executor`, `ExecutorService`, `ScheduledExecutorService`, `ThreadPoolExecutor`, `AbstractExecutorService` | `execute`, `submit`, `invokeAll`, `invokeAny`, `schedule`, `scheduleAtFixedRate`, `scheduleWithFixedDelay` | ASYNC |
| async | `android/os/Handler` | `post`, `postDelayed`, `postAtTime`, `postAtFrontOfQueue` | ASYNC |
| async | `*` (any owner; framework hierarchies are not available, so View and Activity subclasses cannot be told apart) | `runOnUiThread`, `post`, `postDelayed`, `postOnAnimation`, `postOnAnimationDelayed` | ASYNC |
| async | `java/lang/Thread` `<init>` with a `Runnable` argument; `android/os/AsyncTask` static `execute(Runnable)`; `java/util/Timer` `schedule*`; `android/view/ViewPropertyAnimator` and `androidx/core/view/ViewPropertyAnimatorCompat` `withEndAction`, `withStartAction`; `java/util/concurrent/CompletableFuture` `runAsync`, `supplyAsync` | as listed | ASYNC (Thread: guard `the thread is started`) |
| reactive | prefixes `io/reactivex/`, `io/reactivex/rxjava3/`, `rx/`, `androidx/lifecycle/` classes whose simple name contains `LiveData` or is `Transformations` | any | REGISTER, review `reactive` |
| dialog | `android/app/AlertDialog$Builder`, `androidx/appcompat/app/AlertDialog$Builder`, `android/support/v7/app/AlertDialog$Builder`, `com/google/android/material/dialog/MaterialAlertDialogBuilder`, `android/app/AlertDialog`, `androidx/appcompat/app/AlertDialog`, `android/app/Dialog`, `androidx/appcompat/app/AppCompatDialog` | `setPositiveButton`, `setNegativeButton`, `setNeutralButton`, `setItems`, `setSingleChoiceItems`, `setMultiChoiceItems`, `setAdapter`, `setButton`, `setOn*Listener` | REGISTER |
| dialog | `com/afollestad/materialdialogs/MaterialDialog$Builder` | `onPositive`, `onNegative`, `onNeutral`, `onAny`, `callback`, `itemsCallback*`, `input`, `dismissListener`, `cancelListener`, `showListener`, `keyListener`, `listCallback*` | REGISTER |
| dialog | Snackbar (`com/google/android/material/snackbar/Snackbar`, `android/support/design/widget/Snackbar`) | `setAction`, `addCallback` | REGISTER |
| listener | `*` | listener patterns L1-L3 below | REGISTER |
| unknown | `*` | anything else | REGISTER, review `unknown-consumer` |

Listener patterns (Python `re.fullmatch` on the method name): L1 `(set|add)\w*(Listener|Callback|Watcher|Observer)`;
L2 `register\w*(Listener|Callback|Observer|Receiver)`; L3 one of `registerForActivityResult`, `registerReceiver`,
`addTextChangedListener`, `setAdapter`, `observe`, `observeForever`. Public API used by B: `consumers.classify(owner,
name, desc, arg_index) -> (family, kind, review)` and `callgraph.callback_methods(hierarchy, cls, param_type, harvested)
-> (method keys, review)` with `callgraph.harvest_sams(facts) -> harvested`.

Callback methods of a callback object of class C passed for a parameter of type T: for each `(name, arg count)` in
`IFACE_METHODS[simple name of T]`, the methods `select(C, name, desc, ('ext', T))` over the descriptors with that name
and arity declared in C's app superclass chain. `IFACE_METHODS` (keyed by simple name so platform, support and androidx variants
share an entry) contains at least: `View$OnClickListener` onClick/1, `View$OnLongClickListener` onLongClick/1,
`View$OnTouchListener` onTouch/2, `View$OnKeyListener` onKey/3, `View$OnFocusChangeListener` onFocusChange/2,
`View$OnDragListener` onDrag/2, `View$OnScrollChangeListener` onScrollChange/5, `AdapterView$OnItemClickListener`
onItemClick/4, `AdapterView$OnItemLongClickListener` onItemLongClick/4, `AdapterView$OnItemSelectedListener`
onItemSelected/4 + onNothingSelected/1, `TextWatcher` beforeTextChanged/4 + onTextChanged/4 + afterTextChanged/1,
`TextView$OnEditorActionListener` onEditorAction/3, `CompoundButton$OnCheckedChangeListener` onCheckedChanged/2,
`RadioGroup$OnCheckedChangeListener` onCheckedChanged/2, `SeekBar$OnSeekBarChangeListener` onProgressChanged/3 +
onStartTrackingTouch/1 + onStopTrackingTouch/1, `DialogInterface$OnClickListener` onClick/2,
`DialogInterface$OnMultiChoiceClickListener` onClick/3, `DialogInterface$OnCancelListener` onCancel/1,
`DialogInterface$OnDismissListener` onDismiss/1, `DialogInterface$OnShowListener` onShow/1, `DialogInterface$OnKeyListener`
onKey/3, `Preference$OnPreferenceClickListener` onPreferenceClick/1, `Preference$OnPreferenceChangeListener`
onPreferenceChange/2, `SharedPreferences$OnSharedPreferenceChangeListener` onSharedPreferenceChanged/2,
`MenuItem$OnMenuItemClickListener`, `PopupMenu$OnMenuItemClickListener`, `Toolbar$OnMenuItemClickListener`
onMenuItemClick/1, `SearchView$OnQueryTextListener` onQueryTextSubmit/1 + onQueryTextChange/1,
`ViewPager$OnPageChangeListener` onPageScrolled/3 + onPageSelected/1 + onPageScrollStateChanged/1, `ActionMode$Callback`
onCreateActionMode/2 + onPrepareActionMode/2 + onActionItemClicked/2 + onDestroyActionMode/1,
`Animation$AnimationListener` onAnimationStart/1 + onAnimationEnd/1 + onAnimationRepeat/1, `Animator$AnimatorListener`
onAnimationStart/1 + onAnimationEnd/1 + onAnimationCancel/1 + onAnimationRepeat/1, `Runnable` run/0, `Callable` call/0,
`Comparator` compare/2, `TimerTask` run/0, `Handler$Callback` handleMessage/1, `BroadcastReceiver` onReceive/2,
`ContentObserver` onChange/1 + onChange/2, `RecyclerView$OnScrollListener` onScrolled/3 + onScrollStateChanged/2,
`SwipeRefreshLayout$OnRefreshListener` onRefresh/0, `NavigationView$OnNavigationItemSelectedListener`
onNavigationItemSelected/1, `TabLayout$OnTabSelectedListener` onTabSelected/1 + onTabUnselected/1 + onTabReselected/1,
`DrawerLayout$DrawerListener` onDrawerSlide/2 + onDrawerOpened/1 + onDrawerClosed/1 + onDrawerStateChanged/1,
`OnBackPressedCallback` handleOnBackPressed/0, `ActivityResultCallback` onActivityResult/1, `Observer` onChanged/1.
Each run also harvests `(simple T, name, arity)` from the app's own invokedynamic sites (functional interfaces). If T
is unknown and C is anonymous with T among its direct supertypes, every method C declares with `ext_override = true`
is used (review `structural-callback`); otherwise no edge and an `unresolved_callbacks` record. For `this`, the
callback is selected for K and each instantiated subclass of K (`cha` when they differ).

Receiver protocols (`PROTOCOLS`): `execute`/`executeOnExecutor` on an app subclass C of `android/os/AsyncTask`: M → C.
onPreExecute (CALL), M → C.doInBackground (ASYNC), C.doInBackground → C.onPostExecute (ASYNC, guard `task not
cancelled`), → C.onProgressUpdate (ASYNC, guard `publishProgress called`), → C.onCancelled (ASYNC, guard `task
cancelled`); `start` on an app subclass of `java/lang/Thread` → C.run (ASYNC); `sendMessage*`/`sendEmptyMessage*` on an
app subclass of `android/os/Handler` → C.handleMessage (ASYNC). Precise receivers give `exact`, otherwise CHA over
instantiated subclasses. Only methods C declares or inherits from app classes produce edges.

All edges of this section have origin `auto-lambda` (invokedynamic) or `auto-callback` (objects and protocols),
evidence `SRC <File>:<line>` of the hand-off site, and `consumer`/`family`/`review` fields. `auto-callback` extends the
brief's origin list; it is needed because openlauncher, Vanilla-Music, AnyMemo and AnkiDroid have no lambdas at all.

### 9.5 Collapsing excluded code: accessors, synthetic constructors, generated Dagger/Hilt code

Raw edges are computed for every analysed method, universe or excluded. For a raw edge U → X with U in the universe and
X an excluded method with code (accessor `access$NNN`, synthetic constructor, enum helper, `@*Generated*` Dagger/Hilt
method), the builder walks raw edges from X through excluded methods only (at most 8 hops, cycle-safe) and emits U → V
for every universe method V reached. Switch-map holders (`Foo$1.<clinit>`, X5) are never collapse targets: 9.6
creates clinit edges only into universe `<clinit>` methods, and a switch-map initialiser only reads the constants of
an enum that is already initialised whenever one of its values is switched on. The collapsed edge's kind is REGISTER if any hop is
REGISTER, else ASYNC if any is ASYNC, else CALL; `dispatch` is `cha` if any hop is; `candidates` is the maximum;
`requires` concatenates the hops' requirements; `via` lists the excluded methods. Origin and evidence:

- Only synthetic hops (X5, X7-X10): origin and evidence of the first hop (`SRC Main.java:120`), so an accessor call reads
  like the direct call it stands for.
- Any hop in generated-annotated code (X6): origin `auto-generated`, evidence `INFERRED via generated Dagger code
  <simple names of up to 3 generated classes on the chain>; call at <File>:<line>` (orchestrator requirement).

Three resolution rules make injection chains connect. (a) applies in every method, (b) and (c) only inside
generated-annotated code: (a) static pass-through helpers (`consumers.PASSTHROUGH`, applied by the interpreter because
it is semantics-preserving: `dagger/internal/DoubleCheck.provider` and `.lazy`, `dagger/internal/SingleCheck.provider`,
`dagger/internal/Preconditions.checkNotNull*`, `dagger/internal/InstanceFactory.create`,
`dagger/internal/ProviderOfLazy.create`, `java/util/Objects.requireNonNull`) return their first argument's Value;
(b) a `('ret', pc)` token of an exact call to a method whose returns are all precise `new` tokens expands to those
tokens (one level), and fields declared in generated-annotated classes get a flow-insensitive points-to set (the precise
tokens stored into them anywhere); a receiver made only of such tokens dispatches precisely; (c) remaining calls on
`javax/inject/Provider`, `dagger/internal/Provider`, `dagger/Lazy`, `dagger/MembersInjector` or
`dagger/internal/Factory` use CHA over instantiated app-dir implementors, review `di-cha`. Chains through a class
whose simple name ends with `$SwitchingProvider` (Hilt, Aegis) get review `di-switch`: Hilt's switch over binding ids is
not refined, so every binding of that component counts as reachable from any injection into it (a documented
over-approximation, flagged in reports). Typical results: hand-written `@Provides` methods (called by
`Module_XFactory.get`), `@Inject` constructors (`new Foo(...)` in factories), members injection after `inject(this)`
(`X_MembersInjector.injectY` calling `@Inject` setters), and the Hilt base classes in Aegis (`Hilt_*` are reported and in
the universe; their calls into excluded components collapse). Acceptance: Aegis `AegisModule.provideIconPackManager`,
`providePreferences`, `provideVaultManager`, hash-checker `DatabaseHelperModule.databaseHelper`,
`LangHelperModule.langHelper`, `SettingsHelperModule.settingsHelper`, `ThemeHelperModule.themeHelper` and the 36 AnyMemo
methods whose only callers are generated code each get at least one incoming edge from a universe method.

Raw edges from excluded code that no universe method reaches are dropped and counted (`stats.collapsed_dropped`).

### 9.6 Class-initialisation edges (origin `auto-clinit`, evidence INFERRED)

For each analysed method M and each app class X ≠ class(M) with a universe `X.<clinit>`: the first active use of X in M
(`new X`; getstatic/putstatic of a field whose declaring class, found by JVMS field resolution, is X; invokestatic
resolved to a method declared in X) gives M → X.<clinit>, kind CALL, guard `class X not yet initialised in this
process`, evidence `INFERRED clinit: first active use of X (<instruction>) at <File>:<line>`. Also X.<clinit> → S.<clinit>
for an app superclass S with a `<clinit>` (superclass initialised first) and, for every universe constructor of X,
X.<init> → X.<clinit> (covers classes the framework instantiates). One edge per (M, X) pair. javac inlines constant fields, so they never appear as getstatic. Currency precedent:
`CurrencyWidgetProvider.onUpdate → Main.<clinit>` (hand edge, CALL, first access to `Main.CURRENCIES`) is produced as an
auto-clinit edge. On by default (`AUTO_OPTIONS['clinit']`), because without it every class with a static initialiser
has an unresolved `<clinit>`.

### 9.7 `calls.json` (schema `tg-calls/1`)

Top-level keys in this order. Every list is sorted as stated and every object's keys are written sorted unless a key
order is given; `src` is a universe node, or for a site in excluded code the diagnostic form `~<simple class>.<name><desc>`
of 7.2.

- `schema`, `app`, `universe_sha256`, `inventory_sha256` (null with `--no-inventory`, allowed only for A's unit tests).
- `stats`: an object with these keys in this order: `edges_by_origin`, `edges_by_dispatch`, `edges_by_kind`,
  `edges_by_review` (objects of counts with sorted keys; a null review or dispatch is counted under `none`), then the
  integers `call_sites`, `indy_sites`, `indy_external_impl`, `indy_other_bootstrap`, `excluded_candidates`,
  `unresolved_sites`, `unresolved_callbacks`, `ext_dispatch`, `collapsed`, `collapsed_dropped`,
  `instantiated_classes`, `always_live_classes`, `failures`. No timings.
- `instantiated`: `{class: {sources, sites, always_live}}`, classes sorted, only classes with at least one source.
  `sources`: sorted strings (`new`, `ctor-ref`, `framework:<source>` with the 10.6 item 13 source, `reflection`,
  `library-reflection`, `library-created:<creator class>`); `sites`: every universe node containing a `new` or
  `ctor-ref` site of the class, sorted (complete, because liveness depends on it); `always_live`: bool (9.2).
- `edges`: edge records (below), sorted by `(src, dst, kind, origin)`.
- `excluded_candidates`: edge records with the keys of an edge record, then `receiver_classes` (sorted) and `reason`
  (`no instantiation source`); `kind = CALL`, `origin = auto-cha`, `dispatch = cha`, `candidates` = the number of
  uninstantiated targets at the site, `requires = []`, `review = uninstantiated`, evidence `INFERRED CHA <Owner
  simple>.<name>: target selected only by classes without an instantiation source (<simple names, up to 3>); call at
  <File>:<line>`. One record per `(src, dst)`, sites merged, sorted by `(src, dst)`.
- `ext_calls`: `{node: ["<Owner simple>.<name>@<line>", ...]}`, nodes sorted, unique by owner and name, first line
  kept, sorted, at most 40 per method.
- `ext_dispatch`: `[{src, line, pc, owner, name, desc, overriders}]`, sorted by `(src, pc)`; `overriders` = up to 10
  sorted universe nodes of instantiated app classes overriding the external method.
- `unresolved_sites`: `[{src, line, pc, owner, name, desc, reason}]`, sorted by `(src, pc)`; `reason` is
  `only lambda implementations`, `no concrete implementation` or `missing method`.
- `unresolved_callbacks`: `[{src, line, pc, consumer, param_type, class, reason}]`, sorted by `(src, pc)`; `class` is
  the callback object's class (null for lambdas); `reason` is `unknown callback interface` or `no callback method`.
- `failures`: `[{method: [class, name, desc], message}]`, sorted by `method` (non-empty means exit 3).
- `warnings`: strings, sorted.

Edge record, keys in order: `src`, `dst` (universe nodes, never variants or pages), `kind` (CALL, ASYNC or REGISTER),
`origin` (`auto-exact`, `auto-cha`, `auto-lambda`, `auto-callback`, `auto-generated`, `auto-clinit`), `dispatch`
(`exact`, `cha` or null for clinit), `candidates`, `requires` (list of alternatives; each alternative is a list with one
class list per dispatch hop; `[]` = no requirement; at most 10 alternatives, merged by union beyond that), `review`,
`consumer`, `family`, `guard`, `trigger`, `evidence`, `sites` (`[{"file", "line", "pc"}]` sorted by pc, at most 20),
`via`. One record per `(src, dst, kind, origin)`, sites merged; edges sorted by that key. `origin` is `auto-cha` exactly
when `dispatch` is `cha` for a plain call site.

`<File>` below is the class's SourceFile attribute, else `<top-level simple name>.class`; `<line>` is `line(pc)`, else
`pc<n>`. Evidence:

- Exact calls and hand-offs: `SRC <File>:<l1>,<l2>` (distinct lines of the merged sites, ascending, at most 5, then
  `,...`). When the site's class has `generated = true` and no `source_path` (data binding, Hilt, Room, ... without a
  source file in the checkout) the form is `INFERRED bytecode <File>:<l1>,<l2> (generated, no source in checkout)`,
  because there is no source line a reader could check.
- CHA calls: `INFERRED CHA <Owner simple>.<name>: <n> instantiated targets; call at <File>:<line>` (including n = 1).
- Collapsed and clinit edges: the 9.5 and 9.6 forms.

Guard text. A site's label (8.3) gives `case <key>[, <key>...]` or `default`; a key `('int', k)` is written
`R.<type>.<name>` when `'0x%08x' % (k & 0xffffffff)` is in `inventory.res_ids`, `android.R.<type>.<name>` when it is in
`inventory.fw_res_ids` (FW-MEMORY names), else `k` in decimal; a key `('res', t, n)` is `R.<t>.<n>`. Resource names use
R's spelling (`.` in an arsc name becomes `_`). Protocol guards (9.4: `the thread is started`, `task not cancelled`,
...) and the clinit guard (9.6) are appended after the label text with `; `. An edge whose merged sites carry different
guards gets the distinct guards in pc order joined with ` | `; if any merged site has no guard, the edge has none.

Trigger text: one sentence, built from the lowest-pc site:

| Edge | Trigger |
|---|---|
| `auto-exact` CALL | `<prefix>calls <dst>` |
| `auto-cha` CALL | `<prefix>calls <dst> (virtual dispatch, <n> instantiated targets)` |
| `excluded_candidates` record | `<prefix>calls <dst> (virtual dispatch on a class with no instantiation source)` |
| `auto-lambda`/`auto-callback` REGISTER | `<prefix><consumer> registers <dst>[ (via <wrapper>, ...)]` |
| `auto-lambda`/`auto-callback` ASYNC | `<prefix><consumer> runs <dst> later[ (via ...)]` |
| `auto-lambda`/`auto-callback` CALL | `<prefix><consumer> calls <dst>[ (via ...)]` |
| `auto-generated` | `<prefix>calls <dst> through generated code <simple names of up to 3 generated classes>` |
| `auto-clinit` | `first active use of <display of X> runs its static initialiser` |

`<consumer>` is `<Owner simple>.<name>` (or the event name for events 3-7: `stored in a field`, ...). `<prefix>` is
`switch case R.id.<name>: ` (or `switch case android.R.id.<name>: `) when the site's label has a key of type `id` (the
first such key), whichever way the key was found (int constant or `getstatic R$id`); otherwise empty. With this prefix
v1's `gui_steps` names the menu item exactly as for the hand-written Currency edges (`switch case R.id.action_add`).
Expected size: below 15 MB for the largest app.

Currency acceptance (base names; checked by A's tests and the integration cross-check): Main.onCreate →
Main.lambda$onCreate$0 REGISTER (`Toolbar.setNavigationOnClickListener`); Data.startParse → Data.lambda$startParse$2
ASYNC (`ExecutorService.execute`); Data.lambda$startParse$2 → Data.lambda$startParse$0 and → Data.lambda$startParse$1
ASYNC (`Handler.post`); Main.onCreate → Main.onClick REGISTER (`setOnClickListener(this)`); Main.onUpdateClick →
Main.updateDialog CALL exact; Main.onUpdateClick → Main.lambda$onUpdateClick$1 REGISTER (via Main.updateDialog);
Main.<clinit> → Main$Currency.<init> CALL exact; CurrencyWidgetProvider.onUpdate → Main.<clinit> CALL auto-clinit;
Main.onOptionsItemSelected → Main.onAddClick CALL with guard `case R.id.action_add` and a trigger starting
`switch case R.id.action_add: ` (int-constant label resolved through `res_ids`).

Aegis acceptance (label from `getstatic R$id` in an `if` chain): MainActivity.onOptionsItemSelected →
MainActivity.startPreferencesActivity() (overloaded, hence the parameter list) CALL `auto-exact`, guard
`case R.id.action_settings`, trigger starting `switch case R.id.action_settings: `, evidence `SRC MainActivity.java:1089`
(the test is at line 1088).

Liveness acceptance for source 6. A's test: in LibreTorrent's `calls.json` every `*BindingImpl` class has
`always_live = true` with a `library-created:org/proninyaroslav/libretorrent/DataBinderMapperImpl` source, so every
edge whose `requires` names only such classes is traversable from the first liveness round. I's integration check
(recorded in `verify_integration.txt`): a v2 build of LibreTorrent with an empty `graph_def.py` (only `TITLE`,
`USE_AUTO = True`, `S_ENTRY`) in a temp graph dir prunes no edge whose `dst` is a `*BindingImpl` method.

## 10. Question 4: the Android inventory (`tglib/axml.py`, `resources.py`, `android_model.py`, `inventory.py`, owner B)

The inventory records facts with citations; it never defines pages. CLI:
`python3 -I tglib/inventory.py <app_root> --universe <auto/universe.json> --out <auto/inventory.json> --md
<auto/INVENTORY.md>`.

### 10.1 Sources and their roles (decision)

The dataset has no merged manifest, R.txt, R.jar or R classes under `build/` (section 3), so:

- Manifest content comes from the APK's binary `AndroidManifest.xml`: it is the merged manifest the app actually ran
  with (library components, flavor overlays and placeholders resolved; all its component names are fully qualified).
  Citations come from the source manifests `<module_root>/src/<set>/AndroidManifest.xml`, for every module root (5) in
  order and, within a module, its applying source sets in priority order (5); the first declaration that matches an APK
  component is its citation. A source `android:name` value N is matched as follows:
  1. N is relative if it starts with `.` or contains no `.` (Currency and Diary write `android:name="Main"`).
  2. A relative N is qualified with the package P of its own module: the manifest's `package` attribute; failing that,
     the first match of `namespace\s*=?\s*["']([\w.]+)["']` in `<module_root>/build.gradle`, else in
     `build.gradle.kts` (Currency `namespace = "..."`, Diary `namespace "..."`, AnyMemo/LibreTorrent/Markor single
     quotes). Qualified name: `P + N` when N starts with `.`, else `P + '.' + N`. It matches the APK component with
     exactly that name.
  3. If no P is found (Aegis: `namespace packageName` is not a literal) or the qualified name is not an APK component,
     the APK component whose fully qualified name ends with `'.' + N.lstrip('.')` matches, if exactly one does.
  4. An absolute N matches the APK component with exactly that name.
  5. No unique match: the source declaration cites nothing (a warning names file, line and N), and the APK component
     keeps looking in later manifests.

  `<application>` is matched by tag. A component without a source match is cited `APK AndroidManifest.xml (merged;
  from a library or generated)`. The cited line is the line of the element's start tag (`<activity`), which expat
  reports as `CurrentLineNumber` inside the start-element handler.
- Resource files: the APK's `res/` entries are the authoritative list (all configurations, including library
  resources). For each `res/<dir>/<name>.xml` of type layout, menu, xml or navigation, the content is read from the
  source file `<module_root>/src/<set>/res/<dir>/<name>.xml` found first when searching module roots in order (5) and,
  within a module, its applying source sets in priority order; test source sets are never searched. This gives line
  numbers and data-binding expressions. Without a source file the APK binary XML is decoded and cited
  `APK res/<dir>/<name>.xml`. Each resource records `origin: "src" | "apk"`.
- Resource-id map: `resources.arsc` of the APK (all 13 have it). Fallbacks, used only when the arsc is missing or
  unparseable, in order: `R.txt` under a module `build/` dir, `R.jar` (zipfile + A's class parser, ConstantValue
  attributes), `R$*.class` in the class dirs. None of the fallbacks exist in the dataset; they are implemented and
  unit-tested on synthetic files only. `inventory.json` records `res_id_source`.

### 10.2 Binary formats (`axml.py`)

- AXML (binary XML): chunk walk from offset 8 with `(type u16, header_size u16, size u32)` little-endian chunks; string
  pool (0x0001; UTF-8 flag 0x100 with the two length prefixes, otherwise UTF-16LE with 1-2 u16 length), resource map
  (0x0180), namespace start/end (0x0100/0x0101), element start (0x0102: line number, attributes with name, raw value and
  typed value `Res_value(size, res0, dataType, data)`), element end (0x0103), CDATA (0x0104). Typed values: string
  (0x03), reference (0x01, `@0x7f...`), attribute (0x02), integer decimal/hex (0x10/0x11), boolean (0x12), color types
  (0x1c-0x1f), dimension (0x05), fraction (0x06), float (0x04). Attribute names come from the string pool; when a name
  is empty the resource map gives the framework attribute id (for example `0x01010003` = `android:name`); B keeps a
  built-in table of the framework attribute ids it needs (`name`, `id`, `onClick`, `class`, `layout`, `exported`,
  `enabled`, `launchMode`, `theme`, `configChanges`, `windowSoftInputMode`, `targetActivity`, `process`, `permission`,
  `scheme`, `host`, `path*`, `mimeType`, `key`, `title`, `fragment`, `showAsAction`, `actionViewClass`,
  `actionProviderClass`, `targetClass`, `targetPackage`, `action`, `minSdkVersion`, `targetSdkVersion`,
  `versionCode`, `versionName`, `resource`, `value`, `configure`, `initialLayout`, `backupAgent`,
  `appComponentFactory`) and records unknown ones numerically.
- `resources.arsc`: table header, global string pool, package chunks (0x0200: id, name, type and key string pools),
  type spec (0x0202, skipped) and type chunks (0x0201: entry count, flags `FLAG_SPARSE` 0x01 and `FLAG_OFFSET16` 0x02
  handled, `NO_ENTRY` 0xFFFFFFFF/0xFFFF skipped). Entries: a full entry starts `size u16, flags u16, key u32`; an entry
  whose flags have `FLAG_COMPACT` (0x0008) is 8 bytes `key u16, flags u16, data u32` and its key index is that first
  u16. Other chunk types inside a package (0x0203 library, 0x0204 overlayable, 0x0205 overlayable policy, 0x0206 staged
  alias, and any unknown type) are skipped by their `size`; a size that runs past the enclosing chunk is an `AxmlError`.
  Map `0xPPTTEEEE -> (type, entry name)`; every configuration contributes the same names, the first seen wins. Package
  0x7f only (prototype: Currency 250 entries, LibreTorrent 6557, AnkiDroid 2796, Aegis 6492).
- Framework ids (`0x01......`) are not in the app's arsc. A small built-in table, labelled FW-MEMORY (values recalled,
  not checked against framework-res), names the ones menus and dialogs use: `android.R.id.home` 0x0102002c, `content`
  0x01020002, `list` 0x0102000a, `empty` 0x01020004, `text1` 0x01020014, `text2` 0x01020015, `button1..3`
  0x01020019-0x0102001b, `edit` 0x01020003, `input` 0x01020009, `title` 0x01020016, `summary` 0x01020010, `icon`
  0x01020006, `checkbox` 0x01020001, `widget_frame` 0x01020018, `progress` 0x0102000d, `selectAll` 0x0102001f, `cut`
  0x01020020, `copy` 0x01020021, `paste` 0x01020022; `android.R.string.cancel` 0x01040000, `no` 0x01040009, `ok`
  0x0104000a, `yes` 0x01040013; `android.R.style.Theme_NoDisplay` 0x01030055. Other framework ids stay numeric
  (`android:0x0106000d`). Names from this table carry `"fw_memory": true`. `inventory.json` also writes the whole
  table as `fw_res_ids` (10.6 item 4), so `callgraph.py` can name framework ids in guards without importing B's code.
- Every decoder raises `AxmlError(entry, offset, message)` on a malformed chunk; there is no partial result for that file.

### 10.3 Resource-id names and how bytecode constants use them

`res_ids` maps `'0x%08x' % id` (lowercase hex, 8 digits) of every 0x7f id to `"<type>/<name>"` (arsc spelling),
sorted by id; `fw_res_ids` does the same for the FW-MEMORY table. A reverse map `(type, name) -> id` serves Aegis and
AnyMemo, whose bytecode carries `('res', type, name)` tokens instead of ints (R field names spell `.` as `_`, so the
reverse map is keyed by the R spelling). Users: the call graph's case guards and trigger prefixes (8.3, 9.7:
`case R.id.action_copy` from a switch on inlined ints, `case R.id.action_settings` from an `if` chain on
`getstatic R$id`), view ids of registration sites, layout ids of `setContentView`/`inflate`, menu ids of
`inflate`/`findItem`, string ids of titles. Acceptance check (recorded in `verify_inventory.txt` for every
app): at least 99% of 0x7f constants passed to `findViewById`, `setContentView`, `MenuInflater.inflate`,
`LayoutInflater.inflate`, `Menu.findItem` and `getString` resolve to an arsc entry of the expected type (`id`, `layout`,
`menu`, `layout`, `id`, `string`).

### 10.4 `android_model.py` tables

- `BASE_TYPES`: external internal names → family, matched against `ext_supertypes`, in priority order:
  `app-widget-provider` (`android/appwidget/AppWidgetProvider`), `receiver` (`android/content/BroadcastReceiver`),
  `dialog-fragment` (`android/app/DialogFragment`, `androidx/fragment/app/DialogFragment`,
  `android/support/v4/app/DialogFragment`, `androidx/appcompat/app/AppCompatDialogFragment`,
  `com/google/android/material/bottomsheet/BottomSheetDialogFragment`), `preference-fragment`
  (`android/preference/PreferenceFragment`, `androidx/preference/PreferenceFragmentCompat`,
  `android/support/v7/preference/PreferenceFragmentCompat`, `android/preference/PreferenceActivity`), `fragment`
  (`android/app/Fragment`, `androidx/fragment/app/Fragment`, `android/support/v4/app/Fragment`), `activity`
  (`android/app/Activity` and every subclass name: `AppCompatActivity`, `FragmentActivity`, `ComponentActivity`,
  `ListActivity`, `PreferenceActivity`, support variants), `service` (`android/app/Service`, `IntentService`,
  `android/app/job/JobService`, `androidx/core/app/JobIntentService`, `android/service/dreams/DreamService`,
  `android/widget/RemoteViewsService`, `android/service/quicksettings/TileService`,
  `android/accessibilityservice/AccessibilityService`, `android/media/browse/MediaBrowserService`,
  `androidx/media/MediaBrowserServiceCompat`), `provider` (`android/content/ContentProvider`, `androidx/core/content/FileProvider`),
  `application` (`android/app/Application`, `androidx/multidex/MultiDexApplication`), `worker`
  (`androidx/work/Worker`, `ListenableWorker`, `CoroutineWorker`), `view-model` (`androidx/lifecycle/ViewModel`,
  `AndroidViewModel`), `preference` (`android/preference/Preference`, `androidx/preference/Preference` and their
  subclasses), `adapter` (`android/widget/BaseAdapter`, `ArrayAdapter`, `CursorAdapter`, `SimpleCursorAdapter`,
  `androidx/recyclerview/widget/RecyclerView$Adapter`, `ListAdapter`, `androidx/viewpager/widget/PagerAdapter`,
  `androidx/fragment/app/FragmentPagerAdapter`, `FragmentStatePagerAdapter`, `androidx/viewpager2/adapter/FragmentStateAdapter`,
  support variants), `view-holder` (`RecyclerView$ViewHolder`), `view` (`android/view/View`, `ViewGroup` and every
  `android/widget/*`, `androidx/*` widget class seen in ext_supertypes whose simple name ends with `View`, `Layout`,
  `Button`, `Text`, `Bar`, `Pager`, `Spinner`), `async-task` (`android/os/AsyncTask`), `handler` (`android/os/Handler`),
  `thread` (`java/lang/Thread`), `timer-task` (`java/util/TimerTask`), `content-observer` (`android/database/ContentObserver`),
  `other`. Names are full internal names (support-library variants spelled out). Framework class files are not
  available, so `ext_supertypes` only holds the external types that app classes name directly (an app class extending
  `AppCompatActivity` does not reveal `android/app/Activity`); each family therefore lists the concrete framework and
  library classes apps extend. `inventory.py` writes every external supertype that matches no family to `warnings`,
  and `verify_inventory.txt` must show that list for all 13 apps with each entry either added to a family or explained
  as `other`.
- `CALLBACKS[family]`: framework callback names to report per family (activity: `onCreate`, `onStart`, `onRestart`,
  `onResume`, `onPostCreate`, `onPostResume`, `onPause`, `onStop`, `onDestroy`, `onSaveInstanceState`,
  `onRestoreInstanceState`, `onNewIntent`, `onActivityResult`, `onRequestPermissionsResult`, `onConfigurationChanged`,
  `onCreateOptionsMenu`, `onPrepareOptionsMenu`, `onOptionsItemSelected`, `onMenuOpened`, `onCreateContextMenu`,
  `onContextItemSelected`, `onBackPressed`, `onSupportNavigateUp`, `onNavigateUp`, `onKeyDown`, `onKeyUp`,
  `dispatchKeyEvent`, `onTouchEvent`, `dispatchTouchEvent`, `onWindowFocusChanged`, `onUserLeaveHint`,
  `onAttachedToWindow`, `onCreateDialog`, `onPrepareDialog`, `onActionModeStarted`, `onActionModeFinished`,
  `onTrimMemory`, `onLowMemory`, `onAttachFragment`, `onSearchRequested`; fragment adds `onAttach`, `onCreateView`,
  `onViewCreated`, `onActivityCreated`, `onViewStateRestored`, `onDestroyView`, `onDetach`, `onHiddenChanged`,
  `setUserVisibleHint`, `onCreatePreferences`, `onPreferenceTreeClick`, `onDisplayPreferenceDialog`; dialog-fragment adds
  `onCreateDialog`, `onCancel`, `onDismiss`, `onStart`; service: `onCreate`, `onStartCommand`, `onStart`, `onBind`,
  `onUnbind`, `onRebind`, `onDestroy`, `onHandleIntent`, `onHandleWork`, `onStartJob`, `onStopJob`, `onTaskRemoved`,
  `onGetViewFactory`; receiver: `onReceive`; app-widget-provider adds `onUpdate`, `onDeleted`, `onEnabled`,
  `onDisabled`, `onAppWidgetOptionsChanged`, `onRestored`; provider: `onCreate`, `query`, `insert`, `update`, `delete`,
  `getType`, `openFile`, `call`; application: `onCreate`, `onTerminate`, `onConfigurationChanged`, `onLowMemory`,
  `onTrimMemory`, `attachBaseContext`; adapter: `getCount`, `getItem`, `getItemId`, `getView`, `getDropDownView`,
  `getItemViewType`, `getViewTypeCount`, `onCreateViewHolder`, `onBindViewHolder`, `getItemCount`, `instantiateItem`,
  `destroyItem`, `getPageTitle`, `createFragment`, `getFilter`, `areAllItemsEnabled`, `isEnabled`, `hasStableIds`;
  view: `onDraw`, `onMeasure`, `onLayout`, `onSizeChanged`, `onTouchEvent`, `onInterceptTouchEvent`,
  `onAttachedToWindow`, `onDetachedFromWindow`, `onFinishInflate`, `onKeyDown`, `onSaveInstanceState`,
  `onRestoreInstanceState`, `computeScroll`, `dispatchDraw`; preference: `onBindView`, `onBindViewHolder`,
  `onCreateView`, `onClick`, `onDialogClosed`, `onBindDialogView`, `onCreateDialogView`, `onGetDefaultValue`,
  `onSetInitialValue`, `onAttachedToHierarchy`, `onPrepareDialogBuilder`; async-task: `onPreExecute`, `doInBackground`,
  `onProgressUpdate`, `onPostExecute`, `onCancelled`; worker: `doWork`, `startWork`, `onStopped`; view-model:
  `onCleared`; handler: `handleMessage`; thread and timer-task: `run`; content-observer: `onChange`).
- `START_APIS`: `startActivity`, `startActivityForResult`, `startActivities`, `startActivityIfNeeded`,
  `startService`, `startForegroundService`, `bindService`, `stopService`, `sendBroadcast`, `sendOrderedBroadcast`,
  `sendStickyBroadcast` (any owner), `LocalBroadcastManager.sendBroadcast`, `PendingIntent.getActivity|getActivities|
  getService|getForegroundService|getBroadcast`, `ActivityResultLauncher.launch`, `AlarmManager.set*`,
  `JobScheduler.schedule`, `WorkManager.enqueue*|beginWith|beginUniqueWork`, `NavController.navigate`.
- `REFLECTION_APIS`: `Class.forName`, `Class.newInstance`, `Class.getMethod|getDeclaredMethod|getField|getDeclaredField|
  getConstructor|getDeclaredConstructor`, `Method.invoke`, `Constructor.newInstance`, `Field.get*|set*`,
  `Resources.getIdentifier`, `WebView.addJavascriptInterface`, `java/lang/reflect/Proxy.newProxyInstance`,
  `java/util/ServiceLoader.load`.

### 10.5 Bytecode-derived facts (B's use of A's API)

B calls `appdata.load`, `classfile.load_classes`, `bytecode.analyze_all`, `hierarchy.Hierarchy`, `consumers.classify`,
`callgraph.harvest_sams` and `callgraph.callback_methods`; it never parses bytecode itself. Node names
come from `universe.json`. Derived values:

- View id of a receiver: `('ret', pc)` of `findViewById`/`requireViewById`/`findRequiredView*`/`findOptionalView*`/
  `findRequiredViewAsType` with an int or `('res', 'id', n)` argument; a field `(K, f)` that a putfield/putstatic in any
  analysed method of any class assigns such a result (ButterKnife assigns `target.fab` inside `K_ViewBinding.<init>`,
  not in K; Omni-Notes, MMEX), read back as a `('field', K, f, ...)` token (`via: field`; a field assigned several ids
  gets all of them, sorted); a field of a `databinding` class whose name equals the camel-case of an id
  (`fab` → `id/fab`, `toolbarTitle` → `id/toolbar_title`; `via: binding-field`).
- Menu item id: `('ret', pc)` of `Menu.findItem(int)`.
- Intent target of a start site: the Intent argument's `('new', android/content/Intent, pc)` token, then the matching
  `<init>` site (`(Context, Class)` → class literal; `(String)`/`(String, Uri)` → action) and every `setClass`,
  `setClassName`, `setComponent(new ComponentName(.., X.class))`, `setAction` site with that receiver token in the same
  method. Anything else is `target: null, how: "dynamic"`.

### 10.6 `inventory.json` (schema `tg-inventory/1`)

Top-level keys in order (lists sorted as stated):

1. `schema`, `app`, `universe_sha256`.
2. `sources`: `apk`, `manifest: "APK AndroidManifest.xml (merged)"`, `manifest_sources` (rel paths), `res_dirs` (rel
   paths searched, priority order), `res_id_source`.
3. `package`: `id`, `version_name`, `version_code`, `min_sdk`, `target_sdk`, `application_class` (internal name or null).
4. `res_ids`: `{"0x7f080010": "id/action_copy", ...}`; then `fw_res_ids`: `{"0x0102002c": "id/home", ...}` (the
   FW-MEMORY table of 10.2). Keys `'0x%08x'`, sorted.
5. `components`: one per manifest component, sorted by (kind, class): `kind` (activity, activity-alias, service,
   receiver, provider), `class` (internal name), `app_class` (in class dirs), `target` (alias target), `exported`
   (explicit value, else implied by an intent filter for targetSdk < 31, recorded as `"implied"`), `enabled`,
   `launch_mode`, `theme` (`style/...` or `android:0x...`), `theme_hint` (`dialog` if the style name contains `Dialog`,
   `translucent` if it contains `Translucent`, `no-display` for Theme_NoDisplay, else null), `config_changes`,
   `window_soft_input_mode`, `process`, `permission`, `intent_filters` (`actions`, `categories`, `data` objects with
   `scheme`, `host`, `port`, `path`, `pathPrefix`, `pathPattern`, `mimeType`; `priority`), `meta_data` (`name`,
   `value` or `resource`), `cite` (`{"src": "<rel path>:<line>" | null, "apk": "AndroidManifest.xml"}`). The coverage
   harness receiver (`JacocoInstrument`) is listed with `harness: true` and excluded from `entry_points`.
6. `entry_points`: derived, sorted: `launcher` (MAIN + LAUNCHER), `deep-link` (VIEW + BROWSABLE with data), `view-file`
   (VIEW with mimeType or file/content scheme), `share` (SEND, SEND_MULTIPLE, SENDTO), `widget` (APPWIDGET_UPDATE
   receivers with their `android.appwidget.provider` xml and its `configure` activity), `shortcut` (static
   `android.app.shortcuts` meta-data and the shortcut intents), `search` (SEARCH action, `android.app.searchable`),
   `system-broadcast` (BOOT_COMPLETED, PACKAGE_*, MEDIA_*, CONNECTIVITY, ...), `exported-other`. Each:
   `{type, component, detail, cite}`.
7. `layouts`: `{ "layout/main": {...}, "layout-land/main": {...} }` keyed by `<dir>/<name>`, each `origin`, `cite`,
   `views` in document order: `tag`, `class` (app internal name when the tag or `class=` is an app class), `id`,
   `on_click`, `fragment` (`android:name`/`class` of `<fragment>` or `FragmentContainerView`), `include` (layout name),
   `behavior` (`app:layout_behavior`), `bindings` (data-binding `@{...}` attributes from source files: `[attr, expr]`),
   `line`.
8. `menus`: `{ "menu/main": {origin, cite, items} }`, items in order: `id`, `title` (string resource name or literal),
   `show_as_action`, `group`, `checkable`, `visible`, `enabled`, `order`, `action_view_class`, `action_provider_class`,
   `on_click`, `submenu` (nested items), `line`.
9. `preferences`: every `res/xml` file whose root is `PreferenceScreen` (any package) or `preference-headers`:
   `{origin, cite, items}`, items: `tag`, `class` (app class for custom preferences), `key`, `title`, `summary`,
   `fragment`, `dependency`, `default`, `entries`, `entry_values`, `intent` (`action`, `target_class`, `target_package`,
   `data`), `children` (nested screens and categories), `line`.
10. `navigation`: same shape for `res/navigation` files (destinations, actions); empty for all 13 apps.
11. `xml`: other `res/xml` files by root tag: `appwidget-provider` (`initial_layout`, `configure`,
    `update_period_millis`, `preview_image`), `shortcuts` (shortcut `id`, `short_label`, intents), `searchable`,
    `paths` (FileProvider), `network-security-config`, `accessibility-service`, others with `root` only.
12. `classes`: `{internal name: {node_prefix (display name), family, bases, implements (external listener interfaces),
    callbacks: {callback name: [nodes] (the implementation an instance of this class runs, own or inherited)},
    listener_callbacks: {interface simple name: [nodes]}, component (manifest kind or null), layouts (resources that
    reference it), new_sites (universe nodes with `new` of it), generated, generated_kind}}` for every class with a
    universe method or a framework-creation fact.
13. `framework_created`: `[{class, source (manifest|application|application-attr|activity-alias|layout-view|
    layout-fragment|layout-behavior|menu-action-view|menu-action-provider|preference-class|preference-fragment|
    preference-header|appwidget-configure|navigation), cite}]`, sorted by (class, source); only app classes (in the
    class dirs). `application-attr` covers the `<application>` attributes `android:backupAgent` (Aegis
    `AegisBackupAgent`, MMEX `MoneyManagerBackupAgentHelper`) and `android:appComponentFactory`. Consumed by
    `callgraph.py` (9.2 source 3).
14. `registrations`: every hand-off site whose consumer family is listener, dialog, reactive, async or unknown with a
    callback object, sorted by (node, pc): `site` (`node`, `line`, `pc`, `file`), `consumer` (`<Owner simple>.<name>`),
    `family`, `kind`, `review`, `listener` (`{kind: lambda|new|this|field|param|unknown, class, callbacks: [nodes]}`),
    `view_id`, `view_via`, `menu_item_id`.
15. `component_starts`: start sites, sorted by (node, pc): `site`, `api`, `target` (internal name or null), `action`,
    `how` (`class-literal`, `set-class`, `set-class-name`, `component`, `action`, `dynamic`), `pending` (true for
    PendingIntent factories).
16. `async`: `async-task` (subclass, execute sites), `thread` (subclass, start sites), `handler` (subclass, send
    sites), `worker` (class, enqueue sites with class literal), `job` (JobService, schedule sites), `alarm`
    (`AlarmManager.set*` sites with PendingIntent target), `timer` (schedule sites), `executor` (sites creating
    executors), `rx` (counts of subscribe/subscribeOn/observeOn sites per method).
17. `reflection`: sites of `REFLECTION_APIS` with resolved constant arguments; `javascript_interfaces`: objects
    passed to `addJavascriptInterface` with their class and its methods annotated `Landroid/webkit/JavascriptInterface;`.
18. `natives`: `[node or method key]` of ACC_NATIVE app methods (empty in the dataset).
19. `warnings`.

### 10.7 `INVENTORY.md`

Human-readable digest of the same facts, in this order: summary counts; components table (kind, class, exported,
launch mode, theme hint, filters, citation); entry points; per activity/fragment: layouts set or inflated (from
`setContentView`/`inflate` sites with resolved layout ids), views with ids and `onClick`, menus inflated (resolved menu
ids) with their items, registrations grouped by receiver view id; preference screens with keys and fragments;
component starts (caller → target); async constructs; reflection and JavaScript interfaces; framework-created classes;
unresolved items (dynamic intents, unknown listener classes, unresolved ids). Every line that states a fact ends with
its citation (`src/main/res/menu/main.xml:12`, `Main.java:288`, `APK res/layout/x.xml`).

## 11. Question 5: `build_graph.py` v2 (owner I; `build_graph.py` + `tglib/v2graph.py`)

### 11.1 CLI and mode selection

`python3 -I build_graph.py <graph_dir> <file_prefix> [--no-html] [--out DIR]`. `--no-html` skips the HTML file in both
modes; `--out DIR` writes the four outputs to DIR (created if missing) instead of `<graph_dir>/out/`. Unknown options:
usage message, exit 2.

Mode is decided before anything runs, by parsing `graph_def.py` with `ast` (utf-8):

- v2 mode iff the module's top-level statements contain exactly one assignment to `USE_AUTO` and it is
  `USE_AUTO = True` (an `ast.Assign` with the single target `Name('USE_AUTO')` and value `Constant(True)`).
- The opt-in name is `USE_AUTO` only (a bare `AUTO` variable has no meaning, so an existing graph_def.py that happens to
  define `AUTO` cannot opt in by accident).
- `USE_AUTO = False` or no assignment: v1 mode. A top-level `USE_AUTO` assigned anything other than a bool constant, or
  assigned more than once: exit 2. Assignments inside functions or branches are ignored (documented: must be top level).
- If `ast.parse` raises SyntaxError, v1 mode runs and fails exactly as v1 does today.
- v1 mode with a `parts/` directory containing a `*.py` file: exit 2, `parts/ requires USE_AUTO = True in graph_def.py`,
  nothing written (no graph dir has `parts/` today, so this cannot change an existing build).

### 11.2 v1 mode: byte-identical by construction

The v1 `main` of `work/tools/build_graph.py` is copied into the v2 file verbatim as `v1_main(gdir, prefix, outdir,
write_html)`, together with its helpers (`base`, `is_screen`, `param_names`, `method_names`, `bfs`, `path_to`,
`menu_label`, `gui_steps`, the constants). The only edits: `outdir` comes from the parameter (default
`<gdir>/out`), and the HTML block is guarded by `write_html`. v1 mode never reads `auto/`, never imports `tglib`, keeps
the v1 exec namespace (`e`, `SCREENS`, `DEAD`, `FRAMEWORK_ONLY`, `TITLE`, `NOTES`), the v1 report lines, the stdout text
and the exit code. Guarantee: for any graph dir that does not opt in, the JSON, `methods.csv`, the HTML and
`build_report.txt` are byte-identical to v1's, with or without an `auto/` folder, and so are stdout and the exit code.
The oracle is the v1 script itself, run on a snapshot of the same inputs (17.1), not the `out/` folders, which other
workflows may rewrite at any time; the template is the unchanged `viewer_template.html` next to the script. Builds made
by this workflow always use a temp graph dir or a temp `--out`; nobody runs `build_graph.py` on `graphs/Currency` or
`graphs/Diary` in place.

### 11.3 v2 inputs and options

v2 reads `<gdir>/auto/universe.json`, `calls.json`, `inventory.json`, `coverage_baseline.json`, then executes
`graph_def.py` and `parts/*.py` (12). It does not read `<gdir>/method_list.json` or `<gdir>/coverage_baseline.json`.
Missing auto files, a wrong `schema`, or a sha256 chain mismatch (calls/inventory/coverage must name the sha256 of the
`universe.json` bytes, calls must name the sha256 of `inventory.json`): exit 2, `run extract_app.py <App> first`.

`AUTO_OPTIONS` (graph_def.py only; optional dict; unknown keys or non-bool values: exit 2):

| Key | Default | Effect |
|---|---|---|
| `edges` | True | use any auto edges at all (False = v2 universe, checks and parts only) |
| `cha` | True | include `dispatch = cha` edges with `candidates >= 2` (False keeps exact and single-candidate edges) |
| `lambdas` | True | include `auto-lambda` edges |
| `callbacks` | True | include `auto-callback` edges |
| `generated` | True | include `auto-generated` edges |
| `clinit` | True | include `auto-clinit` edges |
| `register` | True | include auto REGISTER edges (they never affect reachability) |
| `uninstantiated` | False | also use the `excluded_candidates` records (CALL, review `uninstantiated`, `requires = []`, so liveness never prunes them; the `relies_on` flag `uninstantiated` marks paths through them) |
| `liveness` | True | prune edges whose receiver classes never become live (11.6) |

The auto list `ALL` is the calls.json `edges` in file order followed by the `excluded_candidates` records in file
order. A record x of `ALL` passes the option filter iff all of these hold: `edges`; `uninstantiated` or x is not an
excluded candidate; `cha` or not (`x.dispatch == 'cha'` and `x.candidates >= 2`); `lambdas` or
`x.origin != 'auto-lambda'`; `callbacks` or `x.origin != 'auto-callback'`; `generated` or
`x.origin != 'auto-generated'`; `clinit` or `x.origin != 'auto-clinit'`; `register` or `x.kind != 'REGISTER'`.

### 11.4 Merge semantics (manual wins)

Let `base(n) = n.split('@')[0]`. The directives `suppress`, `override` and `confirm` are matched against the full,
unfiltered `ALL` list (11.3), never against what is left after filtering or replacement, so a manual edge in one part
or an `AUTO_OPTIONS` change can never turn another part's directive into an error. Steps, in order:

1. Manual edges: every `e(...)` call from graph_def.py, then from each part file in sorted order, in definition order.
   A call that fails V7 is recorded as an error and its edge is dropped.
2. Directive matching. Each directive call is recorded with its file and line while the files run, and resolved after
   all files have run. A record x of `ALL` matches when `x.src == base(src)`, `x.dst == dst`, and, if given, `x.kind`
   equals the directive's `kind` (`suppress`) or `match_kind` (`override`, `confirm`). A `dst` containing `@` never
   matches (auto edges never end on variants). A directive that matches no record of `ALL` is V6. A directive whose
   `src` carries `@` names a variant that must exist (step 6); if it does not, V6 `unknown variant`.
3. Filter: keep the records of `ALL` that pass the option filter (11.3).
4. Manual wins: for every manual edge, the pair `(base(src), base(dst))` is a manual pair. Every kept record whose
   `(src, dst)` is a manual pair is removed, whatever its kind (`replaced`, with the id and file of the first manual edge
   of that pair).
5. Directives with a base `src`, applied to the surviving records they matched: `suppress` removes them (reason kept);
   `override` sets the given fields (the record's `overridden` lists `[file, field]` pairs); `confirm` sets
   `confirmed = true` and `confirm_note`. A matched record that step 3 filtered or step 4 replaced is not an error: the
   directive is listed in `build_report.txt` under `no-effect suppress/override/confirm` with the cause
   (`filtered by AUTO_OPTIONS['cha']`, `replaced by E012 (parts/20_settings.py)`, `suppressed by graph_def.py:40`).
6. Variant propagation: the variant set of X is X itself plus every node `X@C` that appears as src or dst of a manual
   edge. Each remaining record X → Y is materialised once per variant of X, with that variant as `src` and base Y as
   `dst`. Rationale: an auto edge is a context-free fact (X calls Y); whenever any context of X runs, Y can run. Auto
   edges never introduce variants and never touch pages.
7. Directives with an `@` src, applied to the one copy whose `src` is that variant, for each record they matched; a
   matched record without that copy (filtered, replaced or suppressed) is a no-effect listing as in step 5.
8. Liveness pruning (11.6).
9. Edge order and ids: manual edges first in definition order with ids `E001...` (`'E%03d'`, as v1), then auto copies
   sorted by `(src, dst, kind, origin)` with ids `A00001...` (`'A%05d'`).

Precedence: `suppress` beats `override` and `confirm` of the same record or copy (the losing directive is a no-effect
listing plus a warning). An `@`-src `override` is more specific than a base-src one and wins for its copy without a
conflict. Two overrides of the same specificity that set one field of one record to different values: V5 when they
come from different files; within one file the later call wins, with a warning. Equal values from different files: a
warning. `suppress` is idempotent; all reasons are kept.

Each surviving copy becomes a graph edge with the v1 fields (`gui = []`, `reads = writes = []`, `note = null`,
`needs_state = null`, `env = null`, `guard`, `trigger`, `evidence` from the record unless overridden) plus `origin`,
`dispatch`, `candidates`, `review`, `requires`, `consumer`, `confirmed`, `confirm_note`, `overridden`, `part = "auto"`.

The BFS, verdicts, paths, JSON and CSV then work on this one materialised list with v1's `bfs` function, which is the
same search the viewer runs, so the HTML shows the same paths as `methods.csv`.

### 11.5 Checks

v1 checks stay (unknown src/dst base node, bad kind, GUI must go page → method, ENTERS must end on a page, missing or
invalid evidence label, verdict for an unknown method, page not reachable from S_ENTRY, method with no path and no
verdict). v2 errors (reported in `build_report.txt`, outputs still written, exit 1, as v1 does for its errors):

| Id | Error |
|---|---|
| V1 | `CONTRADICTION`: a JaCoCo-reported method hit by APE or Monkey has verdict DEAD, FRAMEWORK_ONLY or UNRESOLVED |
| V2 | a DEAD or FRAMEWORK_ONLY method has an incoming non-REGISTER edge (manual or auto, after suppression and pruning) whose src is reached in the setup BFS; the fix is a `suppress(..., reason=...)` or a different verdict (Currency precedent: `Singleton.getList` is DEAD because its only call site is in a dead else-branch; in v2 the auto edge `ChartActivity.onCreate → Singleton.getList` must be suppressed with that reason) |
| V3 | a manual edge, verdict or note names a method that is not a universe node (for example an excluded `access$000`), or a verdict/note key carries `@` |
| V4 | `S_ENTRY` missing from SCREENS |
| V5 | conflicting declarations across files (12.3) |
| V6 | `suppress`/`override`/`confirm` that matches no record of the unfiltered `ALL` list (11.4 step 2) or names a variant that does not exist; `suppress` without a non-empty reason (so the plain `suppress(src, dst)` form is reported, not a crash); `kind`/`match_kind` not in KINDS; `override` with no field, an unknown field or an invalid value. A directive that matches records which were filtered, replaced or suppressed is not V6 (11.4 step 5) |
| V7 | API misuse caught at call time: wrong argument types for `e()` (src/dst non-empty str, kind in KINDS, trigger str, gui list/tuple of str, guard/note/needs_state/env str or None, reads/writes list/tuple of str, evidence str starting with a valid label), reported with the calling file and line; the edge is not added (so one bad call cannot also produce follow-up errors such as an unknown node) |

v2 warnings: v1's warnings (DEAD/FRAMEWORK_ONLY with incoming edges from unreached nodes), identical duplicates across
files (12.3), exact duplicate manual edges across different files, a part declaring a verdict or note for a method owned
by another part (12.4), auto edges whose review is `di-switch` on a shortest path.

### 11.6 Liveness pruning (RTA refinement, `AUTO_OPTIONS['liveness']`)

An auto copy with a non-empty `requires` (virtual dispatch over instantiated receivers) is traversable only if, for at
least one alternative, every hop's class list contains a live class. The live set is the least fixpoint, computed
upward from the classes that are live without any reachability (standard RTA), so a class whose only creation sites
are reachable only through dispatch on that class, or on a class it creates in turn, never becomes live:

```python
live = {c for c, r in instantiated.items() if r['always_live']}
def ok(x):
    return not x['requires'] or any(all(set(hop) & live for hop in alt) for alt in x['requires'])
for rounds in range(1, len(instantiated) + 2):
    E = manual_edges + [x for x in auto_copies if ok(x)]      # both lists in step-9 order
    prev = bfs(adjacency(E), allow_setup=True, allow_env=True) # v1's bfs, most permissive mode
    reached = {base(n) for n in prev}
    grown = live | {c for c, r in instantiated.items() if reached & set(r['sites'])}
    if grown == live:
        break
    live = grown
else:
    raise InternalError('liveness did not converge')         # impossible: live grows every round; exit 3
```

`E` of the last round is the final edge list: verdicts, paths, the JSON and the CSV all use it. Auto copies not in `E`
are `pruned (receiver class never live)`: left out of the JSON and listed in the report with their required classes.
`live` only grows, so the loop ends within `len(instantiated) + 1` rounds; the report prints the number of rounds
(expected well below 30: it is the length of the longest chain "class live → edge opens → creation site of the next
class reached"). With `AUTO_OPTIONS['liveness'] = False`, `E` = all manual edges and auto copies.

Liveness is flow-insensitive, like RTA: a class created anywhere on any reachable path (including setup and `env`
paths, because the most permissive BFS is used) counts as live for every dispatch site. Effect: a method reachable only
through dispatch on a class whose every creation site is itself unreachable is not reported REACHABLE; it stays
UNRESOLVED, which is loud, rather than falsely reachable.

Unit tests (`test_build_graph_v2.py`, synthetic `auto/` files): (1) class C whose only creation site is in `C.split`,
reached only through an edge requiring C: `C.split` UNRESOLVED and the edge pruned; (2) classes A and B where `A.m`
creates B and `B.n` creates A, each reached only through an edge requiring its own class: both UNRESOLVED; (3) the same
as (1) plus a manual path to a method that creates C: `C.split` REACHABLE, in three rounds (C becomes live, the edge
opens, nothing grows); (4) an `always_live` class
opens its edges in round 1; (5) on 50 random graphs with at most 6 classes (fixed seed `random.Random(7)`), `live`
equals the intersection of every class set L with F(L) ⊆ L, where F(L) = always-live ∪ classes created in nodes
reached with the edges L allows (the Knaster-Tarski least fixpoint, found by enumerating all subsets).

### 11.7 Outputs

- JSON `<prefix>_trigger_graph.json`: keys `title`, `screens`, `methods` (universe nodes, universe order), `verdict`,
  `dead`, `framework_only`, `edges`, then `meta` (`mode: "v2"`, the four input sha256s, `parts` (relative file names),
  `options` (effective AUTO_OPTIONS), `auto` (counts: in `ALL`, filtered, replaced, suppressed, overridden,
  confirmed, no-effect directives, variant copies, pruned, used; `liveness_rounds`)). No timestamps or absolute paths,
  so the bytes are deterministic. Edges carry v1's fields plus `origin` (`manual` or the auto origin), `part`, and for
  auto edges `dispatch`, `candidates`, `review`, `confirmed`, `confirm_note`, `overridden`, `consumer` (`requires` is not
  written).
- `methods.csv`: the 10 v1 columns first, same order, same formatting rules (`steps_from_launch`, `gui_steps_on_shortest_path`
  via v1's `gui_steps`, `shortest_path` joined with ` > `, `incoming_edges` = non-REGISTER edges into any variant,
  `note` as v1 including `needs environment: ...`, `jvm_descriptor`, `monkey_hit`/`ape_hit` = `1`/`0`, blank when the
  method is not JaCoCo-reported). Appended columns: `class` (internal name), `jacoco_reported` (1/0),
  `generated` (1/0), `generated_kind`, `candidate_target` (1 when the verdict is REACHABLE or REACHABLE_AFTER_SETUP, the
  method is JaCoCo-reported and neither APE nor Monkey hit it; 0 otherwise; blank when not JaCoCo-reported),
  `relies_on` (`;`-joined flags of unconfirmed inferred edges on the shortest path, in this order: `cha` = dispatch cha
  with candidates >= 2, `rta` = dispatch cha with one candidate, `lambda` = auto-lambda/auto-callback edge of kind ASYNC
  or CALL, `generated` = auto-generated, `di-switch`, `clinit` = auto-clinit, `uninstantiated` = an
  `excluded_candidates` record),
  `auto_in` (incoming auto edges), `source_file`, `first_line`.
- `<prefix>_trigger_graph.html` unless `--no-html`: the unchanged `viewer_template.html` with `/*DATA*/` replaced as v1.
- `build_report.txt`: v1's lines first (same wording), then v2 sections: `mode v2` line with the input hashes and edge
  accounting; `candidate targets` (count and list grouped by class, labelled `not hit in coverage segments 1..N; launch segment
  00000 is not in merged.ec`), plus the count of REACHABLE methods that Monkey missed but APE hit (the draft's Table III
  split); `shortest paths relying on unconfirmed inferred
  edges` (count per flag, method lists for cha, lambda, generated, di-switch, uninstantiated; rta and clinit as
  counts); `framework-callback
  overrides with no incoming edge` (from `inventory.classes[*].callbacks` and `listener_callbacks`, then structural
  `ext_override` candidates separately, each with its verdict); `review-flagged auto REGISTER edges` (count per review
  reason); `excluded uninstantiated CHA candidates` (count from calls.json); `pruned by liveness` (count, rounds, top
  classes, then every pruned copy with its required classes); `replaced / suppressed (with reasons) / overridden /
  confirmed auto edges`; `no-effect suppress/override/confirm` (each directive with file, line and cause, 11.4);
  per-part table (edges, pages, verdicts, owned methods, owned UNRESOLVED) when parts exist; then `errors: N` and
  `warnings: N` with all items.

### 11.8 Performance (target ~5,000 methods, ~40,000 edges)

Adjacency lists built once; `first_variant` computed in one pass over each BFS's discovery order instead of v1's
per-method scan; page reachability via a set of reached bases; liveness rounds reuse the same BFS. Budget: under 30 s
and under 1 GB for 5,000 methods and 40,000 edges including JSON and CSV (estimated JSON size about 18 MB; use
`--no-html` for the largest apps if the viewer is too slow). An integration test builds a synthetic graph of that size,
including a 30-class instantiation chain (30 liveness rounds, one BFS each), and checks the time budget.

## 12. Question 6: `parts/` layout and the graph-definition API

### 12.1 Layout

```
graphs/<App>/
  graph_def.py      required: TITLE, USE_AUTO = True, AUTO_OPTIONS, shared constants and helper functions, global pages
  parts/            optional: one file per feature area, executed after graph_def.py in sorted file-name order
    10_main.py
    20_settings.py
  auto/             written only by extract_app.py; read-only for modelers
  out/              build outputs
```

Part files: names matching `^[0-9A-Za-z][0-9A-Za-z_.-]*\.py$`, sorted by Python string order. Entries of `parts/` whose
name starts with `_` or `.` (files or directories, e.g. `__pycache__`) are ignored; shared code lives in graph_def.py.
Every other entry must be a regular file: a subdirectory, or a `*.py` file whose name fails the regex, is exit 2
(`parts/<name>: not a valid part file`, nothing written), so a part written by a parallel agent cannot silently vanish.
Other files (`notes.md`, `20_settings.py.bak`) are ignored and listed in `build_report.txt`. One agent owns one part
file; nobody edits another agent's part.

### 12.2 Namespace and API (v2 mode)

Each file runs in a fresh namespace containing:

- `e(src, dst, kind, trigger, gui=(), guard=None, reads=(), writes=(), note=None, needs_state=None, evidence=None,
  env=None)` exactly as v1, plus argument validation (V7). Edges are attributed to the file being executed, even when
  `e` is called from a helper defined in graph_def.py (the builder tracks the current file).
- `suppress(src, dst, reason=None, kind=None)` (a missing or empty `reason` is V6, so `suppress(src, dst)` is reported
  rather than raising `TypeError`), `override(src, dst, match_kind=None, **fields)`,
  `confirm(src, dst, match_kind=None, note=None)` (11.4); allowed override fields: `kind` (CALL, ASYNC, REGISTER,
  FRAMEWORK, INTENT, RESULT, LIFECYCLE, SYSTEM), `trigger`, `guard`, `reads`, `writes`, `note`, `needs_state`, `env`,
  `evidence`. Directives never raise for bad values; they record V6 (wrong argument types, such as a non-str `src`,
  also record V6 with file and line).
- Fresh `SCREENS`, `DEAD`, `FRAMEWORK_ONLY`, `NOTES` dicts for this file.
- Read-only data: `METHODS` (tuple of universe nodes), `INFO` (mapping node → read-only record: `class`, `name`,
  `desc`, `source_file`, `line`, `jacoco_reported`, `monkey`, `ape`, `generated`, `generated_kind`, `ext_override`),
  `AUTO` (the full `ALL` list of 11.3 as a tuple of read-only records, unfiltered and before replacement, the same set
  the directives match against; `x['review'] == 'uninstantiated'` marks the excluded candidates), `INVENTORY` (a deep
  copy of inventory.json per file), `PART` (this file's relative path).
- In part files only: every public name defined by graph_def.py (not starting with `_`, not an API name, not
  `SCREENS`/`DEAD`/`FRAMEWORK_ONLY`/`NOTES`/`TITLE`/`USE_AUTO`/`AUTO_OPTIONS`) as a top-level name, shared by reference
  (treat as constants), and the optional `OWNS` list a part may set.
- graph_def.py additionally sets `TITLE`, `USE_AUTO`, `AUTO_OPTIONS`.

Part files can loop over `METHODS`, `INFO`, `AUTO` and `INVENTORY` to model in bulk (for example all data-binding
`executeBindings` methods, or INTENT edges from `INVENTORY['component_starts']`).

### 12.3 Merge and conflict rules

- `TITLE`, `USE_AUTO`, `AUTO_OPTIONS` set in a part file: error V5.
- `SCREENS`, `DEAD`, `FRAMEWORK_ONLY`, `NOTES`: union over files; the same key in two files with identical text is a
  warning, with different text an error; the same method in DEAD and FRAMEWORK_ONLY (any files) is an error.
- graph_def.py's own dicts are snapshotted after it runs; if a helper called from a part mutates them, that is an error
  (declarations belong in the part's own dicts).
- Edges are concatenated in file order; exact duplicates across files are a warning (both kept, as v1 keeps duplicates).
- Directives: the precedence and conflict rules of 11.4 (two files overriding one field of one record with different
  values at the same specificity: V5; equal values: warning; `suppress` beats `override`/`confirm`; `suppress` is
  idempotent and keeps every reason). A directive whose target another part's manual edge replaced, or an option
  filtered, is a no-effect listing, never an error.
- An exception while executing a file: `build_graph: ERROR: <file> raised <exception>` plus the traceback on stderr,
  exit 2, nothing written.

### 12.4 Ownership (`OWNS`)

A part may set `OWNS = ['org/proninyaroslav/libretorrent/ui/settings/', ...]` (internal-name prefixes). Two parts
owning the same universe method is an error V5. The report lists per part its edges, pages, verdicts, owned methods and
owned UNRESOLVED methods, and the methods no part owns (when any part declares OWNS). A verdict or note for a method
owned by another part is a warning.

### 12.5 Example

```python
# graphs/LibreTorrent/graph_def.py
TITLE = 'LibreTorrent 3.5.2 trigger graph'
USE_AUTO = True
AUTO_OPTIONS = {'cha': True}
ENV_NET = 'network available'
SCREENS = {'S_ENTRY': 'Outside the app', 'S_EXIT': 'App finished', 'S_MAIN': 'MainActivity, torrent list'}

# graphs/LibreTorrent/parts/20_settings.py
OWNS = ['org/proninyaroslav/libretorrent/ui/settings/']
SCREENS['S_SETTINGS'] = 'SettingsActivity, root preference screen'
e('S_MAIN', 'MainActivity.onOptionsItemSelected@MAIN', 'GUI', 'Tap a menu item', gui=['Tap the overflow menu'],
  evidence='SRC MainActivity.java:210')
suppress('SettingsFragment.onCreatePreferences', 'SettingsFragment.debugOnly', reason='branch needs BuildConfig.DEBUG')
override('SettingsFragment.onResume', 'SettingsFragment.refresh', needs_state='second visit in the same process')
for x in AUTO:
    if x['review'] == 'reactive' and x['src'].startswith('SettingsFragment.'):
        # match_kind limits the change to the reactive REGISTER record, not every auto edge of the pair
        override(x['src'], x['dst'], match_kind=x['kind'], kind='ASYNC', guard='the LiveData emits a value')
```

## 13. Extraction driver and summaries (`extract_app.py`, owner I)

```
python3 -I extract_app.py <App> [<App> ...] | --all  [--dataset DIR] [--graphs DIR] [--stages universe,inventory,calls,coverage] [--allow-unexplained]
python3 -I extract_app.py --summary [--graphs DIR]
python3 -I extract_app.py --crosscheck <App> --hand <graph json>
```

Defaults: `--dataset <script dir>/../final_java_only`, `--graphs <script dir>/../graphs` (both resolve correctly from
`tools_dev/` and from `tools/`). Per app, stages run in pipeline order (4.2) into `<graphs>/<App>/auto/` (created if
missing; for Diary and Currency this is the only folder written). Every write goes through `jsonio.write_json` or
`write_text` with `allowed_root = <graphs>/<App>/auto` (4.2 rule 5), so `guard_path` resolves symlinks and raises
`ProtectedPathError` (exit 4) for any target outside that folder. With several apps or `--all` the driver continues
after a failing app, prints a per-app status table, and exits 1 if any app failed (0 if none; a usage error is still 2).
With one app it exits with that app's code.

Outputs per app: `universe.json`, `inventory.json`, `INVENTORY.md`, `calls.json`, `coverage_baseline.json` and
`extract_report.txt`. The aligned `coverage_baseline.json` (schema `tg-coverage/1`): `schema`, `app`,
`universe_sha256`, `reports` (relative paths), `note` (`merged.ec covers coverage segments 1..N; the launch dump
(segment 00000) is not included, so some first-launch code can look unhit`), `methods` in universe order with `node`,
`class`, `name`, `desc`, `jacoco_reported`, `monkey`, `ape` (true when the METHOD counter's `covered > 0`, as v1
`coverage_methods.py`; null when not JaCoCo-reported). `extract_report.txt` holds counts, warnings, output sizes and
per-stage wall times; it is the only non-deterministic output.

`--summary` prints, from existing `auto/` folders, the per-app table for `graphs/AUTO_SUMMARY.md` (universe size and
reconciliation counts, classes, components by kind, layouts, menus, preference screens, registration sites, component
starts, auto edges by origin and dispatch, excluded candidates, baseline hits Monkey/APE/either, JaCoCo-reported
methods hit by neither, runtime, output size) and, for every app above 1,000 universe methods (Omni-Notes,
Vanilla-Music, AnyMemo, Markor, AmazeFileManager, Aegis, AnkiDroid, MMEX, LibreTorrent), a package table (method counts,
activities/fragments/services, auto-edge counts between packages) that the integration agent uses to write the 3-8
feature-area split proposals by hand (packages and components per area, method counts, owned activities/fragments,
owner of shared infrastructure, what still needs manual modelling; informed by `.agents/tasks/ui-map-<App>.md` when
present, never edited).

`--crosscheck` compares the method → method edges of a hand-built graph JSON (read-only) with the app's auto edges by
base pair and prints a markdown skeleton: hand CALL/ASYNC/REGISTER pairs missing from auto, auto pairs missing from the
hand graph, kind disagreements. The integration agent completes it with an explanation per row (framework-mediated,
RTA/CHA miss, extractor bug, real call the hand graph missed, false positive) as `graphs/Currency/auto/crosscheck.md`.

## 14. Error handling

| Operation | Failure | Recoverable? | Caller receives | Logged |
|---|---|---|---|---|
| `appdata.load` | missing/malformed `class_files.json`, class dir or APK missing | fatal for the app | `AppDataError`; CLI exit 2, nothing written | stderr ERROR |
| `classfile.parse_class` | bad magic, unknown constant tag, length mismatch | fatal for the app (dataset is fixed, so it is a bug) | `ClassFormatError(path, offset)`; exit 3 | stderr ERROR with path and offset |
| `bytecode.decode`/`analyze` | invalid opcode, bad branch target, stack-height mismatch, jsr/ret | fatal for the call graph | `MethodFacts.failed`; `callgraph.py` lists all failures in `calls.json.failures`, exits 3 | stderr ERROR per method |
| JaCoCo reports | missing file / XML parse error / method without name or desc | fatal | exit 2 | stderr ERROR |
| universe reconciliation | JaCoCo method excluded by a rule or missing from class dirs; unexplained method; naming collision | fatal (unexplained: recoverable with `--allow-unexplained`) | exit 3, every case listed | stderr ERROR; with the flag a warning in `universe.json` |
| APK zip | `BadZipFile`, missing `resources.arsc` or manifest | fatal for the inventory | exit 2 | stderr ERROR |
| AXML/ARSC decode | malformed manifest or arsc | fatal | `AxmlError`; exit 3 | stderr ERROR |
| AXML decode of one res file | malformed chunk | recoverable | resource recorded with `error`, others continue | warning in `inventory.json` |
| source XML (expat) | parse error | recoverable | APK content used for that resource, `origin: "apk"` | warning |
| stale or missing upstream JSON | sha256 mismatch, wrong schema, missing file | fatal | exit 2 `stale input` / `run extract_app.py first` | stderr ERROR |
| `build_graph` v1 mode | anything | as v1 | as v1 (errors listed, exit 1) | as v1 |
| `build_graph` v2 configuration | bad `USE_AUTO`/`AUTO_OPTIONS`, parts without opt-in, auto inputs missing/stale, exception in a definition file | fatal | exit 2, nothing written | stderr ERROR with file, line, traceback |
| `build_graph` v2 graph content | V1-V7 and v1 checks | build completes | outputs written, exit 1 | `build_report.txt` errors section |
| `build_graph` v2 `parts/` scan | subdirectory or badly named `*.py` in `parts/` (12.1) | fatal | exit 2, nothing written | stderr ERROR naming the entry |
| internal invariants | duplicate edge ids, liveness exceeding `len(instantiated) + 1` rounds (impossible by construction, 11.6), unknown node after merge | fatal | exit 3 | stderr ERROR |
| any output write | permission, disk full, protected path | fatal | exit 4; temp file removed; previous file untouched (atomic replace) | stderr ERROR |

## 15. Validation of external inputs

- CLI: app names must name a folder with `app/class_files.json`; `graph_dir` must contain `graph_def.py`; in v2 mode
  the prefix must match `^[A-Za-z0-9_-]+$` (v1 mode keeps v1's behaviour); `--stages` values from the fixed list. Failure:
  usage message, exit 2.
- `class_files.json`: exactly one key; `classfiles` and `sourcefiles` non-empty lists of relative paths that exist.
- JaCoCo XML: `class@name` and `method@name`/`method@desc` required; `counter@covered` an int; else exit 2.
- JSON inputs: `schema` must equal the expected string; required top-level keys present with the right container types;
  node names unique; else exit 2.
- graph-definition API (v2): V6 and V7 in 11.5; `AUTO_OPTIONS` keys from 11.3 with bool values; `OWNS` a list of
  non-empty strings; `parts/` entries as in 12.1 (exit 2).
- Output locations: the standalone CLIs' `--out`/`--md` must lie in a directory named `auto`; `build_graph.py` v2's
  `--out` must not resolve inside `<gdir>/auto` or the dataset root; else exit 2 before anything runs (4.2 rule 5).
- Hard limits (documented, enforced in code): Value size 16 tokens; parameter-flow depth 3; collapse depth 8; bridge
  re-selection depth 2; `requires` alternatives 10; `ext_calls` 40 per method; `sites` 20 per edge; evidence lines 5;
  interpreter re-processing 64 per block; liveness rounds `len(instantiated) + 1` (a convergence bound, not a
  tuning knob).

## 16. Invariants and who enforces them

| Invariant | Enforced by | Why there |
|---|---|---|
| Node names unique, no `@`/whitespace, class part without `.`; Currency/Diary names unchanged | `naming.py` (assert), re-checked by `build_graph` v2 load | names are created once; every consumer copies them |
| Universe ⊆ class-dir methods with code; every JaCoCo method in universe or X1-X3 | `universe.py` | only place that sees both sources |
| No auto edge touches a non-universe node, a variant or a page | `callgraph.py` (assert before writing), `build_graph` re-check | producer owns correctness, consumer guards against stale files |
| Uninstantiated candidates never become graph edges by default | `callgraph.py` (separate list), `build_graph` (reads them only with `uninstantiated`) | keeps RTA precision visible and reversible |
| Liveness is the least fixpoint (no self-justifying instantiation cycles) | `v2graph.py` (11.6 upward iteration) + its unit tests | only the builder sees manual and auto edges together |
| A directive's validity does not depend on other files or on `AUTO_OPTIONS` | `v2graph.py` (11.4: matching against the unfiltered `ALL`) | parts are written in parallel by different agents |
| Library-created and framework-created classes are always live | `callgraph.py` (9.2 sources 3-6, from `inventory.framework_created` and the class dirs) | the producer of `instantiated` owns its completeness |
| v1 mode output identity | `build_graph.py` dispatcher (v1 code path verbatim) + regression test | identity is a property of the code path |
| Inputs belong together | sha256 chain checked by every consumer | stale `auto/` files cannot silently mix |
| Protected paths never written | `jsonio.guard_path` in every v2 writer; install procedure | one choke point for all writes |
| Determinism | sorted iteration everywhere (no set or dict order from unsorted sources leaks into outputs); tests build twice and compare bytes | outputs are compared byte for byte |

## 17. Testing

Unit tests (stdlib `unittest`, `python3 -I -B -m unittest discover -s tests -t .` from `tools_dev/`, or from
`work/tools/` after install; dataset and graph files are read in place, read-only; everything a test writes goes to a
`tempfile.mkdtemp()` folder that the test removes):

- A's tests that need framework creation or resource names (the Currency, Aegis and LibreTorrent acceptance cases) read
  a hand-written inventory fixture in `tests/fixtures/analyzer/` that holds only the fields `callgraph.py` consumes
  (4.2: `framework_created` for the manifest components, the needed `res_ids`, `fw_res_ids`), so A never waits for B;
  the integration step reruns the same cases on B's real `inventory.json` and records them in
  `verify_integration.txt`.
- A: `test_classfile.py`: every constant tag and attribute on real classes (Currency `ChartActivity.class` with two
  switches, three `showToast` overloads and a lambda; one class each of majors 51, 52, 55, 61); modified UTF-8. 
  `test_bytecode.py`: hand-assembled byte strings for every opcode length class, tableswitch/lookupswitch at all four
  `pc % 4` paddings, `wide` iload and iinc, multianewarray, invalid opcodes, bad targets; interpreter tokens through
  dup/swap/stores, joins, the 16-token cap, case labels; real methods with `access$` accessors (Diary), anonymous classes
  (Vanilla-Music), method references kinds 5/8/9 (Markor, Aegis, LibreTorrent), `wide` (hash-checker, AmazeFileManager).
  Case labels: switch keys sharing one target keep all keys, the default target, `if_icmpeq` and `if_icmpne` with an
  int and with a `('res', 'id', n)` operand (equal successor labelled, not-equal successor keeps the incoming label),
  joins of different labels; `('param', i)` ordinals with long/double parameters; a local missing in one predecessor;
  two LineNumberTable attributes in one Code attribute (synthetic).
  `test_appdata.py`: module roots (openlauncher's three `app/libs/*` modules, MMEX's four), variant source sets
  (AmazeFileManager `fdroidDebug` → `debug`, `fdroid`, `main`; hash-checker `thirdPartyStoresDebug` → `debug`,
  `thirdPartyStores`, `main`; LibreTorrent `baseDebug` → `debug`, `main`), test sets never candidates, `find_source`
  ranks including Markor's `app/thirdparty/java/` (rank 2).
  `test_naming.py`: Currency's 145 and Diary's 286 names equal v1's `method_names` (from `tests/v1ref.load_v1()`)
  applied to their `method_list.json`; AnkiDroid `api/Utils` vs `libanki/Utils`;
  LibreTorrent `drawer/TagItem`; the `GlideApp.with(...)` fully-qualified fallback; synthetic clash cases (nested
  classes, package-suffix ties). `test_universe.py`: the section 3 counts for all 13 apps (integration-level, a few
  seconds each), zero unexplained, Currency/Diary set equality with `method_list.json`, X10 vs enum constant bodies,
  the `excluded` list membership of 6.2.
  `test_callgraph.py`: the Currency, Aegis and source-6 acceptance cases (9.7), accessor collapsing (Diary), bridge
  re-selection, `select` skipping private and other-package package-access declarations (synthetic), private nestmate
  calls (a 61 class), uninstantiated candidates kept apart (synthetic hierarchy), consumer lookup through `resolve`'s
  external type (synthetic `AlertDialog$Builder` subclass), event 5 before the table (`List.add` gives `collection`),
  the anonymous-class exception after an event-2 hop, the Dagger acceptance methods (9.5), clinit edges, `SRC` versus
  `INFERRED bytecode ... (generated, no source in checkout)` evidence, determinism (two runs, same bytes).
- B: `test_axml.py`: Currency's APK manifest gives exactly 10 components (activities Main (launcher), ChartActivity,
  ChoiceDialog, HelpActivity, SettingsActivity, CurrencyWidgetConfigure, CurrencyWidgetRefresh (Theme_NoDisplay);
  service CurrencyWidgetUpdate; receivers CurrencyWidgetProvider and the harness receiver) and an `<application>`
  without a custom class; arsc entry counts (Currency 250, LibreTorrent 6557,
  AnkiDroid 2796, Aegis 6492); sparse/offset16 type chunks, `FLAG_COMPACT` entries and skipped 0x0203-0x0206 chunks on
  synthetic bytes; synthetic R.txt/R.jar/R-class fallbacks.
  `test_resources.py`: Currency menus `main`, `select`, `navigation` item ids; preferences keys; source line citations.
  `test_inventory.py`: all 10 Currency components cite `Currency-#v1.58/src/main/AndroidManifest.xml` at the start-tag
  lines 18, 28, 30, 34, 38, 42, 51, 55, 58, 69 (dot-less names resolved through the `build.gradle` namespace; the
  harness receiver at 69); Aegis components cited through the suffix rule (no `package`, no literal namespace);
  `application-attr` entries for Aegis `AegisBackupAgent` and MMEX `MoneyManagerBackupAgentHelper`; Currency
  `Main.onCreate` registrations (`setNavigationOnClickListener` lambda, `setOnClickListener(this)` with view ids,
  `addTextChangedListener(this)`), Diary layouts and view ids, Aegis `getstatic R$id` names resolved through the reverse
  map, ButterKnife view ids assigned in `*_ViewBinding.<init>` (Omni-Notes), the 99% id-resolution check,
  component-start targets for Currency, `fw_res_ids` present.
- I: `test_build_graph_v1compat.py`: the oracle of 17.1 for Currency (gate: A and B identical; A against
  `graphs/Currency/out/` reported), plus a synthetic v1 graph dir with an `auto/` folder. `test_build_graph_v2.py` on
  synthetic graph dirs in `tests/fixtures/graphs/`: manual wins; directives matched against the unfiltered `ALL`
  (a manual edge in part A plus a `suppress` of that pair in part B is a no-effect listing, not V6; turning
  `AUTO_OPTIONS['cha']` off turns an existing `override` of a cha edge into a no-effect listing; no match is V6;
  `suppress(src, dst)` without a reason is V6; an unknown `@` variant is V6; `suppress` beats `override` with a warning;
  `match_kind` limits an override to one record); variant propagation; the liveness tests of 11.6; V1-V7 (a V7 call
  adds no edge); parts merge and conflicts; invalid `parts/` entries (exit 2); OWNS; `--no-html`; CSV columns;
  determinism (two builds, same bytes); the 5,000-method/40,000-edge performance budget.
  `test_extract.py`: guard_path refusals, sha chain checks, aligned coverage rows, `--all` exit 1 with one failing app
  (synthetic dataset dir).

### 17.1 v1 reference and the v1-compatibility oracle

`tests/v1ref.py` (owner A) provides `V1_SHA256` (section 3), `v1_script()` and `load_v1()`. With `<root>` the folder
that contains `tests/` (`tools_dev/` or, after install, `tools/`) and `<work>` its parent, `v1_script()` returns the
first of `<root>/_backup_v1/build_graph.py`, `<work>/tools/_backup_v1/build_graph.py`, `<work>/tools/build_graph.py`
that exists and whose sha256 equals `V1_SHA256['build_graph.py']`; if none does, the calling test fails with
`v1 reference script not found`. `load_v1()` returns the dict obtained by `exec(compile(source, path, 'exec'), ns)` with
`ns = {'__name__': 'v1_build_graph', '__file__': path}` (no import, no bytecode file, `main` not run).

The oracle for one graph dir G (Currency in the unit suite; Diary only in integration and install verification):

1. Snapshot: copy `G/graph_def.py`, `G/method_list.json` and `G/coverage_baseline.json` into `<tmp>/<App>/`.
2. A: run the v1 script on the snapshot, `[sys.executable, '-I', '-B', v1_script(), '<tmp>/<App>', <prefix>]` with
   `cwd=<tmp>`; it writes `<tmp>/<App>/out/`. Keep stdout and the exit code.
3. B: run the v2 `build_graph.py` under test on the same snapshot with `--out <tmp>/B`. Keep stdout and the exit code.
4. B': add `<tmp>/<App>/auto/` holding a deliberately invalid `universe.json` and run the v2 file again with
   `--out <tmp>/B2`: v1 mode must ignore `auto/`.
5. Gate (test failure if violated): A, B and B' are byte-identical in all four files (`<prefix>_trigger_graph.json`,
   `methods.csv`, `<prefix>_trigger_graph.html`, `build_report.txt`), and their stdout and exit codes are equal.
6. Report only (not a failure): A compared with `G/out/`. For Currency they matched at design time (section 3); a
   difference is reported as `Currency out/ is stale relative to its inputs (pre-existing)`. For Diary a difference is
   reported as `Diary out/ is stale (concurrent hand build)`. If the Diary snapshot does not build (a concurrent edit
   caught mid-way), A and B fail alike, the comparison still runs, and the result is recorded as such.

Prefixes: `currency` for Currency, `diary` for Diary (the existing `out/` file names). Nothing is written outside
`<tmp>`, which the test removes.

Integration evidence (recorded in `verify_integration.txt`): all 13 apps extracted without exceptions (times, sizes);
the 17.1 oracle for Currency and Diary; the Currency cross-check (`crosscheck.md`: hand edges missing from auto and
auto edges missing from the hand graph, each explained, extractor bugs fixed); the LibreTorrent source-6 liveness check
(9.7); spot checks of 10 random methods in each of Diary, Vanilla-Music and LibreTorrent (extracted callees against
source lines); the full unit suite result.

## 18. Install (last step, owner of the install step)

1. Copy every current file of `work/tools/` except `__pycache__/` to `work/tools/_backup_v1/` unless that folder already
   holds them (never overwrite a backup); check the copies against `V1_SHA256` before going on.
2. For each file to install (`build_graph.py`, `extract_app.py`, `README.md`, `tglib/*.py`, `tests/**`): write
   `<target>.tmp-<pid>` in the target's directory, then `os.replace` onto the target. `list_methods.py`,
   `coverage_methods.py` and `viewer_template.html` are byte-identical in `tools_dev/` and are left untouched.
3. Verify with the installed files: the four `_backup_v1/` files and the untouched `list_methods.py`,
   `coverage_methods.py`, `viewer_template.html` match `V1_SHA256`; `list_methods.py` and `coverage_methods.py`
   reproduce Currency's `method_list.json`/`coverage_baseline.json` content in a temp folder; the 17.1 oracle passes
   for Currency (gate) and Diary (gate on A, B and B' only), with `v1_script()` now resolving to
   `_backup_v1/build_graph.py`; the unit suite (`python3 -I -B -m unittest discover -s tests -t .`) passes from
   `work/tools/`.
4. Remove temp folders. Check that `handoff/HANDOFF.md` has the "Tooling v2" section. The integration step appends that
   section (once: it first checks that the heading is absent) without rewriting existing sections; the install step
   never writes `HANDOFF.md`.

## 19. Out of scope and backlog

- Auto INTENT/RESULT/LIFECYCLE edges: the inventory lists component starts with targets; modelers (or a part-file loop
  over `INVENTORY['component_starts']`) write those edges. Reason: the edge semantics depend on launch modes, results and
  back-stack state that the extractor does not model.
- Hilt `SwitchingProvider` binding-id refinement (flagged `di-switch` instead); field-sensitive points-to outside
  generated code; lambdas as dispatch candidates; reflection or string-based dispatch beyond constant arguments.
- Exact external-override detection (needs framework class files, which are not available); `ext_override` stays a
  structural candidate confirmed by the curated callback table.
- Flow-sensitive liveness (a separate live set per BFS mode, so a class created only after setup cannot make a no-setup
  path REACHABLE). Reason: RTA is flow-insensitive by definition and the JSON would need per-mode edge lists; 11.6
  documents the effect.
- Labels for `||` conditions (`if (id == R.id.a || id == R.id.b)` joins two labels into none, 8.3) and string
  switches (`case <hash>` keys). Reason: needs value-keyed label merging; the guard is then missing, never wrong.
- Instantiation sources beyond 9.2 (JSON deserialisers, `Parcelable.Creator`, `ServiceLoader`, non-constant
  `Class.forName`). Reason: no generic static signal; the affected targets stay visible as excluded candidates or
  pruned edges.
- CSV presentation issues reported by the Diary hand build (`graphs/Diary/TOOL_ISSUES.md`: an env-dependent shortest
  path printed without a note when an env-free path exists; `menu_label` only knows `action_*` ids; only `gui[0]` and
  no `needs_state` text in `gui_steps_on_shortest_path`; evidence counted by first label). Reason: v2 keeps the 10 v1
  columns with v1's semantics so v1 and v2 graphs read the same; changing them, or adding columns for them, is a
  decision for the study owner. Recorded so the integration step can raise it in `HANDOFF.md`.
- Emulator verification, framework source checks, Kotlin, apps outside the 13.

## 20. Review log

Iteration 0: `design_review.json` did not exist and no DESIGN.md had been written by the design step, so the first
version was a complete design rather than a tightening pass.
Orchestrator notification received during that step: (1) collapse call chains through excluded generated Dagger/Hilt
code into direct edges with evidence `INFERRED via generated Dagger code <class>`, covering `@Provides` methods,
`@Inject` constructors, members injection and Hilt base classes: specified in 9.5 with measured acceptance cases;
(2) `merged.ec` omits the launch segment 00000: no tool change, recorded in section 3 and carried into the
`coverage_baseline.json` note and the candidate-target report label (11.7).

Revision 1 (answers `design_review.json`, review iteration 0, verdict CHANGES_REQUESTED). All 23 findings are
addressed; none is backlogged or rejected, and none changes what the tooling delivers against the brief. New facts
checked for this revision are in section 3 (v1 reproduces Currency `out/`; source manifests; library-created classes).

| # | Sev | Response |
|---|---|---|
| 1 | HIGH | Addressed (11.6): liveness is now the least fixpoint, computed upward from `always_live` with the reviewer's loop; bound `len(instantiated) + 1` rounds replaces the fixed 50 (11.6, 14, 15); unit tests for a self-instantiating class, a two-class cycle (both UNRESOLVED), a class created on a reachable path (REACHABLE), and a Knaster-Tarski brute-force comparison; invariant row in 16; flow-insensitivity documented. |
| 2 | MEDIUM | Addressed: 9.2 source 5 extended to `generated_kind = butterknife`; new source 6 `library-created:<creator>` (creators: any `DataBinderMapperImpl`, `GeneratedAppGlideModuleImpl`, ButterKnife classes; one level); `framework_created` source `application-attr` for `android:backupAgent` and `android:appComponentFactory` (9.2 source 3, 10.6 item 13, attribute ids in 10.2); 6.4 data-binding text corrected; acceptance in 9.7 (A: every LibreTorrent `*BindingImpl` always live; I: no edge into a `*BindingImpl` method pruned). |
| 3 | MEDIUM | Addressed (8.3, 9.7, 10.3): labels are `('case', keys, pc)` with int or `('res', t, n)` keys; `if_icmpeq`/`if_icmpne` against a single key token label the equal successor, the not-equal successor keeps the incoming label; switch keys sharing a target keep all keys; guard texts `case R.<t>.<n>`, `case android.R.<t>.<n>` (via the new `inventory.fw_res_ids`, because A cannot import B's table), `case <k>`, `default`; the `switch case R.id.<name>: ` trigger prefix for id keys from either source; Aegis acceptance `MainActivity.onOptionsItemSelected → MainActivity.startPreferencesActivity()` with guard `case R.id.action_settings`. |
| 4 | MEDIUM | Addressed (10.1): the five-step name rule (relative = leading `.` or no `.`; package attribute, else `namespace` literal in `build.gradle(.kts)`, else unique suffix match; absolute = exact; otherwise no citation plus a warning), searched over all module roots and applying source sets; cited line = start tag; test: all 10 Currency components cite lines 18, 28, 30, 34, 38, 42, 51, 55, 58, 69 (17). |
| 5 | MEDIUM | Addressed (11.3, 11.4, 11.5 V6, 12.2, 12.3, 12.5): directives match the unfiltered `ALL` list (calls.json edges plus excluded candidates) by `(base src, dst[, kind])`; V6 only when nothing in `ALL` matches or an `@` variant does not exist; matches that were filtered, replaced or suppressed are `no-effect` listings in `build_report.txt`; `AUTO` is that same list; the option filter is now defined exactly; precedence rules (suppress beats override, `@` beats base, same-specificity conflicts V5 across files); the 12.5 loop passes `match_kind=x['kind']`. |
| 6 | MEDIUM | Addressed (11.2, 17.1, 18): the v1 script is the oracle on a snapshot of the inputs (A = v1, B = v2 in v1 mode, B' = with an invalid `auto/`); gate = A, B, B' byte-identical plus equal stdout and exit codes; A versus `out/` is reported only (stale `out/` is pre-existing); Diary runs only in integration and install verification. Checked now: the current v1 script reproduces Currency's `out/` byte for byte (section 3), so that comparison is expected to match. |
| 7 | NIT | Addressed (4.1): A creates `tglib/__init__.py`, `tests/__init__.py` and `tests/v1ref.py` first; I copies the three v1 files and checks them against the pinned hashes. |
| 8 | NIT | Addressed (4.1, 4.2 rule 5, 13, 15): `guard_path`, `sha256_file`, `ProtectedPathError` in jsonio; allowed roots for extract_app, the standalone CLIs (`--out` dir named `auto`) and build_graph (resolved `--out` or `<gdir>/out`, never inside `auto/` or the dataset). |
| 9 | NIT | Addressed (6.2, 6.5): `excluded` lists every method with code under X2, X3, X5-X10; X1 counted only; X4 not listed. |
| 10 | NIT | Addressed (6.4): `build-config` row and flag deleted; protobuf rule covers a top-level name ending in `Protos`. |
| 11 | NIT | Addressed (8.1, 8.3, 8.4): `('param', i)` is the parameter ordinal; a local missing in a predecessor joins to unknown; several LineNumberTables are merged. |
| 12 | NIT | Addressed (9.4): lookup owner from `resolve`'s external type (Methodref owner when missing); event 5 before the table; `*` = any owner; event 2 is a hop and the anonymous-class exception uses the terminal events; `this` does not follow hops. |
| 13 | NIT | Addressed (9.1): `select` skips private, static and other-package package-access declarations and returns `('app', class, method)`. |
| 14 | NIT | Addressed (9.5): switch-map `<clinit>` dropped from the collapse targets, with the reason. |
| 15 | NIT | Addressed (5, 10.1): module roots, source set of a listed dir, camel-case variant matching with the priority variant > build type > flavors > main, test sets never candidates; examples for three apps. |
| 16 | NIT | Addressed (10.2): chunk types 0x0203-0x0206 and unknown types skipped by size; `FLAG_COMPACT` entries decoded. |
| 17 | NIT | Addressed (10.5): field assignments are matched in any analysed method of any class (ButterKnife `*_ViewBinding.<init>`). |
| 18 | NIT | Addressed (11.4, 11.5, 12.2): `suppress(src, dst, reason=None, kind=None)`; a missing reason is V6; directives never raise; a V7 `e()` call adds no edge. |
| 19 | NIT | Addressed (4.3, 13): exit 1 allowed for `extract_app.py` with several apps or `--all`. |
| 20 | NIT | Addressed (18): the integration step appends the HANDOFF section once; install only checks it. |
| 21 | NIT | Addressed (9.7): shapes, key orders and sort keys for `stats`, `instantiated`, `excluded_candidates` (now full edge records), `ext_dispatch`, `unresolved_sites`, `unresolved_callbacks`, `failures`, `warnings`; guard and trigger texts are specified too. |
| 22 | NIT | Addressed (12.1, 14, 15): a subdirectory or a badly named `*.py` in `parts/` is exit 2; `_`/`.` entries ignored; other files listed. |
| 23 | NIT | Addressed (9.7): generated classes without a source file get `INFERRED bytecode <File>:<line> (generated, no source in checkout)`. |

Other tightening in this revision: the "who reads what" contract table (4.2) and the `fw_res_ids` field it needed;
inventory fixtures so A's acceptance tests do not wait for B (17); `excluded_candidates` as complete edge records with
`requires = []`, so `AUTO_OPTIONS['uninstantiated']` is not cancelled by liveness, plus the `uninstantiated` `relies_on`
flag (9.3, 11.3, 11.7); `-B` for test runs so nothing is written into `work/tools/` (2); new backlog items in 19,
including the Diary build's `TOOL_ISSUES.md`.





