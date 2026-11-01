# R5 grep commands (corpus = ~/workspace/overnight/stream-A/corpus/java, 281 files; C=$corpus)
# All outputs below were produced with grep -rn over $C (plus other-sourcesets-src where noted) and teed to these files.
- row30_16_17_callers.txt: grep -n "TorrentStateCode.fromValue|stateCode.value()" TorrentInfo.java; grep -n "ev.value()" TorrentStateCode.java
- new_AdvancedTorrentInfo.txt: grep -rn "new AdvancedTorrentInfo" $C
- getUri.txt: grep -rn "\.getUri\s*(" $C
- new_Torrent.txt: grep -rn "new Torrent(" $C
- setters_getters_addItem.txt: grep -rn "\.setIndex(|\.setPath(|\.setSize(|\.setName(|\.setType(|\.setEnabled(|\.setFragment(|\.setTitle(|\.getChildrenIndexes(|\.getChildrenName(|\.getType(|\.addItem(" $C
- compareTo_sort.txt: grep -rn "\.compareTo(|Collections\.sort|\.sort(|sorted(" $C
- super_noarg.txt: grep -rn "super()" $C/core/model/data/*.java $C/core/model/data/metainfo/*.java
- other_sourcesets_new.txt: grep -rn "new AdvancedTorrentInfo|new Torrent(" other-sourcesets-src
- equals_contains_triage.txt: grep -rn "\.equals(|containsAll(|\.contains(|indexOf(" $C | grep -i "torrenttag|torrentmetainfo|filetree|Torrent\b"
- equals_other.txt: grep -rn "\.equals(" $C (filtered display)
- filetree_contains.txt: grep -rn "boolean contains|contains(" $C/core/model/filetree/*.java
- filetree_getType.txt: grep -rn "\.getType()" $C/core/model/filetree/
- misc_methods.txt: grep -rn "getUri|addItem|setFragment|getChildren|setIndex|setPath|setSize" $C other-sourcesets-src
- setParent.txt: grep -rn "\.setParent(" $C
- Reused (not re-run): phase3/greps/L2/grep_all_parcel_sites.txt, grep_storage_sites.txt, Parcel_8.1 excerpt (via L2/batch30.md, L2/batch28.md, L2/batch114.md).
