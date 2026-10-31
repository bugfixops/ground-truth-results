# R6D: Aegis 3.4.2 route check (3 routes)

Saved by the coordinator from the helper's hand-back (the helper could not write files). Read-only check of G4_3, G4_4, G4_5.

## VaultGroup.equals (steps: 28): ERROR 1, UNCLEAR 20, OK 7
- Step 28 (Ece1490d7, FRAMEWORK lambda -> VaultGroup.equals): ERROR. Verified by the coordinator: GroupManagerActivity.java:150-151 is HashSet(all groups).removeAll(getUsedGroups()); VaultRepository.java:321-330 builds the used list. JDK AbstractSet.removeAll (INFERRED, JDK source not on disk) reaches VaultGroup.equals only through ArrayList.indexOf in the branch where every group is used and at least one group exists. The fresh route has no groups and no entries, so no in-run producer is on the route.
- Steps 8-27: UNCLEAR, inherit from step 8 (cross-run plain-text vault file written by an earlier intro run; IntroActivity.java:100). Not an error under rule D2.
- Suggested fix: an in-run producer chain between step 9 (S_LIST) and step 10 (add a group in EditEntryActivity.java:403-418, vault.addGroup at 410; save with it selected, EditEntryActivity.java:800-804). Structural: the state-blind router will not pick that chain on its own.

## OtpInfo.isAlgorithmValid (steps: 17): ERROR 0, UNCLEAR 10, OK 7
- Steps 8-17: UNCLEAR (cross-run vault file, inherits from step 8).

## GlideOptions.clone (steps: 15): ERROR 0, UNCLEAR 0, OK 15
- Framework and library steps are INFERRED (androidx, Glide not on disk); build classes checked.
