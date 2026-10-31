# Currency v1.33: page-jump and method-call graph

A map of how every method of the open-source Android app **Currency** (upstream tag `v1.33`, commit `72e7dcd506adb8dd6e6cd797c08225427667a102`, by Bill Farmer, GPLv3) is triggered: from which page, by which user gesture or system event, through which framework callback or call, and under which conditions.

## What is in this folder

| File | What it is |
|---|---|
| `currency_trigger_graph.html` | The main result. One self-contained file, no internet needed: open it in any browser. |
| `methods.csv` | One row per method: verdict, number of steps from app launch, the user steps on the shortest path, the shortest path itself, number of incoming edges. Easy to filter in a spreadsheet. |
| `currency_trigger_graph.json` | The same data as the HTML, for programmatic use. |

## Reading the HTML

- **Page map**: every box is a page or UI state; an arrow means "after some gesture or event the user lands here". Hover a box to highlight its arrows, hover an arrow to see which gestures cause it, click a box to open it.
- **Page → next pages**: pick a page; each row is one gesture or event, the callback it fires, the page(s) it leads to, and the guard condition. Menu items are listed one per row.
- **Method → trigger path**: pick a method; you get the shortest chain from app launch to it (page, gesture, callback, call, with GUI steps and guards), every other known way to trigger it, and what it triggers next.
- Two switches: include edges that need a state built earlier (for example a second visit within the same process), and show the paused/exit pseudo pages on the map.
- Colours: purple `GUI` = a user gesture; `CALL` = direct call; `LIFECYCLE`, `SYSTEM`, `ASYNC`, `INTENT`, `RESULT` as named; `FRAMEWORK` = the Android framework calling the app back as a consequence of an app call; `ENTERS` = the method leaves the user on that page.

## Numbers

- 123 core methods (the app's own code; the coverage-instrumentation helper classes are excluded), 16 pages (including 3 pseudo pages: launcher entry, paused, exit), 298 edges.
- Verdicts: 119 reachable, 2 dead code (`ChartParser.startParser(Context,int)`, `Singleton.getList`), 2 framework-only (`CurrencyAdapter.getItem`, `ChoiceAdapter.getItem`: never called by the app, and no known framework path calls them in normal use).

## How much to trust it

- The graph was built by reading all of the app source and resources, and checking Android framework behaviour against AOSP `android-8.1.0_r1` source.
- It was then checked on an Android 8.1 (API 27) emulator with 77 scripted scenarios, each comparing the methods the graph predicts against the methods that actually ran: 76 matched, 1 prediction was wrong and has been corrected in this version. Across those runs 117 of the 123 methods were observed at least once; the other 6 are the 4 above plus 2 trivial private constructors that the coverage tool does not report.

## Limits

- Pages, and which states count as separate pages, were modelled by hand for this app; there is no standard definition behind them.
- The "shortest path" ignores guard conditions that depend on data or settings. Read the guard text on each edge; some paths need a specific state (for example network available, data already loaded).
- Verified on one device (API 27). Some framework behaviour differs across Android versions (for example the order of `onSaveInstanceState` and `onStop` changes at API 28).
- Not verified: the roaming branch, the branch taken when a download is still in progress on re-entry, and the exact order of the first menu build relative to `onResume`.
- Paths that load online exchange rates or chart history need the device to trust the data host's certificate chain; on old system images it is missing and those paths cannot be reached.
- Edges do not carry a per-edge evidence label; the checks above are aggregate.

## JSON shape (short)

```
{ "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|DEAD|FRAMEWORK_ONLY},
  "dead": {method: reason}, "framework_only": {method: reason},
  "edges": [ {id, src, dst, kind, trigger, gui[], guard, reads[], writes[], note, needs_state} ] }
```
`src`/`dst` are methods (`Class.method`) or pages (`S_...`); a suffix `@CONTEXT` means the same method or page reached in a specific context (for example `Main.onOptionsItemSelected@SELECT`: the menu handler while the main page is in selection mode).
