#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
echo "$(curl -s -X POST -d "$2" "$1")"