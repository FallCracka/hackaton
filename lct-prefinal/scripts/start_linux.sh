#!/bin/bash

TWIN_DIR="../LCT_linux"

if [ ! -d "$TWIN_DIR" ]; then
  echo "Error: Digital Twin directory '$TWIN_DIR' not found."
  echo "Please download and extract the Digital Twin archive for Linux."
  echo "The 'LCT_linux' folder should be located next to the project directory."
  exit 1
fi

(cd "$TWIN_DIR" && chmod +x twin.x86_64 && ./twin.x86_64 &)
echo "Digital Twin launched in background from '$TWIN_DIR'."

gnome-terminal --title="ATS" -- bash -c "cd lct-ats; uv run launcher.py --twin; exec bash"

gnome-terminal --title="Client" -- bash -c "cd lct-client; uv run jupyter notebook; exec bash"

echo "ATS and Client launched."
