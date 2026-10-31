import hashlib
import sys

P = '/Users/darshan/Desktop/yang/work/graphs/Aegis/graph_def.py'
BK = '/Users/darshan/Desktop/yang/work/graphs/Aegis/scratch/graph_def_before_s2_G5_1.py'
PRE = '87ece8114853b44f2467d9b76e73b2e9'


def md5(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


if md5(P) != PRE or md5(BK) != PRE:
    sys.exit('precondition failed: graph_def %s backup %s (want %s)' % (md5(P), md5(BK), PRE))

with open(P, encoding='utf-8') as f:
    src = f.read()

EDITS = []

# R1 step 14: the None tap is a GUI edge from the picker page (was ENTERS with a wrong evidence line)
EDITS.append((
"""e('S_INTRO_PICKER', 'S_INTRO_PICKER@NONE', 'ENTERS', 'the user checks None on the security picker (the picker now holds None)',
  evidence='SRC ui/slides/SecurityPickerSlide.java:72-88; INFERRED the radio group checks the tapped button (android.widget.RadioGroup not read)')""",
"""gui('S_INTRO_PICKER', 'S_INTRO_PICKER@NONE', 'Tap the None radio button on the security picker',
    evidence='SRC res/layout/fragment_security_picker_slide.xml:41 (rb_none tapped); INFERRED the radio group checks the tapped button (android.widget.RadioGroup not read); SRC ui/intro/IntroBaseActivity.java:85 (Next saves cryptType, SecurityPickerSlide.java:72-88)')"""))

# R1 step 17: the pager call is a direct CALL chain, not a FRAMEWORK (AppIntro) callback; the NONE condition moves to step 18
EDITS.append((
"""e('IntroBaseActivity.goToNextSlide@NONE', 'IntroActivity.onBeforeSlideChanged@NONE', 'FRAMEWORK',
  'the slide changes after None is chosen: IntroActivity can skip the setup slide',
  guard='the security picker chose none (SecurityPickerSlide.onSaveIntroState saves cryptType, IntroBaseActivity.java:85)',
  evidence=FW_APPINTRO + '; SRC ui/intro/IntroBaseActivity.java:80-93; SRC ui/IntroActivity.java:50-55')""",
"""e('IntroBaseActivity.goToNextSlide@NONE', 'IntroActivity.onBeforeSlideChanged@NONE', 'CALL',
  'the pager moves on: setPagerPosition calls onBeforeSlideChanged, which IntroActivity overrides',
  guard='the current slide is finished and it is not the last slide (IntroBaseActivity.java:82-86)',
  evidence='SRC ui/intro/IntroBaseActivity.java:86,138,149-151; SRC ui/IntroActivity.java:45')"""))

# R1 step 21: guard text only (the VaultManager.initNew producer edge cannot be forced into the route; the router is state-blind)
EDITS.append((
"""e('IntroActivity.onDonePressed', 'MainActivity.lambda$new$1', 'RESULT', 'setResult(RESULT_OK) and finish: the list starts',
  guard='the vault was created or imported without an error dialog (the error branches return at 104 and 121)',""",
"""e('IntroActivity.onDonePressed', 'MainActivity.lambda$new$1', 'RESULT', 'setResult(RESULT_OK) and finish: the list starts',
  guard='the vault was created (IntroActivity.java:100 VaultManager.initNew; that producer is a separate edge and is not shown on this route) or imported, with no error dialog (the error branches return at 104 and 121); the none path needs creds null (IntroActivity.java:92-96)',"""))

# R1 step 22: RESULT_OK guard
EDITS.append((
"""e('MainActivity.lambda$new$1', 'MainActivity.onIntroResult', 'CALL', 'RESULT_OK from the intro: the list is loaded',
  evidence='SRC ui/MainActivity.java:142-148')""",
"""e('MainActivity.lambda$new$1', 'MainActivity.onIntroResult', 'CALL', 'RESULT_OK from the intro: the list is loaded',
  guard='the intro returned RESULT_OK (MainActivity.java:145)',
  evidence='SRC ui/MainActivity.java:142-148')"""))

# R2 step 9: hand edge with the guard (replaces the auto row IconPackManager.rescanIconPacks -> IconPack.fromBytes)
EDITS.append((
"""  evidence='SRC icons/IconPackManager.java:84-90')""",
"""  evidence='SRC icons/IconPackManager.java:84-90')

# G5 (stage 2): the pack load in rescanIconPacks carries its guard (this hand edge replaces the auto row for the pair)
e('IconPackManager.rescanIconPacks', 'IconPack.fromBytes', 'CALL', 'each pack folder with a UUID name and a readable definition file is parsed at startup',
  guard='the icons dir lists files, the entry is a directory with a UUID name, its latest version dir is non-null, and the pack definition file opens (IconPackManager.java:136-158)',
  evidence='SRC icons/IconPackManager.java:136-158 (bytecode line 158)')"""))

# R3 step 13: per-edge evidence (FW_STREAM is shared by 9 edges and is not changed)
EDITS.append((
"""  evidence=FW_STREAM + '; SRC ui/views/EntryAdapter.java:204-210')""",
"""  evidence='INFERRED java.util.stream: the terminal allMatch (EntryAdapter.java:205) runs the predicate lambda once per token (JDK source not read); SRC ui/views/EntryAdapter.java:204-210')"""))

# R3 step 15: per-edge evidence
EDITS.append((
"""  evidence=FW_STREAM + '; SRC ui/views/EntryAdapter.java:226-227')""",
"""  evidence='INFERRED java.util.stream: the terminal anyMatch (EntryAdapter.java:229) pulls elements through filter and map (JDK source not read); SRC ui/views/EntryAdapter.java:226-229')"""))

# R3 steps 8, 10, 14: hand edges with guards (each replaces the auto row for its pair)
EDITS.append((
"""  evidence=FW_STREAM + '; SRC ui/views/EntryAdapter.java:228-229')""",
"""  evidence=FW_STREAM + '; SRC ui/views/EntryAdapter.java:228-229')

# G5 (stage 2): hand edges that carry the guards for the search-filter calls (each replaces the auto row for its pair)
e('MainActivity.onCreateOptionsMenu', 'EntryListView.setSearchFilter', 'CALL', 'a submitted search is restored when the menu is created: the list is filtered by it',
  guard='_pendingSearchQuery == null and _submittedSearchQuery != null (MainActivity.java:1066-1073)',
  evidence='SRC ui/MainActivity.java:1066-1073 (bytecode line 1073)')
e('EntryAdapter.setSearchFilter', 'EntryAdapter.refreshEntryList', 'CALL', 'a changed search text refreshes the list',
  guard='the new search text differs from the current _searchFilter (EntryAdapter.java:271)',
  evidence='SRC ui/views/EntryAdapter.java:271-273 (bytecode line 273)')
e('EntryAdapter.lambda$isEntryFiltered$0', 'EntryAdapter.doesAnyGroupMatchSearchFilter', 'CALL', 'the search token is tested against the group names',
  guard='_searchBehaviorMask includes SEARCH_IN_GROUPS and the token did not match the issuer, name or note (EntryAdapter.java:206-209)',
  evidence='SRC ui/views/EntryAdapter.java:206-209 (bytecode line 209)')"""))

for i, (old, new) in enumerate(EDITS, 1):
    n = src.count(old)
    if n != 1:
        sys.exit('anchor %d matches %d times: %r' % (i, n, old[:90]))
    src = src.replace(old, new, 1)

with open(P, 'w', encoding='utf-8') as f:
    f.write(src)

print('anchors applied: %d' % len(EDITS))
print('graph_def md5 now: %s' % md5(P))
