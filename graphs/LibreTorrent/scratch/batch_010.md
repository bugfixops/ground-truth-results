# LibreTorrent batch 10 source audit

Membership: exactly the 40 batch `10` rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. I independently printed the plan, generated binding grep, candidate method bodies, constructor/factory callers and DataBindingUtil sites. Evidence is in `scratch/batch_010_independent_printed.txt`; the full helper review is in `scratch/batch_010_helper.md` and `scratch/batch_010_helper_printed.txt`.

The three no-trigger labels below are supported by printed declarations and caller searches. XML-instantiated custom view constructors and generated Data Binding routes remain OPEN because source does not establish which overload the framework/library calls. Equality/hash/sorting/spinner accessors remain OPEN where source evidence does not rule out collection, binding or library dispatch.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)` | OPEN | — | Matching DataBindingUtil layout request; generated overload unknown. | `DownloadableFilesAdapter.java:60-65` |
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentListBinding.bind(View)` | OPEN | — | DataBindingUtil request exists; generated bind dispatch absent. | `TorrentListAdapter.java:79-84` |
| `ItemTorrentListBinding.bind(View,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentListBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTorrentListBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTrackersListBinding.bind(View)` | OPEN | — | DataBindingUtil request exists; generated bind dispatch absent. | `TrackerListAdapter.java:73-78` |
| `ItemTrackersListBinding.bind(View,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTrackersListBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `ItemTrackersListBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `TagsListItemBinding.bind(View)` | OPEN | — | DataBindingUtil request exists; generated bind dispatch absent. | `TagsAdapter.java:48-54`; `scratch/batch_010_helper_printed.txt` |
| `TagsListItemBinding.bind(View,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `TagsListItemBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `TagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload unknown. | `scratch/batch_010_independent_printed.txt` |
| `Scheduler.<init>` | UNREACHABLE | no_trigger_in_app | Static utility class; no constructor declaration or app construction site. | `service/Scheduler.java:38-53`; `scratch/batch_010_independent_printed.txt` |
| `EmptyRecyclerView.<init>(Context)` | OPEN | — | XML references the view; source declares several constructors and does not establish which one Android calls. | `scratch/batch_010_helper_printed.txt` |
| `ExpansionHeader.<init>(Context)` | OPEN | — | XML references the view; constructor overload selection remains unverified. | `scratch/batch_010_helper_printed.txt` |
| `FixHintTextInputEditText.<init>(Context)` | OPEN | — | XML references the view; constructor overload selection remains unverified. | `scratch/batch_010_helper_printed.txt` |
| `RecyclerViewDividerDecoration.<init>(Context,int)` | UNREACHABLE | no_trigger_in_app | App construction sites use the Drawable overload; no caller uses `(Context,int)`. | `ui/customviews/RecyclerViewDividerDecoration.java:35-47`; caller output in `scratch/batch_010_independent_printed.txt` |
| `SwitchBar.<init>(Context)` | OPEN | — | XML references the view; constructor overload selection remains unverified. | `scratch/batch_010_helper_printed.txt` |
| `ThemedSpeedDialView.<init>(Context)` | OPEN | — | XML references the view; constructor overload selection remains unverified. | `scratch/batch_010_helper_printed.txt` |
| `PeerItem.hashCode` | OPEN | — | Override body printed; collection/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FeedItemsListItem.compareTo` | OPEN | — | Comparable body printed; sorting-library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FeedItemsListItem.hashCode` | OPEN | — | Override body printed; collection/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.getName` | OPEN | — | Getter body printed; binding/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.getSize` | OPEN | — | Getter body printed; binding/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.setName` | OPEN | — | Setter body printed; binding/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.setSize` | OPEN | — | Setter body printed; binding/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.setStoragePath` | OPEN | — | Setter body printed; binding/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `LogSettingsFragment.newInstance` | UNREACHABLE | no_trigger_in_app | No app source calls this factory. | `ui/log/LogSettingsFragment.java:43-49`; caller probe in `scratch/batch_010_independent_printed.txt` |
| `drawer.TagItem.hashCode` | OPEN | — | Override body printed; collection/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |
| `drawer.TagItem.toString` | OPEN | — | Override body printed; diagnostic/library invocation is not ruled out. | `scratch/batch_010_helper_printed.txt` |

Result: 40 plan rows reviewed; 3 source-supported UNREACHABLE labels and 37 OPEN.
