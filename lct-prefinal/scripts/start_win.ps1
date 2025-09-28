$TwinDir = Resolve-Path ".\LCT_win64" -ErrorAction SilentlyContinue


if (-not $TwinDir) {
    Write-Host "Error: Digital Twin directory 'LCT_win64' not found." -ForegroundColor Red
    Write-Host "Please download and extract the Digital Twin archive for Windows."
    Write-Host "The 'LCT_win64' folder should be located next to the project directory."
    exit 1
}

Start-Process -FilePath (Join-Path $TwinDir.Path "twin.exe") -WorkingDirectory $TwinDir.Path
Write-Host "Digital Twin launched from '$($TwinDir.Path)'."

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd lct-ats; uv run launcher.py --twin"

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd lct-client; uv run jupyter notebook"

Write-Host "ATS and Client launched."
