# AnkiDroid batch 143 (LABEL helper). CardTemplateEditor (4 methods), CardTemplateEditor$2 (3), CardTemplateEditor$CardTemplateFragment$1 (4),
# CardTemplateEditor$TemplatePagerAdapter (4), Reviewer$BuryProvider (5), Reviewer$SuspendProvider (5), SlidingTabStrip (5),
# SlidingTabStrip$SimpleTabColorizer (5), XGrid (5). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 143. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_143.md.
#
# All 40 methods were already labelled REACHABLE by other parts (parts 008, 025, 026, 076, 121; cross-references in 115, 125,
# 135, 137). They are not labelled again here, and no UNREACHABLE entries are written here.
#
# Route gaps in out/ that the edges below close (both methods were UNRESOLVED with incoming 0 in out/methods.csv,
# although parts/label_026.md labels them REACHABLE):
# - CardTemplateEditor$TemplatePagerAdapter.getItemPosition: the override returns POSITION_NONE (CardTemplateEditor.java:311-315).
#   It is reached when selectTemplate calls notifyDataSetChanged (CardTemplateEditor.java:286). Written here: FRAMEWORK
#   CardTemplateEditor.selectTemplate -> CardTemplateEditor$TemplatePagerAdapter.getItemPosition (same pattern as
#   Statistics$SectionsPagerAdapter.getItemPosition at graph_def.py:5195-5199).
# - CardTemplateEditor$TemplatePagerAdapter.getPageTitle: the title is read by SlidingTabLayout.populateTabStrip
#   (SlidingTabLayout.java:222). That path is shared with Statistics, so the edge is drawn from the page node, not from
#   onCollectionLoaded, to avoid a false route through the shared tab strip. Written here: FRAMEWORK
#   S_CARDTEMPLATEEDITOR -> CardTemplateEditor$TemplatePagerAdapter.getPageTitle (same pattern as graph_def.py:5207-5212).
#
# No new constants are defined here. The existing getItem and getItemId edges from S_CARDTEMPLATEEDITOR
# (graph_def.py:3562-3572, parts/label_026.py:51-57) are not repeated.

e('CardTemplateEditor.selectTemplate', 'CardTemplateEditor$TemplatePagerAdapter.getItemPosition', 'FRAMEWORK',
  'the tab set is refreshed after a template is added or removed (notifyDataSetChanged)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:97-100, 282-286, 311-315',
  note='selectTemplate calls notifyChangeInPosition(1) (line 284) and then notifyDataSetChanged (line 286). The support-library PagerAdapter then calls getItemPosition for each page (INFERRED, support library, source not read). The override returns POSITION_NONE (line 314), so every page is rebuilt. selectTemplate is reached from the success branch at CardTemplateEditor.java:97-100 (the automatic CALL edge already in graph_def.py). No gate beyond that route. Precedent: Statistics.selectDropDownItem -> Statistics$SectionsPagerAdapter.getItemPosition (graph_def.py:5195-5199).')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$TemplatePagerAdapter.getPageTitle', 'FRAMEWORK',
  'the tab strip draws the tab titles',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:232, 288, 339-345; SRC com/ichi2/ui/SlidingTabLayout.java:158-166, 199-203, 222',
  note='Tab titles are set by SlidingTabLayout.populateTabStrip (SlidingTabLayout.java:222). populateTabStrip runs from setViewPager (SlidingTabLayout.java:158-164), which onCollectionLoaded calls at CardTemplateEditor.java:232 and selectTemplate calls at line 288. The edge is drawn from the page node, not from those methods (same design as graph_def.py:5207-5212 for Statistics). The receiver of getPageTitle at line 222 is typed PagerAdapter (SlidingTabLayout.java:200), so the dispatch to TemplatePagerAdapter.getPageTitle is INFERRED: the automatic app CALL does not resolve library-typed calls. parts/label_026.md labels this method CALL; the edge written here is FRAMEWORK for that reason.')
