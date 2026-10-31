# AnkiDroid batch 135 (LABEL helper). 40 methods: AnkiDroidWidgetSmall$UpdateService (3), CardTemplateEditor$CardTemplateFragment
# (15) and GraphicsWrap (22). The full row list is in graphs/AnkiDroid/parts/label_135.md.
#
# Labels: all 40 are REACHABLE. There are no UNREACHABLE entries here.
#
# Route ownership:
# - One page-entry ENTERS edge is written here (method to page, env None, same convention as StudyOptionsActivity.onCreate in
#   label_007.py): CardTemplateEditor.onCreate -> S_CARDTEMPLATEEDITOR. Its source method is in batch 025, which did not write it.
#   Without it S_CARDTEMPLATEEDITOR is not reachable from S_ENTRY (build_report.txt line 852), so every page-owned edge into this
#   batch is unrouted. Possible duplicate if 025 adds the same edge later.
# - The Statistics.onCreate -> S_STATISTICS ENTERS edge is not written here: it is already in graph_def.py:11196 and in
#   label_137.py:43 (batch 137).
# - Not written here: the AsyncTask edges that lead into UpdateService.<init>, namely WidgetStatus.update -> UpdateDeckStatusAsyncTask
#   .doInBackground (ASYNC) and doInBackground -> onPostExecute (ASYNC). Neither is in graph_def.py or any part. Their source is in
#   the batch that contains WidgetStatus.update, which has no label row yet. The INTENT edges out of onPostExecute into
#   UpdateService.<init> and NotificationService.<init> are already written in label_080.py.
# - Automatic CALL edges (auto_calls.json) are not written here. The same labels for these 40 methods already exist in
#   label_018.md (UpdateService), label_025.md and label_026.md (CardTemplateFragment) and label_125.md (GraphicsWrap).
#
# Gates: no new gate. The fragment routes need S_CARDTEMPLATEEDITOR; the GraphicsWrap routes need S_STATISTICS and
# ChartView.setData (mDataIsSet). The onActivityResult route needs S_PREVIEWER, whose loader step is not in the graph yet
# (label_036.md). No STATE or ENV constant fits these gates, so env and needs_state are unset.

e('CardTemplateEditor.onCreate', 'S_CARDTEMPLATEEDITOR', 'ENTERS',
  'the template editor screen is shown: the activity starts the collection load and its page is on screen',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:127, 157, 205',
  note='Method to page (ENTERS). The start edges into this activity are INTENT edges from NoteEditor.showCardTemplateEditor (graph_def.py:2134) and ModelBrowser.openTemplateEditor (graph_def.py:4265), written in other batches. The collection load is started at line 157; onCollectionLoaded (line 205) is the ASYNC route written in label_025.py. Possible duplicate of a page-entry edge that batch 025 may add later.')

