STATUS: RUNNING 23:35

| Method | Label | Kind | Reason | Printed file:lines |
|--------|-------|------|--------|-------------------|
| TabFragment.onPageSelected | REACHABLE | LIFECYCLE | ViewPager.OnPageChangeListener callback registered in TabFragment.onCreateView | SRC TabFragment.java:45 (implements ViewPager.OnPageChangeListener), 102 (mViewPager.addOnPageChangeListener(this)) |
| ThemedTextView.<init> | REACHABLE | FRAMEWORK | View constructor called during layout inflation of rowlayout.xml | SRC RecyclerAdapter.java:467 (mInflater.inflate(R.layout.rowlayout, parent, false)); rowlayout.xml contains ThemedTextView; FW-SRC LayoutInflater.java:647 (constructor.newInstance(args)) |
| UsbOtgRepresentation.equals | UNREACHABLE | no_trigger_in_app | Object.equals() override never called in app | SRC MainActivity.java:1134-1151 (List ops: isEmpty(), get(0) only), OTGUtil.java:131-147 (returns ArrayList), SingletonUsbOtg.java:42-44 (uses hashCode() not equals()) |
| WarnableTextInputLayout.<init> | REACHABLE | FRAMEWORK | View constructor called during layout inflation of dialog_encrypt_authenticate.xml | SRC GeneralDialogCreation.java:723 (View.inflate(c, R.layout.dialog_encrypt_authenticate, null)); dialog_encrypt_authenticate.xml contains WarnableTextInputLayout; FW-SRC LayoutInflater.java:647 (constructor.newInstance(args)) |

STATUS: DONE 23:39
