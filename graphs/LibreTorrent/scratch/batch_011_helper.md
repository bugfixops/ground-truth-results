# LibreTorrent batch 11 helper review

Membership is only the rows where `batch=11` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. The plan has **9** rows for batch 11 (although most batches contain 40); I audited exactly those 9 and did not add members. Printed source and call-search output is in `scratch/batch_011_helper_printed.txt`.

| # | Plan method | Result | Kind / reason | Printed source / call-site evidence |
|---:|---|---|---|---|
| 1 | `SettingsFragment.newInstance()` | UNREACHABLE | `no_trigger_in_app` — no call to the factory in supplied app Java source | `ui/settings/SettingsFragment.java:47,63-70`; exact search `SettingsFragment.newInstance(` has no result |
| 2 | `SummaryPreference.<init>(Context)` | OPEN | XML contains the custom preference class; source does not establish whether AndroidX inflation invokes the one-argument overload or only its `(Context,AttributeSet)` overload | `ui/settings/customprefs/SummaryPreference.java:35-62`; `res/xml/pref_anonymous_mode.xml:8-9` |
| 3 | `SwitchBarPreference.<init>(Context)` | OPEN | XML contains the custom preference class; exact constructor dispatch depends on AndroidX preference inflater source, absent here | `ui/settings/customprefs/SwitchBarPreference.java:36-61`; `res/xml/pref_anonymous_mode.xml:3-6` |
| 4 | `TimePreference.<init>(Context)` | OPEN | XML contains this preference twice; exact constructor dispatch depends on AndroidX preference inflater source, absent here | `ui/settings/customprefs/TimePreference.java:20-58`; `res/xml/pref_scheduling.xml:11-17,26-32` |
| 5 | `AddTagButton.<init>(Context,AttributeSet)` | UNREACHABLE | `no_trigger_in_app` — no app creation with this signature and no AddTagButton XML tag | `ui/tag/AddTagButton.java:36-47`; only app creation is `new AddTagButton(context)` at `ui/tag/TorrentTagsList.java:79` |
| 6 | `AddTagButton.<init>(Context,AttributeSet,int)` | UNREACHABLE | `no_trigger_in_app` — no app creation with this signature and no AddTagButton XML tag | `ui/tag/AddTagButton.java:49-57`; exact search finds only the one-argument construction at `TorrentTagsList.java:79` |
| 7 | `tag.TagItem.hashCode()` | UNREACHABLE | `no_trigger_in_app` — app code uses `isSame`/`equals` in its adapter callbacks; no call to this override or a hash collection use was found | `ui/tag/TagItem.java:26-51`; `ui/tag/TagsAdapter.java:65-81`; exact search results in printed file |
| 8 | `tag.TagItem.toString()` | UNREACHABLE | `no_trigger_in_app` — no app call or string interpolation of a `TagItem` found | `ui/tag/TagItem.java:53-59`; exact tag package search in printed file |
| 9 | `TorrentTagsList.<init>(Context)` | UNREACHABLE | `no_trigger_in_app` — no Java construction with one argument; layout XML uses the custom-view form and the source separately defines a `(Context,AttributeSet)` overload | `ui/tag/TorrentTagsList.java:18-38`; XML at `res/layout/add_torrent_info.xml:138-141` and `res/layout/fragment_detail_torrent_info.xml:150-153` |

Totals: 9 plan members; 6 helper UNREACHABLE candidates; 3 OPEN. OPEN is retained for the three custom Preference constructors because their XML usage exists and the specific constructor callback is implemented by external AndroidX code not included in the source upload.
