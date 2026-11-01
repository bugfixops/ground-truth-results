#!/usr/bin/env python3
"""Markor route_11: WikitextLinkResolver.wikitextPagePathToRelativeFilePath.

Method: WikitextLinkResolver.wikitextPagePathToRelativeFilePath
Edge ids (in route order):
    E211966cc Ed6414d9f E0254b914 Ed25af8f4 Eba46a594 E659e191c
    E0ecb8e4d E54b4aedd E4db63107 E2090721b Ecf5bd27f E472c0c60
    E7c8533fa E96aafd43 E44bd8050
Printed route file: graphs/Markor/scratch/route_print/route_11.txt
ROUTES.csv permissions: none.
ROUTES.csv fixtures: none (the quick-note file is created by the app
    on demand; see AppSettings.getQuickNoteFile / getDefaultQuickNoteFile,
    AppSettings.java:108-119).
Setup (verbatim): push fixtures/Documents; first-run tutorial can trap
    a tool.
No pm clear here (run_app.sh does it) and no fixture push here
    (run_app.sh does it per ROUTES.csv).
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "harness"))
from harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_11",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914",
                         "Ed25af8f4", "Eba46a594", "E659e191c",
                         "E0ecb8e4d", "E54b4aedd", "E4db63107",
                         "E2090721b", "Ecf5bd27f", "E472c0c60",
                         "E7c8533fa", "E96aafd43", "E44bd8050"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E211966cc: Tap the Markor launcher icon (MAIN / LAUNCHER
        # intent filter, AndroidManifest.xml:61-71).
        r.launch(args.package + "/net.gsantner.markor.activity.MainActivity",
                 edge="E211966cc")
        # Ed6414d9f: The system calls Application.onCreate.
        r.comment("system calls Application.onCreate", edge="Ed6414d9f")
        # E0254b914: MAIN / LAUNCHER intent starts MainActivity after
        # Application.onCreate on a cold start. No separate action:
        # the launch above starts it.
        r.comment("system starts MainActivity after Application.onCreate",
                  edge="E0254b914")
        # Ed25af8f4: The system calls Activity.onCreate.
        r.comment("system calls Activity.onCreate", edge="Ed25af8f4")
        # Eba46a594: The system calls Activity.onStart then onResume.
        r.comment("system calls onStart then onResume", edge="Eba46a594")
        # E659e191c: Activity.performResume calls onPostResume.
        r.comment("performResume calls onPostResume", edge="E659e191c")
        # E0ecb8e4d: The notebook tab is the first page the pager
        # shows (position 0, MainActivity.java:105-106). No action.
        r.comment("notebook tab is the default startup tab",
                  edge="E0ecb8e4d")
        # E54b4aedd: Tap a bottom navigation tab. The QuickNote item
        # is res/menu/main__bottom_nav.xml:25-27 (title @string/
        # quicknote = "QuickNote", res/values/string-not_translatable
        # .xml:41); the listener is MainActivity.java:109-114.
        r.tap(edge="E54b4aedd", text="QuickNote")
        # E4db63107: Tab Quick note is shown (the listener selects
        # its position). No action.
        r.comment("quick-note tab is shown", edge="E4db63107")
        # E2090721b: Tap an action button in the toolbar of the editor
        # (the document uses the wikitext format). Setup calls under
        # this same edge, all logged against it: (1) the quick-note
        # file defaults to Markdown (QuickNote.md, AppSettings
        # .java:116-119), so switch format via the editor overflow
        # menu: Format submenu, res/menu/document__edit__menu.xml:
        # 107-141, handled at DocumentEditAndViewFragment.java:
        # 525-538; (2) tap the editor (res/layout/document__fragment
        # __edit.xml:49-50, id document__fragment__edit__highlighting
        # _editor) and type a wikitext link; (3) move the cursor
        # inside the link, because WikitextActionButtons
        # .tryExtractWikitextLink (WikitextActionButtons.java:200-214)
        # only returns a link when the cursor lies strictly inside
        # its bounds; (4) tap the open-link action button. Buttons
        # get their content description from rstr(action.stringId)
        # (ActionButtonBase.java:343-354), and the open-link string
        # resource value is literally "abid_common_open_link_browser"
        # (res/values/string-not_translatable.xml:224); the case is
        # WikitextActionButtons.java:136-138 (openLink()).
        r.tap(edge="E2090721b", desc="More options")
        r.tap(edge="E2090721b", text="Format")
        r.tap(edge="E2090721b", text="Wikitext / Zim")
        r.tap(edge="E2090721b",
              res_id="document__fragment__edit__highlighting_editor")
        r.type_text("[[SomePage]]", edge="E2090721b")
        r.key("DPAD_LEFT", edge="E2090721b")
        r.key("DPAD_LEFT", edge="E2090721b")
        r.key("DPAD_LEFT", edge="E2090721b")
        r.tap(edge="E2090721b", desc="abid_common_open_link_browser")
        # Ecf5bd27f: openLink() is a direct call from onActionClick
        # (WikitextActionButtons.java:137, bytecode).
        r.comment("onActionClick calls openLink directly",
                  edge="Ecf5bd27f")
        # E472c0c60: openLink calls WikitextLinkResolver.resolve
        # (WikitextActionButtons.java:185, bytecode).
        r.comment("openLink calls WikitextLinkResolver.resolve",
                  edge="E472c0c60")
        # E7c8533fa: resolve(String,File,File,boolean) calls
        # resolve(String) (WikitextLinkResolver.java:54, bytecode).
        r.comment("resolve calls resolve(String)", edge="E7c8533fa")
        # E96aafd43: resolve(String) calls resolveWikitextPath
        # (WikitextLinkResolver.java:63, bytecode). The typed
        # [[SomePage]] link matches RELATIVE_PATH, so this path
        # reaches wikitextPagePathToRelativeFilePath.
        r.comment("resolve(String) calls resolveWikitextPath",
                  edge="E96aafd43")
        # E44bd8050: resolveWikitextPath calls
        # wikitextPagePathToRelativeFilePath (WikitextLinkResolver
        # .java:108, bytecode). Target method reached.
        r.comment("resolveWikitextPath calls "
                  "wikitextPagePathToRelativeFilePath", edge="E44bd8050")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
