# Batch 12 helper report

Membership is exactly the 40 `batch==12` rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. The exact method list, printed source excerpts, and grep commands are in `scratch/batch_012_helper_printed.txt`.

The source establishes this app call chain: `FeedFetcherWorker` constructs core `FeedParser`; the constructor calls `FeedParserFactory.newParser().parse`; `DefaultFeedParser` creates `XMLInputStream` and a SAX `FeedHandler`; the handler creates Atom/RSS feed and item objects; core `FeedParser` then reads their fields. Rows tied to the SAX parser's invocation of stream read overloads remain OPEN because that specific dispatch is outside the printed source. The generated `DataBinderMapperImpl` constructor is also OPEN because its declaration and generated instantiation path are absent from the listed source root.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `databinding.DataBinderMapperImpl.<init>` | OPEN | — | Generated declaration and caller absent from listed Java source; no generated route evidence. | `batch_012_helper_printed.txt` (rule F grep: no match) |
| `Enclosure.<init>` | REACHABLE | — | SAX item parsing constructs Enclosure; core FeedParser iterates enclosure values. | `AtomItem.java:109-116`; `FeedHandler.java:94-96`; `FeedParser.java:170` |
| `Enclosure.equals` | UNREACHABLE | no_trigger_in_app | Source parser/app paths use the enclosure list and getters but never compare Enclosure objects. | `Enclosure.java:56-67`; source search output in `batch_012_helper_printed.txt` |
| `Enclosure.getType` | REACHABLE | — | Core FeedParser calls this getter while checking enclosure MIME type. | `FeedParser.java:170-176`; `Enclosure.java:40-42` |
| `Enclosure.getUrl` | REACHABLE | — | Core FeedParser calls this getter while checking enclosure URL. | `FeedParser.java:170-176`; `Enclosure.java:28-30` |
| `Enclosure.hashCode` | UNREACHABLE | no_trigger_in_app | No source path hashes Enclosure instances. | `Enclosure.java:69-75`; source search output in `batch_012_helper_printed.txt` |
| `Enclosure.toString` | UNREACHABLE | no_trigger_in_app | No source path renders Enclosure with `toString`. | `Enclosure.java:77-84`; source search output in `batch_012_helper_printed.txt` |
| `EzRssTorrentItem.<init>` | REACHABLE | — | Core parser asks the RSS2 item for EZRSS metadata; EzRss01Parser constructs this value. | `FeedParser.java:147-151,236-242`; `Rss2Item.java:118-120`; `EzRss01Parser.java:26-36` |
| `EzRssTorrentItem.equals` | UNREACHABLE | no_trigger_in_app | No source parser/app path compares EZRSS value objects. | `EzRssTorrentItem.java:97-113`; source search output in `batch_012_helper_printed.txt` |
| `EzRssTorrentItem.getInfoHash` | REACHABLE | — | Core parser reads the info hash returned by the RSS2 item parser. | `FeedParser.java:236-244`; `EzRssTorrentItem.java:61-63` |
| `EzRssTorrentItem.hashCode` | UNREACHABLE | no_trigger_in_app | No source path hashes EZRSS value objects. | `EzRssTorrentItem.java:115-125`; source search output in `batch_012_helper_printed.txt` |
| `EzRssTorrentItem.toString` | UNREACHABLE | no_trigger_in_app | No source path renders EZRSS value objects with `toString`. | `EzRssTorrentItem.java:127-139`; source search output in `batch_012_helper_printed.txt` |
| `FeedException.<init>(String)` | REACHABLE | — | Parser throws this constructor when the SAX handler returns no feed. | `DefaultFeedParser.java:37-40`; `FeedException.java:11-13` |
| `FeedException.<init>(Throwable)` | REACHABLE | — | Parser catch block wraps parse errors with this constructor. | `DefaultFeedParser.java:44-45`; `FeedException.java:15-17` |
| `FeedParserFactory.newParser` | REACHABLE | — | Core FeedParser calls the factory directly when parsing a fetched feed. | `core/FeedParser.java:67-71`; `FeedParserFactory.java:23-25` |
| `FeedType.<clinit>` | REACHABLE | — | FeedHandler reads enum constants while identifying RSS1/RSS2/Atom roots. | `FeedHandler.java:60-78`; `FeedType.java:6-8` |
| `FeedUtils.<clinit>` | REACHABLE | — | Date conversion methods use the static DateFormat fields initialized here. | `FeedUtils.java:12-19`; `FeedUtils.java:28-30,81-84,94-97` |
| `FeedUtils.convertAtomDate` | REACHABLE | — | Atom item date method delegates to this converter; core parser calls item `getPubDate`. | `FeedUtils.java:28-72`; `AtomItem.java:79-83`; `core/FeedParser.java:104-107` |
| `FeedUtils.convertRss1Date` | REACHABLE | — | RSS1 item date method delegates to this converter; core parser calls item `getPubDate`. | `FeedUtils.java:81-85`; `Rss1Item.java:75-80`; `core/FeedParser.java:104-107` |
| `FeedUtils.convertRss2Date` | REACHABLE | — | RSS2 item date method delegates to this converter; core parser calls item `getPubDate`. | `FeedUtils.java:94-103`; `Rss2Item.java:74-78`; `core/FeedParser.java:104-107` |
| `FeedUtils.equalsOrNull` | OPEN | — | BaseItem.equals calls it, but no app/parser caller of equals was established. | `BaseItem.java:52-59`; `FeedUtils.java:112-118` |
| `XML.<clinit>` | OPEN | — | Static map initializer is used by XML.hash, but the root XMLInputStream read callback remains OPEN. | `XML.java:17-23`; `XMLInputStream.java:95-111` |
| `XML.hash` | OPEN | — | XMLInputStream invokes it for entity references; reaching that code depends on unresolved SAX stream-read dispatch. | `XMLInputStream.java:95-111`; `DefaultFeedParser.java:37` |
| `XMLInputStream.<init>` | REACHABLE | — | DefaultFeedParser explicitly constructs the stream passed to SAXParser.parse. | `DefaultFeedParser.java:33-38`; `XMLInputStream.java:27-29` |
| `XMLInputStream.given` | OPEN | — | Read methods call this helper, but the parser's exact read-overload dispatch is unresolved. | `XMLInputStream.java:121-132,134-144`; `DefaultFeedParser.java:37` |
| `XMLInputStream.isAlphaNumeric` | OPEN | — | Called by the stream's ampersand scanner; upstream read dispatch is unresolved. | `XMLInputStream.java:95-101,157-161` |
| `XMLInputStream.isWhiteSpace` | OPEN | — | Called by the stream reader; upstream read dispatch is unresolved. | `XMLInputStream.java:68-77,146-155` |
| `XMLInputStream.length` | UNREACHABLE | no_trigger_in_app | The method has no app/parser caller and is not used by DefaultFeedParser's SAX call. | `XMLInputStream.java:31-40`; printed caller search in `batch_012_helper_printed.txt` |
| `XMLInputStream.read()` | OPEN | — | SAX parser receives this stream, but its choice of `read()` versus other overloads is not shown. | `DefaultFeedParser.java:37`; `XMLInputStream.java:127-132` |
| `XMLInputStream.read(int)` | OPEN | — | Internal reader is called by public read methods, whose SAX invocation is unresolved. | `XMLInputStream.java:42-64,127-143` |
| `XMLInputStream.read(byte[],int,int)` | OPEN | — | SAX parser receives this stream, but invocation of this overload is not shown. | `DefaultFeedParser.java:37`; `XMLInputStream.java:134-144` |
| `XMLInputStream.readAmpersand` | OPEN | — | Internal scan is called for `&`; upstream SAX read dispatch is unresolved. | `XMLInputStream.java:68-85,95-119` |
| `XMLInputStream.readIntoPushBack` | OPEN | — | Internal scan is called by read(int); upstream SAX read dispatch is unresolved. | `XMLInputStream.java:42-63,68-92` |
| `AtomFeed.<init>` | REACHABLE | — | FeedHandler constructs AtomFeed when it sees an Atom feed root. | `FeedHandler.java:74-80`; `AtomFeed.java:34-36` |
| `AtomFeed.getItemList` | REACHABLE | — | Core FeedParser enumerates the parsed feed's items. | `core/FeedParser.java:89-96`; `AtomFeed.java:93-107` |
| `AtomFeed.getTitle` | REACHABLE | — | Core FeedParser returns the feed title through the Feed interface. | `core/FeedParser.java:84-87`; `AtomFeed.java:43-47` |
| `AtomFeed.toString` | UNREACHABLE | no_trigger_in_app | No source caller renders the AtomFeed; method only delegates to getTitle. | `AtomFeed.java:109-113`; caller search in `batch_012_helper_printed.txt` |
| `AtomItem.<init>` | REACHABLE | — | FeedHandler constructs AtomItem for Atom entry elements. | `FeedHandler.java:94-96`; `AtomItem.java:30-32` |
| `AtomItem.getDescription` | UNREACHABLE | no_trigger_in_app | Core FeedParser does not read item description; no other app/parser caller was found. | `AtomItem.java:56-61`; caller search in `batch_012_helper_printed.txt` |
| `AtomItem.getEnclosures` | REACHABLE | — | Core FeedParser reads enclosures while selecting a torrent link. | `FeedParser.java:168-176`; `AtomItem.java:98-120` |

Count: 40 plan rows inspected; 19 REACHABLE; 9 UNREACHABLE (`no_trigger_in_app`); 12 OPEN. No coverage evidence was opened or used.
