# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AmazeFileManager — Glide contradiction group

**Status: PROPOSAL ONLY — UNVERIFIED. No label flipped, nothing pushed, no repo file edited.**
**Repo:** `bugfixops/ground-truth-results`, branch `work-2026-10-31` only.
**Method:** connector-only. Every fetch was ONE `github call-read-tool get_file_contents`
call at a time, spaced ~5–8 s apart. No burst, no `git clone`, no token, no push.
No HTTP 429 was hit during this task. `search_code` was tried once and abandoned:
it searches GitHub globally and ignores the repo scoping, so it is useless here and
was used as evidence for nothing. `get_file_contents` on a directory path returns
the directory listing (that is how the listings below were obtained).

**Source root (all paths below are relative to it unless stated):**
`final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/`

**Contradiction under test (from the task, NOT re-proved here):** the 15 methods
below are labelled UNREACHABLE in the graph but ran in a tool run. Tool coverage is
NEVER evidence, only a pointer — no verdict below rests on it.

## Verdict counts (of 15)

| Verdict | Count | Methods |
|---|---|---|
| REACHABLE | 2 | `GlideRequest.listener` (SOURCE), `GlideRequests.as` (INFERRED delegation step, SOURCE app call sites) |
| UNREACHABLE | 0 | — (see coverage caveat: the whole source tree was NOT printed, so no UNREACHABLE verdict is licensed) |
| OPEN | 13 | `GlideOptions.<init>`, `GlideOptions.apply`, `GlideOptions.autoClone`, `GlideOptions.clone`, `GlideOptions.lock`, `GlideRequest.addListener`, `GlideRequest.apply`, `GlideRequest.downsample`, `GlideRequest.optionalCenterInside`, `GlideRequest.optionalFitCenter`, `GlideRequest.set`, `GlideRequest.transform(Transformation)`, `GlideRequests.setRequestOptions` |

**Headline:** only `GlideRequest.listener` is resolved on printed app source alone.
`GlideRequests.as` is resolved only if the merger accepts the standard generated-code
delegation `asDrawable() → as(Class)` as an INFERRED step (the generated file itself
is NOT in `final_java_only` — see §4). Everything in the `GlideOptions` group stays
OPEN: there is no printed app-source call site for any of it, and the one `.clone()`
in the app is on a `GlideRequest` receiver, not a `GlideOptions` receiver (this
corrects a `label_1.md` error, §5).

## 1. Per-method table

Descriptors are copied from `graphs/AmazeFileManager/method_list.json`
(local scratch copy already printed by an earlier helper; not re-fetched).

| # | Method (desc) | Verdict | confirmed_by | Reason / printed route |
|---|---|---|---|---|
| 1 | `GlideOptions.<init>` `()V` | OPEN | — | No `new GlideOptions()`, no `GlideOptions.` reference at all in any printed file. Only plausible route is unprinted generated code (see §4). What would resolve it: print build-generated `GlideRequests.java` and check for a `new GlideOptions()` static field / wrapping call, plus a receiver-typed grep of the unprinted dirs (§6). |
| 2 | `GlideOptions.apply` `(BaseRequestOptions;)GlideOptions` | OPEN | — | Zero `.apply(` calls on any receiver in the printed corpus. The `label_1.md` claim that it is "called on GlideRequest objects from AppsAdapterPreloadModel" is wrong: that file contains no `.apply(`. Hypothesis only: generated `GlideRequests.setRequestOptions` wrapping (`new GlideOptions().apply(...)`) — unprinted. |
| 3 | `GlideOptions.autoClone` `()GlideOptions` | OPEN | — | No printed call site, no printed caller. Hypothesis only: invoked from generated `GlideRequest`/options chaining — unprinted. Resolver: print generated `GlideRequest.java` + the Glide library `BaseRequestOptions` for the app's Glide version (not in `fw_src`, §4). |
| 4 | `GlideOptions.clone` `()GlideOptions` | OPEN | — | **Not** the `.clone()` in `AppsAdapterPreloadModel.java:44` — that receiver is declared `GlideRequest<Drawable>` (line 24), so it is `GlideRequest.clone`, a different method that is not in this contradiction list. No printed `GlideOptions.clone` site exists. |
| 5 | `GlideOptions.lock` `()GlideOptions` | OPEN | — | No printed call site. Hypothesis only: the Glide library locks the request's options object when building a request — but whether that object is a `GlideOptions` at runtime depends on unprinted generated `GlideRequest` code. Resolver as for #3. |
| 6 | `GlideRequest.addListener` `(RequestListener;)GlideRequest` | OPEN | — | No `.addListener(` on any Glide receiver in the printed corpus. `RecyclerAdapter` uses `.listener(...)` (replace), never `.addListener(...)` (add). A `RequestListener` *implementation* existing (RecyclerAdapter ~:872–:941) is not an `addListener` call. Resolver: receiver-typed grep of unprinted dirs for `.addListener(` on a `GlideRequest`/`RequestBuilder` receiver. |
| 7 | `GlideRequest.apply` `(BaseRequestOptions;)GlideRequest` | OPEN | — | Zero `.apply(` calls in the printed corpus (see §2, note N3). `label_1.md`'s "part of Glide request building chain" is unsupported by any printed line. Resolver: receiver-typed grep of unprinted dirs; any printed `.apply(` on a `GlideRequest`-backed receiver would resolve it by the same virtual-dispatch logic as #9. |
| 8 | `GlideRequest.downsample` `(DownsampleStrategy;)GlideRequest` | OPEN | — | Zero `.downsample(` in the printed corpus. Resolver: receiver-typed grep of unprinted dirs. |
| 9 | `GlideRequest.listener` `(RequestListener;)GlideRequest` | **REACHABLE** | SOURCE | Printed route (§3, R1). Confirms the prior first-set finding; it is re-derived below from printed lines, not copied. |
| 10 | `GlideRequest.optionalCenterInside` `()GlideRequest` | OPEN | — | Zero occurrences in the printed corpus. Printed code calls `centerCrop()` / `fitCenter()` (non-optional variants) only. Resolver: receiver-typed grep of unprinted dirs. |
| 11 | `GlideRequest.optionalFitCenter` `()GlideRequest` | OPEN | — | Same as #10. |
| 12 | `GlideRequest.set` `(Option,Object;)GlideRequest` | OPEN | — | No `GlideRequest.set` call site identified in printed files. (A bare `.set(` grep was deliberately NOT run: it is non-specific and fails rule C5. Any `.set(` hit would still need a receiver-type check.) Resolver: receiver-typed grep of unprinted dirs for `.set(` with a `GlideRequest` receiver and a `com.bumptech.glide.load.Option` first argument. |
| 13 | `GlideRequest.transform(Transformation)` `(Transformation;)GlideRequest` | OPEN | — | Zero `.transform(` calls in the printed corpus. The word "transform" in `RecyclerAdapter` is only a code comment ("transform icon on press"), not a call. Resolver: receiver-typed grep of unprinted dirs. (Only the single-`Transformation` overload is judged here; the `Class+Transformation` and array overloads are separate methods and were not in the contradiction list.) |
| 14 | `GlideRequests.as` `(Class;)GlideRequest` | **REACHABLE** | INFERRED (delegation step) / SOURCE (app call sites) | Two printed `asDrawable()` call sites (§3, R2) on receivers of declared type `GlideRequests` (the return type of `GlideApp.with(...)`). In Glide's generated API, `asDrawable()` is implemented as `as(Drawable.class)`; that delegation step is INFERRED because generated `GlideRequests.java` is not in `final_java_only` and could not be printed (§4). A merger requiring SOURCE-only should hold this as OPEN pending generated-source printout. |
| 15 | `GlideRequests.setRequestOptions` `(RequestOptions;)V` | OPEN | — | No printed call site and no printed caller. No app file calls `setDefaultRequestOptions` / `setRequestOptions` in the printed corpus, and no printed library line calls it either (Glide library source is not in `fw_src`). Hypothesis only: generated override wrapping non-`GlideOptions` arguments — unprinted. Resolver: print generated `GlideRequests.java`. |

## 2. Printed call-site register (receiver-typed; a bare method name is never a site)

All line numbers are from files printed in this task via the connector, except
entries marked "already printed in scratch", which were re-checked by grep in this
task from the local scratch copies (same repo/branch) and whose line numbers below
are the grep-verified ones.

| # | File:line | Code (abridged) | Receiver type as declared | Which Glide method it actually is |
|---|---|---|---|---|
| C1 | `adapters/RecyclerAdapter.java:390` (already printed in scratch) | `preloader = new RecyclerViewPreloader<>(GlideApp.with(mainFrag), modelProvider, sizeProvider, GlideConstants.MAX_PRELOAD_FILES);` | `GlideApp.with(Fragment)` returns `GlideRequests` | `GlideApp.with` (not in list); `GlideRequests` object passed to library `RecyclerViewPreloader` |
| C2 | `adapters/RecyclerAdapter.java:524–527, 694–697` (already printed) | `GlideApp.with(mainFrag).clear(holder.genericIcon);` (×8 views) | `GlideRequests` | `GlideRequests.clear` via library `RequestManager` (not in list) |
| C3 | `adapters/RecyclerAdapter.java:738, 860, 869, 909, 919` (already printed) | `GlideApp.with(mainFrag).load(...).into(...);` | `GlideRequests` → `GlideRequest` (generated `load` override; step INFERRED) | `GlideRequest.load` / `.into` (not in list) |
| C4 | `adapters/RecyclerAdapter.java:899, 945` (already printed) | `modelProvider.getPreloadRequestBuilder(iconData).listener(requestListener).into(view);` | Declared return type `RequestBuilder<Drawable>`; runtime object is the `GlideRequest<Drawable>` field (see R1) | **`GlideRequest.listener`** — verdict #9 |
| C5 | `adapters/glide/RecyclerPreloadModelProvider.java:26, 30` (already printed) | `private GlideRequest<Drawable> request;` / `request = GlideApp.with(fragment).asDrawable().centerCrop();` | `GlideRequests` → `GlideRequest<Drawable>` | `GlideRequests.asDrawable` (not in list) → `GlideRequest.centerCrop` (not in list); the `asDrawable()` step is the SOURCE anchor for verdict #14 |
| C6 | `adapters/glide/RecyclerPreloadModelProvider.java: getPreloadRequestBuilder` (already printed) | `requestBuilder = request.load(...);` (3 branches) | `GlideRequest<Drawable>` field | `GlideRequest.load` (not in list); return value is what C4 calls `.listener()` on |
| C7 | `adapters/glide/AppsAdapterPreloadModel.java:24, 28` (already printed) | `private GlideRequest<Drawable> request;` / `request = GlideApp.with(f).asDrawable().fitCenter();` | `GlideRequests` → `GlideRequest<Drawable>` | `GlideRequests.asDrawable` (not in list) → `GlideRequest.fitCenter` (not in list); second SOURCE anchor for verdict #14 |
| C8 | `adapters/glide/AppsAdapterPreloadModel.java:44–45` (already printed) | `public RequestBuilder getPreloadRequestBuilder(String item) { return request.clone().load(item); }` | `GlideRequest<Drawable>` field | **`GlideRequest.clone`** — NOT `GlideOptions.clone` (verdict #4) and NOT in this contradiction list |
| C9 | `adapters/glide/AppsAdapterPreloadModel.java:48–49` (already printed) | `public void loadApkImage(String item, ImageView v) { request.load(item).into(v); }` | `GlideRequest<Drawable>` field | `GlideRequest.load` / `.into` (not in list) |
| C10 | `fragments/AppsListFragment.java:96–99` (already printed) | `modelProvider = new AppsAdapterPreloadModel(app);` + `new ListPreloader<>(GlideApp.with(app), modelProvider, sizeProvider, ...)` | `GlideRequests` | `GlideApp.with` (not in list); entry point for C7/C8 via list preloading |
| C11 | `adapters/CompressedExplorerAdapter.java:212, 218` (printed this task) | `GlideApp.with(compressedExplorerFragment).load(R.drawable.ic_arrow_left_white_24dp).into(holder.genericIcon);` / `GlideApp.with(compressedExplorerFragment).load(rowItem.iconData.image).into(holder.genericIcon);` | `GlideRequests` | `GlideRequest.load` / `.into` (not in list) |
| C12 | `AmazeFileManagerModule.java:17–23` (printed this task) | `@GlideModule public class AmazeFileManagerModule extends AppGlideModule { registerComponents(...) { registry.prepend(String, Drawable, new ApkImageModelLoaderFactory(...)); registry.prepend(String, Bitmap, new CloudIconModelFactory(...)); } }` | n/a (Glide framework calls `registerComponents`; dispatch INFERRED) | No generated-Glide method call; proves the two custom model loaders are registered, so their `buildLoadData` paths are live framework callbacks (library `ModelLoader` interface, not in list) |

**Negative results in printed files (class-name-aware grep, §6):**
zero occurrences of `.addListener(`, `.apply(`, `.transform(`, `.downsample(`,
`optionalCenterInside`, `optionalFitCenter`, `new GlideOptions`, or any
`GlideOptions` reference in the entire printed corpus (all files in §6).
Note N1: `RecyclerAdapter`'s `setOnClickListener` / `setOnLongClickListener` hits
are Android view listeners, not Glide calls, and were excluded by receiver type.
Note N2: `CloudIconDataFetcher` uses `BitmapFactory.Options` (local variable named
`options`) — that is NOT `GlideOptions` and NOT a `GlideRequest.set` call.
Note N3: the zero-`.apply(` claim covers every file listed in §6 that was grepped
with the method-specific patterns; it is a statement about the printed corpus
only, never about the unprinted remainder of the tree.

## 3. Printed routes for the two REACHABLE verdicts

### R1 — `GlideRequest.listener` (SOURCE)

1. `fragments/MainFragment.java:1108` (printed this task):
   `adapter = new RecyclerAdapter(getMainActivity(), ma, utilsProvider, sharedPref, listView, LIST_ELEMENTS, ma.getActivity());`
   (Launcher entry above this — activity/fragment creation — is standard Android
   lifecycle, INFERRED, as the task allows.)
2. `adapters/RecyclerAdapter.java:389` (already printed, grep-verified):
   `modelProvider = new RecyclerPreloadModelProvider(mainFrag, uris);`
   inside `setItems(...)` (called from the adapter's item-setting path).
3. `adapters/glide/RecyclerPreloadModelProvider.java:26, 30` (already printed):
   field `private GlideRequest<Drawable> request;` initialised by
   `request = GlideApp.with(fragment).asDrawable().centerCrop();`
   — so the object stored in `request` IS a `GlideRequest<Drawable>`.
4. `adapters/glide/RecyclerPreloadModelProvider.java: getPreloadRequestBuilder`
   (already printed): returns `request.load(...)` — still the same
   `GlideRequest` object, declared return type `RequestBuilder<Drawable>`.
5. `adapters/RecyclerAdapter.java:491` `onBindViewHolder` (already printed)
   calls `showThumbnailWithBackground(...)` (:595, :598, :608) and
   `showRoundedThumbnail(...)` (:724, :733) — RecyclerView binding dispatch to
   `onBindViewHolder` itself is framework dispatch, INFERRED.
6. `adapters/RecyclerAdapter.java:856–899` `showThumbnailWithBackground` and
   `:902–945` `showRoundedThumbnail` (already printed): each builds an anonymous
   `RequestListener<Drawable>` (:872–:895 and :922–:941) and ends with
   `modelProvider.getPreloadRequestBuilder(iconData).listener(requestListener).into(view);`
   (:899 and :945).
7. Dispatch step: the compile-time receiver type is the library
   `RequestBuilder<Drawable>`, but Java virtual dispatch invokes the override on
   the runtime object, which printed lines prove is a `GlideRequest<Drawable>`
   (steps 3–4). Hence the executed method is `GlideRequest.listener`
   `(RequestListener;)GlideRequest`. This is SOURCE-grounded (printed declared
   field type + printed call), not tool coverage.

### R2 — `GlideRequests.as` (SOURCE call sites + INFERRED delegation step)

1. `adapters/glide/RecyclerPreloadModelProvider.java:30` (already printed):
   `GlideApp.with(fragment).asDrawable()` — receiver of `.asDrawable()` is the
   `GlideRequests` object returned by `GlideApp.with(...)`.
2. `adapters/glide/AppsAdapterPreloadModel.java:28` (already printed):
   `GlideApp.with(f).asDrawable()` — same shape.
3. Delegation step (INFERRED, not printed): in Glide's generated API,
   `GlideRequests.asDrawable()` is implemented as `as(Drawable.class)`, i.e. it
   calls `GlideRequests.as(Class;)GlideRequest`. Both call sites above therefore
   reach `GlideRequests.as` through one generated-code step. The generated file
   could not be printed (§4), so this verdict is honestly marked INFERRED for
   that step. The `.load(...)` sites (C3, C11) are NOT claimed as `as` routes:
   whether generated `load` delegates through `asDrawable` was not printed and
   is not asserted.

## 4. Why the generated classes cannot be resolved from `final_java_only`

- Directory listing of the source root (printed this task) contains exactly one
  file at that level, `AmazeFileManagerModule.java`, plus subdirectories
  (`activities`, `adapters`, `asynchronous`, `database`, `exceptions`,
  `filesystem`, `fragments`, `ui`, `utils`, `JacocoInstrument`). There is NO
  `GlideApp.java`, `GlideRequest.java`, `GlideOptions.java`, or
  `GlideRequests.java` in the app source: these are annotation-processor
  generated at build time and are not in `final_java_only`.
- Repo root listing (printed this task) shows `fw_src/` contains only
  `android-8.1.0_r1` (AOSP framework). There is NO Glide library source in
  `fw_src`, so no library dispatch line (e.g. a library call to `lock()` /
  `clone()` / `apply()` on an options object, or a library call to
  `GlideRequests.setRequestOptions`) could be printed. All such steps therefore
  remain INFERRED at best, and where even the INFERRED step is not firmly
  anchored (GlideOptions group, `GlideRequests.setRequestOptions`) the verdict
  is OPEN, not REACHABLE.
- Consequence for the tool-run pointer: the tool run evidently executed generated
  and library code paths (that is the only way `GlideOptions.*` methods run at
  all, since no app line references `GlideOptions`). That pointer is consistent
  with the generated-code hypotheses in §1, but per the task it is not evidence,
  so it changes no verdict by itself.

## 5. Corrections to `label_1.md` Glide reasons (all 15 rows)

`label_1.md` marks all 15 REACHABLE, but its reasons do not survive a
receiver-typed re-check:

| `label_1.md` claim | Correction from printed source |
|---|---|
| `GlideOptions.<init>`: "GlideApp.with() calls return GlideOptions" | Wrong type: `GlideApp.with()` returns `GlideRequests`, not `GlideOptions`. No printed `GlideOptions` construction exists. → OPEN |
| `GlideOptions.apply`: "Called on GlideRequest objects from AppsAdapterPreloadModel", citing `:28` `asDrawable().fitCenter()` | `:28` contains no `.apply(` at all. → OPEN |
| `GlideOptions.autoClone` / `.lock`: "Called by Glide framework" | No printed caller of either method; framework dispatch is INFERRED, not a printed route. → OPEN |
| `GlideOptions.clone`: "Called explicitly in AppsAdapterPreloadModel.getPreloadRequestBuilder", citing `:44` `request.clone()` | `:44`'s receiver is declared `GlideRequest<Drawable>` (`:24`), so this is `GlideRequest.clone`, a different method. It is evidence for `GlideRequest.clone` (not in this list), not for `GlideOptions.clone`. → OPEN |
| `GlideRequest.addListener`: "Used in RecyclerAdapter", citing `RequestListener` implementations | A `RequestListener` implementation is not an `addListener` call. RecyclerAdapter calls `.listener(...)` (:899, :945), never `.addListener(...)`. → OPEN |
| `GlideRequest.apply` / `.downsample` / `.optionalCenterInside` / `.optionalFitCenter` / `.set` / `.transform(Transformation)`: "part of chain" / "Glide transformation method" / "option setter" | No printed call site for any of them in the printed corpus (§2, N-notes). Generic method descriptions are not routes. → OPEN |
| `GlideRequest.listener`: "Used in RecyclerAdapter for image load callbacks" | Directionally right, but now grounded properly: R1 above gives the full printed route + receiver-type dispatch argument. → REACHABLE (SOURCE) |
| `GlideRequests.as`: "Called by GlideApp.with().asDrawable() chain", citing the two `asDrawable()` sites | Right call sites, wrong precision: the printed call is `asDrawable()`, not `as()`. The `as()` step is generated-code delegation (INFERRED). → REACHABLE (INFERRED step) |
| `GlideRequests.setRequestOptions`: "Sets default options on GlideRequests" | A description of what the method does, not a call site. No printed caller. → OPEN |

Also corrected: the saved `scratch/glide_method_grep.txt` (per the task) greps bare
method names, e.g. `SharedPreferences.Editor.apply()` / `URLDecoder.decode`,
and therefore proves nothing about any Glide method. No verdict here uses it.
All greps in this task used class- or receiver-aware patterns
(`GlideApp|GlideRequest|GlideOptions`, `.load(`, `.into(`, `.listener(`,
`.addListener(`, `.apply(`, `.transform(`, `.downsample(`, `optional*`,
`new GlideOptions`, `.clone(`) over printed files only.

## 6. Coverage statement (what was printed, what was not)

**Printed in this task via the connector (one file at a time, spaced):**
root listing; `adapters/` listing; `adapters/glide/` listing;
`adapters/glide/apkimage/` listing; `fragments/` listing; `activities/` listing;
`utils/` listing; `utils/glide/` listing; repo-root listing; `fw_src/` listing;
`activities/superclasses/` listing (names only); `ui/` listing (names only);
full files: `AmazeFileManagerModule.java`,
`adapters/glide/apkimage/ApkImageModelLoader.java`,
`ApkImageModelLoaderFactory.java`, `ApkImageDataFetcher.java`,
`adapters/glide/RecyclerPreloadSizeProvider.java`,
`utils/glide/CloudIconModelLoader.java`, `CloudIconModelFactory.java`,
`CloudIconDataFetcher.java`, `utils/GlideConstants.java`,
`adapters/CompressedExplorerAdapter.java`, `adapters/HiddenAdapter.java`,
`adapters/ColorAdapter.java`, `fragments/MainFragment.java`,
`fragments/TabFragment.java`, `fragments/PropertiesSheet.java`,
`fragments/CloudSheetFragment.java`, `fragments/SearchWorkerFragment.java`,
`fragments/ProcessViewerFragment.java`, `fragments/DbViewerFragment.java`,
`fragments/FtpServerFragment.java`, `activities/MainActivity.java`.

**Already printed in `~/workspace/wp2-amaze/scratch/` and re-grepped in this task:**
`adapters/RecyclerAdapter.java`, `adapters/AppsAdapter.java`,
`adapters/glide/RecyclerPreloadModelProvider.java`,
`adapters/glide/AppsAdapterPreloadModel.java`,
`fragments/AppsListFragment.java`, `fragments/CompressedExplorerFragment.java`.

**NOT printed (so no absence claim covers them):**
`activities/DatabaseViewerActivity.java`, `TextEditorActivity.java`,
`PreferencesActivity.java`, `activities/superclasses/*`,
`fragments/preference_fragments/*`, `ui/*` (dialogs, icons, views, colors,
notifications), `adapters/data/*`, `adapters/holders/*`, `filesystem/*`,
`asynchronous/*`, `database/*`, `exceptions/*`, `utils/*` other than
`GlideConstants.java` and `utils/glide/*`, and all generated/build outputs.
**Therefore: zero UNREACHABLE verdicts.** Every OPEN verdict below stays OPEN
until its resolver in §1 is run over the unprinted remainder (or generated
source is printed).

## 7. Proposed fix fragments (NOT applied — for the merger only)

Notation: `callerShort -> calleeShort` with the callee descriptor from
`method_list.json`. The merger must conform these to `graph_def.py`'s actual
edge syntax and must NOT apply the INFERRED edge without noting its basis.
No edge below was added to any repo file.

**Apply (flip UNREACHABLE → REACHABLE, add edges):**

```python
# GlideRequest.listener — SOURCE route R1 (both sites; same edge shape)
# RecyclerAdapter.showThumbnailWithBackground -> GlideRequest.listener (Lcom/bumptech/glide/request/RequestListener;)Lcom/amaze/filemanager/GlideRequest;
# RecyclerAdapter.showRoundedThumbnail     -> GlideRequest.listener (Lcom/bumptech/glide/request/RequestListener;)Lcom/amaze/filemanager/GlideRequest;
# Supporting edges already implied by printed code (add only if missing):
# RecyclerAdapter.setItems -> RecyclerPreloadModelProvider.<init>
# RecyclerPreloadModelProvider.<init> -> GlideRequests.asDrawable   # via GlideApp.with().asDrawable()
# RecyclerAdapter.onBindViewHolder -> RecyclerAdapter.showThumbnailWithBackground
# RecyclerAdapter.onBindViewHolder -> RecyclerAdapter.showRoundedThumbnail
```

```python
# GlideRequests.as — INFERRED delegation step; apply only with the INFERRED flag noted
# GlideRequests.asDrawable -> GlideRequests.as (Ljava/lang/Class;)Lcom/amaze/filemanager/GlideRequest;
#   anchored by printed call sites:
#   RecyclerPreloadModelProvider.<init> -> GlideRequests.asDrawable
#   AppsAdapterPreloadModel.<init>     -> GlideRequests.asDrawable
# If the merger requires SOURCE-only edges, DO NOT apply this block yet; instead
# run resolver R-as: print build-generated GlideRequests.java and confirm
# `asDrawable() { return as(Drawable.class); }`.
```

**Do NOT flip (leave OPEN, no edge):** all 13 methods in §1 marked OPEN.
In particular do NOT add any edge for `GlideOptions.clone` from
`AppsAdapterPreloadModel.getPreloadRequestBuilder` — that site's edge, if the
merger wants it, is `AppsAdapterPreloadModel.getPreloadRequestBuilder ->
GlideRequest.clone ()Lcom/amaze/filemanager/GlideRequest;`, which is outside
this 15-method group.

**Resolvers for the 13 OPEN methods (single follow-up each, cheapest first):**

- R-as / R-setRequestOptions / R-options-init: print build-generated
  `GlideRequests.java` (not in `final_java_only`; look in build/generated
  outputs for this app's Glide version). Confirm or refute: `asDrawable →
  as(...)`, `setRequestOptions` wrapping (`new GlideOptions().apply(...)`),
  and any `new GlideOptions()` static field. This one printout settles #1, #2,
  #14's SOURCE status, and #15.
- R-request: print build-generated `GlideRequest.java` and check which of
  `apply / addListener / downsample / optionalCenterInside / optionalFitCenter /
  set / transform` are invoked from app-reachable generated code vs. only
  defined-but-uncalled. (Definition in generated code alone is not reachability.)
- R-tree: receiver-typed grep over the §6 unprinted dirs for
  `.addListener(`, `.apply(`, `.downsample(`, `.transform(`,
  `optionalCenterInside`, `optionalFitCenter`, `GlideOptions`, and
  `.set(` with a `GlideRequest` receiver + `Option` argument. A bare-name grep
  (old `glide_method_grep.txt` style) must NOT be used as evidence.
- R-lib: obtain the Glide library source for the app's Glide version (not in
  `fw_src`) and check whether library request-building calls `lock()` /
  `clone()` / `autoClone()` on the request's options object, and whether a
  `GlideRequest`'s options object is a `GlideOptions` at runtime. Needed for
  #3, #4, #5 only.

## 8. Method

- No push, no edit to `graph_def.py`, `out/`, `progress/`, `tools/`, or any
  repo file. This report file is the only file written.
- No token used, no `git clone`. All source lines above come from connector
  `get_file_contents` fetches on branch `work-2026-10-31` (this task) or from
  re-grepping already-printed scratch copies (marked as such).
- No 429 encountered; fetches were single-file and spaced throughout.
- Tool-run coverage was treated strictly as a pointer, never as evidence, and
  no verdict cites it.
