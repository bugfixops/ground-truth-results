# Batch 10 helper report

Membership is exactly the 40 plan rows with `batch==10` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the plan output and source/call-site commands are saved in `scratch/batch_010_helper_printed.txt`.

The four generated binding types have app `DataBindingUtil.inflate` call sites but no source declarations in the listed Java root. The exact generated overload paths therefore remain OPEN. Of the remaining rows, three have no demonstrated app trigger: Scheduler's compiler-provided constructor (static utility class, no `new Scheduler` call), the unused `RecyclerViewDividerDecoration(Context,int)` overload (app call sites use the `Drawable` overload), and `LogSettingsFragment.newInstance` (factory has no source caller). The one-argument custom-view constructors remain OPEN because the layouts use those class names while the source also provides separate `AttributeSet` constructors; the allowed printed source does not establish the framework's constructor dispatch. Equality/hash/order and spinner accessors remain OPEN where a library or generated-code call cannot be ruled out from app source alone.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)` | OPEN | — | DataBindingUtil layout request exists; generated overload mapping absent. | `batch_010_helper_printed.txt`; `DownloadableFilesAdapter.java:60-65` |
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; call site does not name the generated overload. | `batch_010_helper_printed.txt`; `DownloadableFilesAdapter.java:60-65` |
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `DownloadableFilesAdapter.java:60-65` |
| `ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `DownloadableFilesAdapter.java:60-65` |
| `ItemTorrentListBinding.bind(View)` | OPEN | — | DataBindingUtil layout request exists; generated bind dispatch absent. | `batch_010_helper_printed.txt`; `TorrentListAdapter.java:79-84` |
| `ItemTorrentListBinding.bind(View,Object)` | OPEN | — | Same; exact bind overload unknown. | `batch_010_helper_printed.txt`; `TorrentListAdapter.java:79-84` |
| `ItemTorrentListBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not call this generated overload directly. | `batch_010_helper_printed.txt`; `TorrentListAdapter.java:79-84` |
| `ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TorrentListAdapter.java:79-84` |
| `ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TorrentListAdapter.java:79-84` |
| `ItemTorrentListBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TorrentListAdapter.java:79-84` |
| `ItemTrackersListBinding.bind(View)` | OPEN | — | DataBindingUtil layout request exists; generated bind dispatch absent. | `batch_010_helper_printed.txt`; `TrackerListAdapter.java:73-78` |
| `ItemTrackersListBinding.bind(View,Object)` | OPEN | — | Same; exact bind overload unknown. | `batch_010_helper_printed.txt`; `TrackerListAdapter.java:73-78` |
| `ItemTrackersListBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not call this generated overload directly. | `batch_010_helper_printed.txt`; `TrackerListAdapter.java:73-78` |
| `ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TrackerListAdapter.java:73-78` |
| `ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TrackerListAdapter.java:73-78` |
| `ItemTrackersListBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TrackerListAdapter.java:73-78` |
| `TagsListItemBinding.bind(View)` | OPEN | — | DataBindingUtil layout request exists; generated bind dispatch absent. | `batch_010_helper_printed.txt`; `TagsAdapter.java:48-54` |
| `TagsListItemBinding.bind(View,Object)` | OPEN | — | Same; exact bind overload unknown. | `batch_010_helper_printed.txt`; `TagsAdapter.java:48-54` |
| `TagsListItemBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not call this generated overload directly. | `batch_010_helper_printed.txt`; `TagsAdapter.java:48-54` |
| `TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TagsAdapter.java:48-54` |
| `TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TagsAdapter.java:48-54` |
| `TagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload mapping absent. | `batch_010_helper_printed.txt`; `TagsAdapter.java:48-54` |
| `Scheduler.<init>` | UNREACHABLE | no_trigger_in_app | Source class is a static utility with no constructor declaration and no `new Scheduler` call; no framework registration is present in source. | `Scheduler.java:43-53`; caller probe in `batch_010_helper_printed.txt` |
| `EmptyRecyclerView.<init>(Context)` | OPEN | — | Layouts use the custom class; printed app code has no one-argument construction, but framework constructor selection was not checked against AOSP. | `EmptyRecyclerView.java:54-67`; XML refs in `batch_010_helper_printed.txt` |
| `ExpansionHeader.<init>(Context)` | OPEN | — | Layouts use the custom class; separate AttributeSet constructors exist, and dispatch to the one-argument form is unverified. | `ExpansionHeader.java:56-76`; XML refs in `batch_010_helper_printed.txt` |
| `FixHintTextInputEditText.<init>(Context)` | OPEN | — | Layouts use the custom class; separate AttributeSet constructors exist, and dispatch to the one-argument form is unverified. | `FixHintTextInputEditText.java:33-49`; XML refs in `batch_010_helper_printed.txt` |
| `RecyclerViewDividerDecoration.<init>(Context,int)` | UNREACHABLE | no_trigger_in_app | All printed app constructor calls use `RecyclerViewDividerDecoration(Drawable)`; this overload has no caller and is not a framework callback. | `RecyclerViewDividerDecoration.java:35-47`; caller probe in `batch_010_helper_printed.txt` |
| `SwitchBar.<init>(Context)` | OPEN | — | Layouts use the custom class; separate AttributeSet constructors exist, and dispatch to the one-argument form is unverified. | `SwitchBar.java:35-56`; XML refs in `batch_010_helper_printed.txt` |
| `ThemedSpeedDialView.<init>(Context)` | OPEN | — | Layout uses the custom class; separate AttributeSet constructors exist, and dispatch to the one-argument form is unverified. | `ThemedSpeedDialView.java:33-51`; XML refs in `batch_010_helper_printed.txt` |
| `PeerItem.hashCode` | OPEN | — | Override implementation is printed, but possible collection/selection-library invocation is not resolved by app source. | `PeerItem.java:26-42` |
| `FeedItemsListItem.compareTo` | OPEN | — | Comparable implementation is printed; no app call found, but library sorting use is not ruled out. | `FeedItemsListItem.java:26-48` |
| `FeedItemsListItem.hashCode` | OPEN | — | Override implementation is printed; possible collection/library invocation is not ruled out. | `FeedItemsListItem.java:26-48` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.getName` | OPEN | — | Getter body printed; no explicit app call identified, but generated binding/library usage is not ruled out. | `FileManagerSpinnerAdapter.java:51-93` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.getSize` | OPEN | — | Getter body printed; no explicit app call identified, but generated binding/library usage is not ruled out. | `FileManagerSpinnerAdapter.java:51-93` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.setName` | OPEN | — | Setter body printed; no explicit app call identified, but generated binding/library usage is not ruled out. | `FileManagerSpinnerAdapter.java:51-93` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.setSize` | OPEN | — | Setter body printed; no explicit app call identified, but generated binding/library usage is not ruled out. | `FileManagerSpinnerAdapter.java:51-93` |
| `FileManagerSpinnerAdapter$StorageSpinnerItem.setStoragePath` | OPEN | — | Setter body printed; no explicit app call identified, but generated binding/library usage is not ruled out. | `FileManagerSpinnerAdapter.java:51-93` |
| `LogSettingsFragment.newInstance` | UNREACHABLE | no_trigger_in_app | Static factory is only called within its own body to construct the fragment; no caller of the factory exists in the printed source inventory. | `LogSettingsFragment.java:36-49`; caller probe in `batch_010_helper_printed.txt` |
| `drawer.TagItem.hashCode` | OPEN | — | Override implementation is printed; possible library collection use is not ruled out. | `ui/main/drawer/TagItem.java:26-61` |
| `drawer.TagItem.toString` | OPEN | — | Override implementation is printed; possible diagnostic/library call is not ruled out. | `ui/main/drawer/TagItem.java:26-61` |

Count: 40 plan rows inspected; 3 UNREACHABLE; 37 OPEN. No coverage evidence was used.
