import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"Created: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"Deleted: {event.src_path}")

if __name__ == "__main__":
    path = "/your/path"
    observer = Observer()
    observer.schedule(MyHandler(), path=path, recursive=True)
    observer.start()
    print(f"Monitoring changes in directory: {Path(path).resolve()}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()