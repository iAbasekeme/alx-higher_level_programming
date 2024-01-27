#!/usr/bin/python3
"""a script that sends a POST request to the passed URL \
        with email as a parameter
"""
from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    if len(argv) > 2:
        url = argv[1]
        email = argv[2]
        value = {'email': email}

        # Encode the data for a POST request
        data = parse.urlencode(value).encode('ascii')
        req = request.Request(url, data)
        with request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf-8'))
