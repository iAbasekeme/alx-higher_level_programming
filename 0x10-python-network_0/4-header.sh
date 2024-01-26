#!/bin/bash
# A script that takes in a url as an argument and sends a Get req
curl -s -H "X-School-User-Id:98" "$1"
