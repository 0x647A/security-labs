# Count Code Lines in a Python File

This script counts the number of actual code lines in a specified Python file, ignoring blank lines and comment lines. It's useful for quickly measuring the size of scripts in terms of meaningful code.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Function Description](#function-description)
- [Sample Output](#sample-output)
- [Notes](#notes)

## Description

The script reads a Python source file and counts the lines that represent actual code, excluding empty lines and lines starting with the comment character (`#`). This helps to determine how many lines of real code (logic) exist in the file.

## Requirements

- Python 3.6 or newer

## Usage

1. **Set the `file` variable:**

   In the script, set the `file` variable to the path of the file you want to analyze, for example:
    ```python
    file = "your_script.py"
    ```

2. **Run the script:**

    ```bash
    python3 count_code_lines.py
    ```
(Replace `count_code_lines.py` with the actual filename, if different.)

## Function Description

- **count_code_lines(filename)**

Reads the given file and counts the number of non-empty, non-comment lines.

- `filename` (str): Path to the Python file.
- **Returns:** Number of actual code lines (int).

## Sample Output

```bash
Number of code lines in compare_dir_scans.py: 49
```

## Notes

- Only top-level comment lines (starting with `#`) are skipped. Inline comments or multiline strings will be counted as code.
- Make sure the `file` variable is set to the correct path and the file exists.
- Useful for simple code metrics and codebase analysis.
