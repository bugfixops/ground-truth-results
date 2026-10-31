# LibreTorrent batch 34 source audit

Membership is the 40-row set in `scratch/batch_034_plan.txt`. I independently reviewed the target source and caller excerpts in `scratch/batch_034_helper_printed.txt`. Several rows have local callers; the audit did not establish app-entry-to-method routes with all callback and library-dispatch steps represented by hand-authored edges. Missing call sites alone are not treated as proof of unreachability.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `FileTree.setType(int)` | OPEN | Body printed; complete entry route not verified. |
| 2 | `FileTree.size()` | OPEN | Recursive tree method; complete entry route not verified. |
| 3 | `FileTree.toString()` | OPEN | Definition printed; candidate indirect use lacks full route. |
| 4 | `TorrentContentFileTree.<init>(int,String,long,int,TorrentContentFileTree)` | OPEN | Construction sites printed; full UI entry route not verified. |
| 5 | `TorrentContentFileTree.<init>(String,long,int)` | OPEN | Construction sites printed; full UI entry route not verified. |
| 6 | `TorrentContentFileTree.<init>(String,long,int,TorrentContentFileTree)` | OPEN | Construction sites printed; full UI entry route not verified. |
| 7 | `TorrentContentFileTree.changePriority(FilePriority,boolean,boolean)` | OPEN | Method/local callers printed; UI-to-entry route not verified. |
| 8 | `TorrentContentFileTree.getAvailability()` | OPEN | Candidate UI caller printed; full entry route not verified. |
| 9 | `TorrentContentFileTree.getFilePriority()` | OPEN | Candidate UI callers printed; full entry route not verified. |
| 10 | `TorrentContentFileTree.getReceivedBytes()` | OPEN | Candidate UI caller printed; full entry route not verified. |
| 11 | `TorrentContentFileTree.nonIgnoreFileSize()` | OPEN | Method/caller evidence printed; full route not verified. |
| 12 | `TorrentContentFileTree.onChangePriority(FilePriority,boolean)` | OPEN | Local invocation printed; full route not verified. |
| 13 | `TorrentContentFileTree.setAvailability(double)` | OPEN | Setter printed; no complete route verified. |
| 14 | `TorrentContentFileTree.setPriority(FilePriority,boolean)` | OPEN | Setter/local callers printed; full route not verified. |
| 15 | `TorrentContentFileTree.setReceivedBytes(long)` | OPEN | Setter printed; no complete route verified. |
| 16 | `TorrentContentFileTree.toString()` | OPEN | Method printed; no complete route verified. |
| 17 | `AdvancedPeerInfo.<init>(peer_info)` | OPEN | Constructed in TorrentDownloadImpl; native/library upstream route unresolved. |
| 18 | `AdvancedPeerInfo.isUtp()` | OPEN | No app caller in saved search; absence is not proof of no route. |
| 19 | `AdvancedPeerInfo.pieces()` | OPEN | No app caller in saved search; absence is not proof of no route. |
| 20 | `AdvancedPeerInfo.port()` | OPEN | No app caller in saved search; absence is not proof of no route. |
| 21 | `IPFilterImpl.<init>()` | OPEN | Session construction/bridge printed; startup route not verified. |
| 22 | `IPFilterImpl.addRange(String,String)` | OPEN | Parser/bridge dispatch route not verified. |
| 23 | `IPFilterImpl.getFilter()` | OPEN | Parser/bridge dispatch route not verified. |
| 24 | `IPFilterParser.<clinit>()` | OPEN | Parser invocation depends on unresolved session/configuration path. |
| 25 | `IPFilterParser.<init>()` | OPEN | TorrentSessionImpl call site printed; full entry route not verified. |
| 26 | `IPFilterParser.errLog(int,String,String)` | OPEN | Parser error path depends on unresolved parser invocation. |
| 27 | `IPFilterParser.parseDAT(InputStream,IPFilter)` | OPEN | No complete source-to-input entry route established. |
| 28 | `IPFilterParser.parseFile(Uri,FileSystemFacade,IPFilter)` | OPEN | Session caller printed; full startup/configuration path not verified. |
| 29 | `IPFilterParser.parseIpAddress(String)` | OPEN | Parser helper; complete parser entry route not verified. |
| 30 | `IPFilterParser.parseP2P(InputStream,IPFilter)` | OPEN | No complete source-to-input route established. |
| 31 | `PriorityConverter.<clinit>()` | OPEN | Static initializer/call sites printed; entry routes not verified. |
| 32 | `PriorityConverter.convert(Priority)#2` | OPEN | Overload/call sites printed; entry routes not verified. |
| 33 | `PriorityConverter.convert(Priority[])` | OPEN | Overload/call sites printed; entry routes not verified. |
| 34 | `PriorityConverter.convert(Priority[])#2` | OPEN | Overload/call sites printed; entry routes not verified. |
| 35 | `SessionErrors.<clinit>()` | OPEN | Error-helper calls printed; event delivery path not verified. |
| 36 | `SessionErrors.getErrorMsg(ErrorCode)` | OPEN | TorrentDownloadImpl caller printed; callback/event entry unresolved. |
| 37 | `SessionErrors.isNonCritical(ErrorCode)` | OPEN | TorrentDownloadImpl caller printed; callback/event entry unresolved. |
| 38 | `SessionErrors$Error.<init>(int,String)` | OPEN | Construction evidence printed; complete route not verified. |
| 39 | `SessionLogger.<clinit>()` | OPEN | Full session construction route not verified. |
| 40 | `SessionLogger.<init>()` | OPEN | TorrentSessionImpl constructor site printed; full app entry route not verified. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
