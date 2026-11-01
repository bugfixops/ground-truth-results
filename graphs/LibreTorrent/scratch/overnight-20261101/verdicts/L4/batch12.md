# L4 verdicts — batch 12 (D13/D8)

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 12/1 | databinding.DataBinderMapperImpl.<init> | OPEN | OPEN | — | verified, no change — superclass link MISSING: zero `extends`/`super(` lines in the batch-12 and batch-17 files, and no generated mapper source printed for either class, so no printed evidence that the libretorrent mapper extends the databinding mapper; batch-17 <init> REACHABLE (D8) does not transfer across packages (D8 no-transfer rule) | A printed generated body showing libretorrent DataBinderMapperImpl extends databinding DataBinderMapperImpl (→ REACHABLE INFERRED via super() from the REACHABLE libretorrent mapper <init>), or a printed databinding-mapper dispatch site |
