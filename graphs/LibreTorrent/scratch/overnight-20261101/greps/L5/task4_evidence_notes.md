# L5 task-4 evidence notes (java + res-layout scope; fetched-res scope appended after fetch)

Scope so far: 281 app Java files (corpus/java, incl. 28 feedparser + NanoHTTPD),
73 res-layout XML, test/androidTest other-sourcesets (checked, zero for all
targets — test callers would not count per D23 anyway). androidx library /
generated sources are NOT in the local corpus; that caveat is stated per row
where it matters. No label verdicts are issued here — rows belong to L1.

## 41/36 TorrentStream.hashCode — grep SUPPORTS UNREACHABLE
- Def: TorrentStream.java:110-113 (`return id.hashCode()` — a String call,
  not a TorrentStream call).
- Zero receiver-typed `.hashCode()` on a TorrentStream variable in 281 Java;
  zero `HashSet/HashMap<TorrentStream>` or similar hash collections
  (grep_41_36_37 + grep_selectable_callers_torrentstream2).
- No plausible unprinted dispatcher: TorrentStream is not a SelectionTracker
  key, not a databinding variable, not a DAO/entity; its only consumers are
  TorrentEngine/TorrentDownloadImpl/TorrentInputStream/TorrentStreamServer,
  which use `stream.id` / `stream.fileSize` fields, never hash the object.
- Res-layout: only `Integer.toString(...)` databinding hits (unrelated).

## 41/37 TorrentStream.toString — grep SUPPORTS UNREACHABLE
- Def: TorrentStream.java:123-136.
- Zero `stream.toString()`, zero log/concat/`String.valueOf`/setText use of a
  TorrentStream variable; TorrentStreamServer.java:153,214,248 concatenates
  `stream.id` / `stream.fileSize` (fields), never the stream itself.
- Res-layout toString hits are `Integer.toString(...)` only.

## 11/7 ui/tag TagItem.hashCode — grep SUPPORTS UNREACHABLE
- Def: ui/tag/TagItem.java:49-51 (`return info.hashCode()` — TagInfo call).
- Consumers: ui/tag/TagsAdapter DiffUtil calls `equals` (areContentsTheSame)
  and `isSame` (areItemsTheSame) only, never hashCode; ViewHolder.bind reads
  `item.info.name` / `item.info.color` only; SelectTagDialog:171
  `TagItem::new` construction + :179 onTagClicked(item) — no hash use.
- Zero hash-collection use of ui/tag TagItem; zero receiver-typed hashCode.
- Trap avoided: drawer TagItem (ui/main/drawer/TagItem.java:51, batch 10/39)
  is a DIFFERENT class; its hashCode body (`info.hashCode()`) is likewise
  only a TagInfo call, not a trigger for ui/tag TagItem.

## 11/8 ui/tag TagItem.toString — grep SUPPORTS UNREACHABLE
- Def: ui/tag/TagItem.java:55-60 (`"TagItem{" + "info=" + info + "}"` —
  the `info +` concat is inside the toString BODY, not a caller).
- Zero printed call, concatenation, log/print on a ui/tag TagItem outside
  that body; TagsAdapter.bind uses fields only; no databinding text
  expression names a TagItem variable (res-layout grep zero for TagItem).

## Batch 39 five flips (9, 11, 23, 28, 29) — grep SUPPORTS UNREACHABLE (all five)
- 39/9 getDhtNodes: only hits are TorrentSession.java:92 (interface decl)
  + TorrentSessionImpl.java:712 (def). handleStats uses `dhtNodes()` (super
  method), NOT getDhtNodes — trap avoided.
- 39/11 getDownloadSpeedLimit (session-level): only interface decl
  (TorrentSession.java:86) + def (:690). TorrentEngine.java:894-902,
  DetailTorrentViewModel:377-379, DetailTorrentFragment:754 are the
  PER-TASK chain (`task.getDownloadSpeedLimit()`), NOT this method.
- 39/23 getUploadSpeedLimit (session-level): same pattern — decl
  (TorrentSession.java:88) + def (:698); per-task chain at
  TorrentEngine.java:883-892, DetailTorrentViewModel:373-375,
  DetailTorrentFragment:753 is a different method.
- 39/28 isDHTEnabled: only decl (TorrentSession.java:112) + def (:847).
- 39/29 isPeXEnabled: only decl (TorrentSession.java:114) + def (:855).
- Res-layout: zero for all five names. Other-sourcesets: zero (checked
  for the Room/selectable set; batch-39 names re-checked in grep_39_flips
  scope — see file).

## 94/7 PeerListAdapter.getItemKey / 94/8 getItemPosition — grep SUPPORTS UNREACHABLE
- Defs: PeerListAdapter.java:86-93 / :95-100. No KeyProvider class for
  peers; no SelectionTracker built for peers in any fragment; the only
  `selectable.getItemKey/getItemPosition` call sites in the tree belong
  to OTHER adapters' KeyProviders (files :280/:286, trackers :241/:247,
  feed channel :289/:295, torrent list :344/:350) and are typed to those
  adapters' item types — they cannot dispatch to PeerListAdapter methods.
- No direct `peerAdapter.getItemKey(` / `getItemPosition(` call anywhere.

## 96/40 FeedItemsAdapter.getItemKey / 97/1 getItemPosition — grep SUPPORTS UNREACHABLE
- Defs: FeedItemsAdapter.java:91-97 / :100-103. Same pattern as peers:
  no KeyProvider for feed items, no SelectionTracker for FeedItemsFragment;
  other adapters' KeyProvider call sites are typed to other item types.
- FeedItemsAdapter.getItemPosition body is `indexOf` (equals-only), which
  is NOT a hashCode trigger and does not call getItemKey.

## 94/31 PiecesView 3-arg ctor — grep SUPPORTS UNREACHABLE (evidence only)
- Def: PiecesView.java:64-69; 2-arg ctor :57-63 does NOT chain to it
  (calls `super(context, attrs)` + `create(...)` only).
- Zero `new PiecesView(` in 281 Java; sole layout declaration
  (fragment_detail_torrent_pieces.xml:73-77) carries NO style attribute,
  so layout inflation uses the 2-arg ctor (D24 pattern).

## 102/13 FileManagerConfig.setFileName — grep SUPPORTS UNREACHABLE
- Def: FileManagerConfig.java:67-71 (fluent setter, returns this).
- Zero `.setFileName(` call sites in 281 Java (only hits: the def itself
  + unrelated `setFileNameFilter` in TorrentBuilder.java:155 /
  CreateTorrentViewModel.java:198); zero in res-layout; zero in
  other-sourcesets.
- Positive bypass evidence (why the setter is dead): callers that preset
  a file name assign the field directly — DetailTorrentFragment.java:541
  `config.fileName = viewModel.mutableParams.getName()`,
  FeedActivity.java:269 `config.fileName = "Feeds-" + ...`,
  LogActivity.java:311 `config.fileName = viewModel.getSaveLogFileName()`.
  Readers (FileManagerDialog.java:175, FileManagerViewModel.java:251)
  read `config.fileName` directly, never via the setter.
