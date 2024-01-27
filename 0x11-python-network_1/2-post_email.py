#!/usr/bin/python3
"""a script that sends a POST request to the passed URL \
        with email as a parameter
"""
from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    if len(argv) > 2:
        # Encode the data for a POST request
        data = parse.urlencode({'email': email}).encode('utf-8')
        req = request.Request(url, {'email': email})
        with request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf-8'))
