# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AnkiDroid — Card.toString hunt (proposal, NOT merged, NOT pushed)

Scope: **only** `com.ichi2.libanki.Card.toString`. No other app, no
`graph_def.py`, `out/`, progress, tools, or another helper's files were
touched. Nothing was pushed. No APK, zip, secret, or token is involved.
No git clone and no token were used.

## Verdict: still UNCLEAR — but narrowed to one decisive question

The label stays as it is for now: **UNREACHABLE, `no_trigger_in_app`**,
as recorded in `graphs/AnkiDroid/out/build_report.txt` and
`graphs/AnkiDroid/scratch/conflicts.md` (per prior WP2 part 1). It is
**not** flipped to REACHABLE on this hunt, and it is **not** flipped on
the APE tool-run hit: tool coverage is NOT evidence and was not used as
evidence anywhere below.

What this hunt found, which prior work had not printed, is the one
in-app mechanism by which libanki `Card.toString` *could* run — and the
gate that decides whether it ever does on an in-app path:

```
Card.flush() / Card.flushSched()          (Card.java:214, :243)
  -> mCol.log(this)                        // `this` is a libanki Card
  -> Collection.log(Object... args)        (Collection.java:1498-1513, fetched, see §2)
  -> TextUtils.join(",  ", args)           // line 1510; join stringifies each arg
  -> libanki Card.toString()               // Card.java:634-648
```

That chain is **gated**: `Collection.log` returns immediately unless
`mDebugLog` is true (Collection.java:1499-1501), and the in-app value of
`mDebugLog` is **not printed** anywhere in this hunt (see §2, item 2c).
So the verdict cannot be closed yet. The exact grep that settles it is
in §4. In one sentence: **find one in-app `new Collection(..., true)`
(or equivalent `log=true` construction) on the standard app path, plus
one reachable `flush()`/`flushSched()` caller, and this becomes
REACHABLE with that route; find that every in-app construction passes
`log=false` (and no hook stringifies a Card arg, §3 item 7), and the
UNREACHABLE label stands with the grep output recorded.**

Evidence discipline used throughout:

- `confirmed_by` SOURCE is used only for lines actually printed in this
  hunt (local files, or the fetched Collection.java resource text).
  Anything else is marked INFERRED or 'not printed'.
- No DYN / FW-MEMORY / UNVERIFIED claim is made.
- Connector `search_code` returning 0/incomplete was **not** used and is
  **never** cited here as evidence of absence (per task rules; prior
  WP2 part 1 already recorded the same caution).
- Old generated graphs and build counts were not used as evidence.
- The single APE tool-run hit (sanity row cited in conflicts.md) is
  recorded only as the contradiction to explain, never as a route.

## 1. The target method (printed, local)

Source root for local files: `~/workspace/wp2-ankidroid/` (copies of
`final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/...`).

- `com.ichi2.libanki.Card`, package `com.ichi2.libanki`
  (Card.java:19), `public class Card implements Cloneable` (Card.java:63).
- `toString` definition, Card.java:630-648 (SOURCE, printed local file):

```java
// A list of class members to skip in the toString() representation
public static final Set<String> SKIP_PRINT = new HashSet<>(Arrays.asList("SKIP_PRINT", "$assertionsDisabled", "TYPE_LRN",
        "TYPE_NEW", "TYPE_REV", "mNote", "mQA", "mCol", "mTimerStarted", "mTimerStopped"));

public String toString() {
    List<String> members = new ArrayList<>();
    for (Field f : this.getClass().getDeclaredFields()) {
        try {
            // skip non-useful elements
            if (SKIP_PRINT.contains(f.getName())) {
                continue;
            }
            members.add(String.format("'%s': %s", f.getName(), f.get(this)));
        } catch (IllegalAccessException | IllegalArgumentException e) {
            members.add(String.format("'%s': %s", f.getName(), "N/A"));
        }
    }
    return TextUtils.join(",  ", members);
}
```

- Grep of the printed Card.java: `toString` occurs only at the comment
  (line 630) and the definition (line 634). **No internal caller of
  `toString` exists in Card.java** (SOURCE, local grep).
- Card.java imports no Timber/Log (imports at lines 21-35 are
  android.content/content, database, text, JSON, reflection, util
  only). So Card.java itself contains no log call that could stringify
  a Card — except the `mCol.log(this)` sites in §2, which are calls
  *out* to Collection, not log calls in Card.java itself.

## 2. The found mechanism: `mCol.log(this)` → `Collection.log(Object...)`

### 2a. The two call sites (SOURCE, printed local Card.java)

- Card.java:214, end of `flush(boolean)` (method at 181-215):
  `mCol.log(this);` — immediately after the `insert or replace into
  cards` DB execute (lines 191-213, whose `new Object[]{...}` array
  contains only scalar fields `mId, mNid, mDid, mOrd, …, mData` — the
  Card object itself is NOT in that array).
- Card.java:243, end of `flushSched()` (method at 218-244):
  `mCol.log(this);` — after the `cards` table update (line 242).
- No other `mCol.log` / `log(this)` / passing of `this` to an
  Object-typed parameter exists in Card.java (SOURCE, local grep for
  `mCol\.`, `log(`: only lines 214 and 243). The two commented-out
  `// TODO: runHook("odueInvalid");` lines (188, 223) are comments, not
  calls, and pass no Card.
- Card.java:291-293 (`_getQA`): `Object[] data` holds model/template
  JSON values, not a Card. Not a trigger.

### 2b. `Collection.log` body (SOURCE, fetched — see fetch note in §5)

Fetched file, branch `work-2026-10-31`:
`final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/libanki/Collection.java`,
lines 1498-1513:

```java
public void log(Object... args) {
    if (!mDebugLog) {
        return;
    }
    StackTraceElement trace = Thread.currentThread().getStackTrace()[3];
    // Overwrite any args that need special handling for an appropriate string representation
    for (int i = 0; i < args.length; i++) {
        if (args[i] instanceof long[]) {
            args[i] = Arrays.toString((long []) args[i]);
        }
    }
    String s = String.format("[%s] %s:%s(): %s", Utils.intNow(), trace.getFileName(), trace.getMethodName(),
            TextUtils.join(",  ", args));
    mLogHnd.println(s);
    Timber.d(s);
}
```

Why this is a genuine trigger *when the gate is open*: `log` takes
`Object... args`, so the libanki Card arrives as an `Object`; the only
special-casing is `long[]` (lines 1505-1507), so a Card is passed
unchanged into `TextUtils.join(",  ", args)` (line 1510).
The final step, `TextUtils.join` converting each element via its
`toString`, is **INFERRED** (standard `StringBuilder.append(Object)` /
`TextUtils.join` semantics), NOT printed: the AOSP `TextUtils.java`
body was not printed in this hunt. It must be confirmed from
`fw_src/` on a full checkout (see §4, grep 5). If that confirmation
failed, this chain would collapse — that is the one framework step
still open, and it is flagged rather than assumed silently.

Note also line 143: the Collection constructor itself calls
`log(path, VersionUtils.getPkgVersionName())` — String args only, not
a Card. Not a trigger.

### 2c. The gate: `mDebugLog` (SOURCE, fetched; in-app value NOT PRINTED)

- Field: Collection.java:94, `private boolean mDebugLog;`
- Constructors (Collection.java:129-139, SOURCE, fetched):
  - 3-arg `Collection(context, db, path)` → delegates with `false`
    (line 130);
  - 4-arg `Collection(context, db, path, server)` → delegates with
    `false` (line 134);
  - 5-arg `Collection(context, db, path, server, log)` →
    `mDebugLog = log;` (line 139).
- `_openLog()` (Collection.java:1516-1535, SOURCE, fetched) also
  returns immediately unless `mDebugLog`, and sets `mDebugLog = false`
  if the log file cannot be opened (line 1533).

Consequence: **if every in-app construction goes through the 3- or
4-arg constructor (or passes `log=false`), `Collection.log` always
returns at line 1499-1501 and `Card.toString` never runs via this
chain in the app, however reachable `flush()`/`flushSched()` are.**
That is exactly consistent with the current UNREACHABLE label — and it
is also consistent with the APE tool hit if the tool harness (not the
app) constructed a Collection with logging on, or invoked the method
directly. That harness explanation is INFERRED speculation, not
evidence, and is recorded here only so the contradiction is not
mysterious; it must not be used to flip the label either way.

What is **not printed** and therefore not decided:

- Any `new Collection(...)` call site, and its `log` argument
  (CollectionHelper / Storage / test or server paths). No such site
  exists in the local files: local grep for `new Collection` returns
  nothing (only `CollectionHelper` import at AdvancedStatistics.java:26
  and `CollectionHelper.getInstance().getCol(context)` at
  AdvancedStatistics.java:177, and `Card.getCol()` at Card.java:605).
- Any caller of `Card.flush()` / `Card.flushSched()`. No such caller
  is in the local files. Flush reachability is therefore NOT claimed
  here (INFERRED expectation only: review/scheduling code flushes
  cards, but an expectation is not a route — see §4, grep 2).

## 3. Every other candidate site checked

Each item states what was printed and the outcome. 'Not printed' means
the file was not available in this hunt; it is never treated as
'checked and absent'.

### 3.1 AdvancedStatistics inner Card — EXCLUDED (SOURCE, local)

This is the trap prior work already identified, re-verified here in
full:

- `com.ichi2.libanki.hooks.AdvancedStatistics` (package line 18)
  imports `com.ichi2.libanki.Collection`, `Decks`, `Stats` only
  (lines 30-32); it imports **no** `com.ichi2.libanki.Card`
  (imports printed, lines 20-44, SOURCE).
- Inner class at AdvancedStatistics.java:399, `private class Card`,
  with its own `toString` at 409-412:
  `"Card [ivl=" + ivl + ", factor=" + factor + ", due=" + due +
  ", correct=" + correct + ", id=" + id + "]"`.
- Every unqualified `Card` in that file resolves to this inner class:
  field `ReviewOutcome.card` (1475), constructor/setter/getter
  (1478, 1483, 1488), `Review.card/prevCard/newCard` fields
  (1548, 1549, 1555, all `new Card(0, 0, 0, 0, 0, 0)`), `CardIterator`
  (569, 597), `simSingleReview(Card c)` (778, 790),
  `applyOutcomeToCard(Card c, …)` (801), `updateNInState(Card …)`
  (1376, 1400), `Review` constructors/methods (1584, 1625, 1647,
  1710, 1733, 1742), and the simulation-loop `Card card = new Card(0,
  0, 0, 0, 0, 0)` (990). All SOURCE, local grep for `Card`.
- The two stringification sites prior work cited are inner-Card only:
  - `ReviewOutcome.toString` (1497-1501): `"card=" + card` where
    `card` is the inner-Card field (1475). Not libanki Card.
  - `Review.writeLog` (1710-1716): `Timber.d(tabs + prevCard)` /
    `Timber.d(tabs + newCard)` where both fields are inner-Card
    (1549, 1555). Not libanki Card. And `writeLog` itself is
    effectively dead: its only call is commented out (line 1685,
    `//writeLog(newCard, outcomeProb)`).
- Commented-out lines 1008 (`//Timber.d("Card started: " + cardN)`)
  and 1014 (`//Timber.d("Card done: " + cardN++)`) concatenate an
  `int` counter, not a Card, and are comments anyway. Line 1680
  (`//Timber.d("Simulation …" + reviewOutcome.toString())`) is
  commented out and, even if live, would call the inner
  `ReviewOutcome.toString`, not libanki `Card.toString`.
- Therefore **no AdvancedStatistics site can trigger libanki
  `Card.toString`**. The inner class is private, so no other file can
  even name it (consistent with label_104's inner-Card rows).

### 3.2 AdvancedStatistics.runFilter / Stats.runFilter call — EXCLUDED (SOURCE, local)

- AdvancedStatistics.java:141-145: `public Object runFilter(Object
  arg, Object... args)` casts `arg` to `StatsMetaInfo` and `args`
  to `Stats.AxisType` / `Context` / `String`. No Card is involved;
  the inner Card never leaves this class as an `Object` argument.
- Stats.java:311 (SOURCE, local): the only local `runFilter` call,
  `Hooks.getInstance(context).runFilter("advancedStatistics",
  metaInfo, type, context, _limit())`, passes a `StatsMetaInfo`, not
  a Card.

### 3.3 Timber / Log / format / concatenation with a libanki Card — NONE FOUND LOCALLY (SOURCE, local greps)

Exhaustive greps over all seven local `.java` files
(Card, AdvancedStatistics, Stats, Hooks, HttpSyncer, CompatHelper,
EasySSLSocketFactory) for `Timber.`, `Log.`, `+ card`, `card +`,
`valueOf(card`, `%s` with card, `String.format` with card,
`Arrays.toString` with Card, explicit `.toString()` on a Card
variable:

- Card.java: no Timber/Log at all; its only `String.format` calls
  are inside `toString` itself (642, 644) and the CSS builder (269).
- AdvancedStatistics.java Timber sites (full list, SOURCE): 332
  (durations), 505/519-523 (deck settings/numbers), 588/851
  (`"%s", query` — a String), 680-688 (`Arrays.toString` of
  `double[]` probability arrays — not Cards), 973/1047-1049/1097/1100
  (ints/longs), 1245 (`s.toString()` where `s` is a `StringBuilder`
  built from a matrix at 1240-1243, not a Card), 1714-1716 (inner
  Card, §3.1). No libanki Card is a Timber argument anywhere here.
- Stats.java Timber sites: 216 (`"New cards query: %s", query`),
  1161 (`"CardsTypes query: %s", query`) — Strings only. No Card
  variable exists in Stats.java at all (grep for `Card` returns only
  `mMaxCards`/`mFound*Cards` counters and `calculateCardTypes`).
- HttpSyncer.java Timber sites: 242, 248, 438 — each `Timber.e(e,
  "<string>")`, exception + constant string. Its `.toString()` hits
  (175, 195, 304, 454) are on buffers/builders/URIs, not Cards.
- Hooks.java Timber sites: 124, 153 (`Timber.e(e, "Exception while
  running hook %s : %s", hook, funcName)` — hook name and function
  name strings only); 140 (constant string). No Card argument.
- CompatHelper.java / EasySSLSocketFactory.java: no `Card`, no
  Timber/Log Card argument (EasySSL's only `Object` is its own
  `equals(Object obj)` parameter, line 108).
- Prior AGENT_NOTES claim (grep for `"+ card"`, `"valueOf(card)"`,
  `"%s, card"` finding no other implicit conversion) is consistent
  with the local greps above, but it is **prior work's claim, not
  re-verified on a full checkout here**; the full-checkout grep in
  §4 re-runs it rather than trusting it.

### 3.4 Collections / arrays of Objects holding a libanki Card — NONE FOUND LOCALLY (SOURCE, local greps)

- No `List<Card>`, `ArrayList<Card>`, `Map<…Card`, `Collection<Card`,
  `Card[]`, or `Arrays.toString(…card…)` with a libanki Card in any
  local file. The only `Object[]` sites are Card.java:194-212 (scalar
  DB fields, §2a), Card.java:291-293 (JSON values), Stats.java:117
  (chart metadata), HttpSyncer.java:357/362 (`Object[] download() /
  upload()` return types — bodies not shown to contain Cards, and
  HttpSyncer has no Card import/variable in the local copy).
- A `List<Card>.toString()` / `Map` stringification route therefore
  has **no printed local instance**. Whether one exists elsewhere is
  a full-checkout grep item (§4, grep 4), not a finding.

### 3.5 `Hooks.runHook(Object... args)` — PASS-THROUGH ONLY, NO STRINGIFICATION IN Hooks.java (SOURCE, local; downstream hooks NOT PRINTED)

- Hooks.java:114-121 (SOURCE, printed in full, 160 lines):

```java
public void runHook(String hook, Object... args) {
    List<Hook> _hook = hooks.get(hook);
    String funcName = "";
    if (_hook != null) {
        try {
            for (Hook func : _hook) {
                funcName = func.getClass().getCanonicalName();
                func.runHook(args);
            }
        } catch (Exception e) {
            Timber.e(e, "Exception while running hook %s : %s", hook, funcName);
            return;
        }
    }
}
```

  Passing a Card here puts it in an `Object[]` and hands the array to
  each `Hook.runHook` — **that alone does not call `toString`**.
  Nothing in Hooks.java stringifies `args` (the Timber.e formats
  only `hook` and `funcName`).
- Prior work (label_104) records a caller,
  `Sched._checkLeech` → `runHook("leech", card, context)` where the
  card is a libanki Card. **That caller and the hook implementations
  (Leech, etc.) are NOT PRINTED in this hunt** — Sched.java and
  Leech.java are not among the local files — so this remains an
  open sub-candidate, not a confirmed route and not a refutation:
  it becomes a route only if a printed hook implementation
  stringifies its Card arg (log/concatenation/format/collection).
  See §4, grep 3. Do not cite label_104's caller line as printed
  SOURCE here; it is prior-work citation only.
- Same reasoning for `Hooks.runFilter` (Hooks.java:138-155, SOURCE,
  local): `arg` is threaded through `func.runFilter(arg, args)` and
  returned; Hooks.java itself never stringifies it. No printed
  caller passes a libanki Card as `arg` (§3.2).

### 3.6 Explicit `.toString()` on a libanki Card, assertions, exceptions — NONE (SOURCE, local)

- No `card.toString()`, `something.getCard().toString()`, or
  equivalent explicit call on a libanki Card variable in any local
  file (all local `.toString()` hits are accounted for in §3.3).
- Card.java asserts (190, 225) compare `mDue` to
  `Long.valueOf("4294967296")` — no Card stringification.
- Hooks.java exception path (§3.5) and HttpSyncer.java exception
  paths (§3.3) format constant strings only.

### 3.7 Files NOT PRINTED (not checked — listed so nothing is silently assumed absent)

Sched.java, DeckTask.java, Reviewer.java, CardBrowser.java,
CollectionHelper.java, Storage.java, Leech.java, Hook.java, all other
`com.ichi2.anki.*` / `com.ichi2.libanki.*` files, and
`fw_src/android-8.1.0_r1/.../TextUtils.java`. Any libanki-Card
Object-typed pass in those files is **unknown**, not absent. The
§4 greps cover exactly these files.

## 4. What a full-checkout grep must print to settle it

Run on a full checkout of the app source root (the dataset root used
for labelling, i.e. the `final_java_only/.../src/main/java` tree),
and save the output under the app's `scratch/` folder. Do not use
connector `search_code` for this — it is unscoped/incomplete and is
not evidence either way.

**Grep 1 — the gate (decisive). Print every Collection construction
and its `log` argument:**

```bash
grep -rn "new Collection(" <srcroot> --include='*.java'
grep -rn "Collection(" <srcroot>/com/ichi2/anki/CollectionHelper.java <srcroot>/com/ichi2/libanki/Storage.java --include='*.java' 2>/dev/null
# then print each construction site in full (constructor call + surrounding lines)
```

Settle rule 1a: if a printed site on the **standard in-app path**
(not a test, server, or tool harness) passes `log=true` (5-arg
constructor), the gate is open in-app.
Settle rule 1b: if every printed in-app site uses the 3-/4-arg
constructor or passes `log=false`, the gate is closed in-app and the
`Collection.log` chain cannot run in the app — regardless of flush
reachability.

**Grep 2 — a reachable flush caller (needed for a route, not for the gate):**

```bash
grep -rn "\.flush()\|\.flushSched()\|\.flush(true)\|\.flush(false)" <srcroot> --include='*.java'
# then print one caller chain back to an entry point, e.g. Reviewer answer
# path -> Sched answer path -> Card.flush/flushSched
```

A REACHABLE verdict needs one such printed chain on a standard path
(plus gate-open from grep 1). Flush reachability alone, without
gate-open, does NOT make `toString` reachable.

**Grep 3 — the hook sub-candidate (alternative route, only if a hook stringifies):**

```bash
grep -rn "runHook(\|runFilter(" <srcroot> --include='*.java' | grep -i "card"
# then print Sched._checkLeech in full, and print every Hook.runHook /
# Hook.runFilter implementation that receives a Card arg (Leech.java first),
# checking each for Timber/Log/concatenation/format/collection stringification
```

A hook route counts only if a printed hook body stringifies the Card
arg. The bare `runHook("leech", card, context)` pass does not count.

**Grep 4 — the exhaustive Object-typed-pass sweep (replaces the prior
`"+ card"` / `"valueOf(card)"` / `"%s, card"` grep with printed output):**

```bash
grep -rnE "Timber\.[a-z]+\([^;]*\bcard\b|Log\.[a-z]+\([^;]*\bcard\b|String\.valueOf\([^;]*\bcard\b|String\.format\([^;]*\bcard\b|\+[[:space:]]*card\b|\bcard\b[[:space:]]*\+|append\([^;]*\bcard\b" <srcroot> --include='*.java'
grep -rnE "List<Card>|ArrayList<Card>|Map<[^>]*Card|Collection<Card|Card\[\]|Arrays\.toString\([^;]*card" <srcroot> --include='*.java'
grep -rnE "\bcard\.toString\(\)|getCard\(\)\.toString\(\)" <srcroot> --include='*.java'
# for each hit, print the file, check the declared type of `card`
# (libanki Card vs AdvancedStatistics inner Card vs other), and check
# whether the enclosing method is on a reachable path
```

Any hit whose `card` is proven (by its declaration/import in the
same printed file) to be a libanki Card, on a reachable path, is a
route. Hits on the AdvancedStatistics inner Card are excluded by
§3.1. Case variants (`Card`, `mCard`, `c`) should be covered by
re-running grep 4 with those identifiers if the first pass is empty.

**Grep 5 — the framework step (closes the INFERRED link in §2b):**

```bash
# print fw_src TextUtils.join(CharSequence, Object[]) and confirm it
# appends each element as an Object (StringBuilder.append(Object) ->
# String.valueOf -> toString) rather than skipping non-String elements
sed -n '<join-method-range>p' fw_src/android-8.1.0_r1/frameworks/base/core/java/android/text/TextUtils.java
```

**Final settle rule (all must be printed, none assumed):**

- REACHABLE with route iff: grep 1 shows gate-open on a standard
  in-app path AND grep 2 shows a reachable `flush()`/`flushSched()`
  caller (route: entry → … → `Card.flush`/`flushSched` →
  `Collection.log(Object...)` → `TextUtils.join` → `Card.toString`,
  with the debug-log gate noted on the route), OR grep 3/4 shows a
  printed hook/log/format/collection stringification of a libanki
  Card on a reachable path. Record the printed citations and the
  gate status on the route; do not cite the APE tool hit.
- Otherwise keep UNREACHABLE, `no_trigger_in_app`, with the grep
  outputs (1-5) saved in `scratch/` and cited — and record that the
  APE tool hit remains unexplained by app source (tool-harness
  behaviour is not a label).

## 5. Fetch note (provenance and staggering)

Local phase used only files already on this VM in
`~/workspace/wp2-ankidroid/` — no fetch. The Collection.java evidence
in §2 was then fetched, one file at a time, spaced ~30 s apart, via
`/opt/hatch/bin/github call-read-tool --name get_file_contents`
(owner `bugfixops`, repo `ground-truth-results`, ref
`refs/heads/work-2026-10-31`, path
`final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/libanki/Collection.java`),
extracting the **resource text field** (not the first text field),
and grepping that text locally for `log(`/`mDebugLog`/constructor
windows. Four spaced fetches of that single file were made (initial
fetch, `log(` extraction, `mDebugLog` extraction, constructor +
`_openLog` windows); no other repo file was fetched, to avoid
bursting while other agents run in parallel. No file was edited in
the repo and nothing was pushed.

## 6. Summary table

| Candidate | Printed? | Outcome |
|---|---|---|
| `Card.toString` definition (Card.java:634-648) | Yes, local | Target exists; reflection-based; no internal caller |
| `Card.flush:214` / `flushSched:243` → `mCol.log(this)` | Yes, local | Only in-app Object-typed pass of a libanki Card found |
| `Collection.log(Object...)` → `TextUtils.join` (1498-1513) | Yes, fetched | Real trigger IF gate open; join→toString step INFERRED, needs fw grep 5 |
| `mDebugLog` gate (94, 129-139, 1499, 1516-1533) | Yes, fetched | Defaults false; in-app `log` argument NOT PRINTED — decisive open item |
| AdvancedStatistics inner Card sites (399, 409-412, 1497-1501, 1710-1716) | Yes, local | Excluded: different, private inner class |
| AdvancedStatistics/Stats `runFilter` (141-145; Stats:311) | Yes, local | Excluded: arg is StatsMetaInfo |
| Timber/Log/format/concat with libanki Card (all local files) | Yes, local greps | None found |
| `List<Card>` / Object collections of libanki Cards | Yes, local greps | None found |
| `Hooks.runHook(Object...)` pass-through (Hooks:114-121) | Yes, local | Pass alone is not a trigger; hook bodies NOT PRINTED |
| `new Collection(...)` sites / flush callers / Sched / Leech / Storage / CollectionHelper bodies | Not printed | Open — greps 1-3 in §4 |
| APE tool-run hit | Prior-work citation only | NOT evidence; does not flip the label |
