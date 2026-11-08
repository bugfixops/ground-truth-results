# Batch 8 helper report

Membership is the exact 40 rows with `batch==8` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the method list and source printout are saved in `scratch/batch_008_helper_printed.txt`.

The source confirms the app requests these layouts with `DataBindingUtil.inflate` and holds typed generated binding results. The required grep over the listed Java source root returned no generated class declarations. The generated method bodies and DataBinding mapper/dispatcher are not in the printed source, so the source does not identify which listed overloads execute. All 40 remain OPEN. No coverage evidence was used.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `FragmentDetailTorrentInfoBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `DetailTorrentInfoFragment.java:100` |
| `FragmentDetailTorrentInfoBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `DetailTorrentInfoFragment.java:100` |
| `FragmentDetailTorrentInfoBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `DetailTorrentInfoFragment.java:100` |
| `FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentInfoFragment.java:100` |
| `FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentInfoFragment.java:100` |
| `FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentInfoFragment.java:100` |
| `FragmentDetailTorrentPeerListBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `DetailTorrentPeersFragment.java:84` |
| `FragmentDetailTorrentPeerListBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `DetailTorrentPeersFragment.java:84` |
| `FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `DetailTorrentPeersFragment.java:84` |
| `FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentPeersFragment.java:84` |
| `FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentPeersFragment.java:84` |
| `FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentPeersFragment.java:84` |
| `FragmentDetailTorrentPiecesBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `DetailTorrentPiecesFragment.java:71` |
| `FragmentDetailTorrentPiecesBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `DetailTorrentPiecesFragment.java:71` |
| `FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `DetailTorrentPiecesFragment.java:71` |
| `FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentPiecesFragment.java:71` |
| `FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentPiecesFragment.java:71` |
| `FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentPiecesFragment.java:71` |
| `FragmentDetailTorrentStateBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `DetailTorrentStateFragment.java:73` |
| `FragmentDetailTorrentStateBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `DetailTorrentStateFragment.java:73` |
| `FragmentDetailTorrentStateBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `DetailTorrentStateFragment.java:73` |
| `FragmentDetailTorrentStateBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentStateFragment.java:73` |
| `FragmentDetailTorrentStateBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentStateFragment.java:73` |
| `FragmentDetailTorrentStateBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentStateFragment.java:73` |
| `FragmentDetailTorrentTrackerListBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `DetailTorrentTrackersFragment.java:105` |
| `FragmentDetailTorrentTrackerListBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `DetailTorrentTrackersFragment.java:105` |
| `FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `DetailTorrentTrackersFragment.java:105` |
| `FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentTrackersFragment.java:105` |
| `FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentTrackersFragment.java:105` |
| `FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `DetailTorrentTrackersFragment.java:105` |
| `FragmentFeedBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `FeedFragment.java:99` |
| `FragmentFeedBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `FeedFragment.java:99` |
| `FragmentFeedBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `FeedFragment.java:99` |
| `FragmentFeedBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `FeedFragment.java:99` |
| `FragmentFeedBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `FeedFragment.java:99` |
| `FragmentFeedBinding.inflate(LayoutInflater,Object)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `FeedFragment.java:99` |
| `FragmentFeedItemsBinding.bind(View)` | OPEN | — | Layout request exists, but generated bind dispatch is not in source. | `batch_008_helper_printed.txt`; `FeedItemsFragment.java:111` |
| `FragmentFeedItemsBinding.bind(View,Object)` | OPEN | — | Same; overload not identified at the call site. | `batch_008_helper_printed.txt`; `FeedItemsFragment.java:111` |
| `FragmentFeedItemsBinding.inflate(LayoutInflater)` | OPEN | — | Same; call site invokes DataBindingUtil, not this overload. | `batch_008_helper_printed.txt`; `FeedItemsFragment.java:111` |
| `FragmentFeedItemsBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | — | Same; generated overload dispatch unavailable. | `batch_008_helper_printed.txt`; `FeedItemsFragment.java:111` |

Count: 40 plan rows inspected; 0 labels authored; 40 OPEN.
