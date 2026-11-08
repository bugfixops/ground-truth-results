# Muse brief: re-audit and fix the labels of five apps

Written 2026-11-05 by Claude (the reviewer), at the user's request.

**Apps:** Aegis, AmazeFileManager, AnkiDroid, LibreTorrent, MMEX.

**Precedence:**
- This file overrides every older Muse brief where they differ.
- Sections 2.1 and 2.2 of `handoff/MUSE_FINISH_ALL.md` (getting a working tree, local builds) still apply, except where section 3 below changes them.
- The rubric is `review/TASK_NOTE.md` (the external reviewer's task note). If this file and the task note ever disagree on how to classify a method, the task note wins. Write the case in `handoff/MUSE_REAUDIT_QUESTIONS.md`.

There is no deadline, but work as fast as the checks allow. You have the credit for 50 to 100 agents at once; section 8 says how to use them.

---

## 0. The short version (read this, then the rest)

1. **The job.** In the five apps, fix the causes that put methods into the wrong class (env, state, library, gui). Re-derive the labels. Re-check the routes that change. Audit the reachable labels by class. Measure against the tuning half of the independent sample. Publish.
2. **Where.**
   - Repo `bugfixops/ground-truth-results`, branch `work-2026-10-31`, through your connector, exactly as before.
   - Branch `result` is updated only by the publish workflow (section 9.5). Never push to `main` or `result` yourself.
3. **Never:**
   - change anything in the other eight apps (Currency, Diary, hash-checker, Omni-Notes, openlauncher, Vanilla-Music, Markor, AnyMemo);
   - name where the independent sample comes from (no publication, venue or project names) or quote results of that work, in any file, note or commit message (`python3 -I tools_dev/check_terms.py` flags such lines);
   - look for, ask for, or reconstruct the held-out half of the sample;
   - write `verification.csv` by hand;
   - report a number you did not print.
4. **Autonomy.**
   - You push yourself, at the points in section 9, with no approval from anyone.
   - CI, emulator runs and publishing start when you push their request files.
   - Questions go to `handoff/MUSE_REAUDIT_QUESTIONS.md` with the default you used, and you carry on.
5. **Done when** gates G1 to G10 in section 11 hold on the official CI.

---

## 1. What is wrong, with the numbers to start from

An external review on 3 November 2026 compared the five apps' full labels with an independent hand-labelled sample of 50 unreached methods per app.

**Agreement was 59%** on 249 methods. Two errors were systematic:
- **too much gui:** methods labelled gui that need state or the environment, or are dead;
- **too little state:** methods labelled env that have an in-app route needing only state.

The reviewer re-checked 23 disagreements from the source. We re-checked the review and confirmed it: it read our labels correctly in 23 of 23 cases, and 6 of 6 source checks agreed. **The dead verdicts are good.**

The causes, and where each shows in the current graphs (official CI `57d051a0`, request `9c51c99c`):

| # | Cause | Where it shows now |
|---|---|---|
| 1 | **Exported or external entries instead of the in-app route** | **LibreTorrent:**<br>- 13 ENTRY edges carry `env='android:exported="true"'`, including the launcher activity itself (`S_ENTRY → MainActivity.onCreate` `Ef4711e98`, `→ MainActivity.<init>` `E558b0012`, `→ MainActivity.<clinit>` `E50191c30`). The launcher is the normal app start.<br>- 3,304 reachable methods have a best route through one of these 13 edges.<br>- The notification receiver entries (`E8d91402a`, `E2f8f0c2f`, env `PendingIntent.getBroadcast(`) gate 357 more methods, although the in-app pause button fires the same action.<br>**AnkiDroid:** 41 such edges, 96 methods. **MMEX:** 17 edges, 44 methods. |
| 2 | **One-time intro screens and first-run state treated as gates** | **Aegis:** the gates "The intro security picker chose none…" (1,528 methods) and "The Welcome slide did not import a vault…" (1,523), plus pages `S_INTRO_WELCOME`, `S_INTRO_PICKER`, `S_INTRO_SETUP`, `S_INTRO_DONE`.<br>**AnkiDroid:** "data: the deck has cards to study" (1,594), "file: a collection file (collection.anki2) exists" (274), "data: a deck exists in the collection" (219).<br>**MMEX:** "at least one account exists…" (382), and a first-run tutorial gate (34).<br>The baseline (section 5) satisfies most of these. |
| 3 | **Calls dispatched to types that are never created; reflection** | Bytecode edges with `dispatch: cha` in `auto_calls.json`: Aegis 328, AmazeFileManager 448, AnkiDroid 633, LibreTorrent 1,167, MMEX 602.<br>Example: `SshClientUtils$2.execute → HybridFile$9.execute` (cha), although `HybridFile$9` is created only in the uncalled no-arg `HybridFile.getInputStream()`.<br>MMEX-03: the reflective creation `showFragment(Class) → AccountListFragment.<init>` is already non_standard, but the fragment's callbacks are reached by explicit and standard edges, so the label is gui instead of library. |
| 4 | **Outside data the route consumes** | Picker results, server responses (Yahoo YQL, a live SSH host key, AnkiWeb sync), data only older app versions write. Cases: Aegis-46, Aegis-47, MMEX-38, AmazeFileManager-12, AnkiDroid-34. |
| 5 | **Guards on the route ignored** | Only 921 of 9,917 code steps on the routes of never-run methods record any guard. Bytecode edges never do.<br>Cases: MMEX-41, MMEX-49, MMEX-20, AmazeFileManager-01, -27, -46, AnkiDroid-07, Aegis-47. |
| 6 | **Library edges classed standard** | Edges on the default class whose evidence mentions XML inflation or reflection: about 25 (Aegis), 30 (AmazeFileManager), 27 (AnkiDroid), 45 (LibreTorrent), 70 (MMEX). Most Rx, EventBus and data-binding edges are already non_standard. |

**Audit gap.** 94–97% of the label rows in these five apps' `verification.csv` are UNREACHABLE methods. Only 25–30 reachable methods per app were audited. W9 closes that gap.

---

## 2. Inputs

| Path | What | State on 2026-11-05 |
|---|---|---|
| `review/TASK_NOTE.md` | the rubric: baseline, class rule, best-route rule, fix order, measurement | on the branch |
| `review/README.md` | public summary of the review | on the branch |
| `review/measure.py` | agreement, confusion table, weighted class shares, blind A/B files | on the branch, tested |
| `review/sample_tune/<App>.csv` | the tuning half: rows whose id ends in an odd number, plus the 23 checked cases | **added by the reviewer when the user saves the files** |
| `review/checked_cases.csv` | the 23 disagreements decided from the source (`right`, `source_class`) | **added by the reviewer when the user saves the files** |
| `tools_dev/check_unchanged_apps.py` | proves the other eight apps did not change (base `46682745`) | on the branch, tested |
| `tools/pack_results.py`, `tools/results_templates/*.md` | regenerate `run_result/` and the READMEs | on the branch, tested |
| `.github/workflows/publish-result.yml` | publishes to `result` when `handoff/PUBLISH_REQUEST.txt` is pushed | on the branch |
| `tools_dev/check_terms.py` | flags lines that would break the publishing rule | on the branch, tested |

**At every start and reset, check whether `review/sample_tune/` exists:**
- **If not:** do W1 to W7 and the W9 draw. W0 and the round measurements wait.
- **If yes:** do W0 first, if it is not done yet.

**The held-out half** (rows whose id ends in an even number, except the 23 checked cases) is not in the repo. The reviewer measures it once, at the end. Never ask for it.

---

## 3. Where and how you work

### 3.1 Tree, builds, tools

1. **Clone.** `git clone --branch work-2026-10-31 https://github.com/bugfixops/ground-truth-results.git gtr`. If github.com is unreachable, use the bundles: `handoff/MUSE_FINISH_ALL.md` 2.1.
2. **Bytecode.** Clone `https://github.com/bugfixops/work-emulator.git` for `classes/<App>/<i>/` (`javap -c -p`), with JDK 17 or newer.
3. **Check the tree.**
   ```
   bash handoff/ci/rebuild.sh Aegis
   ```
   The local SUMMARY must equal `graphs/Aegis/scratch/ci_latest/SUMMARY.txt` on the branch, except the commit line.
4. **Build one app:**
   ```
   python3 -I tools/build_graph.py graphs/<App> <prefix>
   ```
   Prefixes: Aegis `aegis`, AmazeFileManager `amazefilemanager`, AnkiDroid `ankidroid`, LibreTorrent `libretorrent`, MMEX `mmex`.
5. **Build plus the eight checks:** `bash handoff/ci/rebuild.sh <App>`.
6. **Syntax check:** `python3 -m py_compile` on every graph file you edited.
7. **Never-run methods (for W7).** A method counts as never run when it has `monkey_hit` 0 and `ape_hit` 0 in `graphs/<App>/out/sanity_check.csv`. This needs `coverage_baseline.json`, which a plain clone has.
8. **Graph file layout:**
   - AmazeFileManager, AnkiDroid and MMEX are split into `graph_def.py` plus `graph_def_mod/*.py`.
   - LibreTorrent uses `graph_def.py` plus `parts/`.
   - Keep every pushed file below 900 KB. Use `handoff/connector_kit/split_graph_def.py` if one grows, and prove byte-identical outputs.

### 3.2 How the class comes out of the graph (do not write classes directly)

The class of a method is derived from its best route. You change edges and UNREACHABLE entries, never a class column.

| Class | What produces it |
|---|---|
| dead | an `UNREACHABLE` entry, kind `no_trigger_in_app`, `framework_never_calls` or `branch_never_taken` |
| config | an `UNREACHABLE` entry, kind `closed_by_configuration` or `closed_by_api_level` |
| env | an edge on the best route with `env=<text>` and `env_kinds=[...]`; kinds: `network`, `tls_chain`, `permission` (does not count), `hardware`, `other_app`, `system_event`, `time`, `other` |
| state | an edge on the best route with `needs_state=<text>` and `state_kinds=[...]`; kinds: `data`, `settings`, `account`, `file`, `session` |
| library | no route to the method without a `non_standard` edge; an edge becomes non_standard with `cls='non_standard', via='<mechanism> (<file:line>)'` |
| gui | everything else |

**How the builder picks the best route** (converted graphs, `STRICT = True`): the fewest env kinds, then the fewest state kinds, then the fewest steps. It already matches the task note's best-route rule. So put each gate on the edge where it truly is; the builder finds the route that avoids it, if one exists.

**How to edit:**
- **A hand-written edge:** edit its `e(...)` call.
- **A bytecode edge:** use the app's `EDIT` hook, keyed by `(src, dst)` and, if needed, the line, to set `needs_state`, `env`, `cls` or `via`. Use `SUPPRESS` to drop an impossible call, always with a comment that cites the printed source.

**Edge ids change** when an edge's fields change. After each edit, the affected `verification.csv` rows show up as warnings: "edge … no longer exists", or "the verified path … is no longer the best route". W8 handles them; never hide them.

### 3.3 Hard rules (breaking one stops that item; record it and continue)

1. **Only the five apps change.**
   - Run `python3 -I tools_dev/check_unchanged_apps.py` after every local rebuild of the eight apps, and on every CI commit. It must print `ALL UNCHANGED`.
   - Tool changes are switched off by default (W1) and switched on only in the five apps' graph files.
2. **Evidence:**
   - Every gate, edge, SUPPRESS and UNREACHABLE comes from source you printed (`sed -n '<from>,<to>p' <file>`) and read. Its text cites `file:line`.
   - Bytecode (`javap`, `auto_calls.json`) is INFERRED evidence for generated and library code; it never replaces printing the app source around a guard.
   - Tool coverage is never evidence for a label.
3. **Dead verdicts:**
   - Never mark a method UNREACHABLE while a route to it exists.
   - A method that loses its route because of W1/W4 becomes UNREACHABLE only after source shows that nothing reachable creates its type (grep for `new <Class>(`, factory and `Class.forName` calls, `javap` for `<init>` call sites).
   - If the framework, reflection, a Parcel `CREATOR`, a FragmentManager restore or a singleton creates it, add the missing creation edge with evidence instead.
4. **The audit log.**
   - `verification.csv` is written only by `graphs/<App>/make_verification.py`, run from the repo root.
   - Run it twice in a row; the two outputs must be byte-identical.
5. **Publishing rule.**
   - No file, note, commit message or README you write may name where the sample comes from (no publication, venue or project names) or quote results of that work. Run `python3 -I tools_dev/check_terms.py --since 46682745` before every push; it must print `nothing flagged`.
   - Describe the sample only as "an independent hand-labelled sample of 50 unreached methods per app".
   - The generator refuses to publish otherwise.
6. **The held-out half.** Never tune against it; never look for it. Measure only with `review/sample_tune/`.
7. **Numbers.** Never report a number you did not print. Save every output you rely on under `graphs/<App>/scratch/reaudit/` or `review/rounds/<n>/`.
8. **Identity and repo safety:**
   - Commit identity `bugfixops <bugfixops@users.noreply.github.com>`.
   - Never force-push; never delete history.
   - Never commit secrets, APKs, zips, or absolute paths from your machine.

---

## 4. Agents, roles and the check–recheck–check chain

### 4.1 Roles

| Role | Count | Owns |
|---|---|---|
| Coordinator (you) | 1 | the plan and state; the only writer of `handoff/MUSE_RUN_LOG.md`, `MUSE_DECISIONS.md`, `MUSE_REAUDIT_QUESTIONS.md`, `MUSE_REAUDIT_SUMMARY.md`; the only sender of CI, emulator and publish requests |
| Tool lead | 1 | `tools/build_graph.py` and its backup, `tools_dev/` scripts, `tools/results_templates/` (W10 only) |
| Merger | 1 per app (5) | that app's graph files, `make_verification.py`, `verification.csv` (through the writer), `readme_notes.md`, `LESSONS.md`, `AGENT_NOTES.md`, `device/routes/<App>/`; the only one who pushes them; merges audited pieces one at a time, with a local build after each |
| Measurement lead | 1 | runs `review/measure.py`; organises blind adjudication; writes `review/rounds/<n>/` |
| Device lead | 1 | `device/` code (no changes expected), dry and real runs, `compare.py` and the writers' DEVICE rows (through the mergers) |
| Helpers | the bulk | one sized task each (section 8), in a private copy; return edits plus a report with the printed source; never push, never edit the shared files |
| Auditors | per section 8 | never the author of what they check; re-print the source and re-judge blind |

### 4.2 Check, recheck, check: the chain for every change

1. **Check (author).** The helper prints the source, decides, and writes the edit with `file:line`. It tests the edit in its private copy, and the build must not gain errors.
2. **Recheck (auditor, blind).** A different agent gets the claim without the author's verdict, re-prints the cited lines, and decides independently. A mismatch sends the piece to a new helper. Two failures go under `## Blocked`.
3. **Check (merger).** The merger merges, builds locally, runs `py_compile`, runs the item's scripts, and for apps it changed checks that the eight-app script stays `ALL UNCHANGED`.
4. **Official check (CI).** At the end of each work item and each round: CI for all 13 apps, then the item's acceptance lines.
5. **Final check (reviewer).** After W10, Claude re-checks a sample of your edits from source and measures the held-out half. You don't wait for this.

Audit rates (at least): **1 in 3** for gates, edges, SUPPRESS and UNREACHABLE entries; **every** route step for re-verified routes (W8); **1 in 20** for steps the W7 pre-screen cleared; **every** adjudication by 2 agents (W0, W8); **every** reachable-audit row by 2 agents (W9).

---

## 5. The rubric in brief (details: `review/TASK_NOTE.md`)

**Baseline.** A fresh install of the instrumented debug build on an API 27 emulator, plus the first-run setup:
- Aegis: onboarding passed and a vault with two entries;
- MMEX: a database with one checking account;
- AnkiDroid: a sample deck imported;
- Markor: onboarding passed (Markor is not part of this job).

**Never state:** anything the setup creates. Permission prompts are GUI actions.

**Class rule**, first that applies:

| Class | When |
|---|---|
| dead | nothing can run it |
| config | only another build or API level |
| env | something outside the app: another app or the system (pickers, shares, widgets, broadcasts), network or servers, device, time, data from an older version, limits of the API 27 image |
| state | GUI only after in-app actions create state: stored data, a file, a non-default setting, a UI session, an account or vault |
| library | only through an edge that a library or reflection creates: EventBus, Rx, data binding, a class inflated from XML, `Class.newInstance` |
| gui | GUI actions alone; long press, drag, text input and rotation count |

**Best-route rule.** A gate counts only if no other route avoids it. Choose the fewest env gates first, then the fewest state gates.

**Guards** become gates only when (1) the baseline plus ordinary GUI actions cannot satisfy them, and (2) no other route avoids them.
- Never count null checks or similar guards that always hold in normal use.
- Intent extras are env only when the Intent comes from outside the app.

---

## 6. Work items, in order

Within an item, the five apps run in parallel. Across items, start W2 to W6 as soon as W1 is pushed. W7 starts per app when that app's W2 to W6 are merged.

### W0. Round 0: measure the current labels (needs `review/sample_tune/`)

1. **Measure:**
   ```
   python3 -I review/measure.py --sample review/sample_tune --out review/rounds/0
   ```
2. **Adjudicate blind.** Give each row of `review/rounds/0/blind.csv` to **2 adjudicators**, never the key.
   - Each prints the source (callers, guards, manifest) and decides which label the source supports: A, B or neither (and then the class it found), with `file:line`.
   - When the two disagree, a **3rd** decides.
   - Write `review/rounds/0/adjudication.csv` (`id`, `verdict` A|B|neither, `class_found`, `evidence`, `adjudicators`).
   - Then join with `blind_key.csv` and write `review/rounds/0/result.txt`: agreement, sample right, full right, neither, per app and in total.
3. **Re-check the setup-account rows.** Re-check sample rows MMEX-04, MMEX-21, MMEX-29, MMEX-43 and MMEX-44 if they are in the tuning half: the sample may have ignored the setup account. Write each verdict in `result.txt`.
4. **Agents:** the measurement lead, plus 2 adjudicators per disagreement (helper size: 5 rows) and tie-breakers. Expect about 50–60 disagreements, about 25 helper tasks in two waves.
5. **Push** `review/rounds/0/` (coordinator commit: `review round 0: tuning-half agreement N%, adjudication S/F/X`).

### W1. Three switches in the builder (tool lead)

Add three options to `tools/build_graph.py`. Each is **off by default**; only the five apps' `graph_def.py` turn them on. Copy the current file to `tools/build_graph_v10_backup.py` first.

**T1. `SETUP_ONLY = {node, ...}` (pages or methods only the first-run setup shows).**
- While deriving best routes, ignore every edge whose `dst` is in `SETUP_ONLY` or whose `src` is a page in `SETUP_ONLY`.
- A method reachable only through them stays REACHABLE. Its route is then derived with them allowed, and `methods.csv` `note` gets "only during the first-run setup".
- Print `setup-only nodes: N; methods reachable only through them: M` in the build report.

**T2. `RTA = True` (rapid type analysis for bytecode `cha` edges).**
1. After `add_auto_edges`, compute the reachable nodes over all edges (`allow_setup=True`, `allow_env=True`).
2. The instantiated classes are every class C with a reachable `C.<init>` variant. Edges of every kind count: ENTRY, LIFECYCLE, FRAMEWORK, INTENT and non_standard reflection edges create objects too.
3. Drop an auto edge with `dispatch == 'cha'` to method `C.m` unless some instantiated class D (C itself or a subclass) resolves `m` to `C.m`. Use `auto_calls.json` `impl` if it lists inherited methods; otherwise derive the subclass relation from `javap`/`method_list.json`, and say which in a comment.
4. Repeat until nothing changes.
5. Never drop `exact` edges or hand-written edges.
6. Print `RTA: dropped N cha edges in K rounds; methods that lost every route: M` in the build report.

The task note's warning: do **not** require the object to be created on the same route. Creation anywhere reachable is enough.

**T3. `ESR_CREATION = True` (library inherits through reflective creation).**
- `explicit_standard_route` of a method becomes true only if both hold:
  - (a) a route over explicit, standard and page edges reaches it, using env edges only if the method's best route has an env gate;
  - (b) for an instance method of class C (not static, not `<clinit>`; `method_list.json` flags say static): a `C.<init>` variant is reachable under the same restriction.
- So callbacks of an object that only reflection or a library creates in-app become library, even when an exported external entry could also create it.

**Tests (all in a private copy before pushing):**
1. **Switches off.** Rebuild all 13 apps with the new builder and every switch off. Run `python3 -I tools_dev/check_unchanged_apps.py --apps Currency Diary hash-checker Omni-Notes openlauncher Vanilla-Music Markor AnyMemo Aegis AmazeFileManager AnkiDroid MMEX LibreTorrent`; it must print `ALL UNCHANGED` for all 13.
2. **Switches on, in a private copy of the five apps:**
   - AmazeFileManager: `HybridFile$9.execute` loses its route (and needs an UNREACHABLE entry in W4).
   - MMEX: `AccountListFragment.onContextItemSelected` gets `explicit_standard_route` no (library).
   - Aegis, with `SETUP_ONLY` set to the four intro pages: the best route of `KeyDerivationTask.onPostExecute` goes through Settings, not the intro.
3. **Review.** The 2 auditors review the code diff line by line, and one re-runs the tests.

**Push:**
- `tools/build_graph.py` and `tools/build_graph_v10_backup.py` in one commit: `build_graph: SETUP_ONLY, RTA and ESR_CREATION switches (off by default; 13 apps byte-identical with them off)`.
- Then a CI request for all apps. **Accept when** CI shows all 13 apps at 0 errors and 0 warnings, and `check_unchanged_apps.py` for all 13 apps is `ALL UNCHANGED`.

**Agents:** the tool lead, plus 3 helpers (one per switch, writing it against a private copy), plus 2 auditors.

### W2. Baseline and setup-only screens (Aegis, AnkiDroid, MMEX; check the other two)

1. **List** every distinct `needs_state` text on a REACHABLE method's best route, with its count. Save it as `graphs/<App>/scratch/reaudit/state_gates.csv`.
2. **Decide each text.** Can the baseline plus ordinary GUI actions satisfy it? Print the source.
   - **Yes:** clear it through `EDIT` (`needs_state=None`, `state_kinds=[]`), and record the reason and `file:line` in the edge's `note` ("baseline: …").
   - **It only exists during the first-run setup** (an intro or tutorial page): add the page to `SETUP_ONLY`.
   - **No:** keep it.
3. **Expected decisions** (each still confirmed from the printed source):
   - **Aegis:**
     - The two intro gates are cleared, and `S_INTRO_WELCOME`, `S_INTRO_PICKER`, `S_INTRO_SETUP` and `S_INTRO_DONE` go into `SETUP_ONLY`.
     - "The vault is loaded…" and "This MainActivity instance has loaded the entry list" are satisfied by the normal start (unlocking is typing a password, a GUI action).
     - "The vault icons are not marked optimised yet…" needs its source read.
   - **AnkiDroid:** "the deck has cards to study", "a collection file exists" and "a deck exists" are satisfied by the imported sample deck.
   - **MMEX:**
     - "at least one account exists" is satisfied by the setup account.
     - The first-run tutorial goes into `SETUP_ONLY` (default; record it in `MUSE_REAUDIT_QUESTIONS.md`).
     - A gate that needs a second account, an Investment account or transactions stays.
   - **AmazeFileManager and LibreTorrent:** look for first-run screens and gates the same way.
4. **Switch on** `SETUP_ONLY` and the `EDIT` entries in the app's graph files.

**Accept when:**
- the local build has 0 errors;
- no reachable method's best route contains a cleared text or a `SETUP_ONLY` node, except the setup-only methods (script output saved);
- the auditor re-printed 1 text in 3.

**Agents:** per app, 1 helper per 40 gate texts plus 1 auditor per 3 helpers. **Push** per app, after the merge build.

### W3. In-app routes instead of exported or external entries

1. **Launcher entries (LibreTorrent first).**
   - Print the manifest lines of every ENTRY edge with an `exported` env gate.
   - If the activity has the `MAIN`/`LAUNCHER` intent filter, remove the env gate: starting from the launcher is the baseline.
   - Expected: `MainActivity` (`Ef4711e98`, `E558b0012`, `E50191c30`).
2. **Every other exported or external entry with an env gate** (LibreTorrent 13, AnkiDroid 41, MMEX 17, plus the top env-source edges in Appendix A). Find the in-app way to the same code: an explicit `startActivity`, a fragment transaction, a click handler, a ViewModel call, an Rx runnable, an adapter click, a broadcast sent by the app itself.
   - **If it exists:** add the missing in-app edges, with evidence. Keep the external entry with its env gate; the builder will prefer the in-app route.
   - **If not:** keep the env gate and record why.
3. **The notification receiver.** The in-app pause/resume buttons reach the same engine calls as the notification actions (`MainFragment.java:389`, `TorrentDownloadImpl.java:237-239`). Add those in-app edges.
4. **State on the new in-app routes.** If the new route needs a torrent in the list, an item selected or a document created, put that `needs_state` on the GUI edge that needs it (state kind `data` or `session`).

**Accept when:**
- the script "methods whose best route uses an env gate from an exported or external entry" drops, and each remaining case has a recorded reason;
- LibreTorrent-16, -18, -19 and -41 (checked cases) come out as state after W7;
- the local build has 0 errors.

**Agents:** LibreTorrent 1 merger, up to 10 helpers (one per entry-point group) and 3 auditors; the other apps 1 helper per 5 env-source edges and 1 auditor per 3 helpers. **Push** after each merged group.

### W4. Impossible calls (switch on `RTA` per app)

1. Switch on `RTA = True` and build. Save the list of methods that lost every route as `graphs/<App>/scratch/reaudit/rta_lost.csv`.
2. For each one, apply hard rule 3:
   - **No creation anywhere reachable:** add an `UNREACHABLE` entry (`no_trigger_in_app`, a reason like "its class is created only in <method>, which nothing reachable calls", and the evidence).
   - **A missing creation:** add the creation edge.
3. **Impossible calls RTA cannot see** (the type is created, but the call never reaches it): SUPPRESS the edge with printed evidence. Example, Aegis-16: the CHA edge `DatabaseImporter.readFromApp → GoogleAuthUriImporter.getAppPath`. The import-from-app path keeps only importers that support direct import (`DatabaseImporter.java:46, 79-80, 99-101`).
4. **Shared helpers that fan out to one specific target.** Example, MMEX: `MainActivity.showFragment_Internal → AccountListFragment.onActivityCreated` is reached after the Portfolio event, where a PortfolioFragment is shown. Clone the helper per caller (as already done for `@RECURRING`), or move the edge behind the creation of that fragment.

**Accept when:**
- the local build has 0 errors and 0 warnings;
- `HybridFile$9.execute` and `GoogleAuthUriImporter.getAppPath` are UNREACHABLE, with evidence;
- the auditors re-printed 1 entry in 3.

**Agents:** 1 helper per 40 lost methods (grouped by class) and 1 auditor per 3 helpers. **Push** per app.

### W5. Library edges (switch on `ESR_CREATION` per app)

1. Switch on `ESR_CREATION = True`.
2. **List** the edges on the default class whose evidence, trigger or via mentions EventBus, Rx (Flowable, Observable, Single, Completable, subscribe), data binding (`Binding…Impl`, `DataBinderMapper`, `@BindingAdapter`), XML inflation (`inflate`, `PreferenceInflater`, `android:onClick`, XML-declared classes) or reflection (`newInstance`, `Class.forName`, `loadClass`). Include the build report's `REVIEW … edges on the default class mention a library/reflection hint` list.
3. **For each, print the source.** If a library or reflection makes the link, set `cls='non_standard', via='<mechanism> (<file:line>)'`.
4. **LiveData and ViewModel observers:** do **not** change their class. The task note does not name them. Write question Q1 (Appendix D).

**Accept when:**
- MMEX `AccountListFragment.onContextItemSelected` is library;
- every listed edge has a decision in `graphs/<App>/scratch/reaudit/library_edges.csv`;
- the auditors re-printed 1 in 3.

**Agents:** 1 helper per 40 edges and 1 auditor per 3 helpers.

### W6. Outside data the route consumes

For each app, 4 helpers, one per pattern group. Each lists the consuming edges on any route and prints the source:

| Pattern group | What to look for | Env kind |
|---|---|---|
| (a) Results from other apps | `onActivityResult`, ActivityResult launchers with `ACTION_OPEN_DOCUMENT`, `ACTION_CREATE_DOCUMENT`, `ACTION_GET_CONTENT`, `ACTION_PICK`, received `ACTION_SEND`/`ACTION_VIEW` | `other_app` |
| (b) Network and servers | Retrofit, OkHttp, `HttpURLConnection` callbacks, sync clients (AnkiWeb, Yahoo YQL, price providers), SSH/SMB/FTP host responses | `network` |
| (c) Data only older versions write | migration code, legacy fields, version checks | `other`, text "data only an older app version writes" |
| (d) Limits of the API 27 image | features missing on the emulator image | `hardware` or `other` |

Put the env gate on the consuming edge, with the outside source and `file:line` in the text.

**Accept when:**
- Aegis-46, Aegis-47, MMEX-38, AmazeFileManager-12 and AnkiDroid-34 come out as env;
- every decision is in `graphs/<App>/scratch/reaudit/outside_data.csv`;
- the auditors re-printed 1 in 3.

**Agents:** 20 helpers (5 apps × 4 groups) and 7 auditors.

### W7. Guards on the routes (the largest item)

1. **Scope.** After W2 to W6 are merged and built, take the app's never-run methods (section 3.1, point 7) whose class is gui, library or state. List the distinct steps on their best routes (exclude page and ENTERS steps; keep GUI steps) in `graphs/<App>/scratch/reaudit/guard_steps.csv`: edge id, kind, src, dst, cited `file:line`. Starting sizes, before W2 to W6:

   | App | Targets | Code steps | Source files |
   |---|---|---|---|
   | Aegis | 1,604 | 1,909 | 140 |
   | AmazeFileManager | 1,363 | 1,592 | 169 |
   | AnkiDroid | 1,067 | 1,255 | 106 |
   | MMEX | 3,083 | 2,900 | 231 |
   | LibreTorrent | — | — | — |

   LibreTorrent grows after W3. Recompute after W2 to W6.
2. **Pre-screen (tool lead writes `tools_dev/guard_prescreen.py`).** For each step, read the enclosing method in the cited source file. Flag the step when either holds:
   - the call line is inside an `if`, `else`, `switch`, `?:`, loop, `try` or `catch`, or comes after an early `return`, `throw`, `break` or `continue` in the same method;
   - the GUI step needs a list item, a selection or an open dialog.

   Unflagged steps count as unguarded. An auditor re-reads **1 in 20** of them; any miss means the pre-screen rule is widened and rerun. Test the script on the checked cases: MMEX-41 (`PayeeReportFragment.java:216-221`) must be flagged.
3. **Judge the flagged steps** (helpers, grouped by source file, at most 40 steps each). Print the guard and decide with the two conditions in section 5:
   - stored data, files, non-default settings, a UI session or an account → `needs_state` with its kind;
   - another app, the system, network, device, time or older-version data → `env` with its kind;
   - can never hold → dead (UNREACHABLE for the methods only that branch reaches);
   - null checks and always-true guards → nothing.

   Write the gate on the edge (hand edge: `e(...)`; bytecode edge: an `EDIT` entry), with `file:line`.
4. **Merge** per app in batches of at most 40 steps, with a local build after each.

**Accept when:**
- every flagged step has a decision in `graphs/<App>/scratch/reaudit/guard_decisions.csv` (step, decision, gate text, `file:line`, helper, auditor);
- the auditors re-judged 1 in 3 blind, with 0 open mismatches;
- the checked cases MMEX-41, MMEX-49, MMEX-20, AmazeFileManager-01, -27, -46, AnkiDroid-07 and Aegis-47 come out as their `source_class` in `review/checked_cases.csv`;
- the local build has 0 errors.

**Agents:** up to 60–80 helpers in waves, 1 auditor per 3 helpers, 5 mergers. Expect 2,000–4,000 flagged steps.

### W8. Round finish: rebuild, re-verify routes, emulator, measure

Do this after W2 to W7 of a round. **At most 3 rounds**; round 1 covers W2 to W7.

1. **CI** for all 13 apps.
   - Accept when all 13 are at 0 errors and 0 warnings (except W8 point 2's own path warnings while you fix them), and `check_unchanged_apps.py` prints `ALL UNCHANGED`.
2. **Re-verify changed routes.** Every sampled route whose path row now warns ("no longer the best route") or whose edge ids changed is re-verified step by step by **2 independent verifiers**, with every step printed: correct, fixed, wrong or unclear. Their judgments go into `make_verification.py` (never by hand).
   - The stopping rule of the earlier audit still holds for AnkiDroid, Aegis and LibreTorrent: a route drawn WRONG stays WRONG with its reason, unless the re-audit's edits already fixed it.
3. **Emulator.**
   - The device lead updates `device/routes/<App>/ROUTES.csv` and the route scripts for routes that changed.
   - Push `handoff/DEVICE_DRYRUN_REQUEST.txt` for the five apps. Accept when FAIL is 0.
   - Then push `handoff/DEVICE_REPLAY_REQUEST.txt` (the five apps) for one real run. At most one real run per round, and at most 2 in total.
   - Process it with `device/compare.py` and the writers (DEVICE rows: reached gives correct, otherwise unclear, never wrong).
4. **CI** again. Accept as in point 1.
5. **Measure:**
   ```
   python3 -I review/measure.py --sample review/sample_tune --out review/rounds/<n>
   ```
   Then adjudicate every disagreement blind, as in W0 (2 plus a tie-breaker).
6. **Round report** `review/rounds/<n>/result.txt`:
   - agreement before and after;
   - sample right, full right, neither;
   - the confusion table;
   - what changed;
   - which causes still produce wrong labels.
7. **Push** the round.
8. **Start another round** only if the adjudication shows a systematic cause still at work in at least 3 disagreements where the full label is wrong. Otherwise go to W9.

### W9. Audit the reachable labels by class

1. **Draw** after the last round's CI. Tool lead script: `tools_dev/draw_reachable_audit.py`, seed `20261106`.
   - Per app and per class (env, state, library, gui) of REACHABLE methods, draw **15** at random (all if fewer). Exclude methods in `review/sample_tune/` and in the checked cases.
   - Save the draw as `graphs/<App>/scratch/reaudit/audit_draw.csv`, and push it **before** anyone checks a row.
2. **Check.** **2 independent checkers** per method. Each prints the best route's steps and gates, and decides the class from the source with the rubric. When they disagree, a **3rd** decides.
3. **Write** label rows through `make_verification.py`: `result` correct, fixed (wrong, then the graph was corrected), wrong (could not be corrected) or unclear, with `ref` = `file:line` and note "reachable audit, class <X>".
4. **Correct** each wrong label in the graph if you can (W7 style). Then rebuild and run CI.
5. **Report** per app and per class: rows, correct, fixed, wrong, unclear, error rate.

**Agents:** about 300 methods × 2 checkers. Helper size: 5 methods; about 60 agents in waves, plus tie-breakers.

### W10. Finish and publish

1. **Logs** per app:
   - `AGENT_NOTES.md`: `## Current step`, plus a section for this re-audit;
   - `LESSONS.md`: new bullets;
   - `readme_notes.md`: keep the five headings exactly; update "What waits for a device" and add the re-audit's changes under the first heading.
   - Nothing that `tools_dev/check_terms.py` flags.
2. **README template.** Rewrite the "Known problems" section of `tools/results_templates/root_readme.md`:
   - what was fixed;
   - the tuning-half agreement (round 0, last round) and the adjudication counts;
   - the reachable-audit error rates;
   - what still remains;
   - one line: "The held-out half of the sample is measured once by the reviewer."

   Update the matching line in `run_result.md`. Both are generated through `tools/pack_results.py`, which refuses anything `tools_dev/check_terms.py` flags.
3. **Summary.** Write `handoff/MUSE_REAUDIT_SUMMARY.md`, one section per app:
   - CI commit, methods, REACHABLE, UNREACHABLE by kind;
   - class shares before and after (weighted with `review/measure.py`'s app weights, over the never-run methods);
   - changes per cause (W2 to W7 counts);
   - routes re-verified;
   - device run;
   - reachable audit;
   - rounds.
4. **Final CI** for all 13 apps. Accept when G1 to G8 hold.
5. **Publish.** Push `handoff/PUBLISH_REQUEST.txt` with a new line 2. Add `run_of_record <run id>` if W8 made a newer emulator run the one to publish.
   - Wait for the `[publish]` commit, or for the workflow's success if nothing changed.
   - Check that `result` and `work-2026-10-31` point to the same commit.
   - If the workflow fails, read its log, fix the cause (never the workflow), and push the request again.
6. **Final message** (at most 15 lines):
   - CI commit and the published commit;
   - tuning-half agreement, round 0 and last round;
   - adjudication counts;
   - reachable-audit error rates;
   - anything blocked;
   - "ready for the reviewer's held-out measurement".

---

## 7. What to tell nobody and never write

- **Never name where the sample comes from** (no publication, venue or project names) and never quote results of that work, anywhere in the repository: files, notes, commit messages, READMEs. `tools_dev/check_terms.py` flags such lines.
- **The sample:** "an independent hand-labelled sample of 50 unreached methods per app".
- **The reviewer:** "the external review of 3 November 2026".

---

## 8. Agent counts per item (targets; never exceed what the checks can absorb)

| Item | Helpers | Auditors | Others | Helper task size |
|---|---|---|---|---|
| W0 adjudication | about 25 tasks × 2 agents | — | measurement lead, tie-breakers | 5 rows |
| W1 switches | 3 | 2 | tool lead | one switch |
| W2 baseline | 1 per 40 gate texts per app (about 5–10) | 1 per 3 helpers | 5 mergers | 40 gate texts |
| W3 in-app routes | LibreTorrent up to 10; others 1 per 5 env-source edges (about 10) | 3 + 1 per 3 helpers | mergers | one entry-point group or 5 edges |
| W4 RTA | 1 per 40 lost methods | 1 per 3 helpers | mergers | 40 methods, grouped by class |
| W5 library edges | 1 per 40 edges (about 6–8) | 1 per 3 helpers | mergers | 40 edges |
| W6 outside data | 20 | 7 | mergers | one app × one pattern group |
| W7 guards | 60–80 in waves | 1 per 3 helpers, plus 1-in-20 pre-screen audit | tool lead (pre-screen), mergers | 40 flagged steps, one source file group |
| W8 re-verify routes | 2 per changed route | — | device lead | 3 routes |
| W8 adjudication | 2 per disagreement | — | measurement lead | 5 rows |
| W9 reachable audit | about 60 tasks × 2 agents | — | tie-breakers | 5 methods |

**Throughput limits:**
- at most 20 connector requests per minute across all agents (on HTTP 429, wait 60 seconds);
- CI at most once per 10 minutes;
- dry runs at most once per 15 minutes;
- real emulator runs at most once per round.

**A stuck helper** (no output for 30 minutes): give its task to a new helper. If that one stalls too, write it under `## Blocked` and continue.

**If agents or credit run low,** finish in this order: the open merges (never leave a half merge), then W8 for the current round, then W10.

---

## 9. Pushing: when, what, how (no approval needed)

### 9.1 How

Use your connector, to branch `work-2026-10-31` only, with the identity in 3.3 rule 8. Refresh the file from the branch before every push. Never push two changes to the same file at once.

### 9.2 When (automatic)

- after every merged batch that builds locally without new errors;
- after every finished work item for an app;
- after every round report;
- at least every 60 minutes while work goes on;
- immediately before you stop for any reason.

### 9.3 Never push

- a file that fails `py_compile`;
- a build with more errors than before the batch;
- a tools change before its switches-off test passed (W1).

### 9.4 Paths you may write

- the five apps' `graphs/<App>/graph_def.py`, `graph_def_mod/*.py`, `parts/*` (LibreTorrent), `make_verification.py`, `verification.csv` (writer only), `readme_notes.md`, `LESSONS.md`, `AGENT_NOTES.md`, `scratch/**` (not `scratch/ci_latest/`);
- `device/routes/<App>/**` for the five apps;
- `review/rounds/**`;
- `tools/build_graph.py`, `tools/build_graph_v10_backup.py`, `tools_dev/*.py` (tool lead);
- `tools/results_templates/root_readme.md` and `run_result.md` (W10 only);
- `handoff/MUSE_RUN_LOG.md`, `MUSE_DECISIONS.md`, `MUSE_REAUDIT_QUESTIONS.md`, `MUSE_REAUDIT_SUMMARY.md`;
- `handoff/REBUILD_REQUEST.txt`, `DEVICE_DRYRUN_REQUEST.txt`, `DEVICE_REPLAY_REQUEST.txt`, `PUBLISH_REQUEST.txt`.

### 9.5 Never write

- the other eight apps' folders, and their `device/routes/`;
- `graphs/*/out/**`, `graphs/*/scratch/ci_latest/**`, `device/results/**`, `device/dryrun/**` (CI writes these);
- `run_result/**` and `README.md` (the publish workflow writes these);
- `.github/`, `handoff/ci/`, `handoff/connector_kit/`, `final_java_only/`, `fw_src/`, `review/TASK_NOTE.md`, `review/sample_*`, `review/checked_cases.csv`, `review/measure.py`.

### 9.6 Commit messages

- **Graph changes:** `<App> W<n>: <what> (local build: methods N, REACHABLE R, UNREACHABLE U, errors E, warnings W)`
- **Rounds:** `review round <n>: tuning-half agreement N%, adjudication S/F/X`
- **Requests:** `CI rebuild request: <apps>, <purpose>`; `Device dry-run request: …`; `Device replay request: …`; `Publish request: …`

### 9.7 Request files

Each has line 1 unchanged, line 2 `# request <UTC time> <purpose>` (new every time), then the apps, one per line, or `all`.
- `handoff/REBUILD_REQUEST.txt` → CI (commit `[ci] rebuild and checks`)
- `handoff/DEVICE_DRYRUN_REQUEST.txt` → dry run (commit `[device] dryrun <run>`)
- `handoff/DEVICE_REPLAY_REQUEST.txt` → real emulator run (commit `[device] results <run>`)
- `handoff/PUBLISH_REQUEST.txt` → publish to `result` (commit `[publish] …`; no app lines)

If no bot commit appears within 30 minutes, push the request again with a new line 2. That has happened once.

---

## 10. State, logs, resets

- **Run log.** One line per step in `handoff/MUSE_RUN_LOG.md`: UTC time, item, app, what, local build or CI commit, counts.
- **Per app.** `AGENT_NOTES.md` keeps `## Current step`. A `WORKING_LOCK` file younger than 30 minutes means another worker is active: do not start a second one.
- **Decisions** go in `handoff/MUSE_DECISIONS.md`, in your own name (never in the reviewer's or anyone else's).
- **Questions** go in `handoff/MUSE_REAUDIT_QUESTIONS.md`, each with the default you used; then carry on.
- **On every start or reset:**
  - re-read this file;
  - read the last 30 lines of the run log and each app's `## Current step`;
  - pull;
  - check for `review/sample_tune/`;
  - continue. Never redo finished work.
- **On a usage, session or rate limit:** start no new helpers, finish or revert the open merge, save the current step, push, and stop.

---

## 11. Acceptance gates (all on the final official CI)

| Gate | Holds when |
|---|---|
| G1 | The five apps: 0 errors, 0 warnings, check 2 at 0 problems, check 4 at 0, `STRICT = True`, `readme: wrote`. |
| G2 | `python3 -I tools_dev/check_unchanged_apps.py` prints `ALL UNCHANGED` (the other eight apps). |
| G3 | No reachable method's best route in the five apps contains: an env gate from an exported or external entry where an in-app entry exists (each remaining one has a reason in `MUSE_DECISIONS.md`); a cleared baseline text; a `SETUP_ONLY` node, except for setup-only methods. |
| G4 | Every checked case in `review/checked_cases.csv` has the `source_class` as its full-label class. Exceptions need a reason and printed source in `MUSE_DECISIONS.md`; AmazeFileManager-05 follows the rubric (rotation is a GUI action). |
| G5 | No path row is stale: no "no longer the best route" or "edge … no longer exists" warnings. Every changed sampled route was re-verified by 2 verifiers. |
| G6 | The reachable audit rows exist: 15 per class per app (or all), 2 checkers each, with error rates reported. |
| G7 | `review/rounds/0/` and the last round's folder exist, each with `agreement.txt`, `adjudication.csv` and `result.txt`. |
| G8 | Every writer is deterministic; every `readme_notes.md` has its five headings; logs are present; `python3 -I tools_dev/check_terms.py --since 46682745` prints `nothing flagged`. |
| G9 | The publish workflow succeeded; `result` and `work-2026-10-31` point to the same commit; `tools_dev/check_terms.py README.md run_result/README.md` prints `nothing flagged`. |
| G10 | `handoff/MUSE_REAUDIT_SUMMARY.md` is written, and the final message is sent. |

---

## Appendix A. Where the env gates come from now (top sources, CI `57d051a0`)

Counted over never-run methods whose class is env:

| App | Distinct env-source edges | Largest |
|---|---|---|
| LibreTorrent | 9 | `S_ENTRY → MainActivity.onCreate` (1,089 methods), `S_ENTRY → NotificationReceiver.onReceive` (357) |
| AnkiDroid | 63 | `S_ENTRY → CardContentProvider.query` (27), `TranslationActivity.translate → TranslationActivity$BackgroundPost.doInBackground` (22) |
| Aegis | 28 | `VaultManager.fireIntentLauncher → MainActivity.lambda$new$7` (41), `S_PROCESS → PanicResponderActivity.<init>` (21) |
| MMEX | 26 | `S_ENTRY → SmsReceiverTransactions.<init>` (21), `RecurringTransactionBootReceiver → RecurringTransactionReceiver.<init>` (6) |
| AmazeFileManager | 5 | `S_ENTRY → TextEditorActivity.<init>` (21), `ProcessViewerFragment.onResume → …CustomServiceConnection` (5) |

## Appendix B. The 23 checked cases (until `review/checked_cases.csv` arrives)

| Case | Target | Sample | Full label | Source |
|---|---|---|---|---|
| Aegis-16 | `GoogleAuthUriImporter.getAppPath` | dead | state | dead |
| Aegis-38 | `KeyDerivationTask.onPostExecute` | gui | state | gui |
| Aegis-39 | `KeyDerivationTask$Result.<init>` | gui | state | gui |
| Aegis-46 | `Vault.setGroupsMigrationFresh` | env | state | env |
| Aegis-47 | `VaultBackupManager.createBackup(File,Uri)` | env | state | env |
| AmazeFileManager-01 | `DatabaseViewerActivity.getDbTableNames` | state | gui | state |
| AmazeFileManager-05 | `TextEditorActivity.onSaveInstanceState` | state | env | state or gui (rotation is GUI) |
| AmazeFileManager-12 | `SshAuthenticationTask.onPostExecute` | env | gui | env |
| AmazeFileManager-20 | `HybridFile$9.execute` | env | gui | dead |
| AmazeFileManager-27 | `SingletonUsbOtg.getUsbOtgRoot` | env | gui | state |
| AmazeFileManager-46 | `FileUtils.installApk` | state | gui | state |
| AnkiDroid-07 | `BackupManager.repairCollection` | env | gui | state |
| AnkiDroid-34 | `Media.syncDelete` | env | gui | env |
| LibreTorrent-16 | `NoFilesSelectedException.<init>` | state | env | state |
| LibreTorrent-18 | `TorrentEngine.makeTrackerInfoList` | state | env | state |
| LibreTorrent-19 | `TorrentEngineListener.onTorrentPaused` | state | env | state |
| LibreTorrent-41 | `DetailTorrentFilesFragment.subscribeAlertDialog` | state | env | state |
| MMEX-03 | `AccountListFragment.onContextItemSelected` | state | gui | library |
| MMEX-20 | `StockRepository.insert` | state | library | state |
| MMEX-29 | `HomeFragment.getAccountBeingBalanced` | state | library | library |
| MMEX-38 | `YqlSecurityPriceUpdaterRetrofit.getPricesFromJson` | env | state | env |
| MMEX-41 | `PieChartFragment.onValueSelected` | state | gui | state |
| MMEX-49 | `CheckingTransactionEditActivity.loadScheduledTransaction` | state | gui | state |

The evidence for each case is in `review/checked_cases.csv` once it arrives, and in `review/TASK_NOTE.md` sections 1 to 5.

## Appendix C. Commands

```
# build one app; build plus all checks
python3 -I tools/build_graph.py graphs/<App> <prefix>
bash handoff/ci/rebuild.sh <App>            # or: all

# the other eight apps unchanged (after a local rebuild of them, or a pull of a CI commit)
python3 -I tools_dev/check_unchanged_apps.py

# measure against the tuning half
python3 -I review/measure.py --sample review/sample_tune --out review/rounds/<n>

# regenerate run_result and the READMEs locally (the publish workflow does this for real)
python3 -I tools/pack_results.py .
git restore --worktree -- run_result README.md   # do not push them yourself

# writers: run twice, compare
python3 -I graphs/<App>/make_verification.py && md5 graphs/<App>/verification.csv
```

## Appendix D. Open questions, with the default to use until answered

| # | Question | Default |
|---|---|---|
| Q1 | Do LiveData observer callbacks count as library edges? | No change (keep their current class). |
| Q2 | MMEX's first-run tutorial: is it a setup-only screen like Aegis's intro? | Yes, add it to `SETUP_ONLY`. |
| Q3 | Is the Aegis setup vault encrypted? | Unlocking is typing the password, a GUI action, so it is never state. |
| Q4 | Markor's onboarding is part of the baseline, but Markor is not in this job. | Do not touch Markor; count how many Markor best routes pass its intro and report it in the summary. |

Write each answer you get from the user in `MUSE_DECISIONS.md`.
