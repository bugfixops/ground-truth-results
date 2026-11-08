# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AmazeFileManager — non-Glide contradiction group (PROPOSED, NOT MERGED, NOT PUSHED)

Status: **PROPOSED ONLY. No label was flipped, no file in
`bugfixops/ground-truth-results` was edited, nothing was pushed.**
This check was connector-only, on branch `work-2026-10-31` only.
No token was used, no git clone was made, and no
`graph_def.py` / `out/` / `progress/` / `tools/` file was touched.

## Rules followed

- Tool coverage was used ONLY as a pointer to which methods to look at,
  never as evidence for a verdict. The build report's contradiction list
  (`graphs/AmazeFileManager/out/build_report.txt`) is the pointer:
  6 methods labelled UNREACHABLE but ran in a tool run, plus 1
  ENV-gated-but-ran method.
- `confirmed_by` is SOURCE only where app lines were printed in this
  check, otherwise INFERRED. Never DYN / FW-MEMORY / UNVERIFIED.
- No framework claim below rests on a printed `fw_src/` line, because
  none was printed in this check. Framework dispatch steps (RecyclerView
  binding, TextView watcher dispatch, Bundle marshalling, Activity
  instantiation, DialogFragment lifecycle) are therefore standard /
  INFERRED, not FW-SRC, wherever a route depends on them.
- UNREACHABLE was NOT assigned to any method here, because no
  whole-source-folder caller hunt was completed in this check (see
  "Search-code failure" below). Methods without a printed caller chain
  are OPEN, not UNREACHABLE.
- Baseline (from the locally already-present build report, not
  re-derived): AmazeFileManager 2981 methods, 2509 REACHABLE /
  472 UNREACHABLE, route checks not started.

## Fetch method (spaced, single-file only)

Files were fetched ONE at a time via
`/opt/hatch/bin/github call-read-tool --name get_file_contents`
(owner `bugfixops`, repo `ground-truth-results`,
ref `refs/heads/work-2026-10-31`), with ~20 s between fetches.
No HTTP 429 was hit in this check. No burst fetching was done.

Source root for every path below:

`final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/`

Files printed via the connector, in order:

1. `adapters/data/IconDataParcelable.java`
2. `adapters/data/LayoutElementParcelable.java`
3. `ui/views/RoundedImageView.java`
4. `utils/SimpleTextWatcher.java`
5. `activities/TextEditorActivity.java`
6. `adapters/RecyclerAdapter.java`
7. `adapters/holders/ItemViewHolder.java`
8. `ui/dialogs/RenameBookmark.java`
9. `fragments/MainFragment.java`

Local-only inputs (already on this VM, NOT re-fetched):
`~/workspace/wp2-amaze/scratch/graphs__AmazeFileManager__method_list.json`
(2981 methods; class paths and descriptors below come from it),
`graphs__AmazeFileManager__out__build_report.txt`,
`graphs__AmazeFileManager__scratch__unreachable_analysis.txt`,
`graphs__AmazeFileManager__scratch__unreach_lines.json`
(graph_def.py line pointers only — graph_def.py itself was NOT
fetched, it is too large for `get_file_contents`),
and the earlier `WP2_AmazeFileManager_first_set_route_checks.md`.

### Search-code failure (important caveat)

`search_code` returned `total_count: 0, incomplete_results: true`
for `setImageBroken` and for `SimpleTextWatcher` — terms that are
definitely present in this repo (both defining files were printed
in this same check, and `setImageBroken` occurs in RecyclerAdapter).
This matches the first-set report's finding that `search_code`
returns 0 for this repo. **A `search_code` 0/incomplete result was
therefore used as evidence of absence NOWHERE in this report.**
Every positive caller below comes from a fully printed file, and
every OPEN verdict below is open precisely because a whole-folder
grep could not be done connector-only.

## Per-method verdicts

| # | Method (descriptor from method_list.json) | Old label (per build report) | Verdict in this check | Evidence |
|---|---|---|---|---|
| 1 | `IconDataParcelable.setImageBroken` `(Z)V` | UNREACHABLE but ran | **REACHABLE (proposed)** | SOURCE: RecyclerAdapter method-reference call sites + `OnImageProcessed` calls; INFERRED: RecyclerView binding head |
| 2 | `LayoutElementParcelable.writeToParcel` `(Landroid/os/Parcel;I)V` | UNREACHABLE but ran | **REACHABLE (proposed)** | SOURCE: MainFragment `putParcelableArrayList`; INFERRED: Bundle marshalling + lifecycle head |
| 3 | `RoundedImageView.setBackgroundColor` `(I)V` | UNREACHABLE but ran | **REACHABLE (proposed)** | SOURCE: RecyclerAdapter `iconBackground` selection + cast; INFERRED: RecyclerView binding head |
| 4 | `SimpleTextWatcher.afterTextChanged` `(Landroid/text/Editable;)V` | UNREACHABLE but ran | **OPEN** | RenameBookmark overrides it without a super call; no other registration printed; no whole-folder hunt |
| 5 | `SimpleTextWatcher.beforeTextChanged` `(Ljava/lang/CharSequence;III)V` | UNREACHABLE but ran | **REACHABLE (proposed)** | SOURCE: RenameBookmark registrations that do NOT override it; INFERRED: TextView dispatch + dialog-show head |
| 6 | `SimpleTextWatcher.onTextChanged` `(Ljava/lang/CharSequence;III)V` | UNREACHABLE but ran | **REACHABLE (proposed)** | Same as #5 |
| 7 | `TextEditorActivity.<init>` `()V` | REACHABLE, ENV-gated but ran (not a contradiction entry) | **OPEN (ENV-gate question unanswered)** | SOURCE: no constructor, no gate in TextEditorActivity.java itself; gate text not printed; do NOT change label on coverage alone |

Verdict counts: **REACHABLE proposed 5, OPEN 2, UNREACHABLE 0,**
of 7 methods. No method is verified for merge on this report alone:
each REACHABLE proposal still needs the merger's build / C1 checks
and, where noted, the route head to ENTRY.

## 1. IconDataParcelable.setImageBroken — REACHABLE (proposed)

### Printed defining source

`adapters/data/IconDataParcelable.java` — plain setter, no caller
in its own file:

```java
public void setImageBroken(boolean imageBroken) {
    isImageBroken = imageBroken;
}
```

with the matching getter `isImageBroken()` and the field
`private boolean isImageBroken = false;`. The class also parcels
that flag in its own `writeToParcel` (`parcel.writeInt(isImageBroken
? 1 : 0)`), which is consistent with the flag being set and later
read — but the setter's route is below, not the parcel code.

### Printed caller chain (SOURCE)

`adapters/RecyclerAdapter.java`:

- The setter is passed as a method reference, not called directly.
  List branch, IMAGE/VIDEO with thumbnails:
  `:595-596` `showThumbnailWithBackground(holder, rowItem.iconData,
  holder.pictureIcon, rowItem.iconData::setImageBroken);`
  and `:598-599` (same call with `holder.apkIcon`); APK branch
  `:608-609` (same call with `holder.apkIcon`).
  Grid branch: `:724` `showRoundedThumbnail(holder, rowItem.iconData,
  holder.imageView1, rowItem.iconData::setImageBroken);`
  and `:733` (same call with `holder.genericIcon`).
- Both receivers take it as an `OnImageProcessed` parameter:
  `showThumbnailWithBackground` signature at `:856-857`
  `(ItemViewHolder viewHolder, IconDataParcelable iconData, ImageView
  view, OnImageProcessed errorListener)`;
  `showRoundedThumbnail` signature at `:902-903` with the same
  fourth parameter.
- The interface, `:1029-1031`:
  ```java
  public interface OnImageProcessed {
      void onImageProcessed(boolean isImageBroken);
  }
  ```
  Its single method `(Z)V` matches `setImageBroken`'s descriptor
  `(Z)V` exactly, so the method reference implements it.
- The interface method is actually invoked on that parameter in
  both receivers, in three places each:
  - `showThumbnailWithBackground`: `:864`
    `errorListener.onImageProcessed(true);` (already-broken early
    return), `:883` (Glide `onLoadFailed`), `:895`
    `errorListener.onImageProcessed(false);` (Glide
    `onResourceReady`).
  - `showRoundedThumbnail`: `:912` (already-broken early return),
    `:930` (`onLoadFailed`), `:941` (`onResourceReady`, `false`).

Chain: `RecyclerAdapter.onBindViewHolder`
→ `showThumbnailWithBackground` / `showRoundedThumbnail`
→ `OnImageProcessed.onImageProcessed(boolean)`
→ `IconDataParcelable.setImageBroken(boolean)`.
The `onBindViewHolder` → adapter step itself is RecyclerView
framework dispatch (INFERRED, standard; no `fw_src` line printed),
and the full route from ENTRY through MainFragment to the adapter
was not printed in this check — that head is the merger's remaining
step, not a reason to doubt the method-reference link, which is
printed in full.

Why the old label was wrong on printed source: the graph evidently
missed method-reference edges. A `::setImageBroken` argument is a
real call site even though no `setImageBroken(...)` call text
appears in RecyclerAdapter.

### Proposed fix (NOT applied)

Delete the UNREACHABLE entry for `IconDataParcelable.setImageBroken`
(local pointer: `unreach_lines.json` gives graph_def.py line 14064;
merger to verify against a local checkout). Add, if absent:

```python
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.showThumbnailWithBackground', 'CALL',
  'list bind passes iconData::setImageBroken as OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:595-596, 598-599, 608-609')
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.showRoundedThumbnail', 'CALL',
  'grid bind passes iconData::setImageBroken as OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:724, 733')
e('RecyclerAdapter.showThumbnailWithBackground', 'IconDataParcelable.setImageBroken', 'CALL',
  'errorListener.onImageProcessed(...) invokes the method reference passed at the call site',
  evidence='SRC adapters/RecyclerAdapter.java:864, 883, 895')
e('RecyclerAdapter.showRoundedThumbnail', 'IconDataParcelable.setImageBroken', 'CALL',
  'errorListener.onImageProcessed(...) invokes the method reference passed at the call site',
  evidence='SRC adapters/RecyclerAdapter.java:912, 930, 941')
```

(Use the graph's existing node-naming convention for the interface
step if it models `OnImageProcessed.onImageProcessed` as its own node;
the substantive edge is the method-reference resolution above.)

## 2. LayoutElementParcelable.writeToParcel — REACHABLE (proposed)

### Printed defining source

`adapters/data/LayoutElementParcelable.java` — `writeToParcel`
writes, in order, `filetype`, `iconData` via
`p1.writeParcelable(iconData, 0)`, `title`, `desc`, `permissions`,
`symlink`, `isDirectory`, `date`, `header`, `dateModification`,
`size`, `longSize`, `isBack`, mirroring the `Parcel` constructor
that reads them back. No direct app call to `writeToParcel` exists
in its own file — as expected for a `Parcelable` callback; the
call comes from framework marshalling (see below).

### Printed caller chain (SOURCE + INFERRED marshalling)

`fragments/MainFragment.java`:

- `:153` `private ArrayList<LayoutElementParcelable> LIST_ELEMENTS;`
- `:397-398` `public void onSaveInstanceState(Bundle outState) {`
  `super.onSaveInstanceState(outState);`
- `:402` guard: `if (listView != null) {` — the parcel-list line
  below runs only when the list view exists.
- `:415` `outState.putParcelableArrayList("list", LIST_ELEMENTS);`

`putParcelableArrayList` itself stores the objects in the Bundle;
it does not synchronously call `writeToParcel`. The `writeToParcel`
call happens when that saved-state Bundle is actually written to a
Parcel by the framework (FragmentManager / activity state save, e.g.
on configuration change or process recreation). That marshalling
step is standard framework behaviour but is INFERRED here — no
`fw_src` line was printed — and `onSaveInstanceState` being called
at all is likewise lifecycle dispatch (INFERRED). What IS printed
(SOURCE) is the app-side trigger: a real `ArrayList` of real
`LayoutElementParcelable` objects is handed to a Bundle in
`onSaveInstanceState`, so any state save parcels them.

Chain: framework lifecycle → `MainFragment.onSaveInstanceState`
→ `Bundle.putParcelableArrayList("list", LIST_ELEMENTS)`
→ framework Bundle marshalling (INFERRED)
→ `LayoutElementParcelable.writeToParcel(Parcel, int)` for each
element. Side note, not a separate verdict: that method's
`writeParcelable(iconData, 0)` then parcels each element's
`IconDataParcelable`, so this same route also exercises
`IconDataParcelable.writeToParcel` (not in this group).

Why the old label was wrong on printed source: the graph evidently
had no edge from the `putParcelableArrayList` site to
`writeToParcel`. Parcelable callbacks are never called by app code
directly; absence of a direct call site is not absence of a route.

### Proposed fix (NOT applied)

Delete the UNREACHABLE entry for
`LayoutElementParcelable.writeToParcel` (local pointer:
`unreach_lines.json` gives graph_def.py line 11155; merger to
verify). Add, if absent:

```python
e('MainFragment.onSaveInstanceState', 'LayoutElementParcelable.writeToParcel', 'FRAMEWORK',
  'outState.putParcelableArrayList("list", LIST_ELEMENTS); Bundle marshalling calls writeToParcel on each element when the saved-state Bundle is written to a Parcel',
  evidence='SRC fragments/MainFragment.java:397, 402, 415; LIST_ELEMENTS is ArrayList<LayoutElementParcelable> at :153')
```

If the merger's convention uses CALL rather than FRAMEWORK for
Bundle-marshalling edges, keep the same src/dst/evidence and change
only the kind — and record the marshalling step as INFERRED, not
FW-SRC, until a `fw_src` line is printed.

## 3. RoundedImageView.setBackgroundColor — REACHABLE (proposed)

### Printed defining source

`ui/views/RoundedImageView.java` — the class extends `ImageView`
and overrides:

```java
@Override
public void setBackgroundColor(int color) {
    background.setColor(color);
}
```

where `background` is its own `Paint` field (initialised to
`Color.TRANSPARENT` in the `(Context, AttributeSet)` constructor).
Note: the override does NOT call `super.setBackgroundColor(color)`;
it only recolours the paint that `onDraw` uses to draw the icon
background circle. That is the method's observable effect, and it is
exactly why a call through a `View` reference still lands here when
the runtime object is a `RoundedImageView`.

### Printed caller chain (SOURCE)

`adapters/RecyclerAdapter.java` (grid branch of
`onBindViewHolder`) plus `adapters/holders/ItemViewHolder.java`:

- `ItemViewHolder.java` field declarations (printed):
  `public final RoundedImageView pictureIcon;`
  `public final ImageView genericIcon, apkIcon;`
  `public final ImageView imageView1;`
  `public final RelativeLayout iconLayout;`
  So `genericIcon` is statically an `ImageView`, but see the cast.
- `RecyclerAdapter.java:716`, in the grid branch, unconditionally:
  `((RoundedImageView) holder.genericIcon).setRelativeSize(1.25f, 1.25f);`
  That cast executes on every grid bind, so `holder.genericIcon`
  IS a `RoundedImageView` at runtime in the grid layout (otherwise
  every grid bind would throw `ClassCastException`).
- `RecyclerAdapter.java:742`:
  `View iconBackground = getBoolean(PREFERENCE_USE_CIRCULAR_IMAGES)
  ? holder.genericIcon : holder.iconLayout;`
  i.e. when the circular-images preference is on, `iconBackground`
  is that same `RoundedImageView`; when off, it is the
  `RelativeLayout` (`iconLayout`), and calls on it do NOT reach
  this override.
- Calls on `iconBackground` in the grid `onBindViewHolder` body:
  `:744` `iconBackground.setBackgroundColor(iconSkinColor);`
  (directory case; further `setBackgroundColor` calls for video /
  audio / pdf / code / text / archive / apk / go-back colours follow
  in the same block).
- The same selection repeats inside `showRoundedThumbnail`:
  `:905` and `:916`
  `View iconBackground = getBoolean(PREFERENCE_USE_CIRCULAR_IMAGES)
  ? viewHolder.genericIcon : viewHolder.iconLayout;`
  with calls at `:908` (`grey_color`, already-broken branch),
  `:925` (`grey_color`, Glide `onLoadFailed`), `:940`
  (transparent, Glide `onResourceReady`).

Chain (guarded): grid view + `PREFERENCE_USE_CIRCULAR_IMAGES` true
→ `iconBackground == holder.genericIcon`, a `RoundedImageView`
(cast at `:716`) → virtual dispatch on
`iconBackground.setBackgroundColor(...)`
→ `RoundedImageView.setBackgroundColor(int)`. The
`onBindViewHolder` head is RecyclerView dispatch (INFERRED), as in §1.

### What was deliberately NOT cited as proof

- `RecyclerAdapter.java:723`
  `holder.imageView1.setBackgroundColor(Color.BLACK);` (dark/black
  theme, grid IMAGE/VIDEO branch). `imageView1` is statically an
  `ImageView` (`ItemViewHolder.java`), and its runtime type cannot
  be determined from Java source alone — the layout XML is not in
  `final_java_only` (Java only) and was not printed. That line may
  or may not reach the override; it is NOT part of this verdict.
- `iconBackground.setBackgroundColor(...)` in the non-circular
  branch (`iconLayout`, a `RelativeLayout`) resolves to
  `View.setBackgroundColor`, not this override. Only the circular
  branch is claimed.

### Proposed fix (NOT applied)

Delete the UNREACHABLE entry for
`RoundedImageView.setBackgroundColor` (local pointer:
`unreach_lines.json` gives graph_def.py line 13206; merger to
verify). Add, if absent:

```python
e('RecyclerAdapter.onBindViewHolder', 'RoundedImageView.setBackgroundColor', 'CALL',
  'grid branch: iconBackground is holder.genericIcon when PREFERENCE_USE_CIRCULAR_IMAGES, and genericIcon is a RoundedImageView (cast at :716); virtual dispatch reaches the override',
  evidence='SRC adapters/RecyclerAdapter.java:716, 742, 744')
e('RecyclerAdapter.showRoundedThumbnail', 'RoundedImageView.setBackgroundColor', 'CALL',
  'iconBackground is viewHolder.genericIcon when PREFERENCE_USE_CIRCULAR_IMAGES; virtual dispatch reaches the override',
  evidence='SRC adapters/RecyclerAdapter.java:905, 908, 916, 925, 940')
```

Guard to record on both edges if the graph models it:
grid view + `PREFERENCE_USE_CIRCULAR_IMAGES` true.

## 4–6. SimpleTextWatcher trio — two REACHABLE (proposed), one OPEN

### Printed defining source

`utils/SimpleTextWatcher.java`, in full (short file):

```java
public class SimpleTextWatcher implements TextWatcher {

    @Override
    public void beforeTextChanged(CharSequence s, int start, int count, int after) {

    }

    @Override
    public void onTextChanged(CharSequence s, int start, int before, int count) {

    }

    @Override
    public void afterTextChanged(Editable s) {

    }
}
```

All three base methods are empty. That matters for dispatch: a
watcher instance that does NOT override a given callback executes
the base (empty) method for that callback; a watcher that DOES
override it executes the override instead, and the base runs only
if the override calls `super`.

### Printed registration sites (SOURCE)

`ui/dialogs/RenameBookmark.java` (a `DialogFragment`, imports
`SimpleTextWatcher` at `:19`):

- `:86-93`:
  ```java
  conName.addTextChangedListener(new SimpleTextWatcher() {
      @Override
      public void afterTextChanged(Editable s) {
          if (conName.getText().toString().length() == 0)
              t1.setError(s2);
          else t1.setError("");
      }
  });
  ```
- `:112-119`:
  ```java
  ip.addTextChangedListener(new SimpleTextWatcher() {
      @Override
      public void afterTextChanged(Editable s) {
          if (ip.getText().toString().length() == 0)
              t2.setError(s1);
          else t2.setError("");
      }
  });
  ```

Both anonymous subclasses override ONLY `afterTextChanged`. Neither
overrides `beforeTextChanged` or `onTextChanged`, and neither
override calls `super.afterTextChanged(...)`. This is corroborated
by `method_list.json`: `RenameBookmark$1` and `RenameBookmark$2`
list only `<init>` and `afterTextChanged` — no `beforeTextChanged`
or `onTextChanged` entries for either subclass.

### 5. beforeTextChanged — REACHABLE (proposed)

When the user edits `conName` or `ip`, TextView framework dispatch
calls all three watcher callbacks on the registered watcher
(INFERRED standard dispatch; no `fw_src` line printed). For
`beforeTextChanged` there is no override, so dispatch resolves to
`SimpleTextWatcher.beforeTextChanged` (empty, but executed).
Chain: `RenameBookmark.onCreateDialog` → `addTextChangedListener`
(anonymous `SimpleTextWatcher`, `:86`, `:112`) → framework TextView
dispatch on text change (INFERRED) →
`SimpleTextWatcher.beforeTextChanged`. Head caveat: who shows the
RenameBookmark dialog was not printed in this check, so the route
head to ENTRY is INFERRED (dialog shown from the bookmarks UI);
the registration + non-override facts themselves are SOURCE.

Proposed fix (NOT applied): delete the UNREACHABLE entry for
`SimpleTextWatcher.beforeTextChanged` (local pointer:
`unreach_lines.json` gives graph_def.py lines 14477–14479; merger
to verify) and add, if absent:

```python
e('RenameBookmark.onCreateDialog', 'SimpleTextWatcher.beforeTextChanged', 'FRAMEWORK',
  'anonymous SimpleTextWatcher registered on conName/ip overrides only afterTextChanged, so TextView dispatch calls the base beforeTextChanged',
  evidence='SRC ui/dialogs/RenameBookmark.java:86-93, 112-119')
```

### 6. onTextChanged — REACHABLE (proposed)

Identical reasoning to §5, same sites: no override exists in either
anonymous subclass, so TextView dispatch on text change resolves to
`SimpleTextWatcher.onTextChanged`.

Proposed fix (NOT applied): delete the UNREACHABLE entry for
`SimpleTextWatcher.onTextChanged` (local pointer:
`unreach_lines.json` gives graph_def.py lines 14481–14483; merger
to verify) and add, if absent:

```python
e('RenameBookmark.onCreateDialog', 'SimpleTextWatcher.onTextChanged', 'FRAMEWORK',
  'anonymous SimpleTextWatcher registered on conName/ip overrides only afterTextChanged, so TextView dispatch calls the base onTextChanged',
  evidence='SRC ui/dialogs/RenameBookmark.java:86-93, 112-119')
```

### 4. afterTextChanged — OPEN (not REACHABLE, not UNREACHABLE)

The two printed RenameBookmark watchers do NOT help the base
method: their `afterTextChanged` overrides contain no `super`
call, so dispatch on those instances never reaches
`SimpleTextWatcher.afterTextChanged`. The base method would run
only for a registered watcher instance that does not override
`afterTextChanged` (a plain `new SimpleTextWatcher()`, or a
subclass overriding only the other two callbacks), or for an
override elsewhere that calls `super.afterTextChanged(...)`.
No such site was printed in this check, and no whole-folder hunt
was completed (search_code is broken for this repo, see above),
so:

- Do NOT flip it to REACHABLE on tool coverage alone (the task's
  explicit rule, and the RenameBookmark evidence actually cuts the
  other way for these two instances).
- Do NOT confirm it UNREACHABLE either: that would require exactly
  one kind + reason + source reference backed by a real
  whole-folder caller hunt, which was not done.
- One graph hygiene note for the merger (conditional, to verify in
  a local checkout): the local `unreachable_analysis.txt` lists
  `SimpleTextWatcher.afterTextChanged` with source
  `RenameBookmark$1.afterTextChanged`. IF the graph contains an edge
  `RenameBookmark$1.afterTextChanged ->
  SimpleTextWatcher.afterTextChanged`, that edge is unsupported on
  printed source — the printed override at
  `RenameBookmark.java:88-92` contains no `super.afterTextChanged`
  call — and should be deleted. Deleting that edge does not by
  itself settle the label; the label stays OPEN pending the hunt.

What would resolve it: a full-repo grep (local checkout) for
`SimpleTextWatcher` registrations / `extends SimpleTextWatcher`
plus `addTextChangedListener` sites, checking each subclass's
override set and any `super.afterTextChanged` call; or a printed
plain-`SimpleTextWatcher` registration site.

Proposed fix: NONE for the label. Leave the current UNREACHABLE
entry unmerged-as-verified and the method OPEN until that hunt is
done. (Local pointer: `unreach_lines.json` gives graph_def.py
lines 15928–15933.)

## 7. TextEditorActivity.<init> — OPEN (ENV-gate question unanswered)

### What was printed

`activities/TextEditorActivity.java` (full file printed):

- Class header: `public class TextEditorActivity extends
  ThemedActivity implements TextWatcher, View.OnClickListener {`
- **No constructor is declared anywhere in the file.** The
  `<init> ()V` in `method_list.json` is therefore the implicit
  default constructor (implicit `super()` to `ThemedActivity`).
  There is no `<init>` body to inspect for a gate.
- **No ENV gate, permission check, or instantiation condition
  appears in this file.** `onCreate` branches only on theme
  (`AppTheme.DARK` / `BLACK`), on `Build.VERSION.SDK_INT`
  (KITKAT / LOLLIPOP guards for system-bar tinting and circular
  reveal), and on whether the launch `Intent` carries data
  (`getIntent().getData()` null → toast + `finish()`). None of
  those gates instantiation of the activity itself, and none is an
  environment gate of the kind the build report means by
  "ENV-gated".
- The file does show the activity registering itself as a
  `TextWatcher` (`searchEditText.addTextChangedListener(this)` and
  `mInput.addTextChangedListener(this)` in `onCreate`) — that is
  about `TextEditorActivity`'s own watcher callbacks, not about
  `<init>`, and is not used for any verdict here.

### What was NOT printed, and why the gate cannot be judged here

- The build report's "ENV-gated but ran" claim is about the best
  route TO `<init>` in the graph, i.e. about an ENV edge on that
  route — not about anything inside `TextEditorActivity.java`.
  The ENV gate's text, and the edge carrying it, live in
  `graph_def.py`, which could not be fetched connector-only
  (too large for `get_file_contents`) and was not printed.
- The launch path was only partially printed:
  `MainFragment.onListItemClicked` (printed, `:851`) falls through
  to `FileUtils.openFile(new File(e.desc), ...)` at `:933` for
  ordinary files, which is the plausible route toward opening a
  text file in `TextEditorActivity` — but `FileUtils.openFile` /
  `openunknown`, the `Intent` construction, the manifest
  intent-filter declaring `TextEditorActivity`, and the framework
  Activity-instantiation step were NOT printed in this check.
- `TextEditorActivity.<init>` has no entry in the local
  `unreach_lines.json` (it is not an UNREACHABLE entry), consistent
  with the build report treating it as REACHABLE-but-ENV-gated
  rather than as a contradiction entry.

### Verdict

**OPEN.** Specifically:

- Do NOT change the label on tool coverage alone.
- Do NOT confirm the ENV gate as correctly recorded, and do NOT
  correct it, on the evidence printed here — the gate text itself
  is unknown to this check.
- Do NOT claim the file contains an ENV gate: it does not, in the
  sense above. If the merger finds the ENV edge is on the
  Intent-launch route (e.g. a condition on file type / viewer
  resolution / preference), that edge's correctness must be judged
  against the printed launch site + manifest, not against
  `TextEditorActivity.java` alone.

What would resolve it (local checkout required):
1. Print the `graph_def.py` edges into
   `TextEditorActivity.<init>` and identify the ENV edge and its
   exact ENV text.
2. Print the manifest entry for `TextEditorActivity` and the
   `FileUtils.openFile` / `openunknown` body that builds the
   launch `Intent`.
3. Check whether the ENV condition was actually satisfied in the
   tool run's environment (in which case "gated but ran" is
   consistent and the gate may be correctly recorded), or was not
   satisfied (in which case the gate is wrong / too strong and
   needs a proposed correction with a cited launch-site line).
Until then, the ENV-gate question stays OPEN.

Proposed fix: NONE.

## Summary for the merger

- 5 REACHABLE proposals, each with a printed app-side caller chain
  and an explicitly INFERRED framework step (never FW-SRC):
  `setImageBroken` (method reference → interface call),
  `writeToParcel` (`putParcelableArrayList` → Bundle marshalling),
  `setBackgroundColor` (circular-images branch → virtual dispatch
  to the override), `beforeTextChanged` and `onTextChanged`
  (RenameBookmark watchers that override only `afterTextChanged`).
- 2 OPEN: `SimpleTextWatcher.afterTextChanged` (RenameBookmark
  overrides do not call super; needs a whole-folder registration
  hunt) and `TextEditorActivity.<init>` (ENV gate text and launch
  route not printed; needs a local checkout of `graph_def.py` +
  manifest + `FileUtils`).
- 0 UNREACHABLE verdicts in this check, by the stated rule.
- No label was flipped by this report, no repo file was edited,
  nothing was pushed. All fix fragments above are proposals in
  `graph_def.py` `e(...)` syntax for the merger, to be verified
  against a local checkout and the build / C1 checks before any
  merge.
