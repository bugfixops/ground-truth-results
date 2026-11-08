#!/usr/bin/env python3
"""
Apply repair proposals from 1.md, 2.md, 3.md, 4.md systematically.
"""

import re
import sys

def apply_proposal_1_renames(text):
    """Apply all the Full pkg→canonical renames from proposal 1.md"""
    # Dict of old name -> new name
    renames = {
        'com.amaze.filemanager.activities.MainActivity.onActivityResult': 'MainActivity.onActivityResult',
        'com.amaze.filemanager.activities.MainActivity.onCreate': 'MainActivity.onCreate',
        'com.amaze.filemanager.activities.MainActivity.onPause': 'MainActivity.onPause',
        'com.amaze.filemanager.asynchronous.asynctasks.ssh.SshAuthenticationTask.doInBackground': 'SshAuthenticationTask.doInBackground',
        'com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.<init>': 'CustomSshJConfig.<init>',
        'com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.init': 'CustomSshJConfig.init',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$1.<init>': 'BottomBar$1.<init>',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$1.onFinish': 'BottomBar$1.onFinish',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$1.onTick': 'BottomBar$1.onTick',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$3.<init>': 'BottomBar$3.<init>',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$3.lambda$onAnimationEnd$0': 'BottomBar$3.lambda$onAnimationEnd$0',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$3.lambda$onAnimationStart$1': 'BottomBar$3.lambda$onAnimationStart$1',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationCancel': 'BottomBar$3.onAnimationCancel',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationEnd': 'BottomBar$3.onAnimationEnd',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$3.onAnimationStart': 'BottomBar$3.onAnimationStart',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$4.<init>': 'BottomBar$4.<init>',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$4.lambda$onAnimationEnd$0': 'BottomBar$4.lambda$onAnimationEnd$0',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$4.lambda$onAnimationStart$1': 'BottomBar$4.lambda$onAnimationStart$1',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$4.onAnimationEnd': 'BottomBar$4.onAnimationEnd',
        'com.amaze.filemanager.ui.views.appbar.BottomBar$4.onAnimationStart': 'BottomBar$4.onAnimationStart',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.<init>': 'BottomBar.<init>',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.areButtonsShowing': 'BottomBar.areButtonsShowing',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.createArrow': 'BottomBar.createArrow',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.createFolderButton': 'BottomBar.createFolderButton',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$sendScroll$4': 'BottomBar.lambda$sendScroll$4',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$0': 'BottomBar.lambda$showButtons$0',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$1': 'BottomBar.lambda$showButtons$1',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$2': 'BottomBar.lambda$showButtons$2',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.lambda$showButtons$3': 'BottomBar.lambda$showButtons$3',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.onTouch': 'BottomBar.onTouch',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.resetClickListener': 'BottomBar.resetClickListener',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.sendScroll': 'BottomBar.sendScroll',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.setBackgroundColor': 'BottomBar.setBackgroundColor',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.setClickListener': 'BottomBar.setClickListener',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.setFullPathText': 'BottomBar.setFullPathText',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.setPathText': 'BottomBar.setPathText',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.setVisibility': 'BottomBar.setVisibility',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.showButtons': 'BottomBar.showButtons',
        'com.amaze.filemanager.ui.views.appbar.BottomBar.updatePath': 'BottomBar.updatePath',
        'com.amaze.filemanager.ui.views.drawer.Drawer.<init>': 'Drawer.<init>',
        'com.amaze.filemanager.ui.views.drawer.Drawer.deselectEverything': 'Drawer.deselectEverything',
        'com.amaze.filemanager.ui.views.drawer.Drawer.refreshDrawer': 'Drawer.refreshDrawer',
        'com.amaze.filemanager.ui.views.drawer.Drawer.selectCorrectDrawerItemForPath': 'Drawer.selectCorrectDrawerItemForPath',
    }
    
    # Replace each old name with new name
    # Need to be careful to match full names, not partial matches
    for old_name, new_name in renames.items():
        # Replace in e() calls - match quoted strings
        text = re.sub(
            r"(['\"])(" + re.escape(old_name) + r")(['\"])",
            r"\1" + new_name + r"\3",
            text
        )
    
    return text

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    
    with open(graph_path, 'r') as f:
        text = f.read()
    
    print("Applying proposal 1 renames...")
    text = apply_proposal_1_renames(text)
    
    with open(graph_path, 'w') as f:
        f.write(text)
    
    print("Done! Applied renames from proposal 1.")

if __name__ == '__main__':
    main()
