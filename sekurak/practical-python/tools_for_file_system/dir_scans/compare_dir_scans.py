import os
import sys
import time
import tracemalloc
from pathlib import Path


def measure(function, *args):
    tracemalloc.start()
    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        'result': result,
        'time': end_time - start_time,
        'memory': peak / 1024
    }

def list_with_os_walk(base_path):
    result = []
    for dirpath, dirname, filename in os.walk(base_path):
        for name in dirname + filename:
            full_path = os.path.join(dirpath, name)
            result.append(os.path.abspath(full_path))
    return sorted(result)

def list_with_rglob(base_path):
    result = [str(p.resolve()) for p in Path(base_path).rglob('*')]
    return sorted(result)

def list_manual_recursive(base_path):
    result = []
    stack = [str(base_path)]
    while stack:
        current = stack.pop()
        for entry in os.listdir(current):
            full_path = os.path.join(current, entry)
            result.append(os.path.abspath(full_path))
            if os.path.isdir(full_path):
                stack.append(full_path)
    return sorted(result)

if __name__ == "__main__":
    base_path = Path("/your/path")

    if not base_path.exists():
        print(f"The path '{base_path}' does not exist.")
        sys.exit(1)

    results = {
        "os.walk": measure(list_with_os_walk, base_path),
        "rglob": measure(list_with_rglob, base_path),
        "manual": measure(list_manual_recursive, base_path)
    }

    for name, data in results.items():
        print(f"\n{name.upper()}")
        print(f"Execution time: {data['time']:.4f} seconds")
        print(f"Peak memory usage: {data['memory']:.2f} KB")

    a, b, c = results["os.walk"]["result"], results["rglob"]["result"], results["manual"]["result"]

    print("\nRESULT COMPARISON:")
    print("os.walk == rglob:", a == b)
    print("os.walk == manual:", a == c)
    print("rglob == manual:", b == c)

    if a != b:
        print("\nDifferences between os.walk and rglob:")
        print(set(a) - set(b))
        print(set(b) - set(a))

    if a != c:
        print("\nDifferences between os.walk and manual:")
        print(set(a) - set(c))
        print(set(c) - set(a))

    if b != c:
        print("\nDifferences between rglob and manual:")
        print(set(b) - set(c))
        print(set(c) - set(b))
