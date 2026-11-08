# L1 verdicts — batch 106 (hashCode/toString, D30 execution)
Scope key: see batch3.md header (same greps/L1/ set).
| batch/row | method | old label | NEW label | confirmed_by | evidence (file:line or grep path) | revert condition |
| 106/40 | LogMutableParams.toString | OPEN | UNREACHABLE | INFERRED | Def ui/log/LogMutableParams.java:110-120. Zero outside trigger in grep_all_calls.txt, grep_log_concat.txt, grep_getstring_formatargs.txt, grep_databinding_text.txt, grep_layout_types.txt; LogViewModel mutableParams is field/getter use only; LogActivity/LogAdapter/LogDataSource log LogEntry objects (already-REACHABLE row), never LogMutableParams. No plausible unprinted dispatcher | Any printed trigger flips to REACHABLE |
