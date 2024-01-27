#!/usr/bin/python3
"""A script that sends a request and displays the X-Request-Id
"""
import request
from sys import argv

if __name__ == "__main__":
    r = request.get(argv[1])
    print(r.headers['X-Request-Id'])
