# Python File System Tools

A collection of Python scripts written for learning purposes, covering exploring, analysing, and monitoring the local filesystem. Each module explores a different filesystem problem and compares multiple implementation approaches where applicable.

Python 3.6+ required. All modules except `detect_language` and `watch_the_change` use the standard library only.

## Repository Structure

```
.
├── changes_report/       # Scan a directory and generate an HTML report of source file line counts
├── count_lines/          # Count actual code lines in a single Python file
├── detect_language/      # Detect the programming language of a source file (three methods)
├── dir_scans/            # Compare three directory-listing methods by speed and memory usage
├── extension/            # Collect all unique file extensions in a directory tree
├── track_your_progress/  # Track Python code line count over time with JSON history
└── watch_the_change/     # Monitor a directory for file changes (polling vs event-driven)
```

## Modules

### changes_report
Recursively scans a directory for source files, counts non-empty lines, and generates a styled HTML report.

| Script | Output |
|---|---|
| `html_report_which_list_sources.py` | `report.html` — terminal-themed green-on-black table |

```bash
# Set PATH_DIR inside the script, then:
python3 changes_report/html_report_which_list_sources.py
```

### count_lines
Counts meaningful lines of code in a Python file, excluding blank lines and comments.

```bash
# Set the `file` variable inside the script, then:
python3 count_lines/count_code_lines.py
```

### detect_language
Three independent approaches to detecting the programming language of a source file.

| Script | Method | External dependency |
|---|---|---|
| `detect_language_with_pygments.py` | Pygments lexer guessing | `pygments` |
| `detect_language_by_regex.py` | Regex pattern matching | None |
| `detect_language_by_keywords.py` | Keyword scanning | None |

```bash
pip install pygments
python3 detect_language/detect_language_with_pygments.py
python3 detect_language/detect_language_by_regex.py
python3 detect_language/detect_language_by_keywords.py
```

### dir_scans
Benchmarks three methods for recursively listing all files and directories, measuring execution time and peak memory usage.

| Function | Method |
|---|---|
| `list_with_os_walk` | `os.walk` |
| `list_with_rglob` | `Path.rglob('*')` |
| `list_manual_recursive` | `os.listdir` + stack |

```bash
# Set `base_path` inside the script, then:
python3 dir_scans/compare_dir_scans.py
```

### extension
Scans a directory tree and prints all unique file extensions found, sorted alphabetically.

```bash
# Set `base_path` inside the script, then:
python3 extension/list_file_extension.py
```

### track_your_progress
Counts code lines across an entire Python project and saves a timestamped history to `progress.json`. Shows growth or reduction between runs.

```bash
# Set SOURCE_FOLDER inside the script, then:
python3 track_your_progress/tracker.py
```

### watch_the_change
Two approaches to monitoring a directory for file additions, modifications, and deletions.

| Script | Approach | Latency | External dependency |
|---|---|---|---|
| `active_polling.py` | Periodic `mtime` scan (1 s interval) | ~1 s | None |
| `watchdog_monitor.py` | OS filesystem events via `watchdog` | Near-instant | `watchdog` |

```bash
pip install watchdog
python3 watch_the_change/active_polling.py
# or
python3 watch_the_change/watchdog_monitor.py
# Press Ctrl+C to stop
```

## Requirements

- Python 3.6+
- Standard library only, except:
  - `detect_language`: `pip install pygments`
  - `watch_the_change`: `pip install watchdog`
