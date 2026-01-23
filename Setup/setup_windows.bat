@echo off
setlocal

echo == python_dsa setup (Windows .bat) ==

REM Move to repo root (parent of Setup/)
cd /d "%~dp0.."

echo Repo root: %CD%

REM Standardize on .venv
if exist venv if not exist .venv (
  echo WARNING: Found 'venv\' but not '.venv\'. Repo standard is '.venv\'.
  echo          (You can delete 'venv\' later if you want.)
)

REM Create venv
if not exist .venv (
  echo Creating virtual environment in .venv ...
  py -3 -m venv .venv
) else (
  echo .venv already exists. Skipping creation.
)

REM Activate venv (cmd)
call .venv\Scripts\activate.bat

echo Upgrading pip and installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Done.
echo Activate later (cmd): .venv\Scripts\activate.bat
echo Run tests:            python run.py ^<test_file.py^> ^<solution_file.py^> -q

endlocal