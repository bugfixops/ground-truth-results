# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# AnkiDroid WP2 route-check helper — EasySSLSocketFactory equals/hashCode and API 27 vs target 23

Status: **PROPOSAL ONLY — not merged, not pushed, no label flipped.**
Worked only from local files already on this VM in `~/workspace/wp2-ankidroid/`
(`EasySSLSocketFactory.java`, `HttpSyncer.java`, `CompatHelper.java`,
`label_072.md`, and `label_126` as `raw_126md.json` — there is no `label_126.md`
file in that folder). No new file was fetched for this report, no GitHub
connector call was made, and nothing was pushed. No `graph_def.py`, `out/`,
progress, tools, or another helper's files were edited.

`confirmed_by` in this report is SOURCE only for lines printed in this session,
otherwise INFERRED. No DYN, FW-MEMORY, or UNVERIFIED value is used as a
`confirmed_by`. Tool coverage, old generated graphs, and build counts are not
used as evidence for any verdict below.

Standard configuration for judging: debug build, fresh install, API 27 device
(brief/handover), AnkiDroid target_sdk 23 / min_sdk 10 per the DATASET note
quoted in `agent_notes.md:6` (that DATASET line itself was not re-printed from
the repo in this session, so the target-23 figure is quoted, not SOURCE here).

## 1. EasySSLSocketFactory.equals / hashCode — verdict: INFERRED UNREACHABLE STANDS, NOT FLIPPED, NOT SETTLED

Current labels (per `parts/label_126.md`, as printed in `raw_126md.json`):
both methods UNREACHABLE, kind `no_trigger_in_app`, `confirmed_by` INFERRED.

### Printed evidence (SOURCE — lines read in full in this session)

| Fact | Citation |
|---|---|
| Comment warning that some connection managers need these overrides | `EasySSLSocketFactory.java:102-105`: "Both Object.equals() and Object.hashCode() must be overridden for the correct operation of some connection managers" (comment text at :103-104, inside the :102-105 dash block) |
| `equals` definition; body is class-equality only | `EasySSLSocketFactory.java:108-110`; body at :109: `return ((obj != null) && obj.getClass().equals(EasySSLSocketFactory.class));` |
| `hashCode` definition; body is a constant class hash | `EasySSLSocketFactory.java:114-116`; body at :115: `return EasySSLSocketFactory.class.hashCode();` |
| Sole construction in the printed app file, registered for https | `HttpSyncer.java:226-228`: :226 `SchemeRegistry registry = new SchemeRegistry();`, :227 http scheme, :228 `registry.register(new Scheme("https", new EasySSLSocketFactory(), 443));` |
| Registry handed to the connection manager; request executed | `HttpSyncer.java:229`: `ThreadSafeClientConnManager cm = new ThreadSafeClientConnManager(params, registry);` :235 `new DefaultHttpClient(cm, params)`; :236 `httpClient.execute(httpPost);` |
| No printed app code calls equals/hashCode on the factory | Grep of the printed local `.java` files: the only `equals` hits are `Build` brand/model/product strings (`CompatHelper.java:92-93, 97, 102, 107, 111`), `Hook` equality (`Hooks.java:79, 99`), and a method-name string compare (`HttpSyncer.java:201`). None is a call on an `EasySSLSocketFactory` instance. `HttpSyncer.java` itself contains no `equals`/`hashCode` call on the factory. |

### Line-number note (no contradiction)

`label_126` cites equals :107-110 and hashCode :113-116; the local print
shows `@Override` at :107 / :113 with bodies at :108-110 / :114-116. The
ranges agree once the annotation lines are counted, as the earlier
`route_check_part1.md` §2 already noted. `label_126`'s HttpSyncer citations
(:226-228) match the local print exactly.

### Step-by-step judgement

1. The "no app code calls it" half of the label is supported by the printed
   files: the factory is constructed once in the printed `HttpSyncer.req`
   path, registered, and handed to `ThreadSafeClientConnManager`; no printed
   line compares or hashes it.
2. The comment at :102-105 is evidence only that *some* connection managers
   need these overrides. It is NOT evidence that *this* manager
   (`ThreadSafeClientConnManager` + `DefaultHttpClient` as used at
   `HttpSyncer.java:229, 235-236`) compares or hashes the scheme/factory.
   The comment's wording ("some connection managers") cuts both ways and
   cannot by itself flip the label either way.
3. The shape of the overrides (any `EasySSLSocketFactory` instance equals
   any other; constant hash) is *consistent with* use as a map key / set
   member, but consistency is not evidence of a call. It is recorded here
   only as an observation, not as a route.
4. Whether this app's HttpClient path compares or hashes a `Scheme` holding
   the factory is a library question. Apache HttpClient 4.x source is NOT in
   the dataset, was NOT read here, and was NOT downloaded. A step not
   printed counts as not checked.
5. The "sole construction in the source root" claim is quoted from
   `label_126`'s own grep claim (`SchemeRegistry` / `new Scheme(` listing
   only `HttpSyncer`), not independently re-verified here: the full app
   source root is not on this VM, so no exhaustive grep was possible in
   this session. That limitation does not change the verdict, but it is
   part of why the label stays INFERRED rather than SOURCE.

### Per-item verdicts

| Item | Label | Kind | confirmed_by | Verdict |
|---|---|---|---|---|
| `EasySSLSocketFactory.equals` | UNREACHABLE (unchanged) | `no_trigger_in_app` | INFERRED | STANDS as a proposal; do NOT flip without printed library evidence |
| `EasySSLSocketFactory.hashCode` | UNREACHABLE (unchanged) | `no_trigger_in_app` | INFERRED | STANDS as a proposal; do NOT flip without printed library evidence |

If the library question resolves the other way, both flip together: a
manager that compares schemes would invoke `equals`, and one that hashes
them would invoke `hashCode`; the hypothetical route in both cases would
run through `HttpSyncer.req` (:226-236) under an ENV network gate. That
route is NOT claimed here — it is conditional on the decision in §3.

## 2. API 27 vs target 23 — verdict: RESOLVED for Compat dispatch; OPEN for the rest of the app

### Printed evidence (SOURCE — lines read in full in this session)

| Fact | Citation |
|---|---|
| Constructor selects CompatV21 at API ≥ 21 | `CompatHelper.java:33-36`: :33 Nook special case (`getSdkVersion() == 15`); :35 `else if (getSdkVersion() >= 21)`; :36 `mCompat = new CompatV21();` |
| `getSdkVersion()` returns the device API level, not the target SDK | `CompatHelper.java:55-57`: :55-56 `public static int getSdkVersion() { return Build.VERSION.SDK_INT; }` |
| Every other version gate in the printed Compat file is also SDK_INT-based | `CompatHelper.java:61-63` (`isHoneycomb`, `>= HONEYCOMB`), :65-67 (`isLollipop`, `>= LOLLIPOP`), :69-71 (`isMarshmallow`, `>= M`), :124-136 (`removeHiddenPreferences`: `isHoneycomb()`, `>= 13`, `>= 15`, `>= 16`) |
| No targetSdk reference anywhere in the printed Compat file | Grep of local `.java` files: zero hits for `targetSdkVersion` / `target_sdk`. `CompatHelper.java` never reads a manifest target value. |

### Judgement — Compat dispatch: RESOLVED (SOURCE)

On an API 27 device, `getSdkVersion()` returns 27 whatever the manifest
target is, so the constructor at `CompatHelper.java:35-36` selects
`CompatV21` regardless of target_sdk 23. Every `closed_by_api_level` label
that rests on the CompatV21 chain (e.g. the `CompatV10` base bodies
shadowed by overrides, per `label_072.md`) is therefore unaffected by the
target-23 question. No user decision is needed for Compat dispatch itself.

Two printed observations, neither changing the API 27 outcome:

- Constructor branch order at `CompatHelper.java:45-48` puts `>= 11`
  before `>= 12`, so the `CompatV12` branch can never be selected directly
  (any value ≥ 12 already matches ≥ 11). This does not affect API 27
  (V21 is selected first) and is about direct selection only, not about
  the inheritance chain cited in `label_072.md`.
- `CompatHelper.isMarshmallow` (:69-71) is the permission-adjacent helper
  (per `label_072.md`, it backs the provider permission check in
  `CardContentProvider.java:197-212, 709-713`), but its own code is purely
  `getSdkVersion() >= M` — device-API-driven, not target-driven. Whether
  the *framework's* permission enforcement behind that check is
  target-sensitive is a separate framework question (see below).

### Hunt for other targetSdk-sensitive behaviour in the printed local Compat files: NONE FOUND, WITH A SCOPE LIMIT

- Scope of the hunt: the only Compat file present locally is
  `CompatHelper.java`. No `CompatV10`–`CompatV21` source, no manifest, and
  no `CardContentProvider.java` are in `~/workspace/wp2-ankidroid/`, so
  they could not be hunted here.
- Within that scope: no permission-model code, no compatibility shim, and
  no targetSdk read exists. All dispatch in the file keys off
  `Build.VERSION.SDK_INT` via `getSdkVersion()`.
- Outside that scope: this report makes NO claim. Framework behaviour that
  changes with targetSdk (permission model, compatibility shims, or
  anything else) would need printed `fw_src/android-8.1.0_r1/` lines to
  assert, and none were printed in this session. Any such claim here
  would be INFERRED at best and is marked 'source not read', never
  FW-MEMORY. In particular, no method outside Compat dispatch is cleared
  or condemned on targetSdk grounds by this report.

### Per-item verdicts

| Item | Verdict | confirmed_by |
|---|---|---|
| Compat dispatch on API 27 (CompatV21 selection) | RESOLVED — target 23 is irrelevant; API 27 → CompatV21 | SOURCE (`CompatHelper.java:33-36, 55-57`) |
| `closed_by_api_level` labels resting on the CompatV21 chain (per `label_072.md`) | UNAFFECTED by the target-23 question | SOURCE (same lines, via the dispatch) |
| Any other targetSdk-sensitive behaviour in printed local Compat files | NONE FOUND in `CompatHelper.java` (the only local Compat file) | SOURCE for the file's contents; scope limit stated above |
| Framework permission-model / compatibility-shim behaviour vs target 23 | OPEN — 'source not read'; no `fw_src` lines printed | INFERRED at most; no framework claim made |
| API 27 vs target 23 question for the app as a whole | PARTIALLY RESOLVED (Compat only); otherwise OPEN pending decision §3 | — |

## 3. Exact user decisions needed (this helper decides neither)

### Decision A — EasySSLSocketFactory.equals / hashCode

> For AnkiDroid, do you (a) accept the current INFERRED UNREACHABLE
> (`no_trigger_in_app`) labels for `EasySSLSocketFactory.equals` and
> `EasySSLSocketFactory.hashCode` as standing, or (b) authorise reading
> the Apache HttpClient 4.x `Scheme` / `ThreadSafeClientConnManager`
> source from outside the dataset to check whether that manager compares
> or hashes a scheme holding the factory?
>
> Note: the brief's "only download allowed" is AOSP 8.1.0_r1, so option
> (b) needs your explicit authorisation; this helper has not downloaded
> it and will not decide to authorise it. If (b) shows a compare/hash,
> both methods flip to REACHABLE via the `HttpSyncer.req` route
> (`HttpSyncer.java:226-236`, ENV network gate); if it shows none, both
> stay UNREACHABLE and the INFERRED tag can be revisited.

### Decision B — API 27 vs target 23, beyond Compat

> Do you confirm that the standard configuration is "device API 27,
> whatever the manifest target" for ALL AnkiDroid labels, or do you name
> specific target-sensitive methods (e.g. permission-model or framework
> compatibility behaviour) to re-check against printed
> `fw_src/android-8.1.0_r1/` lines?
>
> For Compat dispatch alone no decision is needed — it is resolved
> above on printed source. Until Decision B is answered, the API 27 vs
> target 23 question is closed for Compat dispatch only and remains open
> for the rest of the app.

## What was NOT done (explicit limits)

- No label was flipped, no file in the repo was edited, nothing was
  merged or pushed.
- No Apache HttpClient 4.x source was read or downloaded; no
  `fw_src/android-8.1.0_r1/` lines were printed or cited.
- No exhaustive grep over the full app source root was possible (no full
  checkout on this VM); the "sole construction" and "no caller" claims
  for the factory rest on `label_126`'s grep plus the printed local
  files, which is why both rows stay INFERRED.
- No `CompatV*` class bodies, manifest, or `CardContentProvider.java`
  were printed locally, so the targetSdk hunt covers `CompatHelper.java`
  only.
- No tool coverage, generated-graph, or build-count output was used as
  evidence for any verdict.
