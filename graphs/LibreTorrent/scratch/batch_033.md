# LibreTorrent batch 33 source audit

Membership is the exact 40-row set in `scratch/batch_033_plan.txt`. I checked the helper's printed definitions and focused callers in `scratch/batch_033_helper_printed.txt`. Source-local constructors, tree helpers, and UI use were found, but no complete app-entry-to-method paths composed of hand-authored graph edges exist yet. No row is conclusively no-trigger from this bounded pass. All 40 remain OPEN; no generator or coverage evidence was used.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `BencodeFileTree.<init>(String,long,int)` | OPEN | Tree builder caller (`BencodeFileTreeUtils.java:46-50`); entry route unresolved. |
| 2 | `BencodeFileTree.<init>(String,long,int,BencodeFileTree)` | OPEN | AddTorrentViewModel parent-node construction (`:411-420`); entry route unresolved. |
| 3 | `BencodeFileTree.doSelect` | OPEN | Internal selection helper called by `select` (`BencodeFileTree.java:61-83`); outer route unresolved. |
| 4 | `BencodeFileTree.isSelected` | OPEN | Definition/use search; complete entry route unresolved. |
| 5 | `BencodeFileTree.onChildSelectChange` | OPEN | Selection propagation (`BencodeFileTree.java:66-105`); entry route unresolved. |
| 6 | `BencodeFileTree.select` | OPEN | AddTorrentViewModel caller (`:426-437`); complete UI route unresolved. |
| 7 | `BencodeFileTree.selectedFileSize` | OPEN | Definition/use search; complete caller route unresolved. |
| 8 | `BencodeFileTree.toString` | OPEN | No hand-authored string-conversion route established. |
| 9 | `FileNode$Type.<clinit>` | OPEN | Static fields and builder references at `FileNode.java:30-35`; entry route unresolved. |
| 10 | `FilePriority.<init>(Priority)` | OPEN | DetailTorrentViewModel caller (`:547-550`); full UI route unresolved. |
| 11 | `FilePriority.<init>(Type)` | OPEN | DetailTorrentFilesFragment callers (`:354,486-495`); full UI route unresolved. |
| 12 | `FilePriority.equals` | OPEN | Definition/use search; no complete route established. |
| 13 | `FilePriority.getPriority` | OPEN | DetailTorrentViewModel caller (`:420`); entry route unresolved. |
| 14 | `FilePriority.getType` | OPEN | Detail ViewModel/adapter callers; full route unresolved. |
| 15 | `FilePriority.priorityFrom` | OPEN | Private mapping helper at `FilePriority.java:58-90`; outer route unresolved. |
| 16 | `FilePriority.toString` | OPEN | No hand-authored string-conversion route established. |
| 17 | `FilePriority.typeFrom` | OPEN | Helper called by constructor (`FilePriority.java:36-40,58-75`); outer route unresolved. |
| 18 | `FilePriority$Type.<clinit>` | OPEN | Enum use appears in UI; complete entry route unresolved. |
| 19 | `FileTree.<clinit>` | OPEN | Static constants and builder use (`FileTree.java:38-42`); entry route unresolved. |
| 20 | `FileTree.<init>(int,String,long,int,FileTree)` | OPEN | Used via BencodeFileTree/tree builder (`FileTree.java:61-73`; `BencodeFileTree.java:40-43`; builder `:119-125`); entry route unresolved. |
| 21 | `FileTree.<init>(String,long,int)` | OPEN | Used via BencodeFileTree root constructor and builder (`FileTree.java:51-54`; builder `:46-50`); entry route unresolved. |
| 22 | `FileTree.<init>(String,long,int,FileTree)` | OPEN | Used via BencodeFileTree parent constructor (`FileTree.java:56-59`; `BencodeFileTree.java:45-48`); entry route unresolved. |
| 23 | `FileTree.addChild` | OPEN | Called by tree builder (`FileTree.java:75-78`; `BencodeFileTreeUtils.java:46-115`); UI entry route unresolved. |
| 24 | `FileTree.compareTo` | OPEN | Definition at `FileTree.java:187-191`; no comparator route established. |
| 25 | `FileTree.contains` | OPEN | Definition/use search; complete caller route unresolved. |
| 26 | `FileTree.equals` | OPEN | Definition at `FileTree.java:193-209`; no complete app route established. |
| 27 | `FileTree.getChild` | OPEN | Tree builder and AddTorrentViewModel callers; entry route unresolved. |
| 28 | `FileTree.getChildren` | OPEN | UI/ViewModel caller evidence; complete route unresolved. |
| 29 | `FileTree.getChildrenCount` | OPEN | Definition/use search; caller route unresolved. |
| 30 | `FileTree.getChildrenIndexes` | OPEN | Definition/use search; caller route unresolved. |
| 31 | `FileTree.getChildrenName` | OPEN | Definition/use search; caller route unresolved. |
| 32 | `FileTree.getIndex` | OPEN | Definition/use search; caller route unresolved. |
| 33 | `FileTree.getName` | OPEN | Definition/use search; caller route unresolved. |
| 34 | `FileTree.getParent` | OPEN | AddTorrentViewModel navigation caller (`:418`); full UI route unresolved. |
| 35 | `FileTree.getPath` | OPEN | Definition/use search; caller route unresolved. |
| 36 | `FileTree.getType` | OPEN | Definition/use search; caller route unresolved. |
| 37 | `FileTree.isFile` | OPEN | Definition/use search; caller route unresolved. |
| 38 | `FileTree.setIndex` | OPEN | Definition/use search; complete setter route unresolved. |
| 39 | `FileTree.setName` | OPEN | Definition/use search; complete setter route unresolved. |
| 40 | `FileTree.setParent` | OPEN | Definition/use search; complete setter route unresolved. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
