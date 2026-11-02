# Route_31 unscriptable — hash-checker `LogUtils.e`

- Route: route_31
- Method: `LogUtils.e`
- Status in ROUTES.csv: `unscriptable: LogUtils.e fires only in the
  ActivityNotFoundException catch when no app handles
  ACTION_OPEN_DOCUMENT (HashCalculatorFragment.java:191-200); on the
  replay image DocumentsUI handles the intent, and the harness has no
  supported component-disable action.`
- No script: unscriptable routes have no script. The former
  `route_31.py` (helper group d3-31-35) is NOT in the push bundle;
  the helper original is preserved under `helper/d3-31-35/` for the
  audit trail.
- Decision: HC-D3-31 (coordinator decision, section 6, Muse's own,
  for user/Yang review; recorded in AGENT_NOTES.md).
- Label: UNTOUCHED. `LogUtils.e` keeps its verification.csv label.
  Under D7 a not-reached route maps to unclear, never wrong.

## Reason

`LogUtils.e` fires ONLY in the `ActivityNotFoundException` catch in
`HashCalculatorFragment.openSystemFileManager`, when no app handles
`ACTION_OPEN_DOCUMENT`. On the replay image DocumentsUI handles that
intent, so the catch never fires on a normal run. There is no UI
route the app offers that reaches the catch, and the delivered
harness has no supported component-disable action with which to
manufacture the precondition.

## Printed evidence

File: `final_java_only/hash-checker/app/hash-checker-#v3.7.3/app/
src/main/java/com/smlnskgmail/jaman/hashchecker/features/
hashcalculator/HashCalculatorFragment.java`, lines 191-200 (printed
and verified this session):

```
191:     private void openSystemFileManager() {
192:         try {
193:             Intent openExplorerIntent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
194:             openExplorerIntent.addCategory(Intent.CATEGORY_OPENABLE);
195:             openExplorerIntent.setType("*/*");
196:             startActivityForResult(openExplorerIntent, FILE_SELECT);
197:         } catch (ActivityNotFoundException e) {
198:             LogUtils.e(e);
199:             showSnackbarWithoutAction(R.string.message_error_start_file_selector);
200:         }
201:     }
```

- The intent is `ACTION_OPEN_DOCUMENT` (:193) sent with
  `startActivityForResult` (:196).
- The catch is `ActivityNotFoundException` (:197); `LogUtils.e(e)`
  is called at :198, followed by the "Can't find a file manager on
  your device" snackbar (:199, `strings.xml:21` per the D3 audit).
- The route's ROUTES.csv source cell cites
  `HashCalculatorFragment.java:196-199;
  SharedPreferencesSettings.java:44-49` (the second citation is the
  T3 path-ref exception HC-T3-2, retained as supporting evidence
  for the verification row; the route itself ends at the
  openSystemFileManager catch above).
- Printed route file (pushed to the branch as commit c4adf0b):
  `graphs/hash-checker/scratch/route_print/LogUtils.e.txt`.
- env_kinds for this route in methods.csv: `other` (not `other_app`);
  no permission gate, no fixture.

## Superseded approach (why it is not used)

The former script manufactured the precondition by disabling the
system picker with a non-public harness call
(`runner._shell(["pm", "disable-user", "com.android.documentsui"])`
before the "File" tap, re-enabled in a finally block), explicitly
marked PROVISIONAL pending device-lead confirmation. The
independent D3 auditor's PASS for route_31 was explicitly
conditional on that confirmation ("ACCEPT PENDING device-lead
confirmation"). The device lead, as harness owner, has now
responded: the harness has no component-disable action, adding one
is invasive and risks breaking the other picker routes if not
re-enabled per route, and it recommends reclassification instead.
The condition on the PASS has therefore failed. Manufacturing the
precondition via a private shell call is not a supported replay
step and not a UI route the app offers, so the route is
unscriptable rather than scripted-with-a-workaround.

## Route edge ids (16, in ROUTES.csv order, unchanged)

```
E372472a8 E3101d0cd Edeb6bd90 E56501d6f E9e141121 E3755babd
E9574aba4 E3ac2e1c9 E59c1e403 E79b435a7 Ee69c0c42 Ed943ca35
E8c979876 Eff786918 E12829a50 E76223917
```

## Counts effect

Hash-checker device routes: 37 total = 36 scripted + 1 unscriptable
(route_31) = 2.7% unscriptable, within the D3 10% cap. Previously
37 scripted / 0 unscriptable. No other route's status changed.
