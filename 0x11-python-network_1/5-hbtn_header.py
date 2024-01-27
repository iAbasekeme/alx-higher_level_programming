#!/usr/bin/python3
"""A script that sends a request and displays the X-Request-Id
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = request.get(argv[1])
    if headers['X-Request-Id']:
        print(r.headers['X-Request-Id'])