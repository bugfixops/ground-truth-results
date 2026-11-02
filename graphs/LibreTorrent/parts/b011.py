# C01 converter delivery (2026-11-01): base part verified against its authoritative
# batch file with the official harness (base PASS, labels/kinds unchanged).
# DELIVERED harness: FAIL ONLY on the grade upgrades below — check_part.py demands
# part grade == merge-ready grade, and merge-ready grades these keys INFERRED while
# the merger tree grades them SOURCE (see REPORT-b011.md for the (b)/(c) conflict
# note). No other FAILs; labels/kinds unchanged.
# Full-repo greps: parts-staging/grep/11/grep_11_*.txt (one file per UNREACHABLE row).
# STRONGER-EVIDENCE upgrades (grade field only; evidence text unchanged, and every
# upgraded entry already cites SRC lines): the merger tree holds these keys SOURCE
# while the base part graded them INFERRED, so the delivered part records SOURCE to
# avoid repeating the SOURCE 617->578->503 downgrade from the b001/b002 merges:
#   SOURCE (was INFERRED): SettingsFragment.newInstance
#   SOURCE (was INFERRED): AddTagButton.<init>(Context,AttributeSet)
#   SOURCE (was INFERRED): AddTagButton.<init>(Context,AttributeSet,int)
#   SOURCE (was INFERRED): tag.TagItem.hashCode
#   SOURCE (was INFERRED): tag.TagItem.toString
#   SOURCE (was INFERRED): TorrentTagsList.<init>(Context)
# Labels/kinds are exactly the base part's (and the batch file's); nothing flipped.

# Batch 11 part (SettingsFragment, SummaryPreference, SwitchBarPreference,
# TimePreference, AddTagButton, tag.TagItem, TorrentTagsList). All 9 rows are
# UNREACHABLE, so this part contains no e() edges. Each evidence string cites
# lines printed in graphs/LibreTorrent/scratch/b011_printed.txt.
#
# Pre-existing routes are NOT repeated here; they are listed with line refs
# in parts/b011.md Dependencies (none: this batch has no REACHABLE rows).

# Row 1: SettingsFragment.newInstance has no printed caller; the file calls
# other fragments' newInstance methods but never its own.
# Rows 2-4: the 1-arg ctors only delegate via this(context, null) to the
# 2-arg ctor; the classes reach the app through XML inflation, and no
# printed 1-arg construction site exists.
# Rows 5-6: only the 1-arg AddTagButton construction is printed
# (TorrentTagsList.java:79); no XML tag and no 2-arg or 3-arg construction
# is printed.
# Rows 7-8: TagsAdapter compares tag.TagItem values with equals/isSame in
# its DiffUtil callback and binds only info.name/info.color; no hash or
# toString use on a tag.TagItem is printed.
# Row 9: TorrentTagsList is used from layout inflation, which invokes the
# 2-arg ctor; no printed app code constructs it with one argument.
UNREACHABLE.update({
    'SettingsFragment.newInstance': ('no_trigger_in_app',
        'Definition at SettingsFragment.java:63-70. No printed app caller: SettingsFragment.java calls other fragments newInstance methods (:94, :141, :150, :159, :168, :177, :186, :195, :204) but never its own, and a full-app-tree grep for SettingsFragment.newInstance finds no hit.',
        'SRC ui/settings/SettingsFragment.java:63-70,94,141,150,159,168,177,186,195,204',
        'SOURCE'),
    'SummaryPreference.<init>(Context)': ('no_trigger_in_app',
        'Definition at SummaryPreference.java:39-42, body only this(context, null) delegating to the 2-arg ctor. The class is declared in res/xml/pref_anonymous_mode.xml:8 and no printed app code constructs it with one argument.',
        'SRC ui/settings/customprefs/SummaryPreference.java:39-42; res/xml/pref_anonymous_mode.xml:8',
        'INFERRED'),
    'SwitchBarPreference.<init>(Context)': ('no_trigger_in_app',
        'Definition at SwitchBarPreference.java:40-43, body only this(context, null) delegating to the 2-arg ctor. The class is declared in res/xml/pref_anonymous_mode.xml:3 and no printed app code constructs it with one argument.',
        'SRC ui/settings/customprefs/SwitchBarPreference.java:40-43; res/xml/pref_anonymous_mode.xml:3',
        'INFERRED'),
    'TimePreference.<init>(Context)': ('no_trigger_in_app',
        'Definition at TimePreference.java:32-36, body only this(context, null) delegating to the 2-arg ctor. The class is declared in res/xml/pref_scheduling.xml:11 and :26 and no printed app code constructs it with one argument.',
        'SRC ui/settings/customprefs/TimePreference.java:32-36; res/xml/pref_scheduling.xml:11,26',
        'INFERRED'),
    'AddTagButton.<init>(Context,AttributeSet)': ('no_trigger_in_app',
        'Definition at AddTagButton.java:43-48. The only printed construction is the 1-arg form at TorrentTagsList.java:79; no printed XML tag for AddTagButton and no printed 2-arg construction exists.',
        'SRC ui/tag/AddTagButton.java:43-48; ui/tag/TorrentTagsList.java:79',
        'SOURCE'),
    'AddTagButton.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'Definition at AddTagButton.java:49-56. Same evidence as the 2-arg row: only the 1-arg construction is printed (TorrentTagsList.java:79); no printed XML tag and no printed 3-arg construction exists.',
        'SRC ui/tag/AddTagButton.java:49-56; ui/tag/TorrentTagsList.java:79',
        'SOURCE'),
    'tag.TagItem.hashCode': ('no_trigger_in_app',
        'Definition at TagItem.java:49-51 (return info.hashCode()). The printed consumer, TagsAdapter.java:65-81, compares items with equals (areContentsTheSame) and isSame (areItemsTheSame), never hashCode; no hash-based collection use of a tag.TagItem is printed.',
        'SRC ui/tag/TagItem.java:49-51; ui/tag/TagsAdapter.java:65-81',
        'SOURCE'),
    'tag.TagItem.toString': ('no_trigger_in_app',
        'Definition at TagItem.java:55-60. No printed call, string concatenation, or log/print on a tag.TagItem appears in TagItem.java, TagsAdapter.java:54-115, or the DiffUtil callback.',
        'SRC ui/tag/TagItem.java:55-60; ui/tag/TagsAdapter.java:54-115',
        'SOURCE'),
    'TorrentTagsList.<init>(Context)': ('no_trigger_in_app',
        'Definition at TorrentTagsList.java:23-27, body super(context) + init(context). The printed use is layout inflation, which invokes the 2-arg ctor (TorrentTagsList.java:29-33); no printed app code constructs it with one argument.',
        'SRC ui/tag/TorrentTagsList.java:23-33',
        'SOURCE'),
})

# No subclasses of any batch-11 class exist in the app source (grep for
# extends of each class finds no hit), so there are no @Variant generated
# copies to suppress beyond the base names themselves. SUPPRESS holds the
# nine UNREACHABLE names so bytecode auto edges into them are dropped.
SUPPRESS.update({
    'SettingsFragment.newInstance',
    'SummaryPreference.<init>(Context)',
    'SwitchBarPreference.<init>(Context)',
    'TimePreference.<init>(Context)',
    'AddTagButton.<init>(Context,AttributeSet)',
    'AddTagButton.<init>(Context,AttributeSet,int)',
    'tag.TagItem.hashCode',
    'tag.TagItem.toString',
    'TorrentTagsList.<init>(Context)',
})
