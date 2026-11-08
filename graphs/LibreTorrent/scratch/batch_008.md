# LibreTorrent batch 8 source audit

Membership: exactly the 40 batch `8` rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. I independently printed all plan rows, checked the generated-class source search and read all seven DataBindingUtil call sites. Evidence: `scratch/batch_008_independent_printed.txt`; helper report and full search output: `scratch/batch_008_helper.md` and `scratch/batch_008_helper_printed.txt`.

Each listed class has the generated methods `bind(View)`, `bind(View,Object)`, `inflate(LayoutInflater)`, `inflate(LayoutInflater,ViewGroup,boolean)`, `inflate(LayoutInflater,ViewGroup,boolean,Object)`, and `inflate(LayoutInflater,Object)`, except `FragmentFeedItemsBinding`, which has only the first four methods in this plan. Source shows matching layout requests through DataBindingUtil. The generated mapper/dispatcher is absent, so source does not identify which overload executes. All rows remain OPEN; no edge or label was inferred.

| Class | Planned methods | Label | Evidence / note |
|---|---:|---|---|
| `FragmentDetailTorrentInfoBinding` | 6 | OPEN | Matching layout request at `DetailTorrentInfoFragment.java:100`; generated overload unresolved. |
| `FragmentDetailTorrentPeerListBinding` | 6 | OPEN | Matching layout request at `DetailTorrentPeersFragment.java:84`; generated overload unresolved. |
| `FragmentDetailTorrentPiecesBinding` | 6 | OPEN | Matching layout request at `DetailTorrentPiecesFragment.java:71`; generated overload unresolved. |
| `FragmentDetailTorrentStateBinding` | 6 | OPEN | Matching layout request at `DetailTorrentStateFragment.java:73`; generated overload unresolved. |
| `FragmentDetailTorrentTrackerListBinding` | 6 | OPEN | Matching layout request at `DetailTorrentTrackersFragment.java:105`; generated overload unresolved. |
| `FragmentFeedBinding` | 6 | OPEN | Matching layout request at `FeedFragment.java:99`; generated overload unresolved. |
| `FragmentFeedItemsBinding` | 4 | OPEN | Matching layout request at `FeedItemsFragment.java:111`; generated overload unresolved. |

Result: 40 plan rows reviewed; 0 labels authored; 40 remain OPEN.
