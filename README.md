# Ground-truth trigger graphs for 13 Android apps: results

This branch holds the finished ground truth for 13 Java-only Android apps. All work is here: the trigger graphs, the audit logs, the automated checks, the route scripts, and the emulator run that replayed the routes.

**Status on 2026-11-03: all 13 apps are complete.** In the official CI, every graph builds with 0 errors and 0 warnings, and the citation and bytecode checks report 0 problems. The emulator run on Android 8.1 (API 27) is done, and its results are written into every app's audit log.

**Start here:** [`run_result/`](run_result/) is a tidy copy of every final result, with one folder per app and one for the emulator job. The rest of the branch is the full working record behind those results.

---

## What is done

| Step | Status | Where |
|---|---|---|
| Trigger graph (schema 2) for every app | done, 13 of 13 | [`run_result/apps/<App>/graph/`](run_result/apps/), live copy in `graphs/<App>/out/` |
| Audit against Yang's rules (labels, ENV and STATE gates, edge classes, routes, API 27) | done, 13 of 13, each app ticked by the user | [`handoff/PROGRESS_V2.md`](handoff/PROGRESS_V2.md) |
| Audit log per app | 5,118 label rows, 753 edge rows, 389 route rows | `run_result/apps/<App>/verification.csv` |
| Eight automated checks, run by the official CI | 13 of 13 at 0 errors, 0 warnings (CI request `9c51c99c`) | `run_result/apps/<App>/ci/` |
| Route scripts for the emulator | 389 routes: 355 scripted, 34 unscriptable (reason recorded) | `device/routes/<App>/`, list in `run_result/apps/<App>/routes.csv` |
| Emulator run on GitHub Actions (API 27) | done 2026-11-03, run `41593209101-1`: 104 of 389 routes reached, 100 confirmed (DEVICE_OK) | [`run_result/emulator/`](run_result/emulator/) |
| Emulator results written into the audit logs | done; a route that was not reached never changes a label | `verification.csv` rows with `confirmed_by=DEVICE` |

## The numbers

**29,024 methods and 63,008 edges in 13 graphs: 24,304 methods REACHABLE, 4,720 UNREACHABLE.**

| App | Methods | Edges | REACHABLE | UNREACHABLE | Label errors found | Edge errors found | Route errors found | Emulator: reached | DEVICE_OK |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Currency | 145 | 393 | 140 | 5 | 23 of 47 (0.489) | 0 of 20 (0.000) | 1 of 24 (0.042) | 18 of 28 | 17 |
| Diary | 286 | 1,435 | 265 | 21 | 7 of 51 (0.137) | 0 of 37 (0.000) | 7 of 25 (0.280) | 16 of 30 | 16 |
| hash-checker | 529 | 1,314 | 507 | 22 | 2 of 52 (0.038) | 26 of 35 (0.743) | 13 of 37 (0.351) | 23 of 37 | 23 |
| Omni-Notes | 1,456 | 3,803 | 1,202 | 254 | 7 of 288 (0.024) | 34 of 49 (0.694) | 30 of 33 (0.909) | 8 of 33 | 8 |
| openlauncher | 900 | 1,515 | 728 | 172 | 0 of 199 (0.000) | 3 of 37 (0.081) | 1 of 27 (0.037) | 5 of 27 | 5 |
| Vanilla-Music | 1,473 | 3,429 | 1,325 | 148 | 0 of 178 (0.000) | 10 of 80 (0.125) | 19 of 30 (0.633) | 8 of 30 | 5 |
| Markor | 2,864 | 6,891 | 2,450 | 414 | 48 of 445 (0.108) | 40 of 82 (0.488) | 17 of 30 (0.567) | 7 of 30 | 7 |
| AnyMemo | 2,207 | 4,492 | 1,966 | 241 | 0 of 271 (0.000) | 7 of 45 (0.156) | 0 of 30 (0.000) | 5 of 30 | 5 |
| Aegis | 2,995 | 6,430 | 2,537 | 458 | 1 of 472 (0.002) | 0 of 26 (0.000) | 1 of 14 (0.071) | 1 of 25 | 1 |
| AmazeFileManager | 2,981 | 7,747 | 2,512 | 469 | 25 of 499 (0.050) | 10 of 14 (0.714) | 25 of 30 (0.833) | 0 of 30 | 0 |
| AnkiDroid | 4,186 | 9,815 | 3,275 | 911 | 3 of 941 (0.003) | 0 of 232 (0.000) | 3 of 30 (0.100) | 0 of 30 | 0 |
| MMEX | 4,270 | 8,441 | 3,430 | 840 | 8 of 868 (0.009) | none checked | 8 of 28 (0.286) | 6 of 30 | 6 |
| LibreTorrent | 4,732 | 7,303 | 3,967 | 765 | 9 of 792 (0.011) | 25 of 78 (0.321) | 9 of 27 (0.333) | 7 of 29 | 7 |
| **Total** | 29,024 | 63,008 | 24,304 | 4,720 | 133 of 5,103 (0.026) | 155 of 735 (0.211) | 134 of 365 (0.367) | 104 of 389 | 100 |

How to read the table:
- **"Errors found"** counts items found wrong when they were checked by hand against the source code. Nearly all were corrected afterwards: 120 labels, 155 edges and 120 routes were fixed.
- **Items still wrong:** 13 labels and 14 routes. These are in AnkiDroid, Aegis and LibreTorrent, where the agreed stopping rule allowed no further fix rounds, plus 1 Omni-Notes route. Each is a row with `result=wrong` in that app's `verification.csv`, and the routes show path status WRONG in the graph.
- **Rates:** each rate is errors found ÷ items checked. Each route is counted once.
- **Emulator columns:** "reached" means the emulator's coverage data shows the route's target method actually ran. "DEVICE_OK" means it was reached **and** the whole route script ran to the end.
- **What the label rates cover:** in Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX, 94–97% of the label rows are UNREACHABLE methods. Only 25–30 reachable methods per app were audited, so these apps' label rates mostly measure the dead verdicts, not the state, env and GUI labels of reachable methods (see "Known problems" below).

Route status over all reachable methods: DEVICE_OK 100, SOURCE_OK 214, WRONG 14, UNCHECKED 23,976. "UNCHECKED" means that method's route was not confirmed, either by hand or on the emulator. It does not mean the route is wrong.

## Known problems: state, env and GUI labels in five apps

A review on 3 November 2026 compared the labels of Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX with an independent hand-labelled sample of 50 unreached methods per app, and checked 23 disagreements against the source. We re-checked the review: it read our labels correctly in all 23 cases, and 6 of 6 cases we checked in the source agreed with it.

- **The finding.** On the 249 sampled methods, our labels agree with the sample on only 59% of the classes. Two errors are systematic:
  - **too much gui:** many methods labelled gui need state or the environment, or are dead;
  - **too little state:** many methods labelled env have an in-app route that needs only state.
- **The causes**, all in how the best route is derived:
  - conditions on the route are ignored (for example an empty report, or a menu that exists only for Investment accounts);
  - some routes start from an exported or external entry although an in-app route exists;
  - some call edges cannot occur at run time (calls dispatched to types that are never created);
  - data from other apps, older app versions or servers is missed;
  - one-time intro screens are used as routes.
- **What holds up:** the dead verdicts. 57 of the 58 sampled methods our labels mark dead are dead in the sample too.
- **Until these are fixed,** use the state, env and GUI split of reachable methods in these five apps with care. The verdicts (REACHABLE or UNREACHABLE) are not affected. A re-audit of the five apps is planned.

Since the review, `methods.csv` has a `jvm_class` column with each method's full JVM class name. The `method` key adds a package prefix only where simple class names clash, so match on `jvm_class` and `jvm_descriptor` when joining with other data.

## How the graphs were built and checked

1. **Graph.** Each app's graph is defined in `graphs/<App>/graph_def.py` and built by `tools/build_graph.py`; the format is described in [`handoff/SCHEMA_V2.md`](handoff/SCHEMA_V2.md).
   - Every method gets a verdict: REACHABLE, or UNREACHABLE with a reason (`branch_never_taken`, `framework_never_calls`, `no_trigger_in_app`).
   - Every edge carries an edge class (explicit, standard, non_standard, page) and evidence that cites a source line, from the app or from the Android 8.1 framework source in `fw_src/`.
   - Every reachable method gets a best route from app launch, with its ENV and STATE gates.
2. **Audit.** Labels, edges and a stratified sample of about 30 routes per app were checked by hand against the source. Each check is one row in `verification.csv`, with its result (correct, fixed, wrong, unclear), the source lines read, and a note.
3. **Eight automated checks** (`handoff/ci/rebuild.sh`), run by the official CI on GitHub Actions whenever a rebuild is requested:

   | Check | What it does |
   |---|---|
   | 1 | Build, with 0 errors and 0 warnings required |
   | 2 | Every source citation resolves to a real file and line |
   | 3 | Suspicious routes are flagged for reading by hand |
   | 4 | Every bytecode-cited line really shows the callee |
   | 5–7 | No legacy, memory-only or pending evidence is left |
   | 8 | UNREACHABLE methods that still have a caller in the bytecode are listed for review |

   AnyMemo's single check-3 flag was read by hand and is correct (see its `readme_notes.md`).
4. **Tool coverage is never evidence for a label.** Coverage from automated testing tools appears only as a sanity check.

## The emulator job

Every route was replayed on a real Android 8.1 (API 27) emulator in GitHub Actions: one job per app, all 13 in parallel, about 31 minutes in total.
- **Setup:** the Google APIs x86 image, and each app's instrumented debug build.
- **How a route counts as reached:** after each route, JaCoCo coverage shows whether the route's target method ran.

**Result:** 104 of 389 routes reached (26.7%), and 100 of them ran the whole script (DEVICE_OK).
- Highest: Currency 18/28, hash-checker 23/37, Diary 16/30.
- Lowest: AmazeFileManager 0/30, AnkiDroid 0/30, Aegis 1/25.
- **Most misses come from first-start states**, not from the graphs. For example, AnkiDroid opens on its settings screen, Amaze crashes on start, and Markor shows an intro screen.
- **A miss is recorded as "unclear", never "wrong"**, and it never changes a label.

The full results, all 8 runs (7 attempts that led to the working run), 10 dry runs and the per-route logs are in [`run_result/emulator/`](run_result/emulator/).

## Limits

- **Reach is one run.** 26.7% of routes reached is a single run, and repeats vary by a route or two per app. A higher share would need app-specific setup (sample data, preset settings) for the apps with the lowest share.
- **"Reached" is a weaker claim than "the drawn route was walked".** For 4 routes the target method ran although the script stopped early (Currency route_05; Vanilla-Music routes 05, 23 and 25). Their emulator row says the method ran, but their route keeps its earlier status.
- **Some code was never read.** Library code and other apps' code that were not available are marked INFERRED in the evidence, never SOURCE.
- **The state, env and GUI labels of Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX have known errors.** See "Known problems" above.

## Where everything is

| Folder | What it holds |
|---|---|
| [`run_result/`](run_result/) | **the final results** (frozen copy from commit `7ed4e78b`; see its README) |
| `graphs/<App>/` | the live working folder per app: `graph_def.py`, `out/` (graph outputs), `verification.csv`, `make_verification.py` (writes the audit log), `readme_notes.md` (notes per app), `AGENT_NOTES.md` (work log), `scratch/` (working files and the latest CI output) |
| `device/` | the emulator side: route lists and scripts (`routes/`), harness, runner (`run_app.sh`), collect and compare tools, all run results (`results/`) and dry runs (`dryrun/`) |
| `.github/workflows/` | `rebuild-graphs.yml` (the official checks) and `device-replay.yml` (the emulator job) |
| `tools/` | graph builder, README generator, the checks, sampling and helper tools (`*_backup.py` are earlier versions) |
| `handoff/` | rules, schema, progress list, handovers, reports and run logs of the agents that did the work |
| `final_java_only/` | source code and method lists of the 13 apps (no APKs) |
| `fw_src/` | Android 8.1.0_r1 framework source used for citations |
| `emulator_tests/`, `share_example/`, `tools_dev/`, `.agents/` | earlier test plans, the original output example, development tools and agent settings |

Starting a run:
- **Official checks:** push `handoff/REBUILD_REQUEST.txt` to the work branch.
- **Emulator:** push `handoff/DEVICE_DRYRUN_REQUEST.txt` for a dry run, or `handoff/DEVICE_REPLAY_REQUEST.txt` for a real run.

Both workflows react only to pushes on `work-2026-10-31`. This branch, `result`, is the published copy of it.
