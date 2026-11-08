# L4 verdicts — batch 11 (D24)

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 11/6 | AddTagButton.<init>(Context,AttributeSet,int) | UNREACHABLE no_trigger_in_app | UNREACHABLE no_trigger_in_app | INFERRED | verified, no change — D24: 2-arg ctor body printed (AddTagButton.java:43-48: super(context, attrs) + init, NO this(...) delegation); zero programmatic 3-arg construction (grep_D24_newctors.txt: sole `new AddTagButton(` site is the 1-arg form, TorrentTagsList.java:79); zero `extends AddTagButton` (grep_D24_extends.txt, 0 lines); LayoutInflater calls 2-arg only (printed fw_src, batch file) | A printed 3-arg construction site, or a printed 2-arg ctor delegating via this(...) to the 3-arg ctor |
