# ROUTE_UNSCRIPTABLE_01 — DiaryWidgetUpdate.getYear (Diary route_01)

Status: unscriptable-candidate (no script written for this route).
Proposed ROUTES.csv status change (for the Diary merger to decide):
`unscriptable: needs a Diary widget placed on the home screen through
the launcher; the harness cannot place a widget`.

## Route

Method: DiaryWidgetUpdate.getYear. Edges (19, from ROUTES.csv):
Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E13d2a950
Ec7e88adf E9b269181 E519112ea Ec8b3376c E9ddac6cd Ef7699691
Ede74cf66 Ed30f979f E6bfccc45 E50c0a087 E4c763149 E9433c4e1
E18600188. Printed route: Diary route print, DiaryWidgetUpdate.getYear
section (SOURCE_OK), ref DiaryWidgetUpdate.java:169.

## Why it cannot be driven by adb with the delivered harness

The route's step 13 carries the ENV other_app gate: the ids sent by
Diary.updateWidgets are non-empty only with a placed widget (route
print, edge Ede74cf66). Two later steps then depend on that placed
widget:

1. The widget must exist on the home screen. Diary.updateWidgets
   itself only broadcasts the ids the system already has for placed
   widgets: Diary.java:2357-2368 calls
   `appWidgetManager.getAppWidgetIds(provider)` and broadcasts those
   ids. With no widget placed, that list is empty and the provider's
   onUpdate (which leads to the widget screen) is not reached.
2. Step 15 taps the widget's previous-entry arrow. The provider
   attaches that arrow to a PendingIntent for DiaryWidgetUpdate with
   ENTRY=PREV (DiaryWidgetProvider.java:143-153, set on R.id.prev at
   line 177). The widget layout gives that ImageView no text and no
   content-desc (res/layout/widget.xml: R.id.prev ImageView, with
   `tools:ignore="ContentDescription"`), so there is no harness
   tap-by-text/desc target, and the tap can only happen on a placed
   widget rendered by the launcher host.

Placing a widget is launcher UI work (open the launcher's widget
picker, drag the Diary widget onto the home screen). The delivered
harness (device/harness/harness.py) has no drag operation and no
widget-placement operation: `long_tap` requires text, res_id or desc,
and `tap` with fixed coordinates requires a why string but still
cannot perform the pick-and-drag placement. Inventing a placement
step (for example a fabricated broadcast with invented widget ids)
would not follow the printed route: the route's broadcast is Diary's
own sendBroadcast of placed ids, and DiaryWidgetUpdate is declared
without an intent filter (AndroidManifest.xml:104-106, Theme.NoDisplay
only), so an adb `am start` of it is not a printed, exported entry
point either. No such step was invented, and no script was faked.

## Printed source lines relied on

- Diary.java:2357-2368 — updateWidgets: getAppWidgetIds(provider),
  sendBroadcast APPWIDGET_UPDATE with those ids.
- DiaryWidgetProvider.java:75-96 — onReceive stores the widget entry
  and calls super.onReceive (which dispatches to onUpdate only for a
  non-empty id list; route print cites FW-SRC AppWidgetProvider
  :61-67).
- DiaryWidgetProvider.java:143-153, 177 — PREV PendingIntent for
  DiaryWidgetUpdate, attached to R.id.prev.
- DiaryWidgetProvider.java:181-185 — onUpdate calls
  updateAppWidget(ids, views), producing S_HOME_WIDGET.
- DiaryWidgetUpdate.java:50-75, 82-92, 195-205, 168-175 — onCreate
  PREV branch -> getPrevEntry -> prevMonth -> getYear (target).
- res/layout/widget.xml — R.id.prev has no text and no content-desc.
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
