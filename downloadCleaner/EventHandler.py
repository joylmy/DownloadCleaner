# class extends watchdog.events.FileSystemEventHandler

"""
1.check current non-folder files
2. move files to subfolder according to its extenstion name. if subfolder does not exist, create it.
if extenstion not exists in extenstion dict, move it to folder others

"""

import os
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from extension import extension_paths
import shutil
import stat


class DownloadsCleanEventHandler(FileSystemEventHandler):
    def __init__(self, path: Path):
        # all are PosixPath object
        self.files = [f for f in path.iterdir() if f.is_file()]
        self.path = path
        # print(self.files)
        
    
    # TODO:ensure depulicated files not be overwritten
    def rename_file():
        # return new path here
        pass


    # TODO:add event as argv
    def on_modified(self):
        for f in self.files:
            suffix = f.suffix.lower()
            # check if suffix in extension_paths dict. if yes, then move file to that dir
            if suffix in extension_paths:
                dist = self.path / extension_paths[suffix]
                if not dist.exists():
                    os.makedirs(dist,mode=711) 
                    os.chmod(dist,stat.S_IRWXU)            
                shutil.move(src=f, dst=dist)
            else:
                # move to other dir
                dist = self.path / "other"
                if not dist.exists():
                    os.makedirs(dist,mode=711)
                shutil.move(src=f, dst=dist)


######################TEST#######################################
test = DownloadsCleanEventHandler(Path.home() / "Downloads")
# test.on_modified()

