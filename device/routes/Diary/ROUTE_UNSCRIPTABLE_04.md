# ROUTE_UNSCRIPTABLE_04 — DiaryWidgetUpdate.nextMonth (Diary route_04)

Status: unscriptable-candidate (no script written for this route).
Proposed ROUTES.csv status change (for the Diary merger to decide):
`unscriptable: needs a Diary widget placed on the home screen through
the launcher; the harness cannot place a widget`.

## Route

Method: DiaryWidgetUpdate.nextMonth. Edges (18, from ROUTES.csv):
Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691
Ede74cf66 Ed30f979f Ef930bfbc E1bda1894 E4f7e2de4 E6b9a06e0.
Printed route: Diary route print, DiaryWidgetUpdate.nextMonth
section (SOURCE_OK), ref DiaryWidgetUpdate.java:253.

## Why it cannot be driven by adb with the delivered harness

Same blocker as route_01, on the NEXT side of the widget:

1. The widget must exist on the home screen. Diary.updateWidgets
   broadcasts only placed-widget ids (Diary.java:2357-2368), and
   edge Ede74cf66 gates onUpdate on a non-empty placed-id list, so
   without a placed widget the provider never produces S_HOME_WIDGET.
2. Step 15 taps the widget's next-entry arrow. The provider attaches
   that arrow to a PendingIntent for DiaryWidgetUpdate with
   ENTRY=NEXT (DiaryWidgetProvider.java:154-164, set on R.id.next at
   line 178). The widget layout gives that ImageView no text and no
   content-desc (res/layout/widget.xml: R.id.next ImageView, with
   `tools:ignore="ContentDescription"`), so there is no harness
   tap-by-text/desc target, and the tap can only happen on a placed
   widget rendered by the launcher host.

Placing a widget is launcher UI work (open the launcher's widget
picker, drag the Diary widget onto the home screen). The delivered
harness (device/harness/harness.py) has no drag operation and no
widget-placement operation: `long_tap` requires text, res_id or desc,
and `tap` with fixed coordinates cannot perform the pick-and-drag
placement. Inventing a placement step (for example a fabricated
broadcast with invented widget ids) would not follow the printed
route: the route's broadcast is Diary's own sendBroadcast of placed
ids, and DiaryWidgetUpdate is declared without an intent filter
(AndroidManifest.xml:104-106, Theme.NoDisplay only), so an adb
`am start` of it is not a printed, exported entry point either. No
such step was invented, and no script was faked.

## Printed source lines relied on

- Diary.java:2357-2368 — updateWidgets: getAppWidgetIds(provider),
  sendBroadcast APPWIDGET_UPDATE with those ids.
- DiaryWidgetProvider.java:75-96 — onReceive, then super.onReceive.
- DiaryWidgetProvider.java:154-164, 178 — NEXT PendingIntent for
  DiaryWidgetUpdate, attached to R.id.next.
- DiaryWidgetProvider.java:181-185 — onUpdate calls
  updateAppWidget(ids, views), producing S_HOME_WIDGET.
- DiaryWidgetUpdate.java:50-75, 93-103, 251-261 — onCreate NEXT
  branch -> getNextEntry -> nextMonth (target).
- res/layout/widget.xml — R.id.next has no text and no content-desc.
- AndroidManifest.xml:104-106 — DiaryWidgetUpdate, Theme.NoDisplay,
  no intent filter.
- res/xml/widget.xml — widgetCategory home_screen, i.e. a home-screen
  widget placed through the launcher.

## Note on the D1 judgment

device/routes/Diary/ROUTES_NOTES.md judged routes 01/02/04 scriptable
"with UI automation". That judgment is not followed here because the
harness as delivered provides no widget-placement automation; if the
device lead adds launcher widget-placement support to the harness,
this route should be revisited, not silently passed. As the harness
stands, this route is an unscriptable-candidate. Three widget routes
(01, 02, 04) of 30 Diary routes is exactly 10%, the D3 per-app cap.
