# R1 Summary — LibreTorrent batches 85/26 and 86/7 (Stream A Phase 3 completion)

## Verdict rule applied to both rows

If the full-scope grep is zero for a row AND no layout binding expression
names it AND no framework/library dispatch print names it, the verdict is
UNREACHABLE `no_trigger_in_app` INFERRED. If any printed caller or binding
expression names it, the verdict is REACHABLE with the printed site and
confirmed_by SOURCE if the line names the method itself, else INFERRED. If
the grep scope itself is incomplete (a directory missing or unfetchable),
the row is held OPEN with the exact gap named — never a claimed zero that
was not run. **Neither row is held OPEN: every tasked directory was present
and grepped.**

## Verdicts

| Row | Method | Verdict | Kind | confirmed_by |
|---|---|---|---|---|
| 85/26 | `ColorView.getColor()` (zero-arg) | **UNREACHABLE** | `no_trigger_in_app` | INFERRED |
| 86/7 | `ExpansionHeader.setText(int)` | **UNREACHABLE** | `no_trigger_in_app` | INFERRED |

## Scope grepped (identical for both rows)

- `corpus/java/` — 281 Java files on disk (includes the 252-file app tree
  plus feedparser 28, NanoHTTPD 1, and the rest of the on-disk tree).
- `corpus/res-layout/` — 73 layout XML files.
- `corpus/other-sourcesets-src/` — present, 20 files (13 androidTest +
  7 test). Note: the listing file names 21 entries; the one entry not on
  disk is `src/play/AndroidManifest.xml`, a play-sourceset manifest, not a
  test/androidTest Java file, and it cannot contain a Java call or layout
  binding expression for either row — not a scope gap for these verdicts.
- `phase3/res/` — present, 29 files (menu / menu-large-land-notouch /
  menu-sw600dp-land / xml).
- Extra check beyond the tasked scope: sibling `corpus/res/` (73 files) —
  zero `getColor` / `setText` hits.

## Evidence in one paragraph per row

- **85/26 `ColorView.getColor()`:** zero-arg `.getColor()` in the full Java
  scope returns exactly 5 lines, none on a `ColorView` receiver — 4×
  `AddTagState.getColor()` (`AddTagDialog:123,154`,
  `AddTagViewModel:59,61`) and 1× `Paint.getColor()` inside the definition
  itself (`ColorView.java:103`); all other `.getColor(` hits take arguments
  (`TypedArray` / `ContextCompat` / `Resources`). The only `ColorView`
  receivers in code are the two `binding.color.setColor(...)` sites
  (row 29); `AddTagDialog:153 binding.color` is a `RelativeLayout` row,
  not the `ColorView`. Layouts: zero literal `getColor` in 73 layouts; the
  sole color binding expression, `dialog_add_tag.xml:68`
  `app:color="@{viewModel.state.color}"`, reads `AddTagState.getColor`,
  not `ColorView.getColor`. No framework/library dispatch print names it.
  (Correction to the work file: 3 `ColorView` layouts exist, and
  `dialog_add_tag.xml` does have a `<data>` block — the verdict is
  unaffected, as shown.)
- **86/7 `ExpansionHeader.setText(int)`:** the only two `ExpansionHeader`
  receivers (`MainActivity.tagsGroupHeader`, `DrawerExpandableAdapter
  .groupHeader`) have no `setText(int)` call between them —
  `tagsGroupHeader` never calls `setText` at all, and
  `groupHeader.setText(group.name)` at `:205` passes a `String`
  (`DrawerGroup.java:34`), i.e. the CharSequence overload (row 86/8).
  Every int-argument `.setText(` elsewhere is typed to another receiver
  (`TabLayout.Tab`, `SwitchBar` self, `AddTagButton` self, a `TextView`, or
  the inner `textView` inside the definition body at `:94`). Layouts:
  zero literal `setText` in 73 layouts; `ExpansionHeader` elements carry
  only static `expansion_text`/`expansion_textAppearance` attributes, and
  `expansion_text` is read as a `String` in `init` and forwarded via
  `textView.setText(String)` (`:146`), never via `setText(int)`. No
  framework/library dispatch print names it.

## Grep files cited (all under `phase3/verdicts/R1/`)

- `grep_85_26_getColor_fullscope.txt` — `.getColor(` / zero-arg
  `.getColor()` / bare `getColor`, split by scope (corpus vs
  other-sourcesets), with exit codes.
- `grep_86_7_setText_fullscope.txt` — `.setText(` / bare `setText`, split
  by scope, with exit codes.
- `grep_receivers_ColorView_ExpansionHeader.txt` — all `ColorView` /
  `ExpansionHeader` / `tagsGroupHeader` / `groupHeader` mentions and the
  bare-`setText` sweep.
- `grep_receiver_typing.txt` — receiver-type proofs (`AddTagState`,
  `DrawerGroup.name: String`, `SwitchBar extends SwitchCompat`,
  `AddTagButton extends Chip`, `summaryView: TextView`,
  `binding.color` sites).
- `grep_layout_binding.txt` — full `ColorView` / `ExpansionHeader` /
  `getColor` / `setText` / `<data>` / `@{` sweep over 73 layouts, 29
  phase3/res files, 20 other-sourcesets files, and sibling `corpus/res`.
- `grep_layout_binding_targeted.txt` — the 6 `ColorView`/`ExpansionHeader`
  layouts in full, every `@{...color}` expression, `BindingAdapter`
  inventory, and the other-sourcesets manifest note.
- Per-row verdict files: `85_26.md`, `86_7.md` (this file: `R1_SUMMARY.md`).

## What would change each verdict

- **85/26 → REACHABLE:** any printed caller on a `ColorView`-typed
  receiver (Java code, or a layout binding expression whose receiver is a
  `ColorView` and which names `getColor`), or any framework/library
  dispatch print naming `ColorView.getColor`. Confirmed_by SOURCE if the
  line names the method itself, else INFERRED.
- **86/7 → REACHABLE:** any printed caller passing an int resource id to
  an `ExpansionHeader` receiver, any layout binding expression naming
  `ExpansionHeader.setText` with an int argument, or any framework/library
  dispatch print naming `ExpansionHeader.setText(int)`. Same
  SOURCE/INFERRED rule.
- Neither verdict is changed by: the existing `state.getColor()` calls
  (wrong receiver type), the existing `groupHeader.setText(group.name)`
  call (wrong overload — `String`), the `dialog_add_tag`
  `viewModel.state.color` expression (wrong receiver type), the inner
  `textView.setText(...)` lines inside `ExpansionHeader` (definition body /
  `init`, not external callers), or any further zero grep.

## Hygiene

- No work file under `phase3/work/` was edited; no push was made; no
  branch edit was made; no token appears anywhere in these files.
- Nothing in this directory claims a build, sample, or eight-check result
  — this task was grep-and-verdict only, and the verdicts rest solely on
  the saved greps above.
