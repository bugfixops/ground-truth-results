# L4 verdicts — batch 1 (D13)

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 1/1 | baseAdapters.BR.<init> | OPEN | UNREACHABLE no_trigger_in_app | INFERRED | D13: constants class used only via BR.<field> reads (grep_D13_BRimports.txt: 5 files import androidx.databinding.library.baseAdapters.BR; grep_D13_BRreads.txt shows field reads only); zero `new BR(` in complete local corpus (app Java + res layouts, grep_D13_newBR.txt, 0 lines); no printed construction path (databinding library accesses BR fields, never constructs BR) | A printed `new BR(` site for the baseAdapters BR, or a printed generated/library body constructing it |
