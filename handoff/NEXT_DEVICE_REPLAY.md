# Next device replay (API 27, GitHub Actions)

Status: device preparation for the eight ticked apps' route lists is
done (D1). Route scripts (D3) for those apps are in progress; the
other five apps' route lists and scripts start when each app's final
route table exists. No real emulator run has started, and none starts
from here: the user starts it by hand (below).

## Where and how

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31`.
- Workflow: `.github/workflows/device-replay.yml` (read it first;
  never edit it or anything under `.github/`).
- Dry run: push `handoff/DEVICE_DRYRUN_REQUEST.txt` (line 1 a
  comment, line 2 `# request <UTC time> <purpose>`, then app names
  or `all`). Only the coordinator sends it, at most once per 15
  minutes. Accept when every app shows all scripted routes PASS in
  `device/dryrun/<run>/SUMMARY.md`.
- Real run: the user starts it by hand from the workflow page with
  `dry_run=false`, after choosing the emulator image. Never start a
  real run from an agent, and never run adb against a real device.

## Environment and secrets

None needed. Both repos are public (`ground-truth-results` and
`bugfixops/work-emulator`, which supplies the instrumented debug
APKs, classes, fixtures, and `ci/app_env.py`). No credentials, no
tokens, no APK uploads into this repo. `adb`, `java`, and `python3`
are on the runner.

## Route counts per app (D1)

Ticked apps (one route per `verification.csv` path row):

| App | Routes | Scripted | Unscriptable |
|---|---|---|---|
| Currency | 28 | 28 | 0 |
| Diary | 30 | 30 | 0 |
| hash-checker | 37 | 37 | 0 |
| Omni-Notes | 33 | 31 | 2 |
| openlauncher | 27 | 26 | 1 |
| Vanilla-Music | 30 | 30 | 0 |
| Markor | 30 | 30 | 0 |
| AnyMemo | 30 | 28 | 2 |
| Total (ticked) | 245 | 240 | 5 |

Other five apps (AmazeFileManager, AnkiDroid, MMEX, Aegis,
LibreTorrent): counts pending — one route per final route-check
sample row, once each app's route table is final.

## Unscriptable routes (with reasons)

- Omni-Notes route_01 `DetailFragment.onCoordinatesResolved`:
  geocoder backend unavailable on an AOSP emulator (Android
  Geocoder returns no results without a backend service).
- Omni-Notes route_15 `DetailFragment.removeAttachment(Attachment)`:
  the verification path row has no edges and `methods.csv` marks
  the method UNREACHABLE (`branch_never_taken`); there is no route
  to script. Flagged to the ticked-app stream: whether this path
  row should stay a path row is their call, not a device change.
- openlauncher route_14 `AutoFinishActivity.onCreate`: the caller
  package must be `org.kustom.wallpaper` or `org.kustom.widget`;
  adb runs as shell with no calling package, and no such caller app
  is among the inputs.
- AnyMemo route_02 `UploadDropboxActivity.onDestroy` and route_08
  `DropboxApiHelper$4.call`: a Dropbox account and saved access
  token cannot be created by adb on an AOSP emulator (no account or
  token fixture exists; OAuth login in an external browser/Custom
  Tab and api.dropboxapi.com reachability required).

All other ticked routes are scripted. Unscriptable share per app is
within the 10% limit everywhere (Omni-Notes 6.1%, openlauncher
3.7%, AnyMemo 6.7%, the rest 0%).

## After a run, in order

1. `python3 -I device/compare.py device/results/<run>/` writes
   `graphs/<App>/device/results.csv` (one per app in the run).
2. Each app's `make_verification.py` runs and adds DEVICE rows
   (spec: `device/D7_SPEC.md`; a route not reached never becomes
   `wrong`, and no label changes).
3. A CI rebuild (`handoff/REBUILD_REQUEST.txt`) updates `out/`.
4. Results land in `device/results/<run>/` (small text only);
   screenshots and UI dumps stay in the 30-day run artifacts.

## Reading a result

- `reached=yes`: the method executed during the route's window.
- `reached=no`: the script ran (or partly ran) but the method did
  not execute.
- `reached=not_run`: no coverage evidence (missing dump, or the
  route was unscriptable). Not evidence for or against the label;
  unscriptable routes stay `unclear` in verification.
- Full contract: `device/README.md`.
