# Re-audit and fix the labels of five apps

(The reviewer's task note of 2026-11-05, public copy; its file table refers to the files in this folder.)

Apps: Aegis, AmazeFileManager, AnkiDroid, LibreTorrent, MMEX.
Labels in question: `run_result/apps/<App>/graph/methods.csv` on branch `result` (7b4d495e).

There is no deadline. Do this when it suits you, and in any order.

## Goal

The dead/unreachable verdicts are good. The problem is the split of the other methods into env, state, library, and gui.

On 249 sampled targets, the labels agree with an independent sample on only 59% of the classes. Source checks of 23 disagreements found two systematic errors:

- **Too much gui.** Many targets labelled gui need state, the environment, or are dead.
- **Too little state.** Many targets labelled env have an in-app route that needs only state.

The goal is to fix the causes in the pipeline, re-derive the labels, and audit the reachable labels, not only the dead ones.

## Files in this folder

| File | What it is |
|---|---|
| `sample/<App>.csv` | 50 randomly drawn unreached methods per app, labelled by hand from the source. Columns: `class`, `sub_class`, `reason`, `evidence` (file:line), `route`. Paths are relative to each app's source root. |
| `checked_cases.csv` | 23 sample targets where the sample and your labels disagreed, decided again from the source. `right` says which label held (`sample` 17, `full label` 2, `neither` 4). `source_class` is the class the source supports. |

Columns of `sample/<App>.csv`:

- **`device_check` and `device_result`:** Where `device_result` is filled, the route was tried on the emulator. `hit` means JaCoCo recorded the method; 98 of 99 tried routes hit.
- **`jvm_class`, `method`, and `desc`:** Together these identify the method. They should match your new `jvm_class` column.

**App weights.** To compare class shares across apps, weight each app by its number of unreached targets in the sampling frame:

| App | Unreached targets |
|---|---|
| Aegis | 897 |
| AmazeFileManager | 1,012 |
| AnkiDroid | 1,633 |
| LibreTorrent | 1,510 |
| MMEX | 1,495 |

## Setting (the baseline)

The setting is the instrumented debug build on an Android 8.1 (API 27) emulator, started from a fresh install plus the first-run setup:

- **Aegis:** onboarding passed, and a vault with two entries.
- **MMEX:** a database with one checking account.
- **AnkiDroid:** a sample deck imported.
- **Markor:** onboarding passed.

Anything the first-run setup creates is part of the baseline and never counts as state.

Runtime-permission prompts count as GUI actions.

## Class rule

Assign the first class that applies:

| Class | When |
|---|---|
| dead | Nothing in this build can execute it: no caller, a framework that never calls the override, or a condition that can never hold. |
| config | Runs only in another build or on another API level. |
| env | Needs something outside the app: another app or the system (picker results, shares, widgets, broadcasts), network or servers, device, time, data left by an older app version, or limits of the API 27 image. |
| state | Reachable from the GUI, but only after in-app actions create state: stored data, a file or document, a non-default setting, a UI session (a selection, an open dialog, an unsaved form), or an account or vault. |
| library | Reachable only through an edge that a library or reflection creates. Examples: EventBus, Rx, data binding, a class inflated from XML, `Class.newInstance`. |
| gui | Reachable with GUI actions alone. Long press, drag, text input, and rotation are GUI actions. |

**Best-route rule.** A gate counts only if no other route avoids it. Choose the route with the fewest env gates first, then the fewest state gates.

## What to fix, in suggested order

Each item lists the cases in `checked_cases.csv` that show it.

### 1. Exported or external entries instead of the in-app route

**Cases:** LibreTorrent-16, -18, -19, -41.

The best route starts at an exported activity or a notification receiver and gets an env gate, although the app itself can reach the target. Here, adding a torrent in the app (a typed magnet works offline) and then the in-app pause button.

**Fix:**
- Add the missing in-app edges: UI handler → ViewModel → engine, Rx runnables, adapter clicks.
- Gate an exported entry as env only when no in-app entry exists.

### 2. One-time intro screens

**Cases:** Aegis-38 and Aegis-39.

The best route goes through the first-start intro. After the setup, the intro never appears again, and Settings > Security reaches the same code without any gate.

**Fix:** Start routes from the state after the first-run setup. Do the same for other apps with intro screens.

### 3. Calls that cannot happen, and reflection

**Cases:** AmazeFileManager-20, Aegis-16, MMEX-03.

**Dispatch to types that are never created.** `HybridFile$9` is created only inside the no-arg `getInputStream()`, which nothing calls, yet a class-hierarchy edge lets other routes dispatch to it.

**Fix:** Dispatch a virtual call only to types that are instantiated in some reachable method (RTA-style).

Do not require the object to be created on the same route. Objects are often created on another screen, in an earlier run, or by the framework, for example:
- fragments restored by the FragmentManager;
- objects rebuilt from a Parcel;
- singletons.

Requiring creation on the route would turn real calls into false dead verdicts.

**MMEX-03.** You are right that the reflective edge `showFragment(Class) → AccountListFragment.<init>` is already non_standard. Two further things still produce the gui label:

- **Shared helper.** The "fragment shown" edge from the shared helper `showFragment_Internal` applies to every fragment. The stored best route uses it after the Portfolio event, where the fragment shown is a PortfolioFragment.
- **Drawer route.** The real route, Drawer > Entities > Accounts → `showFragment(Class)` → … → `showFragment_Internal` → `onActivityCreated`, uses only explicit and standard edges. The reflective creation sits on a side edge that the route never crosses.

**Fix:** Callbacks of an object that exists only through reflection should inherit the non_standard class of its creation edge. The expected class of MMEX-03 is then library.

Two ways this can go wrong:
- If the analysis ignores the reflective creation instead, the only remaining route is the exported AccountListActivity, and the label becomes env, which is also wrong.
- Cloning the helper per caller, as already done for `@RECURRING`, removes the impossible Portfolio edge but leaves the real drawer route. On its own it does not change the class.

### 4. Outside data that the route consumes

**Cases:** Aegis-46, Aegis-47, MMEX-38, AmazeFileManager-12, AnkiDroid-34.

**Fix:** Mark these as env on the edge that consumes them:
- results returned by another app, such as the DocumentsUI picker;
- data that only older app versions write;
- responses from a server, such as the Yahoo YQL response, a live SSH host key, or AnkiWeb sync.

### 5. Guards on the route

**Cases:** MMEX-41, MMEX-49, MMEX-20, AmazeFileManager-01, -27, -46, AnkiDroid-07, Aegis-47.

This is the largest source of errors: 6 of the 10 wrong gui labels in the checks come from it. The derived best route ignores guards.

**Fix:** Turn a guard into a gate only when both hold:

1. The baseline plus ordinary GUI actions cannot satisfy it.
2. No other route avoids it.

Classify the gate by what satisfies it:
- stored data, files, non-default settings, a UI session, an account → state;
- another app, the system, network, device, time, data from older versions → env;
- a guard that can never hold → dead.

Do not count null checks or similar guards that always hold in normal use.

Intent extras count as env only when the Intent comes from outside the app. Extras that the app's own screens set are part of the in-app route.

**Scope.** For the class shares, only the routes of unreached methods labelled gui, library, or state matter. Screen those first rather than every step of every route.

### 6. After each round

1. Rebuild the graph and re-derive the labels.
2. Re-check the routes that changed.
3. Rerun the emulator replay if it helps.
4. Measure as described in the next section.

## How to measure

**Hold out part of the sample.** Do not tune against all 250 targets. Before looking at the results, split them by a fixed rule and keep one part untouched until the end. For example, use one or two whole apps, or every second id. Agreement on targets you tuned against will look better than it is.

**The sample is a reference, not ground truth.** The checks found it wrong in 6 of the 23 cases:
- AmazeFileManager-05: depends on whether rotation counts; under the rule above it does.
- AmazeFileManager-20, AmazeFileManager-27, AnkiDroid-07, MMEX-03, MMEX-29.

It is also known to:
- **Ignore MMEX's setup account.** Re-check MMEX-04, MMEX-21, MMEX-29, MMEX-43, and MMEX-44: their reasons say an account is needed, and the setup provides one.
- **Miss EventBus and reflection edges** in places.
- **Sometimes not check whether the method's own caller is reachable.**

**Report two numbers per round:**
1. Class agreement with the held-out sample.
2. For the disagreements, which side the source supports. Decide each from the source, citing file:line.

Agreement alone cannot show which side improved.

**Audit the reachable labels.** The current audit log checks every unreachable method's label, but only 25–30 reachable methods per app. A useful audit draws reachable labels by class (env, state, library, gui) and checks the class, not only whether a route exists.

**Map labels to classes** with the first applicable of:

1. dead or config: verdict UNREACHABLE, split by `unreachable_kind`.
2. env: `env_kinds` other than `permission`.
3. state: `state_kinds`.
4. library: `explicit_standard_route` = no.
5. gui: everything else.

## Publishing

You may put these files and a summary of the findings in your public repository. Describe the sample only as an independent hand-labelled sample of 50 unreached methods per app.
