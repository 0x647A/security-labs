import os
import time
from pathlib import Path

DIR_TO_WATCH = Path("/your/path")

cache = {}

def scan_directory(path):
    changed_files = []
    for root, _, files in os.walk(path):
        for filename in files:
            filepath = Path(root) / filename
            try:
                mtime = os.stat(filepath).st_mtime
                if filepath not in cache or cache[filepath] != mtime:
                    changed_files.append(filepath)
                    cache[filepath] = mtime
            except FileNotFoundError:
                continue
    return changed_files

if __name__ == "__main__":
    print(f"Monitoring changes in directory: {DIR_TO_WATCH.resolve()}")
    while True:
        changed = scan_directory(DIR_TO_WATCH)
        for path in changed:
            print(f"Modified: {path}")
        time.sleep(1)