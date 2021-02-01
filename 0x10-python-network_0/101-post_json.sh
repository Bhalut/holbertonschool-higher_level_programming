#!/bin/bash
# Bash script that sends a JSON POST request
curl -sH "Content-Type: application/json" --data @"$2" "$1"
