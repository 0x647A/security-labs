# Collect Unique File Extensions in a Directory using Python

This script recursively scans a given directory and collects all unique file extensions found in its files. It uses `os.walk` from the standard library to traverse the directory structure.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Function Description](#function-description)
- [Sample Output](#sample-output)
- [Notes](#notes)

## Description

The script traverses all files in the specified base directory (recursively) and extracts file extensions (the suffix after the last dot in filenames). It gathers all unique extensions found and prints them sorted in alphabetical order.

## Requirements

- Python 3.6+
- Only uses standard library modules (`os`, `pathlib`)

## Usage

1. **Set the base path:**

   Modify the `base_path` variable in the script to point to the directory you want to scan, for example:

   ```python
   base_path = Path("/path/to/your/directory")
   ```

2. **Run the script:**

   ```bash
   python3 list_file_extension.py
   ```

## Function Description

- `get_extensions_os_walk(base_path)`

Takes a base directory path and recursively traverses all files under it using `os.walk`. Collects unique file extensions (case-insensitive) present among the files. Returns a sorted list of extensions (strings starting with a dot).

- `base_path` (`Path` or string): Directory to scan.
- **Returns:** Sorted list of unique file extensions found (e.g., `['.py', '.txt', '.md']`).

## Sample Output

```bash
Unique file extensions found:
.py
.md
.txt
.csv
```

If the base path does not exist, the script will print an error message.

## Notes

- Files without extensions are ignored.
- Extensions are normalized to lowercase.
- This script does not follow symbolic links specially; it behaves according to `os.walk` defaults.
- Useful for understanding what kinds of files are in a directory tree.
