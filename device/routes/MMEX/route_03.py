"""MMEX route_03: InvestmentTransactionEditActivity.onActivityResult --
CONVERTED (retry).

Method: InvestmentTransactionEditActivity.onActivityResult
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 E1644b6d5 Ebefa2116
    Ea2519d3d Ef737da54 E05feb9a1 E06d00ceb Ea76e8f15 Eb3519ac5
    E5fcccdfa Ea82a27c6 Edf1407cf E9a2c920e E9c88ed07 E195ec498
    E1fb2742f E9ab6a99b E527238f3 E2fc98a0a E47180ee9 E4398d20a
    E3693b7b2
Printed route source:
    graphs/MMEX/scratch/route_print_final2/InvestmentTransactionEditActivity.onActivityResult.txt
    (25 steps; header env=- state=-). These edge ids match, in order,
    the verification.csv path row for
    InvestmentTransactionEditActivity.onActivityResult exactly
    (checked by the g1 draft; no discrepancy).
Permissions: none (print header env=-; no ENV permission gate).
Fixtures: none (no STATE file gate).
Setup: setup_route_03.py (bootstrap + investment account "RetryInv"
    + stock "TEST"). The previous unscriptable reason (res_id
    first-match collision on the home list; child-row text is
    database data absent from source) is removed by the known
    data: the account name and the stock symbol are chosen by
    setup, so tap(text=...) resolves the child row and the stock
    row respectively. The portfolio list's header row is skipped
    by the app itself (PortfolioFragment.java:144), and the stock
    row's text differs from the header's, so the tap is unambiguous.
Run (from the repo root, after the merger drops this file into
    device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_03.py --package
    com.money.manager.ex --log steps/route_03.log
    --outdir <outdir> [--dry-run] [--adb adb]
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "E1644b6d5",
    "Ebefa2116", "Ea2519d3d", "Ef737da54", "E05feb9a1", "E06d00ceb",
    "Ea76e8f15", "Eb3519ac5", "E5fcccdfa", "Ea82a27c6", "Edf1407cf",
    "E9a2c920e", "E9c88ed07", "E195ec498", "E1fb2742f", "E9ab6a99b",
    "E527238f3", "E2fc98a0a", "E47180ee9", "E4398d20a", "E3693b7b2",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_03", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Launch the MAIN/LAUNCHER activity.
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: Framework calls MainActivity.onCreate.
        r.comment("framework calls MainActivity.onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: onCreate calls initHomeFragment (:238).
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: HomeFragment committed; home screen shown.
        r.comment("home screen shown (HomeFragment committed)",
                  edge="Eff22f7d2")
        # E1644b6d5: Long-press the seeded investment child row,
        # then tap "Portfolio" in its context menu. The child row's
        # text is the setup-known name "RetryInv"; the Portfolio
        # item is added only for INVESTMENT accounts
        # (home/HomeFragment.java:473; menu title R.string.portfolio
        # = "Portfolio", strings.xml:686).
        r.long_tap(text="RetryInv", edge="E1644b6d5")
        r.tap(text="Portfolio", edge="E1644b6d5")
        # Ebefa2116: The Portfolio item posts
        # RequestPortfolioFragmentEvent (HomeFragment.java:474).
        r.comment("Portfolio item posts portfolio event",
                  edge="Ebefa2116")
        # Ea2519d3d: MainActivity.onEvent shows the portfolio
        # fragment (:466). No user action.
        r.comment("onEvent shows portfolio fragment", edge="Ea2519d3d")
        # Ef737da54: showPortfolioFragment creates the fragment
        # (:795). No user action.
        r.comment("showPortfolioFragment creates fragment",
                  edge="Ef737da54")
        # E05feb9a1: newInstance creates the fragment (:57).
        r.comment("newInstance creates fragment", edge="E05feb9a1")
        # E06d00ceb: Framework calls PortfolioFragment.onCreate.
        r.comment("framework calls PortfolioFragment.onCreate",
                  edge="E06d00ceb")
        # Ea76e8f15: Framework calls onCreateView (inflates
        # fragment_portfolio at PortfolioFragment.java:92).
        r.comment("framework calls onCreateView", edge="Ea76e8f15")
        # Eb3519ac5: The portfolio list is shown (list at
        # fragment_portfolio.xml:52). No user action.
        r.comment("portfolio list shown", edge="Eb3519ac5")
        # E5fcccdfa: Tap the seeded stock row. Its text is the
        # setup-known symbol "TEST" (symbolTextView,
        # res/layout/item_portfolio.xml:32; the header row is
        # ignored by the app, PortfolioFragment.java:144).
        r.tap(text="TEST", edge="E5fcccdfa")
        # Ea82a27c6: onItemClick opens the editor for that stock
        # (:149). No user action.
        r.comment("stock row click opens editor", edge="Ea82a27c6")
        # Edf1407cf: openEditInvestmentActivity starts
        # InvestmentTransactionEditActivity (:198-204).
        r.comment("openEditInvestmentActivity starts editor",
                  edge="Edf1407cf")
        # E9a2c920e: Framework calls the editor's onCreate.
        r.comment("framework calls editor onCreate",
                  edge="E9a2c920e")
        # E9c88ed07: onCreate shows the investment transaction edit
        # screen (InvestmentTransactionEditActivity.java:88).
        r.comment("investment transaction edit screen shown",
                  edge="E9c88ed07")
        # E195ec498: Tap the number-of-shares field (numSharesView,
        # activity_investment_transaction_edit.xml:168; @OnClick at
        # InvestmentTransactionEditActivity.java:211-212).
        r.tap(res_id="numSharesView", edge="E195ec498")
        # E1fb2742f: The generated ButterKnife binding calls
        # onNumSharesClick (generated class, INFERRED).
        r.comment("binding calls onNumSharesClick", edge="E1fb2742f")
        # E9ab6a99b: onNumSharesClick opens the calculator with
        # REQUEST_NUM_SHARES (:211-219; common/Calculator.java:79).
        r.comment("onNumSharesClick opens calculator",
                  edge="E9ab6a99b")
        # E527238f3: Framework calls CalculatorActivity.onCreate.
        r.comment("framework calls CalculatorActivity.onCreate",
                  edge="E527238f3")
        # E2fc98a0a: onCreate shows the calculator screen
        # (CalculatorActivity.java:115, 127). No user action.
        r.comment("calculator screen shown", edge="E2fc98a0a")
        # E47180ee9: Enter a share count and press equals. Digit
        # buttons carry their digit as text
        # (activity_calculator.xml:137-160); the equals key is
        # buttonKeyEqual (:162), handled at CalculatorActivity.
        # java:247-250.
        r.tap(text="1", edge="E47180ee9")
        r.tap(text="0", edge="E47180ee9")
        r.tap(res_id="buttonKeyEqual", edge="E47180ee9")
        # E4398d20a: onEqualsClicked returns the amount (:249).
        r.comment("onEqualsClicked returns amount", edge="E4398d20a")
        # E3693b7b2: The calculator result is delivered to the
        # editor's onActivityResult (NUM_SHARES branch,
        # InvestmentTransactionEditActivity.java:128-132) --
        # target reached.
        r.comment("result delivered to onActivityResult (target "
                  "reached)", edge="E3693b7b2")
    finally:
        r.done()


if __name__ == "__main__":
    main()
