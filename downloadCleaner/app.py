'''
1. automatically observe the download folder, Track Download folder
2. Clear current files in the folder, 归类Download现有文件夹内的文件
  - 去新的文件夹
3. move different files going to different folder , 
based on its extention name
  - use a dict to organize it?
4. Run in the background continueslly
5. Run when PC is on
'''

from watchdog.observers import Observer
from pathlib import Path
from time import sleep
 

if __name__ == '__main__':
  watch_path = str(Path.home())+'/Downloads'
  observer = Observer()
  # TODO:event handler
  observer.schedule(event_handler, watch_path, recursive=True)
  observer.start()
  try:
      while True:
          time.sleep(120)
  except KeyboardInterrupt:
      observer.stop()
  observer.join()

