# AnkiDroid batch 066 (LABEL helper). Batch file: graphs/AnkiDroid/scratch/batches/batch_066.txt (36 methods).
# Full row list: graphs/AnkiDroid/parts/label_066.md.
# Methods: ChartView (3 constructors, addFragment, onDraw, onSizeChanged, setData), OverviewStatsBuilder (constructor and
# private helpers), OverviewStatsBuilder$OverviewStats.<init>, StatsMetaInfo (implicit constructor and 18 accessors).
#
# Route ownership:
# - Automatic CALL edges into and out of these methods (Statistics -> addFragment, AnkiStatsTaskHandler -> setData and the
#   OverviewStatsBuilder constructor, the OverviewStatsBuilder internal calls, Stats.calculateDue -> StatsMetaInfo) come
#   from the builder. They are not written here.
# - The three framework edges below have the page S_STATISTICS as source, so they belong to this part (the destination is
#   a method of this batch).
# Gates: STATE_SETTINGS (the advanced statistics preference, for the StatsMetaInfo accessors reached through
# Stats.calculateDue). No MG id is used.

# --- Chart view inflated from fragment_anki_stats.xml (Statistics.ChartFragment.onCreateView, Statistics.java:428).
e('S_STATISTICS', 'ChartView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the statistics chart pages inflate the chart view from fragment_anki_stats.xml',
  cls='non_standard',
  via=['layout XML and LayoutInflater reflection'],
  evidence='SRC com/ichi2/anki/Statistics.java:421-428; SRC res/layout/fragment_anki_stats.xml:5; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='LayoutInflater builds the view with the (Context, AttributeSet) constructor by reflection (LayoutInflater.java:615). The page is opened from the navigation drawer (NavigationDrawerActivity.java:265-268) and its fragments come from SectionsPagerAdapter.getItem (Statistics.java:305-309). No gate.')

# --- View.draw calls onDraw (framework callback on the statistics page).
e('S_STATISTICS', 'ChartView.onDraw', 'FRAMEWORK',
  'the statistics screen draws the chart view; View.draw calls onDraw',
  evidence='SRC com/ichi2/anki/stats/ChartView.java:56-57; FW-SRC core/java/android/view/View.java:19161-19166, 19192, 19308',
  note='onDraw runs for the chart view on every draw of the page. With no data set it calls super.onDraw (ChartView.java:74-75). No gate.')

# --- View.setFrame -> sizeChange -> onSizeChanged (framework callback on the statistics page).
e('S_STATISTICS', 'ChartView.onSizeChanged', 'FRAMEWORK',
  'the chart view is laid out with a new size; View.setFrame calls sizeChange, which calls onSizeChanged',
  evidence='SRC com/ichi2/anki/stats/ChartView.java:91-92; FW-SRC core/java/android/view/View.java:19720, 19752-19753, 19791-19792',
  note='The override calls mFragment.checkAndUpdate() once addFragment has run (ChartView.java:95-96). No gate.')

# --- Unreachable: the layout inflater and the app never use these constructors.
UNREACHABLE['ChartView.<init>(Context)'] = ('framework_never_calls', 'LayoutInflater builds chart views with the (Context, AttributeSet) constructor only, and nothing in the app calls the one-argument constructor (no new ChartView in the source root and no subclass of ChartView)', 'com/ichi2/anki/stats/ChartView.java:40-43; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615; res/layout/fragment_anki_stats.xml:5', 'SOURCE')

UNREACHABLE['ChartView.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'The three-argument constructor runs only when a subclass calls it through super or when code calls new ChartView with a style; the layout inflater uses the two-argument constructor, the two-argument ChartView constructor calls super(context, attrs) (ChartView.java:46), and the source root has no new ChartView and no subclass of ChartView', 'com/ichi2/anki/stats/ChartView.java:45-53; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615', 'SOURCE')
