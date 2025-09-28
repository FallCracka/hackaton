#!/bin/bash

if ! command -v git &> /dev/null
then
    echo "Git not found. Installing..."
    sudo apt-get update
    sudo apt-get install -y git
else
    echo "Git is already installed."
fi

if ! command -v uv &> /dev/null
then
    echo "uv not found. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc
else
    echo "uv is already installed."
fi

echo "Cloning and setting up repositories..."

if [ ! -d "lct-prefinal" ]; then
    git clone https://gitflic.ru/project/lct-prefinal/lct-prefinal.git
    cd lct-prefinal || exit
    sudo chmod +x scripts/start_linux.sh
    cd ..
else
    echo "Directory lct-prefinal already exists. Skipping cloning."
fi

if [ ! -d "lct-client" ]; then
    git clone https://gitflic.ru/project/lct-prefinal/lct-client.git
    cd lct-client || exit
    uv sync
    cd ..
else
    echo "Directory lct-client already exists. Skipping cloning."
fi

if [ ! -d "lct-ats" ]; then
    git clone https://gitflic.ru/project/lct-prefinal/lct-ats.git
    cd lct-ats || exit
    uv sync
    cd ..
else
    echo "Directory lct-ats already exists. Skipping cloning."
fi


echo "Dependencies installation completed."
echo "----------------------------------------------------------------"
echo "IMPORTANT: Restart your terminal or run the command:"
echo "source ~/.bashrc (or ~/.zshrc if you're using zsh)"
echo "to make the 'uv' command available."
echo "----------------------------------------------------------------"
