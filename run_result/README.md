# run_result: the final results

A frozen copy of every final result, taken on 2026-11-09 from commit `1050889e` (official CI request `5fe80ea6`, emulator run `41593209101-1`).

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
    device/results.csv        the emulator result per route of run 41593209101-1
    ci/                       output of the eight checks from the official CI (SUMMARY.txt first)
  emulator/                   the emulator job: run of record, earlier attempts, dry runs, summary (see its README)
```

## Per app

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
| Aegis | 2,995 | 6,362 | 2,522 | 473 | 13 of 552 (0.024) | 0 of 26 (0.000) | 8 of 20 (0.400) | 1 of 25 | 1 |
| AmazeFileManager | 2,981 | 7,318 | 2,450 | 531 | 31 of 618 (0.050) | 10 of 16 (0.625) | 26 of 30 (0.867) | 0 of 30 | 0 |
| AnkiDroid | 4,186 | 9,721 | 3,221 | 965 | 16 of 1,052 (0.015) | 0 of 232 (0.000) | 5 of 30 (0.167) | 0 of 30 | 0 |
| MMEX | 4,270 | 8,410 | 3,426 | 844 | 11 of 932 (0.012) | none checked | 8 of 28 (0.286) | 6 of 30 | 6 |
| LibreTorrent | 4,732 | 7,299 | 3,963 | 769 | 15 of 857 (0.018) | 25 of 78 (0.321) | 9 of 29 (0.310) | 7 of 29 | 7 |
| **Total** | 29,024 | 62,382 | 24,165 | 4,859 | 173 of 5,542 (0.031) | 155 of 737 (0.210) | 144 of 373 (0.386) | 104 of 389 | 100 |

**Known problems.** In Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX, the state, env and GUI split of reachable methods still has known errors (a review on 3 November 2026 found 59% agreement with an independent hand-labelled sample of 50 unreached methods per app). Round 1 of a re-audit changed the setup state, entry points, impossible calls, library creation and outside data; later rounds judged every flagged guard step on the routes; a reachable audit of 300 methods found 29 wrong classes (9.7%), all corrected; a blind second pass by the same worker found 12 more, and a decided rule question (AnkiDroid's unused client API is dead) fixed 2 rows. The audit now counts 257 correct, 41 fixed, 0 wrong, 2 unclear (13.8% wrong before the fixes). It has been checked by one person only so far. Emulator: three real attempts. Run 42560435293-1 reached 14 of 144 sampled routes. Run 42674277844-1 was lost to a GitHub incident and reached no device. Run 42683233983-1 re-ran 9 routes whose best route had changed; 5 LibreTorrent routes were reached on their current routes. Device confirmation of 4 methods was dropped because the graph's best route changed after the old run; the re-scripted routes failed on the device and no run budget was left (Aegis Salsa20Engine.salsaCore; MMEX DefinedDateRange$1.<init>, NumericHelper.getNumberOfDecimals, AppSettings.getPreferences). Their label rates mostly measure the dead verdicts. See "Known problems" in the [main README](../README.md).

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
