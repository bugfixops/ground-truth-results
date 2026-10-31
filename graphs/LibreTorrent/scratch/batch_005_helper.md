# Batch 5 helper report

Membership source: only the 40 `batch==5` rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (the exact command and full output are saved in `scratch/batch_005_helper_printed.txt`). No other batch rows were used.

All rows remain **OPEN**. The listed classes are generated data-binding classes; the mandated real grep over the listed source root found no class declarations. Source confirms several `DataBindingUtil` requests for layouts whose generated binding type matches these names, but it does not show the generated mapper/implementation or identify which overload of the listed generated APIs the library invokes. The code that would resolve that is generated or library code not in this source root. The source evidence therefore does not support a specific hand-written edge per overload, and lack of a Java declaration is not sufficient to call the methods `no_trigger_in_app`.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `ActivityAddTorrentBinding.bind(View)` | OPEN | — | DataBindingUtil call exists, but generated dispatch/overload not printed. | `batch_005_helper_printed.txt`; `AddTorrentActivity.java:102` |
| `ActivityAddTorrentBinding.bind(View,Object)` | OPEN | — | Same; exact generated overload invocation unknown. | `batch_005_helper_printed.txt`; `AddTorrentActivity.java:102` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddTorrentActivity.java:102` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddTorrentActivity.java:102` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddTorrentActivity.java:102` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddTorrentActivity.java:102` |
| `ActivityFilemanagerDialogBinding.bind(View)` | OPEN | — | DataBindingUtil call exists, but generated dispatch/overload not printed. | `batch_005_helper_printed.txt`; `FileManagerDialog.java:142` |
| `ActivityFilemanagerDialogBinding.bind(View,Object)` | OPEN | — | Same; exact generated overload invocation unknown. | `batch_005_helper_printed.txt`; `FileManagerDialog.java:142` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `FileManagerDialog.java:142` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `FileManagerDialog.java:142` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `FileManagerDialog.java:142` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `FileManagerDialog.java:142` |
| `ActivityLogBinding.bind(View)` | OPEN | — | DataBindingUtil call exists, but generated dispatch/overload not printed. | `batch_005_helper_printed.txt`; `LogActivity.java:93` |
| `ActivityLogBinding.bind(View,Object)` | OPEN | — | Same; exact generated overload invocation unknown. | `batch_005_helper_printed.txt`; `LogActivity.java:93` |
| `ActivityLogBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `LogActivity.java:93` |
| `ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `LogActivity.java:93` |
| `ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `LogActivity.java:93` |
| `ActivityLogBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `LogActivity.java:93` |
| `AddTorrentInfoBinding.bind(View)` | OPEN | — | No class declaration or direct app source reference found; generated mapping/source needed to distinguish unused from library-dispatched. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `AddTorrentInfoBinding.bind(View,Object)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `AddTorrentInfoBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `AddTorrentInfoBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DetailTorrentAppbarBinding.bind(View)` | OPEN | — | No class declaration or direct app source reference found; generated mapping/source needed to distinguish unused from library-dispatched. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DetailTorrentAppbarBinding.bind(View,Object)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; no source evidence for an overload route or its absence. | `batch_005_helper_printed.txt` (source-root grep: no match) |
| `DialogAddFeedChannelBinding.bind(View)` | OPEN | — | DataBindingUtil inflate call exists, but generated dispatch/overload not printed. | `batch_005_helper_printed.txt`; `AddFeedDialog.java:202` |
| `DialogAddFeedChannelBinding.bind(View,Object)` | OPEN | — | Same; exact generated overload invocation unknown. | `batch_005_helper_printed.txt`; `AddFeedDialog.java:202` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddFeedDialog.java:202` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddFeedDialog.java:202` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddFeedDialog.java:202` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddFeedDialog.java:202` |
| `DialogAddLinkBinding.bind(View)` | OPEN | — | DataBindingUtil inflate call exists, but generated dispatch/overload not printed. | `batch_005_helper_printed.txt`; `AddLinkDialog.java:184` |
| `DialogAddLinkBinding.bind(View,Object)` | OPEN | — | Same; exact generated overload invocation unknown. | `batch_005_helper_printed.txt`; `AddLinkDialog.java:184` |
| `DialogAddLinkBinding.inflate(LayoutInflater)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddLinkDialog.java:184` |
| `DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; no source evidence that this overload executes. | `batch_005_helper_printed.txt`; `AddLinkDialog.java:184` |

Count: 40 plan rows inspected; 0 labels authored; 40 OPEN. The printed source call sites provide leads for the next pass, but neither generator output nor presumed data-binding internals were used as evidence.
