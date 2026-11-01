# ROUTE_UNSCRIPTABLE_17 — Card.toString (AnyMemo route_17)

Status: unscriptable (no script in the D3 push bundle).
ROUTES.csv change: route_17's status cell `scripted` →
`unscriptable: DAO-failure state cannot be created by adb on an AOSP
emulator (Card.toString fires only in the RuntimeException at
LearnQueueManager.java:267 when cardDao.update returns 0; this chain's
flush is the build-time flush with an empty dirtyCache, and deleting
the card trips the earlier :263 LearningData check first)`.
No script-code change: the route_17.py helper script is mechanically
sound and is EXCLUDED from the push bundle, not modified. No label,
edge, or route change; the method's verification.csv label is
untouched by this reclassification.

## Route

Method: Card.toString. Edges (26, from ROUTES.csv):
Eddc920eb Ee33f0797 E0b0115b9 Ed9aa2280 Efe6c7871 E006becde
E48c9d4a5 Ef4267162 E25e1518b E0336067c E3cdfa763 E0195fc37
Ebf2205c3 E367b72be Ed19034c7 E9519dc75 E8c752a9d Ef70a2160
Edf66ce54 E3c38d575 E2754f845 E3580f705 E7fd725c8 Ea89c981a
E25410e53 Ecb92bfef. Printed route ref:
queue/LearnQueueManager.java:267.

## Why it cannot be driven by adb with the delivered harness

Card.toString fires only inside the RuntimeException message at
queue/LearnQueueManager.java:267 (`"CardDao update failed. Card to
update: " + card`), inside LearnQueueManager$1$1.call (:255-273),
which drains `dirtyCache` on AnyMemoExecutor's single thread. Three
facts, each re-verified from printed source in the rework session,
close every deterministic induction avenue:

1. This chain's flush is the BUILD-time flush (Builder.build at :360
   → refill → flushDirtyCache at :170). At build time dirtyCache is
   empty: the only dirtyCache producer is LearnQueueManager.update
   (:184, `dirtyCache.put(card)` at :193), called after grading
   (StudyActivity.java:608 and QuizActivity.java:422, both with
   DB-loaded cards); the only refill() call sites in the app source
   are update() (:198) and build() (:360). An empty dirtyCache means
   the :258 loop body never runs on this chain, so cardDao.update is
   never called.
2. cardDao.update returns 0 only when no row with the card's id
   exists. A card graded through the UI was loaded from the same
   database, so its row exists. The second update() caller
   (QuizActivity) has the same property (a quiz card loaded from
   the db).
3. Deleting the card does not help: CardDaoImpl.delete
   cascade-deletes the learning data FIRST (refresh + delete of the
   learning data before the card row itself), so a deleted card
   trips the EARLIER check at :263 (learningDataDao.update == 0,
   throwing with the LearningData string) and never reaches the :267
   Card.toString throw. The remaining flush call site (release() at
   :127) drains the same graded-card dirtyCache, so it opens no new
   avenue; and the flush runs promptly on the single-thread executor
   after any update, leaving no deterministic window to delete a card
   between load and flush through the UI. No fixture path populates
   dirtyCache with a nonexistent card either: every dirtyCache entry
   comes from update() on a DB-loaded card.

This is structurally uninducible, not merely unimplemented: unlike a
scripted route with an uncertain outcome, there is no UI action,
fixture, setup step, or harness primitive that puts the system into
the failing state. The honest status is unscriptable with a reason.

## Printed source lines relied on

- queue/LearnQueueManager.java:258 — `while (!dirtyCache.isEmpty())`
  (flush loop; empty at build time, so the body never runs).
- queue/LearnQueueManager.java:261-263 — learningDataDao.update == 0
  check and LearningData throw (earlier check, reached first).
- queue/LearnQueueManager.java:265-267 — cardDao.update == 0 check
  and Card throw (`"CardDao update failed. Card to update: " + card`,
  i.e. Card.toString via string concatenation).
- queue/LearnQueueManager.java:170 — flushDirtyCache() call inside
  refill(); :184/:193 — update() / dirtyCache.put(card); :198 —
  refill() call inside update(); :127 — release() flush;
  :358/:360 — Builder.build() / qm.refill().
- StudyActivity.java:608, QuizActivity.java:422 — update() callers
  after grading, both with DB-loaded cards (per the H34 audit's
  independent re-verification; not re-printed in this rework
  session, which re-printed the LearnQueueManager chain itself).

## D7 consequence

If a device run ever records this route, it records not-reached →
unclear, never wrong. No label change follows from any device
outcome on this route.

## Cap arithmetic

This reclassification makes AnyMemo 3/30 unscriptable = 10.0%,
exactly at (not over) the D3 10% per-app cap (routes 02, 08, 17).
The D1 audit must re-verify the cap arithmetic on the amended
ROUTES.csv before the D3 push (flagged by the H34 audit; the
amended ROUTES.csv in this rework dir is the file to check).

## Revert condition

Revert only on a demonstrated deterministic induction (a replay
step, fixture, or harness primitive that provably puts a
nonexistent card into dirtyCache on this chain) or on a coordinator
decision overriding the H34 audit, recorded as such. The
ROUTES_NOTES.md "Route_17 stays scripted" decision paragraph (with
its own revert condition — "if the auditor or device lead judges
that a script that cannot reach its target must be unscriptable,
flip route_17") is the condition that has now fired: the H34
auditor so judged, so this note supersedes that paragraph at
push-assembly time, and the push continuation must update
ROUTES_NOTES.md accordingly (status line 28 scripted / 2
unscriptable → 27 scripted / 3 unscriptable, 10.0%).
