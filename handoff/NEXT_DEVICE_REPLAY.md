# Next device replay (API 27, GitHub Actions)

Status (2026-11-02, generated from the branch ROUTES.csv files):
device route lists (D1) and route scripts (D3) are done for the
eight ticked apps and for AmazeFileManager (9 apps, 275 routes,
264 scripted, 11 unscriptable); the other four apps' route lists
and scripts start when each app's final route table exists.
No real emulator run has started, and none starts from here:
the user starts it by hand (below).

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

## Workflow-side requirements for Amaze SSH routes (for the
user's reviewer — the workflow file itself is not edited here)

For Amaze SSH routes, `.github/workflows/device-replay.yml` needs
exactly these two items, and nothing else is asserted here:

- a step installing openssh-server (apt);
- WITH_SSH_SERVER=1 for Amaze jobs only.

The reviewer applies these to the workflow; this file does not
edit `.github/` or any workflow file. Amaze SSH routes are 07,
08, 23, 29 and 30; all of them need the throwaway sshd
(`device/run_app.sh` under WITH_SSH_SERVER=1) at run time.

## Route counts per app (D1)

Ticked apps (one route per `verification.csv` path row):

| App | Routes | Scripted | Unscriptable |
|---|---|---|---|
| Currency | 28 | 28 | 0 |
| Diary | 30 | 30 | 0 |
| hash-checker | 37 | 36 | 1 |
| Omni-Notes | 33 | 31 | 2 |
| openlauncher | 27 | 26 | 1 |
| Vanilla-Music | 30 | 30 | 0 |
| Markor | 30 | 30 | 0 |
| AnyMemo | 30 | 27 | 3 |
| Total (ticked) | 245 | 238 | 7 |

AmazeFileManager (this push): 30 routes, 26 scripted, 4
unscriptable (13.3% — accepted under the user's cap ruling, so
F1 is not blocked by the cap alone): route_05
`StreamSource.getCurrentPosition` — reaching it requires a
configured cloud provider account and a media file inside it;
route_06 `StreamSource.read` — a live SMB server plus a resolving
external player are required, and the jcifs SMB1 handshake and
the player resolver remain unproven (a CI-host smbd is
provisionable with sudo in principle, so root alone is not the
reason); route_12 `StreamNotFoundException.<init>(Throwable)` —
reachable only through a write failure the harness cannot
arrange; route_22 `SmbSearchDialog$1.lambda$computerFound$0` —
broadcast SMB discovery cannot cross the emulator router.
Routes 08 and 23 converted to scripted in this push, and
route_22's edge list was refreshed to the post-fix verification
row. Amaze SSH routes (07, 08, 23, 29, 30) need
WITH_SSH_SERVER=1 (see the workflow section above).

Other four apps (AnkiDroid, MMEX, Aegis, LibreTorrent): counts
pending — one route per final route-check sample row, once each
app's route table is final.

## Unscriptable routes (with reasons)

- Omni-Notes route_13 `TextHelper.getAlternativeTitle`:
  needs the DashClock or Pushbullet host app installed and calling the extension; neither host app is available on the AOSP emulator.
- Omni-Notes route_17 `UpgradeProcessor.<init>`:
  needs an older-version database on disk (install an old build with data, then update); no old-version database fixture exists in $WEMU/fixtures.
- openlauncher route_14 `AutoFinishActivity.onCreate`: the caller
  package must be `org.kustom.wallpaper` or `org.kustom.widget`;
  adb runs as shell with no calling package, and no such caller app
  is among the inputs.
- AnyMemo route_02 `UploadDropboxActivity.onDestroy` and route_08
  `DropboxApiHelper$4.call`: a Dropbox account and saved access
  token cannot be created by adb on an AOSP emulator (no account or
  token fixture exists; OAuth login in an external browser/Custom
  Tab and api.dropboxapi.com reachability required).
- AnyMemo route_17 `Card.toString`:
  DAO-failure state cannot be created by adb on an AOSP emulator (Card.toString fires only in the RuntimeException at LearnQueueManager.java:267 when cardDao.update returns 0; this chain's flush is the build-time flush with an empty dirtyCache; and deleting the card trips the earlier :263 LearningData check first).
- hash-checker route_31 `LogUtils.e`:
  LogUtils.e fires only in the ActivityNotFoundException catch when no app handles ACTION_OPEN_DOCUMENT (HashCalculatorFragment.java:191-200); on the replay image DocumentsUI handles the intent, and the harness has no supported component-disable action.

All other ticked routes are scripted. Unscriptable share per app is
within the 10% limit everywhere except AnyMemo, which is exactly at
it: Omni-Notes 6.1% (2/33), openlauncher 3.7% (1/27), AnyMemo 10.0%
(3/30), hash-checker 2.7% (1/37), the rest 0%. AmazeFileManager
(4/30 = 13.3%) is covered by its own cap acceptance above, not by
this paragraph.

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
