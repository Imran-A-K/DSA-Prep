# python_dsa — Local DSA Practice (Python + Pytest)

This repo is a local-first DSA practice environment:
- Write solutions in `src/`
- Write tests in `tests/`
- Run any test file against any implementation file (brute-force or optimized)

Your workflow stays consistent across topics (arrays, recursion, stacks, linked lists, etc.).

---

## Repo Structure (current)

python_dsa/
Setup/
setup_mac.sh
setup_windows.ps1
setup_windows.bat

src/
arrays/
monotonic_array/
sorted_squares/
recursion/
Josephus_problem/

tests/
arrays/
recursion/
Josephus_problem/
_loader.py   (shared helper for dynamic imports)

run.py
requirements.txt
.gitignore

Notes:
- Python will create `__pycache__/` folders automatically (normal). `.gitignore` excludes them.
- Pytest will create `.pytest_cache/` (normal). `.gitignore` excludes it.

---

## Prerequisites

- Python 3.10+ recommended (3.11+ great)
- Git (optional)
- On Windows: PowerShell and/or CMD

---

## Setup (macOS / Linux)

From the repo root:

  1) Run setup script
```bash
   chmod +x Setup/setup_mac.sh
   Setup/setup_mac.sh

  2.	Activate the virtual environment
        source .venv/bin/activate

  3.	Verify pytest is installed
        python -m pytest --version

  Deactivate when done:
        deactivate

Setup (Windows)

PowerShell (recommended)
	1.	If activation is blocked, run once:
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
	2.	Run setup:
    .\Setup\setup_windows.ps1
	3.	Activate venv:
    .\.venv\Scripts\Activate.ps1
    CMD (alternative)
    Setup\setup_windows.bat
    Activate later:
    .\.venv\Scripts\activate.bat

Where to write solutions

Put solutions under src/, organized however you like:

Examples:
	•	src/arrays/sorted_squares/sorted_squares.py
	•	src/arrays/sorted_squares/sorted_array_bf.py
	•	src/recursion/kth_grammar.py
	•	src/Josephus_problem/find_winner.py
Where to write tests

Put tests under tests/ :

Examples:
	•	tests/arrays/test_sorted_squares.py
	•	tests/arrays/test_is_monotonic.py
	•	tests/recursion/test_kth_grammar.py
	•	tests/Josephus_problem/test_find_winner.py

Running tests (the core workflow)

This repo uses run.py to run:
	•	one test file
	•	against one solution file

Syntax
    python run.py <test_file.py> <solution_file.py> [-q|-v ...]

Examples:
    python run.py test_sorted_squares.py sorted_array_bf.py -q
    python run.py test_sorted_squares.py sorted_squares.py -q

The same test file can validate both the brute-force and optimized implementation.
Important rule

Your test file loads a function by name (e.g., sorted_squares).
Therefore, BOTH brute-force and optimized solution files must export the SAME function name:

def sorted_squares(nums):
    ...

    If the function name does not match, you’ll see an error like:
Module ... does not define function 'sorted_squares'.

# python_dsa — Local DSA Practice (Python + Pytest)

A local-first **Data Structures & Algorithms (DSA)** practice repository designed for fast, disciplined iteration.

Core ideas:
- Write solutions in `src/`
- Write test cases in `tests/`
- Run the **same test file** against different implementations (brute-force vs optimized)
- Keep logic, testing, and execution clearly separated

This structure mirrors real-world engineering workflows and scales naturally across topics (arrays, recursion, stacks, linked lists, etc.).

---

## Repository Structure

```
python_dsa/
├── Setup/
│   ├── setup_mac.sh
│   ├── setup_windows.ps1
│   └── setup_windows.bat
├── src/
│   ├── arrays/
│   │   ├── monotonic_array/
│   │   └── sorted_squares/
│   ├── recursion/
│   └── Josephus_problem/
├── tests/
│   ├── arrays/
│   ├── recursion/
│   ├── Josephus_problem/
│   └── _loader.py
├── run.py
├── requirements.txt
└── .gitignore
```

### Notes
- `__pycache__/` directories are created automatically by Python (normal behavior).
- `.pytest_cache/` is created automatically by pytest.
- Both are excluded via `.gitignore`.

---

## Prerequisites

- Python **3.10+** (3.11+ recommended)
- Git (optional, for version control)

### Windows users
- PowerShell or CMD
- You may need to allow script execution for virtual environments (see below).

---

## Setup Instructions

### macOS / Linux

From the repository root:

1. Make the setup script executable (first time only):
```bash
chmod +x Setup/setup_mac.sh
```

2. Run the setup script:
```bash
bash Setup/setup_mac.sh
```

3. Activate the virtual environment:
```bash
source .venv/bin/activate
```

4. Verify installation:
```bash
python -m pytest --version
```

Deactivate when finished:
```bash
deactivate
```

---

### Windows (PowerShell – recommended)

If activation is blocked, run **once**:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Run setup:
```powershell
.\Setup\setup_windows.ps1
```

Activate the virtual environment:
```powershell
.\.venv\Scripts\Activate.ps1
```

Deactivate:
```powershell
deactivate
```

---

### Windows (CMD – alternative)

Run setup:
```bat
Setup\setup_windows.bat
```

Activate later:
```bat
.\.venv\Scripts\activate.bat
```

Deactivate:
```bat
deactivate
```

---

## Writing Solutions

All solution implementations live under `src/`, organized by topic.

Examples:
- `src/arrays/sorted_squares/sorted_squares.py`
- `src/arrays/sorted_squares/sorted_array_bf.py`
- `src/recursion/kth_grammar.py`
- `src/Josephus_problem/find_winner.py`

You may keep **multiple implementations** (e.g., brute-force and optimized) for the same problem.

---

## Writing Tests

All test files live under `tests/`, also organized by topic.

Examples:
- `tests/arrays/test_sorted_squares.py`
- `tests/arrays/test_is_monotonic.py`
- `tests/recursion/test_kth_grammar.py`
- `tests/Josephus_problem/test_find_winner.py`

Tests are written with **pytest** and dynamically load the target implementation.

---

## Running Tests (Core Workflow)

Tests are executed using `run.py`, which allows running:

- one test file
- against one chosen solution file

### Command syntax
```bash
python run.py <test_file.py> <solution_file.py> [-q | -v ...]
```

### Examples

Run brute-force implementation:
```bash
python run.py test_sorted_squares.py sorted_array_bf.py -q
```

Run optimized implementation:
```bash
python run.py test_sorted_squares.py sorted_squares.py -q
```

The **same test file** can be reused to validate different implementations.

---

## Function Name Contract (Important)

Tests dynamically load a function by name using `tests/_loader.py`.

This means **all implementations for the same problem must export the same function name** expected by the tests.

Example:
```python
def sorted_squares(nums):
    ...
```

If the function name does not match, you will see an error like:
```
Module '...' does not define function 'sorted_squares'
```

This contract keeps tests reusable and enforces consistency.

---

## Common Issues

### `__pycache__` or `.pytest_cache` folders appear
This is normal Python/pytest behavior. These directories are ignored by Git.

### Virtual environment activation fails on Windows
Ensure you have run:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## License

This repository is intended for **personal learning and practice**.