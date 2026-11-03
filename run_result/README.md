# run_result: the final results

A frozen copy of every final result, taken on 2026-11-03 from commit `5099f10d` (official CI request `c2e359a1`, emulator run `41593209101-1`).

The live files stay where the tools use them (`graphs/`, `device/`). This folder only collects them in one place, so nothing here needs to be rebuilt. For what was done and how, see the [main README](../README.md).

## Layout

```
run_result/
  SUMMARY.csv                 one row per app: every number in the main README
  apps/<App>/
    graph/                    the trigger graph and its outputs
      <prefix>_trigger_graph.json   pages, methods, verdicts, labels, edges with evidence, verified routes
      <prefix>_trigger_graph.html   viewer for the same graph (open it in a browser)
      methods.csv             one row per method: verdict, gates, best route, path status
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
| Aegis | 2,995 | 6,430 | 2,537 | 458 | 1 of 472 (0.002) | 0 of 26 (0.000) | 1 of 14 (0.071) | 1 of 25 | 1 |
| AmazeFileManager | 2,981 | 7,747 | 2,512 | 469 | 25 of 499 (0.050) | 10 of 14 (0.714) | 25 of 30 (0.833) | 0 of 30 | 0 |
| AnkiDroid | 4,186 | 9,815 | 3,275 | 911 | 3 of 941 (0.003) | 0 of 232 (0.000) | 3 of 30 (0.100) | 0 of 30 | 0 |
| MMEX | 4,270 | 8,441 | 3,430 | 840 | 8 of 868 (0.009) | none checked | 8 of 28 (0.286) | 6 of 30 | 6 |
| LibreTorrent | 4,732 | 7,303 | 3,967 | 765 | 9 of 792 (0.011) | 25 of 78 (0.321) | 9 of 27 (0.333) | 7 of 29 | 7 |
| **Total** | 29,024 | 63,008 | 24,304 | 4,720 | 133 of 5,103 (0.026) | 155 of 735 (0.211) | 134 of 365 (0.367) | 104 of 389 | 100 |

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
