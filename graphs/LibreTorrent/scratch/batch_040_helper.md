# LibreTorrent batch 40 source audit

Membership is exactly the 40 batch 40 plan rows printed at the top of `batch_040_helper_printed.txt`. The saved evidence includes the relevant `TorrentSessionImpl` bodies, `TorrentEngine` wrappers, `TorrentService` lifecycle/task context, and a source-root caller search. I retain OPEN for all rows because this audit has not verified every entry-to-method link; local call chains and superclass/session callbacks alone are not a complete hand-authored route. No missing grep result is treated as proof of unreachability.

| # | Method | Finding | Printed source and unresolved route step |
|---:|---|---|---|
| 1 | `TorrentSessionImpl.loadSettings()SessionParams` | OPEN | `TorrentSessionImpl.java:1192+`; called by `start`, but complete service/start entry chain not verified. |
| 2 | `TorrentSessionImpl.mergeTorrent(String,AddTorrentParams,byte[])V` | OPEN | `TorrentSessionImpl.java:537+`; reached locally during add/merge flow; full entry chain unresolved. |
| 3 | `TorrentSessionImpl.mergeTrackersAndSeeds(String,AddTorrentParams,byte[])V` | OPEN | `TorrentSessionImpl.java:556,570+`; internal caller shown, upstream add-torrent route unresolved. |
| 4 | `TorrentSessionImpl.newTask(TorrentHandle,String)TorrentDownload` | OPEN | `TorrentSessionImpl.java:1430+`; session listener path shown, libtorrent callback delivery unresolved. |
| 5 | `TorrentSessionImpl.notifyListeners(CallListener)V` | OPEN | `TorrentSessionImpl.java:1445+`; many local call sites shown, routes to each caller not verified. |
| 6 | `TorrentSessionImpl.onAfterStart()V` | OPEN | `TorrentSessionImpl.java:991+`; superclass lifecycle hook body printed, framework/library invocation unresolved. |
| 7 | `TorrentSessionImpl.onAfterStop()V` | OPEN | `TorrentSessionImpl.java:1041+`; superclass lifecycle hook body printed, framework/library invocation unresolved. |
| 8 | `TorrentSessionImpl.onApplySettings(SettingsPack)V` | OPEN | `TorrentSessionImpl.java:1048+`; override body printed, caller in superclass/library unresolved. |
| 9 | `TorrentSessionImpl.onBeforeStart()V` | OPEN | `TorrentSessionImpl.java:984+`; superclass lifecycle hook body printed, invocation unresolved. |
| 10 | `TorrentSessionImpl.onBeforeStop()V` | OPEN | `TorrentSessionImpl.java:1028+`; superclass lifecycle hook body printed, invocation unresolved. |
| 11 | `TorrentSessionImpl.operationNotAllowed()Z` | OPEN | `TorrentSessionImpl.java:245+`; called throughout the class; route to public callers unresolved. |
| 12 | `TorrentSessionImpl.parseMagnet(String)MagnetInfo` | OPEN | `TorrentSessionImpl.java:444+`; public parser and engine call sites printed, complete app entry chain unresolved. |
| 13 | `TorrentSessionImpl.parseMagnetUri(String)AddTorrentParams` | OPEN | `TorrentSessionImpl.java:514+`; internal callers printed; complete operation entry route unresolved. |
| 14 | `TorrentSessionImpl.pauseAll()V` | OPEN | `TorrentSessionImpl.java:756+`; engine wrapper and body printed, complete UI/service action route unresolved. |
| 15 | `TorrentSessionImpl.pauseAllManually()V` | OPEN | `TorrentSessionImpl.java:782+`; engine wrapper and body printed, complete UI/service action route unresolved. |
| 16 | `TorrentSessionImpl.removeListener(TorrentEngineListener)V` | OPEN | `TorrentSessionImpl.java:191+`; internal lifecycle callers printed; entry/lifecycle dispatch not verified. |
| 17 | `TorrentSessionImpl.removeLoadedMagnet(String)V` | OPEN | `TorrentSessionImpl.java:240+`; local callers printed; complete add/cancel route unresolved. |
| 18 | `TorrentSessionImpl.requestStop()V` | OPEN | `TorrentSessionImpl.java:911+`; engine/service callers printed, complete stop-event entry path unresolved. |
| 19 | `TorrentSessionImpl.restoreDownload(String)V` | OPEN | `TorrentSessionImpl.java:1681+`; queued restore caller printed; complete startup/restore route unresolved. |
| 20 | `TorrentSessionImpl.restoreTorrents()V` | OPEN | `TorrentSessionImpl.java:396+`; engine/service callers printed, complete startup route unresolved. |
| 21 | `TorrentSessionImpl.resumeAll()V` | OPEN | `TorrentSessionImpl.java:769+`; engine wrapper and body printed, complete UI/service action route unresolved. |
| 22 | `TorrentSessionImpl.resumeAllManually()V` | OPEN | `TorrentSessionImpl.java:795+`; engine wrapper and body printed, complete UI/service action route unresolved. |
| 23 | `TorrentSessionImpl.runNextLoadTorrentTask()V` | OPEN | `TorrentSessionImpl.java:1453+`; queue callers printed; complete restore/start entry chain unresolved. |
| 24 | `TorrentSessionImpl.saveAllResumeData()V` | OPEN | `TorrentSessionImpl.java:950+`; stop caller printed; complete stop lifecycle route unresolved. |
| 25 | `TorrentSessionImpl.saveSettings()V` | OPEN | `TorrentSessionImpl.java:1228+`; internal callers printed; full settings/lifecycle route unresolved. |
| 26 | `TorrentSessionImpl.setAutoManaged(boolean)V` | OPEN | `TorrentSessionImpl.java:836+`; engine wrapper and body printed, complete user action route unresolved. |
| 27 | `TorrentSessionImpl.setDefaultTrackersList(String[])V` | OPEN | `TorrentSessionImpl.java:1677+`; method body and callers printed, complete settings entry route unresolved. |
| 28 | `TorrentSessionImpl.setMaxConnectionsPerTorrent(int)V` | OPEN | `TorrentSessionImpl.java:808+`; engine wrapper and body printed, complete settings action route unresolved. |
| 29 | `TorrentSessionImpl.setMaxUploadsPerTorrent(int)V` | OPEN | `TorrentSessionImpl.java:822+`; engine wrapper and body printed, complete settings action route unresolved. |
| 30 | `TorrentSessionImpl.setRandomPort(SessionSettings)V` | OPEN | `TorrentSessionImpl.java:1402+`; settings helpers call it; session settings entry route unresolved. |
| 31 | `TorrentSessionImpl.setSettings(SessionSettings)V` | OPEN | `TorrentSessionImpl.java:202+`; overload delegates locally, complete settings action route unresolved. |
| 32 | `TorrentSessionImpl.setSettings(SessionSettings,boolean)V` | OPEN | `TorrentSessionImpl.java:207+`; engine/session callers printed, complete settings action route unresolved. |
| 33 | `TorrentSessionImpl.settingsToSettingsPack(SessionSettings,SettingsPack)V` | OPEN | `TorrentSessionImpl.java:1250+`; internal settings callers printed; full initialization/settings route unresolved. |
| 34 | `TorrentSessionImpl.start()V` | OPEN | `TorrentSessionImpl.java:862+`; engine/service lifecycle context printed, superclass/library start chain unresolved. |
| 35 | `TorrentSessionImpl.stopTasks()V` | OPEN | `TorrentSessionImpl.java:920+`; `requestStop` caller printed; complete stop-entry route unresolved. |
| 36 | `TorrentSessionImpl$1.<init>(TorrentSessionImpl)V` | OPEN | Anonymous listener declaration/construction printed with session listener context; outer restore/start route unresolved. |
| 37 | `TorrentSessionImpl$1.onTorrentRemoved(String)V` | OPEN | Anonymous listener callback printed; registration and callback delivery path unresolved. |
| 38 | `TorrentSessionImpl$InnerListener.<init>(TorrentSessionImpl)V` | OPEN | Listener construction/registration printed; startup route and libtorrent dispatch unresolved. |
| 39 | `TorrentSessionImpl$InnerListener.alert(Alert)V` | OPEN | `TorrentSessionImpl.java:1061+`; callback switch printed, libtorrent alert delivery unresolved. |
| 40 | `TorrentSessionImpl$InnerListener.lambda$alert$0(String,TorrentEngineListener)V` | OPEN | Lambda in alert callback printed; callback delivery and route through the listener unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
