# LibreTorrent batch 11 source audit

Membership: exactly the 9 rows with batch `11` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. Independent app-source and plan output is in `scratch/batch_011_independent_printed.txt`; the AOSP constructor-dispatch lines are in `scratch/batch_011_framework_printed.txt`; the helper's supporting printout is `scratch/batch_011_helper_printed.txt`.

| Method | Label | Kind | Reason | Printed file:lines |
|---|---|---|---|---|
| `SettingsFragment.newInstance` | UNREACHABLE | no_trigger_in_app | No app source caller of this factory. | `ui/settings/SettingsFragment.java:63-70`; exact caller search in `scratch/batch_011_independent_printed.txt` |
| `SummaryPreference.<init>(Context)` | OPEN | — | XML uses the preference class; AndroidX constructor dispatch is absent from supplied source. | `ui/settings/customprefs/SummaryPreference.java:35-62`; `res/xml/pref_anonymous_mode.xml:8-9` in `scratch/batch_011_helper_printed.txt` |
| `SwitchBarPreference.<init>(Context)` | OPEN | — | XML uses the preference class; AndroidX constructor dispatch is absent from supplied source. | `ui/settings/customprefs/SwitchBarPreference.java:36-61`; `res/xml/pref_anonymous_mode.xml:3-6` in `scratch/batch_011_helper_printed.txt` |
| `TimePreference.<init>(Context)` | OPEN | — | XML uses the preference class; AndroidX constructor dispatch is absent from supplied source. | `ui/settings/customprefs/TimePreference.java:20-58`; `res/xml/pref_scheduling.xml:11-17,26-32` in `scratch/batch_011_helper_printed.txt` |
| `AddTagButton.<init>(Context,AttributeSet)` | UNREACHABLE | no_trigger_in_app | App constructs AddTagButton with one Context argument; no AddTagButton XML tag exists. | `ui/tag/AddTagButton.java:36-47`; `ui/tag/TorrentTagsList.java:78-86`; caller output in `scratch/batch_011_independent_printed.txt` |
| `AddTagButton.<init>(Context,AttributeSet,int)` | UNREACHABLE | no_trigger_in_app | No app call with this signature and no XML tag invokes the custom view. | `ui/tag/AddTagButton.java:49-57`; caller output in `scratch/batch_011_independent_printed.txt` |
| `tag.TagItem.hashCode` | UNREACHABLE | no_trigger_in_app | App's DiffUtil callbacks use `isSame` and `equals`; no app hash-based use or direct invocation is present. | `ui/tag/TagItem.java:34-51`; `ui/tag/TagsAdapter.java:65-81`; searches in `scratch/batch_011_independent_printed.txt` |
| `tag.TagItem.toString` | UNREACHABLE | no_trigger_in_app | No app invocation/string interpolation of this type is present. | `ui/tag/TagItem.java:53-59`; search output in `scratch/batch_011_independent_printed.txt` |
| `TorrentTagsList.<init>(Context)` | UNREACHABLE | no_trigger_in_app | XML inflation invokes the `(Context,AttributeSet)` constructor; no app source constructs the one-argument overload. | `ui/tag/TorrentTagsList.java:23-33`; `FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,639-647` |

Result: 9 plan rows reviewed; 6 source-supported UNREACHABLE labels and 3 OPEN.
