# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# AnkiDroid WP2 — Hooks.runFilter / AdvancedStatistics.runFilter route check (PROPOSAL)

Status: **PROPOSAL ONLY — not merged, not pushed, no repo file edited.**
Scope: **only** the `Hooks.runFilter` / `AdvancedStatistics.runFilter` pair and its
upstream chain into `Stats.calculateDue`. No LibreTorrent, AmazeFileManager, MMEX,
or Aegis work. No edit to `graph_def.py`, `out/`, `progress`, `tools`, or any
other helper's files was made by this helper.

Evidence rule applied throughout: `confirmed_by` is SOURCE only for lines printed
in this session (local files in `~/workspace/wp2-ankidroid/` or the four spaced
GitHub connector fetches listed below); anything else is INFERRED. No tool
coverage, old generated graphs, or build counts are used as evidence for any
label or edge here.

## Sources printed in this session

Local (already on this VM, first phase, no fetch):

- `Hooks.java` — constructor gate, `addHook`, `runFilter` (full file printed)
- `AdvancedStatistics.java` — class declaration, `runFilter` override, `install` /
  `uninstall`, `calculateDueAsMetaInfo` setting `setStatsCalculated(true)`
- `Stats.java` — `calculateDue(Context,AxisType)` and its fallback
- `label_100.md`, `label_100.py` — the hand edge under judgement
- `label_104.md` — cited only for the preference-toggle `uninstall` route
  (its `Preferences.java` lines were NOT printed in this session, so that route
  is cited, not SOURCE, below)

Spaced GitHub connector fetches (one file at a time, pauses between fetches,
branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`, no 429 hit):

1. `final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/anki/stats/ChartBuilder.java`
2. `.../com/ichi2/anki/Statistics.java`
3. `.../com/ichi2/anki/stats/AnkiStatsTaskHandler.java`
4. `ChartBuilder.java` again, saved to parse exact line numbers

Line numbers below for the three app files are the local-file numbers, which
match the task brief except for one off-by-one noted in step 4. Upstream line
numbers are from the fetched repo copies on `work-2026-10-31` and match
`label_100.md` for the FORECAST path (see §Upstream).

## The route as judged (downstream core)

```
Statistics.ChartFragment (FORECAST tab)
  -> AnkiStatsTaskHandler.createChart(FORECAST)
  -> CreateChartTask.doInBackground -> ChartBuilder.renderChart
  -> ChartBuilder.calcStats case FORECAST -> Stats.calculateDue(Context,AxisType)
  -> Hooks.runFilter("advancedStatistics", ...)   [registry dispatch, NOT a direct call]
  -> AdvancedStatistics.runFilter  [ONLY if registered; see gate MG943]
  -> Stats uses the returned StatsMetaInfo (isStatsCalculated == true)
  else -> Stats.calculateDue(AxisType)  [fallback at Stats.java:331]
```

## Per-step verdicts

### 1. Hooks constructor installs AdvancedStatistics only on the preference — CORRECT (SOURCE)

- `Hooks.java:61-62` (line 60 is blank; the task brief's "60-62" covers the
  same two lines):
  `if (prefs.getBoolean("advanced_statistics_enabled", false)) {`
  `    AdvancedStatistics.install(this); }`
- The default is `false`, so on a fresh/default configuration the hook is NOT
  installed at construction.
- `Hooks.java:38-42`: `getInstance` constructs the singleton only once
  (`if (sInstance == null) { sInstance = new Hooks(context); }`). So the
  preference is read at first `Hooks` construction, not on every `runFilter`
  call. `Stats.java:311` calls `Hooks.getInstance(context).runFilter(...)`,
  which is what triggers that first construction on the forecast path.

### 2. AdvancedStatistics registers itself under key `advancedStatistics` — CORRECT (SOURCE)

- `AdvancedStatistics.java:147-149`:
  `public static void install(Hooks h) { h.addHook("advancedStatistics", new AdvancedStatistics()); }`
- `AdvancedStatistics.java:99`: `public class AdvancedStatistics extends Hook`.
- `Hooks.java:73-87` (`addHook`): appends the `Hook` to the list for the key,
  skipping duplicates by `equals`.
- Caveat (INFERRED scope limit): within the files printed here, only
  `AdvancedStatistics.install` registers the key `advancedStatistics`. An
  exhaustive grep of the whole app source root for
  `addHook("advancedStatistics")` was NOT done in this session, so "only
  registrant" is not claimed as SOURCE (see Open items).

### 3. Stats.calculateDue calls the hook through Hooks.runFilter — CORRECT (SOURCE)

- `Stats.java:308-311`:
  `public boolean calculateDue(Context context, AxisType type) {`
  `    StatsMetaInfo metaInfo = new StatsMetaInfo();`
  `    metaInfo = (StatsMetaInfo) Hooks.getInstance(context).runFilter("advancedStatistics", metaInfo, type, context, _limit());`
- Note: `Hooks.runFilter` is declared `static` (`Hooks.java:138`) but is
  invoked here through the instance returned by `getInstance`. That does not
  change the dispatch: it is still the static registry loop, not a virtual
  call on an `AdvancedStatistics` object.
- Argument order matches the override exactly (SOURCE, both sides printed):
  `runFilter`'s varargs are `(type, context, _limit())`, and
  `AdvancedStatistics.runFilter` reads `args[0]` as `AxisType`, `args[1]` as
  `Context`, `args[2]` as `String` (step 5).

### 4. Hooks.runFilter dispatches through the interface, never directly — CORRECT as a mechanism; WRONG if written as a direct edge

- `Hooks.java:138-158` (`runFilter`): if `hooks == null` it logs, reports,
  and returns `arg` unchanged (139-143); otherwise it looks up
  `hooks.get(hook)` (144) and, only if non-null, loops (146-151):
  `arg = func.runFilter(arg, args);` at **line 150**.
- The receiver at line 150 is typed `Hook` (the loop variable), so the call
  is to the interface method `Hook.runFilter`. There is NO mention of
  `AdvancedStatistics` anywhere in `Hooks.java` except the constructor's
  `install` call (line 62). A direct explicit/auto CALL edge
  `Hooks.runFilter -> AdvancedStatistics.runFilter` would therefore be
  **WRONG as written**: the target is selected only by registry key at
  run time, and the correct representation is the `non_standard` registry
  edge via `Stats.calculateDue` (step 6), not a direct edge out of
  `Hooks.runFilter`.
- Presence in the built graph: **UNCLEAR, not claimed either way** (see
  §Parts-files check). The verdict "wrong" attaches to the edge *if it
  exists*; it is not a claim that it does exist.

### 5. AdvancedStatistics.runFilter override runs the forecast simulation — CORRECT (SOURCE)

- `AdvancedStatistics.java:140-146` (the task brief's "141-146" counts from
  the method line; line 140 is the `@Override` annotation):
  `@Override public Object runFilter(Object arg, Object... args) {`
  `    Context context = (Context) args[1];`
  `    Settings = new Settings(context);`
  `    return calculateDueAsMetaInfo((StatsMetaInfo) arg, (Stats.AxisType) args[0], context, (String) args[2]); }`
- `AdvancedStatistics.java:175` (in `calculateDueAsMetaInfo`):
  `metaInfo.setStatsCalculated(true);` — this is what makes the `Stats`
  caller take the hook branch instead of the fallback.
- `Hook.java` itself was NOT printed locally in this session, so the base
  `Hook.runFilter` body/signature is not judged here; only the
  `@Override` + `extends Hook` facts above are SOURCE.

### 6. The hand edge in label_100.py — CORRECT in class/via/evidence; FIXED on the gate (proposal below, not merged)

- `label_100.py:12-17` as printed locally:
  `e('Stats.calculateDue(Context,AxisType)', 'AdvancedStatistics.runFilter', 'CALL', ...)`
  `cls='non_standard'`,
  `via=['hook registry dispatch (Hooks.runFilter loops over the Hook objects registered under the key advancedStatistics)']`,
  `evidence='SRC ...Stats.java:308-311; ...Hooks.java:61-62, 138-150; ...AdvancedStatistics.java:141-148'`.
- Verdict on the edge as written: the class (`non_standard`), the `via`
  (registry dispatch), and the cited evidence lines are all CORRECT against
  the lines printed here (with the step-5 off-by-one: the override span is
  140-146 including `@Override`, 141-146 for the body lines).
- What is wrong with it as written: the gate is only a `note`
  ("MISSING GATE MG943..."), not an attached STATE settings gate. The fix
  in §Proposed gate and edge fix attaches it. Until a merging agent applies
  that fix, the edge must be treated as **FIXED (pending application)**,
  not as already correct end-to-end.

### 7. Fallback when the hook does not run — CORRECT (SOURCE, with one INFERRED premise)

- `Stats.java:312` (`if (metaInfo.isStatsCalculated())`) takes the hook
  branch (313-329, copies the meta-info fields, returns
  `metaInfo.isDataAvailable()`); `Stats.java:330-332` (`else { return
  calculateDue(type); }`) is the private forecast computation.
- When `AdvancedStatistics` is not registered, `Hooks.runFilter` returns the
  input `metaInfo` unchanged (loop skipped because `hooks.get(
  "advancedStatistics")` is null, or the uninitialized early return), so the
  `else` branch runs. That is SOURCE for the `runFilter` behaviour.
- The one INFERRED premise: `StatsMetaInfo.java` was NOT printed, so the
  fresh object's initial `isStatsCalculated == false` is INFERRED from the
  fallback logic itself, not SOURCE. If a fresh `StatsMetaInfo` ever started
  `true`, the fallback analysis would break; that file should be printed by
  the merging agent (see Open items).

### 8. Exception path inside Hooks.runFilter — noted, not a route step

- `Hooks.java:152-154`: on exception, `runFilter` returns the `String`
  `"Error in filter " + hook + ":" + funcName` instead of the `StatsMetaInfo`.
  `Stats.java:311` casts the result to `StatsMetaInfo`, so on that path the
  cast would fail (Java cast semantics, INFERRED). This is an error path,
  not the normal route, and it does not change any verdict above; it is
  recorded only so a merging agent does not mistake it for a second return
  type of the normal path.

## Proposed gate and edge fix (NOT merged — for the merging agent)

### Exact proposed gate text

Attach gate **MG943** as a STATE settings gate to the hand edge
`Stats.calculateDue(Context,AxisType) -> AdvancedStatistics.runFilter`:

> **MG943 (STATE, settings): SharedPreferences preference
> `advanced_statistics_enabled` must be `true` (default `false`), so that
> `AdvancedStatistics` is registered under hook key `advancedStatistics`
> when `Hooks.runFilter` runs; otherwise `Hooks.runFilter` returns the
> input unchanged and `Stats.calculateDue` falls back to
> `calculateDue(AxisType)` at `Stats.java:331`.**

### Why this wording, and its one precision caveat

- The task's short form ("`advanced_statistics_enabled` must be true") is
  evaluated as **correct in substance but imprecise as a runtime
  condition**: the preference is read once at first `Hooks` construction
  (step 1), while the dispatch condition at run time is registry
  membership. The exact text above states both, so the gate cannot be
  misread as "the preference is re-checked on every `runFilter` call".
- Caveat (cited, not SOURCE here): `label_104.md` records
  `AdvancedStatistics.uninstall` (printed here at
  `AdvancedStatistics.java:150-152`, `remHook("advancedStatistics", ...)`)
  as reachable from `Preferences.updatePreference` when the box is
  unchecked. Those `Preferences.java` lines were NOT printed in this
  session, so the toggle-off route is not SOURCE here — but the gate text
  above is deliberately written in terms of *registration at run time*,
  so it stays correct whether removal happens via that route or any other.
  The merging agent should print the `Preferences` toggle lines before
  relying on the toggle direction.

### Exact proposed edge fix (not applied)

1. **Keep** the `label_100.py` hand edge exactly as written (source,
   target, `CALL`, `cls='non_standard'`, `via` registry dispatch,
   `evidence` lines), and **replace its `note` about MG943 with the
   attached gate MG943 above** (STATE, settings). Do not leave the gate
   as a note-only comment.
2. **Do NOT write** any direct explicit/auto CALL edge
   `Hooks.runFilter -> AdvancedStatistics.runFilter`. If such an edge is
   found in the built graph, suppress or reclassify it (see §Parts-files
   check) and keep only the `non_standard` registry edge from
   `Stats.calculateDue`.
3. Do not change the `Stats.calculateDue -> calculateDue(AxisType)`
   fallback edge: it is the complement of MG943 (gate false), not a
   second route to `AdvancedStatistics.runFilter`.

## Upstream route status — IMPROVED since the previous part, full route still UNCLEAR

The previous part (`route_check_part1.md` §3) left the whole upstream chain
as cited-only. In this session the following upstream steps were printed
via the spaced connector fetches above (all SOURCE, branch
`work-2026-10-31`):

| Step | Printed lines (repo copy) | Status |
|---|---|---|
| `Statistics` activity, `ChartFragment` for the FORECAST tab | `Statistics.java:59` (class), `:62` (`FORECAST_TAB_POSITION = 1`), `:362-378` (`newInstance`: FORECAST case creates a `ChartFragment` with the section number as an argument), `:420-425` (`onCreateView` reads `ARG_SECTION_NUMBER` into `mSectionNumber`) | SOURCE for the fragment/tab mapping |
| `ChartFragment.onCreateView -> createChart` | `Statistics.java:451` (`createChart();`, after the null-`TaskHandler` early return at 444-449) | SOURCE for the call; the fragment lifecycle call into `onCreateView` itself is framework dispatch (INFERRED, standard Android behaviour, not printed `fw_src` here) |
| `ChartFragment.createChart` FORECAST branch | `Statistics.java:483-487`: `createChart()` switches on `mSectionNumber`; `case FORECAST_TAB_POSITION:` calls `getTaskHandler().createChart(Stats.ChartType.FORECAST, mChart, mProgressBar)` | SOURCE; matches `label_100.md`'s `Statistics.java:487` exactly. Branch condition: this runs only when `mSectionNumber == FORECAST_TAB_POSITION` (tab 1) |
| `AnkiStatsTaskHandler.createChart -> CreateChartTask.execute` | `AnkiStatsTaskHandler.java:65-68` (creates the task, calls `execute(views)`) | SOURCE for the call; `execute -> doInBackground` is AsyncTask framework dispatch (INFERRED, same pattern as other async edges in this project) |
| `CreateChartTask.doInBackground -> ChartBuilder.renderChart` | `AnkiStatsTaskHandler.java:95` (`doInBackground`), `:108-110` (`new ChartBuilder(...)`, `return chartBuilder.renderChart(mStatType)`), with the `mIsRunning`/lock guard at 98-105 (a task that is not running returns null at 101-102 before reaching `renderChart`) | SOURCE; matches `label_100.md`'s `AnkiStatsTaskHandler.java:108-110` |
| `ChartBuilder.renderChart -> calcStats` | `ChartBuilder.java:112-113` (`renderChart` calls `calcStats(type)`) | SOURCE; matches `label_100.md`'s `:113` |
| `ChartBuilder.calcStats` FORECAST branch | `ChartBuilder.java:69-70` (`new Stats(...)`), `:72-73` (`case FORECAST: stats.calculateDue(mChartView.getContext(), type)`) | SOURCE; matches `label_100.md`'s `:70, 73` |

**Full-route verdict: UNCLEAR (not correct end-to-end), for exactly one
remaining reason:** the launcher step — which activity/intent starts the
`Statistics` activity and shows the FORECAST tab — was NOT printed in this
session. Every step from `Statistics.ChartFragment` onward is now SOURCE
except the two standard framework dispatches flagged INFERRED above
(fragment `onCreateView`, AsyncTask `execute -> doInBackground`), which
follow the same pattern as the project's other async/library edges and are
not the blocker. The blocker is solely the unprinted launcher entry. Do
not mark the full route correct until that entry is printed; conversely,
no upstream step that *was* printed needs re-printing.

## Parts-files check: direct Hooks.runFilter -> AdvancedStatistics.runFilter edge

- **From the parts files actually seen in this session:** `label_100.py`
  (local) contains exactly one runFilter-related hand edge, and it is
  `Stats.calculateDue(Context,AxisType) -> AdvancedStatistics.runFilter`
  (`non_standard`, registry dispatch). It contains NO edge with source
  `Hooks.runFilter`. `label_104.md` (local) lists runHook-registry edges
  only (`Hooks.runHook -> Leech$LeechHook.runHook`); `label_104.py` was
  NOT available locally, so nothing is claimed about it.
- **NOT claimed:** presence or absence of a direct explicit/auto CALL
  edge `Hooks.runFilter -> AdvancedStatistics.runFilter` in
  `graphs/AnkiDroid/graph_def.py` (1.17 MB) or `auto_calls.json`
  (2.54 MB). Both exceed connector display and were not fetched in this
  session (deliberately, to avoid burst fetches alongside parallel agents).
  The earlier "suspect automatic CALL, not suppressed" note in
  `AGENT_NOTES.md` therefore remains **unconfirmed either way**: if the
  merging agent, on a full checkout, greps those files and finds such an
  edge, apply fix step 2 above; if none is found, record the AGENT_NOTES
  note as stale. Neither outcome may be asserted from the parts files
  seen here.

## Open items (for the merging agent, on a full checkout)

1. Print the launcher entry into the `Statistics` activity (intent caller
   and FORECAST-tab selection) — the sole remaining blocker for a
   correct full route.
2. Grep `graph_def.py` / `auto_calls.json` for
   `Hooks.runFilter -> AdvancedStatistics.runFilter`; suppress/reclassify
   if present, or record the AGENT_NOTES "suspect" note as stale if absent.
3. Apply the MG943 gate attachment in §Proposed gate and edge fix (this
   report does not edit any repo file).
4. Print `StatsMetaInfo.java` (fresh-object default of
   `isStatsCalculated`) and `Hook.java` (base `runFilter`) to convert the
   two INFERRED premises in steps 5 and 7 to SOURCE.
5. Grep the app source root for `addHook("advancedStatistics")` to confirm
   or refute "only registrant", and print the `Preferences.java`
   toggle lines behind `AdvancedStatistics.uninstall` (cited in
   `label_104.md`, not printed here) to settle the toggle-off direction
   of the gate.
6. Run the C1 checks (build, sampler, grep, route checks) on a full
   checkout before anything here is treated as verified or pushable.
   Nothing in this report is a merge or push instruction.

## Verdict summary

- Hooks constructor gate (pref, default false, read once): **correct**
- `AdvancedStatistics.install` registration under `advancedStatistics`: **correct**
- `Stats.calculateDue -> Hooks.runFilter("advancedStatistics", ...)` call + argument order: **correct**
- `Hooks.runFilter` line-150 interface dispatch: **correct** as a mechanism;
  a direct `Hooks.runFilter -> AdvancedStatistics.runFilter` edge: **wrong** (presence in built graph: **unclear**)
- `AdvancedStatistics.runFilter` override + `setStatsCalculated(true)`: **correct**
- Hand edge `Stats.calculateDue -> AdvancedStatistics.runFilter` (`non_standard`, registry dispatch): **correct** in class/via/evidence, **fixed** on the gate (MG943 attached as STATE settings gate in the proposal above, not yet applied)
- Fallback `Stats.calculateDue(AxisType)` at `:331`: **correct** (fresh-`StatsMetaInfo` premise INFERRED)
- Upstream `Statistics.ChartFragment -> ... -> ChartBuilder.calcStats -> Stats.calculateDue`: **correct** for every printed step (SOURCE, line numbers above); framework dispatches INFERRED
- Full route from the launcher: **unclear** (launcher entry not printed)
- Direct edge in parts files seen: none shown; in `graph_def.py` / `auto_calls.json`: **not checked, no claim**
