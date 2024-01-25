#!/bin/bash
# This script takes in a URL, ans send a request
curl -s "${1}" | wc -c