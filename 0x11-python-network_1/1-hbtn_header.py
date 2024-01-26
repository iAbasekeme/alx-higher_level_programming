#!/usr/bin/python3
"""A script that makes a request to a \
    url and dispalys the value of \
    the X-Request-Id variable
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)
