import os
import sys
import pathlib
import html
from datetime import datetime

EXTENSION_LANG_MAP = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.cpp': 'C++',
    '.c': 'C',
    '.cs': 'C#',
    '.html': 'HTML',
    '.rs': 'Rust'
}

PATH_DIR = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

def list_source_files(directory):
    result = []
    for path in pathlib.Path(directory).rglob("*"):
        if path.suffix in EXTENSION_LANG_MAP:
            result.append(path)
    return result

def count_non_empty_lines(filepath):
    with open(filepath, 'r', encoding="utf-8", errors="ignore") as f:
        return sum(1 for line in f if line.strip())
    
def generate_html_report(file_info_list):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>H4CK3R R3P0RT</title>
    <style>
        body {{
            background-color: #000000;
            color: #00FF00;
            font-family: "Courier New", Courier, monospace;
            padding: 20px;
        }}
        h1 {{
            text-shadow: 0 0 5px #00FF00;
            font-size: 32px;
            border-bottom: 2px solid #00FF00;
            padding-bottom: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #00FF00;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #002200;
        }}
        tr:nth-child(even) {{
            background-color: #001100;
        }}
        tr:hover {{
            background-color: #003300;
        }}
        footer {{
            margin-top: 40px;
            font-size: 0.8em;
            color: #00FF00;
        }}
    </style>
</head>
<body>
    <h1>💻 H4CK3R C0D3 R3P0RT 💀</h1>
    <table>
        <tr><th>🗂️ File</th><th>💬 Language</th><th>📏 Lines of Code</th></tr>
"""
    for filepath, lang, line_count in file_info_list:
        html_content += f"<tr><td>{html.escape(filepath)}</td><td>{html.escape(lang)}</td><td>{line_count}</td></tr>\n"

    html_content += f"""    </table>
    <footer>
        Report generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </footer>
</body>
</html>"""
    return html_content


def main():
    print(f"Scanning directory: {PATH_DIR}")
    source_files = list_source_files(PATH_DIR)
    file_info = []

    for path in source_files:
        lang = EXTENSION_LANG_MAP.get(path.suffix, "Unknown")
        line_count = count_non_empty_lines(path)
        file_info.append((str(path.relative_to(PATH_DIR)), lang, line_count))

    print("Generating HTML report...")
    html_report = generate_html_report(file_info)

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html_report)

    print("Report saved as report.html")

if __name__ == "__main__":
    main()