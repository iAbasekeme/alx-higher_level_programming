#!/bin/bash
# A Bash script that takes in a URL
curl -s -I -X OPTIONS "$1" | awk '/Allow/ {print substr(, index(,))}'