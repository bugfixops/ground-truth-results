STATUS: RUNNING 23:30

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| HybridFile$1.<init> | REACHABLE | | Called from HybridFile.lastModified when mode==SFTP | SRC HybridFile.java:194 |
| HybridFile$1.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$2.<init> | REACHABLE | | Called from HybridFile.length when mode==SFTP | SRC HybridFile.java:224 |
| HybridFile$2.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$4.<init> | REACHABLE | | Called from HybridFile.isDirectory(Context) when mode==SFTP | SRC HybridFile.java:485 |
| HybridFile$4.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$5.<init> | REACHABLE | | Called from HybridFile.folderSize(Context) when mode==SFTP | SRC HybridFile.java:584 |
| HybridFile$5.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$6.<init> | REACHABLE | | Called from HybridFile.getUsableSpace when mode==SFTP | SRC HybridFile.java:651 |
| HybridFile$6.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$7.<init> | REACHABLE | | Called from HybridFile.getTotal(Context) when mode==SFTP | SRC HybridFile.java:704 |
| HybridFile$7.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$8.<init> | REACHABLE | | Called from HybridFile.forEachChildrenFile when mode==SFTP | SRC HybridFile.java:737 |
| HybridFile$8.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$9.<init> | REACHABLE | | Called from HybridFile.listFiles(Context,boolean) when mode==SFTP | SRC HybridFile.java:810 |
| HybridFile$9.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$9$1.<init> | INCOMPLETE | | Cannot locate instantiation in source; constructor signature suggests RemoteFile subclass but not found in HybridFile.java:810-831 | Method signature in method_list.json |
| HybridFile$9$1.close | INCOMPLETE | | Depends on HybridFile$9$1.<init> | Same as above |
| HybridFile$10.<init> | REACHABLE | | Called from HybridFile.getInputStream when mode==SFTP | SRC HybridFile.java:905 |
| HybridFile$10.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$10$1.<init> | REACHABLE | | Called from HybridFile$10.execute | SRC HybridFile.java:909 rf.new RemoteFileInputStream |
| HybridFile$10$1.close | REACHABLE | | Overrides RemoteFileInputStream.close, called when stream is closed | SRC HybridFile.java:911-919 method definition |
| HybridFile$11.<init> | REACHABLE | | Called from HybridFile.getInputStream(Context) when mode==SFTP | SRC HybridFile.java:948 |
| HybridFile$11.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$11$1.<init> | REACHABLE | | Called from HybridFile$11.execute | SRC HybridFile.java:953 rf.new RemoteFileInputStream |
| HybridFile$11$1.close | REACHABLE | | Overrides RemoteFileInputStream.close, called when stream is closed | SRC HybridFile.java:955-966 method definition |
| HybridFile$12.<init> | REACHABLE | | Called from HybridFile.getOutputStream(Context) when mode==SFTP | SRC HybridFile.java:1021 |
| HybridFile$12.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:74 calls template.execute |
| HybridFile$13.<init> | REACHABLE | | Called from HybridFile.exists when mode==SFTP | SRC HybridFile.java:1078 |
| HybridFile$13.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |
| HybridFile$14.<init> | REACHABLE | | Called from HybridFile.mkdir(Context) when mode==SFTP | SRC HybridFile.java:1156 |
| HybridFile$14.execute | REACHABLE | | Framework callback from SshClientUtils.execute | SRC SshClientUtils.java:134 calls template.execute |

STATUS: INCOMPLETE 23:33 HybridFile$9$1 methods cannot be verified in source
