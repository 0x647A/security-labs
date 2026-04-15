import re


def detect_language_by_regex(file_path):
    regex_patterns = {
        "Python": [r"^\s*from\s+\w+", r"^\s*for\s+\w+\s+in\s+", r".*:\s*$"],
        "C/C++": [r"^\s*#include\s+<.*>", r"^\s*#define\s+\w+", r"^\s*(int|void|char)\s+\w+\s*\(.*\)"],
        "PHP": [r"<\?php", r"^\s*echo\s+.*;", r"\$\w+\s*="],
        "HTML": [r"<html.*?>", r"<body.*?>", r"<div.*?>"]
    }

    detected_languages = set()

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        for language, patterns in regex_patterns.items():
            if any(re.match(pattern, line) for pattern in patterns):
                detected_languages.add(language)

    for lang in detected_languages:
        print(f"Detected (regex): {lang}")

if __name__ == "__main__":
    detect_language_by_regex("compare_dir_scans.py")
