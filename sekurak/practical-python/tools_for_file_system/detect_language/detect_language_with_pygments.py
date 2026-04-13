from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound


def detect_language_with_pygments(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        lexer = guess_lexer(content)
        print(f"Detected (pygments): {lexer.name}")
    except ClassNotFound:
        print("Could not determine language with pygments")

if __name__ == "__main__":
    detect_language_with_pygments("compare_dir_scans.py")
