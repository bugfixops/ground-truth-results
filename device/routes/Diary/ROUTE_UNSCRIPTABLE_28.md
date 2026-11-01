# Diary route_28: UNSCRIPTABLE (merger decision Diary-D3-28)

Method: `Diary.getNextCalendarMonth`
Route: route_28 in `device/routes/Diary/ROUTES.csv`
Edges (7, in route order):
`Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E55f6b52d E7a3bcc72 E38e0b13b`
Printed route: `overnight/stream-D/Diary/scratch/route_steps.txt`,
section "Diary.getNextCalendarMonth"; edge details in
`graphs/Diary/out/diary_trigger_graph.json` (same edge ids).

No script is written for this route, deliberately: its only path to
the target is a multi-pointer fling, and the delivered D2 harness
offers no multi-pointer action.

## The gate

Edge `E55f6b52d` (`S_DIARY_VIEW` ->
`Diary$GestureListener.onFling@MULTI`) requires a fling right after
a touch with 2+ pointers (`multi == true`), and edge `E7a3bcc72`
requires a vertical fling up (|dy| >= |dx|, |dy| > 256 px,
|vy| > 256 px/s, dy < 0) reaching `onSwipeUp`, which calls
`getNextCalendarMonth` (Diary.java:3027-3031).

Printed handler source (all in the Diary app slice,
`final_java_only/Diary/app/Diary-#v1.105/src/main/`):

- `Diary.java:841-842` (`dispatchTouchEvent`): `multi` is set to
  true only when `event.getPointerCount() > 1`.
- `Diary.java:3440-3441` (`GestureListener.onFling`): `if (!multi)
  return result;` — a single-pointer fling returns before any
  swipe handler runs.
- `Diary.java:3471-3477`: the vertical-fling branch calls
  `onSwipeUp()` when dy < 0; `Diary.java:3485` resets
  `multi = false` after the fling.
- `getNextCalendarMonth` has no other caller in the app slice
  (definition Diary.java:2929-2930; only call Diary.java:3030
  from `onSwipeUp`), and `onSwipeUp` has no other caller (only
  Diary.java:3475 from `onFling`).

## Why no harness action can drive it

The D2 harness (`device/harness/harness.py`, `Runner`) offers only:
launch, tap/long_tap by text/res_id/desc (fixed x/y only with a why
string), type_text, key, back, scroll_to, wait_for, start_intent,
broadcast, grant/deny, push_fixture, screenshot, dump_ui,
assert_text, comment. None produces a two-pointer touch, so `multi`
can never become true, and `onFling` returns early for every
single-pointer gesture the harness can make. `scroll_to` issues a
single-pointer swipe, which fails the same `!multi` guard. No
intent, broadcast, or key reaches `onSwipeUp` (it is only called
from `onFling`).

## Cap consequence (for the coordinator / device lead)

With this row, Diary has 5 unscriptable routes of 30 (01, 02, 04
widget placement; 14 I/O error on save; 28 multi-pointer fling) =
16.7%, over the D3 acceptance cap of at most 10% per app (3/30).
Meeting the cap needs a harness extension, not a re-scripting:
widget placement alone would bring it to 2/30; fling/multi-touch
plus the route_14 directory-fixture avenue together would bring it
to 3/30. Until one of those lands, D3 for Diary is scripts-complete
but acceptance-blocked on the cap prong. This is recorded as
decision Diary-D3-CAP for coordinator decision (harness extension
vs. accepted deviation); it is not waived here.
