#!/bin/bash
# A shell script that transfers data using curl
curl -s -o /dev/null -w "%{http_code}" "$1"
