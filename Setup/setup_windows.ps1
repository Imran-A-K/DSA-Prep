Write-Host "== python_dsa setup (Windows PowerShell) =="

# Move to repo root (parent of Setup/)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..")
Set-Location $RepoRoot

Write-Host "Repo root: $RepoRoot"

# Prefer py launcher if available
$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    $UsePyLauncher = $true
    Write-Host "Using Python: py -3"
    & py -3 --version
} else {
    $UsePyLauncher = $false
    Write-Host "Using Python: python"
    & python --version
}

# Standardize on .venv
if ((Test-Path ".\venv") -and !(Test-Path ".\.venv")) {
    Write-Host "WARNING: Found 'venv\' but not '.venv\'. Repo standard is '.venv\'."
    Write-Host "         (You can delete 'venv\' later if you want.)"
}

if (!(Test-Path ".\.venv")) {
    Write-Host "Creating virtual environment in .venv\ ..."
    if ($UsePyLauncher) {
        & py -3 -m venv .venv
    } else {
        & python -m venv .venv
    }
} else {
    Write-Host ".venv\ already exists. Skipping creation."
}

Write-Host "Activating venv..."
& .\.venv\Scripts\Activate.ps1

Write-Host "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host ""
Write-Host "Done."
Write-Host "Activate later (PowerShell): .\.venv\Scripts\Activate.ps1"
Write-Host "Run tests:                  python run.py <test_file.py> <solution_file.py> -q"