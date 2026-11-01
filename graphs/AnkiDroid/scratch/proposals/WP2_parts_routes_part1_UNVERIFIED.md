# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AnkiDroid — route checks, parts 134–137 (PROPOSAL ONLY, NOT MERGED)

- Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. Nothing pushed.
- Scope: sampled-style routes from small parts files only. graph_def.py (1,173,446 bytes)
  and out/methods.csv (2,805,329 bytes) were NOT read, the official sampler
  tools/verify_sample.py (30, seed 20261025) was NOT run, and NO sample was invented.
- Parts fetched one at a time, spaced, via the GitHub connector
  (get_file_contents, resource text field):
  - graphs/AnkiDroid/parts/label_134.md — complete, 38 rows, all REACHABLE as labelled
    (putString and remConf are in batch 028 and not repeated there).
  - graphs/AnkiDroid/parts/label_135.md — complete, 40 rows, all REACHABLE as labelled.
  - graphs/AnkiDroid/parts/label_136.md — complete, 40 rows, all REACHABLE as labelled.
  - graphs/AnkiDroid/parts/label_137.md — complete, 40 rows, all REACHABLE as labelled.
  - No part file was too large or missing. No .py edge file was re-fetched in this
    check, so every e() edge claimed in a part (label_134.py: 2 edges,
    label_135.py: 1 ENTERS edge, label_136.py: 3 ENTERS edges, label_137.py: 5 edges)
    is NOT CHECKED here.
- Judging rules used: a step counts as checked only if its source lines were
  re-printed in this check (source fetches below, also spaced, one at a time).
  A step cited only in a part file, or only by a graph_def.py line number, is
  marked NOT CHECKED, not correct. confirmed_by is SOURCE only for re-printed
  lines, otherwise INFERRED. No DYN, FW-MEMORY, or UNVERIFIED evidence is used,
  and no tool coverage, old generated graph, or build REACHABLE count is used
  as evidence. Framework/library dispatch steps are INFERRED unless printed.
- Source files re-printed in this check (line ranges actually read):
  - com/ichi2/anki/Reviewer.java (656 lines): 195–235, 345–355, 385–392, 460–470, 522–528
  - com/ichi2/anki/AbstractFlashcardViewer.java (2828 lines): 1050–1056, 1207–1221, 1279–1290
  - com/ichi2/anki/Whiteboard.java (298 lines): 85–135, 195–205
  - com/ichi2/anki/stats/ChartView.java (99 lines): 50–90
  - com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java (181 lines): 30–40, 160–170
  - com/ichi2/anki/multimediacard/activity/TranslationActivity.java (440 lines): 153–165, 196–217, 257–300
  - com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java (494 lines): 90–130, 154–175
  - com/wildplot/android/rendering/YAxis.java (570 lines): 156–190, 213–230
- Result: 10 methods judged (3 from label_134, 2 from label_135, 2 from label_136,
  3 from label_137). All 10 are PROPOSED REACHABLE, none VERIFIED FOR MERGE,
  because in every case at least one upstream entry/framework step was not
  re-printed. The other 150 rows across the four parts were NOT judged here.

## Per-route table

| # | Method (part) | Route steps judged | Verdict | Citations (part + re-printed source) | Proposed fix (not merged) |
|---|---|---|---|---|---|
| 1 | AbstractFlashcardViewer.answerCard (label_134) | (a) S_REVIEWER GUI → Reviewer.onKeyUp — NOT CHECKED (graph_def.py:1406 cited in label_137, not re-printed). (b) Reviewer.onKeyUp:352 `answerCard(getDefaultEase())` — CORRECT, re-printed (Reviewer.java:351–353; also :348 `answerCard(EASE_4)`). (c) answerCard body at :1279, calls hideLookupButton at :1284 — CORRECT, re-printed (AbstractFlashcardViewer.java:1279–1285). | PROPOSED REACHABLE, conditional on (a) | label_134: AbstractFlashcardViewer.java:1279–1325; Reviewer.java:350–353 | None to the method; entry step (a) still needs a printed graph_def/framework check before merge. |
| 2 | AbstractFlashcardViewer.clipboardGetText (label_134) | (a) lookUp:1210 `clipboardGetText()` — CORRECT, re-printed (AbstractFlashcardViewer.java:1207–1211). (b) showLookupButtonIfNeeded:1219 `clipboardGetText()` — CORRECT, re-printed (:1217–1220). (c) Definition at :1053 — CORRECT, re-printed (:1053–1056). (d) Upstream lookUp route via executeCommand / lookUpOrSelectText — NOT CHECKED (not re-printed here). | PROPOSED REACHABLE, conditional on (d) | label_134: AbstractFlashcardViewer.java:1053, 1207–1221 | None to the method; upstream step (d) still needs printing before merge. |
| 3 | AbstractFlashcardViewer.delayedHide (label_134) | (a) Reviewer.onWindowFocusChanged:526 `delayedHide(INITIAL_HIDE_DELAY)` — CORRECT, re-printed (Reviewer.java:522–527). (b) S_REVIEWER FRAMEWORK → onWindowFocusChanged — NOT CHECKED (graph_def.py:1367 cited in label_137, not re-printed). (c) Gesture callers (MyGestureDetector onFling / onSingleTapConfirmed) — NOT CHECKED. | PROPOSED REACHABLE, conditional on (b) | label_134: AbstractFlashcardViewer.java:2640–2778; Reviewer.java:522–528 | None to the method; needs the S_REVIEWER ENTERS fix noted in label_137 before merge. |
| 4 | GraphicsWrap.<init> (label_135) | (a) ChartView.onDraw:64 `new GraphicsWrap(canvas, paint)` — CORRECT, re-printed (ChartView.java:64). (b) Gate `if (mDataIsSet)` at :59 — CORRECT, re-printed (:57–64); setData sets it at :85–88, re-printed. (c) S_STATISTICS FRAMEWORK → ChartView.onDraw and S_STATISTICS ENTERS — NOT CHECKED (graph_def.py:7657 / :11196 cited, not re-printed). | PROPOSED REACHABLE, conditional on (c) | label_135: GraphicsWrap.java:33–37; ChartView.java:56–70 | None to the method; S_STATISTICS entry still needs a printed check before merge. |
| 5 | GraphicsWrap.setClip (label_135) | (a) ChartView.onDraw:68 `g.setClip(...)` — CORRECT, re-printed (ChartView.java:68), under the mDataIsSet gate at :59 (CORRECT). (b) GraphicsWrap.setClip body, claimed empty at :76–78 — NOT CHECKED (those lines were not re-printed in this check). (c) S_STATISTICS entry — NOT CHECKED, as in row 4. | PROPOSED REACHABLE, conditional on (b)+(c) | label_135: GraphicsWrap.java:76–78; ChartView.java:68 | None; re-print GraphicsWrap.java:76–78 before merge to confirm the empty-body claim. |
| 6 | TranslationActivity.translate (label_136) | (a) TranslationActivity$1.onClick:162 `translate()` — CORRECT, re-printed (TranslationActivity.java:153–163). (b) translate body: setCancelable :205, setOnCancelListener :206, computeAddress() :208 — all CORRECT, re-printed (:196–217). (c) S_TRANSLATION GUI → $1.onClick (graph_def.py:6356) and the INTENT entry into TranslationActivity — NOT CHECKED (not re-printed). | PROPOSED REACHABLE, conditional on (c) | label_136: TranslationActivity.java:153–164, 196–217; graph_def.py:6356 | None to the method; entry step (c) still needs printing before merge. |
| 7 | LoadPronounciationActivity.onLoadPronunciation (label_136) | (a) LoadPronounciationActivity$1.onClick:123 `onLoadPronunciation(v)` — CORRECT, re-printed (LoadPronounciationActivity.java:119–126). (b) Body: showProgressDialog :162, computeAddressOfTranslationPage() :164 — CORRECT, re-printed (:154–175). (c) S_LOAD_PRONOUNCIATION GUI → $1.onClick (graph_def.py:6265) — NOT CHECKED. | PROPOSED REACHABLE, conditional on (c) | label_136: LoadPronounciationActivity.java:119–126, 154–175; graph_def.py:6265 | None to the method; entry step (c) still needs printing before merge. |
| 8 | Reviewer.addNote (label_137) | (a) Reviewer.onOptionsItemSelected:220 `addNote()` — CORRECT, re-printed (Reviewer.java:218–221). (b) addNote body :230–234, Intent to NoteEditor + startActivityForResultWithAnimation — CORRECT, re-printed. (c) S_REVIEWER GUI → onOptionsItemSelected (graph_def.py:1399) and the new S_REVIEWER ENTERS edge — NOT CHECKED (label_137.py not re-fetched). | PROPOSED REACHABLE, conditional on (c) | label_137: Reviewer.java:125, 220, 230–234; graph_def.py:1399 | Proposed (not merged, not verified here): the S_REVIEWER ENTERS edge claimed in label_137.py; verify that file and the graph_def entry before merge. |
| 9 | Whiteboard.touchStart (label_137) | (a) Whiteboard.handleTouchEvent:118 `touchStart(x, y)` on ACTION_DOWN — CORRECT, re-printed (Whiteboard.java:112–120); touchStart body at :195–200, re-printed. (b) Reviewer$1.onTouch:469 `mWhiteboard.handleTouchEvent(event)` — CORRECT, re-printed (Reviewer.java:461–470). (c) S_REVIEWER GUI → Reviewer$1.onTouch and the whiteboard-creation step (createWhiteboard) — NOT CHECKED. | PROPOSED REACHABLE, conditional on (c) | label_137: Whiteboard.java:112–118, 195; Reviewer.java:453–463 | None to the method; entry/creation steps still need printing before merge. |
| 10 | YAxis.drawMarkers (label_137) | (a) YAxis.paint:185 `drawMarkers(g)` — CORRECT, re-printed (YAxis.java:185–186); it is unconditional in the printed body (the `if (isOnFrame)` at :164 guards only a comment line, and the isAutoTic block at :166–174 does not gate :185–186 — the part's "least certain" note on this point is consistent with the re-print). (b) drawMarkers branches: drawRightMarker :217, drawLeftMarker :220, drawNumberingOnRightSide :224, drawNumbering :226 — CORRECT, re-printed (YAxis.java:213–227). (c) Upstream PlotSheet / DrawableContainer → YAxis.paint chain — NOT CHECKED (not re-printed; ChartView.onDraw:69–70 `mPlotSheet.paint(g)` was re-printed but does not by itself reach YAxis.paint). | PROPOSED REACHABLE, conditional on (c) | label_137: YAxis.java:156–187, 193; PlotSheet.java:322–328, 352–368, 472–474 (part citations, not re-printed) | None to the method; print the PlotSheet/DrawingContainer caller steps before merge. |

## Counts

- Methods judged: 10
- Proposed REACHABLE: 10
- Proposed UNREACHABLE: 0
- Fully verified for merge: 0 (every route has at least one NOT CHECKED upstream/entry step)
- Steps re-printed and judged CORRECT: all immediate-caller/body steps listed above; no step
  re-printed in this check was judged WRONG.
- Steps marked NOT CHECKED (part citation or graph_def line only, no re-print):
  all S_REVIEWER / S_STATISTICS / S_TRANSLATION / S_LOAD_PRONOUNCIATION entry and
  framework-dispatch steps, and all label_*.py e() edges.
- Rows not judged: 150 (the remaining rows of labels 134–137).

## Caveats / follow-ups for the parent

1. Do NOT merge any of the 10 on this report alone: each needs its NOT CHECKED
   entry step printed (graph_def.py lines are too large to fetch whole; a targeted
   grep/checkout is needed, which this connector-only check did not do).
2. The S_REVIEWER and S_STATISTICS ENTERS gaps flagged in label_137 affect rows 3, 4, 5, 8, 9
   (and, via ChartView, row 10's upstream chain); label_137.py's claimed fix edges
   were not re-fetched and remain unverified here.
3. No batch is finished by this report; it is a proposal file only, saved locally,
   not pushed, per the task.
