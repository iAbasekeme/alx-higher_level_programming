#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
echo "$(curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1")"
