# LibreTorrent batch 38 source audit

Membership is the exact 40 rows for batch 38 printed at the top of `batch_038_helper_printed.txt` from the batch plan. Source bodies, local callers, session/engine wrappers, and listener registration sites are printed in the same evidence file. I leave every row OPEN: methods have local callers or implementations, but the excerpted audit does not finish entry-to-method routes from a hand-authored entry edge; listener callbacks also depend on libtorrent callback dispatch. No UNREACHABLE label is based only on lack of a call-site match.

| # | Method | Finding | Printed evidence and unresolved route step |
|---:|---|---|---|
| 1 | `TorrentDownloadImpl.setMaxUploads(int)V` | OPEN | `TorrentDownloadImpl.java:1445+`; session wrapper caller printed, full app-to-session route unresolved. |
| 2 | `TorrentDownloadImpl.setSequentialDownload(boolean)V` | OPEN | `TorrentDownloadImpl.java:1065+`; session download caller printed, full entry route unresolved. |
| 3 | `TorrentDownloadImpl.setTorrentName(String)V` | OPEN | `TorrentDownloadImpl.java:1156+`; implementation printed, complete route not established. |
| 4 | `TorrentDownloadImpl.setUploadSpeedLimit(int)V` | OPEN | `TorrentDownloadImpl.java:1324+`; session wrapper caller printed, full route unresolved. |
| 5 | `TorrentDownloadImpl.stateToStateCode(TorrentStatus.State)TorrentStateCode` | OPEN | `TorrentDownloadImpl.java:1372+`; internal callers printed, route to their callers unresolved. |
| 6 | `TorrentDownloadImpl.torrentRemoved()V` | OPEN | `TorrentDownloadImpl.java:232,456+`; inner alert handling shown, callback delivery path unresolved. |
| 7 | `TorrentDownloadImpl$1.<init>(TorrentDownloadImpl,AtomicReference,CountDownLatch)V` | OPEN | Anonymous listener construction/registration printed at `TorrentDownloadImpl.java:1656-1695`; complete caller route unresolved. |
| 8 | `TorrentDownloadImpl$1.alert(Alert)V` | OPEN | Anonymous alert callback body and registration context printed at `TorrentDownloadImpl.java:1659-1695`; libtorrent dispatch not independently established. |
| 9 | `TorrentDownloadImpl$1.types()int[]` | OPEN | Anonymous callback body printed at `TorrentDownloadImpl.java:1659-1695`; library callback invocation unresolved. |
| 10 | `TorrentDownloadImpl$InnerListener.<init>(TorrentDownloadImpl)V` | OPEN | Inner listener construction in `TorrentDownloadImpl.java:166+`; route into the containing object unresolved. |
| 11 | `TorrentDownloadImpl$InnerListener.alert(Alert)V` | OPEN | `TorrentDownloadImpl.java:205-282`; listener registration shown, native/library dispatch still unresolved. |
| 12 | `TorrentDownloadImpl$InnerListener.lambda$alert$0(StateChangedAlert,TorrentEngineListener)V` | OPEN | Lambda body is in the printed listener alert switch; dispatch requires callback execution through listener. |
| 13 | `TorrentDownloadImpl$InnerListener.lambda$alert$1(TorrentEngineListener)V` | OPEN | Lambda body is in the printed listener alert switch; dispatch requires callback execution through listener. |
| 14 | `TorrentDownloadImpl$InnerListener.lambda$alert$2(TorrentEngineListener)V` | OPEN | Lambda body is in the printed listener alert switch; dispatch requires callback execution through listener. |
| 15 | `TorrentDownloadImpl$InnerListener.lambda$alert$3(int,TorrentEngineListener)V` | OPEN | Lambda body is in the printed listener alert switch; dispatch requires callback execution through listener. |
| 16 | `TorrentDownloadImpl$InnerListener.types()int[]` | OPEN | `TorrentDownloadImpl.java:205-213`; registration shown, libtorrent callback delivery unresolved. |
| 17 | `TorrentSessionImpl.<clinit>()V` | OPEN | Static setup printed with session source; class initialization route not traced from app entry. |
| 18 | `TorrentSessionImpl.<init>(TorrentRepository,FileSystemFacade,SystemFacade)V` | OPEN | `TorrentSessionImpl.java:162+`; constructor body printed, complete application construction route unresolved. |
| 19 | `TorrentSessionImpl.addDefaultTrackers(add_torrent_params)V` | OPEN | Session helper and its download caller printed; complete download entry route unresolved. |
| 20 | `TorrentSessionImpl.addListener(TorrentEngineListener)V` | OPEN | Method body and registration callers printed; full session startup route unresolved. |
| 21 | `TorrentSessionImpl.addTorrent(AddTorrentParams,boolean)Torrent` | OPEN | Method body and engine callers printed; complete app entry route unresolved. |
| 22 | `TorrentSessionImpl.applyMaxStoredLogs(SessionSettings)V` | OPEN | Helper body and settings caller printed; session settings route unresolved. |
| 23 | `TorrentSessionImpl.applyProxy(SessionSettings,SettingsPack)V` | OPEN | Helper body and settings-pack caller printed; complete settings route unresolved. |
| 24 | `TorrentSessionImpl.applySessionLoggerFilters(SessionSettings)V` | OPEN | Helper body and settings caller printed; complete settings route unresolved. |
| 25 | `TorrentSessionImpl.applySettings(SessionSettings,boolean)V` | OPEN | Method body and session callers printed; end-to-end settings route unresolved. |
| 26 | `TorrentSessionImpl.applySettingsPack(SettingsPack)V` | OPEN | Method body and callers printed; complete session startup/settings route unresolved. |
| 27 | `TorrentSessionImpl.cancelFetchMagnet(String)V` | OPEN | Method body and download/delete callers printed; entry route to those operations unresolved. |
| 28 | `TorrentSessionImpl.checkError(Alert)V` | OPEN | `TorrentSessionImpl.java:1101+`; inner listener dispatch shown, native/library callback delivery unresolved. |
| 29 | `TorrentSessionImpl.checkStop()V` | OPEN | Method and callers printed; complete stop/session callback route unresolved. |
| 30 | `TorrentSessionImpl.convertEncryptMode(EncryptMode)int` | OPEN | Conversion body and settings-pack caller printed; complete settings route unresolved. |
| 31 | `TorrentSessionImpl.convertProxyType(ProxyType,boolean)int` | OPEN | Conversion body and settings-pack caller printed; complete settings route unresolved. |
| 32 | `TorrentSessionImpl.defaultSettingsPack()SettingsPack` | OPEN | Method body and callers printed; session initialization route unresolved. |
| 33 | `TorrentSessionImpl.deleteTorrent(String,boolean)V` | OPEN | Method body and engine callers printed; full app action route unresolved. |
| 34 | `TorrentSessionImpl.dhtBootstrapNodes()String` | OPEN | Method body and settings-pack caller printed; session startup route unresolved. |
| 35 | `TorrentSessionImpl.dhtNodes()long` | OPEN | Method body and stats caller printed; complete stats request route unresolved. |
| 36 | `TorrentSessionImpl.disableIpFilter()V` | OPEN | Method body and engine/settings callers printed; complete settings route unresolved. |
| 37 | `TorrentSessionImpl.download(String,File,boolean,boolean)V` | OPEN | Method body and internal overload callers printed; app-to-session download chain unresolved. |
| 38 | `TorrentSessionImpl.download(String,AddTorrentParams,byte[])V` | OPEN | Method body and caller printed; complete add-torrent entry route unresolved. |
| 39 | `TorrentSessionImpl.download(TorrentInfo,File,Priority[],boolean,boolean,List)V` | OPEN | Method body and callers printed; complete add-torrent entry route unresolved. |
| 40 | `TorrentSessionImpl.download(byte[],File,Priority[],boolean,boolean,List)V` | OPEN | Method body and callers printed; complete add-torrent entry route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
