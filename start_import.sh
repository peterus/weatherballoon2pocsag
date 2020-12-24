#!/bin/bash

SCREEN_NAME="import_aprs"

# list screens
screen -ls
# kill open
screen -X -S $SCREEN_NAME quit
# start the process
screen -S $SCREEN_NAME -d -m ./import.py

