# Batch 33 helper report

Membership is exactly the 40 rows with `batch==33` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; that plan is the sole membership source. Definitions and focused caller excerpts are referenced in `scratch/batch_033_helper_printed.txt`. I leave a method OPEN when the inspected material does not establish an entry-to-method route or a well-supported UNREACHABLE classification.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `BencodeFileTree.<init>(String,long,int)` | OPEN | — | Constructed in the file-tree builder, but complete entry route not established. | `BencodeFileTree.java:35-38`; `BencodeFileTreeUtils.java:46-50` |
| `BencodeFileTree.<init>(String,long,int,BencodeFileTree)` | OPEN | — | Used for parent-directory nodes in AddTorrentViewModel; full entry route not established. | `BencodeFileTree.java:45-48`; `AddTorrentViewModel.java:411-420` |
| `BencodeFileTree.doSelect` | OPEN | — | Internal helper called by select; entry route remains unestablished. | `BencodeFileTree.java:61-83` |
| `BencodeFileTree.isSelected` | OPEN | — | Definition read; no complete entry route established. | `BencodeFileTree.java:50-53`; focused usage search |
| `BencodeFileTree.onChildSelectChange` | OPEN | — | Called by selection propagation; full route not established. | `BencodeFileTree.java:66-105` |
| `BencodeFileTree.select` | OPEN | — | Definition read; UI caller route is not fully established. | `BencodeFileTree.java:61-64`; `AddTorrentViewModel.java:426-437` |
| `BencodeFileTree.selectedFileSize` | OPEN | — | Definition read; no complete caller route established. | `BencodeFileTree.java:107-123`; focused usage search |
| `BencodeFileTree.toString` | OPEN | — | No hand-written string conversion route established. | `BencodeFileTree.java:125-133`; focused usage search |
| `FileNode$Type.<clinit>` | OPEN | — | Static fields are present; class initialization entry route not established. | `FileNode.java:30-35`; builder call sites |
| `FilePriority.<init>(Priority)` | OPEN | — | DetailTorrentViewModel constructs from priorities; complete entry route not established. | `FilePriority.java:36-40`; `DetailTorrentViewModel.java:547-550` |
| `FilePriority.<init>(Type)` | OPEN | — | UI constructs from selected priority types; complete entry route not established. | `FilePriority.java:42-46`; `DetailTorrentFilesFragment.java:354,486-495` |
| `FilePriority.equals` | OPEN | — | No hand-written equality call route established. | `FilePriority.java:92-105`; focused usage search |
| `FilePriority.getPriority` | OPEN | — | Called by the detail ViewModel; complete entry route not established. | `FilePriority.java:48-51`; `DetailTorrentViewModel.java:420` |
| `FilePriority.getType` | OPEN | — | Called by the detail UI and model; full entry route not established. | `FilePriority.java:53-56`; `DetailTorrentViewModel.java:308`; `TorrentContentFilesAdapter.java:234` |
| `FilePriority.priorityFrom` | OPEN | — | Private helper mapping enum type; full entry route not established. | `FilePriority.java:58-90` |
| `FilePriority.toString` | OPEN | — | No hand-written string conversion route established. | `FilePriority.java:107-113`; focused usage search |
| `FilePriority.typeFrom` | OPEN | — | Private helper used by the Priority constructor; full entry route not established. | `FilePriority.java:36-40,58-75` |
| `FilePriority$Type.<clinit>` | OPEN | — | Enum initialization is visible; complete entry route not established. | `FilePriority.java:34`; selected UI uses enum constants |
| `FileTree.<clinit>` | OPEN | — | Static constants are present; complete class initialization route not established. | `FileTree.java:38-42`; tree builder call sites |
| `FileTree.<init>(int,String,long,int,FileTree)` | OPEN | — | Used through BencodeFileTree subclass and tree builder, but complete entry route not established. | `FileTree.java:61-73`; `BencodeFileTree.java:40-43`; `BencodeFileTreeUtils.java:119-125` |
| `FileTree.<init>(String,long,int)` | OPEN | — | Used through BencodeFileTree root construction; complete entry route not established. | `FileTree.java:51-54`; `BencodeFileTree.java:35-38`; `BencodeFileTreeUtils.java:46-50` |
| `FileTree.<init>(String,long,int,FileTree)` | OPEN | — | Used through subclass parent-node constructors; complete entry route not established. | `FileTree.java:56-59`; `BencodeFileTree.java:45-48` |
| `FileTree.addChild` | OPEN | — | Used by tree-building code; complete entry route not established. | `FileTree.java:75-78`; `BencodeFileTreeUtils.java:46-115` |
| `FileTree.compareTo` | OPEN | — | No source comparator call route established. | `FileTree.java:187-191`; focused usage search |
| `FileTree.contains` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:80-83`; focused usage search |
| `FileTree.equals` | OPEN | — | No hand-written equality call route established. | `FileTree.java:193-209`; focused usage search |
| `FileTree.getChild` | OPEN | — | Used by tree builder and ViewModel; full entry route not established. | `FileTree.java:85-88`; `BencodeFileTreeUtils.java:109`; `AddTorrentViewModel.java:426-437` |
| `FileTree.getChildren` | OPEN | — | Used by UI/ViewModel patterns; complete route not established. | `FileTree.java:90-93`; focused usage search |
| `FileTree.getChildrenCount` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:110-113`; focused usage search |
| `FileTree.getChildrenIndexes` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:100-108`; focused usage search |
| `FileTree.getChildrenName` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:95-98`; focused usage search |
| `FileTree.getIndex` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:142-150`; focused usage search |
| `FileTree.getName` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:131-140`; focused usage search |
| `FileTree.getParent` | OPEN | — | Used by ViewModel directory navigation; full entry route not established. | `FileTree.java:120-123`; `AddTorrentViewModel.java:418` |
| `FileTree.getPath` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:173-185`; focused usage search |
| `FileTree.getType` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:153-157`; focused usage search |
| `FileTree.isFile` | OPEN | — | Definition read; complete caller route not established. | `FileTree.java:115-118`; focused usage search |
| `FileTree.setIndex` | OPEN | — | Definition read; no complete setter route established. | `FileTree.java:142-145`; focused usage search |
| `FileTree.setName` | OPEN | — | Definition read; no complete setter route established. | `FileTree.java:131-134`; focused usage search |
| `FileTree.setParent` | OPEN | — | Definition read; no complete setter route established. | `FileTree.java:125-128`; focused usage search |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
