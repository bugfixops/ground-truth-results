# L1 verdicts — batch 81 (hashCode/toString, D30 execution)
Scope key: see batch3.md header (same greps/L1/ set).
| batch/row | method | old label | NEW label | confirmed_by | evidence (file:line or grep path) | revert condition |
| 81/2 | AddTorrentMutableParams.toString ()Ljava/lang/String; | OPEN | UNREACHABLE | INFERRED | Def ui/addtorrent/AddTorrentMutableParams.java:156-170. Zero outside trigger in grep_all_calls.txt, grep_log_concat.txt, grep_getstring_formatargs.txt, grep_databinding_text.txt, grep_layout_types.txt; AddTorrentViewModel mutableParams uses are getter/setter/field uses only; layouts bind mutableParams.* fields (e.g. add_torrent_info.xml dirName) never the whole object. No plausible unprinted dispatcher | Any printed trigger flips to REACHABLE |
