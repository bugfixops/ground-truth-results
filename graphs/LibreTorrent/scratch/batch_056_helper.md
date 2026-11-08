# LibreTorrent batch 56 source audit

Membership is exactly the 40 plan rows printed at the top of `batch_056_helper_printed.txt`. The evidence contains the complete source for the URL-normalization, path, percent-encoding, bencoded file-tree, binding utility, and date utility classes, plus a source-root caller and binding-annotation search. All rows remain OPEN because the relevant call chains from app entry points have not been traced end-to-end; binding methods may be invoked by data binding, and their generated dispatch source is outside this printed app-source excerpt. No missing caller match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `NormalizeUrl.isMatch(String,String[])boolean` | OPEN | `NormalizeUrl.java` body and caller search printed; complete URL input/entry route unresolved. |
| 2 | `NormalizeUrl.join(CharSequence,String[])String` | OPEN | `NormalizeUrl.java` body and caller search printed; complete caller route unresolved. |
| 3 | `NormalizeUrl.makeUserInfo(String,String)String` | OPEN | `NormalizeUrl.java` body and caller search printed; complete normalization entry route unresolved. |
| 4 | `NormalizeUrl.mapToQuery(Map)String` | OPEN | `NormalizeUrl.java` body and caller search printed; complete normalization entry route unresolved. |
| 5 | `NormalizeUrl.normalize(String,Options)String` | OPEN | `NormalizeUrl.java` body and source callers printed; full app input route unresolved. |
| 6 | `NormalizeUrl.parseQuery(String)Map` | OPEN | `NormalizeUrl.java` body and caller search printed; complete parsing entry route unresolved. |
| 7 | `NormalizeUrl.urlToString(String,String,String,String,String,String,String)String` | OPEN | `NormalizeUrl.java` body printed; complete caller route unresolved. |
| 8 | `NormalizeUrl$Options.<init>()V` | OPEN | Options source printed; construction/use route unresolved. |
| 9 | `PathResolver.join(CharSequence,List)String` | OPEN | `PathResolver.java` body and callers printed; complete caller route unresolved. |
| 10 | `PathResolver.merge(String,String)String` | OPEN | `PathResolver.java` body and callers printed; complete caller route unresolved. |
| 11 | `PathResolver.resolve(String,String)String` | OPEN | `PathResolver.java` body and callers printed; complete app entry route unresolved. |
| 12 | `PathResolver.resolve(String[])String` | OPEN | `PathResolver.java` overload body printed; caller path unresolved. |
| 13 | `PercentEncoder.<clinit>()V` | OPEN | `PercentEncoder.java` source/static setup printed; class initialization via an app entry not traced. |
| 14 | `PercentEncoder.decode(String)String` | OPEN | `PercentEncoder.java` body and callers printed; full URL/parser route unresolved. |
| 15 | `PercentEncoder.needsUnescaping(String)boolean` | OPEN | `PercentEncoder.java` body and callers printed; complete normalization route unresolved. |
| 16 | `PercentEncoder.pow(int,int)int` | OPEN | `PercentEncoder.java` helper body printed; route through decoding callers unresolved. |
| 17 | `PercentEncoder.unhex(char[])byte` | OPEN | `PercentEncoder.java` helper body printed; route through decoding callers unresolved. |
| 18 | `BencodeFileTreeUtils.buildFileTree(List)Pair` | OPEN | `BencodeFileTreeUtils.java` body and callers printed; complete torrent add/detail entry route unresolved. |
| 19 | `BencodeFileTreeUtils.makeObject(int,String,long,BencodeFileTree,boolean)BencodeFileTree` | OPEN | `BencodeFileTreeUtils.java` body and internal callers printed; full caller route unresolved. |
| 20 | `BindingAdapterUtils.formatDate(TextView,long)V` | OPEN | Binding adapter declaration/body printed; generated data-binding dispatch route unresolved. |
| 21 | `BindingAdapterUtils.formatETA(Context,long)String` | OPEN | `BindingAdapterUtils.java` body and binding annotation printed; generated dispatch route unresolved. |
| 22 | `BindingAdapterUtils.formatFileSize(TextView,long,String)V` | OPEN | Binding adapter declaration/body printed; generated data-binding dispatch route unresolved. |
| 23 | `BindingAdapterUtils.formatFloat(TextView,double,int)V` | OPEN | Binding adapter declaration/body printed; generated data-binding dispatch route unresolved. |
| 24 | `BindingAdapterUtils.formatPieces(Context,int,int,int)String` | OPEN | `BindingAdapterUtils.java` body/annotation printed; generated dispatch route unresolved. |
| 25 | `BindingAdapterUtils.formatPiecesInfo(Context,int,int,int)String` | OPEN | `BindingAdapterUtils.java` body/annotation printed; generated dispatch route unresolved. |
| 26 | `BindingAdapterUtils.formatProgress(Context,long,long,int)String` | OPEN | `BindingAdapterUtils.java` body/annotation printed; generated dispatch route unresolved. |
| 27 | `BindingAdapterUtils.formatSpeed(Context,long,long)String` | OPEN | `BindingAdapterUtils.java` body/annotation printed; generated dispatch route unresolved. |
| 28 | `DateUtils.<clinit>()V` | OPEN | `DateUtils.java` static fields/setup printed; class initialization route not traced. |
| 29 | `DateUtils.endOfMonth(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 30 | `DateUtils.endOfToday(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 31 | `DateUtils.endOfWeek(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 32 | `DateUtils.endOfYear(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 33 | `DateUtils.endOfYesterday(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 34 | `DateUtils.formatElapsedTime(Context,long)String` | OPEN | `DateUtils.java` body and callers printed; full UI entry route unresolved. |
| 35 | `DateUtils.formatElapsedTime(Context,StringBuilder,long)String` | OPEN | `DateUtils.java` overload body printed; full UI entry route unresolved. |
| 36 | `DateUtils.initFormatStrings(Context)V` | OPEN | `DateUtils.java` initialization helper and callers printed; full application startup route unresolved. |
| 37 | `DateUtils.startOfMonth(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 38 | `DateUtils.startOfToday(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 39 | `DateUtils.startOfWeek(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |
| 40 | `DateUtils.startOfYear(long)long` | OPEN | `DateUtils.java` body printed; complete calendar/scheduler caller route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
