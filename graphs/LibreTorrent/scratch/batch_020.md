# Batch 20 source audit

Membership is the 40 rows in `batch_020_plan.txt`; caller excerpts are in `batch_020_helper_printed.txt`, with independent LogEntry hashCode evidence in `batch_020_independent_printed.txt`.

The helper supports local callers for 39 methods. I kept those OPEN until their complete entry routes are handwritten in graph_def.py. `LogEntry.hashCode` has no app caller and is labeled UNREACHABLE `no_trigger_in_app`.

| Method | Label | Evidence / reason |
|---|---|---|
| `FetchLinkException.<init>(String)` | OPEN | Utils throw sites exist; complete app entry route not handwritten. `Utils.java:466-468,492-494`; exception constructor `30-33`. |
| `FreeSpaceException.<init>()` | OPEN | App throw sites exist; complete routes not handwritten. `AddTorrentViewModel.java:486-497`; `TorrentEngine.java:1200-1204`. |
| `FreeSpaceException.<init>(String)` | OPEN | App throw site exists; complete route not handwritten. `TorrentDownloadImpl.java:415-423`. |
| `IPFilterException.<init>(String)` | OPEN | Parser/configuration path exists; complete route not handwritten. `IPFilterImpl.java:39-62`; `TorrentSessionImpl.java:726-740`; `IPFilterParser.java:162-169,240-246`. |
| `NoFilesSelectedException.<init>()` | OPEN | App throw site exists; complete route not handwritten. `AddTorrentViewModel.java:486-497`. |
| `NormalizeUrlException.<init>(String,Exception)` | OPEN | Wrapping source path exists; complete UI route not handwritten. `NormalizeUrl.java:178-188`; UI callers in helper source print. |
| `TorrentAlreadyExistsException.<init>()` | OPEN | Session throw site exists; complete session route not handwritten. `TorrentSessionImpl.java:280-285`. |
| `UnknownUriException.<init>` | OPEN | Resolver throw site exists; complete caller route not handwritten. `FsModuleResolverImpl.java:42-49`. |
| `TorrentFilterCollection.all` | OPEN | MainViewModel/activity call sites exist; full UI entry path not handwritten. `TorrentFilterCollection.java:27-29`; caller source in helper print. |
| `TorrentFilterCollection.dateAddedMonth` | OPEN | Drawer and filter call sites exist; full UI route not handwritten. `TorrentFilterCollection.java:77-85`; helper print. |
| `TorrentFilterCollection.dateAddedToday` | OPEN | Drawer and filter call sites exist; full UI route not handwritten. `TorrentFilterCollection.java:47-55`; helper print. |
| `TorrentFilterCollection.dateAddedWeek` | OPEN | Drawer and filter call sites exist; full UI route not handwritten. `TorrentFilterCollection.java:67-75`; helper print. |
| `TorrentFilterCollection.dateAddedYear` | OPEN | Drawer and filter call sites exist; full UI route not handwritten. `TorrentFilterCollection.java:87-95`; helper print. |
| `TorrentFilterCollection.dateAddedYesterday` | OPEN | Drawer and filter call sites exist; full UI route not handwritten. `TorrentFilterCollection.java:57-65`; helper print. |
| `TorrentFilterCollection.lambda$all$0` | OPEN | Predicate is evaluated in main list filtering; full UI route not handwritten. `TorrentFilterCollection.java:27-29`; `MainViewModel.java:118-122`. |
| `TorrentFilterCollection.lambda$dateAddedMonth$8` | OPEN | Predicate is evaluated in main list filtering; full UI route not handwritten. `TorrentFilterCollection.java:77-85`; `MainViewModel.java:118-122`. |
| `TorrentFilterCollection.lambda$dateAddedToday$5` | OPEN | Predicate is evaluated in main list filtering; full UI route not handwritten. `TorrentFilterCollection.java:47-55`; `MainViewModel.java:118-122`. |
| `TorrentFilterCollection.lambda$dateAddedWeek$7` | OPEN | Predicate is evaluated in main list filtering; full UI route not handwritten. `TorrentFilterCollection.java:67-75`; `MainViewModel.java:118-122`. |
| `TorrentFilterCollection.lambda$dateAddedYear$9` | OPEN | Predicate is evaluated in main list filtering; full UI route not handwritten. `TorrentFilterCollection.java:87-95`; `MainViewModel.java:118-122`. |
| `TorrentFilterCollection.lambda$dateAddedYesterday$6` | OPEN | Predicate is evaluated in main list filtering; full UI route not handwritten. `TorrentFilterCollection.java:57-65`; `MainViewModel.java:118-122`. |
| `TorrentFilterCollection.lambda$noTags$11` | OPEN | MainActivity installs it and ViewModel tests it; full UI route not handwritten. `TorrentFilterCollection.java:101-103`; `MainActivity.java:295-307`. |
| `TorrentFilterCollection.lambda$statusDownloaded$2` | OPEN | Status filter is installed and evaluated; full UI route not handwritten. `TorrentFilterCollection.java:35-37`; helper print. |
| `TorrentFilterCollection.lambda$statusDownloading$1` | OPEN | Status filter is installed and evaluated; full UI route not handwritten. `TorrentFilterCollection.java:31-33`; helper print. |
| `TorrentFilterCollection.lambda$statusDownloadingMetadata$3` | OPEN | Status filter is installed and evaluated; full UI route not handwritten. `TorrentFilterCollection.java:39-41`; helper print. |
| `TorrentFilterCollection.lambda$statusError$4` | OPEN | Status filter is installed and evaluated; full UI route not handwritten. `TorrentFilterCollection.java:43-45`; helper print. |
| `TorrentFilterCollection.lambda$tag$10` | OPEN | MainActivity installs it and ViewModel evaluates it; full UI route not handwritten. `TorrentFilterCollection.java:97-99`; helper print. |
| `TorrentFilterCollection.noTags` | OPEN | MainActivity calls it; full UI route not handwritten. `TorrentFilterCollection.java:101-103`; `MainActivity.java:295-307`. |
| `TorrentFilterCollection.statusDownloaded` | OPEN | Utils/activity map to it; full UI route not handwritten. `TorrentFilterCollection.java:35-37`; helper print. |
| `TorrentFilterCollection.statusDownloading` | OPEN | Utils/activity map to it; full UI route not handwritten. `TorrentFilterCollection.java:31-33`; helper print. |
| `TorrentFilterCollection.statusDownloadingMetadata` | OPEN | Utils/activity map to it; full UI route not handwritten. `TorrentFilterCollection.java:39-41`; helper print. |
| `TorrentFilterCollection.statusError` | OPEN | Utils/activity map to it; full UI route not handwritten. `TorrentFilterCollection.java:43-45`; helper print. |
| `TorrentFilterCollection.tag(TagInfo)` | OPEN | MainActivity calls it; full UI route not handwritten. `TorrentFilterCollection.java:97-99`; helper print. |
| `LogEntry.<init>` | OPEN | SessionLogger constructs entries; complete logger entry route not handwritten. `SessionLogger.java:117-162`. |
| `LogEntry.equals` | OPEN | DiffUtil call exists; full UI entry route not handwritten. `LogAdapter.java:67-74`; `LogEntry.java:76-90`. |
| `LogEntry.getId` | OPEN | LogAdapter calls it; full UI entry route not handwritten. `LogAdapter.java:77-81`; `LogEntry.java:49-52`. |
| `LogEntry.getMsg` | OPEN | LogAdapter binds it; full UI route not handwritten. `LogAdapter.java:100-110`; `LogEntry.java:60-64`. |
| `LogEntry.getTag` | OPEN | LogAdapter binds it; full UI route not handwritten. `LogAdapter.java:100-110`; `LogEntry.java:54-58`. |
| `LogEntry.getTimeStampAsString` | OPEN | LogAdapter and export paths call it; complete routes not handwritten. `LogEntry.java:71-74,103-106`; `Logger.java:435-438`. |
| `LogEntry.hashCode` | UNREACHABLE | no_trigger_in_app; no hash-key/callsite in app log path. `LogEntry.java:92-101`; `LogAdapter.java:67-81`; `batch_020_independent_printed.txt`. |
| `LogEntry.toString` | OPEN | Logger export invokes it; complete logging route not handwritten. `LogEntry.java:103-113`; `Logger.java:425-442`. |

Count: 40 plan rows; 0 REACHABLE; 1 `UNREACHABLE/no_trigger_in_app`; 39 OPEN. No coverage evidence was used.
