# A1-R5 evidence — LibreTorrent batches 103 / 114 (helper only, NOT the merger)

Scope and method (all read-only; no merge-ready file, graph, part, verification,
or progress file was edited, and nothing was pushed):

- Batch rows read first from:
  - `graphs/LibreTorrent/scratch/merge-ready/batch103-merge-ready.md`
    (rows 34, 35, 36, 40 all OPEN)
  - `graphs/LibreTorrent/scratch/merge-ready/batch114-merge-ready.md`
    (rows 22, 23 both OPEN)
- Source root searched (full tree, java + res, not java-only):
  `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main`
  (633 files: 281 `.java` + 252 `.xml` + manifest/assets; this matches the
  Phase-1 app tree of 252 org + 29 feedparser/NanoHTTPD java files plus res).
  Every method-name grep below ran over this whole root, so layout/databinding
  XML was searched too — there are ZERO res hits for any of the six class
  names or method names.
- Bytecode lookup: `graphs/LibreTorrent/auto_calls.json` (5,496 `calls` edges).
  Exact-`dst` equality was used, not substring matching (substring matching
  falsely counts `addItems` as `addItem` — see row 103/40).
- Every receiver on every near-miss hit was checked by printing its context
  lines; a hit only counts as a caller if its receiver is the row's class
  (or, for the interface setters, a `FileNode`-typed variable that could
  dispatch to `FileManagerNode` — no such call exists; see rows 103/35, 103/36).
- Implicit use checked per row and reported: none found for any of the six.
  These are plain setters / a plain list-add method, not lifecycle,
  Parcelable, `equals`/`compareTo`/`hashCode`, or framework-override methods,
  so no collection, sorting, set-membership, or framework dispatch invokes
  them. (For contrast, the bytecode graph DOES show implicit use for sibling
  rows — `FileManagerNode.compareTo` from `FileManagerAdapter.lambda$static$0`
  and `FileManagerNode.equals` from the DiffUtil callbacks — which is why
  those sibling rows are not in this set.)
- Caveat stated plainly: generated build code and library/framework code
  outside `src/main` were not text-searched. The proposals below rest on two
  independent legs instead of on absence in one tree: (a) the full `src/main`
  grep (java + res) with every hit dispositioned, and (b) the compiled
  bytecode call graph with zero exact edges. No mechanism was found by which
  generated or library code would call these app setters (they are not
  framework overrides and have no databinding/res reference).

Path shorthand below: `SRC` =
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`.
All line numbers were printed with `sed -n` / `grep -n` from the clone at
HEAD 6805252 and are quoted verbatim.

## 103/34 — FileManagerNode.setEnabled — proposed: UNREACHABLE, no_trigger_in_app

- Method: `FileManagerNode.setEnabled(boolean)` — definition
  `SRC/ui/filemanager/FileManagerNode.java:75-78` (`this.enabled = enabled;`).
  The 3-arg constructor (`:39-44`) sets all three fields at construction.
- Grep file: `grep_103_34.txt` — full `grep -rn setEnabled` over `src/main`:
  12 lines, plus appended class-usage grep for `FileManagerNode` (28 lines).
- Disposition of all 12 hits: the definition itself (:75); two
  `setEnabledProtocols` hits in `NanoHTTPD.java:445,447` (a different method);
  `FileManagerAdapter.java:135` `itemView.setEnabled(item.isEnabled())` —
  receiver is the row `View` (`itemView`), and it READS `isEnabled()`
  (printed context `FileManagerAdapter.java:126-160`); eight
  `ProxySettingsFragment.java` hits (`:114,:124,:137,:145,:187,:192,:197,:202`)
  whose receivers are Preference objects, printed at `:100-150`, e.g.
  `EditTextPreference address = findPreference(keyAddress);` followed by
  `address.setEnabled(enableAdvancedSettings);` — none is a
  `FileManagerNode`-typed receiver.
- Bytecode: exact `dst == FileManagerNode.setEnabled`: 0 edges. Any
  `dst` containing `.setEnabled`: 0. The bytecode graph does contain
  `FileManagerNode.isEnabled` callers (`FileManagerAdapter$ViewHolder.bind`
  `:137`) — reads only, never the setter.
- Implicit use: none. `setEnabled` is not a framework method on this class
  and no collection/sorting/framework path calls it.
- Proposed verdict: UNREACHABLE, no_trigger_in_app.

## 103/35 — FileManagerNode.setName — proposed: UNREACHABLE, no_trigger_in_app

- Method: `FileManagerNode.setName(String)` — definition
  `SRC/ui/filemanager/FileManagerNode.java:53-56` (`node = name;`), an
  `@Override` of the interface method declared at
  `SRC/core/model/filetree/FileNode.java:40` (`void setName(String name);`).
- Grep file: `grep_103_35.txt` — full `grep -rn setName` over `src/main`:
  17 lines, plus appended `FileManagerNode` class-usage grep.
- Disposition of all 17 hits: two definitions on other classes
  (`FileManagerSpinnerAdapter$StorageSpinnerItem.java:69` is inside the
  spinner file, a different class; plus `AddFeedMutableParams:65`,
  `AddTagState:47`, `AddTorrentMutableParams:71`,
  `TorrentDetailsMutableParams:43`); the interface declaration
  (`FileNode.java:40`); the sibling implementation
  (`FileTree.java:131`, printed `FileTree.java:120-170`, a `FileTree` setter,
  not a `FileManagerNode` call); other-class call sites
  (`NanoHTTPD.java:334,1819` Thread receivers;
  `TorrentSessionImpl.java:484,1643` — printed `:478-488`, receiver `p`
  with `p.getName()` / `p.getFlags()`, a torrent object, not a node;
  `AddFeedViewModel.java:157`, `AddTagViewModel.java:47`,
  `AddTorrentViewModel.java:344`, `DetailTorrentViewModel.java:437`,
  `DetailTorrentInfoFragment.java:227` — all ViewModel/state receivers).
  No hit has a `FileManagerNode`- or `FileNode`-typed receiver.
- Interface-dispatch check: `FileNode`-typed usages outside the filemanager
  are only `BencodeFileTree` / `TorrentContentFileTree` constructions
  (`BencodeFileTreeUtils.java:48,124-125`,
  `TorrentContentFileTreeUtils.java:48,124-125`,
  `AddTorrentViewModel.java:418`, `DetailTorrentViewModel.java:238`) plus
  `FileNode.Type` constants — none calls `setName`. Bytecode confirms:
  exact `dst == FileNode.setName`: 0 edges, and no `receiver_variants`
  entry for `FileNode`/`FileManagerNode` at all.
- Bytecode: exact `dst == FileManagerNode.setName`: 0 edges. The 8
  substring `.setName` edges are all other classes
  (`AddTorrentMutableParams` x2, `AddTagState` x2,
  `TorrentDetailsMutableParams` x2, `AddFeedMutableParams` x2).
- Construction sites (why no setter is needed): nodes are built fully
  formed by `FileManagerViewModel.getChildItems`
  (`FileManagerViewModel.java:127,134,136`, printed `:113-140`), e.g.
  `items.add(new FileManagerNode(file.getName(), FileNode.Type.DIR, true));`.
  All other `FileManagerNode` usages (28-line class grep) only read
  (`getName`, `getType`, `isEnabled`, `isDirectory`, `compareTo`, `equals`).
- Implicit use: none found.
- Proposed verdict: UNREACHABLE, no_trigger_in_app.

## 103/36 — FileManagerNode.setType — proposed: UNREACHABLE, no_trigger_in_app

- Method: `FileManagerNode.setType(int)` — definition
  `SRC/ui/filemanager/FileManagerNode.java:65-68` (`nodeType = type;`), an
  `@Override` of `FileNode.java:44` (`void setType(int type);`).
- Grep file: `grep_103_36.txt` — full `grep -rn setType` over `src/main`:
  7 lines, plus appended `FileManagerNode` class-usage grep.
- Disposition of all 7 hits: the definition (:65); the interface
  declaration (`FileNode.java:44`); the sibling implementation
  (`FileTree.java:159`, printed `FileTree.java:120-170`); four
  `sharingIntent.setType("text/plain")` Intent call sites
  (`DetailTorrentFragment.java:601`,
  `DetailTorrentFilesFragment.java:520`,
  `DetailTorrentPeersFragment.java:196`,
  `DetailTorrentTrackersFragment.java:384`). No node receiver anywhere.
- Interface-dispatch check: same as row 103/35 — no `FileNode`-typed
  `setType` call exists in source, and bytecode exact
  `dst == FileNode.setType`: 0 edges, no `receiver_variants` entry.
- Bytecode: exact `dst == FileManagerNode.setType`: 0 edges; any
  `dst` containing `.setType`: 0.
- Construction sites are the same fully-formed constructor calls as row
  103/35 (`FileManagerViewModel.java:127,134,136`).
- Implicit use: none found.
- Proposed verdict: UNREACHABLE, no_trigger_in_app.

## 103/40 — FileManagerSpinnerAdapter.addItem — proposed: UNREACHABLE, no_trigger_in_app

- Method: `FileManagerSpinnerAdapter.addItem(StorageSpinnerItem)` — definition
  `SRC/ui/filemanager/FileManagerSpinnerAdapter.java:105-108`
  (`items.add(item);`). Note the plural sibling `addItems(List)` at `:110-113`.
- Grep file: `grep_103_40.txt` — full `grep -rn addItem` over `src/main`:
  15 lines, plus appended `FileManagerSpinnerAdapter` class-usage grep
  (12 lines).
- Singular-vs-plural check (the whole question for this row): a targeted
  `grep -rn '\.addItem('` returns ZERO call sites, and
  `grep -rn 'addItem('` minus `addItems`/`addItemDecoration` returns ONLY
  the definition at `:105`. All other hits in the 15-line file are the
  plural method (`FileManagerDialog.java:210,645`
  `storageAdapter.addItems(spinnerItems);` — printed contexts
  `FileManagerDialog.java:200-215` and `:638-650`, including the adjacent
  `storageAdapter.setTitle(...)` / `clear()` / `notifyDataSetChanged()`
  calls that show the dialog's spinner path uses `addItems` exclusively;
  `FeedRepositoryImpl.java:170`, `FeedDao.java:82`, `FeedRepository.java:68`,
  `FeedFetcherWorker.java:172` — `addItems` on feed objects) or
  `RecyclerView.addItemDecoration` (6 unrelated hits).
- Class-usage check: the adapter's only construction sites are
  `FileManagerDialog.java:208` (`storageAdapter = new FileManagerSpinnerAdapter(this);`)
  and its `StorageSpinnerItem` constructions in
  `FileManagerViewModel.java:367,380` (items are collected into a list and
  handed over via `addItems`, never via singular `addItem`).
- Bytecode: exact `dst == FileManagerSpinnerAdapter.addItem`: 0 edges.
  The 2 substring matches are the plural method:
  `FileManagerDialog.onCreate -> FileManagerSpinnerAdapter.addItems`
  (`FileManagerDialog.java:210`, exact dispatch) and
  `FileManagerDialog.reloadSpinner -> FileManagerSpinnerAdapter.addItems`
  (`:645`, exact dispatch). No singular edge exists.
- Implicit use: none. `BaseAdapter` framework dispatch calls
  `getCount`/`getItem`/`getView`, never an app-defined `addItem`.
- Proposed verdict: UNREACHABLE, no_trigger_in_app.

## 114/22 — PreferenceActivityConfig.setFragment — proposed: UNREACHABLE, no_trigger_in_app

- Method: `PreferenceActivityConfig.setFragment(String)` — definition
  `SRC/ui/settings/PreferenceActivityConfig.java:46-49`
  (`this.fragment = fragment;`).
- Grep file: `grep_114_22.txt` — full `grep -rn setFragment` over `src/main`:
  16 lines, plus appended `PreferenceActivityConfig` class-usage grep
  (14 lines).
- Disposition of all 16 hits: the definition (:46); three DIFFERENT
  `setFragment` methods with a Fragment-typed argument, not a String:
  `PreferenceActivity.java:85`
  (`public <F extends PreferenceFragmentCompat> void setFragment(F fragment)`,
  called at `:82` `setFragment(getFragment(fragment));`),
  `SettingsFragment.java:220`
  (`private <F extends PreferenceFragmentCompat> void setFragment(F fragment, String title)`,
  called at `:94,:141,:150,:159,:168,:177,:186,:195,:204`),
  `NetworkSettingsFragment.java:361` (same two-arg Fragment form, called
  at `:231,:248`). No hit is `config.setFragment(...)` or any call on a
  `PreferenceActivityConfig`-typed receiver.
- Class-usage check (14 lines, all dispositioned): config objects are
  created ONLY by the 2-arg constructor and immediately put in an Intent:
  `SettingsFragment.java:235-239` (printed `:228-242`,
  `new PreferenceActivityConfig(fragment.getSimpleName(), title);`
  + `i.putExtra(PreferenceActivity.TAG_CONFIG, config);`),
  `NetworkSettingsFragment.java:252-256` (printed `:245-260`) and
  `:373-377` (printed `:368-380`, same shape). On the receiving side,
  `PreferenceActivity.java:69-71` (printed `:60-90`) reads ONLY the
  getters: `config.getFragment();` / `config.getTitle();` — never a setter.
- Bytecode: exact `dst == PreferenceActivityConfig.setFragment`: 0 edges.
  The 5 substring `.setFragment` edges are the three other classes above
  (`SettingsFragment` x2, `NetworkSettingsFragment` x2,
  `PreferenceActivity` x1). Bytecode config edges are constructor-only
  (`SettingsFragment.startActivity -> PreferenceActivityConfig.<init>(String,String)`
  `:236`, `NetworkSettingsFragment` `:254,:374`) plus getter reads
  (`PreferenceActivity.onCreate -> getFragment :70`, `getTitle :71`).
- Implicit use: none. Parcelable framework dispatch uses the Parcel
  constructor / `CREATOR`, not this setter; no res/databinding reference.
- Proposed verdict: UNREACHABLE, no_trigger_in_app.

## 114/23 — PreferenceActivityConfig.setTitle — proposed: UNREACHABLE, no_trigger_in_app

- Method: `PreferenceActivityConfig.setTitle(String)` — definition
  `SRC/ui/settings/PreferenceActivityConfig.java:56-59`
  (`this.title = title;`).
- Grep file: `grep_114_23.txt` — full `grep -rn setTitle` over `src/main`:
  40 lines, plus appended `PreferenceActivityConfig` class-usage grep.
- Disposition of all 40 hits: the definition (:56); every other hit is a
  different receiver — `toolbar.setTitle` (e.g.
  `PreferenceActivity.java:76` `toolbar.setTitle(title);`, printed
  `:60-90`, where `title` came from `config.getTitle()`, not from a
  config setter; `AddTorrentActivity.java:279`, `FeedActivity.java:113`,
  `FileManagerDialog.java:154,157,160,165`, `LogActivity.java:97`,
  `SettingsActivity.java:52`, etc.), dialog-builder `setTitle`
  (`BaseAlertDialog.java:150`, `ClipboardDialog.java:102`,
  `AddFeedDialog.java:265,269`, `CreateTorrentDialog.java:283,297,300`,
  etc.), menu-item `setTitle` (`DetailTorrentFragment.java:434,439`,
  `LogActivity.java:211,215,221,225`, `MainFragment.java:454`, etc.),
  `actionMode.setTitle`, and `storageAdapter.setTitle`
  (`FileManagerDialog.java:209,315,646` — the spinner adapter's own
  `setTitle`, defined at `FileManagerSpinnerAdapter.java:182`, a
  different class). No hit is `config.setTitle(...)` or any call on a
  `PreferenceActivityConfig`-typed receiver.
- Class-usage / receiving-side check: identical to row 114/22 —
  construction is 2-arg-ctor + `putExtra` only
  (`SettingsFragment.java:235`, `NetworkSettingsFragment.java:252,373`);
  the receiver reads only `getTitle()` (`PreferenceActivity.java:71`).
- Bytecode: exact `dst == PreferenceActivityConfig.setTitle`: 0 edges.
  The 3 substring `.setTitle` edges are all
  `FileManagerSpinnerAdapter.setTitle` (the spinner adapter, not the config).
- Implicit use: none, same reasoning as row 114/22.
- Proposed verdict: UNREACHABLE, no_trigger_in_app.

## Summary (helper proposals only — merger decides and applies)

| Row | Method | Proposed verdict | Method-grep lines | Bytecode exact edges |
|-----|--------|------------------|-------------------|----------------------|
| 103/34 | FileManagerNode.setEnabled | UNREACHABLE, no_trigger_in_app | 12 | 0 |
| 103/35 | FileManagerNode.setName | UNREACHABLE, no_trigger_in_app | 17 | 0 |
| 103/36 | FileManagerNode.setType | UNREACHABLE, no_trigger_in_app | 7 | 0 |
| 103/40 | FileManagerSpinnerAdapter.addItem | UNREACHABLE, no_trigger_in_app | 15 | 0 (2 plural addItems edges only) |
| 114/22 | PreferenceActivityConfig.setFragment | UNREACHABLE, no_trigger_in_app | 16 | 0 |
| 114/23 | PreferenceActivityConfig.setTitle | UNREACHABLE, no_trigger_in_app | 40 | 0 |

Counts: 6 rows proposed, 6 UNREACHABLE / no_trigger_in_app, 0 REACHABLE,
0 undecided. No row was left undecided: each has a saved full-tree grep
(method name over all of `src/main`, java + res) with every hit
dispositioned by printed context, plus a zero exact-edge bytecode lookup.

Files delivered in this work dir (only dir written to):
`EVIDENCE.md`, `grep_103_34.txt` (42 lines incl. class-usage appendix),
`grep_103_35.txt` (47), `grep_103_36.txt` (37), `grep_103_40.txt` (29),
`grep_114_22.txt` (32), `grep_114_23.txt` (56).
