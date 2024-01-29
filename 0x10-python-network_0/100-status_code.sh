#!/bin/bash
# A shell script that transfers data using curl
echo "$(curl -s -X POST -d "$2" "$1")"
