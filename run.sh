#!/bin/bash

set -x # DEBUG

# Prompt for password
PASSWORD=$(osascript -e 'Tell application "System Events" to display dialog "Enter you password:" default answer "" with hidden answer' -e 'text returned of result')

# Check password
if [ -z "$PASSWORD" ]; then
    echo "No password filled."
    exit 1
fi

# change path
cd Documents/sharingan/

# activate virtual env
source venv/bin/activate

# run script with sudo
echo $PASSWORD | sudo -S python3 main.py
