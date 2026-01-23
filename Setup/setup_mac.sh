#!/usr/bin/env bash
set -euo pipefail

echo "== python_dsa setup (macOS/Linux) =="

# Move to repo root (parent of Setup/)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

echo "Repo root: $REPO_ROOT"

# Prefer python3 if available
PY_BIN="python3"
command -v python3 >/dev/null 2>&1 || PY_BIN="python"

echo "Using Python: $($PY_BIN --version)"

# Standardize on .venv
if [ -d "venv" ] && [ ! -d ".venv" ]; then
  echo "⚠️ Found 'venv/' but not '.venv/'. This repo standard is '.venv/'."
  echo "   (You can delete 'venv/' later if you want.)"
fi

if [ ! -d ".venv" ]; then
  echo "Creating virtual environment in .venv/ ..."
  $PY_BIN -m venv .venv
else
  echo ".venv/ already exists. Skipping creation."
fi

echo "Installing dependencies..."
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Done."
echo "Activate venv: source .venv/bin/activate"
echo "Run tests:     python run.py <test_file.py> <solution_file.py> -q"