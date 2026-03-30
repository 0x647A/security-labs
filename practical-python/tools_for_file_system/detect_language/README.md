# Programming Language Detection Script

This script detects the programming language of a given source code file using three different methods:
1. **Pygments Lexer Guessing** — utilizes the `pygments` library to analyze the file content and guess the language.
2. **Regex Pattern Matching** — searches for language-specific patterns in the file lines using regular expressions.
3. **Keyword Matching** — scans the file content for specific keywords commonly found in certain languages.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Function Descriptions](#function-descriptions)
- [Sample Output](#sample-output)
- [Notes](#notes)

## Description

The script provides three approaches to detect the programming language of a given file:

- **Pygments Lexer Guessing** leverages a comprehensive lexer database to guess the most likely language from the source text.
- **Regex Pattern Matching** checks each line against a set of regexes that identify typical language constructs for Python, C/C++, PHP, and HTML.
- **Keyword Matching** looks for specific keywords/phrases typical to those languages anywhere in the file.

Each method prints out which languages it detects or indicates if detection failed.

## Requirements

- Python 3.6+
- `pygments` library  
  Install with:
  
```bash
pip install pygments
```

## Usage

1. **Set the target file:**
 Edit the target filename at the bottom of the respective script, for example:

```python
detect_language_with_pygments("your_file.py")
detect_language_by_regex("your_file.py")
detect_language_by_keyword("your_file.py")
```

2. **Run each script separately:**

```bash
python3 detect_language_with_pygments.py
python3 detect_language_by_regex.py
python3 detect_language_by_keywords.py
```

## Function Descriptions

- **detect_language_with_pygments(file_path)**  
Reads the file content and uses `pygments.lexers.guess_lexer` to try to identify the language. If it cannot determine, prints a failure message.

- **detect_language_by_regex(file_path)**  
Uses predefined regex patterns to search for language-specific constructs line by line. Prints all languages for which patterns were matched.

- **detect_language_by_keyword(file_path)**  
Reads the entire file content and checks if any known keywords/delimiters unique to certain languages appear. Prints all detected languages.

## Sample Output

```bash
Detected (pygments): Python
Detected (regex): Python
Detected: Python
```

If a method cannot detect the language, it will print a message accordingly or print no detected language.

## Notes

- The detection methods complement each other; some languages might be detected more reliably by one method than others.
- The regex and keyword sets are limited and can be extended to cover more languages or more patterns.
- For accurate results with Pygments, ensure the source file encoding is UTF-8 and the content resembles a known language.
- The script currently detects Python, C/C++, PHP, and HTML — feel free to expand regex/keyword dictionaries as needed.
