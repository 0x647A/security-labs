import os
from pathlib import Path


def get_extensions_os_walk(base_path):
    extension = set()
    for _, _, filenames in os.walk(base_path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext:
                extension.add(ext.lower())
    return sorted(extension)

base_path = Path("/your/path")

if not base_path.exists():
    print(f"The path '{base_path}' does not exist.")
else:
    extensions = get_extensions_os_walk(base_path)
    print("Unique file extensions found:")
    for ext in extensions:
        print(ext)
        