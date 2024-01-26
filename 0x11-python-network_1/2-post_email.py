#!/usr/bin/python3
"""a script that sends a POST request to the passed URL \
        with email as a parameter
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    # Encode the data for a POST request
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')  # Data should be bytes
    with urllib.request.urlopen(url, data) as response:
        result = response.read()
        print(f"Your email is: {format(result.decode('utf-8'))}")
