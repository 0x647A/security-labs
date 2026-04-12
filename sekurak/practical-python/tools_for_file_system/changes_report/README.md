# Source Code Line Count and HTML Report Generator

This Python script recursively scans a specified directory for source code files based on their file extensions, counts the number of non-empty lines in each file, and generates a visually styled HTML report summarizing the results.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)
- [Report Styling](#report-styling)
- [Notes](#notes)

## Description

The script performs the following:

- Scans the specified directory (and subdirectories) for files with particular programming language extensions.
- Counts non-empty lines in each source file (ignoring blank lines).
- Maps file extensions to programming languages.
- Generates an HTML report listing each file, its detected language, and count of lines of code.
- The report is styled with a hacker-themed green-on-black design.

## Requirements

- Python 3.6 or newer
- No external libraries required (uses only standard libraries: `os`, `pathlib`, `datetime`, `collections`)

## Usage

1. **Set the directory to scan:**

   Modify the `PATH_DIR` variable in the script to your target directory, for example:

    ```python
    PATH_DIR = "/path/to/your/source/code"
    ```

2. **Run the script:**

```bash
python3 html_report_which_list_sources.py
```

3. After running, the script creates `report.html` in the current directory.

4. Open `report.html` in any web browser to view the report.

## Function Descriptions

- `list_source_files(directory)`
Recursively lists all files within `directory` that have extensions defined in `EXTENSION_LANG_MAP`. Returns a list of `Path` objects.

- `count_non_empty_lines(filepath)`
Counts lines in `filepath` that are not empty or whitespace-only.

- `generate_html_report(file_info_list)` 
Takes a list of tuples `(file_path_str, language, line_count)` and produces a complete HTML document as a string with stylized table and footer.

- `main()`
Orchestrates scanning, counting, generating the report, and saving it to `report.html`.

## Report Styling

- Color scheme: classic hacker/terminal green text on black background.
- Font: monospace (Courier New or similar).
- Table with alternating row colors and hover effect for readability.
- Header with a styled title including emoji.
- Footer displays the report generation timestamp.

## Notes

- Files without a recognized extension in `EXTENSION_LANG_MAP` are ignored.
- Line counts exclude empty lines but count all others, including comments and whitespace-containing lines.
- The HTML report filename is fixed as `report.html` in the current working directory.
- Modify `EXTENSION_LANG_MAP` dictionary to add support for more file types/languages if needed.