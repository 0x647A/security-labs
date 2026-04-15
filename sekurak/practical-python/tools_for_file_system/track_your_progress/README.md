# Python Code Line Counter with Progress Tracking

This Python script counts the number of actual lines of code in Python source files (`.py`) within a specified directory (including subdirectories). It excludes blank lines and comment lines. The script also maintains a history of counts in a JSON file and shows progress (change in line count) between subsequent runs.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)
- [Sample Output](#sample-output)
- [Notes](#notes)

## Description

The script performs these tasks:

- Recursively walks through a source folder and counts lines of code in `.py` files.
- Counts only non-empty lines that do not start with `#`.
- Stores historical counts in a JSON file (`progress.json`).
- On each run, compares current count with previous count and prints the difference (progress).

This is useful for tracking the growth or reduction of Python code in a project over time.

## Requirements

- Python 3.6 or newer
- No third-party dependencies (uses only standard libraries: `os`, `json`, `datetime`)

## Usage

1. **Set the source folder and optional extensions:**

    Modify the `SOURCE_FOLDER` variable to point to your Python project directory.  
    You can adjust the `EXTENSIONS` list to include other file extensions if desired (e.g., `.pyw`).

    ```python
    SOURCE_FOLDER = "/path/to/your/python/project"
    EXTENSIONS = [".py"]
    ```

2. **Run the script:**

    ```bash
    python3 tracker.py
    ```

3. The script outputs the current total lines of code and progress since last check.

4. Progress history is saved in `progress.json` in the script's directory.

## Function Descriptions

- `is_code_line(line)`
Returns `True` if a line is not empty and does not start with a comment (`#`).

- `count_lines_in_file(filepath)` 
Counts code lines in a given file based on `is_code_line`.

- `count_total_lines(folder)` 
Recursively counts code lines in all files under `folder` matching extensions in `EXTENSIONS`.

- `load_history()`
Loads the progress history from the JSON file (`progress.json`). Returns an empty list if the file does not exist yet.

- `save_history(history)`  
Saves the given history list into the JSON file with pretty formatting.

- `show_progress(history)`
If there are at least two entries, calculates and prints the difference in line counts between the last two runs.

- `main()` 
Orchestrates the counting, loading and saving of history, and progress reporting.

## Sample Output

```bash
🔍 Counting lines of code...
Total: 3245 lines of code in '/your/path'.
Progress since last check: +35 lines of code
```

If it is the first run or not enough history exists, the script will print:

```bash
Not enough data to analyze progress.
```

## Notes

- The script only counts lines in files matching extensions listed in `EXTENSIONS`.
- Lines starting with whitespace followed by `#` are considered comments and excluded.
- Blank lines are excluded.
- The JSON history file accumulates one entry per run with timestamp and line count.
- You can automate running this script periodically (e.g., using cron) to track code growth over time.
