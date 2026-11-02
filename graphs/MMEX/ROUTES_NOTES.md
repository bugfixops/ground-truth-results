# MMEX device routes — notes (final sample, B3 + merged 26/4 package)

Route list source: the final redrawn sample (30 routes, seed 20261025),
as judged in `graphs/MMEX/scratch/route_table.md` (CORRECT 20 / FIXED 8 /
WRONG 0 / UNCLEAR 2). The route list (D1) and scripts (D3) below are
the device package; the graph, writer, and verification.csv are
unchanged by it.

## B3 package (pushed 2026-11-02, commit cdab515a)

30 rows, 22 scripted / 8 unscriptable (routes 06, 07, 08, 10, 11, 12,
14, 19), 22 route scripts + 18 setups. ROUTES.csv blob 4ed18b4c.
The B3-stage reasons for the four routes converted later are in
`graphs/MMEX/AGENT_NOTES.md` ("## Device B3").

## Merged package (LOCAL ONLY until Push 1)

30 rows, 26 scripted / 4 unscriptable (07, 08, 11, 19) = 13.3%,
accepted under the user's cap ruling (decision text forwarded
separately to the coordinator; the merger never writes
handoff/MUSE_DECISIONS.md). Cell-diff vs the B3 ROUTES.csv: ONLY
setup + status cells on routes 06, 10, 12, 14 change; methods,
edges, and sources are identical on all 30 rows. Merged-layout
drycheck 30/0 in both plain and --load-scripts modes on the fresh
8441-edge graph. 1-in-3 script audit PASS (all 10 sampled scripts,
all five contract rulings ACCEPT).

## Per-route setup and status (merged ROUTES.csv, verbatim cells)

| Route | Status | Setup cell |
|---|---|---|
| route_01 | scripted | setup_route_01.py bootstrap (budget + category rows are a follow-up seed, not satisfied here) |
| route_02 | scripted | setup_route_02.py bootstrap |
| route_03 | scripted | setup_route_03.py bootstrap + investment account RetryInv + stock TEST |
| route_04 | scripted | setup_route_04.py bootstrap + account RetryCheck |
| route_05 | scripted | setup_route_05.py bootstrap |
| route_06 | scripted | setup_route_06.py bootstrap + account RetryRecur |
| route_07 | unscriptable | (no setup) needs an investment account row to tap (no account exists on a fresh database, no row text grounded, no MMEX database fixture in $WEMU/fixtures) plus Morningstar as configured quote provider and a live Morningstar price download, a network result adb cannot create (follow-up: specified-but-unverified HTTP substitute) |
| route_08 | unscriptable | (no setup) ENV gate needs a live Fixer price download to finish while the currency list is started (FixerService BASE_URL https://api.fixer.io); a network result adb cannot create (follow-up: specified-but-unverified HTTPS/CA substitute) |
| route_09 | scripted | setup_route_09.py bootstrap (script creates its own category in-script) |
| route_10 | scripted | setup_route_10.py bootstrap + account RetryTxAcct + one transaction (payee RetryPayee) |
| route_11 | unscriptable | (no setup) requires a real online cloud-storage account (Dropbox/OneDrive/GoogleDrive/Box/pCloud) holding a remotely-modified database; the sync-on-start plus remote-only pull branch cannot be produced by adb, fixtures, or setup (genuinely unscriptable on current evidence) |
| route_12 | scripted | setup_route_12.py bootstrap + wm size 1920x1200 density 240 + account Retry12 + Deposit 100 + Withdrawal 50 |
| route_13 | scripted | setup_route_13.py bootstrap + recurring notifications on + check time device-local now+3min |
| route_14 | scripted | setup_route_14.py bootstrap + account + due recurring transaction + passcode 12345 |
| route_15 | scripted | (no setup cell) |
| route_16 | scripted | (no setup cell) |
| route_17 | scripted | (no setup cell) |
| route_18 | scripted | setup_route_18.py bootstrap + account RetryAcct |
| route_19 | unscriptable | (no setup) double blocker, genuinely unscriptable on current evidence: (a) the prefix reaches showMessage only when the base currency is null, but an app-created database always sets a base currency; (b) getLogcat executes only if Toast.show() throws inside the posted Runnable's catch, and no grounded fault trigger exists on a normal foreground flow |
| route_20 | scripted | setup_route_20.py bootstrap |
| route_21 | scripted | setup_route_21.py bootstrap |
| route_22 | scripted | setup_route_22.py bootstrap + account RetryBills |
| route_23 | scripted | setup_route_23.py bootstrap + account RetryMain |
| route_24 | scripted | setup_route_24.py bootstrap |
| route_25 | scripted | no setup; default-account guard remains a live-run risk (route docstring) |
| route_26 | scripted | setup_route_26.py bootstrap |
| route_27 | scripted | setup_route_27.py bootstrap |
| route_28 | scripted | setup_route_28.py bootstrap (warm launch is the first launch; UID info row remains a live-run risk) |
| route_29 | scripted | setup_route_29.py bootstrap + valid .mmb staged at /sdcard/Download/database.mmb |
| route_30 | scripted | setup_route_30.py bootstrap (recent-list precondition remains a live-run risk) |

## Unscriptable routes: why they stay (merged evidence)

- route_07: Morningstar HTTP download + provider switch. The
  specified-but-unverified HTTP substitute (hosts remount +
  CI-host server) is outside the current run_app contract, so the
  route stays unscriptable; it is not counted as convertible on
  an unverified substitute.
- route_08: Fixer HTTPS download + JSON. The specified-but-unverified
  HTTPS substitute (local HTTPS server + system-CA install) is
  likewise outside the current run_app contract.
- route_11: real online cloud-storage account only
  (Dropbox/OneDrive/GoogleDrive/Box/pCloud enum; no WebDAV). No
  fixture, setup, or adb action can produce a remotely-modified
  database.
- route_19: double blocker (null-base-currency branch unreachable
  with an app-created database; Toast-throw trigger uncreatable on
  a normal foreground flow). Genuinely unscriptable on current
  evidence.

Only routes needing a real online account or credentials stay
unscriptable under the user's cap ruling; routes 07 and 08 stay
because their substitutes are specified but unverified and outside
the run_app contract — that reasoning is part of the forwarded cap
decision, not a silent reclassification.

## Converted routes: what changed (B3 unscriptable to merged scripted)

- route_06: UI-driving setup creates the account (RetryRecur) and
  the recurring-transaction entry the route needs; the B3
  form-entry tap sequence is now grounded in setup_route_06.py.
- route_10: UI-driving setup creates the account (RetryTxAcct)
  and one transaction (payee RetryPayee), so the payee report
  query returns a row.
- route_12: UI-driving setup plus wm size 1920x1200 + density 240
  for the tablet layout (fragmentChart), with Deposit 100 +
  Withdrawal 50 seed data; wm is reset in finally (1-in-3 audit
  contract ruling ACCEPT).
- route_14: UI-driving setup creates the account, a due recurring
  transaction, and passcode 12345; the notification-shade tap is
  via live-only adb (1-in-3 audit contract ruling ACCEPT), and
  the script ends with kill_app + passcode handling.

All four conversions use UI-driving setups under the
MMEX-B3-UIDRIVE contract (see AGENT_NOTES B3 section). Two
contract limits apply to every UI-driving setup here: the
drycheck gap (drycheck never executes setups, and MMEX setups
back no gen: fixture, so setups are entirely dry-unvalidated)
and the return-to-home rule (launch is plain am start -W -n with
no task-clearing flags, so setup UI state leaks into route
start; setups must therefore end back on the route's starting
screen).

## Live-run risks disclosed (not pre-D9 edits)

These are D9 observations, not defects to fix before the dry run:

- route_01: budget + category rows are a follow-up seed, not
  satisfied by the setup.
- route_25: default-account guard remains a live-run risk
  (route docstring).
- route_26: due-bill seed follow-up — if the live run reports
  not_reached, the seed is the follow-up (route docstring
  discloses the unseeded guard openly).
- route_28: UID info row remains a live-run risk.
- route_30: recent-list precondition remains a live-run risk.

## Scope limits of these notes

- Drycheck PASS for an unscriptable row checks only that a
  reason exists. The substance of the 07/08/11/19 reasons comes
  from the grounding notes and the cap decision, not from
  drycheck.
- Drycheck does not resolve launch components; launch components
  were verified by the script audit against the printed manifest,
  not by dry mode.
- No DEVICE rows exist in verification.csv yet by design: they
  appear only after a real run writes device/results.csv.
- Route_26/29 merge diffs are doc-only (route docstring setup
  descriptions rewritten to the setup scripts; setup docstrings'
  route-number typo fixed, route_20 to route_26 / route_29).
  No code change in either.
