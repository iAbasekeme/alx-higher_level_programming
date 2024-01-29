#!/bin/bash
# A shell script that transfers data using curl
response=$(curl -s -X POST -d $2 $1)
echo "$response"
