# LibreTorrent batch 5 source audit

Membership is exactly the 40 rows with batch `5` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. I independently rechecked the plan rows, the source-root generated-class grep, and the five DataBindingUtil call sites. Printed evidence: `scratch/batch_005_independent_printed.txt`; helper search and command output: `scratch/batch_005_helper_printed.txt`.

The grep command required by rule F returned no class declarations for these generated binding classes. The app requests five layouts through `DataBindingUtil`, but the source does not show generated mapper dispatch or identify which listed binding overload executes. The remaining binding classes have no direct app source reference. Absence of generated declarations in the Java source tree is not enough to label their methods unreachable. All rows stay OPEN pending the generated binding implementation or other allowed source evidence.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `ActivityAddTorrentBinding.bind(View)` | OPEN | — | Generated overload dispatch absent; DataBindingUtil requests its layout at `AddTorrentActivity.java:102`. | `scratch/batch_005_independent_printed.txt` |
| `ActivityAddTorrentBinding.bind(View,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityAddTorrentBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityFilemanagerDialogBinding.bind(View)` | OPEN | — | Generated overload dispatch absent; DataBindingUtil requests its layout at `FileManagerDialog.java:142`. | `scratch/batch_005_independent_printed.txt` |
| `ActivityFilemanagerDialogBinding.bind(View,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityFilemanagerDialogBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityLogBinding.bind(View)` | OPEN | — | Generated overload dispatch absent; DataBindingUtil requests its layout at `LogActivity.java:93`. | `scratch/batch_005_independent_printed.txt` |
| `ActivityLogBinding.bind(View,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityLogBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `ActivityLogBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `AddTorrentInfoBinding.bind(View)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `AddTorrentInfoBinding.bind(View,Object)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `AddTorrentInfoBinding.inflate(LayoutInflater)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `AddTorrentInfoBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DetailTorrentAppbarBinding.bind(View)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DetailTorrentAppbarBinding.bind(View,Object)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DetailTorrentAppbarBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated class is absent from supplied source; call/dispatch not established. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddFeedChannelBinding.bind(View)` | OPEN | — | Generated overload dispatch absent; DataBindingUtil requests its layout at `AddFeedDialog.java:202`. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddFeedChannelBinding.bind(View,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddFeedChannelBinding.inflate(LayoutInflater,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddLinkBinding.bind(View)` | OPEN | — | Generated overload dispatch absent; DataBindingUtil requests its layout at `AddLinkDialog.java:184`. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddLinkBinding.bind(View,Object)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddLinkBinding.inflate(LayoutInflater)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |
| `DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Generated overload dispatch absent. | `scratch/batch_005_independent_printed.txt` |

Result: 40 rows reviewed; 0 labels authored; 40 OPEN. Do not mark these methods unreachable solely because their generated class files are absent from the supplied source tree.
