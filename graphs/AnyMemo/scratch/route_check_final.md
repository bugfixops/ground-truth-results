# AnyMemo round 3: final route check table

One row per method in the final draw (scratch/kiro_sample_30_final.txt, seed 20261025).
steps = route_edge_ids length = steps_from_launch; steps printed = steps printed by
scratch/route_print.py into scratch/route_print/<method>.txt. Every route judged correct
against its printed source lines (if/catch/for conditions) and AGENT_BRIEF_V2.md section 5.

| method | steps | steps printed | verdict | printed file | one-line reason |
| --- | --- | --- | --- | --- | --- |
| DefaultScheduler.randomNumber | 48 | 48 | correct | scratch/route_print/DefaultScheduler.randomNumber.txt | cold start -> merge -> Preview/Edit search -> card flip -> quiz grade -> schedule noise; every guard source-cited |
| UploadDropboxActivity.onDestroy | 46 | 46 | correct | scratch/route_print/UploadDropboxActivity.onDestroy.txt | Download tab -> Dropbox login (ENV account) -> upload confirm -> upload done -> Back/volume key destroys activity |
| CardDaoImpl.getCardsByCategory | 35 | 35 | correct | scratch/route_print/CardDaoImpl.getCardsByCategory.txt | Recent tap -> Open actions -> Quiz launcher -> quiz by category; refill(Category) guarded by filterCategory!=null + category exists |
| Mnemosyne2CardsImporter$ValueType.<clinit> | 37 | 37 | correct | scratch/route_print/Mnemosyne2CardsImporter_ValueType.<clinit>.txt | Misc Export expanded -> Converter -> file picked (isFile) -> import conversion service -> xmlToCards clinit |
| DownloaderUtils.downloadFile | 34 | 34 | correct | scratch/route_print/DownloaderUtils.downloadFile.txt | Download tab -> AnyMemo downloader -> list -> confirm -> fetch task -> downloadFile when name ends .db |
| AudioRecorderFragment$2.<init> | 43 | 43 | correct | scratch/route_print/AudioRecorderFragment_2.<init>.txt | CardList long-press -> CardEditor -> add audio (RECORD_AUDIO granted) -> recorder dialog -> record/stop then play |
| SettingsScreen$11.onFileBrowserFileClick | 33 | 33 | correct | scratch/route_print/SettingsScreen_11.onFileBrowserFileClick.txt | Settings -> qTypefaceEdit opens FileBrowser -> row tapped (isFile) -> onFileBrowserFileClick |
| DropboxApiHelper$4.call | 40 | 40 | correct | scratch/route_print/DropboxApiHelper_4.call.txt | Dropbox login (ENV account) -> list -> confirm -> fetch task -> DropboxListFragment.fetchDatabase -> downloadFile call |
| ExportAnyMemoDbFragment$3.accept | 31 | 31 | correct | scratch/route_print/ExportAnyMemoDbFragment_3.accept.txt | Misc Export -> export db fragment -> file picked -> exportDatabase -> onActivityResult -> accept |
| DatabaseOperationDialogUtil$4$1.onCancel | 26 | 26 | correct | scratch/route_print/DatabaseOperationDialogUtil_4_1.onCancel.txt | Open tab FileBrowser -> row long-press edit dialog -> rename -> Rx subscribe onCancel |
| Option.getCopyClipboard | 39 | 39 | correct | scratch/route_print/Option.getCopyClipboard.txt | Preview/Edit -> card player -> play -> onPlayCard -> gotoCard -> displayCard -> copyToClipboard -> getCopyClipboard |
| Category.setName | 39 | 39 | correct | scratch/route_print/Category.setName.txt | Preview/Edit -> categories dialog -> CategoryEditor -> New button -> NewCategoryTask -> createOrReturn -> setName |
| AMDateUtil.<init> | 38 | 38 | correct | scratch/route_print/AMDateUtil.<init>.txt | Preview/Edit -> CardPlayer study init -> setupGradeButtons -> GradeButtonsFragment Dagger inject -> AMDateUtil ctor |
| Card.setId | 38 | 38 | correct | scratch/route_print/Card.setId.txt | Preview/Edit -> DetailScreen -> save dialog -> SaveCardTask -> saveEntries -> refreshEntries -> setId |
| FileBrowserActivity.fileClickAction | 33 | 33 | correct | scratch/route_print/FileBrowserActivity.fileClickAction.txt | Merge -> FileBrowser activity (ENV storage) -> row tapped (isFile) -> fileClickAction |
| AlgorithmCustomizationScreen$1$1.<init> | 22 | 22 | correct | scratch/route_print/AlgorithmCustomizationScreen_1_1.<init>.txt | Option tab -> OptionScreen pref -> algorithm warn dialog -> AlgorithmCustomizationScreen pref click -> anon ctor |
| Card.toString | 26 | 26 | correct | scratch/route_print/Card.toString.txt | Recent tap study -> LearnQueueManager refill -> flushDirtyCache async -> call -> Card.toString (string concat, INFERRED JLS) |
| SettingsScreen$12.onFileBrowserFileClick | 33 | 33 | correct | scratch/route_print/SettingsScreen_12.onFileBrowserFileClick.txt | Settings -> aTypefaceEdit opens FileBrowser -> row tapped (isFile) -> onFileBrowserFileClick |
| Option$DictApp.parse | 37 | 37 | correct | scratch/route_print/Option_DictApp.parse.txt | Preview/Edit -> CardPlayer gestures -> gesture -> dictionary lookup -> getDictApp -> DictApp.parse |
| FileBrowserFragment.upOneLevel | 23 | 23 | correct | scratch/route_print/FileBrowserFragment.upOneLevel.txt | Open tab FileBrowser -> options menu -> browseTo/fill -> row tapped -> openFile -> upOneLevel (up row) |
| Card.setCreationDate | 29 | 29 | correct | scratch/route_print/Card.setCreationDate.txt | Preview/Edit save path -> refreshEntries -> setCreationDate (same DetailScreen save chain) |
| CardDaoImpl$1.call | 32 | 32 | correct | scratch/route_print/CardDaoImpl_1.call.txt | Open/study path -> dao async call wrapper -> CardDaoImpl$1.call |
| SpeakWord.stripNonCardContent | 32 | 32 | correct | scratch/route_print/SpeakWord.stripNonCardContent.txt | Card player TTS path -> SpeakWord strips non-card content before speaking |
| NotificationChannelUtil.createConversationNotificationChannel | 5 | 5 | correct | scratch/route_print/NotificationChannelUtil.createConversationNotificationChannel.txt | process start -> AMApplication.onCreate -> createNotificationChannels -> conversation channel (API>=26 guard) |
| DaggerAppComponents$ActivityComponentsBuilder.activity | 5 | 5 | correct | scratch/route_print/DaggerAppComponents_ActivityComponentsBuilder.activity.txt | Dagger activity-component builder; reached at component construction (plain) |
| BaseActivity.onResume | 4 | 4 | correct | scratch/route_print/BaseActivity.onResume.txt | cold start lifecycle AnyMemo.onCreate -> onResume (plain) |
| BaseActivity.updateInterfaceLanguage | 4 | 4 | correct | scratch/route_print/BaseActivity.updateInterfaceLanguage.txt | cold start lifecycle -> updateInterfaceLanguage (plain) |
| DaggerAppComponents$ActivityComponentsBuilder.build | 5 | 5 | correct | scratch/route_print/DaggerAppComponents_ActivityComponentsBuilder.build.txt | Dagger activity-component builder build() (plain) |
| NotificationChannelUtil.createCardPlayerNotificationChannel | 5 | 5 | correct | scratch/route_print/NotificationChannelUtil.createCardPlayerNotificationChannel.txt | AMApplication.onCreate -> createNotificationChannels -> card-player channel (API>=26 guard) |
| NotificationChannelUtil.createReviewReminderNotificationChannel | 5 | 5 | correct | scratch/route_print/NotificationChannelUtil.createReviewReminderNotificationChannel.txt | AMApplication.onCreate -> createNotificationChannels -> review-reminder channel (API>=26 guard) |

Counts over the final draw: correct 30, fixed 0, wrong 0, unclear 0.
Error rate = (fixed + wrong) / (correct + fixed + wrong) = 0 / 30 = 0.0.
