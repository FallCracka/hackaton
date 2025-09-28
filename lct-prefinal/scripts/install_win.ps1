if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Git not found. Installing..."
    winget install --id Git.Git -e --source winget
} else {
    Write-Host "Git is already installed."
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "uv not found. Installing..."
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
} else {
    Write-Host "uv is already installed."
}

Write-Host "Cloning and configuring repositories..."

if (-not (Test-Path -Path "lct-prefinal")) {
    git clone https://gitflic.ru/project/lct-prefinal/lct-prefinal.git
} else {
    Write-Host "Directory lct-prefinal already exists. Skipping cloning."
}

if (-not (Test-Path -Path "lct-client")) {
    git clone https://gitflic.ru/project/lct-prefinal/lct-client.git
    Set-Location lct-client
    uv sync
    Set-Location ..
} else {
    Write-Host "Directory lct-client already exists. Skipping cloning."
}

if (-not (Test-Path -Path "lct-ats")) {
    git clone https://gitflic.ru/project/lct-prefinal/lct-ats.git
    Set-Location lct-ats
    uv sync
    Set-Location ..
} else {
    Write-Host "Directory lct-ats already exists. Skipping cloning."
}

Write-Host "Dependencies installation completed."
