#!/bin/bash
# A Bash script that takes in a URL
curl -sI "$1" | grep Allow | cut -d ' ' -f2-