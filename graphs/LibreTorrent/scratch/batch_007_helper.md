# Batch 7 helper report

Membership was taken only from rows where `batch==7` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. The exact 40 methods and commands/output are in `scratch/batch_007_helper_printed.txt`.

The source has real app call sites through `DataBindingUtil.inflate` and typed generated binding return values. However, it does not include declarations or implementations for these generated classes, and the call sites do not name any of the static overloads listed in this batch. The generated mapper/dispatcher path is outside the printed source. Consequently, the specific method-level route cannot be confirmed, and I left every row OPEN rather than treating one overload as reached or labeling it unreachable.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater)` | OPEN | — | DataBindingUtil request uses the matching layout; generated overload dispatch unavailable. | `batch_007_helper_printed.txt`; `TagsAdapter.java:64-70` |
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; call site does not name this overload. | `batch_007_helper_printed.txt`; `TagsAdapter.java:64-70` |
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; call site does not name this overload. | `batch_007_helper_printed.txt`; `TagsAdapter.java:64-70` |
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; call site does not name this overload. | `batch_007_helper_printed.txt`; `TagsAdapter.java:64-70` |
| `DrawerNoTagsListItemBinding.bind(View)` | OPEN | — | DataBindingUtil request uses the matching layout; generated bind dispatch unavailable. | `batch_007_helper_printed.txt`; `TagsAdapter.java:82-87` |
| `DrawerNoTagsListItemBinding.bind(View,Object)` | OPEN | — | Same; source does not name this overload. | `batch_007_helper_printed.txt`; `TagsAdapter.java:82-87` |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:82-87` |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:82-87` |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:82-87` |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:82-87` |
| `DrawerTagsListItemBinding.bind(View)` | OPEN | — | DataBindingUtil request uses the matching layout; generated bind dispatch unavailable. | `batch_007_helper_printed.txt`; `TagsAdapter.java:73-79` |
| `DrawerTagsListItemBinding.bind(View,Object)` | OPEN | — | Same; source does not name this overload. | `batch_007_helper_printed.txt`; `TagsAdapter.java:73-79` |
| `DrawerTagsListItemBinding.inflate(LayoutInflater)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:73-79` |
| `DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:73-79` |
| `DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:73-79` |
| `DrawerTagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; exact generated overload not established. | `batch_007_helper_printed.txt`; `TagsAdapter.java:73-79` |
| `FragmentAddTorrentFilesBinding.bind(View)` | OPEN | — | Fragment calls DataBindingUtil.inflate for its matching layout; mapper/bind overload absent. | `batch_007_helper_printed.txt`; `AddTorrentFilesFragment.java:78-84` |
| `FragmentAddTorrentFilesBinding.bind(View,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_007_helper_printed.txt`; `AddTorrentFilesFragment.java:78-84` |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentFilesFragment.java:78-84` |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentFilesFragment.java:78-84` |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentFilesFragment.java:78-84` |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentFilesFragment.java:78-84` |
| `FragmentAddTorrentInfoBinding.bind(View)` | OPEN | — | Fragment calls DataBindingUtil.inflate for its matching layout; mapper/bind overload absent. | `batch_007_helper_printed.txt`; `AddTorrentInfoFragment.java:91-96` |
| `FragmentAddTorrentInfoBinding.bind(View,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_007_helper_printed.txt`; `AddTorrentInfoFragment.java:91-96` |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentInfoFragment.java:91-96` |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentInfoFragment.java:91-96` |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentInfoFragment.java:91-96` |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `AddTorrentInfoFragment.java:91-96` |
| `FragmentDetailTorrentBinding.bind(View)` | OPEN | — | Fragment calls DataBindingUtil.inflate for its matching layout; mapper/bind overload absent. | `batch_007_helper_printed.txt`; `DetailTorrentFragment.java:147-153` |
| `FragmentDetailTorrentBinding.bind(View,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_007_helper_printed.txt`; `DetailTorrentFragment.java:147-153` |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFragment.java:147-153` |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFragment.java:147-153` |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFragment.java:147-153` |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFragment.java:147-153` |
| `FragmentDetailTorrentFilesBinding.bind(View)` | OPEN | — | Fragment calls DataBindingUtil.inflate for its matching layout; mapper/bind overload absent. | `batch_007_helper_printed.txt`; `DetailTorrentFilesFragment.java:112-117` |
| `FragmentDetailTorrentFilesBinding.bind(View,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_007_helper_printed.txt`; `DetailTorrentFilesFragment.java:112-117` |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFilesFragment.java:112-117` |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFilesFragment.java:112-117` |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFilesFragment.java:112-117` |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; source does not name this generated overload. | `batch_007_helper_printed.txt`; `DetailTorrentFilesFragment.java:112-117` |

Count: 40 plan rows inspected; 0 labels authored; 40 OPEN. No coverage data was opened or used.
