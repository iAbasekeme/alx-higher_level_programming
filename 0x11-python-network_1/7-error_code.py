#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        r = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response is \
                not None and e.response.status_code >= 400:
            print(f"Error code: {e.response.status_code}")
        else:
            print(f"An error occurred: {e}")
