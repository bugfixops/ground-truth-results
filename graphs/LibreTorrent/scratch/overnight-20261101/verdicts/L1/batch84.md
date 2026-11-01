# L1 verdicts — batch 84 (hashCode/toString, D30 execution)
Scope key: see batch3.md header (same greps/L1/ set).
| batch/row | method | old label | NEW label | confirmed_by | evidence (file:line or grep path) | revert condition |
| 84/30 | CreateTorrentMutableParams.toString | OPEN | UNREACHABLE | INFERRED | Def ui/createtorrent/CreateTorrentMutableParams.java:174-190. Zero outside trigger in grep_all_calls.txt, grep_log_concat.txt, grep_getstring_formatargs.txt, grep_databinding_text.txt, grep_layout_types.txt; CreateTorrent logging sites log exceptions/version only (ViewModel:347/:402, Dialog:353/:474); layouts bind mutableParams.* fields (dialog_create_torrent.xml seedPathName) never the whole object. No plausible unprinted dispatcher | Any printed trigger flips to REACHABLE |
