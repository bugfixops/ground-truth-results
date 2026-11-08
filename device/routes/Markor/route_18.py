"""Markor route_18: GsPreferenceFragmentBase.tintPrefIconsRecursive.

Edge ids in order: E211966cc, Ed6414d9f, E0254b914, Ed25af8f4, Eba46a594,
E659e191c, E0ecb8e4d, E70fd6983, E19ec7a6b, Ec91b9182, E884e8fa9, Ecec8526f,
E174da89e, Eb5446c49, Eeaffa884, E5fd53742.
Printed route file: graphs/Markor/scratch/route_print/route_18.txt.
ROUTES.csv permissions: none. Fixtures: none.
Setup: push fixtures/Documents; first-run tutorial can trap a tool.
Package: net.gsantner.markor_test.

Flow: launch MainActivity (notebook tab is the default startup tab),
tap the More bottom tab. The More page realizes MoreFragment, which
embeds MoreInfoFragment (a GsPreferenceFragmentBase subclass); its
icon-tint callback chain reaches tintPrefIconsRecursive
(GsPreferenceFragmentBase.java:187).
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
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_18",
               edge_ids=["E211966cc", "Ed6414d9f", "E0254b914", "Ed25af8f4",
                         "Eba46a594", "E659e191c", "E0ecb8e4d", "E70fd6983",
                         "E19ec7a6b", "Ec91b9182", "E884e8fa9", "Ecec8526f",
                         "E174da89e", "Eb5446c49", "Eeaffa884", "E5fd53742"],
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)

    # E211966cc: Tap the Markor launcher icon (process start).
    r.launch("net.gsantner.markor_test/net.gsantner.markor.activity.MainActivity",
             "E211966cc")
    # Ed6414d9f: system calls Application.onCreate -- no user action.
    r.comment("Application.onCreate runs by the system", "Ed6414d9f")
    # E0254b914: MAIN/LAUNCHER intent starts MainActivity -- same launch
    # as E211966cc above; no separate user action.
    r.comment("MainActivity started by the E211966cc launch", "E0254b914")
    # Ed25af8f4: system calls Activity.onCreate -- no user action.
    r.comment("Activity.onCreate runs by the system", "Ed25af8f4")
    # Eba46a594: system calls onStart then onResume -- no user action.
    r.comment("onStart/onResume run by the system", "Eba46a594")
    # E659e191c: performResume calls onPostResume -- no user action.
    r.comment("onPostResume runs by the system", "E659e191c")
    # E0ecb8e4d: the notebook tab is the default startup tab, shown
    # after a cold start -- no user action (MainActivity.java:105-106).
    r.comment("Notebook tab shown by default after cold start", "E0ecb8e4d")
    # E70fd6983: Tap the More tab in the bottom bar.
    # Bottom-nav label is @string/more = "More"
    # (res/menu/main__bottom_nav.xml, res/values/strings.xml:107).
    # MainActivity.java:519-520 realizes MoreFragment for this tab.
    r.tap("E70fd6983", text="More")
    # E19ec7a6b: FragmentManager creates the More page view -- no user
    # action (MoreFragment.java:46).
    r.comment("MoreFragment view created by the pager", "E19ec7a6b")
    # Ec91b9182: direct call MoreInfoFragment.newInstance -- no user
    # action (MoreFragment.java:51).
    r.comment("MoreInfoFragment.newInstance runs from onViewCreated",
              "Ec91b9182")
    # E884e8fa9: direct call MoreInfoFragment constructor -- no user
    # action (MoreInfoFragment.java:33).
    r.comment("MoreInfoFragment constructor runs from newInstance",
              "E884e8fa9")
    # Ecec8526f: direct call GsPreferenceFragmentBase constructor -- no
    # user action (MoreInfoFragment.java:29, superclass constructor).
    r.comment("GsPreferenceFragmentBase constructor runs from subclass",
              "Ecec8526f")
    # E174da89e: framework listener registered at
    # GsPreferenceFragmentBase.java:172 fires -- no user action; the
    # icon-tint callback is posted by the fragment itself.
    r.comment("updatePreferenceIcons callback fires from the fragment",
              "E174da89e")
    # Eb5446c49: chained framework listener at
    # GsPreferenceFragmentBase.java:177 -- no user action.
    r.comment("Chained icon-tint callback fires", "Eb5446c49")
    # Eeaffa884: call on the live MoreInfoFragment receiver -- no user
    # action (GsPreferenceFragmentBase.java:177).
    r.comment("tintAllPrefIcons runs on the MoreInfoFragment receiver",
              "Eeaffa884")
    # E5fd53742: direct call tintPrefIconsRecursive -- no user action
    # (GsPreferenceFragmentBase.java:187).
    r.comment("tintPrefIconsRecursive runs from tintAllPrefIcons",
              "E5fd53742")
    r.done()


if __name__ == "__main__":
    main()
