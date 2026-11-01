# AmazeFileManager — LESSONS.md

- Manifest citations rot between schema versions: re-derive every ENTRY
  block range from the printed manifest; a systematic shift (here, all 8
  services plus the receiver) hides behind individually plausible ranges.
- One executor's AsyncTask edges got linked to every task in the graph
  (ZipService.execute -> 7 unrelated doInBackground/onPostExecute methods).
  Only route-level reading catches a builder heuristic error like that; a
  label count never will.
- Superclass-summary edges silently conflate instances: a shared
  BasicActivity.<init> node linked to one subclass's onCreate makes a
  DatabaseViewerActivity prefix "reach" TextEditorActivity. Always print
  the actual `extends` clause before trusting a lifecycle chain.
- Virtual dispatch decides Glide reachability, not the declared type: the
  receiver of `.listener()` is a GlideRequest at runtime (via
  GlideApp.with().asDrawable()), and a method reference is a call site
  when the receiver invokes it (setImageBroken via OnImageProcessed).
- Sibling stream classes must not be crossed: the SMB server reads a
  SmbStreamer StreamSource and the cloud server reads a CloudStreamSource.
  The server doing the reading determines the target, not the shared
  RandomAccessStream parent.
- Sample draws are route-sensitive: fixing edges redraws the sample, so
  the final table is only valid on the post-fix draw, and dropped routes'
  fixes still belong in the fix log.
- The checker's citation resolver needs the basename form for some paths
  (DecryptService): a correct line number with the wrong path form still
  fails check 2, so match the form passing citations already use.
