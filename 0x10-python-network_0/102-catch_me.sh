#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that
curl -sX PUT -H "Content-Type: text/plain" "0.0.0.0:5000/catch_me"