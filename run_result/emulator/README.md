# The emulator job: results

Every route in the ground truth was replayed on an Android 8.1 (API 27) emulator in GitHub Actions. The aim was to see whether the route's target method really runs.

**Result of the run of record `41593209101-1` (2026-11-03):**
- **Reached:** 104 of 389 routes (26.7%).
- **Confirmed:** 100 of the reached routes also ran the whole script; they are `DEVICE_OK` in the graphs.
- **Unclear:** the other 285 routes. That covers not reached, script stopped, or unscriptable. They are never wrong.

**Which run each number comes from.**
- Each app's run total comes from its own run of record: the run its `device/results.csv` was written from. For the eight apps outside the re-audit that is `41593209101-1`. For Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX it is `42560435293-1`, the last real run with results for all five apps.
- Two later real attempts covered only Aegis, LibreTorrent and MMEX. `42674277844-1` was lost to a GitHub incident and reached no device. `42683233983-1` re-ran 9 routes whose best route had changed. Its 5 LibreTorrent rows replace the older rows in the audit log; its raw results are kept in `earlier_runs/`.
- The audit logs (`verification.csv`) hold a second number, the DEVICE rows that confirm the current best route. A reached row that replays an older route is dropped there, so Aegis has 1 fewer reached route than its run total and MMEX has 3 fewer (`SUMMARY.csv` columns `device_rows_reached` and `device_reached`).

## How the job works

| Part | Setting |
|---|---|
| Workflow | `device-replay.yml` (copy in this folder; live in `.github/workflows/`), one job per app, all 13 in parallel, then a `collect` job that commits the text results |
| Emulator | Android 8.1, API 27, **Google APIs x86** image (Google publishes no API 27 Google APIs x86_64 image), `pixel_2` profile, 3 cores, 3 GB RAM, animations off |
| App | each app's instrumented debug build (JaCoCo), from the baseline tool runs in `bugfixops/work-emulator`; installed fresh for each app |
| Route | a Python script per route (`device/routes/<App>/route_NN.py`) taps and types through `adb` and UI dumps, following the route drawn in the graph; at most 10 minutes per route |
| Reached? | after each route, coverage is dumped and the JaCoCo report is searched for the route's target method; covered = **reached** |
| Into the graphs | `device/compare.py` writes `graphs/<App>/device/results.csv`; each app's `make_verification.py` adds one `DEVICE` row per route to `verification.csv`: reached gives `correct`, anything else gives `unclear` |

The tools then treat the `DEVICE` rows as follows:
- they are counted on their own line, never in the route error rate;
- they never lower a route's status, and never override WRONG;
- a reached route whose script finished becomes `DEVICE_OK`.

## Results per app

| App | Routes | Scripted | Unscriptable | Reached | Reached and script finished (DEVICE_OK) | Unclear |
|---|---:|---:|---:|---:|---:|---:|
| Currency | 28 | 28 | 0 | 18 | 17 | 10 |
| Diary | 30 | 30 | 0 | 16 | 16 | 14 |
| hash-checker | 37 | 36 | 1 | 23 | 23 | 14 |
| Omni-Notes | 33 | 31 | 2 | 8 | 8 | 25 |
| openlauncher | 27 | 26 | 1 | 5 | 5 | 22 |
| Vanilla-Music | 30 | 30 | 0 | 8 | 5 | 22 |
| Markor | 30 | 30 | 0 | 7 | 7 | 23 |
| AnyMemo | 30 | 27 | 3 | 5 | 5 | 25 |
| Aegis | 25 | 22 | 3 | 1 | 1 | 24 |
| AmazeFileManager | 30 | 26 | 4 | 0 | 0 | 30 |
| AnkiDroid | 30 | 26 | 4 | 0 | 0 | 30 |
| MMEX | 30 | 26 | 4 | 6 | 6 | 24 |
| LibreTorrent | 29 | 17 | 12 | 7 | 7 | 22 |
| **Total** | 389 | 355 | 34 | 104 | 100 | 285 |

Every route that was not reached is listed in [`DEVICE_RUN_SUMMARY.md`](DEVICE_RUN_SUMMARY.md), with its script status and the last lines of its step log.

The main reasons are first-start states the scripts did not expect:
- AnkiDroid opens on its settings screen instead of the deck list;
- AmazeFileManager crashes on start;
- Markor shows its intro and then a storage request;
- Omni-Notes starts with an empty notes list;
- openlauncher stays in its own launcher setup.

These are candidates for more setup, not errors in the graphs.

## All runs

The first 7 runs were attempts that found and fixed problems in the job itself. The full log of fixes is in [`KIRO_REPORT_EMULATOR.md`](KIRO_REPORT_EMULATOR.md).

| Run | Apps with results | Routes | Reached | What happened |
|---|---:|---:|---:|---|
| [`41578755210-1`](earlier_runs/41578755210-1/) | 0 | 0 | 0 | started by hand; every job failed at emulator setup: no Google APIs x86_64 image exists for API 27, so the image was switched to x86 |
| [`41580035601-1`](earlier_runs/41580035601-1/) | 13 | 12 | 0 | only 1 route per app ran (route list read wrongly in run_app.sh); fixed |
| [`41580858995-1`](earlier_runs/41580858995-1/) | 13 | 359 | 40 | screen dumps could not be parsed (a status line after the XML); fixed |
| [`41581852815-1`](earlier_runs/41581852815-1/) | 13 | 389 | 70 | first complete run; taps came before cold-started screens were drawn; harness now waits |
| [`41583852305-1`](earlier_runs/41583852305-1/) | 12 | 359 | 62 | Markor job lost to a download error; AnyMemo and Amaze launch names fixed |
| [`41586297765-1`](earlier_runs/41586297765-1/) | 13 | 389 | 76 | all-caps button text and the Diary start-up permission dialog; fixed |
| [`41589762145-1`](earlier_runs/41589762145-1/) | 13 | 389 | 102 | shared sample files were not pushed to the device; Vanilla needed storage permission; fixed |
| [`41593209101-1`](run_41593209101-1/) | 13 | 389 | 104 | **run of record** (all results below) |
| [`42168580707-1`](earlier_runs/42168580707-1/) | 5 | 144 | 14 |  |
| [`42560435293-1`](earlier_runs/42560435293-1/) | 5 | 144 | 14 |  |
| [`42674277844-1`](earlier_runs/42674277844-1/) | 0 | 0 | 0 |  |
| [`42683233983-1`](earlier_runs/42683233983-1/) | 3 | 84 | 10 |  |

## Dry runs

A dry run starts no emulator. It loads every route script, prints its planned actions, and checks its edge ids against the current graph.

| Dry run | Apps | Scripts PASS | Scripts FAIL | Note |
|---|---:|---:|---:|---|
| [`41483333085-1`](dry_runs/41483333085-1/) | 9 | 275 | 0 | dry run during the preparation of the route scripts |
| [`41520252284-1`](dry_runs/41520252284-1/) | 0 | – | – | no results collected (early test of the collect step) |
| [`41527411246-1`](dry_runs/41527411246-1/) | 0 | – | – | no results collected (early test of the collect step) |
| [`41535141998-1`](dry_runs/41535141998-1/) | 1 | 30 | 0 | dry run during the preparation of the route scripts |
| [`41557528925-1`](dry_runs/41557528925-1/) | 2 | 55 | 0 | dry run during the preparation of the route scripts |
| [`41575076492-1`](dry_runs/41575076492-1/) | 1 | 29 | 0 | dry run during the preparation of the route scripts |
| [`41576644702-1`](dry_runs/41576644702-1/) | 13 | 389 | 0 | final dry run of all apps before the real run |
| [`41578222764-1`](dry_runs/41578222764-1/) | 13 | 389 | 0 | after the workflow edit (Google APIs image, SSH server for Amaze) |
| [`41579127015-1`](dry_runs/41579127015-1/) | 13 | 389 | 0 | after the switch to the x86 image and the real-run request file |
| [`41579432533-1`](dry_runs/41579432533-1/) | 13 | 389 | 0 | a real-run request that ran as a dry run (fixed in the plan job) |
| [`42167260197-1`](dry_runs/42167260197-1/) | 5 | 97 | 47 | dry run during the preparation of the route scripts |
| [`42168202056-1`](dry_runs/42168202056-1/) | 5 | 144 | 0 | dry run during the preparation of the route scripts |
| [`42559057193-1`](dry_runs/42559057193-1/) | 5 | 144 | 0 | dry run during the preparation of the route scripts |
| [`42667889918-1`](dry_runs/42667889918-1/) | 3 | 54 | 30 | dry run during the preparation of the route scripts |

## What is in a run folder

| File | Content |
|---|---|
| `SUMMARY.md` | per app: routes, reached, not reached, script failed, unscriptable |
| `<App>/results.csv` | one row per route: `route`, `method`, `edges`, `reached` (yes / no / not_run), `script_status` (ok / failed_at_step_N / timeout / unscriptable), steps done, error, run id |
| `<App>/run.log` | the runner's log for the app |
| `<App>/steps/<route>.log` | every step of the route: edge id, action, target, ok or failed |

Screenshots and UI dumps were kept only as 30-day GitHub artifacts and are not in the repository.

## Limits

- **One run.** Repeats vary by a route or two per app; for example, hash-checker reached 25 routes in the run before and 23 in this one.
- **Reached is not the same as walked.** "Reached" says the method ran, not that every step of the drawn route happened. That is why `DEVICE_OK` also needs the whole script to finish. 4 routes reached the method although their script stopped early; they keep their earlier status.
- **A miss proves nothing either way.** A route that was not reached is not evidence that the route is wrong.
