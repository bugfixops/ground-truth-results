# ================================================================== batch 044 (label_044): com.money.manager.ex.core.ioc DaggerMmxComponent: 3 inject(X) overloads, 31 injectX methods, 5 DaggerMmxComponent$Builder methods: 39 methods, 36 REACHABLE, 3 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_044.md; grep output: graphs/MMEX/parts/label_044.grep.txt.
# Edges: none written here. Every REACHABLE row rests on auto_calls.json CALL records (inject(X) <- class <init> or lifecycle, injectX <- inject(X) in batch 043, Builder.* <- MmexApplication.initializeDependencyInjection), which are not written again (D7). Dagger-generated classes have no source in the source root: their labels are INFERRED.

# The outgoing auto records of the UNREACHABLE injectEditPriceDialog (DaggerMmxComponent.java:488-489) are cut in batch 085
# (EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy) and batch 140 (MmxDateTimeUtils_Factory), D14(a): those targets merge later.

# ================================================================== UNREACHABLE (batch 044)

UNREACHABLE['DaggerMmxComponent.injectEditPriceDialog'] = ('no_trigger_in_app',
  'Dagger-generated static member injector for EditPriceDialog (DaggerMmxComponent.java:280 inside the generated inject(EditPriceDialog) path). Its only caller record is inject(EditPriceDialog), and that is called only from EditPriceDialog.<init> (EditPriceDialog.java:91). Nothing in the app constructs EditPriceDialog: no "new EditPriceDialog", no EditPriceDialog.newInstance, no manifest or resource reference. Framework re-creation of a fragment needs an earlier instance, so none can be re-created either',
  'auto_calls EditPriceDialog.<init> -> inject(EditPriceDialog) (EditPriceDialog.java:91) and inject(EditPriceDialog) -> injectEditPriceDialog (DaggerMmxComponent.java:280); label_044.grep.txt sections 1, 2 (no construction site)',
  'INFERRED')

UNREACHABLE['DaggerMmxComponent$Builder.dbModule'] = ('no_trigger_in_app',
  'Dagger-generated builder setter for DbModule. No caller record exists for it in auto_calls.json. MmexApplication.initializeDependencyInjection calls only builder(), mmxModule(...) and build() (MmexApplication.java:202-204). Builder.build creates a default DbModule itself when none was set (DaggerMmxComponent.java:623), so the setter is never needed',
  'auto_calls.json (0 caller records for Builder.dbModule; Builder.build -> DbModule.<init> at DaggerMmxComponent.java:623); MmexApplication.java:202-204; label_044.grep.txt sections 1, 2',
  'INFERRED')

UNREACHABLE['DaggerMmxComponent$Builder.repositoryModule'] = ('no_trigger_in_app',
  'Dagger-generated builder setter for RepositoryModule. No caller record exists for it in auto_calls.json, and MmexApplication.java:202-204 does not call it. Builder.build creates a default RepositoryModule itself when none was set (DaggerMmxComponent.java:626), so the setter is never needed',
  'auto_calls.json (0 caller records for Builder.repositoryModule; Builder.build -> RepositoryModule.<init> at DaggerMmxComponent.java:626); MmexApplication.java:202-204; label_044.grep.txt sections 1, 2',
  'INFERRED')
