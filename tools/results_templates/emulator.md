# The emulator job: results

Every route in the ground truth was replayed on an Android 8.1 (API 27) emulator in GitHub Actions. The aim was to see whether the route's target method really runs.

**Result of the run of record `{{RUN}}` (2026-11-03):**
- **Reached:** {{REACHED}} of {{ROUTES}} routes ({{PCT}}%).
- **Confirmed:** {{DOK}} of the reached routes also ran the whole script; they are `DEVICE_OK` in the graphs.
- **Unclear:** the other {{DUNCL}} routes. That covers not reached, script stopped, or unscriptable. They are never wrong.

**Which run each number comes from.**
- Each app's run total comes from its own run of record: the run its `device/results.csv` was written from. For the eight apps outside the re-audit that is `{{RUN}}`. For Aegis, AmazeFileManager, AnkiDroid, LibreTorrent and MMEX it is `42560435293-1`, the last real run with results for all five apps.
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

{{TABLE_DEVICE}}

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

{{TABLE_RUNS}}

## Dry runs

A dry run starts no emulator. It loads every route script, prints its planned actions, and checks its edge ids against the current graph.

{{TABLE_DRY}}

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
- **Reached is not the same as walked.** "Reached" says the method ran, not that every step of the drawn route happened. That is why `DEVICE_OK` also needs the whole script to finish. {{PARTIAL}} routes reached the method although their script stopped early; they keep their earlier status.
- **A miss proves nothing either way.** A route that was not reached is not evidence that the route is wrong.
