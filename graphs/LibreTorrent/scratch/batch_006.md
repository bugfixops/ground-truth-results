# LibreTorrent batch 6 source audit

Membership: exactly the 40 rows with batch `6` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. I independently printed the rows, checked the generated binding source search, and read the app call sites. Evidence is in `scratch/batch_006_independent_printed.txt`; the helper's full 40-row table and call-site output are in `scratch/batch_006_helper.md` and `scratch/batch_006_helper_printed.txt`.

These methods are generated Data Binding APIs. Source calls `DataBindingUtil.inflate(...)` for layouts, but the generated mapper and overload dispatch are absent. Direct app source calls to the target generated methods were not found. Per rules A and F, the layout request does not establish which target overload executes, and missing generated source is not evidence of no trigger. No labels or edges were authored.

| Plan method | Label | Reason |
|---|---|---|
| `DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent; source layout request at `AddLinkDialog.java:184`. |
| `DialogAddLinkBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogAddTagBinding.bind(View)` | OPEN | DataBindingUtil layout request at `AddTagDialog.java:128`; target overload unknown. |
| `DialogAddTagBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogAddTagBinding.inflate(LayoutInflater)` | OPEN | Generated overload dispatch absent. |
| `DialogAddTagBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Generated overload dispatch absent. |
| `DialogAddTagBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogAddTagBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogCreateTorrentBinding.bind(View)` | OPEN | DataBindingUtil layout request at `CreateTorrentDialog.java:185`; target overload unknown. |
| `DialogCreateTorrentBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogCreateTorrentBinding.inflate(LayoutInflater)` | OPEN | Generated overload dispatch absent. |
| `DialogCreateTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Generated overload dispatch absent. |
| `DialogCreateTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogCreateTorrentBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogErrorBinding.bind(View)` | OPEN | DataBindingUtil layout request at `ErrorReportDialog.java:68`; target overload unknown. |
| `DialogErrorBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogErrorBinding.inflate(LayoutInflater)` | OPEN | Generated overload dispatch absent. |
| `DialogErrorBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Generated overload dispatch absent. |
| `DialogErrorBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogErrorBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogGoToFolderBinding.bind(View)` | OPEN | DataBindingUtil layout request at `GoToFolderDialog.java:99`; target overload unknown. |
| `DialogGoToFolderBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogGoToFolderBinding.inflate(LayoutInflater)` | OPEN | Generated overload dispatch absent. |
| `DialogGoToFolderBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Generated overload dispatch absent. |
| `DialogGoToFolderBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogGoToFolderBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogLogFilterBinding.bind(View)` | OPEN | DataBindingUtil layout request at `SessionLogFilterDialog.java:98`; target overload unknown. |
| `DialogLogFilterBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogLogFilterBinding.inflate(LayoutInflater)` | OPEN | Generated overload dispatch absent. |
| `DialogLogFilterBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Generated overload dispatch absent. |
| `DialogLogFilterBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogLogFilterBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogSelectTagBinding.bind(View)` | OPEN | DataBindingUtil layout request at `SelectTagDialog.java:128`; target overload unknown. |
| `DialogSelectTagBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogSelectTagBinding.inflate(LayoutInflater)` | OPEN | Generated overload dispatch absent. |
| `DialogSelectTagBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Generated overload dispatch absent. |
| `DialogSelectTagBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Generated overload dispatch absent. |
| `DialogSelectTagBinding.inflate(LayoutInflater,Object)` | OPEN | Generated overload dispatch absent. |
| `DrawerEmptyTagsListItemBinding.bind(View)` | OPEN | DataBindingUtil layout request in the `TYPE_EMPTY_ITEM` branch at `TagsAdapter.java:63-70`; mapper dispatch unknown. |
| `DrawerEmptyTagsListItemBinding.bind(View,Object)` | OPEN | Generated overload dispatch absent. |

Result: 40 rows reviewed; 0 labels authored; 40 remain OPEN.
