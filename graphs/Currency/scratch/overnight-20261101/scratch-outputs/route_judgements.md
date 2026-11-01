# Currency route checks — fresh sample re-check (local, 2026-11-01)

Command: `python3 -I tools/verify_sample.py Currency 30 20261025`
Sample drawn: **27 of 140 reachable methods, 107 distinct edges** (the tool's
strata quotas sum to 30, but pools exhaust at 27; this is the tool's own
output, not a truncated run). Full step-by-step printout with cited source
lines: `scratch/routes_full.txt` (2,400 lines, all 27 routes, every step).

## Judgements

| # | Method | Steps | Judgement | Note |
|---|---|---|---|---|
| 1 | AboutPreference.\<init\> | 13 | correct | Preferences inflation via SettingsFragment.java:48 + preferences.xml; matches branch path row (correct). |
| 2 | CurrencyWidgetProvider.onUpdate | 9 | correct | Via Main.onPause -> updateWidgets broadcast; FW-SRC broadcast-limitation citations in graph (see check 2). Matches branch path row. |
| 3 | CurrencyWidgetProvider.onReceive | 8 | correct | Same broadcast chain, ending at onReceive (CurrencyWidgetProvider.java:67-76). Matches branch path row. |
| 4 | CurrencyWidgetProvider.\<init\> | 7 | correct | Same broadcast chain, ending at receiver instantiation. Matches branch path row. |
| 5 | Main.onEditorAction | 6 | unclear | App side verified: listener registered Main.java:324, handler Main.java:1239-1310. Step 5 (soft keyboard opens on focus) is INFERRED — IME behaviour not read; layout file not in local tree. Same as branch path row (unclear, INFERRED). Not counted in error rate. |
| 6 | Parser$Handler.startElement | 5 | correct | STATE data gate; Parser.java:94 Xml.parse SAX callback. Matches branch path row. |
| 7 | Parser$Handler.\<init\> | 5 | correct | NEW route (no branch path row): Main.onResume -> Parser.startParser (Main.java:497, STATE gate) -> new Handler() (Parser.java:93). |
| 8 | Parser.getMap | 4 | correct | Main.java:529 valueMap = parser.getMap(), STATE gate. Matches branch path row. |
| 9 | CurrencyWidgetUpdate.onDestroy | 16 | unclear | App/service chain fully printed (configure -> refresh tap -> service -> Data parse -> onDataResult -> stopSelf -> onDestroy), but step 1 launcher call is INFERRED (launcher source not read) and the static Data listener is shared with Main. Same as branch path row (unclear, INFERRED). Not counted. |
| 10 | ChartActivity$DateAxisValueFormatter.getFormattedValue | 20 | correct | Previously fixed route (now via onActivityResult@OK); formatter registered ChartActivity.java:235, redraw :879-886. Matches branch path row (fixed). |
| 11 | ChartActivity.onInvertClick | 18 | correct | History download -> onDataResult -> chart loaded -> Invert enabled (ChartActivity.java:479,526-527). Matches branch path row. |
| 12 | ChoiceDialog.onRestoreInstanceState | 11 | correct | Rotation recreation; app code ChoiceDialog.java:134-179 printed; framework relaunch step FW-SRC (not in app tree). Matches branch path row. |
| 13 | CurrencyWidgetProvider.onDeleted | 7 | unclear | Step 5 (launcher deletes widget id after RESULT_CANCELED configure) is INFERRED — launcher source not read. Same as branch path row (unclear, INFERRED). Not counted. |
| 14 | Main.onDateResult | 7 | correct | NEW route (no branch path row): Main.onResume (Data.map null + network guard, Main.java:646-695) -> Data.startParse -> executor -> failure branch Data.java:107-112 -> listener.onDateResult(null). Main is the listener in this route (Data.getInstance(this), Main.java:282). |
| 15 | HelpActivity.onOptionsItemSelected | 12 | correct | Navigation popup -> Help -> Up arrow (HelpActivity.java:99,104). Matches branch path row. |
| 16 | AboutPreference.onBindDialogView | 15 | correct | Settings -> tap About; framework DialogPreference bind step FW-SRC (not in app tree). Matches branch path row. |
| 17 | ChartActivity.showToast(String) | 14 | correct | Offline guard ChartActivity.java:401-424 -> showToast overload chain :1026-1027, :1033-1034. Matches branch path row. |
| 18 | CurrencyWidgetUpdate.onDateResult | 15 | unclear | Same launcher + shared-listener caveats as #9 (failure branch Data.java:107-112). Same as branch path row (unclear, INFERRED). Not counted. |
| 19 | Singleton.setMap | 14 | correct | ChartActivity.onPause -> instance.setMap(histMap) (ChartActivity.java:445). Matches branch path row. |
| 20 | Singleton.\<init\> | 12 | correct | ChartActivity.onCreate -> Singleton.getInstance -> new Singleton() (Singleton.java:57-58). Matches branch path row. |
| 21 | Main.lambda$onUpdateClick$1 | 9 | correct | Update menu -> updateDialog -> dialog button listener (Main.java:1046,1102-1103). Matches branch path row. |
| 22 | Main$Currency.\<init\> | 2 | correct | Static CURRENCIES table, Main.java:115-151, new Currency(...) per entry. Matches branch path row. |
| 23 | Data.\<init\> | 4 | correct | Main.onCreate -> Data.getInstance (Main.java:282) -> new Data() (Data.java:56-57). Matches branch path row. |
| 24 | Main.onItemClick | 5 | correct | Tap row in DISPLAY_MODE (Main.java:1329-1402). Matches branch path row. |
| 25 | Main.onRefreshClick | 6 | correct | Menu case Main.java:781-782. Matches branch path row. |
| 26 | Main.onCopyClick | 8 | correct | SELECT_MODE menu case Main.java:809-810. Matches branch path row. |
| 27 | Main.onActivityResult | 10 | correct | Add picker closed with default RESULT_CANCELED (framework step FW-SRC, not in app tree). Matches branch path row. |

## Totals

- correct 23, fixed 0, wrong 0, unclear 4 (routes 5, 9, 13, 18).
- Error rate = (fixed + wrong) / (correct + fixed + wrong) = 0 / 23 = **0.0**.
- No graph fix was needed, so no redraw-after-fix differs from the drawn
  sample: `scratch/sample_30_final.txt` is identical to `scratch/sample_30.txt`
  (verified by diff).
- The 4 unclear routes are exactly the 4 unclear path rows already in the
  branch verification.csv; nothing new was left unclear. The 2 new correct
  routes (#7, #14) have no branch path row — see DECISIONS.md D1: they are
  recorded here, NOT hand-appended to verification.csv, because that file may
  only be produced via tools/make_verification.py, which does not exist on
  branch work-2026-10-31 (see eight-check report).
