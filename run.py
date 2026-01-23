#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def find_solution_file(src_dir: Path, filename: str) -> Path:
    # If user passes a path like src/arrays/x.py, respect it
    candidate = (Path(filename) if Path(filename).is_absolute() else (src_dir.parent / filename)).resolve()
    if candidate.exists() and candidate.suffix == ".py":
        return candidate

    # Otherwise search inside src/ for the filename
    matches = list(src_dir.rglob(filename))
    matches = [m for m in matches if m.is_file() and m.suffix == ".py"]

    if len(matches) == 0:
        raise FileNotFoundError(f"Could not find solution file '{filename}' under {src_dir}")
    if len(matches) > 1:
        msg = "\n".join(str(m) for m in matches[:10])
        raise RuntimeError(f"Multiple matches for '{filename}'. Be specific:\n{msg}")
    return matches[0]

def to_module_dotted(project_root: Path, py_file: Path) -> str:
    # Convert /.../python_dsa/src/arrays/sorted_squares.py -> src.arrays.sorted_squares
    rel = py_file.resolve().relative_to(project_root.resolve())
    parts = list(rel.parts)
    if parts[-1].endswith(".py"):
        parts[-1] = parts[-1][:-3]
    return ".".join(parts)

def main():
    root = Path(__file__).resolve().parent
    tests_dir = root / "tests"
    src_dir = root / "src"

    if not tests_dir.exists():
        print("[ERROR] tests/ folder not found. Create it with: mkdir -p tests")
        return 1
    if not src_dir.exists():
        print("[ERROR] src/ folder not found.")
        return 1

    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage:")
        print("  python run.py <test_file.py> <solution_file.py> [-q|-v ...]")
        print("Examples:")
        print("  python run.py test_sorted_squares.py sorted_squares_bruteforce.py -q")
        print("  python run.py test_sorted_squares.py sorted_squares.py -q")
        return 1

    test_file = args[0]
    sol_file = args[1]
    extra_pytest_args = args[2:]  # e.g., -q, -v, -k ...

    
    # Allow passing test name without path; search recursively under tests/
    matches = list(tests_dir.rglob(test_file))
    if not matches:
        print(f"[ERROR] Test file not found under tests/: {test_file}")
        return 1
    if len(matches) > 1:
        print(f"[ERROR] Multiple test files found for {test_file}:")
        for m in matches:
            print(" ", m)
        return 1

    test_path = matches[0]
    if not test_path.exists():
        # allow passing "tests/test_x.py" too
        alt = (root / test_file)
        if alt.exists():
            test_path = alt
        else:
            print(f"[ERROR] Test file not found: {test_path}")
            return 1

    try:
        sol_path = find_solution_file(src_dir, sol_file)
    except Exception as e:
        print(f"[ERROR] {e}")
        return 1

    # Default to quiet unless user specifies -q/-v themselves
    base = ["python", "-m", "pytest"]
    if not any(a in extra_pytest_args for a in ["-q", "-v", "-vv"]):
        base.append("-q")

    # Pass module name via environment variable
    env = os.environ.copy()
    env["DSA_SOLUTION_MODULE"] = to_module_dotted(root, sol_path)

    cmd = base + [str(test_path)] + extra_pytest_args
    return subprocess.call(cmd, env=env)

if __name__ == "__main__":
    raise SystemExit(main())