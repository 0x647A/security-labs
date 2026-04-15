import os
import json
from datetime import datetime
from pathlib import Path


SOURCE_FOLDER = "/your/path"
HISTORY_FILE = Path(__file__).parent / "progress.json"
EXTENSIONS = [".py"]

def is_code_line(line):
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")

def count_lines_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for line in f if is_code_line(line))
    
def count_total_lines(folder):
    total = 0
    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                full_path = os.path.join(root, file)
                total += count_lines_in_file(full_path)
    return total

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def show_progress(history):
    if len(history) < 2:
        print("Not enough data to analyze progress.")
        return 
    latest = history[-1]
    previous = history[-2]
    diff = latest["line_count"] - previous["line_count"]
    print(f"\nProgress since last check: {diff:+} lines of code")

def main():
    print("🔍 Counting lines of code...")
    current_lines = count_total_lines(SOURCE_FOLDER)
    print(f"Total: {current_lines} lines of code in '{SOURCE_FOLDER}'.")

    history = load_history()
    history.append({
        "timestamp": datetime.now().isoformat(),
        "line_count": current_lines
    })

    save_history(history)
    show_progress(history)

if __name__ == "__main__":
    main()
