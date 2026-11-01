# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 22 — proposal

**UNVERIFIED proposal — NOT merged. No build, sampler, grep, or C1 count is claimed.**
Connector-only work (GitHub connector, branch `work-2026-10-31`, repo `bugfixops/ground-truth-results`).
No token, no local checkout, no push, no edit to `graph_def.py` / `out` / `progress` / `tools`.

## Membership (confirmed first, not guessed)

All 40 rows below are batch 22 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`
(plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`), each
`TODO_CANDIDATE_REACHABLE` — that plan status is a generator candidate, **not**
evidence, and is not used as evidence for any verdict below.

Source files printed (spaced, single-file, via the connector):

- `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/core/model/AddTorrentParams.java` (full, 143 lines)
- `…/core/model/DownloadsCompletedListener.java` (full, 87 lines)
- `…/core/model/SessionErrorFilter.java` (full, 33 lines)
- `…/core/model/TorrentEngine.java` (1659 lines; printed in sections, with
  line-filtered passes for the batch methods and their callers)
- `…/service/TorrentService.java` (sections: `onCreate` L105–114,
  `init()` L116–135, `stopEngine()` L157–162; plus line-filtered passes)

## Printed route anchors

1. **TorrentService (Android Service entry).** `TorrentService.onCreate`
   L109: `engine = TorrentEngine.getInstance(getApplicationContext());`
   `TorrentService.init()` L131: `engine.doStart();` and L132:
   `engine.addListener(engineListener);` `TorrentService.stopEngine()`
   L161: `engine.doStop();`
2. **TorrentEngine singleton.** `TorrentEngine.getInstance` L117–126
   constructs via L121 `INSTANCE = new TorrentEngine(appContext);`
   `TorrentEngine.<init>` L128–141: L135
   `downloadsCompleted = new DownloadsCompletedListener(this);`,
   L140 `session.addListener(engineListener);`. Field initialiser L113:
   `private SessionErrorFilter errorFilter = new SessionErrorFilter();`
3. **Engine start.** `TorrentEngine.doStart` L234–260, comment L230–232
   "Only calls from TorrentService"; L243
   `disposables.add(downloadsCompleted.listen() … .subscribe(…));`
   `doStop` L292–301: L296 `disposables.clear();`, L300 `cleanTemp();`.
4. **Session-error path.** `TorrentEngine.engineListener.onSessionError`
   L1384–1390: L1386 `if (errorFilter.skip(errorMsg)) return;`
   The listener itself is registered in the engine constructor (L140).

## Strict-entry caveat (explicit)

- `doStart` / `doStop` / `listen` and everything downstream of them are
  anchored at `TorrentService`, a Service entry — not a launcher entry.
  Which component starts `TorrentService` (and the `onStartCommand` →
  `init()` step) was not printed in this pass.
- Listener-callback rows (`DownloadsCompletedListener$1.*`,
  `onSessionError` → `skip`) rest on printed registration
  (`session.addListener(...)` / `engine.addListener(...)`); the session /
  framework dispatch that invokes the callback is INFERRED, not a printed
  app line.
- Internal-caller rows (e.g. `addTorrent(Uri)` via `scanTorrentsInDir`)
  rest on a printed call inside `TorrentEngine`; the caller method's own
  entry step was not always printed and is noted per row where relevant.
- A method called only from an OPEN method is OPEN, not REACHABLE
  (this is why `createFetchMagnetSingle` is OPEN: its only printed caller
  is the OPEN `fetchMagnet`).

## Per-row verdicts

### AddTorrentParams (4 rows)

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 1 | `AddTorrentParams.writeToParcel (Parcel, int)V` | OPEN | — | Definition printed (AddTorrentParams.java L96–107). Parcelable framework method; runs only when an `AddTorrentParams` is marshalled. No printed marshalling site (Intent extra / Bundle `putParcelable`) in this pass. Missing evidence: full-repo grep for `putExtra` / `putParcelable` / `getParcelableExtra` involving `AddTorrentParams`. |
| 2 | `AddTorrentParams$1.<init> ()V` | REACHABLE | SOURCE | Anonymous `Parcelable.Creator` instance: `public static final Parcelable.Creator<AddTorrentParams> CREATOR = new Parcelable.Creator<>() { … }` (AddTorrentParams.java L109). Class initialisation instantiates it when `AddTorrentParams` is first used, e.g. `new AddTorrentParams(…)` in `TorrentEngine.addTorrentSync(Uri, TorrentMetaInfo, Uri)` L1187–1198. |
| 3 | `AddTorrentParams$1.createFromParcel (Parcel)AddTorrentParams` | OPEN | — | Definition printed (L111–113: `return new AddTorrentParams(source);`). Framework-unmarshalling method; needs the same marshalling-site evidence as row 1. |
| 4 | `AddTorrentParams$1.newArray (int)AddTorrentParams[]` | OPEN | — | Definition printed (L116–118). Framework method; needs the same marshalling-site evidence as row 1. |

### DownloadsCompletedListener (9 rows)

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 5 | `DownloadsCompletedListener.<init> (TorrentEngine)V` | REACHABLE | SOURCE | `TorrentEngine.<init>` L135: `downloadsCompleted = new DownloadsCompletedListener(this);` |
| 6 | `DownloadsCompletedListener.lambda$listen$0 (CompletableEmitter, ArrayList)V` | REACHABLE | SOURCE for subscribe; INFERRED for Rx dispatch | The `Completable.create((emitter) -> { … })` body (DownloadsCompletedListener.java L47–85), subscribed in `TorrentEngine.doStart` L243–251. |
| 7 | `DownloadsCompletedListener.lambda$listen$1 (TorrentEngineListener)V` | REACHABLE | SOURCE for the call sites; INFERRED for session dispatch | The `eventHandler` Runnable (L50–53), run from `onTorrentFinished` L68–69 and `onTorrentRemoved` L75–76 when `torrentsInProgress.remove(id)` returns true. Runs only if a tracked downloading torrent finishes or is removed. |
| 8 | `DownloadsCompletedListener.lambda$listen$2 (CompletableEmitter)V` | REACHABLE | SOURCE for registration; INFERRED for Rx dispose | The `Disposables.fromAction(() -> engine.removeListener(listener))` action (L82–83), disposed when `doStop` clears `disposables` (TorrentEngine L296) or the emitter is disposed. |
| 9 | `DownloadsCompletedListener.listen ()Completable` | REACHABLE | SOURCE | `TorrentEngine.doStart` L243: `downloadsCompleted.listen()`. |
| 10 | `DownloadsCompletedListener$1.<init> (DownloadsCompletedListener, ArrayList, Runnable)V` | REACHABLE | SOURCE | Anonymous `TorrentEngineListener` created inside `listen()` (L55–78); instantiated when the `lambda$listen$0` body runs (row 6). |
| 11 | `DownloadsCompletedListener$1.onTorrentFinished (String)V` | REACHABLE | SOURCE for registration; INFERRED for session dispatch | Registered via `engine.addListener(listener)` (L81) → `TorrentEngine.addListener` L307–309 → `session.addListener(listener)`. Session invokes it when a torrent finishes (L66–70). |
| 12 | `DownloadsCompletedListener$1.onTorrentRemoved (String)V` | REACHABLE | SOURCE for registration; INFERRED for session dispatch | Same registration as row 11; body L73–77. |
| 13 | `DownloadsCompletedListener$1.onTorrentStateChanged (String, TorrentStateCode, TorrentStateCode)V` | REACHABLE | SOURCE for registration; INFERRED for session dispatch | Same registration as row 11; body L57–63 adds downloading torrents to `torrentsInProgress`. |

### SessionErrorFilter (3 rows)

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 14 | `SessionErrorFilter.<clinit> ()V` | REACHABLE | INFERRED for class-init ordering; SOURCE for the block | Static block L26–28 (`filteredErrors.add("Operation not supported on transport endpoint, code 95")`) runs on first class initialisation, before the field-initialiser construction at `TorrentEngine` L113. |
| 15 | `SessionErrorFilter.<init> ()V` | REACHABLE | SOURCE | Field initialiser `TorrentEngine` L113: `private SessionErrorFilter errorFilter = new SessionErrorFilter();` (implicit default constructor). |
| 16 | `SessionErrorFilter.skip (String)Z` | REACHABLE | SOURCE for the call; INFERRED for session dispatch | `TorrentEngine.engineListener.onSessionError` L1385–1386: `if (errorFilter.skip(errorMsg)) return;` Listener registered in the engine constructor (TorrentEngine L140). |

### TorrentEngine (24 rows)

| # | Method | Verdict (proposed) | confirmed_by | Route / citation |
|---|---|---|---|---|
| 17 | `TorrentEngine.<clinit> ()V` | REACHABLE | INFERRED for class-init ordering; SOURCE for the fields | No static block is printed; `<clinit>` is the static-field initialisation (`TAG` L97, `INSTANCE` L115), run before `getInstance` (L117) executes. |
| 18 | `TorrentEngine.<init> (Context)V` | REACHABLE | SOURCE | `getInstance` L121: `INSTANCE = new TorrentEngine(appContext);` Definition L128–141. |
| 19 | `TorrentEngine.addListener (TorrentEngineListener)V` | REACHABLE | SOURCE | `TorrentService.init()` L132; `DownloadsCompletedListener.listen()` L81; `TorrentEngine.observeEngineRunning()` L223. Definition L307–309 → `session.addListener`. |
| 20 | `TorrentEngine.addTorrent (Uri)V` | REACHABLE | SOURCE | Internal caller `scanTorrentsInDir` L1173: `addTorrent(Uri.fromFile(file));` Definition L359–361 → `addTorrent(file, null)`. Caveat: `scanTorrentsInDir`'s own caller was not printed. |
| 21 | `TorrentEngine.addTorrent (Uri, Uri)V` | REACHABLE | SOURCE | Called by row 20's method, L360: `addTorrent(file, null);` Definition L363–368 → `addTorrentCompletable(file, savePath)`. |
| 22 | `TorrentEngine.addTorrentCompletable (Uri)Completable` | REACHABLE | SOURCE | Internal caller in the watch-dir handler, L1149: `disposables.add(addTorrentCompletable(uri) …)`. Definition L370–372 → 2-arg overload. Caveat: the watch-dir handler's own caller was not printed. |
| 23 | `TorrentEngine.addTorrentCompletable (Uri, Uri)Completable` | REACHABLE | SOURCE | Called by row 21's method, L364. Definition L374–395; its runnable calls row 24's method at L389. |
| 24 | `TorrentEngine.addTorrentSync (Uri, TorrentMetaInfo, Uri)Torrent` | REACHABLE | SOURCE | Called by row 23's method, L389: `addTorrentSync(file, info, savePath);` Definition L1177–1205; builds an `AddTorrentParams` (L1187) and calls row 25's method at L1204. |
| 25 | `TorrentEngine.addTorrentSync (AddTorrentParams, boolean)Torrent` | REACHABLE | SOURCE | Called by `addTorrent(AddTorrentParams, boolean)` L333 and by row 24's method L1204. Definition L401–413 → `session.addTorrent(params, removeFile)`. |
| 26 | `TorrentEngine.addTorrents (List, boolean)V` | OPEN | — | Definition printed (L342–357). No printed caller in this pass (no internal caller; external UI/service caller not printed). Missing evidence: full-repo grep for `addTorrents(` call sites. |
| 27 | `TorrentEngine.addTrackers (String, List)V` | OPEN | — | Definition printed (L568–575). No printed caller. Missing evidence: full-repo grep for `addTrackers(` call sites (detail-torrent / viewmodel layer). |
| 28 | `TorrentEngine.cancelFetchMagnet (String)V` | OPEN | — | Definition printed (L481–486). No printed caller. Missing evidence: full-repo grep for `cancelFetchMagnet(` call sites. |
| 29 | `TorrentEngine.checkPauseTorrents ()Z` | REACHABLE | SOURCE | Internal callers: `rescheduleTorrents` L320, `onTorrentAdded` L1277, `onTorrentLoaded` L1292, and a further engine-listener site L1442. Definition L1023–1044. |
| 30 | `TorrentEngine.cleanTemp ()V` | REACHABLE | SOURCE | Called by `doStop` L300. Definition L1223–1230. |
| 31 | `TorrentEngine.createFetchMagnetSingle (String)Single` | OPEN | — | Definition printed (L431–459), but its only printed caller is row 36 `fetchMagnet` (L422), which is itself OPEN — so this row inherits OPEN. Missing evidence: a printed caller of `fetchMagnet` (see row 36). |
| 32 | `TorrentEngine.deleteTorrents (List, boolean)V` | OPEN | — | Definition printed (L533–541). No printed caller. Missing evidence: full-repo grep for `deleteTorrents(` call sites. |
| 33 | `TorrentEngine.deleteTrackers (String, List)V` | OPEN | — | Definition printed (L543–555). No printed caller. Missing evidence: full-repo grep for `deleteTrackers(` call sites. |
| 34 | `TorrentEngine.doStart ()V` | REACHABLE | SOURCE | `TorrentService.init()` L131: `engine.doStart();` Definition L234–260. |
| 35 | `TorrentEngine.doStop ()V` | REACHABLE | SOURCE | `TorrentService.stopEngine()` L161: `engine.doStop();` Definition L292–301. |
| 36 | `TorrentEngine.fetchMagnet (String)Pair` | OPEN | — | Definition printed (L415–425). No printed caller in this pass (no internal caller; the magnet/add-link UI caller was not printed). Missing evidence: full-repo grep for `fetchMagnet(` call sites. |
| 37 | `TorrentEngine.forceAnnounceTorrents (List)V` | OPEN | — | Definition printed (L520–531). No printed caller. Missing evidence: full-repo grep for `forceAnnounceTorrents(` call sites. |
| 38 | `TorrentEngine.forceRecheckTorrents (List)V` | OPEN | — | Definition printed (L507–518). No printed caller. Missing evidence: full-repo grep for `forceRecheckTorrents(` call sites. |
| 39 | `TorrentEngine.forceStop ()V` | REACHABLE | SOURCE | Internal callers: `handleAutoStop` L145 (reached from the `doStart` subscription, L245) and `requestStop` L279. Definition L282–286 (sends `ACTION_SHUTDOWN` to `TorrentService`). |
| 40 | `TorrentEngine.getBencode (String)byte[]` | REACHABLE | SOURCE for the call; INFERRED for the listener-dispatch step | Called by `saveTorrentFile` L974, which is called by `saveTorrentFileIn` L965, called from engine-listener callbacks (`onTorrentAdded` L1273–1275 and a further site L1431). Definition L927–936. |

## Totals

- REACHABLE proposed: **28**
  (AddTorrentParams 1, DownloadsCompletedListener 9, SessionErrorFilter 3,
  TorrentEngine 15)
- UNREACHABLE proposed: **0** (no UNREACHABLE verdict is claimed; none of the
  40 meets the bar of exactly one kind / reason / source reference)
- OPEN: **12**
  (AddTorrentParams: `writeToParcel`, `$1.createFromParcel`, `$1.newArray`;
  TorrentEngine: `addTorrents`, `addTrackers`, `cancelFetchMagnet`,
  `createFetchMagnetSingle`, `deleteTorrents`, `deleteTrackers`,
  `fetchMagnet`, `forceAnnounceTorrents`, `forceRecheckTorrents`)

## What would resolve the 12 OPEN rows

- **AddTorrentParams parcel trio:** a printed Intent-extra / Bundle
  `putParcelable` site passing an `AddTorrentParams`, or a printed
  `getParcelableExtra` / `getParcelable` read site. Full-repo grep targets:
  `AddTorrentParams` in `putExtra`, `putParcelable`, `getParcelableExtra`.
- **TorrentEngine public APIs (8 + 1 dependent):** one printed caller file
  per method (likely UI / viewmodel / service layer), or a full-repo grep
  saved as printed output for: `addTorrents(`, `addTrackers(`,
  `cancelFetchMagnet(`, `deleteTorrents(`, `deleteTrackers(`,
  `fetchMagnet(`, `forceAnnounceTorrents(`, `forceRecheckTorrents(`.
  Resolving `fetchMagnet` also resolves `createFetchMagnetSingle`.
- **Strict-entry closure for the whole batch:** a printed
  launcher/service-start step for `TorrentService` (who starts it, and the
  `onStartCommand` → `init()` step).

## Method note

- Plan `TODO_CANDIDATE_REACHABLE` labels were treated as candidates only.
- Connector `search_code` returned 0 / incomplete for this repository and
  was ignored (not treated as evidence of absence).
- No verdict was changed without printed lines; every REACHABLE row cites
  printed lines from the files listed above.
- `confirmed_by` is SOURCE or INFERRED only; no DYN / FW-MEMORY /
  UNVERIFIED confirmation labels are used.
