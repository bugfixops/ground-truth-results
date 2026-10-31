# AnkiDroid batch 065 (LABEL helper). AnkiStatsTaskHandler (with its nested tasks CreateChartTask,
# CreateStatisticsOverview and DeckPreviewStatistics) and ChartBuilder: 35 methods. The full row list is in
# graphs/AnkiDroid/parts/label_065.md.
#
# Route ownership:
# - CALL edges (constructors, accessors, createChart, createStatisticsOverview, createReviewSummaryStatistics,
#   renderChart and its setup and tick methods, the <clinit> pseudo-edges) come from auto_calls.json. Not written here.
# - The ASYNC edges below have their source in this batch: the start of each AsyncTask (execute in the three
#   create methods, into the doInBackground of the task) and the hand-back from doInBackground to onPostExecute.
# - The cancel(true) edges into the onCancelled methods come from Statistics.java (Statistics batch). Not written here.
# - No gate is needed: the task edges carry no environment or state.
#
# Gates: none (no MG id used in this batch).

e('AnkiStatsTaskHandler.createChart', 'AnkiStatsTaskHandler$CreateChartTask.doInBackground', 'ASYNC',
  'execute() on a chart task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:65-69; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='execute calls executeOnExecutor, which runs onPreExecute on the caller thread (AsyncTask.java:648), then exec.execute(mFuture) (AsyncTask.java:651). The FutureTask (AsyncTask.java:345-359) runs the worker. CreateChartTask does not override onPreExecute.')

e('AnkiStatsTaskHandler$CreateChartTask.doInBackground', 'AnkiStatsTaskHandler$CreateChartTask.onPostExecute', 'ASYNC',
  'the chart result returns to the UI thread, where the chart is shown',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:94-114, 121-129; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='doInBackground returns the PlotSheet. postResult sends a message to the UI thread handler (AsyncTask.java:369-375). InternalHandler calls finish (AsyncTask.java:712), and finish calls onPostExecute when the task was not cancelled (AsyncTask.java:691-695). The dispatch is the framework handler route.')

e('AnkiStatsTaskHandler.createStatisticsOverview', 'AnkiStatsTaskHandler$CreateStatisticsOverview.doInBackground', 'ASYNC',
  'execute() on the overview task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:70-74; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='Same dispatch as the chart task: executeOnExecutor runs onPreExecute on the caller thread (AsyncTask.java:648), then exec.execute(mFuture) (AsyncTask.java:651). CreateStatisticsOverview does not override onPreExecute.')

e('AnkiStatsTaskHandler$CreateStatisticsOverview.doInBackground', 'AnkiStatsTaskHandler$CreateStatisticsOverview.onPostExecute', 'ASYNC',
  'the overview HTML returns to the UI thread, where it is loaded into the WebView',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:143-162, 169-183; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='Same hand-back as the chart task: postResult (AsyncTask.java:369-375), InternalHandler and finish (AsyncTask.java:691-695, 712), then onPostExecute when the task was not cancelled.')

e('AnkiStatsTaskHandler.createReviewSummaryStatistics', 'AnkiStatsTaskHandler$DeckPreviewStatistics.doInBackground', 'ASYNC',
  'execute() on the deck preview task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:75-79; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='Same dispatch as the chart task (executeOnExecutor, onPreExecute on the caller thread at AsyncTask.java:648, exec.execute at AsyncTask.java:651). DeckPreviewStatistics does not override onPreExecute.')

e('AnkiStatsTaskHandler$DeckPreviewStatistics.doInBackground', 'AnkiStatsTaskHandler$DeckPreviewStatistics.onPostExecute', 'ASYNC',
  'the studied-today text returns to the UI thread, where it is set on the deck list text view',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:197-237, 245-251; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='Same hand-back as the chart task: postResult (AsyncTask.java:369-375), InternalHandler and finish (AsyncTask.java:691-695, 712), then onPostExecute when the task was not cancelled.')

UNREACHABLE['AnkiStatsTaskHandler$DeckPreviewStatistics.onCancelled'] = ('no_trigger_in_app', "DeckPreviewStatistics.onCancelled runs only after cancel(true) on that task. No in-app code holds or cancels a DeckPreviewStatistics: createReviewSummaryStatistics returns it and DeckPicker discards the result (DeckPicker.java:1873). The cancel(true) calls in Statistics.java (543, 574, 681, 692) cancel only the chart and overview tasks, and the DeckTask cancel (DeckTask.java:172) acts on a DeckTask. So the method never runs.", "SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:75-78, 240-242; SRC com/ichi2/anki/DeckPicker.java:1873; SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/async/DeckTask.java:172; FW-SRC core/java/android/os/AsyncTask.java:462-463, 691-693", 'SOURCE')
