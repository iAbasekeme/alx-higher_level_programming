#!/usr/bin/python3
"""A script that sends a POST request using requests
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = argv[2]

    r = requests.post(url, data)
    print(r.text)
