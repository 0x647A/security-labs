def count_code_lines(filename):
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if stripped == "":
                continue
            if stripped.startswith("#"):
                continue
            count += 1
    return count

if __name__ == "__main__":
    file = "../dir_scans/compare_dir_scans.py"
    print(f"Number of code lines in {file}:", count_code_lines(file))
