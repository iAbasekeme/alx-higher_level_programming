#!/usr/bin/python3
"""A script that handles httpError
"""

from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        req = urllib.request.Request(url)
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.URLError as e:
        print(f"Error code: {e.code}")
