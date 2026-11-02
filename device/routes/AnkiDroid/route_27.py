#!/usr/bin/env python3
"""AnkiDroid route_27: Decks.id(String,boolean).

Method: Decks.id(String,boolean)
Target verdict: FIXED (route_table.md route 27)
Route followed: the final BFS route (11 steps). The fix guards are
    in the graph; the script must satisfy them: not mSyncOnResume
    and collection open; focused deck differs from the current deck;
    deck id not in the displayed deck list; deck has at least one
    parent (name contains "::").
Edge ids in order:
    E48de6d58 E26d20f74 E1ad4ef9b E553ad2d8 E0b111c68 Ed294a91e
    Edd7cc90a E70bf0011 E7e48b538 E390606b0 E5762310b
Printed route: graphs/AnkiDroid/scratch/route_print/
    Decks.id(String,boolean).txt
Permissions: android.permission.WRITE_EXTERNAL_STORAGE (run_app.sh
    grant for collection access; see route_16 for the full manifest
    list). No graph env entry is carried on this route's edges.
Fixtures: collection file exists; a nested deck whose name contains
    "::" (so it has at least one parent); a stored focused deck that
    differs from the current deck and whose id is not in the displayed
    deck list; launch is not a sync-on-resume launch and the
    collection is open.
Launcher: <package>/.IntentHandler (AndroidManifest.xml:81-89,
    MAIN/LAUNCHER). run_app.sh setup precedes this script; see
    route_16. At merge time this file lives under
    device/routes/AnkiDroid/, so the import matches Currency.

Mapping notes:
  - No user action is needed after launch: every step is automatic
    once the deck list loads, given the fixtures above.
  - FIXTURE FLAG: the exact mechanism that sets the stored focused
    deck (which preference or intent extra sets mFocusedDeck) was
    not re-verified in this draft beyond the guard text on
    Edd7cc90a ("focused deck differs from current deck; result
    non-null"). The merger must confirm the fixture sets that state
    before a real run; if it cannot be set, this route needs a
    different entry, not a forced tap.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness import Runner  # noqa: E402

EDGE_IDS = [
    "E48de6d58", "E26d20f74", "E1ad4ef9b", "E553ad2d8", "E0b111c68",
    "Ed294a91e", "Edd7cc90a", "E70bf0011", "E7e48b538", "E390606b0",
    "E5762310b",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="AnkiDroid route_27")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(package=args.package, route="route_27", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    # E48de6d58 S_ENTRY -> IntentHandler.onCreate.
    r.launch(args.package + "/.IntentHandler", edge="E48de6d58")
    # E26d20f74 IntentHandler.onCreate -> DeckPicker.<init>.
    r.comment("launcher else branch starts DeckPicker", edge="E26d20f74")
    # E1ad4ef9b DeckPicker.<init> -> DeckPicker.onCreate.
    r.comment("system instantiates DeckPicker, then onCreate",
              edge="E1ad4ef9b")
    # E553ad2d8 DeckPicker.onCreate -> DeckPicker.onResume.
    r.comment("DeckPicker resumed", edge="E553ad2d8")
    # E0b111c68 DeckPicker.onResume -> DeckPicker.updateDeckList:
    # guard not mSyncOnResume and collection open (colIsOpen()).
    r.comment("deck list updated", edge="E0b111c68")
    # Ed294a91e DeckPicker.updateDeckList ->
    # DeckPicker$22.onPostExecute. Automatic.
    r.comment("deck list load finished", edge="Ed294a91e")
    # Edd7cc90a DeckPicker$22.onPostExecute ->
    # DeckPicker.scrollDecklistToDeck: guard focused deck differs
    # from current deck, result non-null. Automatic.
    r.comment("scroll to focused deck", edge="Edd7cc90a")
    # E70bf0011 DeckPicker.scrollDecklistToDeck ->
    # DeckAdapter.findDeckPosition. Automatic.
    r.comment("deck position looked up", edge="E70bf0011")
    # E7e48b538 DeckAdapter.findDeckPosition -> Decks.parents: guard
    # deck id not in the displayed deck list. Automatic.
    r.comment("deck parents walked", edge="E7e48b538")
    # E390606b0 Decks.parents -> Decks.id(String): guard deck has at
    # least one parent (name contains "::"). Automatic.
    r.comment("parent deck id resolved", edge="E390606b0")
    # E5762310b Decks.id(String) -> Decks.id(String,boolean).
    # Automatic; this is the target edge.
    r.comment("deck id with boolean flag reached", edge="E5762310b")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
