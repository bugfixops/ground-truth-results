# ROUTE_UNSCRIPTABLE_02 — DiaryWidgetProvider.getHome (Diary route_02)

Status: unscriptable-candidate (no script written for this route).
Proposed ROUTES.csv status change (for the Diary merger to decide):
`unscriptable: needs a Diary widget placed on the home screen through
the launcher; the harness cannot place a widget`.

## Route

Method: DiaryWidgetProvider.getHome. Edges (19, from ROUTES.csv):
Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691
Ede74cf66 E6308923b Ef07452ff E90a3fefc E2adbb115 Eeb8ea610
Efbe8cd80. Printed route: Diary route print,
DiaryWidgetProvider.getHome section (SOURCE_OK), ref
DiaryWidgetProvider.java:225.

## Why it cannot be driven by adb with the delivered harness

Unlike routes 01/04, this route needs no tap on the widget itself:
its target is reached inside the provider's update chain
(onUpdate -> getText -> getFile -> getDay -> getMonth -> getYear ->
getHome). But that chain only runs when onUpdate runs, and onUpdate
only runs for a placed widget:

- Diary.updateWidgets broadcasts only the ids the system already has
  for placed widgets (Diary.java:2357-2368:
  `appWidgetManager.getAppWidgetIds(provider)`).
- Edge Ede74cf66 states the gate explicitly: the ids sent by
  Diary.updateWidgets are non-empty only with a placed widget (route
  print cites FW-SRC AppWidgetProvider :61-67: APPWIDGET_UPDATE ->
  onUpdate only for a non-empty id list).
- With no widget placed, the broadcast carries an empty id list, so
  super.onReceive (DiaryWidgetProvider.java:75-96) does not dispatch
  to onUpdate (DiaryWidgetProvider.java:115-185), getText
  (DiaryWidgetProvider.java:117-121) is never called, and getHome
  (DiaryWidgetProvider.java:223-227) is never reached.

The only adb shortcut around this would be to broadcast
APPWIDGET_UPDATE directly to the provider with fabricated widget ids.
That was rejected, not used: it would fabricate the route's own
precondition (placed ids from Diary.updateWidgets) rather than drive
the printed route, and it is exactly the kind of faked step the task
forbids. Placing a widget for real is launcher UI work, and the
delivered harness (device/harness/harness.py) has no drag or
widget-placement operation (see ROUTE_UNSCRIPTABLE_01.md). Hence no
script was written.

## Printed source lines relied on

- Diary.java:2357-2368 — updateWidgets: getAppWidgetIds(provider),
  sendBroadcast APPWIDGET_UPDATE with those ids.
- DiaryWidgetProvider.java:75-96 — onReceive, then super.onReceive.
- DiaryWidgetProvider.java:115-185 — onUpdate: getText(context) at
  117-121, then RemoteViews + updateAppWidget.
- DiaryWidgetProvider.java:193 — getText -> getFile(entry).
- DiaryWidgetProvider.java:257-261 — getFile(Calendar) -> getDay.
- DiaryWidgetProvider.java:239-253 — getDay -> getMonth.
- DiaryWidgetProvider.java:231-235 — getMonth -> getYear.
- DiaryWidgetProvider.java:223-227 — getYear -> getHome (target).
- res/xml/widget.xml — widgetCategory home_screen, i.e. a home-screen
  widget placed through the launcher.

## Note on the D1 judgment

device/routes/Diary/ROUTES_NOTES.md judged routes 01/02/04 scriptable
"with UI automation". That judgment is not followed here for the
reason above: the harness as delivered provides no widget-placement
automation. If the device lead adds launcher widget-placement support
to the harness, this route should be revisited. Three widget routes
(01, 02, 04) of 30 Diary routes is exactly 10%, the D3 per-app cap.
