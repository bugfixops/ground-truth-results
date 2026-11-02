# Device replay: what this directory is

Schema 2 ground-truth routes are replayed on an API 27 emulator in
GitHub Actions, after all labelling, route checks, and logs are done.
Nothing in this directory runs an emulator by itself, and no real
emulator run starts from here: the user starts it by hand with
`.github/workflows/device-replay.yml` (`dry_run=false`), after
choosing the emulator image. This directory holds the preparation:
route lists, replay scripts, the harness, the runner, and the
collect/compare tools. The workflow itself (`.github/`) is never
edited from this project side.

## What the workflow does

1. **Plan** (`device/plan.py <apps...>` or `all`): prints exactly one
   line `matrix={"app": [...]}` listing the requested apps that have
   at least one `device/routes/<App>/route_*.py`. No scripts for an
   app means the app is not in the matrix (exit 1 when none qualify).
2. **Run** (one job per app, `device/run_app.sh <App> <glob> <outdir>`
   with or without `--dry-run`): installs the instrumented debug APK
   from the work-emulator checkout (`$WEMU`), replays each scripted
   route, and writes `results.csv` plus per-route evidence.
3. **Collect** (`device/collect.py collected <dest>`): copies only
   small text files (`results.csv`, `run.log`, `steps/*.log`,
   `dryrun_report.txt`) into `device/<kind>/<run>/`; screenshots and
   UI dumps stay in the 30-day artifacts and are never committed.
   It also writes `SUMMARY.md` for the run.

A dry run is triggered by pushing `handoff/DEVICE_DRYRUN_REQUEST.txt`
(line 1 a comment, line 2 `# request <UTC time> <purpose>`, then app
names or `all`); only the coordinator sends that request, at most
once per 15 minutes. A dry run passes for an app only when every
scripted route shows PASS in its `dryrun_report.txt`.

## Inputs

- `device/routes/<App>/ROUTES.csv` (D1): one row per route, columns
  `route,method,edges,source,env_kinds,state_kinds,permissions,
  fixtures,setup,status`. For the eight ticked apps the rows are the
  `verification.csv` path rows in order; for the other five apps they
  are the final route-check sample. `permissions` lists dangerous
  runtime permissions only (verified declared in the manifest);
  `fixtures` is semicolon-separated, one entry per fixture, in three
  forms: a plain path under `$WEMU/fixtures` (pushed to the same
  path under `/sdcard/`); `<repo-relative> -> <dst>` for a text
  fixture committed under `device/routes/<App>/` (conventionally
  `device/routes/<App>/fixtures/`, pushed to `<dst>`); or
  `gen:<name> -> <dst>` for a file generated at run time by the
  route's per-route setup script (see below, pushed to `<dst>`).
  Text fixtures only under `device/routes/` — never binaries.
  `setup` is the work-emulator `apps.csv` setup text for the app,
  plus, for `gen:` fixtures, the generation step (naming the setup
  script and the generated file); `status` is `scripted` or
  `unscriptable: <reason>`.
- `device/routes/<App>/route_NN.py` (D3): one script per scripted
  route (see "Route scripts" below). An optional per-app
  `device/routes/<App>/setup.py` runs once per route after `pm clear`
  and before the route script; it must be idempotent (it runs before
  every route, not once per app). An optional per-route
  `device/routes/<App>/setup_<route>.py` runs after the app setup
  and before the fixture phase, when the route needs a file
  generated at run time (e.g. a zip built with python `zipfile`, or
  a system font copied from the runner); it writes generated files
  into `<outdir>/gen/<route>/` (passed as `--gen-dir`, and as
  `GEN_DIR` in the environment of the route script), and nothing it
  generates is ever committed — generated files live only under
  `<outdir>`. A per-route setup failure ends the route with
  `error=setup_failed` (unclear, never wrong). If a setup script
  needs a system package on the runner (AnyMemo's `setup_route_07.py`
  / `setup_route_18.py` copy `DejaVuSans.ttf` from system fonts —
  the runner needs `fonts-dejavu`), that prerequisite is documented
  in the script itself, and its absence fails loudly at setup.
- Work-emulator checkout (`$WEMU`, public `bugfixops/work-emulator`):
  `apks/<App>.apk` (instrumented debug builds), `classes/<App>/<i>/`
  (for JaCoCo reports), `fixtures/`, `ci/apps.csv`, `ci/app_env.py`
  (prints `PKG`, `RECEIVER`, `APK`, `CLASSES` for an app).

## The harness (D2)

`device/harness/` is Python 3 standard library plus adb only. A route
script builds one `Runner`:

```python
from device.harness import Runner
r = Runner(package="org.example.app", route="route_01",
           edge_ids=["E0123...", ...], log_path="steps/route_01.log")
```

Functions: `launch(component)`; `tap(text=|res_id=|desc=)` and
`tap(x=, y=, why=)`; `long_tap(...)`; `drag(x1, y1, x2, y2,
duration_ms, why=)` and `drag_from(x2, y2, text=|res_id=|desc=,
duration_ms, why=)` (long-press drags: a swipe whose duration
covers the ~500 ms long-press threshold registers as a press first
and then a drag — widget placement through the launcher);
`type_text(s)`; `key(name)`; `back()`; `rotate(orientation)`;
`kill_app()` (HOME, then `am kill` — HOME first is enforced, since
`am kill` only kills background processes); `relaunch(component)`
(fresh task stack — NOT a stack restore);
`restore_from_recents(text)` (APP_SWITCH, 1 s settle, tap the
recents card — the system restores the stack with
savedInstanceState); `set_always_finish(bool)` and
`set_locale(locale)` (GLOBAL settings: `pm clear` does NOT reset
them, so a script that changes one MUST restore it before
`done()`); `two_finger_swipe(device, start1, start2, end1, end2,
steps)` and `two_finger_tap(device, point1, point2)` (sendevent MT
slot-protocol sequences, one shell command each; the touchscreen
event node varies per emulator — discover it with `adb shell
getevent -i` and pass it as `device`; a wrong node silently does
nothing, so a gesture on a wrong node is unclear, never wrong);
route scripts read `$TOUCH_DEVICE` (discovered once per run by
run_app.sh from `getevent -i` via `device/touch_device.py`,
defaulting to `/dev/input/event0` when discovery fails) instead
of hardcoding a node; `dwell(seconds)` (host-side sleep, 0 <
seconds <= 600, no adb call — timed routes); `scroll_to(text=|res_id=)`;
`wait_for(text=|res_id=, timeout)`; `tap_row_action(row_text,
res_id)` (drawer rows whose action view shares one res_id across
rows: resolves the row by text, then taps that row's action node
— closest centre-y within 100 px — instead of the first row's
icon; anything else fails loudly, never taps the wrong row);
`start_intent(action, data,
mime, extras, component)`; `broadcast(action, extras, component)`;
`grant(perm)` / `deny(perm)`; `push_fixture(path)`;
`screenshot(name)` / `dump_ui(name)`; `assert_text(text)`;
`comment(text)` for no-action edges.

Rules:

- Every action takes an `edge=` id, and every action logs one line
  to the steps log: `<UTC ISO> <edge> <action> <target> <result>`.
  An edge id not in the route's edge list raises `ValueError`.
  Setup scripts pass `edge_ids=None` (no edge checks).
- Views are found by parsing `uiautomator dump` (resource-id, text,
  or content-desc) and tapping the centre of the bounds. Fixed
  coordinates are allowed only with a `why` string saying why no
  id, text, or desc exists.
- Dry-run mode (`dry_run=True`) never calls adb: it records the
  planned commands and validates edge ids. Node resolution is
  skipped in dry mode (there is no device to dump).
- Tests: `python3 -I device/harness/test_harness.py` (30 tests,
  sample dumps shaped from Currency layout XML).
- System UI needs no special primitive: the dump path has no
  package filter, so `dump_ui` / `tap` / `wait_for` / `scroll_to` /
  `assert_text` operate on whatever is foreground — the system
  file picker, permission dialogs, and the launcher are driven
  with the same primitives as app UI. A route that needs the
  picker or the launcher documents that in its header.

## Route scripts (D3)

A script runs as:

```
python3 -I device/routes/<App>/route_NN.py --package <pkg> \
  --log steps/route_NN.log --outdir <outdir> [--dry-run] [--adb adb]
```

from the repo root. Because `python3 -I` ignores `PYTHONPATH`, the
script bootstraps `sys.path` from its own location (four
`dirname` calls up from `device/routes/<App>/route_NN.py` reach the
repo root) and then does `from device.harness import Runner`. Exit 0
means ok; any other exit (except 124, which `timeout` uses for a
timeout) means failed.

Body: one block per route edge, in route order, each block commented
with its edge id and the edge's trigger text, calling the harness.
Start from the edge's `gui` list and trigger text in
`out/<prefix>_trigger_graph.json`, plus layout XML (`res/layout*/`,
`res/menu/`, `res/xml/`), `strings.xml`, and printed handler source
(`.agents/tasks/ui-map-<App>.md` files are leads only). Lifecycle
and framework edges with no user action get a `comment(...)` block,
not a tap. An intent from another app, a system broadcast, boot, or
a widget becomes `start_intent` / `broadcast` over adb, with a
comment. Time, network, or hardware conditions adb cannot create on
an AOSP emulator make the route `unscriptable: <reason>` in
ROUTES.csv instead of a script.

Standard configuration for every route: start from `pm clear <PKG>`,
grant only the ROUTES.csv permissions, push only the listed
fixtures, run the listed setup steps first. One exception:
permission-dialog routes (method `onRequestPermissionsResult`) are
NOT pre-granted — their edges include the permission dialog itself,
and pre-granting would prevent it from appearing; the script drives
the dialog instead (see the runner section).

## The runner (D4)

`bash device/run_app.sh <App> <glob> <outdir> [--dry-run]`. Real mode
installs the APK with `adb install -r -t` — WITHOUT `-g`, so each
route grants only its own permissions. Exception: permission-dialog
routes (method `onRequestPermissionsResult`) skip pre-grants
entirely, because their route includes the dialog; pre-granting
would prevent it from appearing. Environment: `WEMU` (required);
`RUN_ID` (default `local-<UTC timestamp>`); `JACOCO_JAR`
(default `$WEMU/.cache/jacococli.jar`); `WITH_SSH_SERVER=1` (see
below); `SSH_PORT` (default 2222); `TOUCH_DEVICE` (discovered per
run, see below).

### Throwaway SSH server (`WITH_SSH_SERVER=1`)

For routes that need a live SSH server (Amaze SFTP routes), the
runner starts a per-run `sshd` on the CI host before the route
loop: host key + client keypair generated at run time with no
passphrase (never committed, never logged), listening on
127.0.0.1:`$SSH_PORT`, password auth off, only the per-run client
key authorized, serving only the CI user. The emulator reaches
the host at 10.0.2.2:`$SSH_PORT`. Route scripts that need the
client key read `$OUTDIR/ssh_client_key` via their `--outdir`
argument and push it to the device themselves. run_app.sh
exports `$SSH_PORT` (default 2222) and `$SSH_USER` (the CI
user's login name, from `whoami`) for route scripts, so scripts
never hardcode a port or a username that varies per runner
image. The server is
killed on exit (trap) so no per-run server outlives the run. If
`sshd`/`ssh-keygen` is missing or the server fails to start, the
run exits 2 immediately with a provisioning message — SSH routes
are never run without a server. SMB is NOT supported this way:
`smbd` needs root (ports 139/445 plus user management), so routes
needing a live SMB host stay unscriptable with that precise
reason; no user-space SMB server is faked.

### Touchscreen node (`TOUCH_DEVICE`)

Multi-touch scripts read `$TOUCH_DEVICE` (default
`/dev/input/event0` when unset). The runner discovers it once per
run from `adb shell getevent -i` via `device/touch_device.py`
(the device whose ABS set has MT POSITION_X/Y). If discovery
fails, scripts fall back to the default node and a gesture on a
wrong node is unclear, never wrong.
`pm clear`; app setup + per-route setup (if present) + fixtures +
grants; one coverage dump, discarded (the receiver resets
counters); the script with a 10-minute timeout;
a final coverage dump; a JaCoCo report for that dump (`--classfiles`
from `CLASSES`); `device/jacoco_lookup.py` maps the target method
(graph name to class/name/descriptor via `tools/build_graph.py`
`method_names`, the `tools/emu_compare.py` pattern) in the JaCoCo
XML report (`INSTRUCTION covered > 0` means reached).

`<outdir>/results.csv` columns:
`app,route,method,edges,reached,script_status,steps_done,steps_total,
error,run_id`.

- `reached`: `yes`, `no`, or `not_run`. Coverage truth is reported
  even when the script failed or timed out. A missing/invalid final
  dump gives `not_run` with `error=coverage_missing`; a method absent
  from the JaCoCo report gives `no` with
  `error=method_absent_in_report`.
- `script_status`: `ok`, `failed_at_step_N` (N = steps_done + 1;
  step 0 = setup, per-route setup, or fixture phase), `timeout`, or
  `unscriptable`. Unscriptable rows have no script and are never
  executed.
- `steps_total` comes from a dry-mode planning pass of the script
  before the real run; `steps_done` is the lines in the real steps
  log. Evidence per route: `screens/route_NN/` and
  `logcat/route_NN.txt` in `<outdir>`.

`--dry-run` runs no adb: it runs `device/drycheck.py --load-scripts`,
which checks every ROUTES.csv edge id exists in the current trigger
graph, the edges form a contiguous chain from `S_ENTRY` to the
method node (a trailing `@VARIANT` suffix on the final node is
allowed), the method exists in `methods.csv`, permissions are
declared in the manifest, and every fixture entry resolves: plain
entries under `$WEMU/fixtures`, `<repo-relative> -> <dst>` entries
as committed text files under `device/routes/<App>/`, and
`gen:<name> -> <dst>` entries via an existing, compiling
per-route setup script named in the route's setup cell. Any other
fixture form FAILs loudly. Every scripted script must also accept
`--adb` (run_app.sh always passes it; a script without the
argument would exit 2 live even though the dry run passes) and
load in dry mode under the harness. With `--load-scripts`, every
file a script pushes in dry mode must be named in the route's
fixtures cell (basename match) — a script pushing an unlisted file
FAILs. Launch-component resolution is NOT checked here: dry mode
never resolves a component, so scripts' launch components are
verified by the script audit against the printed manifest. An
unscriptable row PASSes on a non-empty reason alone — that checks
only that a reason EXISTS; reason substance is verified directly
by the unscriptable-retry table and the independent audit, not by
drycheck. It writes `<outdir>/dryrun_report.txt`:
one line per route (`PASS`, or `FAIL` with reason) plus
`<App>: N PASS, M FAIL`. The dry run ignores the glob and checks
every ROUTES row.

## Collect and compare (D5, D6)

- `python3 -I device/collect.py collected <dest>`: see "What the
  workflow does" step 3. Logs over 5 MB are truncated with a marker.
  Tests: `python3 -I device/test_collect.py`.
- `python3 -I device/compare.py <results_dir> [--out-root R]`: reads
  `<results_dir>/<App>/results.csv` (a committed
  `device/results/<run>/` folder) and writes
  `<out-root>/<App>/device/results.csv` with columns
  `route,method,edges,reached,script_status,run,script` (`run` = the
  input directory basename, `script` = `<route>.py`). `--out-root`
  defaults to `<repo>/graphs`; tests use a temp dir so no real
  `graphs/<App>/device/results.csv` is written in this phase.
  Tests: `python3 -I device/test_compare.py`.

## DEVICE rows (D7)

After a real run, `device/compare.py` output feeds each app's
`make_verification.py`: when `graphs/<App>/device/results.csv`
exists, it appends one row per route AFTER the existing rows, in
`device/results.csv` order, without re-sorting existing rows:
`type=path`, `item=<method>`, `result=correct` when reached,
otherwise `unclear`, `confirmed_by=DEVICE`,
`ref=device run <run>/<script>`, `edges=<edges>`, `note` = script
status (for `unclear`, the reason: not reached, script failed, or
unscriptable). A route not reached never becomes `wrong`, and no
label changes. When the file does not exist, `make_verification.py`
output must be byte-identical to before. Full spec with the
synthetic-results test: `device/D7_SPEC.md`. D7 changes go through
each app's merger, not the device lead.

## How to interpret a run

- `reached=yes`: the target method's instructions executed during
  the route's final coverage window.
- `reached=no`: the script ran (or partly ran) but the method did
  not execute — the route as scripted does not reach it.
- `reached=not_run`: no coverage evidence (missing dump, or the
  route was unscriptable). It is not evidence for or against the
  label; unscriptable routes stay `unclear` in verification.
- `unscriptable` routes (at most 10% per app, each with a reason)
  are reported honestly, never forced into scripts.

## After a run (D8)

1. `device/compare.py` writes `graphs/<App>/device/results.csv`.
2. Each app's `make_verification.py` runs and adds DEVICE rows.
3. A CI rebuild updates `out/`.
See `handoff/NEXT_DEVICE_REPLAY.md` for route counts per app, the
unscriptable list, and the environment/secrets list (none needed:
public repos, no credentials, no APK uploads).
