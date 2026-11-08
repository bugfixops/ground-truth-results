# L4 verdicts — batch 17 (D8)

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 17/36 | libretorrent.DataBinderMapperImpl.collectDependencies | OPEN | OPEN | — | verified, no change — runtime-API method with no printed caller: grep_D13_1736.txt (0 hits for collectDependencies/convertBrIdToString in app Java); D8 M-dispatch covers the inflate path only, not runtime-API methods | A printed generated dispatch or app caller for collectDependencies |
| 17/37 | libretorrent.DataBinderMapperImpl.convertBrIdToString | OPEN | OPEN | — | verified, no change — same as 17/36: grep_D13_1736.txt, 0 hits; runtime-API method, not on the inflate path under D8 | A printed generated dispatch or app caller for convertBrIdToString |
