#!/bin/bash

# Path to the timestamp file
TIMESTAMP_FILE="/home/risriddle/Workstation/Projects/Python/setWallpaper/last_run_timestamp.txt"

# Check if the script has already run today
if [ -f "$TIMESTAMP_FILE" ]; then
    LAST_RUN=$(cat "$TIMESTAMP_FILE")
    CURRENT_DATE=$(date +%Y-%m-%d)

    if [ "$LAST_RUN" == "$CURRENT_DATE" ]; then
        echo "Script has already run today. Exiting."
        exit 0
    fi
    
    # Delete the previous day's timestamp file
    rm "$TIMESTAMP_FILE"
fi

# Run the script
/home/risriddle/Workstation/Projects/Python/setWallpaper/set_wallpaper_on_login.sh

# Update the timestamp
date +%Y-%m-%d > "$TIMESTAMP_FILE"
