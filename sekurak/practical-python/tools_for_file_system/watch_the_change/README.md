# Directory Change Monitoring Scripts in Python

This repository contains two Python scripts for monitoring file changes in a specified directory. They demonstrate two approaches:

1. **Manual Polling**: Periodically scanning the directory and checking for modified files by comparing file modification times.
2. **Event-Driven Monitoring**: Using the `watchdog` library to listen for filesystem events such as creation, modification, and deletion of files.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Notes](#notes)

## Description

Monitoring filesystem changes is often needed for automation, synchronization, or auditing tasks. This repository provides two example scripts for watching changes inside a specified directory:

- The **Manual Polling** script periodically walks through the directory tree and detects files that have been added or modified since the last scan based on their last modified timestamp (`mtime`).

- The **Watchdog Event Handler** script uses Python’s `watchdog` library, which watches the directory for filesystem events emitted by the operating system and reacts instantly to file creation, modification, or deletion.

Both approaches print the paths of changed files to the console.

## Requirements

- Python 3.6+
- For the event-driven script, install the `watchdog` library:

  ```bash
  pip install watchdog
  ```

- Both scripts rely on standard libraries such as `os`, `time`, and `pathlib`.

## Setup

1. **Set the directory to monitor:**

    In both scripts, modify the path variable (`DIR_TO_WATCH` or `path`) to the directory you want to watch. For example:

    ```python
    DIR_TO_WATCH = Path("/path/to/your/directory")
    ```
    or
    ```python
    path = "/path/to/your/directory"
    ```

The two scripts are:

- `active_polling.py` — manual polling script
- `watchdog_monitor.py` — event-driven script

## Usage

Run each script separately in the terminal:

```bash
python3 active_polling.py
```
or
```bash
python3 watchdog_monitor.py
```
Press `Ctrl+C` to stop the observer-based script gracefully.

## Scripts Overview

### Manual Polling Script

- Uses `os.walk` to recursively scan the directory tree.
- Compares last modification times (`mtime`) to track changes.
- Maintains a cache dictionary where keys are file paths and values are last known `mtime`.
- Prints the paths of any modified or newly detected files each scan cycle.
- Pauses 1 second between scans to limit CPU usage.

### Event-Driven Script (watchdog_monitor.py)

- Uses `watchdog.observers.Observer` to watch the directory.
- Registers a `FileSystemEventHandler` subclass (`MyHandler`) to respond to:
  - `on_created` events — prints when files are created.
  - `on_modified` events — prints when files are modified.
  - `on_deleted` events — prints when files are deleted.
- Monitors recursively in all subdirectories.
- Runs indefinitely until interrupted (e.g., with Ctrl+C).

## Notes

- The manual polling method introduces a delay (poll interval) and may miss very rapid changes that occur between scans.
- The watchdog method provides near-instant notifications but requires a third-party package and OS event support.
- Choose the approach based on your requirements for precision, dependencies, and event latency.
- Both scripts monitor files only; directory events themselves are ignored unless a file inside is affected.
- Handle exceptions or file access permissions in a production scenario for robustness.
