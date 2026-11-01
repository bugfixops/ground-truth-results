# AmazeFileManager — LESSONS DRAFT (local mirror only, not final)

Status: DRAFT — bullets drawn from tonight's re-derivation and the prior
WP2 reports (input only). Final LESSONS.md must be written after the
build and sampler pass on a full checkout.

- Receiver type beats method name: `request.clone()` at
  AppsAdapterPreloadModel.java:45 is GlideRequest.clone, not
  GlideOptions.clone, because the field is declared
  GlideRequest<Drawable>; bare-name greps (old glide_method_grep.txt)
  conflated the two and also matched unrelated methods
  (SharedPreferences.Editor.apply, URLDecoder.decode).
- Lambda numbering is not source order: SftpConnectDialog's
  lambda$null$2 / $6 are dialog handlers by descriptor
  (trailing DialogInterface,int), and only lambda$null$5 (7 captures,
  no trailing interface parameter) fits the removeConnection Runnable;
  assigning $2 vs $6 needs bytecode order, not guessing.
- Method references are call sites: `rowItem.iconData::setImageBroken`
  passed as an OnImageProcessed argument is a real route to
  IconDataParcelable.setImageBroken even though no `setImageBroken(...)`
  call text exists; likewise Parcelable callbacks arrive via Bundle
  marshalling, not direct calls.
- A one-line citation error can hide a wrong edge: the E89 edge cited
  :198 (a closing brace) for an `.execute()` at :199, and its source
  lambda was wrong as well — check both the line and the method.
- Absence in a printed subset is not absence in the app: no
  UNREACHABLE verdict was assigned tonight for any method whose
  whole-tree caller hunt was not completed (13 Glide methods,
  SimpleTextWatcher.afterTextChanged, TextEditorActivity ENV gate).
- The connector's ~1 MB display limit is a hard blocker for this app:
  graph_def.py, auto_calls.json, and methods.csv are all over it, and
  there is no range read — plan full-checkout work accordingly rather
  than working around it with search snippets or substitute files.
