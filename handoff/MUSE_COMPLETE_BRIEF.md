# Complete brief: all 13 apps to 100% (labels, route checks, device checks, logs)

Written 2026-11-01 by the orchestrator (Claude, on the user's Mac), on the user's instruction: "give all details to Muse ... for all 13 apps to complete 100% on all sections".

This file extends `handoff/MUSE_HANDOVER.md`. Read both. Where they differ, this file wins. Every number here was printed on the user's Mac on 2026-11-01, from files identical to this branch. The raw outputs are in `handoff/baseline_2026-11-01/`. Re-run each command yourself before you rely on a number.

## 0. What is new since MUSE_HANDOVER.md

1. **You may install tools in your own VM:** a JDK (for `javap`), git, and Python packages for parsing. Never install anything on the user's machines.
2. **You can run every tool yourself.** This branch holds `tools/`, `fw_src/android-8.1.0_r1/`, `final_java_only/` (the sources of all 13 apps), `graphs/` and `handoff/`. With a clone and `python3` you run the builds and all eight checks in your VM. You no longer need the user's Mac for checks.
3. **Bytecode is available for every app, including generated classes.**
   - `graphs/<App>/auto_calls.json` (on this branch): the bytecode call edges as `{src, dst, file, line}` under the key `calls`, plus `lambdas`, `framework_calls` and `impl`.
   - The class files are in the public repo `bugfixops/work-emulator`, under `classes/<App>/<i>/` (for example, `classes/LibreTorrent/0/org/proninyaroslav/libretorrent/core/storage/dao/TorrentDao_Impl$1.class`). Read them with `javap -c -p`.
   - **App code.** With `USE_AUTO = True`, the build turns each bytecode call into an edge that cites the app source line of the call, and check 4 (`check_bytecode_lines.py`) verifies that the line shows the callee. That is how the ticked apps were built.
   - **Generated and library code with no source in the upload.** Bytecode is INFERRED evidence. AnyMemo, a ticked app, cites "bytecode edge of MainTabsBindingImpl.<init>" this way.
   - **Never** treat bytecode as a reason to skip printing the app source around a guard.
4. **Device replay is in scope now** (section 6). The user's instruction of 2026-11-01 is the go.
5. **Your eight LibreTorrent "convention" questions are answered** in section 4.2. None of them needed the user: the written rules and the eight ticked apps already decide them.

## 1. Setup (do once)

1. **Clone the work branch.** Run `git clone --branch work-2026-10-31 https://github.com/bugfixops/ground-truth-results.git gtr`. The repo is private. The user gives you a fine-grained token for this one repo (Contents: read and write) through the vault. Use a credential helper. Never put the token in the clone URL, a file, a commit, a log or a chat message.
2. **Clone the emulator repo.** Run `git clone --depth 1 https://github.com/bugfixops/work-emulator.git wemu`. It is public, so no login is needed. It holds:
   - `apks/<App>.apk`: all 13 apps, instrumented debug builds
   - `classes/<App>/<i>/`: the class files that match the APKs
   - `fixtures/`: Documents, Download, Music and Pictures
   - `.github/workflows/emulator.yml`, `ci/run_app.sh` and `ci/apps.csv`: package, coverage receiver and setup notes per app
3. **Install tools.** Install a JDK 17 or newer, and check it with `javap -version`. Python 3.10 or newer.
4. **Work from the `gtr` root** (it is `work/` on the user's Mac). Run every tool as `python3 -I tools/<tool>.py ...`.
5. **Locks and notes.** Create `handoff/WORKING_LOCK` before you work on an app, and remove it when you stop. Update `graphs/<App>/AGENT_NOTES.md` after every step, with the time and the build file name.
6. **Pushing.** Push only to `work-2026-10-31`. Never push to `main` or `result`, and never force-push. Commit as `bugfixops <bugfixops@users.noreply.github.com>`. The user also accepts their own identity, which earlier commits used. Never commit APKs, zips, tokens, secrets or personal data.
7. **UI maps.** `.agents/tasks/ui-map-<App>.md` on this branch are UI maps per app, from the original upload. They are leads for writing device scripts, not evidence.

## 2. Baseline on 2026-11-01 (user's Mac, files identical to this branch)

Build results. "uncl." is the count of unclassified placeholder rows. "STRICT" is the line in `graph_def.py`. "auto" is the number of bytecode edges that `USE_AUTO` added.

| App | Methods | REACHABLE | UNREACHABLE | uncl. | Errors | Warnings | STRICT | auto |
|---|---|---|---|---|---|---|---|---|
| Currency | 145 | 140 | 5 | 0 | 0 | 0 | True | 0 |
| Diary | 286 | 265 | 21 | 0 | 0 | 0 | True | 0 |
| hash-checker | 529 | 507 | 22 | 0 | 0 | 0 | True | 654 |
| Omni-Notes | 1456 | 1202 | 254 | 0 | 0 | 0 | True | 1437 |
| openlauncher | 900 | 728 | 172 | 0 | 0 | 0 | True | 637 |
| Vanilla-Music | 1473 | 1325 | 148 | 0 | 0 | 0 | True | 2103 |
| Markor | 2864 | 2450 | 414 | 0 | 0 | 0 | True | 5214 |
| AnyMemo | 2207 | 1966 | 241 | 0 | 0 | 0 | True | 2983 |
| Aegis | 2995 | 2537 | 458 | 0 | 0 | 0 | True | 4342 |
| AmazeFileManager | 2981 | 2509 | 472 | 0 | 0 | 0 | True | 4357 |
| AnkiDroid | 4186 | 3275 | 911 | 0 | 0 | 0 | **False** (a), the only failure | 8146 |
| MMEX | 4270 | 3430 | 840 | 0 | 0 | 0 | **False** (a), the only failure | 6800 |
| LibreTorrent | 4732 | 1986 | 2746 | **2266** | 0 | **222** | **False** | 4880 |

Checks 2 to 8 and the logs. The check numbers follow MUSE_HANDOVER section 2: 2 citation problems, 3 flagged routes, 4 bytecode lines that do not show the callee, 5 to 7 the DEAD/FRAMEWORK_ONLY, FW-MEMORY and PENDING greps, 8 UNREACHABLE methods with a bytecode caller outside the UNREACHABLE set. "Path rows" and "DEVICE rows" count the rows in `verification.csv`.

| App | Ch. 2 | Ch. 3 | Ch. 4 | Ch. 5 | Ch. 6 | Ch. 7 | Ch. 8 | Path rows | DEVICE rows |
|---|---|---|---|---|---|---|---|---|---|
| Currency | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 28 | 0 |
| Diary | 0 | 0 | 0 | 5 (b) | 0 | 0 | n/a (c) | 30 | 0 |
| hash-checker | 0 | 0 | 0 | 7 (b) | 0 | 4 (b) | 4 | 37 | 0 |
| Omni-Notes | 0 | 0 | 0 | 11 (b) | 0 | 0 | 5 | 33 | 0 |
| openlauncher | 0 | 0 | 0 | 0 | 0 | 1 (b) | 2 | 27 | 0 |
| Vanilla-Music | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 30 | 0 |
| Markor | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 0 |
| AnyMemo | 0 | 1 (d) | 0 | 0 | 0 | 0 | 3 | 30 | 0 |
| Aegis | **2** (e) | 0 | 0 | 0 | 0 | 0 | 0 | no verification.csv | 0 |
| AmazeFileManager | **23** | 0 | **63** | 0 | 0 | 0 | 4 | no verification.csv | 0 |
| AnkiDroid | **3** | 0 | **48** | 0 | 0 | 0 | **169** | no verification.csv | 0 |
| MMEX | **43** | 0 | **244** | **2** | 0 | 0 | 19 | no verification.csv | 0 |
| LibreTorrent | **102** | 0 | **crash** (f) | 2 | **2** | 0 | 5 | no verification.csv | 0 |

Notes:

- **(a)** With `STRICT = True` set in a copy, AnkiDroid and MMEX still build with errors 0 and warnings 0 (`1_build_STRICT_TRUE.txt`). Change the line to `STRICT = True`. That is the only change needed for the label gate.
- **(b)** These are not placeholders. Do not edit the ticked apps for them; record each hit in their `readme_notes.md` under `## Limits`.
  - Diary, hash-checker and Omni-Notes use `DEAD` and `FRAMEWORK_ONLY` only as temporary dictionaries, which the file converts to UNREACHABLE entries and then empties (for example, Diary lines 1608 to 1629).
  - hash-checker's 4 PENDING hits are the page id `S_MAIN_EXIT_PENDING`. Renaming it would change the edge ids and turn the checked paths STALE.
  - openlauncher's PENDING hit is AsyncTask code text at line 942.
- **(c)** Diary has no `auto_calls.json`, so check 8 has nothing to compare.
- **(d)** AnyMemo's one flagged route is explained in its `readme_notes.md` at line 77, verdict correct. That is allowed.
- **(e)** Aegis edges E24649299 and E2a97bab7 cite `services/LaunchScannerTileService.java`, which is not in the upload. Fix the citation, or make the claim INFERRED with "source not read".
- **(f)** `check_bytecode_lines.py` crashes on LibreTorrent with an IndexError, because some edge cites a line number past the end of its source file. Find it and fix it.

Markor's `graph_def.py` reads four files from `graphs/Markor/scratch/`: `hier.json`, `textcount.json`, `dotcount.json` and `route_guards.json`. Keep them.

How it was run: a copy of `graphs/` and `tools/` (byte-identical to this branch: `graph_def.py`, `method_list.json`, `auto_calls.json` and the tools were compared by git hash), with `final_java_only/` and `fw_src/` linked in. For each app, the run used `python3 -I tools/build_graph.py graphs/<App> <prefix>`, then the checks of MUSE_HANDOVER section 2. Prefixes: Currency currency, Diary diary, hash-checker hash-checker, Omni-Notes omni-notes, openlauncher openlauncher, Vanilla-Music vanilla, Markor markor, AnyMemo anymemo, Aegis aegis, AmazeFileManager amazefilemanager, AnkiDroid ankidroid, MMEX mmex, LibreTorrent libretorrent.

## 3. Definition of 100% (unchanged from MUSE_HANDOVER section 8)

An app is 100% only when all five hold, with the printed output saved in `graphs/<App>/scratch/`:

1. **Labels.** The build shows UNRESOLVED 0, errors 0 and warnings 0, and `graph_def.py` has `STRICT = True` and no `USE_AUTO = True`. Every method in `method_list.json` has one label from printed source. No "unclassified" placeholder rows remain.
2. **Route checks.** A sample of 30 routes, with every step printed and judged as correct, fixed, wrong or unclear. The error rate is reported, and all eight checks pass.
3. **Device checks.** Every sampled route is replayed on the API 27 emulator with a script (section 6). Reached routes get DEVICE rows in `verification.csv`. A route that was not reached is `unclear` until its script is checked.
4. **Logs.**
   - `verification.csv`, written by `graphs/<App>/make_verification.py`, never by hand
   - `readme_notes.md` with the five headings, then `python3 -I tools/gen_readme_v2.py <App>`
   - `LESSONS.md`
   - `AGENT_NOTES.md`
5. **Status.** The app's line in `handoff/PROGRESS_V2.md` reads `- [K] <App> (100% DONE <date>, awaiting user tick)`. Never write `[x]`; the user ticks.

## 4. LibreTorrent

### 4.1 State

- **Proposals.** Commit 07aa73c has 120 merge-ready proposal files in `graphs/LibreTorrent/scratch/merge-ready/`. All are UNVERIFIED. Totals: 3,858 REACHABLE, 310 UNREACHABLE and 564 OPEN, out of 4,732.
- **Nothing from the merge-ready files is merged.** `graph_def.py` holds the earlier runs' work, and of the parts, only batches 13 and 14 (lines 3567 and 3678).
- **Header lines.** `graph_def.py` has `STRICT = False` (line 8), `USE_AUTO = True` (line 9), an `AUTO_DEAD` placeholder (line 47), and code at lines 52 to 53 that rewrites `FW-MEMORY` to `INFERRED` in evidence text.
  - `STRICT = True` is required.
  - `AUTO_DEAD` must go: under STRICT it is an error, and every UNREACHABLE needs an authored reason.
  - The `FW-MEMORY` rewrite must go. Fix each such claim: print the FW-SRC lines, or write it as INFERRED with "source not read".
- **USE_AUTO: same standard as the ticked apps** (the orchestrator's call on 2026-11-01; the user may reverse it). LibreTorrent's AGENT_NOTES calls `USE_AUTO = True` temporary, and CHATGPT_PROMPT_LIBRETORRENT_3 rule A calls the bytecode scan "candidates only". But hash-checker, Omni-Notes, openlauncher, Vanilla-Music, Markor and AnyMemo were all ticked with `USE_AUTO = True`. Those bytecode edges cite the source line of the call, `check_bytecode_lines.py` checks that the line shows the callee, and calls inside branches that can never run are removed with `SUPPRESS`, each with a reason. The user asked for LibreTorrent "like the 8 other apps", so:
  - You may keep `USE_AUTO = True`.
  - Check 4 must reach 0 bad lines (it crashes now).
  - Every `SUPPRESS` needs its reason.
  - Every route still faces the route checks.
  - Where an auto edge ignores a guard, `SUPPRESS` it and write the hand edge with the guard.
  - The build's REACHABLE count is still not evidence by itself.
- **Current baseline (2026-11-01):** REACHABLE 1,986, UNREACHABLE 2,746, unclassified 2,266, errors 0, warnings 222, citation problems 102.
- **The plan.** `handoff/LIBRETORRENT_BATCH_PLAN.tsv` has 4,732 rows in 120 batches. Batch 11 has 9 rows, batch 120 has 3, and every other batch has 40.

### 4.2 Answers to your convention questions (apply these; no user decision is needed)

Each answer names its basis: a written rule, a ticked app that did the same, or the bytecode.

1. **The grep standard.** Run `grep -rn` over the whole app source folder, `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main`. That folder has 281 `.java` files plus `res/`, including the 41 data-binding layouts.
   - Your "252-file tree" is only `org/proninyaroslav/libretorrent`. It misses `com/ernieyu/feedparser` (28 files), `org/nanohttpd/NanoHTTPD.java` and every XML file.
   - Basis: KIRO_CONVERT_APPS.md section 3, which says grep "over the app's source folder". `tools/scan_unreachable.py`, which is check 8, searches all `.java`, `.xml` and `.kt` files under `final_java_only/<App>/app/*/`, skipping only `build`, `androidTest` and `test`.
   - Re-check every row that you flipped on the 252-file grep, including batches 39 to 42.
2. **Batches 5 to 9: the 200 base `*Binding` statics** (`inflate` and `bind` of 34 classes). Label all 200 UNREACHABLE `no_trigger_in_app`, INFERRED. Reason: "no call of this static method in the app source; the binding is built through DataBindingUtil, which uses the generated mapper and its *BindingImpl constructor".
   - Basis: AnyMemo labelled every base `*Binding.inflate` and `bind` exactly this way (`graphs/AnyMemo/out/methods.csv`).
   - The rule F grep was run on the user's Mac on 2026-11-01 and found no call for any of the 34 classes. As positive controls, the same folder has 35 `DataBindingUtil.inflate` or `setContentView` calls and 83 whole-word mentions of the 34 class names. The output with every command is in `graphs/LibreTorrent/scratch/ruleF_batch5-9_static_grep_2026-11-01.txt`. Cite that file and re-run it yourself.
3. **The generated mapper** (batches 1, 2, 12, 17 and 18). Follow the AnyMemo pattern in `graphs/AnyMemo/graph_def.py` lines 2235 to 2251:
   - Start from the `DataBindingUtil` call for layout X on a reachable route.
   - That call reaches `databinding.DataBinderMapperImpl.<init>`, then `libretorrent.DataBinderMapperImpl.getDataBinder`, then `XBindingImpl.<init>`, then `<clinit>`. These are FRAMEWORK edges, non_standard, via the data-binding library, INFERRED.
   - The bytecode shows `getDataBinder` creating every `*BindingImpl` (82 targets in `auto_calls.json`).
   - Each `*BindingImpl` is reachable only through the `DataBindingUtil` call for its own layout id.
   - The `InnerBrLookup` and `InnerLayoutIdLookup` rows get their callers from the bytecode in the same way.
4. **The data-binding callbacks** (batches 63 to 67 and similar).
   - **`setVariable`.** In the bytecode, `setVariable` calls `setViewModel` (16 BindingImpl classes), and nothing calls `setVariable`. The app source has 0 `.setVariable(` calls. So `setVariable` is UNREACHABLE `no_trigger_in_app` (the AnyMemo precedent). Batch 65 has the direction backwards; batches 63 and 64 are right.
   - **`getViewModel`.** The bytecode has 0 callers, and the Java source has 0 calls. UNREACHABLE `no_trigger_in_app`.
   - **`invalidateAll`.** Every `*BindingImpl.<init>` calls it (bytecode, 39 classes). It is REACHABLE wherever that constructor is reachable.
   - **`executeBindings` and `hasPendingBindings`.** The library's pending-bindings pass calls them. Use an edge from `invalidateAll`, non_standard, via "androidx ViewDataBinding pending-bindings pass", INFERRED (AnyMemo lines 2245 to 2248).
   - **`onFieldChange`.** `framework_never_calls` only when the layout declares no `<variable>` (AnyMemo line 2251). Otherwise, find the observable field in the layout XML and the bytecode.
   - **Variant and configuration gates and no-variable layouts.** Decide them from the layout XML and the bytecode for each layout, not by one global switch.
5. **Room.** Generated `*_Impl` classes are INFERRED (KIRO_CONVERT_APPS section 3, which names Room `*_Impl`).
   - **`$N`: use STRICT.** The bytecode pins which method creates each anonymous class, so there is nothing to guess. For example, `TorrentDao_Impl$1` to `$6` are created in `TorrentDao_Impl.<init>` at lines 52, 99, 117, 133, 151 and 203. `$7` is created in `getTorrentByIdSingle` at line 495, and `$8` in `observeTorrentById` at line 593. For the fields `<init>` fills, `javap -c -p` shows which field each `$N` goes into (`putfield`), and which DAO method reads that field (`getfield`). Do the same for `FeedDao_Impl`, `TagInfoDao_Impl` and `FastResumeDao_Impl`.
   - A DAO `_Impl` method is REACHABLE when the app calls the matching DAO interface method on a reachable route. Use an INFERRED edge for the interface dispatch. Otherwise it is UNREACHABLE `no_trigger_in_app`, with the full-folder grep for the interface method name.
   - **Converters.** `AppDatabase_Impl.getRequiredTypeConverters` calls each `*Dao_Impl.getRequiredConverters` (bytecode lines 272 to 275). Room calls `getRequiredTypeConverters` when the database is built (library source not read). So all four are REACHABLE, INFERRED, from the database build on the route.
6. **`finalize`.** REACHABLE, INFERRED. Write an edge from the class's `<init>` to `finalize`, of kind LIFECYCLE, non_standard, via "JVM finalizer rule". This is the AnyMemo precedent (`C4_FINAL`, AnyMemo `graph_def.py` lines 2480 to 2514). It applies to `TorrentDao_Impl$7` and `$8.finalize`, and to the others like them.
7. **Parcelable** (writeToParcel, createFromParcel, newArray, describeContents and the Parcel constructor). Use the rule from Omni-Notes and openlauncher, which is the strict marshalling-site rule.
   - **`writeToParcel` and `createFromParcel`.** REACHABLE only from a printed marshalling site on a reachable route. Write sites include `putExtra`, `putParcelable`, `putParcelableArrayList`, `writeParcelable`, `onSaveInstanceState`, Fragment arguments and `ParcelableUtil.marshall`. Read sites include `getParcelableExtra`, `getParcelable` and `readParcelable`. Cite FW-SRC `core/java/android/os/Parcel.java` lines, as openlauncher `graph_def.py` line 113 does.
   - **`newArray`.** UNREACHABLE `framework_never_calls`, unless a printed site reads an array of that type (`readParcelableArray`, `createTypedArray`, `readTypedArray`). This is openlauncher lines 1218 to 1219. Batch 102's REACHABLE `newArray` stays only if it has such a site; otherwise it goes the same way as batch 114.
   - **`describeContents`.** `framework_never_calls`, INFERRED, as openlauncher lines 1214 to 1216 have it.
   - **"Internal construction"** (an object that is only created, never marshalled) is not a route.
8. **`hashCode`, `toString` and `equals`.** One rule for every batch (hash-checker, Vanilla-Music, AnyMemo, Omni-Notes): REACHABLE only from a printed call on a reachable route. A printed call is one of:
   - an explicit call
   - an implicit string conversion: concatenation, a log call, `String.valueOf`, an `ArrayAdapter` row text
   - a key in a HashMap, HashSet or similar (AnyMemo: `QuizQueueManager.update -> Card.hashCode`)
   - an `equals` from DiffUtil, `List.contains` or `indexOf`

   Otherwise, UNREACHABLE `no_trigger_in_app`, with the full-folder grep (Vanilla-Music `Song.toString`, hash-checker `HistoryItem.hashCode`). Batches 39 to 42 must be re-checked under this rule and the full-folder grep, just like every other batch.
9. **Constructors, including the three AndroidX preference 1-argument constructors.** Label each constructor from its own callers: grep for `new X(` and the `this(...)` chains, plus the bytecode callers in `auto_calls.json`. There is no all-or-none bundling. Layout and preference XML inflation calls the `(Context, AttributeSet)` constructor. That is androidx code, not read, so the edge is INFERRED, non_standard.
10. **The strict entry rule is not a choice.** REACHABLE needs a route from the launcher entry (SCHEMA_V2.md, "How the labels are derived"), and every step must be a hand-written edge (CHATGPT_PROMPT_LIBRETORRENT_3 rule D).
    - Library dispatch steps (WorkManager, SAX callbacks, Room, data binding, the JVM finalizer, Rx) may be INFERRED edges, as in the ticked apps. App-code steps must be printed.
    - `confirmed_by` for a REACHABLE method is computed by the build from its best route: SOURCE when every edge cites a source line, INFERRED otherwise (SCHEMA_V2.md). Do not set it per row, and drop your "whole-route alternative" note.
    - The 1,067 to 1,102 REACHABLE rows that you marked "at revert risk" need their trunks printed up to the launcher. That is work, not a decision. Example: the feed-settings trunk. `FeedSettingsFragment` is opened by `SettingsFragment.java` lines 122 and 195 to 198 and by `PreferenceActivity.java` lines 113 to 114. Print those lines, then the route from the launcher to the settings screen.
11. **Anonymous classes in app code (`Foo$1`, `Foo$2`).** javac numbers them in the order they appear in the source file. Confirm each one with the bytecode: `auto_calls.json` shows which method creates `Foo$N`, at which line.
12. **A case none of these rules cover.** First look for a precedent in the eight ticked apps (grep their `graph_def.py` and `out/methods.csv`), apply it, and record it under `## Convention calls` in `graphs/LibreTorrent/AGENT_NOTES.md`. Ask the user only if there is no rule and no precedent and the choice changes a label.

### 4.3 Steps to [L]

1. Apply 4.2 to all 564 OPEN rows, and re-check every row that 4.2 changes. Re-run the full-folder grep for every row flipped on the 252-file grep. Use spot-checks as before: at least 1 claim in 5, printed with `sed -n`.
2. **Turn each merge-ready file into a part,** `graphs/LibreTorrent/parts/b<NNN>.py` and `.md`, in the format of the existing `parts/b013.py` and `b014.py`. That means hand-written `e(...)` edges citing printed lines, `UNREACHABLE[m] = (kind, reason, source_ref, confirmed_by)`, and `sup(...)` only with a reason. For the idioms, see `graphs/AnyMemo/graph_def.py`.
3. **Merge one part at a time, in plan order.** Append each part to `graph_def.py` as `# ---- part: batch <n> (parts/b<NNN>.py; printed evidence scratch/b<NNN>_printed.txt)`. Then:
   - run `python3 -m py_compile graphs/LibreTorrent/graph_def.py`
   - run the build, and save the output as `scratch/build_<next number>.txt`
   - check that errors did not rise
   - record the merge in AGENT_NOTES

   These are the C1 conditions in KIRO_CORRECTIONS.md. Up to 4 helpers can write parts in parallel. Only you merge.
4. **Print the shared trunks** from the launcher entry, and merge them first. The trunks are: feed refresh, torrent service and engine, add-torrent, settings, the streaming server, and the notification actions.
5. **Switch to `STRICT = True`, and remove `AUTO_DEAD` and the `FW-MEMORY` rewrite.** Do it as soon as the trunks are in. Every build after that shows the honest count of unclassified rows, as errors.
6. **The gate.** UNRESOLVED 0, errors 0, warnings 0, unclassified 0, `STRICT = True`. Check 4 must run without crashing and show 0 bad lines, and check 2 must show 0 problems. Then change the LibreTorrent line in PROGRESS_V2.md to `- [L] LibreTorrent (labelled <date>; route checks not started)`.
7. **Then:** route checks (MUSE_HANDOVER WP2 steps), logs, device checks (section 6), and `[K]`.

## 5. The other 12 apps: what is left for 100%

The baseline table in section 2 has each app's current counts. Per app:

- **Currency, Diary, hash-checker, Omni-Notes** (ticked)
  - Device checks (section 6).
  - Logs: `LESSONS.md` and `make_verification.py` are missing from their folders. Their `verification.csv` exists.
    - `handoff/examples/` has `make_vlog_hash_checker.py` and `make_vlog_omni_notes.py`. Going by their names, they write those two apps' logs. Check that each one regenerates the current `verification.csv` byte for byte, copy it to `graphs/<App>/make_verification.py`, then extend it with the DEVICE rows.
    - Currency and Diary have no writer named. Write `make_verification.py` so that it reproduces the current file exactly, and log that.
  - Checks 5 and 7 hits: see note (b) in section 2. Record them in `readme_notes.md` and do not edit `graph_def.py`.
  - Write `LESSONS.md` with 3 to 8 bullets, taken from their `readme_notes.md` and `AGENT_NOTES.md`.
- **openlauncher, Vanilla-Music, Markor, AnyMemo** (ticked): device checks. Their logs exist.
- **All eight ticked apps:** no label or route changes, unless a device run or a source re-read shows an error. If one does, fix it, rebuild, reprint the route, log it in `scratch/fix_log.md`, and list the app in your report. Keep their `[x]` lines as they are.
- **AmazeFileManager, AnkiDroid, MMEX** (labelled, route checks not started): WP2 in MUSE_HANDOVER. That means a sample of 30, print and judge every step, fix, the eight checks, then the logs, then the device checks.
  - Your unverified WP2 proposals in `graphs/<App>/scratch/proposals/` are inputs only.
  - The known issues are in MUSE_HANDOVER WP2: the AmazeFileManager Glide contradictions and the E89e2cedd and Ee1aeff93 items; AnkiDroid `Card.toString`, `EasySSLSocketFactory.equals` and `hashCode`, the API 27 versus target 23 question, and `Hooks.runFilter`; and the MMEX INFERRED UNREACHABLE entries.
  - None of these apps has `make_verification.py`, `readme_notes.md` or `LESSONS.md` yet. Use AnyMemo's `make_verification.py` as the model.
  - The baseline check failures (section 2) are work items in their route-check stage:
    - **AmazeFileManager:** 23 citation problems and 63 bytecode lines that do not show the callee.
    - **AnkiDroid:** 3 citation problems and 48 bad bytecode lines. Set `STRICT = True`. 169 UNREACHABLE methods have a bytecode caller outside the set (check 8), and each needs its reason to explain that caller.
    - **MMEX:** 43 citation problems and 244 bad bytecode lines. Set `STRICT = True`. 2 lines use the word DEAD in reason text (lines 13360 and 13485): reword them.

    The full lists are in `handoff/baseline_2026-11-01/<App>/`. Fix each item from printed source, then rebuild.
- **Aegis:** route steps 6 to 10 (MUSE_HANDOVER WP3), then logs and device checks.
  - Fix its 2 citation problems (note (e) in section 2).
  - Its 7 "Decision for Yang" items are listed in section 7. Stop on those routes only, and finish everything else.
  - Aegis has no `make_verification.py`, `verification.csv` or `LESSONS.md` yet.

## 6. Device checks on all 13 apps (in scope now)

### 6.1 Repos

- **`bugfixops/test-13` was not found** on 2026-11-01, either anonymously or with the user's saved git login ("Repository not found"). Either it does not exist, or that login cannot see it. Check with your connector.
  - If it does not exist, create it as a public repo. Public repos get unlimited Actions minutes, and `handoff/NEXT_DEVICE_REPLAY.md` already says public.
  - If it exists, check its visibility before the first push.
- **Put in it only:** the workflow, the route scripts, the route list and the comparison script. No APKs, no graph notes, no personal data, no secrets.
- **The workflow downloads the APKs, class files and fixtures** from `bugfixops/work-emulator` (already public) at run time.

### 6.2 Emulator (until Yang decides D4)

- Copy the emulator step from `work-emulator/.github/workflows/emulator.yml`. It uses `reactivecircus/android-emulator-runner@v2` with these settings:
  - `api-level: 27`
  - `target: default` (AOSP, no Google APIs)
  - `arch: x86_64`, `profile: pixel_2`
  - `cores: 3`, `ram-size: 3072M`, `heap-size: 512M`, `disk-size: 4096M`
  - the same `emulator-options`
  - `disable-animations: true`
  - the "Enable KVM" step
- This is the image the baseline tool runs used, so the results stay comparable.

### 6.3 Secrets and environment

- **No secret is needed.** The APKs, classes and fixtures come from a public repo. Results are committed with the workflow's own `GITHUB_TOKEN` (`permissions: contents: write`) to a `results` branch of `test-13`.
- Write this list into `handoff/NEXT_DEVICE_REPLAY.md` before the first push.

### 6.4 Which routes

- **For each app, the final sample routes.**
  - For the ticked apps and AnyMemo: the routes in the `path` rows of `verification.csv`.
  - For the others: the final sample table of their route checks.
- **30 per app now.** `NEXT_DEVICE_REPLAY.md` asks for more on Omni-Notes, Vanilla-Music, Markor, hash-checker and AnyMemo edges. The number is the user's call (D3). Run the 30 first.

### 6.5 One script per route

Write `routes/<App>/route_<NN>.py` in `test-13`, built from the printed route:

- **Start from a fresh install.** Run `adb shell pm clear <package>`, as the standard configuration requires. Then do the setup that `ci/apps.csv` names for the app: fixtures, the Vanilla-Music media scan, the AnkiDroid deck import.
- **First-run setups are part of the route** and get scripted steps: the Aegis vault, the AnkiDroid import, the Markor tutorial, the MMEX database.
- **Each edge's trigger becomes one action:**
  - `am start -n <package>/<launcher activity>` for the launcher entry
  - a tap on a view found by resource-id or text in `uiautomator dump`, never by fixed coordinates
  - `input text` for text entry
  - `input keyevent` for keys
- **Runtime permissions:** `pm grant` only for the permissions the route's ENV `permission` gate needs. Deny the others.
- **Save evidence per step:** a screenshot (`screencap`) and the `uiautomator` XML. Save logcat per route.

### 6.6 "Reached" signal

- **Discard the dump before the script.** Before the script, send the coverage broadcast `edu.gatech.m3.emma.COLLECT_COVERAGE` to the app's receiver (the `receiver` column of `ci/apps.csv`) and discard that dump, as `ci/run_app.sh` does. The receiver resets its counters after each dump.
- **Decide from the dump after the script.** After the last step, dump again and build `methods_hit.csv` with JaCoCo (`ci/get_jacoco.sh`, using `classes/<App>/<i>/`). The route is reached when the target method has `hit = 1`.
- **JaCoCo here is only the reached signal of our own scripted replay** of a printed route (DEVICE in SCHEMA_V2.md). Monkey and APE coverage are still never evidence.
- **Names.** Convert JaCoCo method names to graph names with the naming in `tools/build_graph.py`, as `tools/emu_compare.py` does. `emu_compare.py` itself was written for Monkey runs under schema 1; write a new route comparer in `test-13`, not in `tools/`.

### 6.7 Results and verification rows

- **Per route, record:** app, method, route edge ids, reached (yes or no), the steps that ran, the screenshots, logcat and the run id.
- **Pull the results** into `graphs/<App>/device/results.csv` on the work branch.
- **`make_verification.py` writes the DEVICE rows:**
  - `type=path`
  - `item=<method>`
  - `result=correct` when reached, otherwise `unclear`
  - `confirmed_by=DEVICE`
  - `ref=test-13 run <id>/<script>`
  - `edges=<route edge ids>`
  - `note`
- **Three rules for failures:**
  - A route that was not reached stays `unclear` until its script is checked.
  - A failed script is not evidence that the route is wrong.
  - No label changes from a device run unless you read the source again first.

### 6.8 Runs

- **One job per app,** with `workflow_dispatch` inputs as in `emulator.yml` (apps, run id). The job timeout is 340 minutes.
- **Order:** the eight ticked apps first, because their routes are final. Then each other app after its route checks pass.

## 7. Decisions only the user or Yang can make

Record each one under `## Open decisions for the user` in the app's AGENT_NOTES. Stop on that item only, and carry on with everything else.

- **D1, Aegis:** the 7 "Decision for Yang" items in `graphs/Aegis/AGENT_NOTES.md`:
  1. **Line 379, R1 step 13.** Page node, or a SYSTEM producer with needs_state on the Next edges.
  2. **Line 479, route 4 step 9.** It needs an icon pack left from an earlier run: reclassify the route as non-standard, or add the precondition.
  3. **Line 599, route 1 step 21.** A continuation node after `initNew` is needed, and `build_graph.py` has no RETURN kind.
  4. **Line 603, step 14, SEARCH_IN_GROUPS.** A two-process route: ERROR, or UNCLEAR under rule D2.
  5. **Line 609, G3_5 step 34.** The default Authy app-import path is no longer modelled.
  6. **Line 636, GlideRequests step 50.** The router's cheaper choice needs root.
  7. **Line 659, `GoogleAuthImporter.readFromApp`.** The row-tap edge versus the OK button that reads the checked row.
- **D2, AnyMemo storage permission:** only if a route check or device run depends on it (MUSE_HANDOVER section 4).
- **D3, device scope:** the number of extra routes for the five apps, and whether to delete `test-13` and `work-emulator` afterwards.
- **D4, API 27 image:** use the work-emulator image (6.2) until Yang says otherwise.

Nothing else is a user decision. Convention questions are settled by section 4.2, the rules and the ticked apps' precedents.

## 8. Order and parallel streams

Run these streams in parallel. Each stream locks its own app folders and never edits another stream's apps. At most 4 helpers per app, and at most 40 methods (labels) or 10 routes (route checks) per helper.

- **A, LibreTorrent:** section 4.3, then route checks, logs and device checks.
- **B, route checks:** AmazeFileManager, then AnkiDroid, then MMEX, one app at a time. Then their logs and device checks.
- **C, Aegis:** steps 6 to 10, then logs and device checks, except D1.
- **D, device infrastructure:** create `test-13`, the workflow, the script harness and the route comparer. Then the eight ticked apps' device runs. Then each other app's runs when its route checks pass.
- **E, logs for the ticked apps:** `LESSONS.md` and `make_verification.py` for Currency, Diary, hash-checker and Omni-Notes.

## 9. Report and safety (unchanged)

- **After each batch, app or run, report:**
  - the exact command
  - the printed counts: methods, REACHABLE, UNREACHABLE, UNRESOLVED, errors, warnings
  - the route table: correct, fixed, wrong, unclear, error rate
  - the device table: reached, not reached, script failed
  - the status line you changed
  - blockers
- **Never report a count you did not print in the same session.** Never write "passed" without the saved output.
- **Proposals stay under `scratch/`, marked UNVERIFIED,** until they pass the build and the C1 checks.
- **No tool coverage as label evidence:** no Monkey, APE, `coverage_baseline.json`, `sanity_check.csv` or JaCoCo from tool runs. No old generated graphs as evidence.
