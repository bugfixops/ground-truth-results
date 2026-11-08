# Aegis device routes — run_app.sh wiring (no runner fork)

No change to any shared runner, workflow, or harness file is proposed or
made by this package. The per-app layer only is placed, exactly as the D7
plan requires: `device/routes/Aegis/` containing ROUTES.csv, one
`route_NN.py` per scripted route, per-route `setup_route_NN.py`
generators, and a no-op `setup.py` (see ROUTES_NOTES.md for why the
shared setup is a no-op proposal).

## Placement (done in this push)

Placed in this push: `turn/device-final/routes/` contents copied to `device/routes/Aegis/` in the repo (ROUTES.csv from `turn/device-final/ROUTES.csv` to `device/routes/Aegis/ROUTES.csv`). File list:

- ROUTES.csv (25 rows, sampler order).
- route_01, 03, 04, 05, 06, 07, 08, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20,
  21, 22, 23, 24, 25 (.py; 22 scripts). No route_02, route_09, or
  route_17 script exists, by design (unscriptable rows).
- setup_route_01, 03, 04, 05, 06, 07, 08, 12, 14, 15, 16, 18, 20 (.py;
  13 generators). No setup_route file for rows without a `gen:` fixture.
- setup.py (no-op; logs only).

## Runner invocation (coordinator action, not done here)

From the repo root, with a booted emulator (real run) or without one
(dry run), the shared runner is invoked unchanged, for example:

- Dry run: `bash device/run_app.sh Aegis "route_*.py" <outdir> --dry-run`
- Real run (user-started only; never started from this side):
  `bash device/run_app.sh Aegis "route_*.py" <outdir>`

Per-route order inside the runner (current phase-2 contract, verified
against the runner text for this staging note): dry plan first; then
`pm clear`; then shared `setup.py` if present; then per-route
`setup_<route>.py` if present (with `--gen-dir <outdir>/gen/<route>`,
generating the `gen:` files); then fixture push for every ROUTES.csv
fixture entry (for `gen:` entries, from the gen dir to the stated device
path); then per-route permission grants from ROUTES.csv (with the single
literal exception: methods containing `onRequestPermissionsResult` skip
pre-grants — no Aegis row triggers it); then a discard coverage dump,
the route script under a 10-minute timeout, a final coverage dump, a
JaCoCo report against `classes/Aegis/0`, and `jacoco_lookup.py` mapping
for the target method. Output: `<outdir>/results.csv` plus steps logs,
screens, and logcat evidence.

## D9 gate (what a dry run must show before D9 can be claimed)

D9 passes for Aegis ONLY when EVERY scripted route shows PASS in
`dryrun_report.txt` (one FAIL fails the app's dry run; there is no
partial-pass threshold). The dry run checks every ROUTES.csv row,
scripted and unscriptable, and for scripted rows it checks: every edge
id exists in the CURRENT trigger graph; the edges form a contiguous
chain from S_ENTRY to the method node; the method exists in methods.csv;
permissions are declared in the manifest; `gen:` fixtures resolve via
an existing, compiling `setup_<route>.py` named in the ROUTES.csv setup
cell; and every scripted script loads in dry mode with no edge error
and with a `--adb` argument (run_app.sh passes `--adb adb` on live runs;
a script lacking it would exit 2 on a live run even if the dry run
passed — all staged scripts accept `--adb`).

Dry-mode blind spot, stated explicitly (it must appear in the merger
review, not be hidden): dry mode skips node resolution, so a wrong
launch component would PASS the dry run and fail every real run. The
launch component staged here
(com.beemdevelopment.aegis.debug/com.beemdevelopment.aegis.ui.MainActivity)
is the tree-manifest-verified component from the D7 plan, but the dry
run does NOT prove it; only a real run does. A dry-run PASS must never
be presented as launch coverage.

## What is NOT wired here

- No `.github/workflows/device-replay.yml` edit, no DEVICE_DRYRUN
  request, no REBUILD_REQUEST, no CI watch. Drycheck and any real run
  are coordinator-dispatched later.
- No timeout change (10 minutes per route stands; the longest staged
  route is 67 steps).
- No new runner flags, results.csv columns, coverage receiver, APK
  install change, or workflow change.
