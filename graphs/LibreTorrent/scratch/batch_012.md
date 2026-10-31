# Batch 12 source audit

Membership is the 40 rows in batch 12 of `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (exact list in `batch_012_plan.txt`). Source excerpts are saved in `batch_012_helper_printed.txt`; independent caller search output is `batch_012_call_audit.txt`.

I did not promote a candidate to REACHABLE based on bytecode or an incomplete entry route. The helper identified 19 methods whose local parser call chain is supported by source, but graph_def.py does not yet contain the complete hand-written worker/entry route required by the brief. Twelve methods remain OPEN for incomplete upstream routes or non-app dispatch. Nine have no source caller within the app and bundled feed parser and are labeled `UNREACHABLE/no_trigger_in_app`.

| Method | Label | Kind / reason | Printed evidence |
|---|---|---|---|
| `databinding.DataBinderMapperImpl.<init>` | OPEN | Generated source and dispatch absent; grep under rule F has no match. | `batch_012_helper_printed.txt` |
| `Enclosure.<init>` | OPEN | Parser source constructs it, but complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `Enclosure.equals` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `Enclosure.java:56-67`; `batch_012_call_audit.txt` |
| `Enclosure.getType` | OPEN | Parser source calls getter, but complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `Enclosure.getUrl` | OPEN | Parser source calls getter, but complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `Enclosure.hashCode` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `Enclosure.java:69-75`; `batch_012_call_audit.txt` |
| `Enclosure.toString` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `Enclosure.java:77-84`; `batch_012_call_audit.txt` |
| `EzRssTorrentItem.<init>` | OPEN | Parser source constructs it, but complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `EzRssTorrentItem.equals` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `EzRssTorrentItem.java:97-113`; `batch_012_call_audit.txt` |
| `EzRssTorrentItem.getInfoHash` | OPEN | Parser source calls getter, but complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `EzRssTorrentItem.hashCode` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `EzRssTorrentItem.java:115-125`; `batch_012_call_audit.txt` |
| `EzRssTorrentItem.toString` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `EzRssTorrentItem.java:127-139`; `batch_012_call_audit.txt` |
| `FeedException.<init>(String)` | OPEN | Source throw site exists; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedException.<init>(Throwable)` | OPEN | Source catch/wrap site exists; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedParserFactory.newParser` | OPEN | Source caller exists; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedType.<clinit>` | OPEN | Enum is referenced by parser source; complete route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedUtils.<clinit>` | OPEN | Static date fields are referenced by parser source; complete route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedUtils.convertAtomDate` | OPEN | Parser source calls it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedUtils.convertRss1Date` | OPEN | Parser source calls it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedUtils.convertRss2Date` | OPEN | Parser source calls it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `FeedUtils.equalsOrNull` | OPEN | Called by `BaseItem.equals`; whether equality is triggered remains unresolved. | `BaseItem.java:52-59`; `FeedUtils.java:112-118` |
| `XML.<clinit>` | OPEN | Static map initialization is tied to an XMLInputStream branch whose upstream dispatch is unresolved. | `batch_012_helper_printed.txt` |
| `XML.hash` | OPEN | Called by XMLInputStream entity handling; upstream stream-read dispatch is unresolved. | `batch_012_helper_printed.txt` |
| `XMLInputStream.<init>` | OPEN | Parser source constructs it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `XMLInputStream.given` | OPEN | Internal source calls exist, but upstream SAX stream-read dispatch is unresolved. | `batch_012_helper_printed.txt` |
| `XMLInputStream.isAlphaNumeric` | OPEN | Internal source call exists, but upstream SAX stream-read dispatch is unresolved. | `batch_012_helper_printed.txt` |
| `XMLInputStream.isWhiteSpace` | OPEN | Internal source call exists, but upstream SAX stream-read dispatch is unresolved. | `batch_012_helper_printed.txt` |
| `XMLInputStream.length` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `XMLInputStream.java:31-40`; `batch_012_call_audit.txt` |
| `XMLInputStream.read()` | OPEN | SAX receives the wrapper, but source does not establish which read overload it invokes. | `DefaultFeedParser.java:37`; `XMLInputStream.java:127-132` |
| `XMLInputStream.read(int)` | OPEN | Internal reader is called, but its public entry overload remains unresolved. | `batch_012_helper_printed.txt` |
| `XMLInputStream.read(byte[],int,int)` | OPEN | SAX receives the wrapper, but source does not establish this overload dispatch. | `DefaultFeedParser.java:37`; `XMLInputStream.java:134-144` |
| `XMLInputStream.readAmpersand` | OPEN | Internal path depends on unresolved SAX read dispatch. | `batch_012_helper_printed.txt` |
| `XMLInputStream.readIntoPushBack` | OPEN | Internal path depends on unresolved SAX read dispatch. | `batch_012_helper_printed.txt` |
| `AtomFeed.<init>` | OPEN | FeedHandler source constructs it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `AtomFeed.getItemList` | OPEN | Core parser source calls it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `AtomFeed.getTitle` | OPEN | Core parser source calls it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `AtomFeed.toString` | UNREACHABLE | no_trigger_in_app: no source caller in app/parser. | `AtomFeed.java:109-113`; `batch_012_call_audit.txt` |
| `AtomItem.<init>` | OPEN | FeedHandler source constructs it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |
| `AtomItem.getDescription` | UNREACHABLE | no_trigger_in_app: core parser does not read it and no app/parser caller was found. | `AtomItem.java:56-61`; `batch_012_call_audit.txt` |
| `AtomItem.getEnclosures` | OPEN | Core parser source calls it; complete app entry route is not yet handwritten. | `batch_012_helper_printed.txt` |

Count: 40 plan rows; 0 REACHABLE; 9 `UNREACHABLE/no_trigger_in_app`; 31 OPEN. No coverage evidence was opened or used.
