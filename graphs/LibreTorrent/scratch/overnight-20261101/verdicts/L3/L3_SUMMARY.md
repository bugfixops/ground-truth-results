# Stream A Phase 3 — Group L3 summary: generated bindings (batches 58–70)

**Scope judged: 81 OPEN rows, all flipped, 0 staying OPEN.**
- D14 abstract getters → UNREACHABLE `no_trigger_in_app` INFERRED: **16**
- D15 setVariable → UNREACHABLE `no_trigger_in_app` INFERRED: **20**
- D16 onFieldChange → UNREACHABLE `no_trigger_in_app` INFERRED: **3** (58/34, 62/37, 66/8)
- D4c pattern test, onFieldChange → UNREACHABLE `no_trigger_in_app` INFERRED: **1** (67/7)
- D17 hasPendingBindings → REACHABLE INFERRED: **41** (all OPEN hasPendingBindings rows in 58–70, together)
- Total: 81 judged, 81 flipped, 0 OPEN remainders within the L3 kinds.

**Files:** one verdict file per batch under `phase3/verdicts/L3/batch<N>.md`
(58: 4 rows, 59: 7, 60: 6, 61: 6, 62: 7, 63: 6, 64: 6, 65: 8, 66: 9, 67: 10,
68: 4, 69: 5, 70: 3). Saved greps under `phase3/greps/L3/`. No batch file,
work file, or DECISIONS.md was edited. No push, no branch edit, no tick marker.

## Shared grep evidence (local corpus: 281 app-Java files + 73 res layouts + 20 test-sourceset files)

- `greps/L3/getters_appjava.txt` — **0 lines**: zero `.getViewModel(` / `.getDetailError(` hits in 281 app-Java files.
- `greps/L3/getters_broad.txt` — **0 lines**: zero `getViewModel|getDetailError` hits in app Java + res XML + test sourcesets (covers method-reference/non-call syntax too).
- `greps/L3/setVariable_appjava.txt` — **0 lines**: zero `.setVariable(` hits in 281 app-Java files.
- `greps/L3/onFieldChange_appjava.txt` — **0 lines**: zero `.onFieldChange(` hits in 281 app-Java files.
- `greps/L3/hasPendingBindings_appjava.txt` — **0 lines**: zero `hasPendingBindings` hits in 281 app-Java files.
- `greps/L3/test_sourcesets_hits.txt` — **0 lines**: zero getter/setVariable/onFieldChange/hasPendingBindings hits in test sourcesets (excluded by D23 in any case).
- `greps/L3/typed_setters_appjava.txt` — 15 lines: every printed typed setter in the app tree
  (setViewModel × 14 sites, setDetailError × 1 at ErrorReportDialog:69). A printed typed setter
  is zero evidence its setVariable ran (D4d direction) and zero evidence its getter ran (D4a field-read).
- `greps/L3/includes_full.txt` — all 15 `<include>` elements in all 73 res layouts. Only
  variable pass-through in the entire res tree is `app:viewModel="@{viewModel}"` to
  `@layout/add_torrent_info` (fragment_add_torrent_info.xml, base + both variants). Note: this
  project uses the `app:` namespace for the pass-through, NOT `bind:` — a literal `bind:` grep
  (`greps/L3/bind_attrs_resxml.txt`, 0 lines) would have missed it; the include-block grep is the
  operative check. The pass-through belongs to the already-REACHABLE 59/32
  (AddTorrentInfoBindingImpl.setVariable) and to no OPEN row: no OPEN setVariable row's layout is
  an include target (targets are only toolbar, main_drawer_content, add_torrent_info,
  detail_torrent_appbar).
- `greps/L3/data_variables.txt` — `<data>` variable declarations (or NO `<data>`) for all 73 layouts.

## D17 — ViewDataBinding rebind print outcome: QUERY FOUND → all 41 flip to REACHABLE INFERRED

Print: `ViewDataBinding.java`, platform/frameworks/data-binding, master branch,
blob `70c79c41354afe54c2f30e52944c01f8341999b6`, package `android.databinding`
(upstream of `androidx.databinding`), fetched as page text 2026-11-01 from
https://android.googlesource.com/platform/frameworks/data-binding/+/master/extensions/library/src/main/java/android/databinding/ViewDataBinding.java
(full excerpt saved in `greps/L3/viewdatabinding_rebind_print.txt`).

Exact rebind path (rendered line numbers from the fetch):
- `mRebindRunnable.run()` ends with `executePendingBindings();` (rendered L348).
- `mFrameCallback.doFrame()` calls `mRebindRunnable.run()` (rendered L474–480).
- `ROOT_REATTACHED_LISTENER.onViewAttachedToWindow` calls `binding.mRebindRunnable.run()` (rendered L282–288).
- `requestRebind()` posts the frame callback via Choreographer (SDK ≥ 16) or the runnable via Handler (rendered L894–920).
- `executePendingBindings()` body (rendered L676–690):
  `public void executePendingBindings() {`
  `  if (mIsExecutingPendingBindings) { requestRebind(); return; }`
  `  if (! hasPendingBindings()) { return; }` ← **rendered L686: the query**
  `  mIsExecutingPendingBindings = true; … if (! mRebindHalted) { executeBindings(); … }`
  `  mIsExecutingPendingBindings = false; }`
- `hasPendingBindings` declared abstract (rendered L768): `public abstract boolean hasPendingBindings();`

Reading: the query is a virtual call on `this`, so it dispatches polymorphically to each
generated `*BindingImpl` override. Every created Impl reaches it via ctor `invalidateAll()`
(D4e) → `requestRebind()` → Choreographer frame callback → `mRebindRunnable` →
`executePendingBindings()`. Per the D17 binary rule, all 41 OPEN hasPendingBindings rows
(58/32; 59/2, 59/13, 59/27; 60/9, 60/17, 60/25, 60/35; 61/20, 61/35; 62/9, 62/35; 63/6, 63/20;
64/1, 64/10, 64/19, 64/28, 64/38; 65/11, 65/22, 65/33; 66/5, 66/17, 66/29;
67/5, 67/15, 67/27, 67/38; 68/7, 68/16, 68/25, 68/34; 69/3, 69/12, 69/21, 69/30, 69/39;
70/8, 70/17, 70/26) flip together to REACHABLE INFERRED, with no split — including variant
Impls (creation stands under D4b) and no-variable-layout Impls (their ctors still call
invalidateAll). App-tree callers being zero is consistent, not the basis.

**Version caveat (does not block the flip, recorded for the merger):** the print is the
master-branch upstream file, not a pinned `androidx.databinding:databinding-runtime` release
version — no pinned androidx raw source URL was returned by search, so none is cited. The
`executePendingBindings → hasPendingBindings()` query is the same shape in the
databinding-runtime 4.0.1 analysis and the API-23 copy found in search, and no version was
found in which `executePendingBindings` does NOT query `hasPendingBindings()`. If the merger
requires a pinned androidx release print, that is the one follow-up print owed for D17.

## D18 — 67/7 pattern test: ALL FOUR ELEMENTS HOLD → UNREACHABLE under D4c

Row 67/7 (FragmentDetailTorrentPeerListBindingImpl.onFieldChange), layout
`fragment_detail_torrent_peer_list.xml`:
- (i) Layout declares NO `<data>` variable — verified from printed XML
  (`greps/L3/data_variables.txt`; layout has no `<data>` block; its only `@{...}` expression
  is a static dimen sum, `@{@dimen/fab_size + @dimen/fab_margin}`, referencing no variable).
- (ii) NO `<include>` parent passes a variable to it — no `<include>` anywhere targets
  `fragment_detail_torrent_peer_list` (`greps/L3/includes_full.txt`).
- (iii) Zero `.setVariable(` / `.onFieldChange` hits in the complete tree
  (`greps/L3/setVariable_appjava.txt`, `greps/L3/onFieldChange_appjava.txt`, both 0 lines).
- (iv) No typed-setter call on that binding — DetailTorrentPeersFragment inflates (:84) and
  uses view fields only (`binding.peerList`, `binding.emptyViewPeerList`); no setViewModel
  for this binding appears in `greps/L3/typed_setters_appjava.txt`.
→ 67/7 flips to UNREACHABLE `no_trigger_in_app` INFERRED under D4c. Its companion 67/8
(setVariable) flips under D15 on the same zero-call + no-include evidence.

## D18 — 58/34, 58/35: PREMISE FAILURE RECORDED, verdicts unchanged in outcome

The task/DECISIONS text states 58/34 and 58/35 do not extend under D4c because "their layout
declares a viewModel variable". **Printed XML contradicts that reason for these two rows:**
`activity_add_torrent.xml` (the ActivityAddTorrentBindingImpl layout) declares NO `<data>`
block at all (`greps/L3/data_variables.txt`), and no qualified variant of it exists. The
viewModel-declaring layout in batch 58 is `activity_filemanager_dialog.xml` (row 58/37's
layout), not `activity_add_torrent.xml` — the D18 reason appears misattributed between the
two batch-58 bindings. This is reported, not re-decided: per the task instruction, 58/34 and
58/35 were judged under D15/D16, not D4c, and both flip to UNREACHABLE anyway —
58/35 under D15 (zero `.setVariable(` + no include targets `activity_add_torrent`), 58/34
under D16(a) (no variable, no typed setter, no observable registration; AddTorrentActivity
uses view fields only). A merger that corrects the attribution would reach the same labels
via D4c for these two rows; no row depends on the disputed premise for its outcome.

## D16 detail (other rows)

- 62/37 (DialogErrorBindingImpl.onFieldChange): D16(b) — variable `detailError` IS set
  (ErrorReportDialog:69 `setDetailError`), but `dialog_error.xml` declares it type `String`
  with a plain `android:text="@{detailError}"` expression (:66): a non-observable, so no
  field-change registration exists for it.
- 66/8 (FragmentDetailTorrentBindingImpl.onFieldChange): D16(a) — `fragment_detail_torrent.xml`
  declares NO `<data>`; DetailTorrentFragment inflates (:150) and uses view fields only, no
  typed setter; its only include (`detail_torrent_appbar`) passes NO variable.

## Rows NOT judged (out of L3 kinds, flagged for the coordinator)

- **66/7 (FragmentDetailTorrentBindingImpl.onChangeAppbar)** — the only other OPEN binding row
  in batches 58–70. It is a child-appbar `onChange*` callback, not a getter / setVariable /
  onFieldChange / hasPendingBindings row, so it is outside the L3 kinds as assigned. It stays
  OPEN with resolver: a printed observable registration for the appbar child binding (its
  layout binds no observable; see batch 66's own note). No other OPEN binding row in 58–70
  was found outside the judged set (verified by scanning all OPEN table rows for "Binding").
- Rows already REACHABLE/UNREACHABLE in 58–70 were not re-judged, including standing 59/32
  (setVariable via parent `app:viewModel` pass-through) and all D4c-unreachable 68–70
  setVariable/onFieldChange rows. All OPEN rows in scope were already normalised to `—`
  (no confirmed_by fix needed).

## Premises applied, not re-decided

- D4a field-read premise (generated `executeBindings` reads the field, never the abstract
  getter) and the D14 library premise (databinding library never calls typed getters; it uses
  the base `ViewDataBinding` API) were applied as decided. No local copy of the databinding
  library exists in the corpus to grep (final_java_only on the branch holds app source, not the
  library); the D17 print corroborates the base-API half (library code calls the abstract
  `hasPendingBindings()`, not typed getters).
- No additional res XML needed a connector fetch: the local corpus already holds all 73 res
  layouts (fetched fresh from the branch in Phase 1), so no connector call was made in this
  task and no 429 was hit.

## Blockers

None for these 81 rows. Single follow-up print owed (non-blocking, see D17 caveat): a pinned
androidx databinding-runtime release copy of `ViewDataBinding.executePendingBindings` if the
merger requires a version-pinned print rather than the master upstream print.
