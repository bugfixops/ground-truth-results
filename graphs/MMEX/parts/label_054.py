# ================================================================== batch 054 (label_054): AccountRepository (13 methods),
# AccountTransactionRepository (5), AttachmentRepository (7), BudgetEntryRepository (5), BudgetRepository (5), CategoryRepository (5).
# Result: 33 REACHABLE, 7 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_054.md).
# No e() or GUI edges are written here. Every REACHABLE route runs through auto CALL records (auto_calls.json, USE_AUTO) and through
# the ENTRY, INTENT, GUI and EventBus edges that the owning batches write (CheckingTransactionEditActivity, AccountEditActivity,
# BudgetListFragment, HomeFragment, ...). A CALL edge into any owned method would duplicate an auto record (D7), so none is written.
# No SCREENS key is defined: no edge of this batch starts or ends on a page.
# UNREACHABLE: AttachmentRepository.add, delete, load, save, getAllColumns and BudgetEntryRepository.load, getAllColumns.
# Each has no caller in the app source: the two classes are used only through their constructors, loadAttachmentsFor,
# getKeyForCategories and loadForYear, and every getAllColumns() call in app source has a concrete non-target receiver
# (no Dataset or RepositoryBase receiver, so the abstract Dataset.getAllColumns does not dispatch to these overrides).
# Application classes only (no library or generated method), so no label_054.grep.txt is written.
# sup (D14a): the 14 auto CALL records whose caller is one of the UNREACHABLE methods of this batch are cut.

UNREACHABLE['AttachmentRepository.add'] = ('no_trigger_in_app',
    'never called: the only uses of AttachmentRepository in app source are the constructor sites (MmxContentProvider.java:114, CheckingTransactionEditActivity.java:403) and loadAttachmentsFor (line 404)',
    'datalayer/AttachmentRepository.java:51-53; MmxContentProvider.java:114; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['AttachmentRepository.delete'] = ('no_trigger_in_app',
    'never called: no call site of delete(int) in app source; the instance uses above are the constructor and loadAttachmentsFor only',
    'datalayer/AttachmentRepository.java:55-60; MmxContentProvider.java:114; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['AttachmentRepository.getAllColumns'] = ('no_trigger_in_app',
    'its only direct caller is AttachmentRepository.load (line 66), itself UNREACHABLE; no virtual getAllColumns() call reaches this override (every receiver in app source is a concrete non-Attachment type)',
    'datalayer/AttachmentRepository.java:40-49, 62-71; auto_calls.json (AttachmentRepository.load -> AttachmentRepository.getAllColumns, line 66)', 'SOURCE')

UNREACHABLE['AttachmentRepository.load'] = ('no_trigger_in_app',
    'never called: no call site of load(Integer) in app source; loadAttachmentsFor reads the attachments by a query and does not use load',
    'datalayer/AttachmentRepository.java:62-71; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['AttachmentRepository.save'] = ('no_trigger_in_app',
    'never called: no call site of save(Attachment) in app source',
    'datalayer/AttachmentRepository.java:93-96; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['BudgetEntryRepository.getAllColumns'] = ('no_trigger_in_app',
    'no getAllColumns() call on a BudgetEntryRepository or on a Dataset/RepositoryBase receiver in app source; loadForYear builds its own query and no auto_calls.json record targets this method',
    'datalayer/BudgetEntryRepository.java:44; auto_calls.json (no record with this dst)', 'SOURCE')

UNREACHABLE['BudgetEntryRepository.load'] = ('no_trigger_in_app',
    'never called: the class is used only through its constructor (MmxContentProvider.java:108, BudgetAdapter.java:251), the static getKeyForCategories (BudgetAdapter.java:226, 239) and loadForYear (BudgetAdapter.java:252); no load(int) call',
    'datalayer/BudgetEntryRepository.java:52-64; BudgetAdapter.java:226, 239, 251-252; MmxContentProvider.java:108', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AttachmentRepository.add', 'RepositoryBase.insert'),
    ('AttachmentRepository.delete', 'MmxDatabaseUtils.<clinit>'),
    ('AttachmentRepository.delete', 'RepositoryBase.delete'),
    ('AttachmentRepository.delete', 'MmxDatabaseUtils.getArgsForId'),
    ('AttachmentRepository.load', 'MmxDatabaseUtils.<clinit>'),
    ('AttachmentRepository.load', 'RepositoryBase.first'),
    ('AttachmentRepository.load', 'MmxDatabaseUtils.getArgsForId'),
    ('AttachmentRepository.load', 'AttachmentRepository.getAllColumns'),
    ('AttachmentRepository.save', 'RepositoryBase.update(EntityBase,String)'),
    ('AttachmentRepository.save', 'Attachment.getId'),
    ('BudgetEntryRepository.load', 'RepositoryBase.first'),
    ('BudgetEntryRepository.load', 'WhereStatementGenerator.getWhere'),
    ('BudgetEntryRepository.load', 'WhereStatementGenerator.addStatement(String,String,Integer)'),
    ('BudgetEntryRepository.load', 'WhereStatementGenerator.<init>'))
