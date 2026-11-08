# LibreTorrent batch 7 source audit

Membership: exactly the 40 batch `7` rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. I independently read the plan rows, generated-class search and app call sites. Printed evidence is in `scratch/batch_007_helper_printed.txt`; the independent source print is `scratch/batch_007_independent_printed.txt`.

These are generated Data Binding methods. The app calls `DataBindingUtil.inflate` for matching layouts, but the generated binding mapper/dispatcher and implementation are absent from supplied Java source. These calls do not identify which overload below executes. I left all entries OPEN; the lack of generated Java source is not evidence of `no_trigger_in_app`.

| Method | Label | Reason |
|---|---|---|
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater)` | OPEN | Matching layout request at `TagsAdapter.java:64-70`; generated dispatch absent. |
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |
| `DrawerNoTagsListItemBinding.bind(View)` | OPEN | Matching layout request at `TagsAdapter.java:82-87`; generated dispatch absent. |
| `DrawerNoTagsListItemBinding.bind(View,Object)` | OPEN | Same; overload not identified. |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater)` | OPEN | Same; overload not identified. |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `DrawerNoTagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |
| `DrawerTagsListItemBinding.bind(View)` | OPEN | Matching layout request at `TagsAdapter.java:73-79`; generated dispatch absent. |
| `DrawerTagsListItemBinding.bind(View,Object)` | OPEN | Same; overload not identified. |
| `DrawerTagsListItemBinding.inflate(LayoutInflater)` | OPEN | Same; overload not identified. |
| `DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `DrawerTagsListItemBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentFilesBinding.bind(View)` | OPEN | Matching layout request at `AddTorrentFilesFragment.java:81`; generated dispatch absent. |
| `FragmentAddTorrentFilesBinding.bind(View,Object)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentFilesBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentInfoBinding.bind(View)` | OPEN | Matching layout request at `AddTorrentInfoFragment.java:93`; generated dispatch absent. |
| `FragmentAddTorrentInfoBinding.bind(View,Object)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `FragmentAddTorrentInfoBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentBinding.bind(View)` | OPEN | Matching layout request at `DetailTorrentFragment.java:150`; generated dispatch absent. |
| `FragmentDetailTorrentBinding.bind(View,Object)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentFilesBinding.bind(View)` | OPEN | Matching layout request at `DetailTorrentFilesFragment.java:114`; generated dispatch absent. |
| `FragmentDetailTorrentFilesBinding.bind(View,Object)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; overload not identified. |
| `FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,Object)` | OPEN | Same; overload not identified. |

Result: 40 plan rows reviewed; 0 labels authored; 40 remain OPEN.
