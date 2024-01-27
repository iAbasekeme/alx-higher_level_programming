#!/usr/bin/python3
"""A script that sends a POST request using requests
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    print(requests.post(url, data).text)
