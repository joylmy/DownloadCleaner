"""

4. Run in the background continueslly
5. Run when PC is on
"""

import time
from watchdog.observers import Observer
from pathlib import Path
from extension import extension_paths
from EventHandler import DownloadsCleanEventHandler


# if __name__ == '__main__' this app.py run as the main programe, not imported by others
if __name__ == "__main__":
    # / only for path object
    watch_path = Path.home() / "Downloads"
    # TODO:event_handler : FileSystemEventhandler,
    event_handler = DownloadsCleanEventHandler(watch_path)
    # recursive=True watch the whole directory  
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(2)
            print('observe')
    except KeyboardInterrupt:
        observer.stop()
    # This blocks the calling thread until the thread whose join() method is called terminates – either normally or through an unhandled exception or until the optional timeout occurs.
    observer.join()
