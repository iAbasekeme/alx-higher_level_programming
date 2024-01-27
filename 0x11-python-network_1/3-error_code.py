#!/usr/bin/python3
"""A script that handles httpError
"""

from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.URLError as e:
        print(f"Error code: {e}")
