#!/usr/bin/python3
"""A script that sends a request and displays the X-Request-Id
"""
import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get('X-Request-Id'))
