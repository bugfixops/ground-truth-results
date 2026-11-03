# Next device replay (API 27, GitHub Actions)

Status (2026-11-03, generated from the branch ROUTES.csv files):
device route lists (D1) and route scripts (D3) are done for all
13 apps (389 routes, 355 scripted, 34 unscriptable), and every app
passed the final all-apps dry run `41576644702-1` (FAIL 0 for all
13). The workflow is ready for the real run (commit `e6ad6ad8`:
Google APIs x86_64 default, Amaze SSH server), and the all-apps dry
run after that edit, `41578222764-1`, passed (FAIL 0 for all 13).
No real emulator run has started, and none starts from here: the
user starts it by hand (below).

Emulator image: Google APIs, x86_64, API 27 (`target: google_apis`),
user decision 2026-11-03.

## Where and how

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31`.
- Workflow: `.github/workflows/device-replay.yml` (read it first;
  agents never edit it or anything under `.github/`, except the
  user-approved edit of 2026-11-03, commit `e6ad6ad8`).
- Dry run: push `handoff/DEVICE_DRYRUN_REQUEST.txt` (line 1 a
  comment, line 2 `# request <UTC time> <purpose>`, then app names
  or `all`). Only the coordinator sends it, at most once per 15
  minutes. Accept when every app shows all scripted routes PASS in
  `device/dryrun/<run>/SUMMARY.md`.
- Real run: the user starts it by hand from the workflow page with
  `dry_run=false` (image chosen: Google APIs x86_64, see below).
  Never start a real run from an agent, and never run adb against
  a real device.

## Environment and secrets

None needed. Both repos are public (`ground-truth-results` and
`bugfixops/work-emulator`, which supplies the instrumented debug
APKs, classes, fixtures, and `ci/app_env.py`). No credentials, no
tokens, no APK uploads into this repo. `adb`, `java`, and `python3`
are on the runner.

## Workflow-side requirements for Amaze SSH routes: Done

Done in commit `e6ad6ad8` (user decision 2026-11-03): the workflow
has a step "SSH server for Amaze SSH routes" that installs
openssh-server (apt) for the AmazeFileManager job only, and the
"Emulator and route replay" step sets `WITH_SSH_SERVER=1` for the
AmazeFileManager job only (`0` for every other app). Amaze SSH
routes are 07, 08, 23, 29 and 30; `device/run_app.sh` starts the
throwaway sshd for them at run time.

## How the user starts the real run

1. On GitHub: Settings → General → Default branch, switch to
   `work-2026-10-31`, and confirm.
2. Actions → "Device replay" → Run workflow. Choose branch
   `work-2026-10-31` and set:
   - apps `all`
   - routes `route_*.py`
   - api_level `27`
   - target `google_apis`
   - arch `x86_64`
   - dry_run `false`
3. Wait about 1 to 1.5 hours (all 13 apps run in parallel; each
   route stops after 10 minutes at most; each app's job stops after
   340 minutes at most). The last job (`collect`) commits
   `[device] results <run>`, with the results under
   `device/results/<run>/`.
4. Tell Kiro the run id; processing the results (Part B) starts then.

## Route counts per app (D1)

One route per `verification.csv` path row (the final route-check
sample for AnkiDroid, MMEX, Aegis and LibreTorrent):

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
| AmazeFileManager | 30 | 26 | 4 |
| AnkiDroid | 30 | 26 | 4 |
| MMEX | 30 | 26 | 4 |
| Aegis | 25 | 22 | 3 |
| LibreTorrent | 29 | 17 | 12 |
| Total | 389 | 355 | 34 |

AmazeFileManager's 4 unscriptable of 30 (13.3%) is accepted under the
user's cap ruling, so F1 is not blocked by the cap alone. AnkiDroid,
Aegis and LibreTorrent: routes judged WRONG are listed as
`unscriptable: route WRONG as drawn` under the user's stopping rule
(no fix round). MMEX and Aegis: their unscriptable share was accepted
by recorded decisions (MMEX-D3-CAP, Aegis-D3-CAP-ACCEPT). Amaze SSH
routes (07, 08, 23, 29, 30) need WITH_SSH_SERVER=1 (see the workflow
section above).

## Unscriptable routes (with reasons)

- hash-checker route_31 `LogUtils.e`: LogUtils.e fires only in the ActivityNotFoundException catch when no app handles ACTION_OPEN_DOCUMENT (HashCalculatorFragment.java:191-200); on the replay image DocumentsUI handles the intent, and the harness has no supported component-disable action.
- Omni-Notes route_13 `TextHelper.getAlternativeTitle`: needs the DashClock or Pushbullet host app installed and calling the extension; neither host app is available on the AOSP emulator
- Omni-Notes route_17 `UpgradeProcessor.<init>`: needs an older-version database on disk (install an old build with data, then update); no old-version database fixture exists in $WEMU/fixtures
- openlauncher route_14 `AutoFinishActivity.onCreate`: caller package must be org.kustom.wallpaper or org.kustom.widget (FiveSecsDelayContentProvider.checkCallingPackage); adb shell content delete runs as shell with no calling package and throws SecurityException, and no such caller app is among the inputs
- AnyMemo route_02 `UploadDropboxActivity.onDestroy`: Dropbox account and saved access token cannot be created by adb on an AOSP emulator (no Dropbox account or token fixture exists; OAuth login in an external browser/Custom Tab and api.dropboxapi.com reachability required)
- AnyMemo route_08 `DropboxApiHelper$4.call`: Dropbox account and saved access token cannot be created by adb on an AOSP emulator (no Dropbox account or token fixture exists; OAuth login in an external browser/Custom Tab and api.dropboxapi.com reachability required)
- AnyMemo route_17 `Card.toString`: DAO-failure state cannot be created by adb on an AOSP emulator (Card.toString fires only in the RuntimeException at LearnQueueManager.java:267 when cardDao.update returns 0; this chain's flush is the build-time flush with an empty dirtyCache; and deleting the card trips the earlier :263 LearningData check first)
- AmazeFileManager route_05 `StreamSource.getCurrentPosition`: reaching the target requires a configured cloud provider account and a media file inside it, which adb and the harness cannot create
- AmazeFileManager route_06 `StreamSource.read(byte[],int,int)`: reaching read() requires a live SMB server and an external player fetching the app's local HTTP stream; the harness provides no SMB server fixture and adb cannot create one
- AmazeFileManager route_12 `StreamNotFoundException.<init>(Throwable)`: the (Throwable) constructor is reachable only through a write failure the harness cannot arrange (read-only content URI grant; delete-then-save yields EXCEPTION_IO, not the RuntimeException needed)
- AmazeFileManager route_22 `SmbSearchDialog$1.lambda$computerFound$0`: computerFound fires ONLY when a real SMB host responds on the local network (adb cannot create one; the emulator network has no SMB host)
- AnkiDroid route_02 `EasyX509TrustManager.<init>`: reaching the target requires a logged-in AnkiWeb account (stored hkey non-empty) and a real HTTPS sync to the AnkiWeb server; no test account exists and a real sync must not be attempted; with an empty hkey the flow diverts to the not-logged-in dialog before any Connection.sync
- AnkiDroid route_26 `CollectionLoader.deliverResult`: the row's only entry is the no-space dialog, shown only when BackupManager.enoughDiscSpace is false (DeckPicker.java:848-850); no harness action (launch, tap, key, type, scroll, rotate, push_fixture) creates a below-threshold free-space state, the threshold is 10 MiB (BackupManager.java:47, 207-208), and filling storage risks breaking the collection load the route itself needs; other loader entries (for example Reviewer onCreate) are not this row's route and must not be substituted
- AnkiDroid route_36 `Models.validateBrackets`: route WRONG as drawn (see route_table.md)
- AnkiDroid route_37 `Collection.getServer`: route WRONG as drawn (see route_table.md)
- MMEX route_07 `StockHistoryRepository$UpdateType.<init>`: needs an investment account row to tap (no account exists on a fresh database, no row text grounded, no MMEX database fixture in $WEMU/fixtures) plus Morningstar as configured quote provider and a live Morningstar price download, a network result adb cannot create (follow-up: specified-but-unverified HTTP substitute)
- MMEX route_08 `CurrencyRepository.saveExchangeRate`: ENV gate needs a live Fixer price download to finish while the currency list is started (FixerService BASE_URL https://api.fixer.io); a network result adb cannot create (follow-up: specified-but-unverified HTTPS/CA substitute)
- MMEX route_11 `DatabaseMetadataFactory.getInstance(String,String)`: requires a real online cloud-storage account (Dropbox/OneDrive/GoogleDrive/Box/pCloud) holding a remotely-modified database; the sync-on-start plus remote-only pull branch cannot be produced by adb, fixtures, or setup (genuinely unscriptable on current evidence)
- MMEX route_19 `ExceptionHandler.getLogcat`: double blocker, genuinely unscriptable on current evidence: (a) the prefix reaches showMessage only when the base currency is null, but an app-created database always sets a base currency; (b) getLogcat executes only if Toast.show() throws inside the posted Runnable's catch, and no grounded fault trigger exists on a normal foreground flow
- Aegis route_02 `FreeOtpImporter$DecryptedStateV2.<init>`: rooted device plus su grant plus installed FreeOTP V2 tokens.xml data; no in-run producer (table steps 48, 50, 52); adb root does not provide the app's libsu su call
- Aegis route_09 `IconAdapter$CategoryHeader.getPosition`: drawn route omits the Google Authenticator app-import sub-flow needing root plus an installed Google Authenticator app plus its import result, and an installed icon pack (table steps 46, 48); creating entries in-run cures neither precondition
- Aegis route_17 `AuthActivity.lambda$onCreate$3`: drawn steps false as drawn: step 28 lock-icon tap impossible (lock item hidden on the unencrypted NONE vault, MainActivity.java:1155-1160) and step 35 biometric-button tap impossible (no BiometricSlot plus keystore key; steps 8 and 21-22 contradict a biometric vault); changing the vault type would be a different route, not this one
- LibreTorrent route_02 `TorrentDownloadImpl.havePiece`: step 13 (NanoHTTPD$ClientHandler.run) needs an HTTP client connected to the app streaming server and the route needs a downloaded piece to stream (TorrentInputStream.waitForPiece); no harness primitive makes an HTTP request on the device, and piece data needs a live BitTorrent peer (network)
- LibreTorrent route_03 `FeedDao_Impl$11.finalize`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_04 `PathResolver.join`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_05 `SafFileSystem$FakePath.serialize`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_06 `FeedDao_Impl$1.bind`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_07 `BaseElement.getUri`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_08 `AdvancedPeerInfo.isUtp`: the route builds a PeerInfo for a connected peer (PeerInfo.java:110); a connected BitTorrent peer needs a live swarm on the network, which adb cannot create on an AOSP emulator
- LibreTorrent route_11 `AddTagViewModel$TagAlreadyExistsException.<init>`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_12 `SettingsRepositoryImpl.proxyRequiresAuth(boolean)`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_13 `TorrentEngine$5.lambda$onTorrentMoving$4`: the route needs a torrent that finishes downloading (TorrentDownloadImpl.handleTorrentFinished, step 11) with move-after-download on; finishing needs the data from a live BitTorrent peer (network)
- LibreTorrent route_20 `SafFileSystem.getParentDirUri`: route WRONG as drawn (see route_table.md)
- LibreTorrent route_22 `SafFileSystem$FakePath.makeRelativePathNodes`: route WRONG as drawn (see route_table.md)

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
