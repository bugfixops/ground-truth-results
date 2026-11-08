# Final summary: trigger graphs for the 13 Java-only apps (overnight run, 2026-10-24/25)

> **UPDATE 2026-10-25 (evening): superseded by Yang's audit.** The eight generated graphs are not ground truth (Yang found 48 of 90 edges and 10 of 25 paths correct, `FRAMEWORK_ONLY` never used, `DEAD` only meaning "no route found"),
> and "0 contradictions with the baseline" was reached by tuning the generator on those contradictions, so it is not independent evidence. They are to be rebuilt by hand; the five hand-written graphs get the new labels (UNREACHABLE / REACHABLE,
> ENV / STATE fields, edge kinds) and path verification. Generator output stays only as a cross-check. See memory `ground-truth-requirements`.

**Status: all 13 apps have `graphs/<App>/out/` with the graph JSON, `methods.csv`, `README.md` and the optional HTML viewer.** Index and rebuild commands: `graphs/SUMMARY.md`. Five graphs were written by hand earlier (Currency, Diary by Kiro, hash-checker, openlauncher, Omni-Notes); the other eight (Vanilla-Music, AnyMemo, Markor, Aegis, AmazeFileManager, AnkiDroid, MMEX, LibreTorrent) were produced overnight by a **generator** (`tools/gen_edges.py`) plus a short per-app review, because hand-writing took about 2.5 hours and 450k tokens per app and the eight apps hold 25.5k methods.

## Numbers (recomputed by `tools/summary_table.py`)

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

## What the generated graphs are, and are not

- Built from the bytecode call graph, `AndroidManifest.xml` and `res/` XML: entry points, lifecycle, callbacks of constructed classes, lambdas, intents, XML-instantiated classes, activity / permission results, `Handler` messages, and glue for ButterKnife, EventBus, data binding, Dagger / Hilt, Glide, Room, Icepick, Parceler, ORMLite, reflection by method name. Methods that nothing reaches are `DEAD` (automatic, `AUTO_DEAD`).
- **Validation.** 0 errors, 0 warnings and **0 contradictions with the baseline coverage** (no DEAD method ran in the 1-hour APE / Monkey runs) in all 8; every contradiction found during development was a missing generator rule and was fixed. Run on the five hand-written apps the generator agrees on 97.2% (Currency), 96.5% (Diary), 98.5% (hash-checker), 92.9% (openlauncher), 93.8% (Omni-Notes) of the methods for dead-versus-alive, and on 93.8% (Currency), 95.5% (Diary), 71.1% (hash-checker), 76.9% (openlauncher), 63.1% (Omni-Notes) of the exact verdicts. The five hand-written graphs were rebuilt with the changed tools and came out identical.
- **Limit that matters most:** `REACHABLE` in a generated graph means "no modelled setup". State gates beyond list rows (data that must exist, settings, files) are only modelled where `review_notes.md` / `graph_def.py` of the app lists them, so the split REACHABLE / REACHABLE_AFTER_SETUP is less reliable than in the hand-written graphs. Callbacks are reachable once an instance is constructed; Handler messages, EventBus subscribers and Dagger objects are linked from every send / post / graph-build site (INFERRED).
- **New in the generated CSVs:** the `frontier_*` columns say, for each never-run reachable method, where the chain from code that did run first enters code that never ran (a branch not taken, or an event nobody triggered). Each README lists the ten frontier nodes that unlock the most never-run methods.

## Findings about the baseline (from the hit counts)

- **MMEX: only 271 of 4267 observable methods ran.** The hits stop at the tutorial, `SelectDatabaseActivity`, the password screen and the settings; no method of the packages `account`, `transactions`, `investment`, `reports`, `recurring`, `search`, `fragment`, `adapter` ran and `HomeFragment` was never created. `MainActivity.onCreate` ran but returns early when `showPrerequisite()` is true (the tutorial is still needed, or no valid database is selected: it starts `TutorialActivity` / `SelectDatabaseActivity` and calls `finish()`), so `initHomeFragment` never ran and 1650 never-run methods sit behind it. The MMEX graph gates those packages behind that prerequisite (read from `MainActivity.java`, stated in its README).
- **Aegis: 751 of 2955.** The baseline got past the first-run setup and showed the vault list, but the vault stayed empty (`EntryAdapter.onBindViewHolder` never ran), and it never opened `EditEntryActivity` (add / edit an entry), the importers of the other authenticator apps, the backup preferences, or the unlock screen (`AuthActivity`).
- **LibreTorrent:** no method of the torrent detail screens ran (apparently no torrent was added; the fixtures have no `.torrent`).
- **Fixtures:** Vanilla-Music had 12 mp3 + 3 wav (so no fixture for the Opus / Ogg / FLAC / MP4 tag parsers); the Download folder has 19 files (`archive.zip`, `table.csv`, `todo.txt`, `tasks.org`, `notes.md`, `journal.md`, `sample_deck.apkg`, `sample.pdf`, `page.html`, `config.xml`, `data.json`, `events.ics`, `contacts.vcf`, six images), so csv, todo.txt and AnkiDroid-import files existed, but there is no fixture for 7z / gz / bz2 archives, apk or db files, Mnemosyne / SuperMemo files, `.jenc` notes or torrents; Markor's `Documents` fixture folder is missing.
- From earlier in the session: `merged.ec` omits the launch dump `00000.ec` (first-launch code can show `monkey_hit = 0` although it ran); one dump per run is unreadable; APE seems to wipe app data mid-run in Aegis, Markor and hash-checker; Yang's `share/methods.csv` drops the final tap in 4 rows whose path ends in `*.onOptionsItemSelected`.

## Open questions for Yang (unchanged, still unanswered)

1. Is device verification (emulator) required for each app, and for which edges?
2. Baseline tool: the draft says Monkey, `tool_run_set_38.csv` says APE.
3. The missing `fixtures/Documents` folder (Markor).
4. How were Aegis and MMEX set up on the baseline (coverage 25% and 6%)?
5. The draft counts 41 apps; here there are 13 Java-only apps.
6. Are generated graphs with class-level review acceptable as ground truth, or should selected apps be hand-curated further (the biggest gains: Aegis, MMEX, AnkiDroid, LibreTorrent state gates)?

## If more time is spent

- Hand-curate the `needs_state` gates of the biggest never-run clusters (each README lists them; `review_notes.md` says what is assumed) and re-run `tools/check_gen.sh`.
- Rebuild Diary with the current tools (Kiro's graph used older ones; its inputs `method_list.json` / `auto_calls.json` are not in `graphs/Diary/`).
- Verify the `FW-MEMORY` rules and the frontier edges on an emulator.
