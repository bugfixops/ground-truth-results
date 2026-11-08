# LibreTorrent batch 38 source audit

Membership is the exact 40-row set in `scratch/batch_038_plan.txt`. I checked source bodies, local callers, session/engine wrappers and listener registration in `scratch/batch_038_helper_printed.txt`. Local calls and listener registration are visible, but complete app-entry routes are not represented by hand-authored edges; libtorrent callbacks add an unresolved dispatch step. All rows remain OPEN.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentDownloadImpl.setMaxUploads(int)` | OPEN | Session wrapper caller; full app-to-session route unresolved. |
| 2 | `TorrentDownloadImpl.setSequentialDownload(boolean)` | OPEN | Session download caller; full entry route unresolved. |
| 3 | `TorrentDownloadImpl.setTorrentName(String)` | OPEN | Definition printed; complete route unresolved. |
| 4 | `TorrentDownloadImpl.setUploadSpeedLimit(int)` | OPEN | Session wrapper caller; full route unresolved. |
| 5 | `TorrentDownloadImpl.stateToStateCode(TorrentStatus.State)` | OPEN | Internal callers shown; their caller routes unresolved. |
| 6 | `TorrentDownloadImpl.torrentRemoved()` | OPEN | Inner alert handling shown; callback delivery unresolved. |
| 7 | `TorrentDownloadImpl$1.<init>(TorrentDownloadImpl,AtomicReference,CountDownLatch)` | OPEN | Listener construction/registration shown; caller route unresolved. |
| 8 | `TorrentDownloadImpl$1.alert(Alert)` | OPEN | Alert callback body shown; libtorrent dispatch unresolved. |
| 9 | `TorrentDownloadImpl$1.types()` | OPEN | Callback body shown; library invocation unresolved. |
| 10 | `TorrentDownloadImpl$InnerListener.<init>(TorrentDownloadImpl)` | OPEN | Constructed in TorrentDownloadImpl; containing-object entry route unresolved. |
| 11 | `TorrentDownloadImpl$InnerListener.alert(Alert)` | OPEN | Listener registered; native/library dispatch unresolved. |
| 12 | `TorrentDownloadImpl$InnerListener.lambda$alert$0(StateChangedAlert,TorrentEngineListener)` | OPEN | Lambda executes within listener alert switch; callback dispatch unresolved. |
| 13 | `TorrentDownloadImpl$InnerListener.lambda$alert$1(TorrentEngineListener)` | OPEN | Lambda executes within listener alert switch; callback dispatch unresolved. |
| 14 | `TorrentDownloadImpl$InnerListener.lambda$alert$2(TorrentEngineListener)` | OPEN | Lambda executes within listener alert switch; callback dispatch unresolved. |
| 15 | `TorrentDownloadImpl$InnerListener.lambda$alert$3(int,TorrentEngineListener)` | OPEN | Lambda executes within listener alert switch; callback dispatch unresolved. |
| 16 | `TorrentDownloadImpl$InnerListener.types()` | OPEN | Registration shown; libtorrent callback delivery unresolved. |
| 17 | `TorrentSessionImpl.<clinit>()` | OPEN | Static setup printed; app-entry initialization route not traced. |
| 18 | `TorrentSessionImpl.<init>(TorrentRepository,FileSystemFacade,SystemFacade)` | OPEN | Constructor printed; complete app construction route unresolved. |
| 19 | `TorrentSessionImpl.addDefaultTrackers(add_torrent_params)` | OPEN | Called by download path; full download entry route unresolved. |
| 20 | `TorrentSessionImpl.addListener(TorrentEngineListener)` | OPEN | Registration callers shown; full session startup route unresolved. |
| 21 | `TorrentSessionImpl.addTorrent(AddTorrentParams,boolean)` | OPEN | Engine caller shown; app entry route unresolved. |
| 22 | `TorrentSessionImpl.applyMaxStoredLogs(SessionSettings)` | OPEN | Settings caller shown; complete session-settings route unresolved. |
| 23 | `TorrentSessionImpl.applyProxy(SessionSettings,SettingsPack)` | OPEN | Settings-pack caller shown; route unresolved. |
| 24 | `TorrentSessionImpl.applySessionLoggerFilters(SessionSettings)` | OPEN | Settings caller shown; route unresolved. |
| 25 | `TorrentSessionImpl.applySettings(SessionSettings,boolean)` | OPEN | Session callers shown; end-to-end settings route unresolved. |
| 26 | `TorrentSessionImpl.applySettingsPack(SettingsPack)` | OPEN | Callers shown; session startup route unresolved. |
| 27 | `TorrentSessionImpl.cancelFetchMagnet(String)` | OPEN | Download/delete callers shown; entry paths unresolved. |
| 28 | `TorrentSessionImpl.checkError(Alert)` | OPEN | Inner listener dispatch shown; native callback delivery unresolved. |
| 29 | `TorrentSessionImpl.checkStop()` | OPEN | Callers shown; stop/session callback route unresolved. |
| 30 | `TorrentSessionImpl.convertEncryptMode(EncryptMode)` | OPEN | Settings-pack caller shown; settings entry route unresolved. |
| 31 | `TorrentSessionImpl.convertProxyType(ProxyType,boolean)` | OPEN | Settings-pack caller shown; settings entry route unresolved. |
| 32 | `TorrentSessionImpl.defaultSettingsPack()` | OPEN | Callers shown; session initialization route unresolved. |
| 33 | `TorrentSessionImpl.deleteTorrent(String,boolean)` | OPEN | Engine callers shown; full app action route unresolved. |
| 34 | `TorrentSessionImpl.dhtBootstrapNodes()` | OPEN | Settings-pack caller shown; session startup route unresolved. |
| 35 | `TorrentSessionImpl.dhtNodes()` | OPEN | Stats caller shown; stats request route unresolved. |
| 36 | `TorrentSessionImpl.disableIpFilter()` | OPEN | Engine/settings callers shown; settings route unresolved. |
| 37 | `TorrentSessionImpl.download(String,File,boolean,boolean)` | OPEN | Internal overload callers shown; app-to-session route unresolved. |
| 38 | `TorrentSessionImpl.download(String,AddTorrentParams,byte[])` | OPEN | Caller shown; complete add-torrent route unresolved. |
| 39 | `TorrentSessionImpl.download(TorrentInfo,File,Priority[],boolean,boolean,List)` | OPEN | Callers shown; complete add-torrent route unresolved. |
| 40 | `TorrentSessionImpl.download(byte[],File,Priority[],boolean,boolean,List)` | OPEN | Callers shown; complete add-torrent route unresolved. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
