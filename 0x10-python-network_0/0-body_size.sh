#!/bin/bash
# This script 
if [ $# -eq 0 ];
then
    exit 1
fi
curl -s "${1}" | wc -c