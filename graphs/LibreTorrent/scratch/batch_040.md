# LibreTorrent batch 40 source audit

Membership is the exact 40-row set in `scratch/batch_040_plan.txt`. I checked the helper's TorrentSessionImpl bodies, TorrentEngine wrappers, TorrentService lifecycle/task context and caller search in `scratch/batch_040_helper_printed.txt`. Local chains exist, but complete app-entry routes with hand-authored edges and superclass/libtorrent callback dispatch are not verified end to end. No absence of a grep match is used as proof of unreachability.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentSessionImpl.loadSettings()` | OPEN | Called by start; service-to-session entry chain unresolved. |
| 2 | `TorrentSessionImpl.mergeTorrent(String,AddTorrentParams,byte[])` | OPEN | Local add/merge flow; entry chain unresolved. |
| 3 | `TorrentSessionImpl.mergeTrackersAndSeeds(String,AddTorrentParams,byte[])` | OPEN | Internal caller; add-torrent route unresolved. |
| 4 | `TorrentSessionImpl.newTask(TorrentHandle,String)` | OPEN | Session listener path; libtorrent callback delivery unresolved. |
| 5 | `TorrentSessionImpl.notifyListeners(CallListener)` | OPEN | Local call sites exist; routes to each caller unverified. |
| 6 | `TorrentSessionImpl.onAfterStart()` | OPEN | Superclass lifecycle hook; invocation unresolved. |
| 7 | `TorrentSessionImpl.onAfterStop()` | OPEN | Superclass lifecycle hook; invocation unresolved. |
| 8 | `TorrentSessionImpl.onApplySettings(SettingsPack)` | OPEN | Override; superclass/library caller unresolved. |
| 9 | `TorrentSessionImpl.onBeforeStart()` | OPEN | Superclass lifecycle hook; invocation unresolved. |
| 10 | `TorrentSessionImpl.onBeforeStop()` | OPEN | Superclass lifecycle hook; invocation unresolved. |
| 11 | `TorrentSessionImpl.operationNotAllowed()` | OPEN | In-class callers; public caller routes unresolved. |
| 12 | `TorrentSessionImpl.parseMagnet(String)` | OPEN | Engine call sites exist; full app-entry chain unresolved. |
| 13 | `TorrentSessionImpl.parseMagnetUri(String)` | OPEN | Internal callers; complete operation-entry route unresolved. |
| 14 | `TorrentSessionImpl.pauseAll()` | OPEN | Engine wrapper; full UI/service action route unresolved. |
| 15 | `TorrentSessionImpl.pauseAllManually()` | OPEN | Engine wrapper; full UI/service action route unresolved. |
| 16 | `TorrentSessionImpl.removeListener(TorrentEngineListener)` | OPEN | Lifecycle callers; entry/lifecycle dispatch unresolved. |
| 17 | `TorrentSessionImpl.removeLoadedMagnet(String)` | OPEN | Local callers; add/cancel route unresolved. |
| 18 | `TorrentSessionImpl.requestStop()` | OPEN | Engine/service callers; stop-event entry unresolved. |
| 19 | `TorrentSessionImpl.restoreDownload(String)` | OPEN | Queued restore caller; startup/restore route unresolved. |
| 20 | `TorrentSessionImpl.restoreTorrents()` | OPEN | Engine/service callers; startup route unresolved. |
| 21 | `TorrentSessionImpl.resumeAll()` | OPEN | Engine wrapper; UI/service action route unresolved. |
| 22 | `TorrentSessionImpl.resumeAllManually()` | OPEN | Engine wrapper; UI/service action route unresolved. |
| 23 | `TorrentSessionImpl.runNextLoadTorrentTask()` | OPEN | Queue callers; restore/start route unresolved. |
| 24 | `TorrentSessionImpl.saveAllResumeData()` | OPEN | Stop caller; lifecycle route unresolved. |
| 25 | `TorrentSessionImpl.saveSettings()` | OPEN | Internal callers; settings/lifecycle route unresolved. |
| 26 | `TorrentSessionImpl.setAutoManaged(boolean)` | OPEN | Engine wrapper; user-action route unresolved. |
| 27 | `TorrentSessionImpl.setDefaultTrackersList(String[])` | OPEN | Callers shown; settings-entry route unresolved. |
| 28 | `TorrentSessionImpl.setMaxConnectionsPerTorrent(int)` | OPEN | Engine wrapper; settings-action route unresolved. |
| 29 | `TorrentSessionImpl.setMaxUploadsPerTorrent(int)` | OPEN | Engine wrapper; settings-action route unresolved. |
| 30 | `TorrentSessionImpl.setRandomPort(SessionSettings)` | OPEN | Settings helper callers; session-settings entry unresolved. |
| 31 | `TorrentSessionImpl.setSettings(SessionSettings)` | OPEN | Overload delegates locally; settings-action route unresolved. |
| 32 | `TorrentSessionImpl.setSettings(SessionSettings,boolean)` | OPEN | Engine/session callers; settings-action route unresolved. |
| 33 | `TorrentSessionImpl.settingsToSettingsPack(SessionSettings,SettingsPack)` | OPEN | Internal settings callers; initialization/settings route unresolved. |
| 34 | `TorrentSessionImpl.start()` | OPEN | Service/lifecycle context exists; superclass/library start chain unresolved. |
| 35 | `TorrentSessionImpl.stopTasks()` | OPEN | Called by requestStop; stop-entry route unresolved. |
| 36 | `TorrentSessionImpl$1.<init>(TorrentSessionImpl)` | OPEN | Anonymous listener in restore/start path; outer route unresolved. |
| 37 | `TorrentSessionImpl$1.onTorrentRemoved(String)` | OPEN | Callback; registration/delivery path unresolved. |
| 38 | `TorrentSessionImpl$InnerListener.<init>(TorrentSessionImpl)` | OPEN | Listener registration printed; startup and libtorrent dispatch unresolved. |
| 39 | `TorrentSessionImpl$InnerListener.alert(Alert)` | OPEN | Callback switch printed; libtorrent alert delivery unresolved. |
| 40 | `TorrentSessionImpl$InnerListener.lambda$alert$0(String,TorrentEngineListener)` | OPEN | Alert callback lambda; listener delivery route unresolved. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
