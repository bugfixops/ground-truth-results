# Trigger graphs of the 13 Java-only apps

Each folder `graphs/<App>/out/` holds the same set of files as `share/` has for Currency: `<prefix>_trigger_graph.json` (pages, methods, verdicts, edges with evidence labels), `methods.csv` (one row per method: verdict, steps from launch, taps on the best path, path, baseline hits), `README.md` (numbers, how much to trust it, limits), `<prefix>_trigger_graph.html` (optional viewer) and `build_report.txt` (validation output). **The JSON and the CSV are the data.**

## Two ways of building

- **Hand-written** (Currency, Diary, hash-checker, openlauncher, Omni-Notes): the edge definitions were written by reading the source; state gates (`needs_state`) and environment gates (`env`) come from a human reading the code. Diary was made by Kiro with older tools.
- **Generated** (Vanilla-Music, AnyMemo, Markor, Aegis, AmazeFileManager, AnkiDroid, MMEX, LibreTorrent): `tools/gen_edges.py` derives entry points, lifecycle, callbacks, lambdas, intents, XML-instantiated classes and library glue (ButterKnife, EventBus, data binding, Dagger, Glide, Room, ...) from the bytecode, the manifest and `res/` XML; the per-app `graph_def.py` only adds a few gates; `review_notes.md` records what was reviewed by hand. Run on the five hand-written apps (`tools/calibrate.py`), the generator agrees with the hand-written graphs on **97.2% (Currency), 96.5% (Diary), 98.5% (hash-checker), 92.9% (openlauncher), 93.8% (Omni-Notes) of the methods for dead-versus-alive** and on 93.8% (Currency), 95.5% (Diary), 71.1% (hash-checker), 76.9% (openlauncher), 63.1% (Omni-Notes) of the exact verdicts; the gap is `needs_state` (a human reads "needs a note / a folder / a setting" out of the code). So in the generated graphs `REACHABLE` means "no modelled setup", not "no setup".
- The generated graphs add five columns to `methods.csv` (`frontier_from`, `frontier_first_unrun`, `frontier_edge_kind`, `frontier_edge_evidence`, `steps_after_frontier`): for a method the baseline never ran, the edge where the chain from code that did run first enters code that never ran, i.e. the branch or event that blocked the baseline. Each generated README lists the ten frontier nodes that unlock the most never-run methods.

## Numbers (recomputed from the files by `tools/summary_table.py`)

| App | method | methods | pages | edges | reachable | after setup | dead | framework-only | baseline-run | never run: dead / env / setup / clean | contradictions |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Currency | hand | 145 | 22 | 391 | 140 | 0 | 2 | 3 | 103 | 5 / 22 / 0 / 13 | 0 |
| Diary | hand (Kiro) | 286 | 34 | 1435 | 263 | 2 | 17 | 4 | 187 | 20 / 7 / 1 / 70 | 0 |
| hash-checker | hand | 529 | 39 | 1234 | 419 | 90 | 14 | 6 | 404 | 16 / 34 / 43 / 26 | 0 |
| openlauncher | hand | 900 | 43 | 1606 | 592 | 135 | 162 | 11 | 520 | 172 / 68 / 64 / 75 | 0 |
| Omni-Notes | hand | 1456 | 68 | 3780 | 731 | 474 | 205 | 46 | 848 | 223 / 110 / 222 / 23 | 0 |
| Vanilla-Music | generated | 1473 | 46 | 3355 | 1213 | 187 | 73 | 0 | 1101 | 67 / 45 / 78 / 175 | 0 |
| AnyMemo | generated | 2207 | 71 | 5244 | 1747 | 306 | 154 | 0 | 1271 | 141 / 155 / 96 / 527 | 0 |
| Markor | generated | 2859 | 38 | 8081 | 2245 | 310 | 304 | 0 | 1611 | 303 / 107 / 257 / 575 | 0 |
| Aegis | generated | 2995 | 48 | 6233 | 2043 | 760 | 192 | 0 | 751 | 155 / 116 / 731 / 1202 | 0 |
| AmazeFileManager | generated | 2981 | 37 | 7745 | 2062 | 700 | 219 | 0 | 1132 | 216 / 338 / 484 / 808 | 0 |
| AnkiDroid | generated | 4186 | 78 | 11395 | 3376 | 280 | 530 | 0 | 2011 | 521 / 338 / 239 / 1065 | 0 |
| MMEX | generated | 4270 | 104 | 10886 | 663 | 3067 | 540 | 0 | 271 | 538 / 388 / 2892 / 178 | 0 |
| LibreTorrent | generated | 4732 | 73 | 12622 | 3108 | 1215 | 409 | 0 | 2080 | 403 / 240 / 1147 / 856 | 0 |

Total: 29019 methods, 74007 edges in 13 graphs.

"never run: dead / env / setup / clean" splits the methods that neither APE nor Monkey ran: dead or framework-only, reachable only through an outside environment, reachable after in-app setup, reachable with no modelled setup (the clearest target list for the paper). "baseline-run" counts the methods that ran in at least one of the two 1-hour API 27 runs. "contradictions" are dead or framework-only methods that ran anyway (must be 0).

## Rebuild

`python3 -I tools/build_graph.py graphs/<App> <prefix>` (from `work/`), then for generated apps `python3 -I tools/gen_readme.py <App> <prefix>` and `python3 -I tools/write_summaries.py`. `tools/check_gen.sh` re-runs the generator on the two hand-written apps and prints the agreement. The recipe, the tool facts and the rules learned are in `handoff/HANDOFF.md`.
