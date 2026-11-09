# run_result: the final results

A frozen copy of every final result, taken on 2026-11-05 from commit `{{BASE}}` (official CI request `{{CI}}`, emulator run `{{RUN}}`).

The live files stay where the tools use them (`graphs/`, `device/`). This folder only collects them in one place, so nothing here needs to be rebuilt. For what was done and how, see the [main README](../README.md).

## Layout

```
run_result/
  SUMMARY.csv                 one row per app: every number in the main README
  apps/<App>/
    graph/                    the trigger graph and its outputs
      <prefix>_trigger_graph.json   pages, methods, verdicts, labels, edges with evidence, verified routes
      <prefix>_trigger_graph.html   viewer for the same graph (open it in a browser)
      methods.csv             one row per method: verdict, gates, best route, path status, full JVM class (jvm_class)
      README.md               generated summary of the app's graph, with the notes below
      build_report.txt, sanity_check.csv   build report; tool-coverage sanity check (never evidence)
    verification.csv          audit log: every label, edge and route checked, plus the emulator (DEVICE) rows
    readme_notes.md           notes on the app: what changed in the audit, how routes were chosen, what waits for a device, limits
    routes.csv                the app's route list for the emulator (scripted or unscriptable, with the reason)
    device/results.csv        the emulator result per route of run {{RUN}}
    ci/                       output of the eight checks from the official CI (SUMMARY.txt first)
  emulator/                   the emulator job: run of record, earlier attempts, dry runs, summary (see its README)
```

## Per app

{{TABLE_MAIN}}

**Known problems.** In Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX, the state, env and GUI split of reachable methods still has known errors (a review on 3 November 2026 found 59% agreement with an independent hand-labelled sample of 50 unreached methods per app). Round 1 of a re-audit changed the setup state, entry points, impossible calls, library creation and outside data; later rounds judged every flagged guard step on the routes; a reachable audit of 300 methods found 28 wrong classes (9.4%), all corrected, checked by one person only so far. Their label rates mostly measure the dead verdicts. See "Known problems" in the [main README](../README.md).

## Columns of `SUMMARY.csv`

| Column | Meaning |
|---|---|
| `methods`, `pages`, `edges`, `reachable`, `unreachable` | size of the graph and its verdicts (from `ci/SUMMARY.txt`) |
| `<type>_rows` | audit rows of that type: label, edge or path (route); emulator rows not counted |
| `<type>_checked` | rows judged `correct`, `fixed` or `wrong` |
| `<type>_fixed`, `<type>_wrong`, `<type>_unclear` | how those rows split |
| `<type>_error_rate` | (fixed + wrong) ÷ checked; each route counted once |
| `device_routes`, `device_scripted`, `device_unscriptable` | routes in the emulator job |
| `device_reached` | routes whose target method ran on the emulator |
| `device_ok` | routes reached with the whole script finished |
| `device_unclear` | all other routes |
| `path_status_*` | route status over all reachable methods (from `graph/README.md`) |
| `ci_request` | the commit the official CI built |
