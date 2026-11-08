# Batch 03 output - READ-ONLY helper slot 3
# Generated: 2024-10-28 23:35

# Method 1: TabFragment.onPageSelected
e('TabFragment.onCreateView', 'TabFragment.onPageSelected', 'LIFECYCLE',
  'ViewPager.OnPageChangeListener callback registered at line 102',
  evidence='SRC TabFragment.java:102 addOnPageChangeListener(this); TabFragment implements ViewPager.OnPageChangeListener (line 45); framework callback dispatch is INFERRED (ViewPager is support library, source not in fw_src)')

# Method 2: ThemedTextView.<init>
e('RecyclerAdapter.onCreateViewHolder', 'ThemedTextView.<init>', 'FRAMEWORK',
  'View constructor called during layout inflation',
  evidence='SRC RecyclerAdapter.java:467 mInflater.inflate(R.layout.rowlayout, parent, false); rowlayout.xml contains ThemedTextView; FW-SRC LayoutInflater.java:647 constructor.newInstance(args) calls View(Context, AttributeSet) constructor')

# Method 3: UsbOtgRepresentation.equals
UNREACHABLE['UsbOtgRepresentation.equals'] = (
    'no_trigger_in_app',
    'Object.equals() override never called: grep over app source shows no .equals() calls on UsbOtgRepresentation objects, and the List<UsbOtgRepresentation> usage only calls isEmpty() and get(0), never contains/remove/indexOf or other collection methods that would invoke equals()',
    'SRC MainActivity.java:1134-1151 (List operations: isEmpty(), get(0) only); OTGUtil.java:131-147 (returns ArrayList); SingletonUsbOtg.java:42-44 (uses hashCode(), not equals())',
    'SOURCE'
)

# Method 4: WarnableTextInputLayout.<init>
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'WarnableTextInputLayout.<init>', 'FRAMEWORK',
  'View constructor called during layout inflation',
  evidence='SRC GeneralDialogCreation.java:723 View.inflate(c, R.layout.dialog_encrypt_authenticate, null); dialog_encrypt_authenticate.xml contains WarnableTextInputLayout; FW-SRC LayoutInflater.java:647 constructor.newInstance(args) calls View(Context, AttributeSet) constructor')

