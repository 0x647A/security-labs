def detect_language_by_keyword(file_path):
    keywords = {
        "C/C++": ["#include", "#define"],
        "PHP": ["<?php"],
        "Python": ["def ", "import "],
        "HTML": ["<html", "<body", "<div"]
    }

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    detected_language = set()

    for language, words in keywords.items():
        if any(word in content for word in words):
            detected_language.add(language)

    for lang in detected_language:
        print(f"Detected: {lang}")

if __name__ == "__main__":
    detect_language_by_keyword("compare_dir_scans.py")
