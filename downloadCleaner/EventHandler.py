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
        # BUG: self.files shall be dynamic, not be fixed at __init,
        # That's why it cannot configured modification of dir
        # TODO: fix this in on_modified
        self.files = [f for f in path.iterdir() if f.is_file()]
        self.path = path

    def rename_file(self,file:Path,dist:Path):
        '''
        helper function: If a file of the same
        name already exists in the destination folder, the file name is numbered and
        incremented until the filename is unique (prevents overwriting files).    
        
        :param Path source: source of file to be moved
        :param Path destination_path: path to destination directory  
        '''
        if Path( dist/ file.name).exists():
            copy = 0
            while True:
                copy += 1
                new_path = dist / f'{file.stem}-{copy}{file.suffix}'
                if not new_path.exists():
                    return new_path
        else:
            return dist / file.name
                

        
    def on_modified(self, event):
        print("call on_modified")
        for f in self.files:
            # .DS_Store doesn't count as suffix
            if f.name == '.DS_Store':
                continue        
            suffix = f.suffix.lower()
            # check if suffix in extension_paths dict. if yes, then move file to that dir
            if suffix in extension_paths:
                # dist here is folder
                dist = self.path / extension_paths[suffix]
                # check if folder exists
                if not dist.exists():
                    os.makedirs(dist, mode=711)
                    os.chmod(dist, stat.S_IRWXU)
                dist = self.rename_file(f,dist)
                shutil.move(src=f, dst=dist)
                print("Moved f to",dist)
            else:
                # move to other dir
                dist = self.path / "other"
                if not dist.exists():
                    os.makedirs(dist, mode=711)
                shutil.move(src=f, dst=dist)


