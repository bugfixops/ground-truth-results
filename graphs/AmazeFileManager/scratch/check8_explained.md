# AmazeFileManager check 8 (--callers) explained (B4, 2026-11-01)

Acceptance: every method listed by `scan_unreachable.py AmazeFileManager --callers`
has its bytecode caller named and explained in its reason. After B4 the list has
3 methods (was 4); the fourth was given a route (see below). All four pairs were
already in SUPPRESS (mod/01.py sup() blocks), so no auto edge exists for any of
them and the build shows warnings 0 throughout.

## 1. AES256SHA256Decoder$1.<init> — FLIPPED to REACHABLE (was framework_never_calls)
- Bytecode caller: AES256SHA256Decoder.decode (AES256SHA256Decoder.java:36).
- Printed lines: decode() :34-36 `return new InputStream() { ... }` — the anonymous
  InputStream subclass ($1) is instantiated unconditionally on every decode call.
- decode() itself is REACHABLE in the graph (INFERRED via Coders.java:79): the 7z
  fork registers the decoder at Coders.java:57
  (`put(SevenZMethod.AES256SHA256, new AES256SHA256Decoder())`) and dispatches
  `cb.decode(...)` at :79, reached from SevenZFile.buildDecodingStream (:1030) /
  readStreamsInfo (:435) on the archive-extraction route.
- The old reason ("instantiated only by decode", "unreachable library decoder")
  contradicted the graph's own decode route: a reachable caller that
  unconditionally instantiates the class means the constructor runs.
- Fix: removed all four UNREACHABLE entries for this method from graph_def.py
  (dict entry + three assignments) and added a hand edge
  AES256SHA256Decoder.decode -> AES256SHA256Decoder$1.<init> (CALL,
  evidence 'SRC AES256SHA256Decoder.java:36 ... creates the anonymous subclass
  instance'). The (decode, $1.<init>) SUPPRESS entry is retained as a no-op guard;
  the hand edge now covers the pair, so the auto edge stays skipped via the
  manual check. Counts after the flip: REACHABLE 2510, UNREACHABLE 471.
- Observation (no change made, not flagged by check 8): the $1 sibling methods
  (read(), read(byte[],int,int), init) keep their existing UNREACHABLE entries;
  they are not listed by --callers and are out of B4 scope.

## 2. CustomNavigationView$SavedState.<clinit> — stays UNREACHABLE (closed_by_api_level)
- Bytecode caller: CustomNavigationView.onSaveInstanceState (CustomNavigationView.java:76).
- Printed lines: onSaveInstanceState :68-82; guard :69
  `if (isNavigationViewSavedStateMissing()) { return super.onSaveInstanceState(); }`
  (:70); instantiation :76 `SavedState ss = new SavedState(superState);`.
  isNavigationViewSavedStateMissing() (:115-118) returns true for SDK 23-28, hence
  at API 27 (standard configuration) the method returns early at :70 and never
  reaches :76, so the SavedState class is never loaded or instantiated.
- Reason extended (mod/01.py) to name the caller, the :76 site, the :69-70 early
  return, and the :115-118 SDK range. SUPPRESS already contains
  (onSaveInstanceState, SavedState.<clinit>).

## 3. CustomNavigationView$SavedState.<init>(Parcelable) — stays UNREACHABLE (closed_by_api_level)
- Bytecode caller: same onSaveInstanceState :76 site as (2); same guard argument.
- Reason extended (mod/01.py) to name the caller and the :69-70 / :76 lines
  (correcting the old "line 67-69" reference: the guard check is :69, the early
  return :70). SUPPRESS already contains (onSaveInstanceState, SavedState.<init>(Parcelable)).
- Note: onRestoreInstanceState has the same guard (:86-88, early return before the
  `instanceof SavedState` check at :92), so no second path loads the class at API 27.

## 4. HybridFile$2.<init> — stays UNREACHABLE (no_trigger_in_app), no reason change needed
- Bytecode caller: HybridFile.length()@HybridFileParcelable (HybridFile.java:224).
- Printed lines: length() :220-229, deprecated ("use length(Context)"), case SFTP
  :224 `return SshClientUtils.execute(new SFtpClientTemplate(path) { ... })`.
- Reason already names the caller and the mechanism: every app call site targets
  the non-deprecated length(Context) overload (7 callers listed in the source_ref;
  zero callers of the no-arg length()), and length() itself is UNREACHABLE
  no_trigger_in_app ("Parameterless overload not used; app calls length(Context)").
  The caller therefore never runs in the standard configuration.
- SUPPRESS already contains both (length(), $2.<init>) and
  (length()@HybridFileParcelable, $2.<init>).
