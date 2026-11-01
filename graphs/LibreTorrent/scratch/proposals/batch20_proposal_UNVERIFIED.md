# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 20 — proposal, UNVERIFIED, NOT merged

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Membership: exactly 40 rows in handoff/LIBRETORRENT_BATCH_PLAN.tsv (SHA 0104806dd666c840049b3db52823d4b384fa1c92), all TODO_CANDIDATE_REACHABLE — candidates, not evidence.
Status: UNVERIFIED proposal. No build, sampler, full-repo grep, or C1 check was run for this batch, and no such count is claimed. No graph_def.py / out/ edit was made, nothing was pushed by the helper in this stage.
Rules: confirmed_by SOURCE only where lines were printed, otherwise INFERRED, never DYN / FW-MEMORY / UNVERIFIED. Tool coverage, old generated graphs, and build REACHABLE counts are never evidence. Connector search_code 0/incomplete is NOT evidence of absence and was not used.

## Counts (proposal, not verified)
- Judged: 40 / 40. REACHABLE proposed: 36. UNREACHABLE proposed: 0. OPEN: 4.
- Exceptions: 5 REACHABLE / 3 OPEN. TorrentFilterCollection: 24 / 24 REACHABLE. LogEntry: 7 REACHABLE / 1 OPEN.

## Exceptions (8)
Definitions are in core/exception/*.java (plan descriptors match the ctor signatures; file contents were not re-printed line-by-line in this stage except via throw sites below — ctor existence is taken from the plan, throw sites are printed).

| # | Method | Label | confirmed_by | Printed citations |
|---|---|---|---|---|
| 1 | FetchLinkException.<init>(String) | REACHABLE | SOURCE (previously printed) | Utils.java:467 string-ctor site, inside fetchHttpUrl() :462-475, printed in the batch 19 session (see batch19 proposal, Utils sites :467, :493, :509, :522). Route in batch 19: AddTorrentViewModel.startDecode -> TorrentDecodeTask http/https branch -> Utils.fetchHttpUrl. The :467 site is inside fetchHttpUrl; the other sites are in other Utils methods and are not needed for this verdict. Caveat: Utils.java was not re-printed in this session. |
| 2 | FreeSpaceException.<init>() | REACHABLE | SOURCE | TorrentEngine.java:1201 `throw new FreeSpaceException();` (addTorrentSync free-space check); also AddTorrentViewModel.java:496 `throw new FreeSpaceException();` in the add-torrent free-space check. |
| 3 | FreeSpaceException.<init>(String) | OPEN | — | No string-ctor throw site printed in files read this stage (TorrentEngine/AddTorrentViewModel use the no-arg ctor). Not a global-unused claim; pending full-repo grep. |
| 4 | IPFilterException.<init>(String) | REACHABLE | SOURCE | IPFilterImpl.java:44, :54, :58 `throw new IPFilterException(...)`. Caller of addRange: IPFilterParser.java:163 (parseDAT) and :241 (parseP2P) call filter.addRange(startAddr, endAddr). Caveat: the upstream caller that runs IPFilterParser itself was not printed in this stage. |
| 5 | NoFilesSelectedException.<init>() | REACHABLE | SOURCE | AddTorrentViewModel.java:493 `throw new NoFilesSelectedException();` when selectedFiles is empty in the add-torrent check. |
| 6 | NormalizeUrlException.<init>(String,Exception) | OPEN | — | No throw site printed in files read this stage. Not a global-unused claim; pending full-repo grep. |
| 7 | TorrentAlreadyExistsException.<init>() | REACHABLE | SOURCE | TorrentSessionImpl.java:282 `throw new TorrentAlreadyExistsException();`. Route: TorrentEngine.addTorrentSync :400-410 (throws declaration) -> session.addTorrent. |
| 8 | UnknownUriException.<init>(String) | OPEN | — | TorrentEngine declares it (addTorrentSync :408, saveTorrentFile :973) and catches it (:1155), but no `new UnknownUriException(String)` throw site was printed in files read this stage. Not a global-unused claim; pending full-repo grep. |

## TorrentFilterCollection (24) — all REACHABLE proposed
Definition file: core/filter/TorrentFilterCollection.java, 104 lines, printed in full. Each static method returns a lambda; TorrentFilter extends io.reactivex.functions.Predicate<TorrentInfo> (TorrentFilter.java), so lambdas run via Predicate.test(). MainViewModel.getFilter() :118-122 tests statusFilter, dateAddedFilter, searchFilter and tagFilter against each TorrentInfo — the test() dispatch itself is library/Rx dispatch, INFERRED, lambda bodies SOURCE.

Static-method callers, all printed:
- MainViewModel.java:53-55 initialises statusFilter, dateAddedFilter, tagFilter all to TorrentFilterCollection.all().
- MainActivity.java:299-306, :335, :499-521 drawer/tag clicks call setTagFilter(TorrentFilterCollection.tag(...)), setTagFilter(all()), setTagFilter(noTags()).
- MainActivity.java:590-623 drawer clicks call setStatusFilter / setDateAddedFilter with Utils.getDrawerGroupStatusFilter / getDrawerGroupDateAddedFilter results.
- Utils.java:841-851, :858-870, :879-887 getDrawerGroup* methods return, respectively: all(), statusDownloading(), statusDownloaded(), statusDownloadingMetadata(), statusError(), and all(), dateAddedToday(), dateAddedYesterday(), dateAddedWeek(), dateAddedMonth(), dateAddedYear(), all(), plus a second status group (all/statusDownloading/statusDownloaded/statusDownloadingMetadata/statusError).

Lambda mapping (compiler numbering, verified against method order in the file): all->$0, statusDownloading->$1, statusDownloaded->$2, statusDownloadingMetadata->$3, statusError->$4, dateAddedToday->$5, dateAddedYesterday->$6, dateAddedWeek->$7, dateAddedMonth->$8, dateAddedYear->$9, tag->$10, noTags->$11.

| Method | Label | Callers |
|---|---|---|
| all, lambda$all$0 | REACHABLE | MainViewModel:53-55; MainActivity:304,335,499,510; Utils:841,851,858,870,879 |
| statusDownloading, lambda$statusDownloading$1 | REACHABLE | Utils:843,881 |
| statusDownloaded, lambda$statusDownloaded$2 | REACHABLE | Utils:845,883 |
| statusDownloadingMetadata, lambda$statusDownloadingMetadata$3 | REACHABLE | Utils:847,885 |
| statusError, lambda$statusError$4 | REACHABLE | Utils:849,887 |
| dateAddedToday, lambda$dateAddedToday$5 | REACHABLE | Utils:860 |
| dateAddedYesterday, lambda$dateAddedYesterday$6 | REACHABLE | Utils:862 |
| dateAddedWeek, lambda$dateAddedWeek$7 | REACHABLE | Utils:864 |
| dateAddedMonth, lambda$dateAddedMonth$8 | REACHABLE | Utils:866 |
| dateAddedYear, lambda$dateAddedYear$9 | REACHABLE | Utils:868 |
| tag, lambda$tag$10 | REACHABLE | MainActivity:300,521 |
| noTags, lambda$noTags$11 | REACHABLE | MainActivity:306,502 |

## LogEntry (8)
Definition file: core/logger/LogEntry.java, 114 lines, printed in full.

| # | Method | Label | confirmed_by | Printed citations |
|---|---|---|---|---|
| 33 | LogEntry.<init>(int,String,String,long) | REACHABLE | SOURCE | SessionLogger.java:124, :132, :144, :152, :158 `new LogEntry(nextLogEntryId++, ...)` in send(Alert) :117-166, called from TorrentSessionImpl (batch 19: sessionLogger.send(alert) :1102-1103). SessionLogger extends Logger (:32) and its send(entry) :166 calls Logger.send(LogEntry). |
| 34 | LogEntry.equals(Object) | REACHABLE | SOURCE | LogAdapter.java diffCallback areContentsTheSame :~75 `oldItem.equals(newItem)` (PagedListAdapter DiffUtil, framework dispatch INFERRED). |
| 35 | LogEntry.getId() | REACHABLE | SOURCE | LogAdapter.java diffCallback areItemsTheSame `oldItem.getId() == newItem.getId()`. |
| 36 | LogEntry.getMsg() | REACHABLE | SOURCE | LogAdapter.java ViewHolder.bind `binding.msg.setText(entry.getMsg())`. |
| 37 | LogEntry.getTag() | REACHABLE | SOURCE | LogAdapter.java ViewHolder.bind `binding.tag.setText(entry.getTag())`; also SessionLogger.java:66-74 filter lambdas call entry.getTag().equals(...). |
| 38 | LogEntry.getTimeStampAsString() | REACHABLE | SOURCE | LogAdapter.java ViewHolder.bind `binding.timeStamp.setText(entry.getTimeStampAsString())`; also LogEntry.toStringWithTimeStamp calls it (batch 21). |
| 39 | LogEntry.hashCode() | OPEN | — | No hashCode caller printed in files read this stage. equals() is called (above), but that does not by itself print a hashCode call. Not UNREACHABLE; pending full-repo grep. |
| 40 | LogEntry.toString() | REACHABLE | SOURCE | Logger.java:437 `entry.toStringWithTimeStamp() : entry.toString()` in write(...); LogViewModel.java copyLogEntryToClipboard `entry.toString()` as clipboard text. |

Note: LogEntry.getTimeStamp() (no-arg, returns long) is NOT in batch 20 or 21; do not conflate it with getTimeStampAsString() above.
