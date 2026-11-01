# L1 SUMMARY — Stream A Phase 3, Group L1: hashCode / toString (D6/D7/D30)

## Totals
- Rows judged: 55. All row identities verified from their batch files under
  phase3/work/batch<N>-merge-ready.md (read-only copies); no list was trusted blindly.
  Scope check: scanning the 23 listed batches (3, 10, 20, 21, 28, 29, 30, 31, 32, 33, 34,
  47, 73, 81, 82, 84, 90, 92, 95, 99, 103, 106, 112) found no additional OPEN hashCode/toString
  rows beyond the 51 below. Already-REACHABLE rows (e.g. 20/40 LogEntry.toString,
  21/1 LogEntry.toStringWithTimeStamp) and non-target rows (e.g. 73/21 ClipboardDialog ctor
  whose item.toString() is a CharSequence) were excluded.
- Flips OPEN -> UNREACHABLE (no_trigger_in_app, INFERRED): 46.
- Verified, no change (UNREACHABLE stands): 4 (11/7, 11/8, 41/36, 41/37).
- Staying OPEN: 5 (3/26, 73/31, 95/35, 99/18, 112/30).
- Flips to REACHABLE: 0. No printed trigger outside an OPEN body was found for any row.
  90/16 was traced FIRST as instructed: TorrentDetailsInfo.toString (ui/detailtorrent/
  TorrentDetailsInfo.java:115-125) concatenates torrent/metaInfo/torrentInfo/advancedInfo,
  but itself has no outside trigger, so the gate does not flip and its dependents
  (31/40, 32/35, 30/9, 28/29) were judged on their own (also zero) triggers.

## Flips (old -> new), all OPEN -> UNREACHABLE INFERRED
HashCode: 10/30 PeerItem, 10/32 FeedItemsListItem, 10/39 drawer TagItem, 20/39 LogEntry,
21/39 AddTorrentParams, 28/28 AdvancedTorrentInfo, 29/2 MagnetInfo, 29/17 PeerInfo,
29/35 SessionStats, 30/8 TorrentInfo, 30/27 TrackerInfo, 31/1 FeedChannel, 31/13 FeedItem,
31/37 Torrent, 32/7 TorrentTagInfo, 32/34 TorrentMetaInfo.
ToString: 10/40 drawer TagItem, 21/40 AddTorrentParams, 28/29 AdvancedTorrentInfo,
29/3 MagnetInfo, 29/18 PeerInfo, 29/28 ReadPieceInfo, 29/36 SessionStats, 30/9 TorrentInfo,
30/29 TrackerInfo, 31/2 FeedChannel, 31/14 FeedItem, 31/25 TagInfo, 31/40 Torrent,
32/8 TorrentTagInfo, 32/20 BencodeFileItem, 32/35 TorrentMetaInfo, 33/8 BencodeFileTree,
33/16 FilePriority, 34/3 FileTree, 34/16 TorrentContentFileTree, 47/21 BaseSorting,
73/32 FileItem, 81/2 AddTorrentMutableParams, 82/13 DownloadableFileItem,
84/30 CreateTorrentMutableParams, 90/16 TorrentDetailsInfo, 90/28 TorrentDetailsMutableParams,
92/35 TorrentContentFileItem, 103/37 FileManagerNode, 106/40 LogMutableParams.
Dependency consistency (all verified from printed bodies): 90/16 UNREACHABLE is consistent
with 31/40, 32/35, 30/9, 28/29 UNREACHABLE (their only in-app concat sites are inside the
90/16 body); 34/16 UNREACHABLE closes 33/16 (priority concat) and, with 33/8 UNREACHABLE,
34/3 (both super.toString() hosts gone); 82/13 + 92/35 UNREACHABLE close 73/32 (both
super.toString() hosts gone); 10/40 + 30/9 + 21/40 (+ 11/8) UNREACHABLE close 31/25
(the only `+ tags` sites in the tree are the 30/9 and 21/40 bodies; the only `info`
concats are the 10/40 and 11/8 bodies).

## Staying OPEN, with resolvers
- 112/30 TorrentListItem.hashCode — resolver: printed androidx MutableSelection/Selection
  source showing hash-backed storage -> REACHABLE INFERRED (MainFragment copySelection
  sites :575-576/:599-600/:610-611). Otherwise stays OPEN per D30.
- 99/18 FeedChannelItem.hashCode — same resolver (FeedFragment copySelection
  :446-447/:466-467/:483-484/:496-497/:511-512).
- 95/35 TrackerItem.hashCode — same resolver (DetailTorrentTrackersFragment copySelection
  :362-363/:376-377).
- 73/31 FileItem.hashCode — same resolver via inheritance: TorrentContentFileItem defines
  no hashCode; its keys enter MutableSelection (DetailTorrentFilesFragment copySelection
  :438-439/:496-497/:511-512), so a hash-backed print would dispatch to the inherited
  FileItem.hashCode -> REACHABLE INFERRED. (D30's named list omits this case; see below.)
- 3/26 TagInfo.hashCode — resolver as named by D30 (the MutableSelection print), BUT the
  delegation chain it depends on fails independently (see "D30 premise that failed" 1).
  Its two delegators are now both UNREACHABLE (10/39 this set, 11/7 standing), so the
  merger should decide whether 3/26 follows its delegators to UNREACHABLE or stays OPEN
  on the carve-out; this verdict holds it OPEN per the task's explicit instruction.

## MutableSelection print outcome: NOT OBTAINED
Four web searches (queries in greps/L1/grep_mutableselection_search.txt) returned only
developer.android.com API reference pages. The Selection doc says the class "tracks
selected items by managing two sets" (primary + provisional) — a Set-interface statement,
not a concrete storage class, and not evidence that key.hashCode() is invoked (a Set may
be hash-, tree-, or ArraySet-backed). No AOSP/GitHub source URL was returned by any
search, so no source file text could be opened (browser.open requires a verbatim URL
from a tool result). Per D30, the SelectionTracker rows therefore stay OPEN with this
print named as resolver. No print was fabricated and no row was flipped on the API doc.

## D30 premises that failed (or needed correction)
1. D6's claim that 3/26 "flips with them via the drawer-TagItem delegation (10/39)" if
   MutableSelection is hash-backed: FAILED on printed app source. The delegation itself
   exists (drawer TagItem.hashCode :50-51 returns info.hashCode()), but NO
   SelectionTracker<TagItem> site exists anywhere in the 281 files
   (grep_selectiontracker.txt lists only TorrentListItem, FeedChannelItem, TrackerItem,
   TorrentContentFileItem keys). A hash-backed print would flip the three key rows, but
   cannot reach drawer TagItem or TagInfo through that route. 3/26 needs a REACHABLE
   delegator or another printed trigger, not the MutableSelection print.
2. D30's SelectionTracker list omits 73/31: TorrentContentFileItem keys enter
   MutableSelection, and their hashCode is the inherited FileItem.hashCode (73/31).
   73/31 is therefore held OPEN on the same print, although it is a toString-adjacent
   batch's hashCode row rather than a named SelectionTracker row.
3. Re-derivation flags do NOT revert: 41/36, 41/37, 11/7, 11/8 all MEET the full-repo
   standard on the fresh grep set below (for 11/7 and 11/8 the fresh grep closes the
   "pending saved full-repo grep" gap their proposals recorded). 41/28 stands under the
   private-nested exception and was not touched, as instructed.
4. Literal D30 reading applied to non-hash prints: D30/task text says the named rows stay
   OPEN even if the print shows non-hash storage. This verdict follows that literally;
   the merger may close them to UNREACHABLE after a non-hash print under outcome 2.

## Full-scope grep actually run (saved under phase3/greps/L1/)
- 281 app Java files (corpus/java: 252 app + 28 feedparser + 1 nanohttpd — the
  final_java_only library sources in scope): grep_all_calls.txt (every .hashCode() and
  .toString() line), grep_hash_collections.txt (every HashSet/HashMap/LinkedHashMap site;
  all target-typed collections are absent — every site is String/Integer/Long keyed),
  grep_selectiontracker.txt, grep_log_concat.txt (all 49 Log concat lines; operands are
  Strings/ints/fields/throwables only), grep_getstring_formatargs.txt (all getString
  format args are primitives/Strings/formatted values), grep_barevar_concat.txt,
  grep_implicit_dispatch.txt (Arrays.toString on primitive arrays only; String.valueOf on
  ints only; zero distinct/toSet/groupBy/Collectors), grep_rx_hash_ops.txt (zero),
  type_<Type>.txt per type (every occurrence line).
- 73 layout XML (corpus/res-layout): grep_layout_types.txt (zero target type names),
  grep_databinding_text.txt (all android:text expressions are field accesses; the sole
  bare-object expression is String-typed detailError in dialog_error.xml).
- 31 menu/xml XML fetched one at a time via the GitHub connector from branch
  work-2026-10-31 with ~30 s pauses (res-xml/fetch_log.txt, SHAs recorded):
  14 menu + 2 variant detail_torrent.xml + 14 xml (12 pref_* + provider_paths +
  searchable) + 1 xml-v26 pref_appearance. grep_resxml_fetched.txt: zero databinding
  expressions, zero type/hashCode/toString hits. Menu/preference XML structurally cannot
  reference Java objects (items/keys/titles only, all @string/@drawable refs).
- NOT individually fetched (stated scope limit, not hidden): values-*/ (strings, dimens,
  styles, arrays — no object references possible; their only dispatch route is Java
  getString/format args, all grepped above), drawable/color/animator/mipmap XML (no code
  references possible). Generated databinding/Room code is not in final_java_only; its
  inputs were covered instead (layout XML for databinding; printed DAOs/entities for
  Room, whose generated code operates on columns/keys, not entity hashCode/toString —
  the per-row argument the merger may overturn for the five Room-entity hashCode rows
  31/1, 31/13, 31/37, 32/7 and the entity toString rows if it requires a printed Room
  source rather than this argument).
- Near-misses explicitly rejected (not counted as triggers): List.contains/containsAll/
  indexOf and DiffUtil equals routes (equals-only); .hashCode()/.toString() calls on
  fields inside definition bodies (String id/name/url, List tags, primitive arrays);
  being a Map value or List element; TorrentInfo.java:210 tags.hashCode() (List call);
  ClipboardDialog.java:112 item.toString() (CharSequence); TorrentEngine.java:1188
  file.toString() (File); TagsAdapter.java:114 "Unknown item: " + item (AbstractTagItem-
  typed AND instanceof-guarded — a TagItem never reaches it); TorrentContentFilesAdapter
  :237 format arg `priority` (a String local, not FilePriority); Utils.java:924 String
  `val` (not a sorting object); TorrentStreamServer stream.id/fileSize (fields, not the
  stream); FileTree parent concat (self-type recursion inside its own body).
- Connector hygiene: no 429 was hit. One transient empty response on a variant-menu
  directory listing (not a 429) was recovered by a retry-after-pause in a hardened fetch
  script; no retry loop on any rate limit was needed. No token was used anywhere.
  No pushes, no branch edits, no tick markers written; only phase3/verdicts/L1/ and
  phase3/greps/L1/ were written, as instructed.
