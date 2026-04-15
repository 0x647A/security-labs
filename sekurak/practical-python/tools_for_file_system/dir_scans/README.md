# Comparison of File/Directory Listing Methods in Python

This script is designed to compare three methods of recursively listing all files and directories in a chosen folder, while measuring the execution time and peak memory usage of each method.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)
- [Sample Output](#sample-output)
- [Notes](#notes)

## Description

The script compares three methods that return a list of paths to all files and directories inside a specified folder:
1. Using `os.walk`
2. Using `Path.rglob` from the `pathlib` library
3. Manual recursion using `os.listdir`

For each method, the script measures execution time and peak memory usage. It also compares results to indicate any differences in the listed files.

## Requirements

- Python 3.6+
- No additional libraries required (only uses standard library modules)

## Usage

1. **Edit the base path:**

   Set the `base_path` variable in the code to your target folder, for example:
   ```python
   base_path = Path("/path/to/your/folder")
   ```

2. **Run the script:**
    ```bash
    python3 compare_dir_scans.py
    ```

## Function Descriptions

- **measure(function, *args)**
Measures execution time and peak memory usage while running the given function.

- **list_with_os_walk(base_path)**  
Returns a sorted list of all files and folders using `os.walk`.

- **list_with_rglob(base_path)**  
Returns a sorted list of all files and folders using recursive search with `Path.rglob('*')`.

- **list_manual_recursive(base_path)**
Implements manual iterative traversal using `os.listdir` and a stack.

## Sample Output

``` bash
OS.WALK
Execution time: 0.0123 seconds
Peak memory usage: 155.00 KB
RGLOB
Execution time: 0.0101 seconds
Peak memory usage: 120.00 KB
MANUAL
Execution time: 0.0250 seconds
Peak memory usage: 180.00 KB
RESULT COMPARISON:
os.walk == rglob: True
os.walk == manual: True
rglob == manual: True
```

If there are any differences between the results, the script will print the differences between the methods.

## Notes

- The base path (`base_path`) must exist on disk and be correct (the script will exit with an error if the folder does not exist).
- Performance and memory usage results depend on the number of files and the folder structure.
