#!/usr/bin/python3
"""a script that sends a POST request to the passed URL \
        with email as a parameter
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    # Encode the data for a POST request
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')  # Data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(f"Your email is: {result.decode('utf-8')}")
