# AnkiDroid batch 144 (LABEL helper, 2026-10-30). 40 methods in 10 classes, 4 each: ChartView, CompatV15$1, CompatV19,
# FilteredDeckOptions, FontMetricsWrap, HttpFetcher, LanguageListerBase, LoadPronounciationActivity$DownloadFileTask,
# SlidingTabLayout, Statistics.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 144. The full row list (label, kind, reason, printed
# file:lines) is in graphs/AnkiDroid/parts/label_144.md.
#
# Labels: all 40 methods already have REACHABLE rows in parts 029, 037, 047, 063, 066, 067, 072, 073, 075 and 125.
# None is labelled again here. No UNREACHABLE entry is written.
#
# Route gap closed here: build_report.txt lines 288-289 report "no path" for CompatV19.showViewWithAnimation and
# CompatV19.hideViewWithAnimation. Their only automatic CALL edges come from CompatV19$1.onSystemUiVisibilityChange
# (CompatV19.java:56-65, auto_calls.json exact). That listener has only a REGISTER edge from CompatV19$1.<init>
# (part 073, graph_def.py:8458-8461), and REGISTER does not count for reachability. The framework delivers the callback
# through View.dispatchSystemUiVisibilityChanged (View.java:22695-22700), which ViewRootImpl calls at ViewRootImpl.java:6007.
# The edge below starts from the registering method CompatV19.setFullScreen, the same pattern as the CompatV15 TTS
# listener edges (label_072.py:11-27). Its destination is a part 073 method. It is written here only so that the
# batch 144 methods have a route.
#
# Not written here: CompatV19$2.onAnimationEnd (build_report.txt line 292) has the same gap. It has only a REGISTER edge
# (graph_def.py:8463-8466), it is in part 073 and not in batch 144, so it is reported to the parent.
#
# Gate: the same missing gate as MG672 in part 073. No constant fits, so env and needs_state are unset.

e('CompatV19.setFullScreen', 'CompatV19$1.onSystemUiVisibilityChange', 'FRAMEWORK',
  'the framework calls the decor view listener that setFullScreen registers when the system bar visibility changes',
  evidence='SRC com/ichi2/compat/CompatV19.java:41-43; FW-SRC core/java/android/view/View.java:22684-22700; FW-SRC core/java/android/view/ViewRootImpl.java:5990-6007',
  note='MISSING GATE MG672 (as on the REGISTER edge in part 073): the callback runs only when the global system UI visibility changes (ViewRootImpl.java:6005-6007), for example after a touch reveals the bars. The app does not call it directly. The null guard at CompatV19.java:49-51 returns early when a view is missing.')
